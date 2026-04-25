class BaseDeviceDriver:
    def __init__(self, base_page):
        self.base_page = base_page  # 引用 BasePage 以便访问通用属性
        self.screen_w = 0
        self.screen_h = 0

    async def initialize(self):
        pass

    async def connect_close(self):
        pass

    async def press_position(self, position: list[float], duration: float):
        pass

    async def swipe(self, point_start: list[float], point_end: list[float], duration: float):
        pass

    async def get_screen_shot(self, x: float, y: float, w: float, h: float):
        pass

    def start_video_recording(self, output_path: str):
        """开始视频录制，output_path 为本地 mp4 文件路径"""
        pass

    def stop_video_recording(self) -> str | None:
        """停止视频录制，返回保存的视频文件路径（或 None）"""
        pass