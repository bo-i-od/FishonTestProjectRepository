"""PC (Unity on Windows) driver.

用于驱动在 Windows 上原生运行的 Unity 游戏（.exe 或 Unity Editor 播放模式）。
不依赖 airtest，窗口定位 / 鼠标事件 / 截图 / 录屏 全部在本文件内独立实现。

device_id 语义
---------------
- None / 空字符串: 使用默认关键字（"UnityContainerWndClass"）按窗口类名/标题匹配。
- int 或全数字字符串: 直接当作窗口句柄 HWND。
- 其他字符串: 作为窗口标题或类名的不区分大小写子串匹配。

使用约束
---------
- Unity 窗口必须可见且非最小化，initialize 会显式 SW_RESTORE + 置前台。
- 自动处理 Unity Editor 模式下的 GameView 子窗口定位与工具栏裁剪。
- 点击/滑动期间会占用真实系统鼠标光标，不要手动操作鼠标。
- DPI 缩放被 GetClientRect + ClientToScreen 自然吸收，无需额外系数。
"""

import asyncio
import base64
import threading
import time
import zlib

import cv2
import mss
import numpy as np
import win32con
import win32gui
from pywinauto import mouse as _pw_mouse

from common import rpc_method_request
from common.driver.base_driver import BaseDeviceDriver
from common.log import get_logger
from common.rpc_method_request import get_screen_size

logger = get_logger("pc_driver")

_DEFAULT_WINDOW_KEYWORD = "UnityContainerWndClass"


def _find_hwnd_by_keyword(keyword: str) -> int | None:
    """按标题或类名子串（不区分大小写）在可见顶层窗口中查找 HWND。"""
    if not keyword:
        return None

    keyword_l = keyword.lower()
    matched: list[int] = []

    def _enum(hwnd, _):
        # 卫语句：过滤不可见窗口
        if not win32gui.IsWindowVisible(hwnd):
            return True

        title = (win32gui.GetWindowText(hwnd) or "").lower()
        cls = (win32gui.GetClassName(hwnd) or "").lower()

        # 布尔条件拆分
        match_title = keyword_l in title
        match_cls = keyword_l in cls

        if match_title or match_cls:
            matched.append(hwnd)
        return True

    win32gui.EnumWindows(_enum, None)
    return matched[0] if matched else None


def _find_game_view_child(parent_hwnd: int) -> int | None:
    """在父窗口中查找标题包含 'UnityEditor.GameView' 的子窗口"""
    matched = []

    def _enum_child(hwnd, _):
        title = win32gui.GetWindowText(hwnd) or ""
        if "UnityEditor.GameView" in title:
            matched.append(hwnd)
        return True

    try:
        win32gui.EnumChildWindows(parent_hwnd, _enum_child, None)
    except Exception:
        pass

    return matched[0] if matched else None


