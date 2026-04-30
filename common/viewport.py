import asyncio
import random
from enum import Enum

from common.log import get_logger
from tools.common_tools import merge_list

logger = get_logger("viewport")

_DEFAULT_SETTLE_TIME = 0.3


class Direction(Enum):
    Undefined = 0
    X = 1
    Y = 2


class Viewport:
    def __init__(self, bp, element_data, element_data_items=None,
                 item_id_list=None, direction=None, range=None,
                 edge=None, delta_len=None, camera_name=""):
        self.base_page = bp
        self.element_data = element_data
        self.element_data_items = element_data_items
        self.object_id = None
        self.position = None
        self.size = None
        self.item_id_list = item_id_list
        self.direction = direction
        self.range = range
        self.edge = edge
        self.delta_len = delta_len
        self.camera_name = camera_name
        self.settle_time = _DEFAULT_SETTLE_TIME

    @classmethod
    async def create(cls, bp, element_data, **kwargs):
        instance = cls(bp, element_data, **kwargs)

        info = await bp.get_scroll_view_info(element_data=element_data)

        instance.object_id = info.get('instanceId')
        instance.position = info.get('position')
        instance.size = info.get('size')

        if instance.element_data_items is not None:
            instance.item_id_list = await bp.get_object_id_list(
                element_data=instance.element_data_items)
        if instance.item_id_list is None:
            instance.item_id_list = info.get('contentChildrenIds') or []

        if instance.direction is None:
            horizontal = info.get('horizontal', False)
            vertical = info.get('vertical', False)
            if horizontal and vertical:
                instance.direction = Direction.Undefined
            elif horizontal:
                instance.direction = Direction.X
            elif vertical:
                instance.direction = Direction.Y
            else:
                instance.direction = Direction.Undefined

        if instance.direction == Direction.Undefined:
            instance.direction = await instance._detect_direction_by_position()

        if instance.delta_len is None:
            first_child_size = info.get('firstChildSize')
            if first_child_size:
                if instance.direction == Direction.X:
                    instance.delta_len = first_child_size[0] * 0.5
                elif instance.direction == Direction.Y:
                    instance.delta_len = first_child_size[1] * 0.5
                else:
                    instance.delta_len = 0.01
            else:
                instance.delta_len = 0.01

        if instance.edge is None:
            instance.edge = [instance.delta_len * 0.5, instance.delta_len * 0.5]

        if instance.range is None:
            instance.range = instance._compute_range()
        instance._range_shift()

        return instance

    async def _detect_direction_by_position(self):
        """item 位置兜底：当 ScrollRect 的 horizontal/vertical 都为 false 或都为 true 时，
        通过首尾子项位置推断方向。"""
        if len(self.item_id_list) < 2:
            return Direction.Undefined
        pos_start, pos_end = await asyncio.gather(
            self.base_page.get_position_by_id(object_id=self.item_id_list[0]),
            self.base_page.get_position_by_id(object_id=self.item_id_list[-1]),
        )
        if abs(pos_start[0] - pos_end[0]) > abs(pos_start[1] - pos_end[1]):
            return Direction.X
        return Direction.Y

    def _compute_range(self):
        if self.direction == Direction.Y:
            range_start = self.position[1] - self.size[1] * 0.5
            range_end = self.position[1] + self.size[1] * 0.5
        else:
            range_start = self.position[0] - self.size[0] * 0.5
            range_end = self.position[0] + self.size[0] * 0.5
        return [max(0, range_start), min(1, range_end)]

    def _range_shift(self):
        if self.edge:
            self.range[0] += self.edge[0]
            self.range[1] -= self.edge[1]
        self.range[0] = max(0, self.range[0])
        self.range[1] = min(1, self.range[1])
        if self.range[0] >= self.range[1]:
            mid = (self.range[0] + self.range[1]) * 0.5
            self.range = [mid - 0.01, mid + 0.01]
            logger.warning(
                f"_range_shift: edge 过大导致判定区域反转，"
                f"已回退到中心点附近 {self.range}")

    def _random_start_point(self):
        """在可见区域内随机取一个坐标作为滑动起点。"""
        margin = 0.1
        half_w = self.size[0] * (0.5 - margin)
        half_h = self.size[1] * (0.5 - margin)
        x = random.uniform(self.position[0] - half_w, self.position[0] + half_w)
        y = random.uniform(self.position[1] - half_h, self.position[1] + half_h)
        return [x, y]

    def _target_axis_pos(self, target_position):
        """取目标在滚动轴上的坐标分量。"""
        if self.direction == Direction.X:
            return target_position[0]
        return target_position[1]

    def _is_in_range(self, axis_val):
        return self.range[0] < axis_val < self.range[1]

    _MAX_SCROLL_ATTEMPTS = 30
    _STALE_THRESHOLD = 0.005

    async def move_delta_len(self, target_id):
        """滑动一步，让 target 靠近可见区域。

        Returns:
            None  -- 目标已在可见范围内
            (axis_val, swipe_dir) -- 目标轴坐标和滑动方向 (-1 / +1)
        """
        target_position = await self.base_page.get_position_by_id(
            object_id=target_id, locator_camera=self.camera_name)
        axis_val = self._target_axis_pos(target_position)

        if self._is_in_range(axis_val):
            return None

        edge_start, edge_end = self.range
        axis = 0 if self.direction == Direction.X else 1

        if axis_val > edge_start:
            dist_to_edge = axis_val - edge_end
            swipe_dir = -1
        else:
            dist_to_edge = edge_start - axis_val
            swipe_dir = 1

        actual_delta = min(
            self.delta_len,
            max(dist_to_edge * 0.6, self.delta_len * 0.25))

        point_start = self._random_start_point()
        point_end = list(point_start)
        point_end[axis] += swipe_dir * actual_delta

        await self.base_page.swipe_base(
            point_start=point_start, point_end=point_end,
            t=actual_delta * 4)
        return axis_val, swipe_dir

    async def move_until_appear(self, target_id, ignore_element_list=None):
        prev_axis = None
        stale_count = 0

        for _ in range(self._MAX_SCROLL_ATTEMPTS):
            result = await self.move_delta_len(target_id)

            if result is None:
                return

            cur_axis = result[0]

            if prev_axis is not None:
                if abs(cur_axis - prev_axis) < self._STALE_THRESHOLD:
                    stale_count += 1
                else:
                    stale_count = 0

            if stale_count >= 2:
                logger.warning(
                    f"move_until_appear: 目标位置连续无变化 "
                    f"(pos={cur_axis:.4f})，停止滑动")
                return

            prev_axis = cur_axis
            await self.base_page.sleep(self.settle_time)

        logger.warning(
            f"move_until_appear: 达到最大尝试次数 "
            f"{self._MAX_SCROLL_ATTEMPTS}，停止滑动")

    async def get_clickable_icon_and_position_list(self):
        icon_list = []
        position_list = []
        if self.element_data_items:
            icon_list, position_list = await asyncio.gather(
                self.base_page.get_icon_list(element_data=self.element_data_items),
                self.base_page.get_position_list(element_data=self.element_data_items),
            )
        elif self.item_id_list:
            raw_icons, raw_positions = await asyncio.gather(
                self.base_page.get_icon_list_by_id(object_id_list=self.item_id_list),
                self.base_page.get_position_list_by_id(object_id_list=self.item_id_list),
            )
            icon_list = merge_list(raw_icons)
            position_list = merge_list(raw_positions)

        clickable_icon_list = []
        clickable_position_list = []
        for i, pos in enumerate(position_list):
            axis_val = pos[1] if self.direction == Direction.Y else pos[0]
            if self.range[0] <= axis_val <= self.range[1]:
                clickable_icon_list.append(icon_list[i])
                clickable_position_list.append(pos)
        return clickable_icon_list, clickable_position_list

    async def get_clickable_index_list(self):
        position_list = []
        if self.element_data_items:
            position_list = await self.base_page.get_position_list(
                element_data=self.element_data_items)
        elif self.item_id_list:
            raw = await self.base_page.get_position_list_by_id(
                object_id_list=self.item_id_list)
            position_list = merge_list(raw)

        clickable_index_list = []
        for i, pos in enumerate(position_list):
            axis_val = pos[1] if self.direction == Direction.Y else pos[0]
            if self.range[0] <= axis_val <= self.range[1]:
                clickable_index_list.append(i)
        return clickable_index_list

    async def change_item(self, element_data=None, object_id_list=None):
        if object_id_list is not None:
            self.item_id_list = object_id_list
            return
        self.item_id_list = await self.base_page.get_object_id_list(
            element_data=element_data)


if __name__ == "__main__":
    pass
