from common.log import get_logger
logger = get_logger("android_driver")
import datetime
import os
import socket
import struct
import subprocess
import threading
import time

import cv2
import numpy as np
from ppadb.client import Client as AdbClient
from common.driver.base_driver import BaseDeviceDriver


class AndroidDriver(BaseDeviceDriver):
    def __init__(self, page):
        super().__init__(page)
        self.adb_session = None
        self.mini_cap_service = None
        self._screenrecord_process = None
        self._remote_video_path = None
        self._video_output = None
        self._video_running = False
        self._video_thread = None
        self._video_segments: list[str] = []
        self._video_size_args: list[str] = []

    async def initialize(self):
        """初始化 Android ADB 连接并获取屏幕信息。"""
        if not self.base_page.device_id:
            client = AdbClient(host="127.0.0.1", port=5037)
            self.base_page.device_id = client.devices()[0]
        self.adb_session = ADBSession(device_id=self.base_page.device_id)

        wm_size = self.adb_session.cmd(cmd="shell wm size")
        w, h = map(int, wm_size.split(':')[-1].strip().lower().split('x'))
        """
            ROTATION_0 = 0 （0度，正常竖屏）
            ROTATION_90 = 1 （90度，横屏，设备顺时针旋转90度）
            ROTATION_180 = 2 （180度，倒立竖屏）
            ROTATION_270 = 3 （270度，横屏，设备逆时针旋转90度，或者说是顺时针旋转270度）
        """
        orientation = self.adb_session.cmd(cmd="shell dumpsys display | grep mCurrentOrientation")
        rotation = 0
        if orientation:
            rotation = int(orientation.split("=")[-1].strip())
        self.screen_w, self.screen_h = w, h
        # if rotation % 2 == 0:
        #     self.screen_w, self.screen_h = w, h
        # else:
        #     self.screen_w, self.screen_h = h, w

        try:
            # 假设 MinicapService 在同一个文件或已导入
            self.mini_cap_service = MinicapService(device_id=self.base_page.device_id)
            self.mini_cap_service.start(display_width=self.screen_w, display_height=self.screen_h)
        except RuntimeError:
            logger.warning(f"无法使用minicap使用adb截图")
            self.mini_cap_service = None
        except Exception as e:
            logger.warning(f"{e}")
            self.mini_cap_service = None

    async def connect_close(self):
        if self.adb_session:
            self.adb_session.session_close()
            self.adb_session = None
        if self.mini_cap_service:
            self.mini_cap_service.stop()
            self.mini_cap_service = None

    async def press_position(self, position: list[float], duration: float):
        position_x = int(position[0] * self.screen_w)
        position_y = int(position[1] * self.screen_h)
        if duration <= 0.1:
            self.adb_session.shell(cmd=f"input tap {position_x} {position_y}")
            return
        self.adb_session.shell(f"input swipe {position_x} {position_y} {position_x} {position_y} {duration}")
        return

    async def swipe(self, point_start, point_end, duration):
        t = int(duration * 1000)
        start_x = int(point_start[0] * self.screen_w)
        start_y = int(point_start[1] * self.screen_h)
        end_x = int(point_end[0] * self.screen_w)
        end_y = int(point_end[1] * self.screen_h)
        self.adb_session.shell(f"input swipe {start_x} {start_y} {end_x} {end_y} {t}")

    async def get_screen_shot(self, x: float, y: float, w: float, h: float):
        pixel_x = self.screen_w * (x - 0.5 * w)
        pixel_y = self.screen_h * (y - 0.5 * h)
        pixel_w = self.screen_w * w
        pixel_h = self.screen_h * h
        is_full = False
        if x == 0.5 and y == 0.5 and w == 1 and h == 1:
            is_full = True

        if self.mini_cap_service:
            full_image = self.mini_cap_service.get_frame()
        else:
            full_image = self.capture_screen_via_adb()

        if is_full:
            screen_shot = full_image

        else:
            box = (pixel_x, pixel_y, pixel_x + pixel_w, pixel_y + pixel_h)
            screen_shot = full_image.crop(box)

        return screen_shot

    def capture_screen_via_adb(self):
        """
        通过ADB命令截图，并返回与原先代码兼容的OpenCV图像对象。
        返回：成功返回cv2图像，失败返回None。
        """
        try:
            # 关键步骤：使用adb exec-out命令直接获取二进制的PNG数据流
            # 这避免了临时文件，效率更高
            command = ['adb', '-s', f'{self.base_page.device_id}','exec-out', 'screencap', '-p']
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            png_data, error = process.communicate()

            if process.returncode != 0:
                logger.warning(f"ADB截图失败: {error.decode()}")
                return None

            img_binary = png_data
            # 将二进制数据转换为OpenCV图像格式
            img_array = np.frombuffer(img_binary, dtype=np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)  # 注意此处标志位修正

            if img is None:
                logger.warning(f"警告：cv2.imdecode未能解析出有效图像。")
            return img

        except FileNotFoundError:
            logger.warning(f"未找到ADB命令，请确保Android SDK平台工具已安装并在PATH中。")
            return None
        except Exception as e:
            logger.warning(f"截图过程中发生未知错误: {e}")
            return None

    def _get_half_resolution(self, device_id: str) -> list[str]:
        """获取设备屏幕分辨率并缩小一半，用于降低录屏体积。"""
        try:
            result = subprocess.run(
                ["adb", "-s", device_id, "shell", "wm", "size"],
                capture_output=True, text=True, timeout=5)
            dims_str = ""
            for line in reversed(result.stdout.strip().splitlines()):
                if 'x' in line:
                    dims_str = line.split(':')[-1].strip()
                    break
            if dims_str:
                parts = dims_str.split('x')
                w = int(parts[0]) // 2 & ~1
                h = int(parts[1]) // 2 & ~1
                return ["--size", f"{w}x{h}"]
        except Exception as e:
            logger.debug(f"获取设备分辨率失败: {e}")
        return []

    def _start_new_segment(self):
        """启动一个新的 screenrecord 片段（180 秒上限）。"""
        device_id = self.base_page.device_id
        remote_path = f"/sdcard/rec_{int(time.time())}.mp4"
        self._video_segments.append(remote_path)
        self._remote_video_path = remote_path
        self._screenrecord_process = subprocess.Popen(
            ["adb", "-s", device_id, "shell",
             "screenrecord", "--bit-rate", "2000000"] + self._video_size_args +
            ["--time-limit", "180", remote_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def _stop_current_segment(self):
        """停止当前正在运行的 screenrecord 进程。"""
        if not self._screenrecord_process:
            return
        device_id = self.base_page.device_id
        try:
            pid_result = subprocess.run(
                ["adb", "-s", device_id, "shell", "pidof", "screenrecord"],
                capture_output=True, text=True, timeout=5)
            pid = pid_result.stdout.strip()
            if pid:
                subprocess.run(
                    ["adb", "-s", device_id, "shell", "kill", "-2", pid],
                    capture_output=True, text=True, timeout=5)
            self._screenrecord_process.wait(timeout=10)
        except Exception as e:
            logger.warning(f"停止 screenrecord 片段异常: {e}")
            try:
                self._screenrecord_process.kill()
            except Exception:
                pass
        self._screenrecord_process = None
        time.sleep(1)

    def start_video_recording(self, output_path: str):
        device_id = self.base_page.device_id
        self._video_output = output_path
        self._video_running = True
        self._video_segments = []
        self._video_size_args = self._get_half_resolution(device_id)
        self._start_new_segment()

        seg_duration = 170

        def _monitor():
            while self._video_running:
                for _ in range(seg_duration):
                    if not self._video_running:
                        return
                    time.sleep(1)
                if not self._video_running:
                    return
                logger.info("screenrecord 片段轮换中…")
                self._stop_current_segment()
                if self._video_running:
                    self._start_new_segment()

        self._video_thread = threading.Thread(
            target=_monitor, daemon=True, name="adb-video-monitor")
        self._video_thread.start()
        logger.info(f"Android 视频录制已启动 (自动分段): {output_path} "
                     f"(2Mbps{', ' + self._video_size_args[1] if self._video_size_args else ''})")

    def stop_video_recording(self) -> str | None:
        if not self._video_running:
            return None
        self._video_running = False
        if self._video_thread:
            self._video_thread.join(timeout=5)
            self._video_thread = None

        self._stop_current_segment()
        time.sleep(0.5)

        device_id = self.base_page.device_id
        local_segments = []
        for i, remote_path in enumerate(self._video_segments):
            if len(self._video_segments) == 1:
                local_path = self._video_output
            else:
                base, ext = os.path.splitext(self._video_output)
                local_path = f"{base}_part{i}{ext}"
            try:
                subprocess.run(
                    ["adb", "-s", device_id, "pull", remote_path, local_path],
                    check=True, capture_output=True, text=True, timeout=60)
                subprocess.run(
                    ["adb", "-s", device_id, "shell", "rm", remote_path],
                    capture_output=True, text=True, timeout=5)
                local_segments.append(local_path)
            except Exception as e:
                logger.warning(f"拉取视频片段失败: {e}")

        if not local_segments:
            return None

        if len(local_segments) == 1:
            logger.info(f"Android 视频已保存: {self._video_output}")
            return self._video_output

        if self._concat_videos(local_segments, self._video_output):
            for seg in local_segments:
                try:
                    os.remove(seg)
                except Exception:
                    pass
            logger.info(f"Android 视频已保存 ({len(local_segments)} 段合并): {self._video_output}")
            return self._video_output

        logger.warning(f"视频合并失败，保留 {len(local_segments)} 个片段文件")
        return local_segments[0]

    @staticmethod
    def _concat_videos(segment_paths: list[str], output_path: str) -> bool:
        """合并多段视频。优先 ffmpeg（快速无损），回退 cv2（逐帧拷贝）。"""
        # --- ffmpeg ---
        try:
            list_file = output_path + ".filelist.txt"
            with open(list_file, 'w', encoding='utf-8') as f:
                for seg in segment_paths:
                    f.write(f"file '{os.path.abspath(seg)}'\n")
            subprocess.run(
                ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
                 "-i", list_file, "-c", "copy", output_path],
                check=True, capture_output=True, timeout=120)
            os.remove(list_file)
            return True
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            logger.debug(f"ffmpeg 合并失败，回退 cv2: {e}")

        # --- cv2 fallback ---
        try:
            writer = None
            for seg in segment_paths:
                cap = cv2.VideoCapture(seg)
                if not cap.isOpened():
                    continue
                if writer is None:
                    fps = cap.get(cv2.CAP_PROP_FPS) or 24
                    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                    writer = cv2.VideoWriter(output_path, fourcc, fps, (w, h))
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    writer.write(frame)
                cap.release()
            if writer:
                writer.release()
                return True
        except Exception as e:
            logger.warning(f"cv2 合并失败: {e}")
        return False


class ADBSession:
    def __init__(self, device_id):
        self.process = None
        self.device_id = device_id
        # 可以启动一个adb shell会话
        self.process = subprocess.Popen(
            ["adb", "-s", f"{self.device_id}", "shell"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def shell(self, cmd):
        if not self.process:
            return
        self.process.stdin.write(f"{cmd}\n")
        self.process.stdin.flush()

    def cmd(self, cmd):
        # , "shell", "wm", "size"
        cmd_list = ["adb", "-s", f"{self.device_id}"]
        for cmd_part in cmd.split(" "):
            if not cmd_part:
                continue
            cmd_list.append(cmd_part)
        try:
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout
        except Exception as e:
            logger.warning(f"error:{e}")
            return ""

    def session_close(self):
        if self.process:
            self.process.terminate()

    @staticmethod
    def list_devices() -> list[str]:
        """获取所有已连接 ADB 设备的序列号列表（不需要实例）。
        首次调用可能触发 adb server 启动，需要较长超时。"""
        try:
            result = subprocess.run(
                ["adb", "devices"], capture_output=True, text=True, timeout=30
            )
            devices = []
            for line in result.stdout.strip().splitlines()[1:]:
                parts = line.split("\t")
                if len(parts) >= 2 and parts[1].strip() == "device":
                    devices.append(parts[0].strip())
            return devices
        except Exception as e:
            logger.warning(f"ADB 设备列表获取失败: {e}")
            return []

    @staticmethod
    def reverse(device_id: str, port: int):
        """执行 adb -s <device_id> reverse tcp:<port> tcp:<port>，不需要实例。"""
        subprocess.run(
            ["adb", "-s", device_id, "reverse", f"tcp:{port}", f"tcp:{port}"],
            check=True, capture_output=True, text=True, timeout=15
        )

    @staticmethod
    def remove_reverse(device_id: str, port: int):
        """执行 adb -s <device_id> reverse --remove tcp:<port>，不需要实例。"""
        subprocess.run(
            ["adb", "-s", device_id, "reverse", "--remove", f"tcp:{port}"],
            capture_output=True, text=True, timeout=15
        )


class MinicapService:
    # [共享] 类级别端口管理，所有实例共享
    _used_ports = set()
    _port_lock = threading.Lock()
    _base_port = 1313  # 起始端口

    @classmethod
    def _allocate_port(cls, preferred_port=None):
        """自动分配一个未被占用的端口"""
        with cls._port_lock:
            # 如果指定了端口且未被占用，直接使用
            if preferred_port and preferred_port not in cls._used_ports:
                cls._used_ports.add(preferred_port)
                return preferred_port

            # 自动从 base_port 开始找一个空闲端口
            port = cls._base_port
            while port in cls._used_ports:
                port += 1
            cls._used_ports.add(port)
            return port

    @classmethod
    def _release_port(cls, port):
        """释放端口"""
        with cls._port_lock:
            cls._used_ports.discard(port)

    def __init__(self, device_id=None, local_port=None):
        """
        :param device_id: 设备ID，如 '127.0.0.1:21553'
        :param local_port: 指定端口（可选），不指定则自动分配
        """
        self.device_id = device_id
        # ✅ 自动分配端口，不同设备使用不同端口
        self.local_port = MinicapService._allocate_port(local_port)
        self.socket = None
        self.reader_thread = None
        self.running = False
        self.latest_frame = None
        self.frame_lock = threading.Lock()
        self._adb_prefix = ['adb'] if not device_id else ['adb', '-s', device_id]

        logger.info(f"[Minicap][{self.device_id}] 分配端口: {self.local_port}")

    def _recv_exact(self, length):
        """保证精确读取指定字节数"""
        data = b''
        while len(data) < length:
            chunk = self.socket.recv(length - len(data))
            if not chunk:
                raise ConnectionError("Socket 连接断开")
            data += chunk
        return data

    def _parse_banner(self):
        """正确解析 Minicap Banner 头"""
        header = self._recv_exact(2)
        version, banner_size = struct.unpack('<BB', header)

        rest = self._recv_exact(banner_size - 2)

        pid, real_w, real_h, virt_w, virt_h, orientation, quirks = struct.unpack(
            '<IIIIIbb', rest[:22]
        )

        return {
            'version': version,
            'real_size': (real_w, real_h),
            'virt_size': (virt_w, virt_h),
            'orientation': orientation
        }

    def start(self, display_width, display_height):
        """启动 Minicap 服务"""
        try:
            self._kill_existing_minicap()

            cmd = [
                'shell',
                'LD_LIBRARY_PATH=/data/local/tmp',
                '/data/local/tmp/minicap',
                '-P', f'{display_width}x{display_height}@{display_width}x{display_height}/0',
                '-S'
            ]
            subprocess.Popen(
                self._adb_prefix + cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            time.sleep(2)

            # ✅ 每台设备转发到各自独立的本地端口
            subprocess.run(
                self._adb_prefix + ['forward', f'tcp:{self.local_port}', 'localabstract:minicap'],
                check=True, capture_output=True
            )
            logger.info(f"[Minicap][{self.device_id}] 端口转发: localhost:{self.local_port} -> minicap")

            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('127.0.0.1', self.local_port))
            self.socket.settimeout(10.0)

            self.running = True
            self.reader_thread = threading.Thread(
                target=self._read_stream,
                daemon=True,
                name=f"minicap-{self.device_id}-{self.local_port}"  # ✅ 线程命名便于调试
            )
            self.reader_thread.start()

            self._wait_for_first_frame(timeout=10)

        except Exception as e:
            self.stop()
            raise RuntimeError(f"[Minicap][{self.device_id}] 启动失败: {e}")

    def _wait_for_first_frame(self, timeout=10):
        """等待首帧就绪"""
        start = time.time()
        while time.time() - start < timeout:
            with self.frame_lock:
                if self.latest_frame is not None:
                    logger.info(f"[Minicap][{self.device_id}] 首帧已就绪 [OK]")
                    return
            time.sleep(0.1)
        logger.warning(f"[Minicap][{self.device_id}] [警告] 等待首帧超时")

    def _read_stream(self):
        """持续读取帧数据"""
        while self.running and self.socket:
            try:
                header = self._recv_exact(4)
                frame_size = struct.unpack('<I', header)[0]

                if frame_size <= 0 or frame_size > 10 * 1024 * 1024:
                    logger.warning(f"[Minicap][{self.device_id}] [警告] 异常帧大小: {frame_size}，跳过")
                    continue

                frame_data = self._recv_exact(frame_size)

                img_array = np.frombuffer(frame_data, dtype=np.uint8)
                frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

                if frame is not None:
                    with self.frame_lock:
                        self.latest_frame = frame.copy()
                else:
                    logger.warning(f"[Minicap][{self.device_id}] [警告] JPEG 解码失败")

            except socket.timeout:
                continue
            except ConnectionError as e:
                logger.warning(f"[Minicap][{self.device_id}] 连接断开: {e}")
                break
            except Exception as e:
                logger.warning(f"[Minicap][{self.device_id}] 读取异常: {e}")
                break

    def get_frame(self):
        """获取最新帧"""
        with self.frame_lock:
            if self.latest_frame is not None:
                return self.latest_frame.copy()
        return None

    def _kill_existing_minicap(self):
        """停止设备上的 minicap 进程"""
        try:
            subprocess.run(
                self._adb_prefix + ['shell', 'pkill', '-f', 'minicap'],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            time.sleep(0.5)
        except:
            pass

    def stop(self):
        """停止服务，释放资源"""
        self.running = False
        try:
            if self.socket:
                self.socket.close()
        except:
            pass
        self._kill_existing_minicap()
        subprocess.run(
            self._adb_prefix + ['forward', '--remove', f'tcp:{self.local_port}'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        # ✅ 释放端口，允许其他实例复用
        MinicapService._release_port(self.local_port)
        logger.info(f"[Minicap][{self.device_id}] 服务已停止，释放端口: {self.local_port}")