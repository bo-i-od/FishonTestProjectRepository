"""
录制回放 GUI 工具

精简版（不含 Auto_test 中的安全区相关功能）。

使用方式:
    python -m gui.recorder_gui
    python gui/recorder_gui.py
"""
import sys
import os

if sys.platform == "darwin":
    os.environ.setdefault("NSApplicationSupportsSecureRestorableState", "YES")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
import json
import logging
import queue
import socket
import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, ttk

import websockets

from common.base_page import BasePage
from common.recorder.recorder_server import RecorderServer
from common.script_runner import ScriptRunner
from common.ws_server import RPCServer
from configs.path_config import DEFAULT_CAMERA_CONFIG


_GUI_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
_RECORDING_DIR = _GUI_DIR / "recordingScripts"
_CONFIG_PATH = _GUI_DIR / "recorder_config.json"


class _PaletteColors:
    """界面调色板（macOS / Windows 通用偏中性蓝白色调）。"""
    bg = "#f3f4f6"
    card = "#ffffff"
    border = "#e5e7eb"
    text = "#111827"
    sub = "#6b7280"
    primary = "#3b82f6"
    primary_h = "#60a5fa"
    green = "#22c55e"
    green_h = "#4ade80"
    amber = "#f59e0b"
    amber_h = "#fbbf24"
    red = "#ef4444"
    red_h = "#f87171"
    gray_btn = "#6b7280"
    gray_h = "#9ca3af"
    log_bg = "#0f172a"
    log_fg = "#e2e8f0"
    log_ok = "#34d399"
    log_warn = "#fbbf24"
    log_err = "#f87171"


# ============================================================================
#  GUI 日志 Handler
# ============================================================================

class _GuiLogHandler(logging.Handler):
    """把 logging 输出转送到 GUI 日志面板。"""

    def __init__(self, sink):
        super().__init__()
        self.sink = sink
        self.setLevel(logging.INFO)

    def emit(self, record: logging.LogRecord):
        try:
            msg = self.format(record)
        except Exception:
            return
        tag = ""
        if record.levelno >= logging.ERROR:
            tag = "err"
        elif record.levelno >= logging.WARNING:
            tag = "warn"
        elif record.levelno >= logging.INFO:
            tag = ""
        try:
            self.sink(msg, tag)
        except Exception:
            pass


# ============================================================================
#  Tab 主类
# ============================================================================