class PCDriver(BaseDeviceDriver):
    def __init__(self, page):
        super().__init__(page)
        self._hwnd: int | None = None
        self.client_w: int = 0
        self.client_h: int = 0
        self._client_origin: tuple[int, int] = (0, 0)
        self._mss = None

        self._video_running = False
        self._video_thread: threading.Thread | None = None
        self._video_writer: cv2.VideoWriter | None = None
        self._video_output: str | None = None

    async def initialize(self):
        size = await get_screen_size(server=self.base_page.server)
        self.screen_w = size[0]
        self.screen_h = size[1]

        dev_id = self.base_page.device_id
        hwnd = self._parse_device_id(dev_id)

        # 未能找到窗口直接结束后续初始化
        if not hwnd or not win32gui.IsWindow(hwnd):
            logger.warning(f"未能找到 Unity 窗口 (device_id={dev_id!r})，press/swipe/本地截图将不可用")
            self._hwnd = None
            return

        self._hwnd = hwnd
        self._bring_to_foreground(hwnd)
        self._refresh_client_geometry()

        logger.info(
            f"已绑定 Unity 窗口 hwnd={hwnd}, title={win32gui.GetWindowText(hwnd)!r}, "
            f"client={self.client_w}x{self.client_h}@{self._client_origin}"
        )

        self._init_mss()

    def _parse_device_id(self, dev_id) -> int | None:
        """解析并获取设备 ID 对应的 HWND"""
        if isinstance(dev_id, int):
            return dev_id

        if isinstance(dev_id, str) and dev_id.strip():
            s = dev_id.strip()
            if s.isdigit():
                return int(s)
            return _find_hwnd_by_keyword(s)

        return _find_hwnd_by_keyword(_DEFAULT_WINDOW_KEYWORD)

    def _init_mss(self):
        """初始化截图工具"""
        try:
            self._mss = mss.mss()
        except Exception as e:
            logger.warning(f"mss 初始化失败: {e}")
            self._mss = None

    @staticmethod
    def _bring_to_foreground(hwnd: int) -> None:
        try:
            placement = win32gui.GetWindowPlacement(hwnd)
            show_cmd = win32con.SW_RESTORE if placement[1] == win32con.SW_SHOWMINIMIZED else win32con.SW_SHOW
            win32gui.ShowWindow(hwnd, show_cmd)
            win32gui.SetForegroundWindow(hwnd)
        except Exception as e:
            logger.debug(f"SetForegroundWindow 失败（可忽略）: {e}")

    def _refresh_client_geometry(self) -> None:
        """刷新客户区像素尺寸与屏幕绝对坐标。"""
        if not self._hwnd:
            return

        try:
            # 优先尝试 Unity Editor 模式，成功则返回
            if self._refresh_for_editor():
                return
            # 回退到独立包 (.exe) 模式
            self._refresh_for_exe()
        except Exception as e:
            logger.warning(f"读取窗口几何失败: {e}")
            self.client_w, self.client_h = 0, 0
            self._client_origin = (0, 0)

    def _refresh_for_editor(self) -> bool:
        """封装：处理 Editor 模式下的 GameView 子窗口尺寸（裁剪工具栏）"""
        game_view_hwnd = _find_game_view_child(self._hwnd)
        if not game_view_hwnd:
            return False

        left, top, right, bottom = win32gui.GetClientRect(game_view_hwnd)
        offset_top = 40  # 扣除面板顶部的工具栏

        self.client_w = max(0, right - left)
        self.client_h = max(0, bottom - top - offset_top)

        ox, oy = win32gui.ClientToScreen(game_view_hwnd, (0, offset_top))
        self._client_origin = (ox, oy)

        logger.debug(f"已锁定 GameView 子窗口: hwnd={game_view_hwnd}, client={self.client_w}x{self.client_h}")
        return True

    def _refresh_for_exe(self) -> None:
        """封装：处理独立运行包的窗口尺寸"""
        left, top, right, bottom = win32gui.GetClientRect(self._hwnd)
        self.client_w = max(0, right - left)
        self.client_h = max(0, bottom - top)
        self._client_origin = win32gui.ClientToScreen(self._hwnd, (0, 0))

    async def connect_close(self):
        try:
            if self._video_running:
                self.stop_video_recording()
        finally:
            if self._mss is not None:
                try:
                    self._mss.close()
                except Exception:
                    pass
                self._mss = None
            self._hwnd = None

    def _normalized_to_abs(self, nx: float, ny: float) -> tuple[int, int]:
        """归一化坐标 → 屏幕绝对像素坐标。"""
        if not self._hwnd or self.client_w <= 0 or self.client_h <= 0:
            self._refresh_client_geometry()

        ox, oy = self._client_origin
        ax = ox + int(nx * self.client_w)
        ay = oy + int(ny * self.client_h)
        return ax, ay

    def _do_press(self, ax: int, ay: int, duration: float) -> None:
        try:
            _pw_mouse.move(coords=(ax, ay))
            _pw_mouse.press(button="left", coords=(ax, ay))
            time.sleep(max(duration, 0.01))
            _pw_mouse.release(button="left", coords=(ax, ay))
        except Exception as e:
            logger.warning(f"press_position 失败: {e}")

    def _do_swipe(self, ax1: int, ay1: int, ax2: int, ay2: int, duration: float) -> None:
        try:
            # 卫语句：处理极短时间的瞬间滑动
            if duration <= 0:
                _pw_mouse.move(coords=(ax1, ay1))
                _pw_mouse.press(button="left", coords=(ax1, ay1))
                _pw_mouse.move(coords=(ax2, ay2))
                _pw_mouse.release(button="left", coords=(ax2, ay2))
                return

            _pw_mouse.move(coords=(ax1, ay1))
            _pw_mouse.press(button="left", coords=(ax1, ay1))

            start_time = time.perf_counter()

            # 基于真实时间的插值循环
            while True:
                elapsed = time.perf_counter() - start_time
                if elapsed >= duration:
                    break

                # 计算当前进度 (0.0 ~ 1.0)
                progress = elapsed / duration

                # 计算当前坐标
                x = int(ax1 + (ax2 - ax1) * progress)
                y = int(ay1 + (ay2 - ay1) * progress)

                _pw_mouse.move(coords=(x, y))
                time.sleep(0.01)  # 短暂休眠，防止 CPU 空转并留给系统响应事件

            # 确保最后停在终点并释放
            _pw_mouse.move(coords=(ax2, ay2))
            _pw_mouse.release(button="left", coords=(ax2, ay2))

        except Exception as e:
            logger.warning(f"swipe 失败: {e}")

    async def press_position(self, position, duration):
        if not self._hwnd:
            logger.warning("press_position: 未绑定 Unity 窗口，忽略")
            return

        ax, ay = self._normalized_to_abs(position[0], position[1])
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._do_press, ax, ay, float(duration))

    async def swipe(self, point_start, point_end, duration):
        if not self._hwnd:
            logger.warning("swipe: 未绑定 Unity 窗口，忽略")
            return

        ax1, ay1 = self._normalized_to_abs(point_start[0], point_start[1])
        ax2, ay2 = self._normalized_to_abs(point_end[0], point_end[1])
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self._do_swipe, ax1, ay1, ax2, ay2, float(duration))

    async def get_screen_shot(self, x: float, y: float, w: float, h: float):
        pixel_x, pixel_y = self.screen_w * x, self.screen_h * y
        pixel_w, pixel_h = self.screen_w * w, self.screen_h * h

        [img_b64encode, fmt] = await rpc_method_request.screen_shot(
            self.base_page.server, pixel_x, pixel_y, pixel_w, pixel_h)

        if fmt.endswith('.deflate'):
            imgdata = zlib.decompress(base64.b64decode(img_b64encode))
            img_b64encode = base64.b64encode(imgdata)

        img_b64decode = base64.b64decode(img_b64encode)
        img_array = np.frombuffer(img_b64decode, np.uint8)
        return cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

    def _local_snapshot(self):
        """使用 mss 抓取 Unity 窗口客户区，返回 BGR numpy 数组。"""
        # 卫语句：拦截无效状态
        if not self._mss or not self._hwnd:
            return None

        if self.client_w <= 0 or self.client_h <= 0:
            self._refresh_client_geometry()

        if self.client_w <= 0 or self.client_h <= 0:
            return None

        x, y = self._client_origin
        monitor = {
            "left": int(x), "top": int(y),
            "width": int(self.client_w), "height": int(self.client_h),
        }

        try:
            sct_img = self._mss.grab(monitor)
            return np.array(sct_img, dtype=np.uint8)[..., :3]
        except Exception as e:
            logger.debug(f"mss grab 失败: {e}")
            return None

    def start_video_recording(self, output_path: str):
        if self._video_running:
            logger.warning("视频录制已在运行，忽略重复调用")
            return

        if not self._hwnd:
            logger.warning("start_video_recording: 未绑定 Unity 窗口，无法录制")
            return

        self._video_output = output_path
        self._video_running = True
        self._video_writer = None

        self._video_thread = threading.Thread(
            target=self._recording_loop, args=(output_path, 10),
            daemon=True, name="pc-video-recorder"
        )
        self._video_thread.start()
        logger.info(f"PC 视频录制已启动: {output_path}")

    def _recording_loop(self, output_path: str, fps: int):
        """录屏主循环（优化缩进层级）"""
        interval = 1.0 / fps
        try:
            while self._video_running:
                t0 = time.monotonic()
                self._process_single_video_frame(output_path, fps)

                dt = time.monotonic() - t0
                if dt < interval:
                    time.sleep(interval - dt)
        except Exception as e:
            logger.warning(f"视频录制线程异常: {e}")

    def _process_single_video_frame(self, output_path: str, fps: int):
        """封装：处理单帧录制逻辑"""
        frame = self._local_snapshot()
        if frame is None:
            return

        if self._video_writer is None:
            self._init_video_writer(frame, output_path, fps)

        try:
            self._video_writer.write(frame)
        except Exception as e:
            logger.debug(f"写帧失败: {e}")

    def _init_video_writer(self, frame, output_path: str, fps: int):
        """封装：初始化视频写入器"""
        h, w = frame.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._video_writer = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

    def stop_video_recording(self) -> str | None:
        if not self._video_running:
            return None

        self._video_running = False

        if self._video_thread:
            self._video_thread.join(timeout=5)
            self._video_thread = None

        if self._video_writer:
            try:
                self._video_writer.release()
            except Exception:
                pass
            self._video_writer = None

        logger.info(f"PC 视频录制已停止: {self._video_output}")
        return self._video_output