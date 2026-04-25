# common/step_recorder.py
from common.log import get_logger
logger = get_logger("step_recorder")
import datetime
from pathlib import Path
import cv2


class StepRecorder:
    """步骤跟踪与截图录制。"""

    def __init__(self, screenshots_dir: Path):
        self.screenshots_dir = Path(screenshots_dir)
        self.screenshots_dir.mkdir(parents=True, exist_ok=True)

        self._current_step = None
        self._current_step_key = None
        self.step_execution_count = {}
        self.step_screenshot_count = {}
        self.screenshot_counter = 0

    @property
    def current_step(self):
        return self._current_step

    def set_step(self, step_num):
        self._current_step = step_num
        if step_num not in self.step_execution_count:
            self.step_execution_count[step_num] = 0
        self.step_execution_count[step_num] += 1
        self._current_step_key = (step_num, self.step_execution_count[step_num])
        self.step_screenshot_count[self._current_step_key] = 0

    def _get_next_screenshot_index(self) -> int:
        if self._current_step_key not in self.step_screenshot_count:
            self.step_screenshot_count[self._current_step_key] = 0
        self.step_screenshot_count[self._current_step_key] += 1
        return self.step_screenshot_count[self._current_step_key]

    def save_img(self, img, img_name: str = "", notes: str = ""):
        is_success, im_buf_arr = cv2.imencode(".jpg", img)
        if not is_success:
            return
        if img_name:
            im_buf_arr.tofile(img_name)
            return

        prefix = ""
        if self._current_step is not None:
            step_num = self._current_step
            execution_count = self.step_execution_count.get(step_num, 1)
            screenshot_index = self._get_next_screenshot_index()
            prefix = f"{step_num:03d}_{execution_count:02d}_{screenshot_index:02d}_"

        self.screenshot_counter += 1

        if notes:
            filename = f"NO{self.screenshot_counter:03d}_{prefix}{notes}.jpg"
        else:
            timestamp = datetime.datetime.now().strftime("%H%M%S%f")
            filename = f"NO{self.screenshot_counter:03d}_{prefix}{timestamp}.jpg"

        full_path = self.screenshots_dir / filename
        im_buf_arr.tofile(str(full_path))

    @staticmethod
    def draw_marker(img, center_coordinates: list):
        img_h, img_w = img.shape[:2]
        center = [int(center_coordinates[0] * img_w), int(center_coordinates[1] * img_h)]
        color = (0, 255, 0)
        cv2.circle(img, center=center, radius=5, color=color, thickness=-1)
        cv2.circle(img, center=center, radius=20, color=color, thickness=2)
        cv2.circle(img, center=center, radius=30, color=color, thickness=2)

    @staticmethod
    def draw_viewport_rect(img, viewport: dict, color=(0, 255, 0), thickness: int = 3):
        """在全屏截图上绘制归一化视口矩形（x,y 为中心点，w,h 为宽高）。"""
        img_h, img_w = img.shape[:2]
        cx, cy = viewport["x"], viewport["y"]
        half_w, half_h = viewport["w"] / 2, viewport["h"] / 2
        x1 = int((cx - half_w) * img_w)
        y1 = int((cy - half_h) * img_h)
        x2 = int((cx + half_w) * img_w)
        y2 = int((cy + half_h) * img_h)
        cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)