class RecorderTab:
    """录制回放页签（独立运行）。"""

    _WAIT_MODE_LABELS = ("显性等待", "强制等待")
    _WAIT_MODE_MAP = {
        "显性等待": "explicit",
        "强制等待": "forced",
    }
    _DEVICE_TYPES = ("pc", "android", "harmony", "ios")

    def __init__(self, root: tk.Tk):
        self.root = root
        self._palette = _PaletteColors()

        self._loop = asyncio.new_event_loop()
        threading.Thread(target=self._loop.run_forever, daemon=True).start()
        self._ui_queue: queue.Queue = queue.Queue()

        self._rpc_server: RPCServer | None = None
        self._ws_server = None
        self._connected = False
        self._server_running = False
        self._current_port = 0

        self._recorder: RecorderServer | None = None
        self._recording = False
        self._playing = False
        self._playback_future = None  # concurrent.futures.Future
        self._hide_count_timer = None
        self._gui_log_handler: logging.Handler | None = None

        self._config = self._load_config()

        self._build_ui()
        self._install_log_handler()
        self._refresh_ui()
        self._poll_ui_queue()
        self._poll_state()

    # ------------------------------------------------------------------
    #  配置持久化
    # ------------------------------------------------------------------

    def _load_config(self) -> dict:
        try:
            with open(_CONFIG_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_config(self):
        try:
            with open(_CONFIG_PATH, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    # ------------------------------------------------------------------
    #  UI 构造
    # ------------------------------------------------------------------

    def _build_ui(self):
        c = self._palette
        self.root.configure(bg=c.bg)

        self._build_connection_bar(self.root)

        outer = tk.Frame(self.root, bg=c.bg)
        outer.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self._build_card_recording(outer)
        self._build_card_playback(outer)
        self._build_card_log(outer)

    # -------- 连接栏 --------

    def _build_connection_bar(self, parent):
        c = self._palette
        self._conn_bar = bar = tk.Frame(parent, bg=c.red, height=38)
        bar.pack(fill=tk.X, padx=10, pady=(8, 0))
        bar.pack_propagate(False)

        self._conn_status_var = tk.StringVar(value="  ● 服务未启动")
        self._conn_status_lbl = tk.Label(
            bar, textvariable=self._conn_status_var,
            bg=c.red, fg="white", font=("Microsoft YaHei", 10, "bold"),
        )
        self._conn_status_lbl.pack(side=tk.LEFT, padx=8)

        self._conn_btn = tk.Button(
            bar, text="▶ 启动服务", command=self._on_toggle_conn,
            bg=c.red, fg="white", font=("Microsoft YaHei", 9, "bold"),
            relief=tk.FLAT, bd=0, padx=14, pady=2, activebackground=c.red_h,
            activeforeground="white",
        )
        self._conn_btn.pack(side=tk.RIGHT, padx=(0, 8), pady=4)

        self._conn_port_var = tk.StringVar(value=str(self._config.get("port", 5101)))
        self._conn_port_entry = tk.Entry(
            bar, textvariable=self._conn_port_var, width=6,
            font=("Consolas", 10), relief=tk.FLAT, bd=0,
            bg="#fef2f2", fg=c.text,
        )
        self._conn_port_entry.pack(side=tk.RIGHT, ipady=2, padx=(0, 8), pady=5)

        self._conn_port_label = tk.Label(bar, text="端口:", bg=c.red, fg="#fecaca",
                                         font=("Microsoft YaHei", 9))
        self._conn_port_label.pack(side=tk.RIGHT, padx=(0, 2))

        self._conn_ip_var = tk.StringVar(value=self._detect_local_ip())
        self._conn_ip_lbl = tk.Label(bar, textvariable=self._conn_ip_var,
                                     bg=c.red, fg="#fecaca",
                                     font=("Consolas", 10))
        self._conn_ip_lbl.pack(side=tk.RIGHT, padx=(0, 10))

        self._conn_ip_label = tk.Label(bar, text="IP:", bg=c.red, fg="#fecaca",
                                       font=("Microsoft YaHei", 9))
        self._conn_ip_label.pack(side=tk.RIGHT, padx=(0, 2))

    @staticmethod
    def _detect_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "?"

    # -------- 录制卡 --------

    def _build_card_recording(self, parent):
        c = self._palette
        card, content = self._make_card(parent, "录制")

        device_row = tk.Frame(content, bg=c.card)
        device_row.pack(fill=tk.X, pady=(0, 6))

        tk.Label(device_row, text="设备类型:", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._device_type_var = tk.StringVar(
            value=self._config.get("device_type", "pc"))
        device_combo = ttk.Combobox(device_row, textvariable=self._device_type_var,
                                    values=list(self._DEVICE_TYPES),
                                    width=10, state="readonly")
        device_combo.pack(side=tk.LEFT, padx=(6, 12))
        device_combo.bind("<<ComboboxSelected>>", lambda e: self._on_device_type_changed())

        tk.Label(device_row, text="设备号:", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._device_id_var = tk.StringVar(
            value=self._config.get("device_id", ""))
        self._device_id_entry = tk.Entry(device_row, textvariable=self._device_id_var,
                                         width=22, font=("Consolas", 9))
        self._device_id_entry.pack(side=tk.LEFT, padx=(6, 0), fill=tk.X, expand=True)
        self._device_id_var.trace_add("write", lambda *_: self._on_device_id_changed())

        ios_row = tk.Frame(content, bg=c.card)
        ios_row.pack(fill=tk.X, pady=(0, 6))
        tk.Label(ios_row, text="iOS WDA 项目:", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._ios_wda_project_var = tk.StringVar(
            value=self._config.get("ios_wda_project", ""))
        tk.Entry(ios_row, textvariable=self._ios_wda_project_var,
                 width=42, font=("Consolas", 9)).pack(side=tk.LEFT, padx=(6, 0),
                                                       fill=tk.X, expand=True)
        self._ios_wda_project_var.trace_add(
            "write", lambda *_: self._on_ios_wda_project_changed())

        btn_row = tk.Frame(content, bg=c.card)
        btn_row.pack(fill=tk.X, pady=(4, 0))

        self._rec_btn = tk.Button(btn_row, text="● 开始录制",
                                   command=self._on_toggle_recording,
                                   bg=c.green, fg="white", relief=tk.FLAT, bd=0,
                                   font=("Microsoft YaHei", 9, "bold"),
                                   activebackground=c.green_h,
                                   activeforeground="white",
                                   padx=14, pady=4)
        self._rec_btn.pack(side=tk.LEFT)

        self._undo_btn = tk.Button(btn_row, text="↩ 撤销上一步",
                                    command=self._on_undo_event,
                                    bg=c.gray_btn, fg="white", relief=tk.FLAT, bd=0,
                                    font=("Microsoft YaHei", 9),
                                    activebackground=c.gray_h,
                                    activeforeground="white",
                                    padx=12, pady=4)
        self._undo_btn.pack(side=tk.LEFT, padx=(8, 0))

        self._event_count_var = tk.StringVar(value="")
        tk.Label(btn_row, textvariable=self._event_count_var,
                 bg=c.card, fg=c.sub,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT, padx=(12, 0))

    # -------- 回放卡 --------

    def _build_card_playback(self, parent):
        c = self._palette
        card, content = self._make_card(parent, "回放")

        path_row = tk.Frame(content, bg=c.card)
        path_row.pack(fill=tk.X, pady=(0, 6))
        tk.Label(path_row, text="脚本:", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._file_var = tk.StringVar(value=self._config.get("playback_path", ""))
        tk.Entry(path_row, textvariable=self._file_var,
                 font=("Consolas", 9)).pack(side=tk.LEFT, padx=(6, 6),
                                             fill=tk.X, expand=True)
        tk.Button(path_row, text="选择…", command=self._on_pick_file,
                  bg=c.gray_btn, fg="white", relief=tk.FLAT, bd=0,
                  font=("Microsoft YaHei", 9), padx=10, pady=2,
                  activebackground=c.gray_h,
                  activeforeground="white").pack(side=tk.LEFT)
        self._file_var.trace_add("write", lambda *_: self._on_playback_path_changed())

        opts = tk.Frame(content, bg=c.card)
        opts.pack(fill=tk.X, pady=(0, 6))

        tk.Label(opts, text="操作延时(s):", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._delay_var = tk.StringVar(
            value=str(self._config.get("playback_delay", 1.0)))
        tk.Entry(opts, textvariable=self._delay_var, width=5,
                 font=("Consolas", 9)).pack(side=tk.LEFT, padx=(6, 12))
        self._delay_var.trace_add("write", lambda *_: self._on_delay_changed())

        tk.Label(opts, text="循环次数:", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._loop_var = tk.StringVar(
            value=str(self._config.get("loop_count", 1)))
        tk.Entry(opts, textvariable=self._loop_var, width=5,
                 font=("Consolas", 9)).pack(side=tk.LEFT, padx=(6, 12))
        self._loop_var.trace_add("write", lambda *_: self._on_loop_changed())

        tk.Label(opts, text="等待模式:", bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT)
        self._wait_mode_var = tk.StringVar(
            value=self._config.get("wait_mode_label", "显性等待"))
        wait_combo = ttk.Combobox(opts, textvariable=self._wait_mode_var,
                                  values=list(self._WAIT_MODE_LABELS),
                                  width=10, state="readonly")
        wait_combo.pack(side=tk.LEFT, padx=(6, 0))
        wait_combo.bind("<<ComboboxSelected>>",
                        lambda e: self._on_wait_mode_changed())

        btn_row = tk.Frame(content, bg=c.card)
        btn_row.pack(fill=tk.X, pady=(4, 0))

        self._play_btn = tk.Button(btn_row, text="▶ 开始回放",
                                    command=self._on_toggle_playback,
                                    bg=c.primary, fg="white", relief=tk.FLAT, bd=0,
                                    font=("Microsoft YaHei", 9, "bold"),
                                    activebackground=c.primary_h,
                                    activeforeground="white",
                                    padx=14, pady=4)
        self._play_btn.pack(side=tk.LEFT)

        self._play_status_var = tk.StringVar(value="")
        tk.Label(btn_row, textvariable=self._play_status_var,
                 bg=c.card, fg=c.sub,
                 font=("Microsoft YaHei", 9)).pack(side=tk.LEFT, padx=(12, 0))

    # -------- 日志卡 --------

    def _build_card_log(self, parent):
        c = self._palette
        card, content = self._make_card(parent, "日志", expand=True)

        log_frame = tk.Frame(content, bg=c.card)
        log_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self._log_text = tk.Text(log_frame,
                                  bg=c.log_bg, fg=c.log_fg,
                                  insertbackground=c.log_fg,
                                  font=("Consolas", 9),
                                  relief=tk.FLAT, bd=0,
                                  wrap=tk.WORD,
                                  yscrollcommand=scrollbar.set)
        self._log_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        scrollbar.config(command=self._log_text.yview)

        self._log_text.tag_config("ok", foreground=c.log_ok)
        self._log_text.tag_config("warn", foreground=c.log_warn)
        self._log_text.tag_config("err", foreground=c.log_err)
        self._log_text.config(state=tk.DISABLED)

        bottom = tk.Frame(content, bg=c.card)
        bottom.pack(fill=tk.X, pady=(6, 0))
        tk.Button(bottom, text="清空日志", command=self._clear_log,
                  bg=c.gray_btn, fg="white", relief=tk.FLAT, bd=0,
                  font=("Microsoft YaHei", 9), padx=10, pady=2,
                  activebackground=c.gray_h,
                  activeforeground="white").pack(side=tk.RIGHT)

    def _make_card(self, parent, title: str, expand: bool = False):
        c = self._palette
        outer = tk.Frame(parent, bg=c.card, highlightbackground=c.border,
                         highlightthickness=1)
        pack_kw = dict(fill=tk.BOTH, expand=True, pady=(0, 10)) if expand \
            else dict(fill=tk.X, pady=(0, 10))
        outer.pack(**pack_kw)

        header = tk.Frame(outer, bg=c.card)
        header.pack(fill=tk.X, padx=14, pady=(10, 6))
        tk.Label(header, text=title, bg=c.card, fg=c.text,
                 font=("Microsoft YaHei", 11, "bold")).pack(side=tk.LEFT)

        tk.Frame(outer, bg=c.border, height=1).pack(fill=tk.X, padx=14)

        content = tk.Frame(outer, bg=c.card, padx=14, pady=8)
        content.pack(**(dict(fill=tk.BOTH, expand=True) if expand
                        else dict(fill=tk.X)))
        return outer, content

    # ------------------------------------------------------------------
    #  日志
    # ------------------------------------------------------------------

    def _install_log_handler(self):
        if self._gui_log_handler is not None:
            return
        h = _GuiLogHandler(lambda m, tag="": self._ui(lambda: self._log(m, tag)))
        h.setFormatter(logging.Formatter('[%(name)s] %(message)s'))
        logging.getLogger().addHandler(h)
        self._gui_log_handler = h

    def _log(self, msg: str, tag: str = ""):
        self._log_text.config(state=tk.NORMAL)
        ts = datetime.now().strftime("%H:%M:%S")
        line = f"[{ts}] {msg}\n"
        if tag:
            self._log_text.insert(tk.END, line, tag)
        else:
            self._log_text.insert(tk.END, line)
        self._log_text.see(tk.END)
        self._log_text.config(state=tk.DISABLED)

    def _clear_log(self):
        self._log_text.config(state=tk.NORMAL)
        self._log_text.delete("1.0", tk.END)
        self._log_text.config(state=tk.DISABLED)

    # ------------------------------------------------------------------
    #  线程调度
    # ------------------------------------------------------------------

    def _ui(self, fn):
        """从异步线程把 UI 操作调度回主线程。"""
        self._ui_queue.put(fn)

    def _poll_ui_queue(self):
        try:
            while True:
                fn = self._ui_queue.get_nowait()
                try:
                    fn()
                except Exception as e:
                    print(f"[ui] {e}")
        except queue.Empty:
            pass
        self.root.after(50, self._poll_ui_queue)

    def _schedule(self, coro):
        return asyncio.run_coroutine_threadsafe(coro, self._loop)

    def _poll_state(self):
        """周期性刷新 UI 状态（含录制事件计数）。"""
        if self._recording and self._rpc_server is not None:
            try:
                evts = self._rpc_server.get_recording_events()
                self._event_count_var.set(f"已捕获 {len(evts)} 个事件")
            except Exception:
                pass
        self.root.after(500, self._poll_state)

    def _schedule_hide_event_count(self):
        if self._hide_count_timer:
            self.root.after_cancel(self._hide_count_timer)
        self._hide_count_timer = self.root.after(
            5000, lambda: self._event_count_var.set(""))

    # ------------------------------------------------------------------
    #  UI 状态刷新
    # ------------------------------------------------------------------

    def _refresh_ui(self):
        self._refresh_connection_bar()
        self._refresh_buttons()

    def _refresh_connection_bar(self):
        c = self._palette
        srv_on = self._server_running
        conn = self._connected

        if not srv_on:
            bar_bg = c.red
            self._conn_status_var.set("  ● 服务未启动")
        elif not conn:
            bar_bg = c.amber
            self._conn_status_var.set("  ● 等待客户端连接…")
        else:
            bar_bg = c.green
            port_txt = f" (端口 {self._current_port})" if self._current_port else ""
            self._conn_status_var.set(f"  ● 已连接{port_txt}")

        for w in (self._conn_bar, self._conn_status_lbl,
                  self._conn_port_label, self._conn_ip_label, self._conn_ip_lbl):
            w.config(bg=bar_bg)

        port_label_fg = {c.red: "#fecaca", c.amber: "#fef3c7",
                          c.green: "#bbf7d0"}.get(bar_bg, "#fecaca")
        port_entry_bg = {c.red: "#fef2f2", c.amber: "#fffbeb",
                          c.green: "#f0fdf4"}.get(bar_bg, "#fef2f2")
        self._conn_port_label.config(fg=port_label_fg)
        self._conn_port_entry.config(bg=port_entry_bg)
        self._conn_ip_label.config(fg=port_label_fg)
        self._conn_ip_lbl.config(fg=port_label_fg)

        btn_colors = {
            c.red: (c.red, c.red_h),
            c.amber: (c.amber, c.amber_h),
            c.green: (c.green, c.green_h),
        }
        btn_bg, btn_hover = btn_colors.get(bar_bg, (c.red, c.red_h))
        self._conn_btn.config(
            text="■ 停止服务" if srv_on else "▶ 启动服务",
            bg=btn_bg, activebackground=btn_hover,
        )

    def _refresh_buttons(self):
        c = self._palette
        connected = self._connected and self._rpc_server is not None
        device_type = self._device_type_var.get()

        rec_enabled = connected and not self._playing and device_type == "pc"
        self._rec_btn.config(
            text="■ 停止录制" if self._recording else "● 开始录制",
            bg=c.red if self._recording else c.green,
            activebackground=c.red_h if self._recording else c.green_h,
            state=tk.NORMAL if rec_enabled or self._recording else tk.DISABLED,
        )
        self._undo_btn.config(
            state=tk.NORMAL if self._recording else tk.DISABLED,
        )

        play_enabled = connected and not self._recording
        if self._playing:
            self._play_btn.config(text="■ 终止回放",
                                   bg=c.red, activebackground=c.red_h,
                                   state=tk.NORMAL)
        else:
            self._play_btn.config(text="▶ 开始回放",
                                   bg=c.primary, activebackground=c.primary_h,
                                   state=tk.NORMAL if play_enabled else tk.DISABLED)

    # ------------------------------------------------------------------
    #  连接管理
    # ------------------------------------------------------------------

    def _on_toggle_conn(self):
        if self._server_running:
            self._log("正在停止服务…")
            self._schedule(self._conn_stop_server())
            return

        try:
            port = int(self._conn_port_var.get())
        except ValueError:
            self._log("端口号无效，请输入数字", "err")
            return
        self._config["port"] = port
        self._save_config()
        self._log(f"正在启动服务，端口 {port}…")
        self._schedule(self._conn_start_server(port))

    async def _conn_start_server(self, port: int):
        self._server_running = True
        self._current_port = port
        self._ui(self._refresh_ui)
        try:
            self._ws_server = await websockets.serve(
                self._conn_ws_handler, "0.0.0.0", port,
            )
            self._ui(lambda: self._log(
                f"服务已启动 ws://0.0.0.0:{port}，等待客户端连接…", "ok"))
            self._ui(self._refresh_ui)
        except Exception as e:
            self._server_running = False
            self._current_port = 0
            err_msg = str(e)
            self._ui(lambda: self._log(f"启动服务失败: {err_msg}", "err"))
            self._ui(self._refresh_ui)

    async def _conn_ws_handler(self, ws):
        if self._rpc_server is not None:
            await ws.close()
            return
        self._rpc_server = RPCServer(ws)
        await self._rpc_server.start()
        self._rpc_server.handle_msg_start()
        self._connected = True
        self._ui(lambda: self._log("客户端已连接", "ok"))
        self._ui(self._refresh_ui)

        try:
            await self._rpc_server.listener_task
        except asyncio.CancelledError:
            pass
        except Exception as e:
            err_msg = str(e)
            self._ui(lambda: self._log(f"连接异常断开: {err_msg}", "err"))
        finally:
            close_code = getattr(ws, 'close_code', None)
            close_reason = getattr(ws, 'close_reason', None) or ''
            self._connected = False
            self._rpc_server = None
            detail = f" (code={close_code}, reason={close_reason})" if close_code else ""
            self._ui(lambda: self._log(f"客户端已断开{detail}", "warn"))
            self._ui(self._refresh_ui)

    async def _conn_stop_server(self):
        if self._recording:
            try:
                await self._async_stop_recording()
            except Exception:
                pass
        if self._playing and self._playback_future is not None:
            self._playback_future.cancel()

        if self._rpc_server is not None:
            try:
                await self._rpc_server.close()
            except Exception:
                pass
            self._rpc_server = None
        if self._ws_server is not None:
            self._ws_server.close()
            await self._ws_server.wait_closed()
            self._ws_server = None
        self._server_running = False
        self._current_port = 0
        self._connected = False
        self._ui(lambda: self._log("服务已停止"))
        self._ui(self._refresh_ui)

    # ------------------------------------------------------------------
    #  录制
    # ------------------------------------------------------------------

    def _on_device_type_changed(self):
        self._config["device_type"] = self._device_type_var.get()
        self._save_config()
        self._refresh_buttons()

    def _on_device_id_changed(self):
        self._config["device_id"] = self._device_id_var.get()
        self._save_config()

    def _on_ios_wda_project_changed(self):
        self._config["ios_wda_project"] = self._ios_wda_project_var.get()
        self._save_config()

    def _on_toggle_recording(self):
        if not self._connected or self._rpc_server is None:
            self._log("尚未连接客户端，无法录制", "warn")
            return

        if self._device_type_var.get() != "pc":
            self._log("仅支持 PC 模式录制（请先切换到 pc 设备类型）", "warn")
            return

        if self._recording:
            self._log("正在停止录制…")
            self._schedule(self._async_stop_recording())
            return

        camera_config_list = list(DEFAULT_CAMERA_CONFIG)
        if not camera_config_list:
            self._log("DEFAULT_CAMERA_CONFIG 为空，请先在 configs/path_config.py 配置相机", "err")
            return

        self._recording = True
        self._refresh_buttons()
        self._log("正在启动录制…")
        self._schedule(self._async_start_recording(camera_config_list))

    def _on_undo_event(self):
        if not self._recording or self._rpc_server is None:
            return
        ok = self._rpc_server.recording_undo()
        if ok:
            self._log("已撤销上一步事件", "ok")
        else:
            self._log("没有可撤销的事件", "warn")

    def _read_long_press_threshold(self) -> float | None:
        """读取长按时间阈值（秒）。返回 None 表示让 RecorderServer 走默认值。"""
        raw = self._config.get("recorder_long_press_threshold_s")
        if raw is None:
            return None
        try:
            v = float(raw)
            return v if v >= 0 else None
        except (TypeError, ValueError):
            return None

    async def _async_start_recording(self, camera_config_list: list[dict]):
        if not self._rpc_server:
            self._recording = False
            self._ui(self._refresh_ui)
            return
        try:
            recorder = RecorderServer(self._rpc_server,
                                      output_dir=str(_RECORDING_DIR),
                                      long_press_threshold_s=self._read_long_press_threshold())
            ok = await recorder.start_recording(camera_config_list=camera_config_list)
            if not ok:
                self._recording = False
                self._ui(lambda: self._log("启动录制失败（Unity 端拒绝）", "err"))
                self._ui(self._refresh_ui)
                return
            self._recorder = recorder
            self._ui(lambda: self._log("录制中，请在游戏中操作…", "ok"))
            self._ui(self._refresh_ui)
        except Exception as e:
            self._recording = False
            self._recorder = None
            err_msg = str(e)
            self._ui(lambda: self._log(f"启动录制异常: {err_msg}", "err"))
            self._ui(self._refresh_ui)

    async def _async_stop_recording(self):
        recorder = self._recorder
        if not recorder:
            self._recording = False
            self._ui(self._refresh_ui)
            return
        try:
            filepath = await asyncio.wait_for(recorder.stop_recording(), timeout=10.0)
            if filepath:
                self._ui(lambda: self._log(f"录制已保存: {filepath}", "ok"))
                self._ui(lambda: self._file_var.set(filepath))
            else:
                self._ui(lambda: self._log("录制已停止（无操作事件）", "warn"))
        except asyncio.TimeoutError:
            self._ui(lambda: self._log("停止录制超时（10s），已强制停止", "warn"))
            try:
                self._rpc_server.recording_stop()
            except Exception:
                pass
        except Exception as e:
            err_msg = str(e)
            self._ui(lambda: self._log(f"停止录制异常: {err_msg}", "err"))
        finally:
            self._recording = False
            self._recorder = None
            self._ui(self._refresh_ui)
            self._ui(self._schedule_hide_event_count)

    # ------------------------------------------------------------------
    #  回放
    # ------------------------------------------------------------------

    def _on_pick_file(self):
        initial = self._file_var.get().strip()
        initial_dir = str(_RECORDING_DIR)
        if initial and os.path.dirname(initial):
            initial_dir = os.path.dirname(initial)
        path = filedialog.askopenfilename(
            title="选择回放脚本",
            initialdir=initial_dir,
            filetypes=[("Python", "*.py"), ("All", "*.*")],
        )
        if path:
            self._file_var.set(path)

    def _on_playback_path_changed(self):
        self._config["playback_path"] = self._file_var.get()
        self._save_config()

    def _on_delay_changed(self):
        try:
            self._config["playback_delay"] = float(self._delay_var.get())
        except ValueError:
            return
        self._save_config()

    def _on_loop_changed(self):
        try:
            self._config["loop_count"] = int(self._loop_var.get())
        except ValueError:
            return
        self._save_config()

    def _on_wait_mode_changed(self):
        self._config["wait_mode_label"] = self._wait_mode_var.get()
        self._save_config()

    def _on_toggle_playback(self):
        if self._playing:
            if self._playback_future is not None:
                self._playback_future.cancel()
            self._log("正在终止回放…")
            return

        if not self._connected or self._rpc_server is None:
            self._log("尚未连接客户端，无法回放", "warn")
            return

        filepath = self._file_var.get().strip()
        if not filepath:
            self._log("请先选择回放脚本", "warn")
            return
        if not os.path.exists(filepath):
            self._log(f"脚本不存在: {filepath}", "err")
            return

        try:
            loop_count = max(1, int(self._loop_var.get()))
        except ValueError:
            loop_count = 1
        try:
            playback_delay = max(0.0, float(self._delay_var.get()))
        except ValueError:
            playback_delay = 1.0

        self._playing = True
        self._refresh_buttons()
        self._playback_future = self._schedule(
            self._async_start_playback(filepath, loop_count, playback_delay))

    async def _async_start_playback(self, filepath: str, loop_count: int = 1,
                                     playback_delay: float = 1.0):
        if not self._rpc_server:
            self._playing = False
            self._ui(self._refresh_ui)
            return

        try:
            self._ui(lambda: self._log("正在初始化回放…"))
            device_type = self._device_type_var.get()
            device_id = self._device_id_var.get().strip() or None
            if device_type == "pc":
                device_id = None

            bp = BasePage(server=self._rpc_server,
                          device_type=device_type,
                          device_id=device_id,
                          is_record=False)
            if device_type == "ios":
                bp.ios_wda_project = self._ios_wda_project_var.get().strip() or None
            await bp.initialize()
            bp.playback_delay = playback_delay
            wait_mode = self._WAIT_MODE_MAP.get(
                self._wait_mode_var.get(), "explicit")
            setattr(bp, "playback_wait_mode", wait_mode)

            engine = ScriptRunner(bp, filepath)
            self._ui(lambda: self._log(
                f"加载脚本 '{engine.name}'，循环 {loop_count} 次", "ok"))

            for i in range(1, loop_count + 1):
                round_msg = f"({i}/{loop_count})" if loop_count > 1 else ""
                self._ui(lambda m=round_msg:
                         self._play_status_var.set(f"● 脚本运行中... {m}"))
                if loop_count > 1:
                    self._ui(lambda idx=i: self._log(
                        f"第 {idx}/{loop_count} 轮开始"))
                result = await engine.run()
                if not result.success:
                    self._ui(lambda msg=result.error_message:
                             self._log(f"回放失败: {msg}", "err"))
                    break
                if loop_count > 1:
                    self._ui(lambda idx=i: self._log(
                        f"第 {idx}/{loop_count} 轮完成", "ok"))
            self._ui(lambda: self._log(
                f"回放全部完成（共 {loop_count} 轮）", "ok"))
        except asyncio.CancelledError:
            self._ui(lambda: self._log("回放已终止", "warn"))
        except FileNotFoundError as e:
            err_msg = str(e)
            self._ui(lambda: self._log(f"文件未找到: {err_msg}", "err"))
        except Exception as e:
            err_msg = str(e)
            self._ui(lambda: self._log(f"回放异常: {err_msg}", "err"))
        finally:
            self._playing = False
            self._playback_future = None
            self._ui(lambda: self._play_status_var.set(""))
            self._ui(self._refresh_ui)

    # ------------------------------------------------------------------
    #  生命周期
    # ------------------------------------------------------------------

    def shutdown(self):
        if self._gui_log_handler is not None:
            logging.getLogger().removeHandler(self._gui_log_handler)
            self._gui_log_handler = None

    def _on_close(self):
        if self._server_running:
            future = self._schedule(self._conn_stop_server())
            future.add_done_callback(lambda _: self._ui(self._force_close))
            self.root.after(5000, self._force_close)
            return
        self._force_close()

    def _force_close(self):
        self.shutdown()
        try:
            self._loop.call_soon_threadsafe(self._loop.stop)
        except RuntimeError:
            pass
        try:
            self.root.destroy()
        except tk.TclError:
            pass

    def start(self):
        port = self._config.get("port", 5101)
        self._schedule(self._conn_start_server(port))

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self.start()
        self.root.mainloop()


# ============================================================================
#  入口
# ============================================================================

def main():
    root = tk.Tk()
    root.title("录制回放工具")
    root.geometry("760x720")
    root.minsize(620, 560)
    if sys.platform == "darwin":
        try:
            ttk.Style().theme_use("clam")
        except tk.TclError:
            pass

    tab = RecorderTab(root)
    root.protocol("WM_DELETE_WINDOW", tab._on_close)
    tab.start()
    root.mainloop()


if __name__ == "__main__":
    main()
