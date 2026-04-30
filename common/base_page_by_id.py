from __future__ import annotations
import random

from common import rpc_method_request
from common.error import FindNoElementError, PluralElementError
from common.log import get_logger
from tools.common_tools import merge_list

logger = get_logger("base_page_by_id")

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from common.base_page import BasePageMain
class BasePageByIdMixin:
    self: BasePageMain  # 仅供类型检查，运行时不生效
    """通过 object_id / object_id_list 查询和设置元素属性的方法集合。

    由 BasePageMain 继承后即可直接使用，运行时 self.server 等属性
    来自 BasePageMain 实例。
    """

    @staticmethod
    def is_single_element(element_list: list):
        """保证元素列表中的元素数量是1，防止取单一元素时取到多个或没取到。"""
        if len(element_list) == 0:
            raise FindNoElementError("FindNoElement")
        elif len(element_list) > 1:
            raise PluralElementError("PluralElement")

    # ---- exist ----

    async def exist_by_id(self, object_id, offspring_path=""):
        if await self.get_offspring_id_list_by_id(object_id=object_id, offspring_path=offspring_path):
            return True
        return False

    # ---- offspring id ----

    async def get_offspring_id_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_offspring_id_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_offspring_id_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_offspring_id_by_id(self, object_id, offspring_path=""):
        offspring_id_list = await self.get_offspring_id_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(offspring_id_list)
        return offspring_id_list[0]

    # ---- parent id ----

    async def get_parent_id_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_parent_id_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_parent_id_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_parent_id_by_id(self, object_id, offspring_path=""):
        parent_id_list = await self.get_parent_id_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(parent_id_list)
        return parent_id_list[0]

    # ---- text ----

    async def get_text_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_text_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_text_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_text_by_id(self, object_id, offspring_path=""):
        text_list = await self.get_text_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(text_list)
        return text_list[0]

    async def set_text_list_by_id(self, object_id=0, object_id_list=None, offspring_path="", text=""):
        if object_id_list is not None:
            await rpc_method_request.set_text_by_id(self.server, object_id_list, offspring_path, text)
            return
        await self.set_text_list_by_id(object_id_list=[object_id], offspring_path=offspring_path, text=text)

    async def set_text_by_id(self, object_id, offspring_path="", text=""):
        await self.set_text_list_by_id(object_id=object_id, offspring_path=offspring_path, text=text)

    # ---- icon ----

    async def get_icon_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_img_name_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_icon_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_icon_by_id(self, object_id, offspring_path=""):
        icon_list = await self.get_icon_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(icon_list)
        return icon_list[0]

    # ---- name ----

    async def get_name_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_name_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_name_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_name_by_id(self, object_id, offspring_path=""):
        name_list = await self.get_name_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(name_list)
        return name_list[0]

    # ---- slider value ----

    async def get_slider_value_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_slider_value_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_slider_value_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_slider_value_by_id(self, object_id, offspring_path=""):
        slider_value_list = await self.get_slider_value_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(slider_value_list)
        return slider_value_list[0]

    # ---- size ----

    async def get_size_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_size_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_size_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_size_by_id(self, object_id, offspring_path=""):
        size_list = await self.get_size_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(size_list)
        return size_list[0]

    # ---- toggle is on ----

    async def get_toggle_is_on_list_by_id(self, object_id=0, object_id_list=None, offspring_path=""):
        if object_id_list is not None:
            return await rpc_method_request.get_toggle_is_on_by_id(self.server, object_id_list, offspring_path)
        return (await self.get_toggle_is_on_list_by_id(object_id_list=[object_id], offspring_path=offspring_path))[0]

    async def get_toggle_is_on_by_id(self, object_id, offspring_path=""):
        toggle_is_on_list = await self.get_toggle_is_on_list_by_id(object_id=object_id, offspring_path=offspring_path)
        self.is_single_element(toggle_is_on_list)
        return toggle_is_on_list[0]

    # ---- position (特殊：带 focus / locator_camera) ----

    async def get_position_list_by_id(self, object_id=0, object_id_list=None, offspring_path="",
                                      focus: list[float] = None, locator_camera=""):
        if focus is None:
            focus = [0.5, 0.5]
        if object_id_list is not None:
            return await rpc_method_request.get_position_by_id(
                self.server, object_id_list, offspring_path, focus, locator_camera)
        return (await self.get_position_list_by_id(
            object_id_list=[object_id], offspring_path=offspring_path,
            focus=focus, locator_camera=locator_camera))[0]

    async def get_position_by_id(self, object_id, offspring_path="",
                                 focus: list[float] = None, locator_camera=""):
        position_list = await self.get_position_list_by_id(
            object_id=object_id, offspring_path=offspring_path,
            focus=focus, locator_camera=locator_camera)
        self.is_single_element(position_list)
        return position_list[0]

    # ============================================================
    # by_id 动作方法
    # ============================================================

    async def press_by_id(self, object_id, duration=2.0, offspring_path="",
                          locator_camera="", ignore_element_list=None, focus=None):
        """定位元素后按压 duration 秒。"""
        await self.clear_popup(ignore_element_list)
        position_list = await self.get_position_list_by_id(
            object_id=object_id, offspring_path=offspring_path,
            focus=focus, locator_camera=locator_camera)
        self.is_single_element(position_list)
        await self.press_position_base(position=position_list[0], duration=duration)
        return position_list[0]

    async def click_by_id(self, object_id, offspring_path="", locator_camera="",
                          ignore_element_list=None, focus=None):
        """定位元素后点击。"""
        logger.info(f"click_by_id 点击 object_id={object_id}")
        return await self.press_by_id(
            object_id=object_id, duration=0, offspring_path=offspring_path,
            locator_camera=locator_camera, ignore_element_list=ignore_element_list,
            focus=focus)

    async def click_plural_by_id(self, object_id=0, object_id_list=None, offspring_path="",
                                 focus=None, index=None, viewport=None,
                                 element_viewport=None, viewport_direction=None,
                                 viewport_range=None, viewport_edge=None, delta_len=None,
                                 locator_camera="", ignore_element_list=None):
        """通过 object_id 点击一堆物体中的其中一个。"""
        if object_id != 0:
            await self.click_plural_by_id(
                object_id_list=[object_id], offspring_path=offspring_path,
                index=index, viewport=viewport, element_viewport=element_viewport,
                viewport_direction=viewport_direction, viewport_range=viewport_range,
                viewport_edge=viewport_edge, delta_len=delta_len,
                locator_camera=locator_camera, focus=focus,
                ignore_element_list=ignore_element_list)
            return

        if element_viewport:
            from common.viewport import Viewport
            viewport = await Viewport.create(
                self, element_data=element_viewport,
                item_id_list=object_id_list, direction=viewport_direction,
                range=viewport_range, edge=viewport_edge,
                delta_len=delta_len, camera_name=locator_camera)

        if viewport:
            if index is None:
                index = random.randint(0, len(viewport.item_id_list) - 1)
            if index < 0:
                index = len(viewport.item_id_list) + index
            target_id = viewport.item_id_list[index]
            await viewport.move_until_appear(target_id=target_id, ignore_element_list=ignore_element_list)

        position_list = await self.get_position_list_by_id(
            object_id_list=object_id_list, offspring_path=offspring_path,
            focus=focus, locator_camera=locator_camera)
        position_list = merge_list(position_list)

        if index is None:
            index = random.randint(0, len(position_list) - 1)
        if index < 0:
            index = len(position_list) + index

        await self.click_position(position=position_list[index], ignore_element_list=ignore_element_list)

    async def click_outside_by_id(self, object_id, locator_camera="", ignore_element_list=None):
        """通过 object_id 点击元素外部区域。"""
        await self.clear_popup(ignore_element_list=ignore_element_list)
        click_result = await self.click_outside_safe_by_id(
            object_id=object_id, locator_camera=locator_camera)
        if not click_result:
            raise FindNoElementError(f"object_id{object_id}不存在")

    async def click_outside_safe_by_id(self, object_id, locator_camera=""):
        """通过 object_id 点击元素外部区域（不清除弹窗）。"""
        position_list = await self.get_position_list_by_id(
            object_id=object_id, locator_camera=locator_camera)
        size_list = await self.get_size_list_by_id(object_id=object_id)
        if not position_list:
            logger.warning("点击目标不存在")
            return False
        if not size_list:
            logger.warning("点击目标不存在")
            return False
        position = position_list[0]
        size = size_list[0]

        margin = 0.01
        left_gap = position[0] - 0.5 * size[0]
        right_gap = 1 - position[0] - 0.5 * size[0]
        up_gap = position[1] - 0.5 * size[1]
        down_gap = 1 - position[1] - 0.5 * size[1]

        areas = {
            "left": {"area": left_gap,
                     "position": [(position[0] - 0.5 * size[0] - margin) * 0.5,
                                  position[1]]},
            "right": {"area": right_gap,
                      "position": [(position[0] + 0.5 * size[0] + margin + 1) * 0.5,
                                   position[1]]},
            "up": {"area": up_gap,
                   "position": [position[0],
                                (position[1] - 0.5 * size[1] - margin) * 0.5]},
            "down": {"area": down_gap,
                     "position": [position[0],
                                  (position[1] + 0.5 * size[1] + margin + 1) * 0.5]},
        }

        best_direction = max(areas, key=lambda k: areas[k]["area"])
        position_out_side = list(areas[best_direction]["position"])
        await self.press_position_base(position_out_side, duration=0)
        logger.info(f"click_outside_safe_by_id object_id={object_id}, 位置={position_out_side}, 方向={best_direction}")
        return True

    async def click_safe_by_id(self, object_id, offspring_path="",
                               focus=None, locator_camera=""):
        """通过 object_id 安全点击（元素不存在时不报错）。"""
        position_list = await self.get_position_list_by_id(
            object_id=object_id, offspring_path=offspring_path,
            focus=focus, locator_camera=locator_camera)
        if not position_list:
            return
        try:
            r = random.randint(0, len(position_list) - 1)
            await self.press_position_base(position=position_list[r], duration=0)
        except:
            pass

    async def swipe_by_id(self, object_id, point_end=None, t=0.5,
                          ignore_element_list=None, focus=None, locator_camera=""):
        """通过 object_id 定位元素作为滑动起点，清除弹窗后滑动。"""
        await self.clear_popup(ignore_element_list)
        point_start = await self.get_position_by_id(
            object_id=object_id, focus=focus, locator_camera=locator_camera)
        await self.swipe_base(
            point_start=point_start, point_end=point_end, t=t)

    async def get_element_shot_by_id(self, object_id, offspring_path=""):
        """通过 object_id 截取指定元素。"""
        ui_x, ui_y = await self.get_position_by_id(
            object_id=object_id, offspring_path=offspring_path)
        ui_w, ui_h = await self.get_size_by_id(
            object_id=object_id, offspring_path=offspring_path)
        ui_x, ui_y = int(ui_x * self.screen_w), int(ui_y * self.screen_h)
        ui_w, ui_h = int(ui_w * self.screen_w), int(ui_h * self.screen_h)
        img = await self.get_screen_shot(ui_x, ui_y, ui_w, ui_h)
        return img

    async def ray_input_by_id(self, kind, object_id, offspring_path=""):
        """通过 object_id 进行光线操作。"""
        await rpc_method_request.ray_input_by_id(
            self.server, [object_id], offspring_path, kind)
