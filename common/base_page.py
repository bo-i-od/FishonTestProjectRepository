import asyncio
import base64
import os
import random
import time
import zlib
from pathlib import Path

import cv2
import numpy as np

from common import rpc_method_request
from common.error import FindNoElementError, PluralElementError, InvalidOperationError
from common.log import get_logger
from common.step_recorder import StepRecorder
from common.viewport import Viewport

from configs.panel_data import PANEL_DATA_MAP, PanelType

from configs.panel_data import PanelData
from configs.path_config import DEFAULT_CAMERA_CONFIG
from tools.common_tools import merge_list

logger = get_logger("base_page")


class BasePageMain:
    def __init__(self, server, device_type="pc", device_id=None, is_record=False, session_dir=None):
        self.server = server

        self.device_type = device_type

        # 设备号
        self.device_id = device_id

        # 控制是否截图
        self.is_record = is_record

        # 获取父目录
        file_path = os.path.join(os.path.dirname(__file__))
        self.root_dir = os.path.abspath(os.path.dirname(file_path))

        self.test_name = ""

        # 会话目录和截图计数器
        self.session_dir = Path(session_dir) if session_dir else None
        # 如果有 session_dir，创建 screenshots 子目录
        if self.session_dir:
            screenshots_dir = self.session_dir / "screenshots"
        else:
            screenshots_dir = Path(self.root_dir) / "logs" / "common"
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        # 步骤跟踪与截图录制
        self.recorder = StepRecorder(screenshots_dir)

        self.playback_delay = 1.0
        self.ios_wda_project = None

        self.camera_config_list: list[dict] = list(DEFAULT_CAMERA_CONFIG)

        self.panel_home_name_list = ["UILevelHUD._main", "UILevelHUD"]
        self.directory_ui = "ui_layer/view/"
        self.directory_3d = "root/scene/"

        # 实例化对应的驱动
        if self.device_type == "android":
            from common.driver.android_driver import AndroidDriver
            self.driver = AndroidDriver(self)
        elif self.device_type == "harmony":
            from common.driver.harmony_driver import HarmonyDriver
            self.driver = HarmonyDriver(self)
        elif self.device_type == "ios":
            from common.driver.ios_driver import IOSDriver
            self.driver = IOSDriver(self)
        elif self.device_type == "pc":
            from common.driver.pc_driver import PCDriver

            self.driver = PCDriver(self)
        else:
            logger.warning(f"device_type={self.device_type}是未知设备类型")

        # 开启倍速后的默认加速倍率
        self.time_scale_default = 5

        self.panel_data_waiting_list = []

        # BasePageExt(self)

    async def initialize(self):
        """
        初始化驱动和设备连接。
        包括通过 camera_config_list 同步相机注册表、连接设备或启动浏览器。
        """
        for cfg in self.camera_config_list:
            await rpc_method_request.set_camera(
                self.server, cfg["path_node"], cfg["path_camera"], cfg["camera_type"]
            )
            await self.sleep(0.1)

        # 建立连接
        await self.driver.initialize()

    async def connect_close(self):
        if self.server:
            await self.server.close()
        await self.driver.connect_close()

    @staticmethod
    def panel_data_list_to_panel_element_data_list(panel_data_list: list[PanelData]):
        """
        将 UIData 对象列表转换为 element_data 字典列表。

        :param panel_data_list: UIData 对象列表
        :return: element_data 字典列表
        """
        panel_element_data_list = []
        for panel_data in panel_data_list:
            element_data = panel_data.element_data
            panel_element_data_list.append(element_data)
        return panel_element_data_list

    @staticmethod
    def log(*msg):
        """
        打印日志信息到控制台。

        :param msg: 任意数量的日志内容
        """
        logger.info(" ".join(str(m) for m in msg))

    # 判断列表是不是长度为1，不为1会报错
    @staticmethod
    def is_single_element(element_list: list):
        """函数功能简述
            保证元素列表中的元素数量是1
            防止取单一元素时，取到多个或没取到

        参数:
            element_list: 获取到的元素组成的列表
        """
        if len(element_list) == 0:
            raise FindNoElementError("FindNoElement")
        elif len(element_list) > 1:
            raise PluralElementError("PluralElement")

    @staticmethod
    def _prepare_element_data_list(element_data_list: list[dict], offspring_path: str = "", **kwargs) -> list[dict]:
        """处理偏移路径并注入额外参数（不修改原始 dict）。
        值为 None 或空字符串的 kwargs 会被跳过；dict 中已有的字段不会被覆盖。"""
        params = {k: v for k, v in kwargs.items() if v is not None and v != ""}
        if not offspring_path and not params:
            return element_data_list
        result = []
        for ed in element_data_list:
            changes = {}
            if offspring_path:
                changes["locator"] = ed["locator"] + '/' + offspring_path
            for k, v in params.items():
                if k not in ed:
                    changes[k] = v
            result.append({**ed, **changes} if changes else ed)
        return result

    async def exist(self, object_id=0, element_data=None, offspring_path=""):
        """函数功能简述
            判断元素是否存在

        参数:
            object_id和element_data输入其中的一个
            object_id: 优先object_id定位元素
            element_data: 元素定位信息定位
            offspring_path: 偏移路径

        返回:
            存在返回True
            不存在返回False
        """
        if object_id != 0:
            if await self.get_offspring_id_list(object_id=object_id, offspring_path=offspring_path):
                return True
            return False

        if await self.get_offspring_id_list(element_data=element_data, offspring_path=offspring_path):
            return True
        return False

    # 得到元素的Instance Id列表
    async def get_object_id_list(self, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        """函数功能简述
            获取元素id

        参数:
            element_data和element_data_list输入其中一个
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入element_data_list时，返回list[list[int]]
            输入element_data时，返回list[int]
        """
        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_object_id(self.server, element_data_copy_list)

        return (await self.get_object_id_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    # 得到元素的Instance Id
    async def get_object_id(self, element_data: dict, offspring_path=""):
        """函数功能简述
            获取元素id

        参数:
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            object_id_list有且只有一个元素时，返回int
        """
        object_id_list = await self.get_object_id_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(object_id_list)
        return object_id_list[0]

    # 得到后代的Instance Id
    async def get_offspring_id_list(self, offspring_path, object_id=0, object_id_list=None, element_data=None,
                              element_data_list: list = None):
        """函数功能简述
            根据偏移路径获取元素id

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: object_id组成的list
            element_data: 元素定位信息
            element_data_list: element_data组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[int]
            输入object_id_list或element_data_list时，返回list[list[int]]
        """
        if object_id_list is not None:
            return await rpc_method_request.get_offspring_id_by_id(self.server, object_id_list, offspring_path)

        if object_id != 0:
            return (await self.get_offspring_id_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await self.get_object_id_list(element_data_list=element_data_copy_list)

        return (await self.get_object_id_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_offspring_id(self, offspring_path, object_id=0, element_data=None):
        """函数功能简述
            根据偏移路径获取元素id

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            object_id_list有且只有一个元素时，返回int
        """
        offspring_id_list = await self.get_offspring_id_list(object_id=object_id, element_data=element_data,
                                                       offspring_path=offspring_path)
        self.is_single_element(offspring_id_list)
        return offspring_id_list[0]

    # 得到父节点
    async def get_parent_id_list(self, object_id=0, object_id_list=None, element_data=None, element_data_list: list = None,
                           offspring_path=""):
        """函数功能简述
            定位元素后取元素的父节点id

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[int]
            输入object_id_list或element_data_list时，返回list[list[int]]
        """
        if object_id_list is not None:
            return await rpc_method_request.get_parent_id_by_id(self.server, object_id_list, offspring_path)

        if object_id != 0:
            return (await self.get_parent_id_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_parent_id(self.server, element_data_copy_list)

        return (await self.get_parent_id_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_parent_id(self, object_id=0, element_data=None, offspring_path=""):
        """函数功能简述
            定位元素后取元素的父节点id

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            parent_id_list有且只有一个元素时，返回int
        """
        if object_id != 0:
            parent_id_list = await self.get_parent_id_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(parent_id_list)
            return parent_id_list[0]

        parent_id_list = await self.get_parent_id_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(parent_id_list)
        return parent_id_list[0]

    # 获得文本
    async def get_text_list(self, object_id=0, object_id_list: list = None, element_data: dict = None,
                      element_data_list: list = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素文本组件的值

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[str]
            输入object_id_list或element_data_list时，返回list[list[str]]
        """
        if object_id_list is not None:
            return await rpc_method_request.get_text_by_id(self.server, object_id_list, offspring_path)

        if object_id != 0:
            return (await self.get_text_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_text(self.server, element_data_copy_list)

        return (await self.get_text_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_text(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素文本组件的值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            text_list有且只有一个元素时，返回str
        """
        if object_id != 0:
            text_list = await self.get_text_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(text_list)
            return text_list[0]

        text_list = await self.get_text_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(text_list)
        return text_list[0]

    # 修改文本
    async def set_text_list(self, object_id=0, object_id_list: list = None, element_data: dict = None,
                      element_data_list: list = None, text="", offspring_path=""):
        """函数功能简述
            定位元素后设元素文本组件的值

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            None
        """
        if object_id_list is not None:
            await rpc_method_request.set_text_by_id(self.server, object_id_list, offspring_path, text)
            return

        if object_id != 0:
            await self.set_text_list(object_id_list=[object_id], offspring_path=offspring_path, text=text)
            return

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            await rpc_method_request.set_text(self.server, element_data_copy_list, text)
            return

        await self.set_text_list(element_data_list=[element_data], text=text, offspring_path=offspring_path)

    async def set_text(self, object_id: int = 0, element_data: dict = None, text="", offspring_path=""):
        """函数功能简述
            定位元素后设元素文本组件的值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            None
        """
        if object_id != 0:
            await self.set_text_list(object_id=object_id, offspring_path=offspring_path, text=text)
            return

        await self.set_text_list(element_data=element_data, text=text, offspring_path=offspring_path)

    # 获取图标名
    async def get_icon_list(self, object_id=0, object_id_list: list = None, element_data: dict = None,
                      element_data_list: list = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素图标组件的Sprite名

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[str]
            输入object_id_list或element_data_list时，返回list[list[str]]
        """
        if object_id_list is not None:
            res = await rpc_method_request.get_img_name_by_id(self.server, object_id_list, offspring_path)
            return res

        if object_id != 0:
            return (await self.get_icon_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            res = await rpc_method_request.get_img_name(self.server, element_data_copy_list)
            return res

        return (await self.get_icon_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_icon(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素图标组件的Sprite名

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            icon_list有且只有一个元素时，返回str
        """
        if object_id != 0:
            icon_list = await self.get_icon_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(icon_list)
            icon = icon_list[0]
            return icon

        icon_list = await self.get_icon_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(icon_list)
        return icon_list[0]

    # 获取节点名称
    async def get_name_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
                      element_data_list: list = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素图标组件的Sprite名

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[str]
            输入object_id_list或element_data_list时，返回list[list[str]]
        """

        # 输入object_id_list的情况，直接调用rpc
        if object_id_list is not None:
            return await rpc_method_request.get_name_by_id(self.server, object_id_list, offspring_path)

        # 输入object_id的情况，将object_id加上[]转为object_id_list
        if object_id != 0:
            return (await self.get_name_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        # 输入element_data_list的情况，直接调用rpc
        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_name(self.server, element_data_copy_list)

        # 输入element_data的情况,将element_data加[]转为element_data_list
        return (await self.get_name_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_name(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素名

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            name_list有且只有一个元素时，返回str
         """
        if object_id != 0:
            name_list = await self.get_name_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(name_list)
            return name_list[0]

        name_list = await self.get_name_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(name_list)
        return name_list[0]

    # 获取滑条值，值在0~1
    async def get_slider_value_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
                              element_data_list: list = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素slider组件的值

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[float]
            输入object_id_list或element_data_list时，返回list[list[float]]
        """
        if object_id_list is not None:
            return await rpc_method_request.get_slider_value_by_id(self.server, object_id_list, offspring_path)

        if object_id != 0:
            return (await self.get_slider_value_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_slider_value(self.server, element_data_copy_list)

        return (await self.get_slider_value_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    # 获取到的滑条值是float类型，值在0~1
    async def get_slider_value(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素slider组件的值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            slider_value_list有且只有一个元素时，返回float
            值在0~1
         """
        if object_id != 0:
            slider_value_list = await self.get_slider_value_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(slider_value_list)
            return slider_value_list[0]

        slider_value_list = await self.get_slider_value_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(slider_value_list)
        return slider_value_list[0]

    # 获取下拉列表当前值
    async def get_dropdown_value(self, element_data):
        """函数功能简述
            定位元素后取元素dropdown组件的值

        参数:
            element_data: 元素定位信息

        返回:
            slider_value_list有且只有一个元素时，返回int
            值是自然数
         """
        dropdown_value_list = await rpc_method_request.get_dropdown_value(self.server, [element_data])
        self.is_single_element(dropdown_value_list)
        return dropdown_value_list[0]

    async def set_dropdown_value(self, element_data, index):
        """函数功能简述
            定位元素后设元素dropdown组件的值

        参数:
            element_data: 元素定位信息

        返回:
            None
         """
        await rpc_method_request.set_dropdown_value(self.server, [element_data], index)

    # 获取元素尺寸
    async def get_size_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
                      element_data_list: list = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素的width和height值

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[[float, float]]
            输入object_id_list或element_data_list时，返回list[list[[float, float]]]
        """
        if object_id_list is not None:
            return await rpc_method_request.get_size_by_id(self.server, object_id_list, offspring_path)

        if object_id != 0:
            return (await self.get_size_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_size(self.server, element_data_copy_list)

        return (await self.get_size_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_size(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素的width和height值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            size_list有且只有一个元素时，返回[float, float]
            width和height值在0~1
         """
        if object_id != 0:
            size_list = await self.get_size_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(size_list)
            return size_list[0]

        size_list = await self.get_size_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(size_list)
        return size_list[0]

    # 获取勾选状态
    async def get_toggle_is_on_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
                              element_data_list: list = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素toggle组件的IsOn

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[bool]
            输入object_id_list或element_data_list时，返回list[list[bool]]
        """
        if object_id_list is not None:
            return await rpc_method_request.get_toggle_is_on_by_id(self.server, object_id_list, offspring_path)

        if object_id != 0:
            return (await self.get_toggle_is_on_list(object_id_list=[object_id], offspring_path=offspring_path))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(element_data_list, offspring_path)
            return await rpc_method_request.get_toggle_is_on(self.server, element_data_copy_list)

        return (await self.get_toggle_is_on_list(element_data_list=[element_data], offspring_path=offspring_path))[0]

    async def get_toggle_is_on(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            定位元素后取元素toggle组件的IsOn

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            toggle_is_on_list有且只有一个元素时，返回bool
        """
        if object_id != 0:
            toggle_is_on_list = await self.get_toggle_is_on_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(toggle_is_on_list)
            return toggle_is_on_list[0]

        toggle_is_on_list = await self.get_toggle_is_on_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(toggle_is_on_list)
        return toggle_is_on_list[0]

    # 获取位置
    async def get_position_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
                                element_data_list: list = None, offspring_path="",focus: list[float] = None, locator_camera=""):
        """函数功能简述
            定位元素后取元素的position值

        参数:
            object_id, object_id_list, element_data, element_data_list输入其中一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径

        返回:
            输入object_id或element_data时，返回list[[float, float]]
            输入object_id_list或element_data_list时，返回list[list[[float, float]]]
        """
        if focus is None:
            focus = [0.5, 0.5]

        if object_id_list is not None:
            return await rpc_method_request.get_position_by_id(self.server, object_id_list, offspring_path, locator_camera)

        if object_id != 0:
            return (await self.get_position_list(object_id_list=[object_id], offspring_path=offspring_path, locator_camera=locator_camera))[0]

        if element_data_list is not None:
            element_data_copy_list = self._prepare_element_data_list(
                element_data_list, offspring_path, focus=focus, locator_camera=locator_camera)
            return await rpc_method_request.get_position(self.server, element_data_copy_list)

        return (await self.get_position_list(element_data_list=[element_data], offspring_path=offspring_path,
                                             focus=focus, locator_camera=locator_camera))[0]

    async def get_position(self, object_id: int = 0, element_data: dict = None, offspring_path="", locator_camera=""):
        """函数功能简述
            定位元素后取元素的position值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            position_list有且只有一个元素时，返回[float, float]
            float值在0~1，以屏幕左上角作为原点

        """
        """
               (0, 0)    (0.5, 0)   (1, 0)
                      ______ ______
                     |      |      |
             (0, 0.5)|______|______|(1, 0.5)
                     |      |      |
                     |______|______|
               (0, 1)    (0.5, 1)   (1, 1)
        """
        if object_id != 0:
            position_list = await self.get_position_list(object_id=object_id, offspring_path=offspring_path, locator_camera=locator_camera)
            self.is_single_element(position_list)
            return position_list[0]

        position_list = await self.get_position_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(position_list)
        return position_list[0]

    # 元素长按
    async def press(self, object_id: int = 0, element_data: dict = None, duration: float = 2.0, offspring_path=""):
        """函数功能简述
            定位元素后取元素的position值
            取到position值后，按压该位置duration秒

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径
            duration: 按压时长（默认值为2s
         """
        position = await self.get_position(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        await self.press_position(position=position, duration=duration)

    # 位置长按
    async def press_position(self, position, duration: float = 2.0, ignore_element_list=None):
        """函数功能简述
                    按压position位置duration秒

                参数:
                    object_id和element_data输入其中的一个
                    object_id: 元素id
                    element_data: 元素定位信息
                    offspring_path: 偏移路径
                    duration: 按压时长（默认值为2s）
                 """
        await self.clear_popup(ignore_element_list)
        await self.press_position_base(position=position, duration=duration)

        # 位置点击
        # position=[x,y]
        # 0<=x<=1, 0<=y<=1

    async def press_position_base(self, position: list[float], duration: float = 2.0):
        """函数功能简述
            点击position处
            self.record=True时，每次点击前会进行截图
        参数:
            position[float, float]
        """
        await self.waiting_reconnect()
        if not (0 <= position[0] <= 1) or not (0 <= position[1] <= 1):
            raise InvalidOperationError('Click position out of screen. pos={}'.format(repr(position)))

        # 点击前进行截图保存
        if self.is_record:
            img = await self.get_full_screen_shot()
            StepRecorder.draw_marker(img=img, center_coordinates=[position[0], position[1]])
            self.recorder.save_img(img=img, notes=f"press{position}{duration}s")
        await self.driver.press_position(position, duration)

    def draw_circle(self, img, center_coordinates):
        """函数功能简述
            在img图像上以center_coordinates为圆心画圆
        参数:
            img: 输入图片
            center_coordinates: 圆心
        """
        center_coordinates = (int(center_coordinates[0] * self.screen_w), int(center_coordinates[1] * self.screen_h))
        # 定义圆形的半径
        radius0 = 20
        radius1 = 30
        # 定义圆形的颜色 (B, G, R)
        color = (0, 0, 255)
        # 定义圆形的厚度; -1表示圆形将会被填充，默认值是1
        thickness = 2
        # 在图片上画一个圆形
        cv2.circle(img, center_coordinates, 5, color, -1)
        cv2.circle(img, center_coordinates, radius0, color, thickness)
        cv2.circle(img, center_coordinates, radius1, color, thickness)

    async def click_position(self, position, ignore_element_list=None):
        """
        点击屏幕指定位置 (归一化坐标)。
        点击前会自动尝试清理弹窗。

        :param position: [x, y] 归一化坐标
        :param ignore_element_list: 清理弹窗时忽略的 UI 列表(选填)
        """
        await self.press_position(position=position, duration=0, ignore_element_list=ignore_element_list)

        # 元素点击

    async def click_element(self, object_id: int = 0, element_data: dict = None, offspring_path="", locator_camera="", ignore_element_list=None, focus=None):
        """函数功能简述
            定位元素后取元素的position值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径
            ignore_element_list: 需要忽略清除的弹窗
            focus: 元素锚点，用于计算元素中心位置

        返回:
            position_list有且只有一个元素时，返回[float, float]
        """
        logger.info(f"click_element 点击 {element_data} {focus}")
        position = await self.press_element(duration=0, object_id=object_id, element_data=element_data,
                                            offspring_path=offspring_path, focus=focus,
                                            locator_camera=locator_camera, ignore_element_list=ignore_element_list)
        return position

    async def press_element(self, object_id: int = 0, element_data: dict = None, duration: float = 2.0, offspring_path="", locator_camera="", ignore_element_list=None, focus=None):
        """函数功能简述
            定位元素后取元素的position值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径
            ignore_element_list: 需要忽略清除的弹窗
            focus: 元素锚点，用于计算元素中心位置

        返回:
            position_list有且只有一个元素时，返回[float, float]
        """
        await self.clear_popup(ignore_element_list)
        position_list = await self.get_position_list(object_id=object_id, element_data=element_data, offspring_path=offspring_path, focus=focus, locator_camera=locator_camera)
        self.is_single_element(position_list)
        await self.press_position_base(position=position_list[0], duration=duration)
        return position_list[0]

    async def click_object_of_plural_objects(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path="", index=None, viewport: Viewport = None, element_viewport: dict = None, viewport_direction=None, viewport_range=None, viewport_edge=None, delta_len=None, locator_camera="", ignore_element_list=None):
        """函数功能简述
            点击一堆物体中的其中一个
        """
        if object_id != 0:
            await self.click_object_of_plural_objects(object_id_list=[object_id], offspring_path=offspring_path,
                                                      index=index, viewport=viewport, element_viewport=element_viewport,
                                                      viewport_direction=viewport_direction, viewport_range=viewport_range,
                                                      viewport_edge=viewport_edge, delta_len=delta_len,
                                                      locator_camera=locator_camera, ignore_element_list=ignore_element_list)
            return
        if element_data is not None:
            await self.click_object_of_plural_objects(element_data_list=[element_data], offspring_path=offspring_path,
                                                      index=index, viewport=viewport, element_viewport=element_viewport,
                                                      viewport_direction=viewport_direction, viewport_range=viewport_range,
                                                      viewport_edge=viewport_edge, delta_len=delta_len,
                                                      locator_camera=locator_camera, ignore_element_list=ignore_element_list)
            return

        # 如果传入viewport的定位就得到viewport
        if element_viewport:
            viewport = Viewport(self, element_viewport=element_viewport, element_item_list=element_data_list[0], item_id_list=object_id_list, viewport_direction=viewport_direction, viewport_range=viewport_range, viewport_edge=viewport_edge, delta_len=delta_len, locator_camera=locator_camera)

        # 如果有viewport就挪动到元素出现
        if viewport:

            if index is None:
                index = random.randint(0, len(viewport.item_id_list) - 1)
            if index < 0:
                index = len(viewport.item_id_list) + index
            target_id = viewport.item_id_list[index]
            await viewport.move_until_appear(target_id=target_id, ignore_element_list=ignore_element_list)

        # 得到位置
        position_list = await self.get_position_list(element_data_list=element_data_list, object_id_list=object_id_list, offspring_path=offspring_path, locator_camera=locator_camera)
        position_list = merge_list(position_list)

        if index is None:
            index = random.randint(0, len(position_list) - 1)
        # 如果index没有赋合法值，就随机点击一个
        if index < 0:
            index = len(position_list) + index

        await self.click_position(position=position_list[index], ignore_element_list=ignore_element_list)

    async def click_element_outside(self, object_id: int = 0, element_data: dict = None, locator_camera: str = "",
                                    ignore_element_list=None):
        """
        点击元素外部区域。
        计算元素周围上下左右的空间，点击空间最大的那一侧。
        通常用于点击非蒙层关闭气泡。

        :param element_data: 元素定位信息
        :param object_id: 元素 ID
        :param locator_camera: 指定摄像机

        """
        await self.clear_popup(ignore_element_list=ignore_element_list)
        click_result = await self.click_element_outside_safe(object_id=object_id, element_data=element_data,
                                                             locator_camera=locator_camera)
        if click_result:
            return
        if object_id:
            raise FindNoElementError(f"object_id{object_id}不存在")
        if element_data:
            raise FindNoElementError(f"element_data{element_data}不存在")

    async def click_element_outside_safe(self, object_id: int = 0, element_data: dict = None, locator_camera: str = ""):
        """
        点击元素外部区域。
        计算元素周围上下左右的空间，点击空间最大的那一侧。且**不清除弹窗**。
        通常用于点击非蒙层关闭气泡。

        :param element_data: 元素定位信息
        :param object_id: 元素 ID
        :param locator_camera: 指定摄像机
        :return 如果检测到目标，返回 True；否则返回 False
        """
        position_list = await self.get_position_list(object_id=object_id, element_data=element_data,
                                                     locator_camera=locator_camera)
        size_list = await self.get_size_list(object_id=object_id, element_data=element_data)
        if not position_list:
            logger.warning(f"点击目标不存在")
            return False
        if not size_list:
            logger.warning(f"点击目标不存在")
            return False
        position = position_list[0]
        size = size_list[0]

        margin = 0.01  # 元素外侧安全边距，防止落点仍落在命中区内
        # 元素四边到屏幕边界的可用距离
        left_gap = position[0] - 0.5 * size[0]
        right_gap = 1 - position[0] - 0.5 * size[0]
        up_gap = position[1] - 0.5 * size[1]
        down_gap = 1 - position[1] - 0.5 * size[1]

        areas = {
            # 落点 = 元素外侧那块空白区域的几何中点
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
        logger.info(f"click_element_outside_safe 尝试点击: {element_data}, 位置={position_out_side}, 方向={best_direction}")
        return True

        # 在b元素出现前一直尝试点击a元素

    async def click_a_until_b_appear(self, element_data_a: dict, element_data_b: dict, interval: float = 0.5, ignore_element_list=None):
        """函数功能简述
            在element_data_b元素出现之前，一直点击element_data_a元素
        """
        while not await self.exist(element_data=element_data_b):
            await self.click_element_safe(element_data=element_data_a)
            await self.clear_popup(ignore_element_list=ignore_element_list)
            await self.sleep(interval)

    async def click_a_until_b_appear_list(self, perform_list: list):
        """函数功能简述
            依次类推进行click_a_until_b_appear
        """
        cur = 0
        while cur < len(perform_list) - 1:
            await self.click_a_until_b_appear(perform_list[cur], perform_list[cur + 1])
            cur += 1

        # 在b元素消失前一直尝试点击a元素

    async def click_a_until_b_disappear(self, element_data_a: dict, element_data_b: dict, interval: float = 0.5,
                                        ignore_element_list=None):
        """函数功能简述
            在element_data_b元素消失之前，一直点击element_data_a元素
        """
        await self.wait_for_appear(element_data=element_data_b, is_click=False)
        while await self.exist(element_data=element_data_b):
            await self.clear_popup(ignore_element_list=ignore_element_list)
            await self.click_element_safe(element_data=element_data_a)
            await self.sleep(interval)

        # 在a元素消失前一直尝试点击a元素

    async def click_until_disappear(self, element_data: dict = None, interval: float = 0.5, ignore_element_list=None):
        """函数功能简述
            在element_data元素消失之前，一直点击element_data元素
        """
        await self.click_a_until_b_disappear(element_data_a=element_data, element_data_b=element_data, interval=interval,
                                             ignore_element_list=ignore_element_list)

        # 等待指定元素出现

    async def wait_for_appear(self, element_data: dict = None, element_data_list=None, is_click: bool = False,
                              interval: float = 0.5, timeout=40, ignore_element_list=None):
        """函数功能简述
            等待元素出现
        """
        if element_data_list is None:
            return await self.wait_for_appear(element_data_list=[element_data], is_click=is_click, interval=interval, timeout=timeout, ignore_element_list=ignore_element_list)
        cur = 0
        position_list = []
        position_list_merge = []
        while cur < timeout:
            await self.clear_popup(ignore_element_list=ignore_element_list)
            position_list = await self.get_position_list(element_data_list=element_data_list)
            position_list_merge = merge_list(position_list)
            if position_list_merge:
                break
            await self.sleep(interval)
            cur += interval

        if not position_list_merge:
            return position_list

        if not is_click:
            return position_list

        await self.click_position(position_list_merge[0])
        return position_list

        # 等待指定元素消失

    async def wait_for_disappear(self, element_data: dict, interval: float = 0.5, ignore_element_list=None):
        """函数功能简述
            等待元素消失
        """
        while await self.exist(element_data=element_data):
            await self.clear_popup_once(ignore_element_list=ignore_element_list)
            await self.sleep(interval)

        # 安全点击

    async def click_element_safe(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            元素存在且在屏幕范围内时再点击
        """
        position_list = await self.get_position_list(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        if not position_list:
            return
        try:
            r = random.randint(0, len(position_list) - 1)
            await self.press_position_base(position=position_list[r], duration=0)
        except:
            pass

    async def clear_popup_once(self, ignore_element_list=None):
        """函数功能简述
            清除弹窗一次
        """
        ignore_element_list = ignore_element_list or []
        ignore_name_set = set()
        for ed in ignore_element_list:
            # locator 形如 "ui_layer/view/UIXxx/..."，取出第三段作为面板名
            locator = ed.get("locator", "") if isinstance(ed, dict) else ""
            parts = [p for p in locator.split("/") if p]
            if len(parts) >= 3:
                ignore_name_set.add(parts[2])
            elif len(parts) >= 1:
                ignore_name_set.add(parts[-1])

        # 筛选出所有类型为 Pop 的页面名称
        pop_panel_names = [name for name, data in PANEL_DATA_MAP.items() if data.panel_type == PanelType.Pop]
        if not pop_panel_names:
            return True

        # 获取当前显示的面板名称
        element_data_list = [PANEL_DATA_MAP[name].element_data for name in pop_panel_names]
        panel_name_list = await self.get_name_list(element_data_list=element_data_list)
        panel_name_list = merge_list(panel_name_list)

        # 弹窗 = 检测到的弹窗 - 忽略的弹窗
        pop_window_set = (set(panel_name_list) & set(pop_panel_names)) - ignore_name_set

        # 如果没有符合条件的弹窗，提前返回
        if not pop_window_set:
            return True

        for panel_name in pop_window_set:
            panel_data = PANEL_DATA_MAP.get(panel_name)

            # 卫语句：不存在配置或没有配置关闭路径，直接跳过
            if not panel_data or not panel_data.close_path:
                continue

            for close_action in panel_data.close_path:
                # 兼容字典格式和直接传 element_data 的格式
                element = close_action.get("click_element_outside") if isinstance(close_action, dict) else close_action
                if not element:
                    continue

                await self.click_element_safe(element_data=element)
                await self.sleep(1)

        return False

    async def clear_popup(self, ignore_element_list=None):
        """函数功能简述
            一直清弹窗直到没有弹窗
        """
        while True:
            res = await self.clear_popup_once(ignore_element_list)
            if res:
                break

        # 执行清除弹窗直到element_data出现

    # 回到主界面
    async def waiting_reconnect(self):
        """
        等断线重连弹窗消失
        """
        element_data_list = self.panel_data_list_to_panel_element_data_list(panel_data_list=self.panel_data_waiting_list)
        id_list = await self.get_object_id_list(element_data_list=element_data_list)
        id_list = merge_list(list_before_merge=id_list)
        while id_list:
            id_list = await self.get_object_id_list(element_data_list=element_data_list)
            id_list = merge_list(list_before_merge=id_list)
            await self.sleep(1)

    async def go_home(self, cur_panel=None, target_panel=None):
        """函数功能简述
            回到主界面
        """
        # 获取设定的主界面名称列表，如果没有设定默认使用预设值

        while True:
            # 卫语句：如果存在目标面板且目标面板已打开，直接返回
            if target_panel and target_panel in PANEL_DATA_MAP:
                if await self.exist(element_data=PANEL_DATA_MAP[target_panel].element_data):
                    return

            # 判断当前是否已在大厅（只要其中一个home页面存在就算）
            at_home = False
            for home_name in self.panel_home_name_list:
                if home_name in PANEL_DATA_MAP and await self.exist(element_data=PANEL_DATA_MAP[home_name].element_data):
                    at_home = True
                    break

            # 判断当前指定面板是否已关闭
            cur_panel_closed = True
            if cur_panel and cur_panel in PANEL_DATA_MAP:
                cur_panel_closed = not await self.exist(element_data=PANEL_DATA_MAP[cur_panel].element_data)

            # 卫语句：同时满足回到大厅及当前面板已关闭，退出循环
            if at_home and cur_panel_closed:
                return

            await self.clear_panel_except_home()
            await self.sleep(0.5)

        # 去指定界面

    async def go_to_panel(self, panel):
        """函数功能简述
            去指定面板
        """
        # 卫语句：如果配置表中不存在该面板，记录警告并退出
        if panel not in PANEL_DATA_MAP:
            logger.warning(f"UI_DATA_MAP 中不存在 {panel}")
            return

        panel_data = PANEL_DATA_MAP[panel]

        # 卫语句：如果已经在目标面板，直接退出
        if await self.exist(element_data=panel_data.element_data):
            return

        await self.go_home(target_panel=panel)

        while not await self.exist(element_data=panel_data.element_data):
            await self.clear_popup_once()

            # 卫语句：如果没有打开路径，防止死循环跳出
            if not panel_data.open_path:
                break

            for open_action in panel_data.open_path:
                element = open_action.get("click_element") if isinstance(open_action, dict) else open_action
                if not element:
                    continue

                await self.click_element_safe(element_data=element)
                await self.sleep(0.5)

        # 关除了主界面的界面

    async def clear_panel_except_home(self):
        """函数功能简述
            关除了主界面的其它界面一次
        """
        # 筛选出所有常规界面和弹窗页面，排除大厅页面列表
        panel_names = [name for name in PANEL_DATA_MAP.keys() if name not in self.panel_home_name_list]
        if not panel_names:
            return

        element_data_list = [PANEL_DATA_MAP[name].element_data for name in panel_names]

        panel_name_list = await self.get_name_list(element_data_list=element_data_list)
        panel_name_list = merge_list(panel_name_list)

        for panel_name in panel_name_list:
            # 未在记录中或是没有配置关闭路径，直接跳过
            if panel_name not in PANEL_DATA_MAP:
                continue

            panel_data = PANEL_DATA_MAP[panel_name]
            if not panel_data.close_path:
                continue

            await self.clear_popup_once()

            for close_action in panel_data.close_path:
                element = close_action.get("click_element_outside") if isinstance(close_action, dict) else close_action
                if not element:
                    continue

                await self.click_element_safe(element_data=element)
            break

        await self.sleep(0.2)

    async def swipe(self, object_id: int = 0, element_data: dict = None, point_start=None, point_end=None, t: float = 0.5,
                    offspring_path="", ignore_element_list=None):
        """函数功能简述
            清除弹窗后滑动
        """
        await self.clear_popup(ignore_element_list)
        await self.swipe_base(object_id, element_data, point_start, point_end, t, offspring_path)

    async def swipe_base(self, object_id: int = 0, element_data: dict = None, point_start=None, point_end=None,
                         t: float = 0.5, offspring_path=""):
        """函数功能简述
            滑动
        """
        if point_start is not None:
            await self.driver.swipe(point_start, point_end, t)
            return
        if object_id != 0:
            point_start = await self.get_position(object_id=object_id)
            await self.driver.swipe(point_start, point_end, t)
            return
        [element_data_copy] = self._prepare_element_data_list(element_data_list=[element_data], offspring_path=offspring_path)
        point_start = await self.get_position(element_data=element_data_copy)
        await self.driver.swipe(point_start, point_end, t)

    async def swipe_slider_base(self, slider, value_start=None, value_end=None):
        if not value_start:
            value_start = random.random()
        if not value_end:
            value_end = random.random()
        point_start, point_end = slider.get_slide_point_start_and_end(slide_range=[value_start, value_end])
        if value_start > value_end:
            t = value_start - value_end
        else:
            t = value_end - value_start
        await self.swipe(point_start=point_start, point_end=point_end, t=t)

    async def get_screen_shot(self, x, y, w, h):
        """函数功能简述
            截取屏幕
        """
        img_b64encode, fmt = await rpc_method_request.screen_shot(self.server, x, y, w, h)
        if fmt.endswith('.deflate'):
            imgdata = base64.b64decode(img_b64encode)
            imgdata = zlib.decompress(imgdata)
            img_b64encode = base64.b64encode(imgdata)
        img_b64decode = base64.b64decode(img_b64encode)
        img_array = np.frombuffer(img_b64decode, np.uint8)
        img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)
        return img

        # 保存截图到report

    def save_img(self, img, img_name=""):
        """函数功能简述
            保存截图到report文件夹
        """
        path = f"{self.root_dir}/report"

        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        if img_name == "":
            num_png = len(os.listdir(path))
            cur = num_png
            img_name = f'/{cur}.jpg'
        cv2.imwrite(path + img_name, img)

        # 整屏截取

    async def get_full_screen_shot(self):
        """函数功能简述
            截取整个屏幕
        """
        img = await self.get_screen_shot(self.screen_w * 0.5, self.screen_h * 0.5, self.screen_w, self.screen_h)
        return img

        # 对指定元素进行截取

    async def get_element_shot(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            指定元素截图
        """
        ui_x, ui_y = await self.get_position(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        ui_w, ui_h = await self.get_size(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        ui_x, ui_y = int(ui_x * self.screen_w), int(ui_y * self.screen_h)
        ui_w, ui_h = int(ui_w * self.screen_w), int(ui_h * self.screen_h)
        img = await self.get_screen_shot(ui_x, ui_y, ui_w, ui_h)
        return img

    async def click_button(self, element_data: dict = None, element_data_list: list = None):
        """函数功能简述
            元素身上有按钮组件才进行点击
        """
        if element_data_list is not None:
            await rpc_method_request.click_button(self.server, element_data_list)
            return
        await self.click_button(element_data_list=[element_data])

    async def ray_input(self, kind: str, object_id: int = 0, element_data: dict = None, offspring_path: str = ""):
        """函数功能简述
            对target_name身上有Empty4Raycast组件进行光线操作
        """
        if object_id != 0:
            await rpc_method_request.ray_input_by_id(self.server, [object_id], offspring_path, kind)
            return
        [element_data_copy] = self._prepare_element_data_list([element_data], offspring_path)
        await rpc_method_request.ray_input(self.server, [element_data_copy], kind)

        # 设定节点激活状态

    async def set_object_active_list(self, path_list: list[str], active: bool = False):
        """函数功能简述
            设定节点激活状态
        """
        if not path_list:
            return
        await rpc_method_request.set_object_active(self.server, path_list, active)

    async def set_object_active(self, path: str, active: bool = False):
        """函数功能简述
            设定节点激活状态
        """
        if not path:
            return
        await self.set_object_active_list(path_list=[path], active=active)

        # 设置时间缩放

    async def set_time_scale(self, time_scale: float = None):
        """函数功能简述
            设定Unity时间倍率
        """
        if not time_scale:
            time_scale = self.time_scale_default

        if not getattr(self, "is_time_scale", False):
            await rpc_method_request.set_time_scale(self.server, 1)
            return
        await rpc_method_request.set_time_scale(self.server, time_scale)

        # 休息t秒

    @staticmethod
    async def sleep(t: float = 1):
        """
        强制等待指定时间。

        :param t: 等待时长(秒)(选填)
        默认为1s
        """
        await asyncio.sleep(t)

    async def custom_cmd_list(self, command_list):
        """函数功能简述
            批量自定义的命令
        """
        if not command_list:
            return
        await rpc_method_request.custom_cmd(self.server, command_list)

    async def custom_cmd(self, command):
        """函数功能简述
            批量自定义的命令
        """
        if not command:
            return
        await self.custom_cmd_list([command])


class BasePage(BasePageMain):
    def __init__(self, server, device_type="pc", device_id=None, is_record=False, session_dir=None):
        super().__init__(server=server, device_type=device_type, device_id=device_id, is_record=is_record, session_dir=session_dir)





if __name__ == '__main__':
    # 示例用法需要包含异步执行环境 (asyncio.run)
    pass
