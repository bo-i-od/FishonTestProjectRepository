from common.log import get_logger
logger = get_logger("ios_driver")
import asyncio
import os
import queue
import socket
import subprocess
import threading
import time
from typing import Optional

import cv2
import numpy as np
import requests as _requests
import wda
from common.driver.base_driver import BaseDeviceDriver


class IOSDriver(BaseDeviceDriver):
    _xcodebuild_proc: Optional[subprocess.Popen] = None
    _iproxy_proc: Optional[subprocess.Popen] = None
    _iproxy_serial: Optional[str] = None
    _current_serial: Optional[str] = None
    _wda_url: Optional[str] = None

    def __init__(self, page):
        super().__init__(page)
        self.wda_client = None
        self._video_running = False
        self._video_thread = None
        self._video_writer = None
        self._video_output = None

    # ================================================================
    #  工具方法
    # ================================================================

    @staticmethod
    def _is_port_open(port: int, host: str = "127.0.0.1", timeout: float = 2.0) -> bool:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except (OSError, ConnectionRefusedError):
            return False

    @staticmethod
    def _free_port(port: int):
        """强制释放被占用的端口"""
        try:
            r = subprocess.run(["lsof", "-ti", f":{port}"], capture_output=True, text=True, timeout=5)
            for pid_str in r.stdout.strip().splitlines():
                pid = int(pid_str)
                if pid <= 0:
                    continue
                subprocess.run(["kill", "-9", str(pid)], capture_output=True, timeout=5)
                logger.info(f"已终止占用端口 {port} 的进程 (PID={pid})")
        except Exception as e:
            logger.debug(f"端口清理失败: {e}")

    @staticmethod
    def _is_wda_ready(port: int) -> bool:
        return IOSDriver._check_wda_url(f"http://localhost:{port}")

    @staticmethod
    def _check_wda_url(base_url: str) -> bool:
        try:
            resp = _requests.get(f"{base_url}/status", timeout=3)
            return resp.ok and resp.json().get("value", {}).get("ready", False)
        except Exception:
            return False

    @staticmethod
    def _verify_wda_connection(port: int) -> bool:
        """深度验证 WDA 连接（排除残留 iproxy 转发到已死 WDA 的情况）"""
        try:
            resp = _requests.get(f"http://localhost:{port}/wda/healthcheck", timeout=5)
            return resp.ok
        except Exception:
            return False

    @staticmethod
    def _resolve_xcode_project(path: str) -> str:
        """将用户选择的路径解析为实际的 .xcodeproj/.xcworkspace。
        支持直接传入 .xcodeproj、包含 .xcodeproj 的父目录两种情况。"""
        if path.endswith(('.xcodeproj', '.xcworkspace')):
            return path
        for name in os.listdir(path):
            if name.endswith('.xcodeproj'):
                resolved = os.path.join(path, name)
                logger.info(f"自动定位项目文件: {resolved}")
                return resolved
        raise RuntimeError(
            f"在 {path} 中未找到 .xcodeproj 文件。\n"
            "请选择包含 WebDriverAgent.xcodeproj 的目录。")

    # ================================================================
    #  核心入口：确保 WDA 可用
    # ================================================================

    @classmethod
    def _ensure_wda(cls, serial: Optional[str], wda_project: Optional[str],
                    port: int = 8100):
        """确保 WDA 可用：复用已有 → xcodebuild 启动"""
        device_changed = (serial and cls._current_serial
                          and serial != cls._current_serial)

        def _wda_reachable() -> bool:
            if cls._wda_url and cls._check_wda_url(cls._wda_url):
                return True
            return cls._is_wda_ready(port)

        if not device_changed:
            if (cls._xcodebuild_proc and cls._xcodebuild_proc.poll() is None
                    and _wda_reachable()):
                logger.info(f"复用已有 xcodebuild (pid={cls._xcodebuild_proc.pid})")
                return
            if cls._is_wda_ready(port) and cls._verify_wda_connection(port):
                logger.info(f"检测到 WDA 已就绪 (localhost:{port})")
                cls._current_serial = serial
                return
            if cls._wda_url and cls._check_wda_url(cls._wda_url):
                logger.info(f"检测到 WDA 已就绪 ({cls._wda_url})")
                cls._current_serial = serial
                return

        if not wda_project:
            raise RuntimeError(
                "WDA 未就绪且未配置项目路径。\n"
                "请在设置中填入 WebDriverAgent.xcodeproj 的完整路径，\n"
                "或先通过 Xcode 手动启动 WDA。")

        if device_changed:
            logger.info(f"设备切换: {cls._current_serial} → {serial}，重启 WDA…")

        cls._wda_url = None
        cls._stop_xcodebuild()
        cls._stop_iproxy()
        cls._cleanup_port(port)

        if cls._start_wda_xcodebuild(serial, wda_project, port):
            cls._current_serial = serial
            return

        raise RuntimeError(
            "WDA 无法启动。请检查：\n"
            "1. WebDriverAgent.xcodeproj 路径是否正确\n"
            "2. 设备已通过 USB 连接并信任此 Mac\n"
            "3. Xcode 中已配置签名 (Signing & Capabilities)\n"
            "4. 已安装 iproxy: brew install libimobiledevice")

    @classmethod
    def _cleanup_port(cls, port: int):
        """释放端口上残留的占用进程"""
        if not cls._is_port_open(port):
            return
        logger.info(f"端口 {port} 被占用，强制清理…")
        cls._free_port(port)
        time.sleep(0.5)

    # ================================================================
    #  xcodebuild 启动 WDA
    # ================================================================

    @classmethod
    def _start_wda_xcodebuild(cls, serial: Optional[str], wda_project: str,
                               port: int = 8100, timeout: float = 120) -> bool:
        """通过 xcodebuild test 启动 WDA，配合 iproxy 做端口转发"""
        cls._stop_xcodebuild()
        cls._ensure_iproxy(serial, port)

        wda_project = cls._resolve_xcode_project(wda_project)

        if wda_project.endswith('.xcworkspace'):
            proj_flag = ["-workspace", wda_project]
        else:
            proj_flag = ["-project", wda_project]

        destination = f"id={serial}" if serial else "generic/platform=iOS"
        cmd = [
            "xcodebuild", "test",
            *proj_flag,
            "-scheme", "WebDriverAgentRunner",
            "-destination", destination,
            "-allowProvisioningUpdates",
        ]
        logger.info(f"启动 WDA: xcodebuild test → {destination}")

        try:
            cls._xcodebuild_proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except FileNotFoundError:
            logger.warning("未找到 xcodebuild，请确保已安装 Xcode Command Line Tools")
            return False
        except Exception as e:
            logger.warning(f"xcodebuild 启动失败: {e}")
            return False

        cls._xcbuild_output_q = queue.Queue()


        def _reader():
            try:
                for raw in cls._xcodebuild_proc.stdout:
                    line = raw.decode("utf-8", errors="replace").rstrip()
                    if line:
                        cls._xcbuild_output_q.put(line)
            except Exception:
                pass

        threading.Thread(target=_reader, daemon=True).start()
        return cls._wait_wda_ready(port, timeout)

    _xcbuild_output_q: Optional[queue.Queue] = None

    @staticmethod
    def _log_xcodebuild_line(line: str):
        """过滤 xcodebuild 输出，只记录有价值的信息"""
        if any(kw in line for kw in ("error:", "BUILD FAILED", "FAILED TO")):
            logger.warning(f"[xcodebuild] {line}")
        elif "ServerURLHere" in line:
            logger.info(f"[xcodebuild] {line}")
        elif line.startswith("Test Suite") or "Running tests" in line:
            logger.info(f"[xcodebuild] {line}")

    @staticmethod
    def _extract_server_url(line: str) -> Optional[str]:
        tag = "ServerURLHere->"
        end_tag = "<-ServerURLHere"
        idx = line.find(tag)
        if idx < 0:
            return None
        start = idx + len(tag)
        end = line.find(end_tag, start)
        if end < 0:
            return None
        return line[start:end].strip()

    @classmethod
    def _wait_wda_ready(cls, port: int, timeout: float) -> bool:
        """等待 xcodebuild 启动的 WDA 变为可用"""
        if not cls._xcodebuild_proc:
            return False

        collected: list[str] = []
        oq = cls._xcbuild_output_q
        device_url: Optional[str] = None
        last_diag = 0.0
        start = time.time()

        deadline = start + timeout
        while time.time() < deadline:
            if oq:
                while not oq.empty():
                    line = oq.get_nowait()
                    collected.append(line)
                    cls._log_xcodebuild_line(line)
                    if not device_url:
                        url = cls._extract_server_url(line)
                        if url:
                            device_url = url

            if cls._xcodebuild_proc.poll() is not None:
                time.sleep(0.3)
                if oq:
                    while not oq.empty():
                        collected.append(oq.get_nowait())
                logger.warning(f"xcodebuild 退出 (code={cls._xcodebuild_proc.returncode})")
                for line in collected[-10:]:
                    logger.warning(f"  {line}")
                cls._xcodebuild_proc = None
                return False

            local_url = f"http://localhost:{port}"
            if cls._check_wda_url(local_url):
                cls._wda_url = local_url
                logger.info("WDA 已就绪 (via iproxy)")
                return True

            if device_url and cls._check_wda_url(device_url):
                cls._wda_url = device_url
                logger.info(f"WDA 已就绪 (via WiFi: {device_url})")
                return True

            now = time.time()
            if device_url and now - last_diag > 10:
                elapsed = int(now - start)
                try:
                    resp = _requests.get(
                        f"{local_url}/status", timeout=3)
                    logger.info(f"WDA 探测 ({elapsed}s): iproxy HTTP {resp.status_code}, "
                                f"body={resp.text[:200]}")
                except Exception as e:
                    logger.warning(f"WDA 探测 ({elapsed}s): iproxy "
                                   f"{type(e).__name__}: {e}")
                last_diag = now

            time.sleep(2)

        logger.warning(f"WDA 启动超时 ({timeout}s)")
        cls._stop_xcodebuild()
        return False

    @classmethod
    def _stop_xcodebuild(cls):
        if not cls._xcodebuild_proc or cls._xcodebuild_proc.poll() is not None:
            cls._xcodebuild_proc = None
            return
        cls._xcodebuild_proc.terminate()
        try:
            cls._xcodebuild_proc.wait(timeout=5)
        except Exception:
            try:
                cls._xcodebuild_proc.kill()
            except Exception:
                pass
        cls._xcodebuild_proc = None

    # ================================================================
    #  iproxy 端口转发 (CLI, brew install libimobiledevice)
    # ================================================================

    @classmethod
    def _ensure_iproxy(cls, serial: Optional[str], port: int = 8100):
        if (cls._iproxy_proc and cls._iproxy_proc.poll() is None
                and cls._iproxy_serial == serial):
            logger.info(f"复用已有 iproxy: localhost:{port}")
            return

        cls._stop_iproxy()

        cmd = ["iproxy", str(port), "8100"]
        if serial:
            cmd.extend(["-u", serial])
        logger.info(f"启动端口转发: {' '.join(cmd)}")

        try:
            cls._iproxy_proc = subprocess.Popen(
                cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            raise RuntimeError(
                "未找到 iproxy，请运行: brew install libimobiledevice")
        except Exception as e:
            logger.warning(f"iproxy 启动失败: {e}")
            return

        time.sleep(1)
        if cls._iproxy_proc.poll() is not None:
            logger.warning(f"iproxy 立即退出 (code={cls._iproxy_proc.returncode})")
            cls._iproxy_proc = None
            cls._iproxy_serial = None
        else:
            cls._iproxy_serial = serial
            logger.info(f"iproxy 已启动 (pid={cls._iproxy_proc.pid})")

    @classmethod
    def _stop_iproxy(cls):
        if not cls._iproxy_proc:
            return
        try:
            cls._iproxy_proc.terminate()
            cls._iproxy_proc.wait(timeout=3)
        except Exception:
            try:
                cls._iproxy_proc.kill()
            except Exception:
                pass
        cls._iproxy_proc = None
        cls._iproxy_serial = None

    # ================================================================
    #  生命周期
    # ================================================================

    @classmethod
    def shutdown_proxy(cls):
        """程序退出时清理所有子进程"""
        cls._stop_xcodebuild()
        cls._stop_iproxy()
        cls._current_serial = None
        cls._wda_url = None

    async def initialize(self):
        """初始化 iOS WDA 连接（含一次自动重试）"""
        try:
            await self._do_initialize()
        except Exception as first_err:
            logger.warning(f"首次连接失败 ({first_err})，清理后重试…")
            self._cleanup_port(8100)
            await self._do_initialize()

    async def _do_initialize(self):
        local_port = 8100
        serial = self.base_page.device_id or None
        wda_project = getattr(self.base_page, "ios_wda_project", None)

        loop = asyncio.get_event_loop()

        wda_url_before = IOSDriver._wda_url or f"http://localhost:{local_port}"
        saved_bundle = self._get_active_bundle_id(wda_url_before)
        if saved_bundle:
            logger.info(f"记录当前前台 App: {saved_bundle}")

        await loop.run_in_executor(
            None, self._ensure_wda, serial, wda_project, local_port)

        wda_url = IOSDriver._wda_url or f"http://localhost:{local_port}"
        self.wda_client = wda.Client(wda_url)

        try:
            status = self.wda_client.status()
        except Exception as e:
            raise RuntimeError(f"WDA 无法获取状态: {e}") from e

        logger.info(f"WDA 状态: ready={status.get('ready')}, "
                     f"device={status.get('os', {}).get('version', '?')}")

        existing_sid = status.get("sessionId")
        if existing_sid:
            self.wda_client._session_id = existing_sid
            logger.info(f"复用已有 session: {existing_sid[:8]}…")
        else:
            self._create_empty_session(wda_url)

        try:
            self.screen_w, self.screen_h = self.wda_client.window_size()
        except Exception as e:
            logger.warning(f"session 已失效 ({type(e).__name__})，删除旧 session 并重建…")
            if existing_sid:
                try:
                    _requests.delete(f"{wda_url}/session/{existing_sid}", timeout=5)
                except Exception:
                    pass
            self._create_empty_session(wda_url)
            self.screen_w, self.screen_h = self.wda_client.window_size()

        logger.info(f"iOS 屏幕: {self.screen_w}x{self.screen_h}")

        if saved_bundle:
            self._restore_foreground_app(wda_url, saved_bundle)

    def _restore_foreground_app(self, wda_url: str, expected_bundle: str):
        """检查前台 App 是否还是预期的，如果被切走则拉回来"""
        current = self._get_active_bundle_id(wda_url)
        if current == expected_bundle:
            return
        logger.warning(f"前台 App 已切换: {current}，正在恢复 {expected_bundle}…")
        sid = self.wda_client._session_id
        if sid:
            self._activate_app(wda_url, sid, expected_bundle)
            time.sleep(1)
            verify = self._get_active_bundle_id(wda_url)
            if verify == expected_bundle:
                logger.info(f"前台 App 已恢复: {expected_bundle}")
            else:
                logger.warning(f"恢复失败，当前前台: {verify}")

    @staticmethod
    def _get_active_bundle_id(wda_url: str) -> Optional[str]:
        """获取当前前台 App 的 bundleId"""
        try:
            resp = _requests.get(f"{wda_url}/wda/activeAppInfo", timeout=5)
            if resp.ok:
                return resp.json().get("value", {}).get("bundleId")
        except Exception:
            pass
        return None

    @staticmethod
    def _activate_app(wda_url: str, session_id: str, bundle_id: str):
        """通过 WDA activate 接口将 App 拉回前台（不重启）"""
        try:
            _requests.post(
                f"{wda_url}/session/{session_id}/wda/apps/activate",
                json={"bundleId": bundle_id}, timeout=10)
            logger.info(f"已激活前台 App: {bundle_id}")
        except Exception as e:
            logger.warning(f"激活 App 失败: {e}")

    def _create_empty_session(self, wda_url: str):
        """创建空 session；若前台 App 被切走则自动拉回"""
        saved_bundle = self._get_active_bundle_id(wda_url)
        if saved_bundle:
            logger.info(f"记录当前前台 App: {saved_bundle}")

        caps = {"shouldWaitForQuiescence": False}
        try:
            resp = _requests.post(
                f"{wda_url}/session",
                json={"capabilities": {"alwaysMatch": caps}},
                timeout=10)
            new_sid = resp.json().get("value", {}).get("sessionId")
            if new_sid:
                self.wda_client._session_id = new_sid
                logger.info(f"创建空 session: {new_sid[:8]}…")
                if saved_bundle:
                    self._activate_app(wda_url, new_sid, saved_bundle)
                return
            logger.warning(f"session 响应异常: {resp.text[:200]}")
        except Exception as e:
            if "Not authorized" in str(e):
                raise RuntimeError(
                    "iOS 设备未开启 UI 自动化权限，"
                    "请在 iPhone 上：设置 → 开发者 → 启用 UI 自动化"
                ) from e
            logger.warning(f"创建 session 失败: {e}")

    # ================================================================
    #  设备列表 / 连接关闭
    # ================================================================

    @staticmethod
    def list_devices() -> list[str]:
        """获取已连接的 iOS 设备 UDID 列表"""
        for cmd, parser in (
            (["idevice_id", "-l"], IOSDriver._parse_idevice_id),
            (["xcrun", "xctrace", "list", "devices"], IOSDriver._parse_xctrace),
        ):
            try:
                r = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                if r.returncode == 0:
                    devices = parser(r.stdout)
                    if devices:
                        return devices
            except FileNotFoundError:
                continue
            except Exception as e:
                logger.debug(f"{cmd[0]} 失败: {e}")
        return []

    @staticmethod
    def _parse_idevice_id(output: str) -> list[str]:
        return [s.strip() for s in output.strip().splitlines() if s.strip()]

    @staticmethod
    def _parse_xctrace(output: str) -> list[str]:
        """从 xcrun xctrace list devices 输出中提取真机 UDID"""
        devices = []
        in_devices = False
        for line in output.splitlines():
            if "== Devices ==" in line:
                in_devices = True
                continue
            if "== Simulators ==" in line:
                break
            if not in_devices or not line.strip():
                continue
            # 格式: DeviceName (osVersion) (UDID)
            idx = line.rfind("(")
            if idx < 0:
                continue
            udid = line[idx + 1:].rstrip(")")
            if len(udid) >= 24:
                devices.append(udid)
        return devices

    async def connect_close(self):
        if not self.wda_client:
            return
        loop = asyncio.get_event_loop()
        try:
            await asyncio.wait_for(
                loop.run_in_executor(None, self.wda_client.close), timeout=5.0)
        except asyncio.TimeoutError:
            logger.warning("wda_client.close() 超时")
        except Exception as e:
            logger.warning(f"wda_client.close() 异常: {e}")
        self.wda_client = None

    # ================================================================
    #  设备操作：点击 / 滑动 / 截图
    # ================================================================

    async def press_position(self, position, duration):
        x = int(position[0] * self.screen_w)
        y = int(position[1] * self.screen_h)
        loop = asyncio.get_event_loop()
        try:
            fn = self.wda_client.click if duration <= 0.1 else self.wda_client.tap_hold
            args = (x, y) if duration <= 0.1 else (x, y, duration)
            await asyncio.wait_for(loop.run_in_executor(None, fn, *args), timeout=10)
        except Exception as e:
            logger.warning(f"操作异常: {type(e).__name__}: {e}")
            raise

    async def swipe(self, point_start, point_end, duration):
        loop = asyncio.get_event_loop()
        await asyncio.wait_for(
            loop.run_in_executor(
                None, self.wda_client.swipe,
                int(point_start[0] * self.screen_w),
                int(point_start[1] * self.screen_h),
                int(point_end[0] * self.screen_w),
                int(point_end[1] * self.screen_h),
                int(duration * 1000)),
            timeout=10)

    async def get_screen_shot(self, x: float, y: float, w: float, h: float):
        loop = asyncio.get_event_loop()
        full_image = await asyncio.wait_for(
            loop.run_in_executor(None, self.wda_client.screenshot), timeout=10)

        is_full = (x == 0.5 and y == 0.5 and w == 1 and h == 1)
        if not is_full:
            px, py = self.screen_w * (x - 0.5 * w), self.screen_h * (y - 0.5 * h)
            full_image = full_image.crop((px, py, px + self.screen_w * w, py + self.screen_h * h))

        return cv2.cvtColor(np.array(full_image), cv2.COLOR_RGB2BGR)

    # ================================================================
    #  视频录制（基于 WDA 截图）
    # ================================================================

    def start_video_recording(self, output_path: str):
        if not self.wda_client:
            logger.warning("WDA 未连接，无法录制视频")
            return
        self._video_output = output_path
        self._video_running = True
        self._video_writer = None

        client = self.wda_client
        scale = 0.5

        def _capture_loop():
            fps = 5
            interval = 1.0 / fps
            try:
                while self._video_running:
                    t0 = time.monotonic()
                    try:
                        pil_img = client.screenshot(png_filename=None)
                        frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
                    except Exception:
                        time.sleep(interval)
                        continue
                    small = cv2.resize(frame, None, fx=scale, fy=scale,
                                       interpolation=cv2.INTER_AREA)
                    if self._video_writer is None:
                        h, w = small.shape[:2]
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                        self._video_writer = cv2.VideoWriter(
                            output_path, fourcc, fps, (w, h))
                    self._video_writer.write(small)
                    elapsed = time.monotonic() - t0
                    sleep_time = interval - elapsed
                    if sleep_time > 0:
                        time.sleep(sleep_time)
            except Exception as e:
                logger.warning(f"iOS 视频录制线程异常: {e}")

        self._video_thread = threading.Thread(
            target=_capture_loop, daemon=True, name="ios-video-recorder")
        self._video_thread.start()
        logger.info(f"iOS 视频录制已启动: {output_path}")

    def stop_video_recording(self) -> str | None:
        if not self._video_running:
            return None
        self._video_running = False
        if self._video_thread:
            self._video_thread.join(timeout=5)
            self._video_thread = None
        if self._video_writer:
            self._video_writer.release()
            self._video_writer = None
        logger.info(f"iOS 视频录制已停止: {self._video_output}")
        return self._video_output
