from common.log import get_logger
logger = get_logger("harmony_driver")
import math
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time

import cv2
from common.driver.base_driver import BaseDeviceDriver

_NO_WINDOW = subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
_hdc_path_cache: str | None = None


def get_hdc_path() -> str:
    """查找 hdc 可执行文件的完整路径，优先 PATH，再搜索 DevEco Studio 常见安装位置。"""
    global _hdc_path_cache
    if _hdc_path_cache is not None:
        return _hdc_path_cache

    found = shutil.which("hdc")
    if found:
        _hdc_path_cache = found
        return found

    candidates: list[str] = []
    if platform.system() == "Darwin":
        candidates = [
            "/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc",
            os.path.expanduser("~/Library/Huawei/Sdk/openharmony/toolchains/hdc"),
        ]
    elif platform.system() == "Windows":
        local = os.environ.get("LOCALAPPDATA", "")
        if local:
            candidates.append(os.path.join(local, "Huawei", "Sdk", "openharmony", "toolchains", "hdc.exe"))
        candidates.append(r"C:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\toolchains\hdc.exe")
    else:
        candidates = [
            os.path.expanduser("~/Huawei/Sdk/openharmony/toolchains/hdc"),
        ]

    for p in candidates:
        if os.path.isfile(p) and os.access(p, os.X_OK):
            _hdc_path_cache = p
            logger.info(f"在 DevEco Studio 中找到 hdc: {p}")
            return p

    _hdc_path_cache = "hdc"
    return "hdc"


