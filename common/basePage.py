import threading
from datetime import datetime

from airtest.core.helper import G
from poco.drivers.unity3d.device import UnityEditorWindow
import netMsg.luaLog
import json
from importlib import import_module

import tools.commonTools
from common.uimonitor import UIMonitor
from configs.pathConfig import EXCEL_PATH
from tools.excelRead import ExcelTools

import time
import pyautogui
import base64
import cv2
import numpy as np
from poco.drivers.unity3d import UnityPoco
from airtest.core.api import connect_device
from common import rpcMethodRequest, resource
from common.error import *
import zlib

import os
from configs.elementsData import ElementsData
from configs.jumpData import JumpData

import logging
import wda


class BasePageMain:
    def __init__(self, serial_number=None, dev=None, is_mobile_device=False, is_monitor=False):
        # 不打印airtest日志
        logging.getLogger("airtest").setLevel(logging.ERROR)
        # unity窗口使用UnityEditorWindow()
        # 手机使用connect_device("android://127.0.0.1:5037/设备号")

        # 是否在手机, Unity需要改为False
        self.is_mobile_device = is_mobile_device

        # 是否截图记录
        self.record = False

        # 是否打印日志
        self.is_debug_log = False

        # Unity是否发日志给python
        self.send_log_flag = False

        # 是否开启战斗倍速
        self.is_time_scale = False

        self.is_ios = False
        if is_mobile_device is True and serial_number is None:
            self.is_ios = True

        # 默认端口 5001
        addr = ('', 5001)
        # Unity log接收端口5002
        addr_listen = ('', 5002)
        self.dev = dev
        if self.dev is None:
            print("self.dev is None")
            self.dev = self.get_device(serial_number=serial_number)

        self.poco = UnityPoco(addr, device=dev)
        self.poco_listen = None

        # 不是ios就可以开启Unity log接收
        if not self.is_ios:
            self.poco_listen = UnityPoco(addr_listen, device=dev)
        self.screen_w, self.screen_h = self.poco.get_screen_size()  # 获取屏幕尺寸

        # ios设备出现过poco获取屏幕尺寸与wda尺寸不同的情况，所以需要scale_factor对点击位置做下矫正
        self.scale_factor_w = 1
        self.scale_factor_h = 1

        if self.is_ios:
            self.udid = wda.usbmux.pyusbmux.list_devices()[0].serial
            usb_dev = wda.Client(f"http+usbmux://{self.udid}:8100")
            window_size = usb_dev.window_size()
            self.scale_factor_w = window_size[0] / self.screen_w * usb_dev.scale
            self.scale_factor_h = window_size[1] / self.screen_h * usb_dev.scale

        if self.is_debug_log:
            print(self.screen_w, self.screen_h)

        self.warning_list = []
        self.erro_list = []
        file_path = os.path.join(os.path.dirname(__file__))
        # print(file_path)
        # # 获取当前工作目录
        # current_dir = os.getcwd()
        # 获取父目录
        self.root_dir = os.path.abspath(os.path.dirname(file_path))
        self.element_data_home = ElementsData.Home.HomePanel

        # BasePageExt(self)

    def get_device(self, serial_number=None):
        """函数功能简述
            连接并返回设备，以便后续使用

        参数:
            serial_number: 设备号
            当self.is_mobile_device是False时，设备号没有意义

        返回:
            设备
        """
        # unity端
        if not self.is_mobile_device:
            dev = UnityEditorWindow()
            return dev

        # 非unity
        # 已连接
        try:
            dev = G.DEVICE
            return dev
        # 未连接，新建连接
        except Exception as e:
            print(e)
            print("进行设备连接")
        if self.is_ios:
            dev = connect_device(f"ios:///http://127.0.0.1:8100")
            return dev
        dev = connect_device(f"android://127.0.0.1:5037/{serial_number}")
        # dev = connect_device("android://127.0.0.1:5037/b6h65hd64p5pxcyh")
        # dev = connect_device("android://127.0.0.1:5037/28cce18906027ece")
        return dev

    # 断开poco连接
    def connect_close(self):
        """函数功能简述
            关闭与c#的rpc连接
            当开启Unity log接收端口也同时关闭
        """
        self.send_log_flag = False
        self.poco.agent.c.conn.close()
        if self.poco_listen is not None:
            self.poco_listen.agent.c.conn.close()

    def debug_log(self, *msg):
        """函数功能简述
            使用一个标志位is_debug_log控制打印

        参数:
            msg: 需要打印的内容
        """
        if self.is_debug_log:
            print(*msg)

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
    def get_element_data(element_data, offspring_path):
        """函数功能简述
            把路径和偏移路径合成为当前要用的的element_data

        参数:
            element_data: 元素定位信息，主要是路径信息
            offspring_path: 偏移路径

        返回:
            dict
        """
        element_data_copy = element_data
        if offspring_path != "":
            element_data_copy = element_data.copy()
            element_data_copy["locator"] = element_data_copy["locator"] + '>' + offspring_path
        return element_data_copy

    def get_element_data_list(self, element_data_list, offspring_path):
        """函数功能简述
            调用 get_element_data()方法
            依次把element_data_list中的element_data和offspring_path合成

        参数:
            element_data_list: 元素定位信息组成的列表
            offspring_path: 偏移路径

        返回:
            list[dict]
        """
        if offspring_path == "":
            return element_data_list
        cur = 0
        while cur < len(element_data_list):
            element_data_list[cur] = self.get_element_data(element_data_list[cur], offspring_path)
            cur += 1
        return element_data_list

    def exist(self, object_id=0, element_data=None, offspring_path=""):
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
            if self.get_offspring_id_list(object_id=object_id, offspring_path=offspring_path):
                return True
            return False

        if self.get_offspring_id_list(element_data=element_data, offspring_path=offspring_path):
            return True
        return False

    # 得到元素的Instance Id列表
    def get_object_id_list(self, element_data: dict = None, element_data_list: list = None, offspring_path=""):
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
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_object_id(self.poco, element_data_copy_list)

        return self.get_object_id_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    # 得到元素的Instance Id
    def get_object_id(self, element_data: dict, offspring_path=""):
        """函数功能简述
            获取元素id

        参数:
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回:
            object_id_list有且只有一个元素时，返回int
        """
        object_id_list = self.get_object_id_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(object_id_list)
        return object_id_list[0]

    # 得到后代的Instance Id
    def get_offspring_id_list(self, offspring_path, object_id=0, object_id_list=None, element_data=None,
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
            return rpcMethodRequest.get_offspring_id_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_offspring_id_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return self.get_object_id_list(element_data_list=element_data_copy_list)

        return self.get_object_id_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_offspring_id(self, offspring_path, object_id=0, element_data=None):
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
        offspring_id_list = self.get_offspring_id_list(object_id=object_id, element_data=element_data,
                                                       offspring_path=offspring_path)
        self.is_single_element(offspring_id_list)
        return offspring_id_list[0]

    # 得到父节点
    def get_parent_id_list(self, object_id=0, object_id_list=None, element_data=None, element_data_list: list = None,
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
            return rpcMethodRequest.get_parent_id_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_parent_id_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_parent_id(self.poco, element_data_copy_list)

        return self.get_parent_id_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_parent_id(self, object_id=0, element_data=None, offspring_path=""):
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
            parent_id_list = self.get_parent_id_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(parent_id_list)
            return parent_id_list[0]

        parent_id_list = self.get_parent_id_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(parent_id_list)
        return parent_id_list[0]

    # 获得文本
    def get_text_list(self, object_id=0, object_id_list: list = None, element_data: dict = None,
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
            return rpcMethodRequest.get_text_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_text_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_text(self.poco, element_data_copy_list)

        return self.get_text_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_text(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            text_list = self.get_text_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(text_list)
            return text_list[0]

        text_list = self.get_text_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(text_list)
        return text_list[0]

    # 修改文本
    def set_text_list(self, object_id=0, object_id_list: list = None, element_data: dict = None,
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
            rpcMethodRequest.set_text_by_id(self.poco, object_id_list, offspring_path, text)
            return

        if object_id != 0:
            self.set_text_list(object_id_list=[object_id], offspring_path=offspring_path, text=text)
            return

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            rpcMethodRequest.set_text(self.poco, element_data_copy_list, text)
            return

        self.set_text_list(element_data_list=[element_data], text=text, offspring_path=offspring_path)

    def set_text(self, object_id: int = 0, element_data: dict = None, text="", offspring_path=""):
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
            self.set_text_list(object_id=object_id, offspring_path=offspring_path, text=text)
            return

        self.set_text_list(element_data=element_data, text=text, offspring_path=offspring_path)

    # 获取图标名
    def get_icon_list(self, object_id=0, object_id_list: list = None, element_data: dict = None,
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
            res = rpcMethodRequest.get_img_name_by_id(self.poco, object_id_list, offspring_path)
            cur = 0
            while cur < len(res):
                icon_list = res[cur]
                resource.check_icon_list(icon_list)
                cur += 1
            return res

        if object_id != 0:
            return self.get_icon_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            res = rpcMethodRequest.get_img_name(self.poco, element_data_copy_list)
            cur = 0
            while cur < len(res):
                icon_list = res[cur]
                resource.check_icon_list(icon_list)
                cur += 1
            return res

        return self.get_icon_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_icon(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            icon_list = self.get_icon_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(icon_list)
            icon = resource.check_icon(icon_list[0])
            return icon

        icon_list = self.get_icon_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(icon_list)
        return icon_list[0]

    # 获取节点名称
    def get_name_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
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
            return rpcMethodRequest.get_name_by_id(self.poco, object_id_list, offspring_path)

        # 输入object_id的情况，将object_id加上[]转为object_id_list
        if object_id != 0:
            return self.get_name_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        # 输入element_data_list的情况，直接调用rpc
        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_name(self.poco, element_data_copy_list)

        # 输入element_data的情况,将element_data加[]转为element_data_list
        return self.get_name_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_name(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            name_list = self.get_name_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(name_list)
            return name_list[0]

        name_list = self.get_name_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(name_list)
        return name_list[0]

    # 获取滑条值，值在0~1
    def get_slider_value_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
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
            return rpcMethodRequest.get_slider_value_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_slider_value_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_slider_value(self.poco, element_data_copy_list)

        return self.get_slider_value_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    # 获取到的滑条值是float类型，值在0~1
    def get_slider_value(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            slider_value_list = self.get_slider_value_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(slider_value_list)
            return slider_value_list[0]

        slider_value_list = self.get_slider_value_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(slider_value_list)
        return slider_value_list[0]

    # 获取下拉列表当前值
    def get_dropdown_value(self, element_data):
        """函数功能简述
            定位元素后取元素dropdown组件的值

        参数:
            element_data: 元素定位信息

        返回:
            slider_value_list有且只有一个元素时，返回int
            值是自然数
         """
        dropdown_value_list = rpcMethodRequest.get_dropdown_value(self.poco, [element_data])
        self.is_single_element(dropdown_value_list)
        return dropdown_value_list[0]

    def set_dropdown_value(self, element_data, index):
        """函数功能简述
            定位元素后设元素dropdown组件的值

        参数:
            element_data: 元素定位信息

        返回:
            None
         """
        rpcMethodRequest.set_dropdown_value(self.poco, [element_data], index)

    # 获取元素尺寸
    def get_size_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
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
            return rpcMethodRequest.get_size_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_size_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_size(self.poco, element_data_copy_list)

        return self.get_size_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_size(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            size_list = self.get_size_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(size_list)
            return size_list[0]

        size_list = self.get_size_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(size_list)
        return size_list[0]

    # 获取勾选状态
    def get_toggle_is_on_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
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
            return rpcMethodRequest.get_toggle_is_on_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_toggle_is_on_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_toggle_is_on(self.poco, element_data_copy_list)

        return self.get_toggle_is_on_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_toggle_is_on(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            toggle_is_on_list = self.get_toggle_is_on_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(toggle_is_on_list)
            return toggle_is_on_list[0]

        toggle_is_on_list = self.get_toggle_is_on_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(toggle_is_on_list)
        return toggle_is_on_list[0]

    # 获取位置
    def get_position_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None,
                          element_data_list: list = None, offspring_path=""):
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
        if object_id_list is not None:
            return rpcMethodRequest.get_position_by_id(self.poco, object_id_list, offspring_path)

        if object_id != 0:
            return self.get_position_list(object_id_list=[object_id], offspring_path=offspring_path)[0]

        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            return rpcMethodRequest.get_position(self.poco, element_data_copy_list)

        return self.get_position_list(element_data_list=[element_data], offspring_path=offspring_path)[0]

    def get_position(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
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
            position_list = self.get_position_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(position_list)
            return position_list[0]

        position_list = self.get_position_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(position_list)
        return position_list[0]

    # 元素长按
    def press(self, object_id: int = 0, element_data: dict = None, duration: float = 2.0, offspring_path=""):
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
        position = self.get_position(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        self.press_position(position, duration)

    # 位置长按
    def press_position(self, position, duration: float = 2.0):
        """函数功能简述
            按压position位置duration秒

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径
            duration: 按压时长（默认值为2s）
         """
        self.poco.long_click(position, duration)

    # 位置点击
    # position=[x,y]
    # 0<=x<=1, 0<=y<=1
    def click_position_base(self, position):
        """函数功能简述
            点击position处
            self.record=True时，每次点击前会进行截图
        参数:
            position[float, float]
        """
        position[0] = self.scale_factor_w * position[0]
        position[1] = 1 - self.scale_factor_h * (1 - position[1])
        if not (0 <= position[0] <= 1) or not (0 <= position[1] <= 1):
            raise InvalidOperationError('Click position out of screen. pos={}'.format(repr(position)))
        # 点击前进行截图保存
        if self.record:
            img = self.get_full_screen_shot()
            self.draw_circle(img, (position[0], position[1]))
            self.save_img(img)
        self.poco.agent.input.click(position[0], position[1])

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

    def click_position(self, position, ignore_set=None):
        """函数功能简述
            点击position处
            点击前会清除一遍弹窗
        参数:
            position[float, float]
            ignore_set: 需要忽略清除的弹窗
        """
        self.clear_popup(ignore_set)
        self.click_position_base(position)

    # 元素点击
    def click_element(self, object_id: int = 0, element_data: dict = None, offspring_path="", ignore_set=None,  focus=None):
        """函数功能简述
            定位元素后取元素的position值

        参数:
            object_id和element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径
            ignore_set: 需要忽略清除的弹窗
            focus: 元素锚点，用于计算元素中心位置

        返回:
            position_list有且只有一个元素时，返回[float, float]
        """
        if object_id != 0:
            position = self.get_position(object_id=object_id, offspring_path=offspring_path)
            if focus is None:
                self.click_position(position)
                return position
            size = self.get_size(object_id=object_id)
            bias_x = 0.5 - focus[0]
            bias_y = 0.5 - focus[1]
            position[0] += size[0] * bias_x
            position[1] += size[1] * bias_y
            self.click_position(position)
            return position

        self.clear_popup(ignore_set)
        position_list = self.get_position_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(position_list)
        self.click_position_base(position_list[0])
        return position_list[0]

    # 在b元素出现前一直尝试点击a元素
    def click_a_until_b_appear(self, element_data_a: dict, element_data_b: dict, interval: float = 0.5, ignore_set=None):
        """函数功能简述
            在element_data_b元素出现之前，一直点击element_data_a元素

        参数:
            element_data_a: 点击元素
            element_data_a: 检测元素
            interval: 点击间隔（默认0.5s）
            ignore_set: 需要忽略清除的弹窗
        """
        while not self.exist(element_data=element_data_b):
            self.click_element_safe(element_data=element_data_a)
            self.clear_popup(ignore_set=ignore_set)
            self.sleep(interval)


    def click_a_until_b_appear_list(self, perform_list: list):
        """函数功能简述
            第一次循环element_data_a=perform_lis[0], element_data_b=perform_lis[1]
            第一次循环element_data_a=perform_lis[1], element_data_b=perform_lis[2]
            以此类推进行click_a_until_b_appear

        参数:
            perform_list: element_data组成的list
        """
        cur = 0
        while cur < len(perform_list) - 1:
            # print(perform_list[cur], perform_list[cur + 1])
            self.click_a_until_b_appear(perform_list[cur], perform_list[cur + 1])
            cur += 1

    # 在b元素消失前一直尝试点击a元素
    def click_a_until_b_disappear(self, element_data_a: dict, element_data_b: dict, interval: float = 0.5,
                                  ignore_set=None):
        """函数功能简述
            在element_data_b元素消失之前，一直点击element_data_a元素
            首先会等待element_data_b元素出现

        参数:
            element_data_a: 点击元素
            element_data_a: 检测元素
            interval: 点击间隔（默认0.5s）
            ignore_set: 需要忽略清除的弹窗
        """
        self.wait_for_appear(element_data=element_data_b, is_click=False)
        while self.exist(element_data=element_data_b):
            self.clear_popup(ignore_set=ignore_set)
            self.click_element_safe(element_data=element_data_a)
            self.sleep(interval)

    # 在a元素消失前一直尝试点击a元素
    def click_until_disappear(self, element_data: dict = None, interval: float = 0.5, ignore_set=None):
        """函数功能简述
            在element_data元素消失之前，一直点击element_data元素

        参数:
            element_data: 点击元素和检测元素
            interval: 点击间隔（默认0.5s）
            ignore_set: 需要忽略清除的弹窗
        """
        self.click_a_until_b_disappear(element_data_a=element_data, element_data_b=element_data, interval=interval,
                                       ignore_set=ignore_set)

    # 等待指定元素出现
    def wait_for_appear(self, element_data: dict = None, element_data_list=None, is_click: bool = False,
                        interval: float = 0.2, timeout=120, ignore_set=None):
        """函数功能简述
            等待元素出现

        参数:
            element_data和element_data_list输入其中一个
            element_data: 检测元素
            element_data_list: 检测元素列表，检测到其中一个就算检测到
            is_click: True的话出现后点击
            interval: 检测间隔（默认0.2s）
            timeout: 超时次数（默认120次检测）超时后会跳出循环
            ignore_set: 需要忽略清除的弹窗
        """

        # element_data转为element_data_list
        if element_data_list is None:
            self.wait_for_appear(element_data_list=[element_data], is_click=is_click, interval=interval,
                                 timeout=timeout, ignore_set=ignore_set)
            return

        cur = 0
        position_list = []
        while cur < timeout:
            self.clear_popup(ignore_set=ignore_set)
            position_list = self.get_position_list(element_data_list=element_data_list)
            position_list = tools.commonTools.merge_list(position_list)
            if position_list:
                break
            self.sleep(interval)
            cur += interval

        # 没找到直接返回
        if not position_list:
            return

        # 找到后不点击
        if not is_click:
            return

        # 找到后点击
        self.click_position(position_list[0])

    # 等待指定元素消失
    def wait_for_disappear(self, element_data: dict, interval: float = 0.2, ignore_set=None):
        """函数功能简述
            等待元素消失

        参数:
            element_data: 检测元素
            interval: 检测间隔（默认0.2s）
            ignore_set: 需要忽略清除的弹窗
        """
        while self.exist(element_data=element_data):
            self.clear_popup_once(ignore_set=ignore_set)
            self.sleep(interval)

    # 安全点击
    # 判断元素存在后再点击
    def click_element_safe(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            元素存在且在屏幕范围内时再点击

        参数:
            object_id和element_data选择一个输入
            object_id: 元素id
            element_data: 检测元素
            offspring_path: 偏移路径
        """
        position_list = self.get_position_list(object_id=object_id, element_data=element_data,
                                               offspring_path=offspring_path)

        if not position_list:
            return
        try:
            self.click_position_base(position_list[0])
        except:
            pass
            # print("超出屏幕范围，没有进行点击")
        # print(f"{object_id, element_data}元素不存在，没有进行点击")

    # 尝试进行一系列操作，若操作过程报错则尝试关闭弹窗再重试
    def try_actions(self, action_list):
        try:
            self.clear_popup_once()
            for i in range(len(action_list)):
                # 获取当前需要执行的函数及其参数
                action_list[i]()
                self.sleep(0.5)
        except Exception as e:
            print("正在检查是否有弹窗遮挡", e)
            self.clear_popup_once()
            self.sleep(1)
            self.try_actions(action_list)

    # 清除一遍弹窗
    def clear_popup_once(self, ignore_set=None):
        """函数功能简述
            清除弹窗一次

        参数:
            ignore_set: 忽略的弹窗
        """
        if ignore_set is None:
            ignore_set = set()
        panel_name_list = self.get_name_list(element_data=ElementsData.Panels)
        # 弹窗=检测到的弹窗-忽略的弹窗
        pop_window_set = set(panel_name_list) & JumpData.pop_window_set - ignore_set

        # 没有弹窗
        if not pop_window_set:
            return True
        for panel_name in pop_window_set:
            # 开鱼卡特殊处理，进行一次点击跳过动画
            if panel_name == "FishBagPanel":
                self.click_position_base([0.5, 0.5])
                self.sleep(0.5)
            for close_element in JumpData.panel_close_dict[panel_name]:
                self.click_element_safe(element_data=close_element)
                self.sleep(1)
        return False

    # 清除干净弹窗
    def clear_popup(self, ignore_set=None):
        """函数功能简述
            一直清弹窗直到没有弹窗

        参数:
            ignore_set: 忽略的弹窗
        """
        while True:
            res = self.clear_popup_once(ignore_set)
            if res:
                break

    # 执行清除弹窗直到element_data出现
    def clear_popup_until_appear(self, element_data):
        """函数功能简述
            清弹窗直到元素出现

        参数:
            element_data: 元素定位信息
        """
        while not self.exist(element_data=element_data):
            self.clear_popup_once()
            self.sleep(0.5)

    # 回到主界面
    def go_home(self, cur_panel=None, target_panel=None):
        """函数功能简述
            回到主界面

        参数:
            cur_panel: 有一些面板会在HomePanel存在时同时存在，需要特殊记录这些面板
            target_panel: 目标面板，在回主界面的过程中，如果遇到target_panel也会跳出循环
        """
        cur = 0
        at_home_flag = False
        while not at_home_flag:
            # 关闭一次除了HomePanel的所有面板
            self.clear_panel_except_home()
            self.sleep(0.5)

            # 在返回大厅过程中找到目标面板就直接返回
            at_target_panel_flag = False
            if target_panel:
                at_target_panel_flag = self.exist(element_data=JumpData.panel_dict[target_panel]["element_data"])
            if at_target_panel_flag:
                return

            # 关闭面板30次还没回到大厅大概率卡住了
            cur += 1
            if cur > 30:
                raise FindNoElementError("FindNoElement")

            # 有HomePanel且没有cur_panel需要关闭时才判断停止
            at_home_flag = self.exist(element_data=self.element_data_home)
            if cur_panel is not None:
                at_home_flag = at_home_flag and not self.exist(
                    element_data=JumpData.panel_dict[cur_panel]["element_data"])

    # 去指定界面
    def go_to_panel(self, panel):
        """函数功能简述
            去指定面板

        参数:
            panel: 目标面板
        """
        panel_dict = JumpData.panel_dict[panel]
        # 在目标面板就直接返回
        if self.exist(element_data=panel_dict["element_data"]):
            return

        # 回大厅
        self.go_home(target_panel=panel)

        # 按照JumpData.panel_dict中记录的路径尝试点击，直到到目标面板
        while not self.exist(element_data=panel_dict["element_data"]):
            self.clear_popup_once()
            for element_data in panel_dict["open_path"]:
                self.click_element_safe(element_data=element_data)
                self.sleep(0.5)

    # 关除了主界面的界面
    def clear_panel_except_home(self):
        """函数功能简述
            关除了主界面的其它界面一次
        """
        panel_name_list = self.get_name_list(element_data_list=[ElementsData.Panels])
        panel_name_list = tools.commonTools.merge_list(panel_name_list)
        for panel_name in panel_name_list:
            if panel_name not in JumpData.panel_close_dict:
                continue
            self.clear_popup_once()
            for close_element in JumpData.panel_close_dict[panel_name]:
                self.click_element_safe(element_data=close_element)
            break
        self.sleep(0.2)

    # 元素滑动
    def swipe(self, object_id: int = 0, element_data: dict = None, point_start=None, point_end=None, t: float = 0.5,
              offspring_path="", ignore_set=None):
        """函数功能简述
            清除弹窗后滑动

        参数:
            object_id、element_data、point_start三个选择一个输入，object_id或element_data都是为了得到滑动起始点坐标
            object_id: 元素id
            element_data: 元素定位信息
            point_start: 滑动起始点坐标
            point_end: 滑动终止点坐标
            t: 滑动时间
            offspring_path: 偏移路径
            ignore_set: 忽略的弹窗
        """
        self.clear_popup(ignore_set)
        self.swipe_base(object_id, element_data, point_start, point_end, t, offspring_path)

    def swipe_base(self, object_id: int = 0, element_data: dict = None, point_start=None, point_end=None,
                   t: float = 0.5, offspring_path=""):
        """函数功能简述
            滑动

        参数:
            object_id、element_data、point_start三个选择一个输入，object_id或element_data都是为了得到滑动起始点坐标
            object_id: 元素id
            element_data: 元素定位信息
            point_start: 滑动起始点坐标
            point_end: 滑动终止点坐标
            t: 滑动时间
            offspring_path: 偏移路径
        """
        if point_start is not None:
            self.poco.swipe(p1=point_start, p2=point_end, duration=t)  # direction可以填'left','right','up','down'
            return
        if object_id != 0:
            point_start = self.get_position(object_id=object_id)
            self.poco.swipe(p1=point_start, p2=point_end, duration=t)
            return
        element_data_copy = self.get_element_data(element_data, offspring_path)
        point_start = self.get_position(element_data=element_data_copy)
        self.poco.swipe(p1=point_start, p2=point_end, duration=t)

    def get_screen_shot(self, x, y, w, h):
        """函数功能简述
            截取屏幕

        参数:
            x,y为坐标
            w,h为宽高

        返回值:
            Opencv格式图像
        """
        img_b64encode, fmt = rpcMethodRequest.screen_shot(self.poco, x, y, w, h)
        if fmt.endswith('.deflate'):
            # fmt = fmt[:-len('.deflate')]
            imgdata = base64.b64decode(img_b64encode)
            imgdata = zlib.decompress(imgdata)
            img_b64encode = base64.b64encode(imgdata)
        img_b64decode = base64.b64decode(img_b64encode)  # base64解码
        img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
        img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
        return img

    # 保存截图到report
    def save_img(self, img, img_name=""):
        """函数功能简述
            保存截图到report文件夹

        参数:
            img: Opencv格式图像
            img_name: 图片名（不填则以数字命名）

        返回值:
            Opencv格式图像
        """
        path = f"{self.root_dir}/report"  # 输入文件夹地址

        # 不存在就创建
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        if img_name == "":
            num_png = len(os.listdir(path))  # 读入文件夹,统计文件夹中的文件个数
            cur = num_png
            img_name = f'/{cur}.jpg'
        cv2.imwrite(path + img_name, img)

    # 整屏截取
    def get_full_screen_shot(self):
        """函数功能简述
            截取整个屏幕

        返回值:
            Opencv格式图像
        """
        img = self.get_screen_shot(self.screen_w * 0.5, self.screen_h * 0.5, self.screen_w, self.screen_h)
        return img

    # 对指定元素进行截取
    def get_element_shot(self, object_id: int = None, element_data: dict = None, offspring_path=""):
        """函数功能简述
            指定元素截图

        参数:
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径

        返回值:
            Opencv格式图像
        """
        ui_x, ui_y = self.get_position(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        ui_w, ui_h = self.get_size(object_id=object_id, element_data=element_data, offspring_path=offspring_path)
        ui_x, ui_y = int(ui_x * self.screen_w), int(ui_y * self.screen_h)
        ui_w, ui_h = int(ui_w * self.screen_w), int(ui_h * self.screen_h)
        img = self.get_screen_shot(ui_x, ui_y, ui_w, ui_h)
        return img

    def click_button(self, element_data: dict = None, element_data_list: list = None):
        """函数功能简述
            元素身上有按钮组件才进行点击

        参数:
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list

        """
        if element_data_list is not None:
            rpcMethodRequest.click_button(self.poco, element_data_list)
            return
        self.click_button(element_data_list=[element_data])

    #
    def ray_input(self, kind: str, object_id: int = 0, element_data: dict = None, offspring_path: str = ""):
        """函数功能简述
            对target_name身上有Empty4Raycast组件进行光线操作

        参数:
            object_id和element_data选择一个输入
            kind有up，down，click三种
            object_id: 元素id
            element_data: 元素定位信息，只对定位到的第一个元素生效
            offspring_path: 偏移路径
        """
        if object_id != 0:
            rpcMethodRequest.ray_input_by_id(self.poco,[object_id], offspring_path, kind)
            return
        element_data_copy = self.get_element_data(element_data, offspring_path)
        rpcMethodRequest.ray_input(self.poco,[element_data_copy], kind)

    # 设定节点激活状态
    def set_object_active_list(self, active: bool = False, object_id=0, object_id_list: list = None, element_data: dict = None,
                               element_data_list: list = None, offspring_path=""):
        """函数功能简述
            设定节点激活状态

        参数:
            active: 激活状态，暂时只能把激活节点设为未激活，所以填False
            object_id、object_id_list、element_data、element_data_list输入其中的一个
            object_id: 元素id
            object_id_list: 元素id组成的list
            element_data: 元素定位信息
            element_data_list: 元素定位信息组成的list
            offspring_path: 偏移路径
        """
        if object_id_list is not None:
            rpcMethodRequest.set_object_active_by_id(self.poco, object_id_list, offspring_path, active)
            return
        if object_id != 0:
            self.set_object_active_list(active=active, object_id_list=[object_id], offspring_path=offspring_path)
            return
        if element_data_list is not None:
            element_data_copy_list = self.get_element_data_list(element_data_list, offspring_path)
            rpcMethodRequest.set_object_active(self.poco, element_data_copy_list, active)
            return

        self.set_object_active_list(active=active, element_data_list=[element_data], offspring_path=offspring_path)

    def set_object_active(self, active: bool = False, object_id: int = 0, element_data: dict = None, offspring_path=""):
        """函数功能简述
            设定节点激活状态

        参数:
            active: bool 激活状态，暂时只能把激活节点设为未激活，所以填False
            object_id、element_data输入其中的一个
            object_id: 元素id
            element_data: 元素定位信息
            offspring_path: 偏移路径
        """
        if object_id != 0:
            self.set_object_active_list(active=active, object_id=object_id, offspring_path=offspring_path)
            return

        self.set_object_active_list(active=active, element_data=element_data, offspring_path=offspring_path)

    # 设置时间缩放
    def set_time_scale(self, time_scale=5):
        """函数功能简述
            设定Unity时间倍率

        参数:
            time_scale: float
            正常速率为1
        """
        if not self.is_time_scale:
            return
        rpcMethodRequest.set_time_scale(self.poco, time_scale)

    # 休息t秒
    @staticmethod
    def sleep(t: float):
        """函数功能简述
            休息t秒
        """
        time.sleep(t)

    # 键盘输入
    @staticmethod
    def send_key(key: str):
        """函数功能简述
            打字限windows上使用
        """
        pyautogui.typewrite(key)


class BasePage(BasePageMain):
    def __init__(self, serial_number=None, dev=None, is_mobile_device=False, is_monitor=False):
        super().__init__(serial_number, dev, is_mobile_device, is_monitor)
        # 是否测试会拉起支付的按钮
        self.is_pay = True

        # 全局变量
        self.cur = 0

        # 消息储存队列
        self.log_list = []

        self.log_list_duel = []

        # 是否监听Unity发来的log
        self.listen_log_flag = False

        # 是否将Unity发来的log加到消息列表里
        self.log_list_flag = False

        # 是否让Unity发log
        self.set_send_log_flag(False)

        if not self.is_ios:
            # 是否监听Unity发来的log
            self.listen_log_flag = True

            # 是否将Unity发来的log加到消息列表里
            self.log_list_flag = True

            # 是否让Unity发log
            self.set_send_log_flag(True)

        self.is_monitor = is_monitor

        # self._extend_base_page()

        # 配置表的路径
        self.excelTools = ExcelTools(EXCEL_PATH)

        if self.is_monitor:
            self.monitor = UIMonitor(self)
            self.monitor.start_monitoring(threading.current_thread())

    def get_fishery_id_list(self):
        """函数功能简述
            根据配置表获取渔场id列表
        """
        fishery_id_list = []
        table_data_object_list = self.excelTools.get_table_data_detail(book_name="FISHERIES.xlsm")[0]
        for table_data_object in table_data_object_list:
            if "tpId" not in table_data_object:
                continue
            if "enabled" not in table_data_object:
                continue
            if table_data_object["enabled"] != 1:
                continue
            fishery_id = table_data_object["tpId"]
            fishery_id_list.append(fishery_id)
        return fishery_id_list

    def get_fish_id_list(self, fishery_id):
        """函数功能简述
            根据fishery_id获取该渔场的鱼id列表

        参数:
            fishery_id: 渔场id
        """
        table_data_object = self.excelTools.get_table_data_object_by_key_value(key="tpId", value=fishery_id,
                                                                               book_name="FISHERIES.xlsm")
        fish_list = table_data_object["fish"]
        res_list = []
        for fish in fish_list:
            if not fish:
                continue
            res_list.append(str(fish))
        return res_list

    def get_tpid(self, item_name: str = "", item_icon_name: str = ""):
        """函数功能简述
            根据RESOURCE.xlsm或ITEM_MAIN.xlsm
            以道具名或icon名获取道具tpid列表

        参数:
            item_name和item_icon_name选择一个输入
            item_name: 道具名
            item_icon_name: 图标名

        输出:
            list[str]
        """
        item_tpid_list = []
        book_list = [{"book_name": "RESOURCE.xlsm", "name": "name", "id": "resourceID", "icon": "itemIcon"},
                     {"book_name": "ITEM_MAIN.xlsm", "name": "name", "id": "itemTpId", "icon": "iconName"}]
        for book_dict in book_list:
            book_name = book_dict["book_name"]
            table_data_detail = self.excelTools.get_table_data_detail(book_name=book_name)

            if item_name != "":
                table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key=book_dict["name"],
                                                                                                 value=item_name,
                                                                                                 table_data_detail=table_data_detail)
                if table_data_object_list:
                    for table_data_object in table_data_object_list:
                        item_tpid = table_data_object[book_dict["id"]]
                        item_tpid_list.append(item_tpid)

            if item_icon_name != "":
                table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key=book_dict["icon"],
                                                                                                 value=item_icon_name,
                                                                                                 table_data_detail=table_data_detail)
                if table_data_object_list:
                    for table_data_object in table_data_object_list:
                        item_tpid = table_data_object[book_dict["id"]]
                        item_tpid_list.append(item_tpid)

        return item_tpid_list

    def get_tpid_list(self, item_name_list=None, item_icon_name_list=None):
        """函数功能简述
            以道具名或icon名获取道具tpid列表

        参数:
            item_name_list和item_icon_name_list选择一个输入
            item_name_list: item_name组成的list
            item_icon_name_list: item_icon_name组成的list

        输出:
            list[list[str]]
        """
        item_tpid_list = []
        if item_name_list is not None:
            cur = 0
            while cur < len(item_name_list):
                item_tpid_list.append(self.get_tpid(item_name=item_name_list[cur])[0])
                cur += 1
            return item_tpid_list
        cur = 0
        while cur < len(item_icon_name_list):
            item_tpid_list.append(self.get_tpid(item_icon_name=item_icon_name_list[cur])[0])
            cur += 1
        return item_tpid_list

    def get_unlock_lv(self, system_name):
        """函数功能简述
            从UNLOCK_SYSTEM.xlsm中获取系统解锁等级

        参数:
            item_name_list和item_icon_name_list选择一个输入
            item_name_list: item_name组成的list
            item_icon_name_list: item_icon_name组成的list

        输出:
            list[list[str]]
        """
        table_data_object = self.excelTools.get_table_data_object_by_key_value(key="name", value=system_name,
                                                                               book_name="UNLOCK_SYSTEM.xlsm")
        unlock_lv = int(table_data_object["content"])
        return unlock_lv

    def get_fish_type(self, fish_tpid, table_data_detail=None):
        """函数功能简述
            从FISH.xlsm中获取鱼的体型

        参数:
            fish_tpid: 鱼id

        输出:
            str
            "小"，"中"，"大"，"特大"，"超巨"，"奇珍"，"超奇珍"，"典藏"，"其它"
        """
        if table_data_detail is None:
            table_data_detail = self.excelTools.get_table_data_detail("FISH.xlsm")
        if fish_tpid == '':
            return "钓鱼失败"
        table_data_object = self.excelTools.get_table_data_object_by_key_value(key="tpId", value=fish_tpid,
                                                                               table_data_detail=table_data_detail)

        fishClass = 0
        fishType = 0
        if "fishClass" in table_data_object:
            fishClass = table_data_object["fishClass"]
        if "fishType" in table_data_object:
            fishType = table_data_object["fishType"]
        # index = table_data_object_list["tpId"].index(int(fish_tpid))

        if fishClass == 1:
            if fishType == 1:
                return "小"
            if fishType == 2:
                return "中"
            if fishType == 3:
                return "大"
            if fishType == 4:
                return "特大"
            if fishType == 5:
                return "超巨"
        if fishClass == 2:
            return "奇珍"
        if fishClass == 3:
            return "超奇珍"
        if fishClass == 4:
            return "典藏"
        return "其它"

    def get_fish_type_list(self, fish_list):
        """函数功能简述
            从get_fish_type()方法中获取鱼的体型

        参数:
            fish_list: 鱼id组成的list

        输出:
            list[str]
        """
        table_data_detail = self.excelTools.get_table_data_detail("FISH.xlsm")
        fish_type_list = []
        cur = 0
        while cur < len(fish_list):
            fish_type = self.get_fish_type(fish_tpid=fish_list[cur], table_data_detail=table_data_detail)
            fish_type_list.append(fish_type)
            cur += 1
        return fish_type_list

    # 获取物品数量
    def get_item_count(self, item_name: str = "", item_icon_name: str = "", item_tpid: str = ""):
        """函数功能简述
            获取物品数量

        参数:
            item_name、item_icon_name、item_tpid选择一个输入
            item_name和item_icon_name会转换成item_tpid
            item_name: 物品名
            item_icon_name: 物品图标名
            item_tpid: 物品tpid


        输出:
            int
        """
        if item_tpid != "":
            item_count_list = self.get_item_count_list(item_tpid_list=[item_tpid])
            self.is_single_element(item_count_list)
            return item_count_list[0]
        item_tpid = self.get_tpid(item_name, item_icon_name)[0]
        tpid_list = [item_tpid]
        item_count_list = self.get_item_count_list(item_tpid_list=tpid_list)
        self.is_single_element(item_count_list)
        return item_count_list[0]

    # 设置物品数量
    def set_item_count(self, target_count, item_name: str = "", item_icon_name: str = "", item_tpid: str = ""):
        """函数功能简述
            设定物品数量

        参数:
            item_name、item_icon_name、item_tpid选择一个输入，item_name和item_icon_name会转换成item_tpid
            target_count: 设定数量
            item_name: 物品名
            item_icon_name: 物品图标名
            item_tpid: 物品tpid

        """
        # 参数给的是icon_name或item_name就转换为tpid
        if item_tpid == "":
            item_tpid = self.get_tpid(item_name, item_icon_name)[0]
        item_count = self.get_item_count(item_tpid=item_tpid)
        count = target_count - item_count
        if not isinstance(count, int):
            return
        if count == 0:
            return
        self.cmd(f"add {item_tpid[0]} {item_tpid} {target_count - item_count}")

    def set_item_count_list(self, target_count_list, item_name_list: list = None, item_icon_name_list: list = None,
                            item_tpid_list: list = None):
        """函数功能简述
            批量设定物品数量

        参数:
            item_name_list、item_icon_name_list、item_tpid_list选择一个输入，item_name_list和item_icon_name_list会转换成item_tpid_list
            target_count_list: 设定数量组成的list
            item_name_list: 物品名组成的list
            item_icon_name_list: 物品图标名组成的list
            item_tpid_list: 物品tpid组成的list

        """
        if item_tpid_list is None:
            item_tpid_list = self.get_tpid_list(item_name_list=item_name_list, item_icon_name_list=item_icon_name_list)
        item_count_list = self.get_item_count_list(item_tpid_list=item_tpid_list)
        command_list = []
        cur = 0
        while cur < len(item_tpid_list):
            item_tpid = item_tpid_list[cur]
            target_count = target_count_list[cur]
            item_count = item_count_list[cur]
            count = target_count - item_count
            if not isinstance(count, int):
                cur += 1
                continue
            if count == 0:
                cur += 1
                continue
            command_list.append(f"add {item_tpid[0]} {item_tpid} {count}")
            cur += 1
        self.cmd_list(command_list=command_list)

    # 判断资源是否充足
    def is_resource_enough(self, icon_list, value_list):
        cur = 0
        while cur < len(icon_list):
            item_count = self.get_item_count(item_icon_name=icon_list[cur])
            if item_count < value_list[cur]:
                return False
            cur += 1
        return True

    # 根据图标得到物品数量列表
    def get_item_count_list(self, item_name_list=None, item_icon_name_list=None, item_tpid_list=None):
        """函数功能简述
            批量获取物品数量

        参数:
            item_name、item_icon_name、item_tpid选择一个输入
            item_name和item_icon_name会转换成item_tpid

        输出:
            int
        """
        if item_tpid_list is not None:
            item_count_list = rpcMethodRequest.get_item_count(self.poco, item_tpid_list)
            return item_count_list
        item_tpid_list = self.get_tpid_list(item_name_list=item_name_list, item_icon_name_list=item_icon_name_list)
        item_count_list = rpcMethodRequest.get_item_count(self.poco, item_tpid_list)
        return item_count_list

    # 得到消耗后的物品数量列表
    def get_consumed_item_count_list(self, icon_list, count_list):
        item_count_list = self.get_item_count_list(item_icon_name_list=icon_list)
        cur = 0
        while cur < len(item_count_list):
            item_count_list[cur] -= count_list[cur]
            cur += 1
        return item_count_list

    def cmd(self, command):
        """函数功能简述
            gm命令

        参数:
            command:str
        """
        if not command:
            return
        self.cmd_list(command_list=[command])

    def cmd_list(self, command_list):
        """函数功能简述
            批量gm命令

        参数:
            command_list:list[str]
        """
        if not command_list:
            return
        lua_code = "local ConsolePanel = require('View.Common.ConsolePanel')\n"
        for command in command_list:
            lua_code += f'ConsolePanel:OnPocoCMD("{command}")\n'
        self.lua_console(lua_code)

    def lua_console(self, command):
        """函数功能简述
            lua代码片段

        参数:
            command:str
        """
        if not command:
            return
        self.lua_console_list([command])

    def lua_console_list(self, command_list):
        """函数功能简述
            批量lua代码片段

        参数:
            command_list:list[str]
        """
        if not command_list:
            return
        rpcMethodRequest.lua_console(self.poco, command_list)

    # lua_code_main是lua代码主体
    # lua_code_res是需要接收的部分
    def lua_console_with_response(self, lua_code_main="", lua_code_return=""):
        """函数功能简述
            有返回值的lua代码片段

        参数:
            lua_code_main: lua代码片段的逻辑主体部分（简单情况下为空）
            lua_code_return: 需要返回值的部分
        返回值:
            str
        """
        # 清空消息列表 开始收消息
        self.log_list.clear()
        self.log_list_flag = True
        title = f'<==== [C#] Receive LuaSnippets Response "{lua_code_return}" ====>'

        lua_code = lua_code_main

        if lua_code:
            lua_code += "\n"
        if lua_code_return:
            lua_code += """
function table_to_string(tbl, already_printed)
    if type(tbl) ~= "table" then
        if type(tbl) == "string" then
            return '"'..tbl..'"'
        end
        return tostring(tbl)
    end

    already_printed = already_printed or {}
    if already_printed[tbl] then
        return "<循环引用>"
    end
    already_printed[tbl] = true

    local result = "{"
    local first = true

    -- 先处理数组部分
    local max_index = 0
    for i, v in ipairs(tbl) do
        if not first then result = result.."," end
        first = false
        result = result..table_to_string(v, already_printed)
        max_index = i
    end

    -- 再处理其他键值对
    for k, v in pairs(tbl) do
        if type(k) ~= "number" or k > max_index or k < 1 then
            if not first then result = result.."," end
            first = false
            local key
            if type(k) == "string" and k:match("^[%a_][%w_]*$") then
                key = k
            else
                key = "["..table_to_string(k, already_printed).."]"
            end
            result = result..key.."="..table_to_string(v, already_printed)
        end
    end

    return result.."}"
end
"""
            lua_code += rf"print('{title}',table_to_string({lua_code_return}))"
        # 发送消息
        self.lua_console(lua_code)

        target_log = self.receive_until_get_msg(msg_name="", key_sc=title)

        if not target_log:
            return None

        return target_log.split(title)[1].strip()

    def custom_cmd_list(self, command_list):
        """函数功能简述
            批量自定义的命令

        参数:
            command_list:list[str]
        """
        if not command_list:
            return
        rpcMethodRequest.custom_cmd(self.poco, command_list)

    def custom_cmd(self, command):
        """函数功能简述
            批量自定义的命令

        参数:
            command:str
                autofish (下一杆自动钓鱼)
                setTension x (x的范围在0~1)
                setSceneType x (x=1是pve，x=2是pvp)
        """
        if not command:
            return
        self.custom_cmd_list([command])

    def get_scene_list(self):
        """函数功能简述
            获取当前激活的场景名
        """
        return rpcMethodRequest.get_scene_list(self.poco)

    def get_target_log(self, msg_key):
        """函数功能简述
            在self.log_list中找到包含msg_key的消息

        参数:
            msg_key: 关键词

        返回值: 带关键词的log
        """
        target_log = ""
        for log in self.log_list:
            if msg_key not in log:
                continue
            target_log = log
            break
        return target_log

    def receive_until_get_msg(self, msg_name, time_interval=0.05, timeout=5, key_sc='<==== [Lua] Receive Net Msg "SC'):
        """函数功能简述
            循环接收消息直到找到目标消息

        参数:
            key_sc + msg_name组成关键词
            time_interval: 检测间隔
            timeout: 超时时长

        返回值: 带关键词的log
        """
        cur = 0
        while cur < timeout:
            cur += time_interval
            self.sleep(time_interval)
            # 在最近收集的消息列表中筛出目标消息
            msg_key = key_sc + msg_name
            target_log = self.get_target_log(msg_key)
            if target_log == "":
                continue
            return target_log
        return None

    def set_send_log_flag(self, send_log_flag):
        """函数功能简述
            设置send_log_flag
            如果设置C#发送消息，Python这边把接收消息也打开
        """
        self.send_log_flag = send_log_flag
        rpcMethodRequest.set_send_log_flag(self.poco, send_log_flag)
        if send_log_flag:
            self.wait_msg()

    # 接收C#传来的消息
    def circulate_update(self):
        """函数功能简述
            接收C#传来的消息
        """
        while self.send_log_flag:
            if not self.listen_log_flag:
                time.sleep(0.1)
                continue
            # 每隔一段时间取一下接收区的消息
            try:
                rec = self.poco_listen.agent.c.conn.recv()
            except:
                # print(e)
                break
            for m in rec:
                # 转格式加处理消息
                data = json.loads(m)
                self.handle_message(data)
                self.handle_request(data)
                # 返回消息给C#
                # poco.agent.c.conn.send("ok")
            time.sleep(0.01)

    def handle_message(self, data):
        """函数功能简述
            data消息中筛出'msg'字段的值
            当self.log_list_flag=True时，将'msg'字段的值加到self.log_list中
        """
        if 'msg' not in data:
            return
        msg = data['msg']
        if self.log_list_flag:
            self.log_list.append(msg)
        self.log_list_duel.append(msg)
        netMsg.luaLog.deal_with_msg(msg)

    def handle_request(self, data):
        """函数功能简述
            C#请求Python的函数
            data消息中筛出'method'和'params'字段的值
        """
        if 'method' not in data:
            return
        method = data['method']
        params = data['params']
        self.call_function("common.rpcMethodResponse", method, self, params)

    def wait_msg(self):
        """函数功能简述
            开启线程循环检测消息
        """
        from threading import Thread
        t = Thread(target=self.circulate_update, args=[])
        t.daemon = True
        t.start()

    @staticmethod
    def call_function(module_name, function_name, *args, **kwargs):
        """函数功能简述
            以字符串形式调方法

        参数:
            module_name: 模块名
            function: 方法名
            *args, **kwargs: 方法的参数
        """
        # 动态导入模块
        module = import_module(module_name)
        # 获取函数
        function = getattr(module, function_name)
        # 调用函数并返回结果
        return function(*args, **kwargs)

    def get_drop_item_id_list(self, spot_id):
        """函数功能简述
            获取钓点的出鱼列表

        参数:
            spot_id: 钓点id
        """
        fishDropInfo_list = []
        # 鱼骨tpid转missionConditionID
        table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key="tpId", value=spot_id,
                                                                                         book_name="FISH_SPOT.xlsm")

        for table_data_object in table_data_object_list:
            fishDropInfo = table_data_object["fishDropInfo"]
            for f in fishDropInfo:
                fishDropInfo_list.append(f)

        # 拿到对应钓点的DropID列表
        drop_id_list = []
        for fishDropInfo in fishDropInfo_list:
            if "DropID" not in fishDropInfo:
                continue
            drop_id = fishDropInfo["DropID"]
            drop_id_list.append(drop_id)

        # 鱼骨tpid转missionConditionID
        drop_pack_id_list = []
        table_data_detail = self.excelTools.get_table_data_detail("DROP_PACK.xlsm")
        for drop_id in drop_id_list:
            table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key="dropId",
                                                                                             value=drop_id,
                                                                                             table_data_detail=table_data_detail)
            for table_data_object in table_data_object_list:
                if table_data_object["enabled"] in [0, "0"]:
                    continue
                dropPackId = table_data_object["dropPackId"]
                drop_pack_id_list.append(dropPackId)

        # drop_pack_id转item_id
        item_id_list = []
        table_data_detail = self.excelTools.get_table_data_detail("DROP_ENTITY.xlsm")
        for drop_pack_id in drop_pack_id_list:
            table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key="dropPackId",
                                                                                             value=int(drop_pack_id),
                                                                                             table_data_detail=table_data_detail)
            for table_data_object in table_data_object_list:
                if table_data_object["enabled"] in [0, "0"]:
                    continue
                itemID = table_data_object["itemID"]
                item_id_list.append(itemID)

        return item_id_list

    def fish_bone_to_fish(self, fish_bone_id):
        """函数功能简述
            获得鱼骨id对应的鱼id

        参数:
            fish_bone_id: 鱼骨id
        """
        # 鱼骨tpid转missionConditionID
        table_data_object = self.excelTools.get_table_data_object_by_key_value(key="triggerKeyS", value=fish_bone_id,
                                                                               book_name="MISSION_CONDITION.xlsm")
        mission_condition_id = table_data_object["missionConditionID"]

        # missionConditionID转鱼id
        table_data_object = self.excelTools.get_table_data_object_by_key_value(key="startConditionId",
                                                                               value=mission_condition_id,
                                                                               book_name="FISH_STATE.xlsm")
        fish_id = table_data_object["fishChange"][0]["fish"]

        return str(fish_id)

    def get_spot_id_list(self, fishery_id):
        """函数功能简述
            获得渔场的钓点id列表

        参数:
            fishery_id: 钓场id
        """
        table_data_object_activity_double_week = self.excelTools.get_table_data_object_by_key_value(key="fishSceneTpId",
                                                                                                    value=fishery_id,
                                                                                                    book_name="ACTIVITY_DOUBLE_WEEK.xlsm")
        if "TimerId" not in table_data_object_activity_double_week:
            return table_data_object_activity_double_week["fishSpot"], False
        timer_id = table_data_object_activity_double_week["TimerId"]
        table_data_object_timer_main = self.excelTools.get_table_data_object_by_key_value(key="timerID", value=timer_id,
                                                                                          book_name="TIMER_MAIN.xlsm")
        open_time = table_data_object_timer_main["openTime"]
        open_time = datetime.strptime(open_time, '%Y-%m-%d %H:%M:%S')
        open_time = int(time.mktime(open_time.timetuple()))
        end_time = table_data_object_timer_main["endTime"]
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        end_time = int(time.mktime(end_time.timetuple()))
        cur_time = time.time()
        if cur_time > end_time:
            return table_data_object_activity_double_week["fishSpotB"], False
        if cur_time > open_time:
            return table_data_object_activity_double_week["fishSpotB"], True
        return table_data_object_activity_double_week["fishSpot"], False


if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="b6h65hd64p5pxcyh")
    # "127.0.0.1:21613"
    # "b6h65hd64p5pxcyh"
    # "TimeMgr:GetServerTime()"
    # t = bp.lua_console_with_response(lua_code_print="_G.PassiveNewbieGuideEnum")
    # bp.cmd_list(["levelupto 69", "guideskip"])
    # bp.sleep(1)

    # bp.go_to_panel("TournamentsPanel")
    bp.go_home()

    # bp.cmd_list(["guideskip", "levelupto 90"])
    # bp.cmd("levelupto 12")
    # bp.lua_console('PanelMgr:OpenPanel("HomePanel")')
    # bp.set_text(element_data={"locator":"UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_id>value"}, text="1000002002")
    bp.connect_close()

