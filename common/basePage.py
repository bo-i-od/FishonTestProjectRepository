import json
from importlib import import_module

from airtest.core.helper import G
from poco.drivers.unity3d.device import UnityEditorWindow

import netMsg.luaLog
from tools.excelRead import ExceTools
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

from configs.pathConfig import EXCEL_PATH

class BasePage:
    def __init__(self, serial_number=None, dev=None):
        # unity窗口使用UnityEditorWindow()
        # 手机使用connect_device("android://127.0.0.1:5037/设备号")

        # 是否在安卓手机, Unity需要改为False
        self.is_android = False

        # 是否测试会拉起支付的按钮
        self.is_pay = True

        # 是否截图记录
        self.record = False

        # 是否开启战斗倍速
        self.is_time_scale = False

        # 是否打印日志
        self.is_debug_log = False

        # 是否监听Unity发来的log
        self.listen_log_flag = True

        # 是否将Unity发来的log加到消息列表里
        self.log_list_flag = True

        self._send_log_flag = False

        # 默认端口 5001
        addr = ('', 5001)
        addr_listen = ('', 5002)
        self.dev = dev
        if self.dev is None:
            print("self.dev is None")
            self.dev = self.get_device(serial_number=serial_number)

        self.poco = UnityPoco(addr, device=dev)
        self.poco_listen = UnityPoco(addr_listen, device=dev)
        self.screen_w, self.screen_h = self.poco.get_screen_size()  # 获取屏幕尺寸

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
        # 配置表的路径
        self.excelTools = ExceTools(EXCEL_PATH)

        # 是否让Unity发log
        self.set_send_log_flag(True)

        # 消息储存队列
        self.log_list = []


    def get_device(self, serial_number=None):
        # pc端
        if not self.is_android:
            dev = UnityEditorWindow()
            return dev

        # 已连接
        try:
            dev = G.DEVICE
            return dev
        # 未连接，新建连接
        except Exception as e:
            print(e)
            print("进行设备连接")
        if serial_number is None:
            serial_number = "127.0.0.1:21503"
        dev = connect_device(f"android://127.0.0.1:5037/{serial_number}")
        # dev = connect_device("android://127.0.0.1:5037/b6h65hd64p5pxcyh")
        # dev = connect_device("android://127.0.0.1:5037/28cce18906027ece")
        return dev

    # 断开poco连接
    def connect_close(self):
        self._send_log_flag = False
        self.poco.agent.c.conn.close()
        self.poco_listen.agent.c.conn.close()


    # 开启调试打印再打印
    def debug_log(self, *msg):
        if self.is_debug_log:
            print(*msg)

    # 判断列表是不是长度为1，不为1会报错
    @staticmethod
    def is_single_element(element_list: list):
        if len(element_list) == 0:
            raise FindNoElementError
        elif len(element_list) > 1:
            raise PluralElementError

    # 把路径和后代路径合成为当前要用的的element_data
    @staticmethod
    def get_element_data(element_data, offspring_path):
        element_data_copy = element_data
        if offspring_path != "":
            element_data_copy = element_data.copy()
            element_data_copy["locator"] = element_data_copy["locator"] + '>' + offspring_path
        return element_data_copy

    # 判断元素是否存在
    # 元素若存在返回的列表不为空
    def exist(self, object_id=0, element_data=None, element_data_list: list = None, offspring_path=""):
        if object_id != 0:
            if self.get_offspring_id_list(object_id_list=[object_id], offspring_path=offspring_path):
                return True
            return False
        if element_data_list is not None:
            return self.get_offspring_id_list(element_data_list=element_data_list, offspring_path=offspring_path)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        if self.exist(element_data_list=[element_data_copy])[0]:
            return True
        return False


    # 得到元素的Instance Id列表
    def get_object_id_list(self, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if element_data_list is not None:
            return rpcMethodRequest.get_object_id(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_object_id_list(element_data_list=[element_data_copy])[0]

    # 得到元素的Instance Id
    def get_object_id(self, element_data: dict, offspring_path=""):
        element_data_copy = self.get_element_data(element_data, offspring_path)
        object_id_list = self.get_object_id_list(element_data=element_data_copy)
        self.is_single_element(object_id_list)
        return object_id_list[0]

    # # 传入子物体名字可以获取子物体，为空字符串就获得全部子物体
    # def get_child_id_list(self, child_name="", object_id=0, object_id_list=None, element_data=None):
    #     if object_id_list is not None:
    #         child_id_list = []
    #         for object_id in object_id_list:
    #             child_id_list_temp = self.get_child_id_list(child_name=child_name, object_id=object_id)
    #             child_id_list += child_id_list_temp
    #         return child_id_list
    #     if object_id != 0:
    #         return rpcMethodRequest.get_child_id_by_id(self.poco, object_id, child_name)
    #     return rpcMethodRequest.get_child_id(self.poco, element_data, child_name)
    #
    # def get_child_id(self, child_name="",object_id=0, element_data=None):
    #     child_id_list = self.get_child_id_list(child_name, object_id=object_id, element_data=element_data)
    #     self.is_single_element(child_id_list)
    #     return child_id_list[0]

    # 得到后代的Instance Id
    def get_offspring_id_list(self, offspring_path, object_id=0, object_id_list=None, element_data=None, element_data_list: list = None):
        if object_id_list is not None:
            return rpcMethodRequest.get_offspring_id_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_offspring_id_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            element_data_copy_list = []
            cur = 0
            while cur < len(element_data_list):
                element_data_copy = self.get_element_data(element_data_list[cur], offspring_path)
                element_data_copy_list.append(element_data_copy)
                cur += 1
            return self.get_object_id_list(element_data_list=element_data_copy_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_object_id_list(element_data_list=[element_data_copy])[0]

    def get_offspring_id(self, offspring_path, object_id=0, element_data=None):
        offspring_id_list = self.get_offspring_id_list(offspring_path, object_id=object_id, element_data=element_data)
        self.is_single_element(offspring_id_list)
        return offspring_id_list[0]

    # 得到指定元素/元素列表的父节点
    def get_parent_id_list(self, object_id=0, object_id_list=None, element_data=None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_parent_id_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_parent_id_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_parent_id(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_parent_id_list(element_data_list=[element_data_copy])[0]

    def get_parent_id(self, object_id=0, element_data=None, offspring_path=""):
        if object_id != 0:
            parent_id_list = self.get_parent_id_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(parent_id_list)
            return parent_id_list[0]
        parent_id_list = self.get_parent_id_list(element_data=element_data, offspring_path=offspring_path)
        self.is_single_element(parent_id_list)
        return parent_id_list[0]

    # 获得文本
    def get_text_list(self, object_id=0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_text_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_text_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_text(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_text_list(element_data_list=[element_data_copy])[0]

    def get_text(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            text_list = self.get_text_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(text_list)
            return text_list[0]
        element_data_copy = self.get_element_data(element_data, offspring_path)
        text_list = self.get_text_list(element_data=element_data_copy)
        self.is_single_element(text_list)
        return text_list[0]

    # 修改文本
    def set_text_list(self, object_id=0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, text="",
                      offspring_path=""):
        if object_id_list is not None:
            rpcMethodRequest.set_text_by_id(self.poco, object_id_list, offspring_path, text)
            return
        if object_id != 0:
            self.set_text_list(object_id_list=[object_id], offspring_path=offspring_path, text=text)
            return
        if element_data_list is not None:
            rpcMethodRequest.set_text(self.poco, element_data_list, text)
            return
        element_data_copy = self.get_element_data(element_data, offspring_path)
        self.set_text_list(element_data_list=[element_data_copy], text=text)

    def set_text(self, object_id: int = 0, element_data: dict = None, text="", offspring_path=""):
        if object_id != 0:
            self.set_text_list(object_id=object_id, offspring_path=offspring_path, text=text)
            return
        element_data_copy = self.get_element_data(element_data, offspring_path)
        self.set_text_list(element_data=element_data_copy, text=text)

    # 获取图标名
    def get_icon_list(self, object_id=0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            icon_list = rpcMethodRequest.get_img_name_by_id(self.poco, object_id_list, offspring_path)
            resource.check_icon_list(icon_list)
            return icon_list
        if object_id != 0:
            return self.get_icon_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            res = rpcMethodRequest.get_img_name(self.poco, element_data_list)
            cur = 0
            while cur < len(res):
                icon_list = res[cur]
                resource.check_icon_list(icon_list)
                cur += 1
            return res
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_icon_list(element_data_list=[element_data_copy])[0]

    def get_icon(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            icon_list = self.get_icon_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(icon_list)
            icon = resource.check_icon(icon_list[0])
            return icon
        element_data_copy = self.get_element_data(element_data, offspring_path)
        icon_list = self.get_icon_list(element_data=element_data_copy)
        self.is_single_element(icon_list)
        return icon_list[0]

    # 获取节点名称
    def get_name_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_name_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_name_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_name(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_name_list(element_data_list=[element_data_copy])[0]

    def get_name(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            name_list = self.get_name_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(name_list)
            return name_list[0]
        element_data_copy = self.get_element_data(element_data, offspring_path)
        name_list = self.get_name_list(element_data=element_data_copy)
        self.is_single_element(name_list)
        return name_list[0]

    # 获取滑条值
    def get_slider_value_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_slider_value_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_slider_value_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_slider_value(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_slider_value_list(element_data_list=[element_data_copy])[0]

    # 获取到的滑条值是float类型，值在0~1
    def get_slider_value(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            slider_value_list = self.get_slider_value_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(slider_value_list)
            return slider_value_list[0]
        element_data_copy = self.get_element_data(element_data, offspring_path)
        slider_value_list = self.get_slider_value_list(element_data=element_data_copy)
        self.is_single_element(slider_value_list)
        return slider_value_list[0]

    # 获取下拉列表当前值
    def get_dropdown_value(self, element_data):
        return rpcMethodRequest.get_dropdown_value(self.poco, [element_data])[0]

    def set_dropdown_value(self, element_data, index):
        rpcMethodRequest.set_dropdown_value(self.poco, [element_data], index)

    # 获取元素尺寸
    def get_size_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_size_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_size_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_size(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_size_list(element_data_list=[element_data_copy])[0]

    def get_size(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            size_list = self.get_size_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(size_list)
            return size_list[0]
        element_data_copy = self.get_element_data(element_data, offspring_path)
        size_list = self.get_size_list(element_data=element_data_copy)
        self.is_single_element(size_list)
        return size_list[0]

    # 获取勾选状态
    def get_toggle_is_on_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_toggle_is_on_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_toggle_is_on_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_toggle_is_on(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_toggle_is_on_list(element_data_list=[element_data_copy])[0]

    def get_toggle_is_on(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            toggle_is_on_list = self.get_toggle_is_on_list(object_id=object_id, offspring_path=offspring_path)
            self.is_single_element(toggle_is_on_list)
            return toggle_is_on_list[0]
        element_data_copy = self.get_element_data(element_data, offspring_path)
        toggle_is_on_list = self.get_toggle_is_on_list(element_data=element_data_copy)
        self.is_single_element(toggle_is_on_list)
        return toggle_is_on_list[0]

    # 获取位置
    def get_position_list(self, object_id: int = 0, object_id_list: list = None, element_data: dict = None, element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            return rpcMethodRequest.get_position_by_id(self.poco, object_id_list, offspring_path)
        if object_id != 0:
            return self.get_position_list(object_id_list=[object_id], offspring_path=offspring_path)
        if element_data_list is not None:
            return rpcMethodRequest.get_position(self.poco, element_data_list)
        element_data_copy = self.get_element_data(element_data, offspring_path)
        return self.get_position_list(element_data_list=[element_data_copy])[0]

    def get_position(self, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            position_list = rpcMethodRequest.get_position_by_id(self.poco, [object_id], offspring_path)
            self.is_single_element(position_list)
            return position_list[0]
        element_data_copy = self.get_element_data(element_data, offspring_path)
        position_list = self.get_position_list(element_data=element_data_copy)
        self.is_single_element(position_list)
        return position_list[0]

    # 元素长按
    def press(self, object_id: int = 0, element_data: dict = None, duration: float = 2.0, offspring_path=""):
        element_data_copy = self.get_element_data(element_data, offspring_path)
        position = self.get_position(object_id=object_id, element_data=element_data_copy)
        self.press_position(position, duration)

    # 位置长按
    def press_position(self, position, duration: float = 2.0):
        self.poco.long_click(position, duration)

    # 位置点击
    # position=[x,y]
    # 0<=x<=1, 0<=y<=1
    def click_position_base(self, position):
        if not (0 <= position[0] <= 1) or not (0 <= position[1] <= 1):
            raise InvalidOperationError('Click position out of screen. pos={}'.format(repr(position)))
        # 点击前进行截图保存
        if self.record:
            img = self.get_full_screen_shot()
            self.draw_circle(img, (position[0], position[1]))
            self.save_img(img)
        self.poco.agent.input.click(position[0], position[1])

    def draw_circle(self, img, center_coordinates):
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
        # 清除一遍弹窗
        self.clear_popup(ignore_set)
        self.click_position_base(position)

    # 元素点击
    def click_element(self, object_id: int = 0, element_data: dict = None, offspring_path="", ignore_set=None, focus=None):
        if object_id != 0:
            position = self.get_position(object_id=object_id)
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
        element_data_copy = self.get_element_data(element_data, offspring_path)
        self.clear_popup(ignore_set)
        position_list = self.get_position_list(element_data=element_data_copy)
        self.is_single_element(position_list)
        self.click_position_base(position_list[0])
        return position_list[0]

    # 在b元素出现前一直尝试点击a元素
    def click_a_until_b_appear(self, element_data_a: dict, element_data_b: dict):
        while not self.exist(element_data=element_data_b):
            self.click_element_safe(element_data=element_data_a)
            self.sleep(0.5)

    # 第一次a为列表第1个元素 b为第2个元素
    # 第二次a为列表第2个元素 b为第3个元素
    # 以此类推进行click_a_until_b_appear
    def click_a_until_b_appear_list(self, perform_list: list):
        cur = 0
        while cur < len(perform_list) - 1:
            # print(perform_list[cur], perform_list[cur + 1])
            self.click_a_until_b_appear(perform_list[cur], perform_list[cur + 1])
            cur += 1

    # 在b元素消失前一直尝试点击a元素
    def click_a_until_b_disappear(self, element_data_a: dict, element_data_b: dict, interval: float = 0.5):
        self.wait_for_appear(element_data_b, is_click=False)
        while self.exist(element_data=element_data_b):
            self.click_element_safe(element_data=element_data_a)
            self.sleep(interval)

    # 在a元素消失前一直尝试点击a元素
    def click_until_disappear(self, element_data: dict = None, interval: float = 0.5):
        self.click_a_until_b_disappear(element_data_a=element_data, element_data_b=element_data, interval=interval)

    # 等待指定元素出现
    def wait_for_appear(self, element_data: dict, is_click: bool = False, interval: float = 0.2, timeout=120):
        cur = 0
        position = []
        while cur < timeout:
            position = self.get_position_list(element_data=element_data)
            if position:
                break
            self.sleep(interval)
            cur += interval
        if not position:
            return
        if not is_click:
            return
        self.click_position(position[0])

    # 等待指定元素消失
    def wait_for_disappear(self, element_data: dict, interval: float = 0.1):
        while self.exist(element_data=element_data):
            self.sleep(interval)

    # 安全点击
    # 判断元素存在后再点击
    def click_element_safe(self, object_id: int = 0, element_data: dict = None):
        position_list = self.get_position_list(object_id=object_id, element_data=element_data)
        if not position_list:
            return
        try:
            self.click_position_base(position_list[0])
        except:
            pass
            # print("超出屏幕范围，没有进行点击")
        # print(f"{object_id, element_data}元素不存在，没有进行点击")

    # # 尝试点击
    # # 如果点击失败就看是否有弹窗遮挡
    # # 关闭弹窗后会再次点击
    # def try_click_element(self, object_id: int = 0, element_data: dict = None):
    #
    #     try:
    #         self.click_element(object_id=object_id, element_data=element_data)
    #     except PluralElementError:
    #         print("请检查元素的定位信息")
    #     except FindNoElementError:
    #         print("正在检查是否有弹窗遮挡")
    #         self.clear_popup_once()
    #         self.try_click_element(object_id=object_id, element_data=element_data)
    #         return

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
        if ignore_set is None:
            ignore_set = set()
        panel_name_list = self.get_name_list(element_data=ElementsData.Panels)
        pop_window_set = set(panel_name_list) & JumpData.pop_window_set - ignore_set
        if not pop_window_set:
            return True
        for panel_name in pop_window_set:
            if panel_name == "FishBagPanel":
                self.click_position_base([0.5, 0.5])
                self.sleep(0.5)
            for close_element in JumpData.panel_close_dict[panel_name]:
                self.click_element_safe(element_data=close_element)
                self.sleep(1)
        return False

    def clear_popup(self, ignore_set=None):
        while True:
            res = self.clear_popup_once(ignore_set)
            if res:
                break

    # 执行清除弹窗直到elements_data出现
    def clear_popup_until_appear(self, elements_data):
        while not self.exist(element_data=elements_data):
            self.clear_popup_once()
            self.sleep(0.5)

    # 回到主界面
    def go_home(self, cur_panel=None):
        cur = 0
        at_home_flag = True
        while at_home_flag:
            self.clear_panel_except_home()
            self.sleep(0.5)
            cur += 1
            if cur > 30:
                raise FindNoElementError
            at_home_flag = (not self.exist(element_data=ElementsData.Home.HomePanel))
            if cur_panel is not None:
                at_home_flag = at_home_flag or self.exist(element_data=JumpData.panel_dict[cur_panel])

    # 去指定界面
    def go_to_panel(self, panel):
        if self.exist(element_data=JumpData.panel_dict[panel]):
            return
        self.go_home()
        while not self.exist(element_data=JumpData.panel_dict[panel]):
            self.clear_popup_once()
            for element_data in JumpData.panel_open_dict[panel]:
                self.click_element_safe(element_data=element_data)
                self.sleep(0.5)

    # 关除了主界面的界面
    def clear_panel_except_home(self):
        panel_name_list = self.get_name_list(element_data=ElementsData.Panels)
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
        self.clear_popup(ignore_set)
        self.swipe_base(object_id, element_data, point_start, point_end, t, offspring_path)

    def swipe_base(self, object_id: int = 0, element_data: dict = None, point_start=None, point_end=None, t: float = 0.5,
              offspring_path=""):
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

    # 截取屏幕
    # x,y为坐标
    # w,h为宽高
    def get_screen_shot(self, x, y, w, h):
        img_b64encode, fmt = rpcMethodRequest.screen_shot(self.poco, x, y, w, h)
        if fmt.endswith('.deflate'):
            fmt = fmt[:-len('.deflate')]
            imgdata = base64.b64decode(img_b64encode)
            imgdata = zlib.decompress(imgdata)
            img_b64encode = base64.b64encode(imgdata)
        img_b64decode = base64.b64decode(img_b64encode)  # base64解码
        img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
        img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
        return img

    # 保存截图到report
    def save_img(self, img, img_name=""):
        path = f"{self.root_dir}/report"  # 输入文件夹地址
        num_png = len(os.listdir(path))  # 读入文件夹,统计文件夹中的文件个数
        cur = num_png
        cv2.imwrite(path + f'/{img_name}{cur}.jpg', img)

    # 整屏截取
    def get_full_screen_shot(self):
        img = self.get_screen_shot(self.screen_w * 0.5, self.screen_h * 0.5, self.screen_w, self.screen_h)
        return img

    # 对指定元素进行截取
    def get_element_shot(self, element_data: dict, offspring_path=""):
        element_data_copy = self.get_element_data(element_data, offspring_path)
        ui_x, ui_y = self.get_position(element_data=element_data_copy)
        ui_w, ui_h = self.get_size(element_data=element_data_copy)
        ui_x, ui_y = int(ui_x * self.screen_w), int(ui_y * self.screen_h)
        ui_w, ui_h = int(ui_w * self.screen_w), int(ui_h * self.screen_h)
        img = self.get_screen_shot(ui_x, ui_y, ui_w, ui_h)
        return img

    # 获取物品数量
    def get_item_count(self, item_name: str = "", item_icon_name: str = "", item_tpid: str = ""):
        if item_tpid != "":
            item_count_list = self.get_item_count_list(item_tpid_list=[item_tpid])
            self.is_single_element(item_count_list)
            return item_count_list[0]
        item_tpid = self.get_tpid(item_name, item_icon_name)
        tpid_list = [item_tpid]
        item_count_list = self.get_item_count_list(item_tpid_list=tpid_list)
        self.is_single_element(item_count_list)
        return item_count_list[0]

    def get_tpid(self, item_name: str = "", item_icon_name: str = ""):
        item_tpid = ""
        book_list = self.excelTools.get_book_list()
        for book_dict in book_list:
            worksheet = self.excelTools.get_worksheet(book_dict["book_name"], "模板数据")
            if item_name != "":
                res = self.excelTools.same_row_different_column_convert(worksheet, book_dict["name"], book_dict["id"],
                                                                        item_name)
                if res is not None:
                    item_tpid = res
                    break
            if item_icon_name != "":
                res = self.excelTools.same_row_different_column_convert(worksheet, book_dict["icon"], book_dict["id"],
                                                                        item_icon_name)
                if res is not None:
                    item_tpid = res
                    break
        return str(item_tpid)

    def get_tpid_list(self, item_name_list=None, item_icon_name_list=None):
        item_tpid_list = []
        if item_name_list is not None:
            cur = 0
            while cur < len(item_name_list):
                item_tpid_list.append(self.get_tpid(item_name=item_name_list[cur]))
                cur += 1
            return item_tpid_list
        cur = 0
        while cur < len(item_icon_name_list):
            item_tpid_list.append(self.get_tpid(item_icon_name=item_icon_name_list[cur]))
            cur += 1
        return item_tpid_list

    # 设置物品数量
    def set_item_count(self, target_count, item_name: str = "", item_icon_name: str = "", item_tpid: str = ""):
        # 参数给的是icon_name或item_name就转换为tpid
        if item_tpid == "":
            item_tpid = self.get_tpid(item_name, item_icon_name)
        item_count = self.get_item_count(item_tpid=item_tpid)
        count = target_count - item_count
        if not isinstance(count, int):
            return
        if count == 0:
            return
        self.cmd(f"add {item_tpid[0]} {item_tpid} {target_count - item_count}")

    def set_item_count_list(self, target_count_list, item_name_list: list=None, item_icon_name_list: list=None, item_tpid_list: list=None):
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
        if item_tpid_list is not None:
            item_count_list = rpcMethodRequest.get_item_count(self.poco, item_tpid_list)
            return item_count_list
        item_tpid_list = self.get_tpid_list(item_name_list=item_name_list, item_icon_name_list=item_icon_name_list)
        item_count_list = rpcMethodRequest.get_item_count(self.poco, item_tpid_list)
        return item_count_list

    # 得到消耗后的物品数量列表
    def get_cosumed_item_count_list(self, icon_list, count_list):
        item_count_list = self.get_item_count_list(item_icon_name_list=icon_list)
        cur = 0
        while cur < len(item_count_list):
            item_count_list[cur] -= count_list[cur]
            cur += 1
        return item_count_list

    def cmd_list(self, command_list):
        if not command_list:
            return
        if command_list is None:
            return
        rpcMethodRequest.cmd(self.poco, command_list)

    def cmd(self, command):
        if command == "":
            return
        if command is None:
            return
        self.cmd_list(command_list=[command])

    def lua_console_list(self, command_list):
        if not command_list:
            return
        if command_list is None:
            return
        rpcMethodRequest.lua_console(self.poco, command_list)

    def lua_console(self, command):
        if command == "":
            return
        if command is None:
            return
        self.lua_console_list([command])

    def custom_cmd_list(self, command_list):
        if not command_list:
            return
        if command_list is None:
            return
        rpcMethodRequest.custom_cmd(self.poco, command_list)

    def custom_cmd(self, command):
        if command == "":
            return
        if command is None:
            return
        self.custom_cmd_list([command])

    def click_button(self, element_data: dict = None, element_data_list: list = None):
        if element_data_list is not None:
            rpcMethodRequest.click_button(self.poco, element_data_list)
            return
        self.click_button(element_data_list=[element_data])

    # kind包含up，down，click
    def ray_input(self, target_name: str, kind: str, element_data:dict = None,element_data_list: list = None):
        if element_data_list is not None:
            rpcMethodRequest.ray_input(self.poco, element_data_list, target_name, kind)
            return
        self.ray_input(target_name=target_name, kind=kind,element_data_list=[element_data])

    # 设定节点激活状态
    def set_object_active_list(self, active, object_id=0, object_id_list: list = None, element_data: dict = None,element_data_list: list = None, offspring_path=""):
        if object_id_list is not None:
            rpcMethodRequest.set_object_active_by_id(self.poco, object_id_list, offspring_path, active)
            return
        if object_id != 0:
            self.set_object_active_list(active=active, object_id_list=[object_id], offspring_path=offspring_path)
            return
        if element_data_list is not None:
            rpcMethodRequest.set_object_active(self.poco, element_data_list, active)
            return
        element_data_copy = self.get_element_data(element_data, offspring_path)
        self.set_object_active_list(active=active, element_data_list=[element_data_copy])

    def set_object_active(self, active, object_id: int = 0, element_data: dict = None, offspring_path=""):
        if object_id != 0:
            self.set_object_active_list(active=active, object_id=object_id, offspring_path=offspring_path)
            return
        element_data_copy = self.get_element_data(element_data, offspring_path)
        rpcMethodRequest.set_object_active(self.poco, element_data_copy, active)

    # 设置时间缩放
    def set_time_scale(self, time_scale=5):
        if not self.is_time_scale:
            return
        rpcMethodRequest.set_time_scale(self.poco, time_scale)

    def get_scene_list(self):
        return rpcMethodRequest.get_scene_list(self.poco)

    def set_send_log_flag(self, send_log_flag):
        self._send_log_flag = send_log_flag
        rpcMethodRequest.set_send_log_flag(self.poco, send_log_flag)
        if send_log_flag:
            self.wait_msg()

    # 休息t秒
    @staticmethod
    def sleep(t: float):
        time.sleep(t)

    # 键盘输入
    @staticmethod
    def send_key(key: str):
        pyautogui.typewrite(key)

    # 接收C#传来的消息
    def circulate_update(self):
        while self._send_log_flag:
            if not self.listen_log_flag:
                self.sleep(0.1)
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
        if 'msg' not in data:
            return
        msg = data['msg']
        if self.log_list_flag:
            self.log_list.append(msg)
        netMsg.luaLog.deal_with_msg(msg)

    def handle_request(self, data):
        if 'method' not in data:
            return
        method = data['method']
        params = data['params']
        self.call_function("common.rpcMethodResponse", method, self, params)

    def wait_msg(self):
        from threading import Thread
        t = Thread(target=self.circulate_update, args=[])
        t.daemon = True
        t.start()

    @staticmethod
    def call_function(module_name, function_name, *args, **kwargs):
        # 动态导入模块
        module = import_module(module_name)
        # 获取函数
        function = getattr(module, function_name)
        # 调用函数并返回结果
        return function(*args, **kwargs)




if __name__ == '__main__':
    bp = BasePage()
    bp.cmd("uptable")
    # bp.clear_popup_once()

    bp.connect_close()
    # while True:
    #     # a = bp.get_object_id_list(element_data=ElementsData.Login.btn_login)
    #     bp.sleep(1)

    # b = bp.poco2.agent.c.call("GetObjectId", ElementsData.Login.btn_login)

    # lua_code = ""
    # bp.lua_console(lua_code)


    # a = bp.get_item_count(item_tpid="100200")
    # print(a)
    # bp.cmd("mode 400301 301013")
    # "mode 400312 390116"
    # bp.cmd("mode 400302 390015")
    # bp.cmd_list(["add 1 100200 1000000", ""])
    # serial_number = "127.0.0.1:21593"
    # dev = connect_device(f"android://127.0.0.1:5037/{serial_number}")
    # poco = AndroidUiautomationPoco()
    # poco()
    # a = bp.excelTools.get_table_data("ACHIEVEMENT_CATEGORY.xlsm")
    #
    # print(a)
    # cur = 0
    # phone = ""
    # while cur < 8:
    #     r = random.randint(0,9)
    #     phone += str(r)
    #     cur += 1
    # print(phone)
    #
    # cur = 0
    # password = ""
    # while cur < 6:
    #     r = random.randint(0,9)
    #     password += str(r)
    #     cur += 1
    # print(password)
    # lv = 1
    # while lv < 60:
    #     a = bp.excelTools.get_exp_limit(lv)
    #     print(lv, a)
    #     lv += 1


    # bp.go_home(cur_panel="QuestionnairePanel")
    # bp.ray_input(element_data=ElementsData.Battle.joystick, target_name="BattlePanel", kind="down")
    # bp.sleep(1)
    # bp.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="up")
    # bp.sleep(0.2)
    # bp.ray_input(element_data=ElementsData.Home.btn_add_100000, target_name="btn_add", kind="up")
    # bp.ray_click(position[0], position[1])
    #
    # res = bp.get_item_count_list(item_tpid_list=["100100", "100000", "207004", "211091"])
    # print(res)


    # bp.go_to_panel("BattlePassPanel")
    # a= bp.get_object_id_list(element_data= {"locator": "UICanvas>Default>>>>btn_cast>btn_normal"})
    # print(a)
    # img = bp.get_full_screen_shot()
    # bp.save_img(img, "306006")
    # target_count_list = [100]
    # item_tpid_list = ["100100"]
    # bp.set_item_count_list(target_count_list=target_count_list, item_tpid_list=item_tpid_list)
    # rpcMethodRequest.set_btn_enabled(bp.poco, element=ElementsData.FishCardUpgrade.FishCardUpgradePanel,
    # enabled=True)
    # screen_h = bp.screen_h
    # screen_w = bp.screen_w
    # step = 50
    # x = 0
    # while x < screen_w:
    #     y = 0
    #     while y < screen_h:
    #         bp.click_position([x/screen_w, y/screen_h])
    #         y += step
    #     x += step

    # bp.lua_console('PanelMgr:OpenPanel("HomePanel")')
    # bp.get_item_count(item_icon_name="achv_group_icon_8")
    # print(get_text(bp.poco,ElementsData.BattlePass.btn_task_text))
    # print(get_slider_value(bp.poco,ElementsData.PlayerSetting.options_music))
    # action_list = [
    #     lambda: bp.go_to_panel("PVPHallPanel")]
    # bp.try_actions(action_list=action_list)
    # print(bp.get_object_id_list(element_data=ElementsData.PVPHall.entrance_list))