class HarmonyDriver(BaseDeviceDriver):

    def __init__(self, page):
        super().__init__(page)
        self.hdc_session: HDCSession | None = None
        self._video_running = False

    async def initialize(self):
        """初始化鸿蒙 HDC 连接并获取屏幕信息。"""
        if not self.base_page.device_id:
            devices = HDCSession.list_devices()
            if not devices:
                raise RuntimeError("未检测到鸿蒙设备，请确认 hdc 已安装且设备已连接")
            self.base_page.device_id = devices[0]
        self.hdc_session = HDCSession(device_id=self.base_page.device_id)

        w, h = self._detect_screen_size()
        self.screen_w, self.screen_h = w, h
        logger.info(f"[Harmony] 屏幕尺寸: {w}x{h}")

    def _detect_screen_size(self) -> tuple[int, int]:
        """通过 hidumper 获取屏幕分辨率，失败时回退截图探测。"""
        try:
            return self._detect_screen_size_hidumper()
        except Exception as e:
            logger.info(f"[Harmony] hidumper 获取分辨率失败({e})，回退截图探测")
            return self._detect_screen_size_screenshot()

    def _detect_screen_size_hidumper(self) -> tuple[int, int]:
        output = self.hdc_session.cmd("shell hidumper -s RenderService -a screen")
        if not output:
            raise RuntimeError("hidumper 无输出")
        import re
        match = re.search(r'(\d{3,5})\s*[xX×*]\s*(\d{3,5})', output)
        if not match:
            raise RuntimeError(f"无法从 hidumper 输出中解析分辨率: {output[:200]}")
        w, h = int(match.group(1)), int(match.group(2))
        if w <= 0 or h <= 0:
            raise RuntimeError(f"解析到无效分辨率: {w}x{h}")
        return w, h

    def _detect_screen_size_screenshot(self) -> tuple[int, int]:
        remote_path = "/data/local/tmp/_autotest_probe.jpeg"
        local_tmp = os.path.join(tempfile.gettempdir(), "_hdc_probe.jpeg")
        self.hdc_session.cmd(f"shell snapshot_display -f {remote_path}")
        try:
            HDCSession.file_recv(self.base_page.device_id, remote_path, local_tmp)
            img = cv2.imread(local_tmp)
        except Exception as e:
            raise RuntimeError(f"[Harmony] 无法获取屏幕分辨率: {e}") from e
        finally:
            try:
                os.remove(local_tmp)
            except OSError:
                pass
            self.hdc_session.cmd(f"shell rm -f {remote_path}")

        if img is None:
            raise RuntimeError("[Harmony] 截图解码为空")
        h, w = img.shape[:2]
        return w, h

    async def connect_close(self):
        if not self.hdc_session:
            return
        self.hdc_session.session_close()
        self.hdc_session = None

    async def press_position(self, position: list[float], duration: float):
        x = int(position[0] * self.screen_w)
        y = int(position[1] * self.screen_h)
        if duration <= 0.1:
            self.hdc_session.cmd(f"shell uitest uiInput click {x} {y}")
        else:
            self.hdc_session.cmd(f"shell uitest uiInput longClick {x} {y}")

    async def swipe(self, point_start, point_end, duration):
        sx = int(point_start[0] * self.screen_w)
        sy = int(point_start[1] * self.screen_h)
        ex = int(point_end[0] * self.screen_w)
        ey = int(point_end[1] * self.screen_h)
        distance = math.sqrt((ex - sx) ** 2 + (ey - sy) ** 2)
        speed = max(200, int(distance / max(duration, 0.05)))
        self.hdc_session.cmd(f"shell uitest uiInput swipe {sx} {sy} {ex} {ey} {speed}")

    async def get_screen_shot(self, x: float, y: float, w: float, h: float):
        full_image = self._capture_screen_via_hdc()

        if x == 0.5 and y == 0.5 and w == 1 and h == 1:
            return full_image

        pixel_x = self.screen_w * (x - 0.5 * w)
        pixel_y = self.screen_h * (y - 0.5 * h)
        pixel_w = self.screen_w * w
        pixel_h = self.screen_h * h
        box = (pixel_x, pixel_y, pixel_x + pixel_w, pixel_y + pixel_h)
        return full_image.crop(box)

    def _capture_screen_via_hdc(self):
        """通过 hdc snapshot_display 截图并返回 cv2 图像。"""
        remote_path = "/data/local/tmp/_autotest_screen.jpeg"
        local_tmp = os.path.join(tempfile.gettempdir(), "_hdc_screen.jpeg")
        try:
            self.hdc_session.cmd(f"shell snapshot_display -f {remote_path}")
            HDCSession.file_recv(self.base_page.device_id, remote_path, local_tmp)
            img = cv2.imread(local_tmp)
        except FileNotFoundError:
            logger.warning("未找到 hdc 命令，请确保 HarmonyOS SDK toolchains 已在 PATH 中")
            return None
        except Exception as e:
            logger.warning(f"[Harmony] 截图失败: {e}")
            return None
        finally:
            try:
                os.remove(local_tmp)
            except OSError:
                pass

        if img is None:
            logger.warning("[Harmony] 截图解码失败")
            return None
        return img

    _RECORDER_BUNDLE = "com.huawei.hmos.screenrecorder"
    _RECORDER_ABILITY = "com.huawei.hmos.screenrecorder.ServiceExtAbility"

    def start_video_recording(self, output_path: str):
        device_id = self.base_page.device_id
        self._video_running = True
        try:
            subprocess.run(
                self._hdc_prefix(device_id) + [
                    "shell", "aa", "start",
                    "-b", self._RECORDER_BUNDLE,
                    "-a", self._RECORDER_ABILITY,
                ],
                capture_output=True, text=True, timeout=10,
                creationflags=_NO_WINDOW)
            logger.info("[Harmony] 系统录屏已启动 (视频保留在设备端)")
        except Exception as e:
            logger.warning(f"[Harmony] 启动录屏失败: {e}")
            self._video_running = False

    RECORDING_ON_DEVICE = "__on_device__"

    def stop_video_recording(self) -> str | None:
        if not self._video_running:
            return None
        self._video_running = False
        device_id = self.base_page.device_id
        try:
            subprocess.run(
                self._hdc_prefix(device_id) + [
                    "shell", "aa", "start",
                    "-b", self._RECORDER_BUNDLE,
                    "-a", self._RECORDER_ABILITY,
                ],
                capture_output=True, text=True, timeout=10,
                creationflags=_NO_WINDOW)
            logger.info("[Harmony] 系统录屏已停止，视频保存在设备端")
        except Exception as e:
            logger.warning(f"[Harmony] 停止录屏失败: {e}")
            return None
        return self.RECORDING_ON_DEVICE

    @staticmethod
    def _hdc_prefix(device_id: str) -> list[str]:
        hdc = get_hdc_path()
        if device_id:
            return [hdc, "-t", device_id]
        return [hdc]


class HDCSession:
    def __init__(self, device_id):
        self.process = None
        self.device_id = device_id
        self.process = subprocess.Popen(
            [get_hdc_path(), "-t", f"{self.device_id}", "shell"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            creationflags=_NO_WINDOW,
        )

    def shell(self, cmd):
        if not self.process:
            return
        self.process.stdin.write(f"{cmd}\n")
        self.process.stdin.flush()

    def cmd(self, cmd):
        cmd_list = [get_hdc_path(), "-t", self.device_id, *cmd.split()]
        try:
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=15,
                creationflags=_NO_WINDOW,
            )
            return result.stdout
        except Exception as e:
            logger.warning(f"[HDC] error: {e}")
            return ""

    def session_close(self):
        if not self.process:
            return
        self.process.terminate()

    @staticmethod
    def list_devices() -> list[str]:
        """获取所有已连接鸿蒙设备列表。"""
        try:
            result = subprocess.run(
                [get_hdc_path(), "list", "targets"],
                capture_output=True, text=True, timeout=30,
                creationflags=_NO_WINDOW,
            )
            devices = []
            for line in result.stdout.strip().splitlines():
                dev = line.strip()
                if dev and dev != "[Empty]":
                    devices.append(dev)
            return devices
        except Exception as e:
            logger.warning(f"HDC 设备列表获取失败: {e}")
            return []

    @staticmethod
    def rport(device_id: str, port: int):
        """hdc -t <device_id> rport tcp:<port> tcp:<port> (反向端口转发)"""
        subprocess.run(
            [get_hdc_path(), "-t", device_id, "rport", f"tcp:{port}", f"tcp:{port}"],
            check=True, capture_output=True, text=True, timeout=15,
            creationflags=_NO_WINDOW,
        )

    @staticmethod
    def remove_rport(device_id: str, port: int):
        """移除反向端口转发。"""
        subprocess.run(
            [get_hdc_path(), "-t", device_id, "rport", "rm", f"tcp:{port}", f"tcp:{port}"],
            capture_output=True, text=True, timeout=15,
            creationflags=_NO_WINDOW,
        )

    @staticmethod
    def fport(device_id: str, host_port: int, device_port: int):
        """hdc -t <device_id> fport tcp:<host_port> tcp:<device_port> (正向端口转发)"""
        subprocess.run(
            [get_hdc_path(), "-t", device_id, "fport", f"tcp:{host_port}", f"tcp:{device_port}"],
            check=True, capture_output=True, text=True, timeout=15,
            creationflags=_NO_WINDOW,
        )

    @staticmethod
    def file_recv(device_id: str, remote_path: str, local_path: str):
        """从设备拉取文件到本地。"""
        subprocess.run(
            [get_hdc_path(), "-t", device_id, "file", "recv", remote_path, local_path],
            check=True, capture_output=True, text=True, timeout=60,
            creationflags=_NO_WINDOW,
        )

    @staticmethod
    def file_send(device_id: str, local_path: str, remote_path: str):
        """推送本地文件到设备。"""
        subprocess.run(
            [get_hdc_path(), "-t", device_id, "file", "send", local_path, remote_path],
            check=True, capture_output=True, text=True, timeout=60,
            creationflags=_NO_WINDOW,
        )
