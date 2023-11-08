from poco.drivers.unity3d import UnityPoco
from poco.drivers.unity3d.device import UnityEditorWindow
from tools.excelRead import ExceTools
import time
import pyautogui
import base64
import cv2
import numpy as np
import os
from configs.elementsData import ElementsData
from common.error import *
from poco.drivers.unity3d import UnityPoco
from airtest.core.api import connect_device
from tools import rpcMethod


class BasePage:
    def __init__(self):
        # unity窗口使用UnityEditorWindow()
        # 手机使用connect_device("android://127.0.0.1:5037/设备号")
        dev = UnityEditorWindow()
        # dev = connect_device("android://127.0.0.1:5037/127.0.0.1:21573")
        # make sure your poco-sdk in the game runtime listens on the following port.
        # 默认端口 5001
        # IP is not used for now
        addr = ('', 5002)
        self.poco = UnityPoco(addr, device=dev)
        self.screen_w, self.screen_h = self.poco.get_screen_size()  # 获取屏幕尺寸
        self.excelTools = ExceTools("C:/trunk/datapool/策划模板导出工具/")
        self.pop_window_dict, self.pop_window_close_dict = self.set_pop_window_dict()  # 设定弹窗及其关闭方式
        self.is_pay = True

    # pop_window_dict存放弹窗的ElementsData
    # pop_window_close_dict存放弹窗对应的关闭按钮的ElementsData
    @staticmethod
    def set_pop_window_dict():
        pop_window_dict = {"FishBagPanel":ElementsData.FishBag.FishBagPanel,
                           "BaitAndRodShowPanel":ElementsData.BaitAndRodShow.BaitAndRodShowPanel,
                           }
        pop_window_close_dict = {"FishBagPanel":ElementsData.FishBag.tap_to_continue,
                                 "BaitAndRodShowPanel":ElementsData.BaitAndRodShow.closeArea
                                 }
        return pop_window_dict, pop_window_close_dict

    # 判断列表是不是长度为1，不为1会报错
    @staticmethod
    def is_single_element(element_list: list):
        if len(element_list) == 0:
            raise FindNoElementError
        elif len(element_list) > 1:
            raise PluralElementError

    # 判断元素是否存在
    def exist(self, object_id=0, element_data=None):
        if object_id != 0:
            if rpcMethod.get_object_id_by_id(self, object_id):
                return True
            return False
        if len(self.get_object_id_list(element_data=element_data)) > 0:
            return True
        return False

    def get_object_id_list(self, element_data: dict):
        object_id_list = rpcMethod.get_object_id(self, element_data)
        return object_id_list

    def get_object_id(self, element_data: dict):
        object_id_list = self.get_object_id_list(element_data=element_data)
        self.is_single_element(object_id_list)
        return object_id_list[0]

    # 传入子物体名字可以获取子物体，为空字符串就获得全部子物体
    def get_child_id_list(self, child_name="", object_id=0, object_id_list=None, element_data=None):
        if object_id_list is not None:
            child_id_list = []
            for object_id in object_id_list:
                child_id_list_temp = self.get_child_id_list(child_name=child_name, object_id=object_id)
                child_id_list += child_id_list_temp
            return child_id_list
        if object_id != 0:
            return rpcMethod.get_child_id_by_id(self, object_id, child_name)
        return rpcMethod.get_child_id(self, element_data, child_name)

    def get_child_id(self, child_name="",object_id=0, element_data=None):
        child_id_list = self.get_child_id_list(child_name,object_id=object_id, element_data=element_data)
        self.is_single_element(child_id_list)
        return child_id_list[0]

    def get_offspring_id_list(self, offspring_path, object_id=0, object_id_list=None, element_data=None):
        if object_id_list is not None:
            offspring_id_list = []
            for object_id in object_id_list:
                offspring_id_list_temp = self.get_offspring_id_list(offspring_path, object_id=object_id)
                offspring_id_list += offspring_id_list_temp
            return offspring_id_list
        if object_id != 0:
            return rpcMethod.get_offspring_id_by_id(self, object_id, offspring_path)
        element_data_new = element_data.copy()
        element_data_new["locator"] = element_data_new["locator"] + ">" + offspring_path
        return rpcMethod.get_object_id(self, element_data_new)

    def get_offspring_id(self, offspring_path, object_id=0, element_data=None):
        offspring_id_list = self.get_offspring_id_list(offspring_path, object_id=object_id, element_data=element_data)
        self.is_single_element(offspring_id_list)
        return offspring_id_list[0]

    def get_parent_id_list(self, object_id_list=None, element_data=None):
        if object_id_list is not None:
            parent_id_list = []
            for object_id in object_id_list:
                parent_id = self.get_parent_id(object_id=object_id)
                parent_id_list.append(parent_id)
            return parent_id_list
        return rpcMethod.get_parent_id(self, element_data)

    # 输入是定位信息时，请保证定位信息是单数的
    def get_parent_id(self, object_id=0, element_data=None):
        if object_id != 0:
            return rpcMethod.get_parent_id_by_id(self, object_id)
        parent_id_list = self.get_parent_id_list(element_data=element_data)
        self.is_single_element(parent_id_list)
        return parent_id_list[0]

    def get_text_list(self, object_id_list: list = None, element_data: dict = None):
        if object_id_list is not None:
            text_list = []
            for object_id in object_id_list:
                text_list.append(self.get_text(object_id=object_id))
            return text_list
        text_list = rpcMethod.get_text(self, element_data)
        return text_list

    def get_text(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            return rpcMethod.get_text_by_id(self, object_id)
        text_list = self.get_text_list(element_data=element_data)
        self.is_single_element(text_list)
        return text_list[0]

    # 可以修改一批文本
    def set_text_list(self, object_id_list: list = None, element_data: dict = None, text=""):
        if object_id_list is not None:
            for object_id in object_id_list:
                self.set_text(object_id=object_id, text=text)
        rpcMethod.set_text(self, element_data, text)

    def set_text(self, object_id: int = 0, element_data: dict = None, text=""):
        if object_id != 0:
            rpcMethod.set_text_by_id(self, object_id, text)
            return
        rpcMethod.set_text(self, element_data, text)

    def get_icon_list(self, object_id_list: list = None, element_data: dict = None):
        if object_id_list is not None:
            icon_list = []
            for object_id in object_id_list:
                icon_list.append(self.get_icon(object_id=object_id))
            return icon_list
        icon_list = rpcMethod.get_img_name(self, element_data)
        return icon_list

    # 获取到的icon是icon的名称，因此是str类型的
    def get_icon(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            return rpcMethod.get_img_name_by_id(self, object_id)
        icon_list = self.get_icon_list(element_data=element_data)
        self.is_single_element(icon_list)
        return icon_list[0]

    def get_slider_value_list(self, object_id_list: list = None, element_data: dict = None):
        if object_id_list is not None:
            slider_value_list = []
            for object_id in object_id_list:
                slider_value_list.append(self.get_slider_value(object_id=object_id))
            return slider_value_list
        return rpcMethod.get_slider_value(self, element_data)

    # 获取到的滑条值是float类型，值在0~1
    def get_slider_value(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            return rpcMethod.get_slider_value_by_id(self, object_id)
        slider_value_list = self.get_slider_value_list(element_data=element_data)
        self.is_single_element(slider_value_list)
        return slider_value_list[0]

    def get_size_list(self, object_id_list: list = None, element_data: dict = None):
        if object_id_list is not None:
            size_list = []
            for object_id in object_id_list:
                size_list.append(self.get_size(object_id=object_id))
            return size_list
        size_list = rpcMethod.get_size(self, element_data)
        return size_list

    def get_size(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            return rpcMethod.get_size_by_id(self, object_id)
        size_list = self.get_size_list(element_data=element_data)
        self.is_single_element(size_list)
        return size_list[0]

    def get_toggle_is_on_list(self, object_id_list: list = None, element_data: dict = None):
        if object_id_list is not None:
            toggle_is_on_list = []
            for object_id in object_id_list:
                toggle_is_on_list.append(self.get_toggle_is_on(object_id=object_id))
            return toggle_is_on_list
        toggle_is_on_list = rpcMethod.get_toggle_is_on(self, element_data)
        return toggle_is_on_list

    def get_toggle_is_on(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            return rpcMethod.get_toggle_is_on_by_id(self, object_id)
        toggle_is_on_list = self.get_toggle_is_on_list(element_data=element_data)
        self.is_single_element(toggle_is_on_list)
        return toggle_is_on_list[0]

    def get_position_list(self, object_id_list: list = None, element_data: dict = None):
        if object_id_list is not None:
            position_list = []
            for object_id in object_id_list:
                position_list.append(self.get_position(object_id=object_id ))
            return position_list
        position_list = rpcMethod.get_position(self, element_data)
        if "focus" in element_data:
            size_list = rpcMethod.get_size(self, element_data)
            bias_x = 0.5 - element_data["focus"][0]
            bias_y = 0.5 - element_data["focus"][1]
            cur = 0
            while cur < len(position_list):
                position_list[cur][0] += size_list[cur][0] * bias_x
                position_list[cur][1] += size_list[cur][1] * bias_y
                cur += 1
        return position_list

    def get_position(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            position = rpcMethod.get_position_by_id(self, object_id)
            return position
        position_list = self.get_position_list(element_data=element_data)
        self.is_single_element(position_list)
        return position_list[0]

    def press(self, object_id: int = 0, element_data: dict = None, duration: float = 2.0):
        position = self.get_position(object_id=object_id, element_data=element_data)
        self.press_position(position, duration)

    def press_position(self, position, duration: float = 2.0):
        self.poco.long_click(position, duration)

    def click_position(self, position):
        self.poco.click(position)

    # 元素点击
    def click_element(self, object_id: int = 0, element_data: dict = None):
        if object_id != 0:
            position = self.get_position(object_id)
            self.click_position(position)
            return position
        position_list = self.get_position_list(element_data=element_data)
        if len(position_list) > 1:
            raise PluralElementError("定位到多个元素")
        elif len(position_list) == 0:
            raise FindNoElementError("没有定位到元素")
        self.click_position(position_list[0])
        return position_list[0]

    # 在b元素出现前一直尝试点击a元素
    def click_a_until_b_appear(self, element_data_a: dict, element_data_b: dict):
        while self.exist(element_data=element_data_b) is False:
            self.click_element_safe(element_data=element_data_a)
            self.sleep(0.5)

    # 第一次列表第1个元素是a 第2个元素是b
    # 第二次列表第2个元素是a 第3个元素是b
    # 以此类推进行click_a_until_b_appear
    def click_a_until_b_appear_list(self, perform_list: list):
        cur = 0
        while cur < len(perform_list) - 1:
            self.click_a_until_b_appear(perform_list[cur], perform_list[cur + 1])
            cur += 1

    # 在b元素消失前一直尝试点击a元素
    def click_a_until_b_disappear(self, element_data_a: dict, element_data_b: dict):
        self.wait_for_appear(element_data_b, is_click=False)
        while self.exist(element_data=element_data_b):
            self.click_element_safe(element_data=element_data_a)
            self.sleep(0.5)

    # 在a元素消失前一直尝试点击a元素
    def click_until_disappear(self, element_data: dict = None):
        self.click_a_until_b_disappear(element_data_a=element_data, element_data_b=element_data)

    # 等待指定元素出现
    def wait_for_appear(self, element_data: dict, is_click: bool = True, interval: float = 0.1):
        while self.exist(element_data=element_data) is False:
            self.sleep(interval)
        if is_click:
            self.click_element(element_data=element_data)

    # 等待指定元素消失
    def wait_for_disappear(self, element_data: dict, interval: float = 0.1):
        while self.exist(element_data=element_data):
            self.sleep(interval)

    # 安全点击
    # 判断元素存在后再点击
    def click_element_safe(self, object_id: int = 0, element_data: dict = None):
        if self.exist(object_id=object_id, element_data=element_data):
            self.click_element(object_id=object_id, element_data=element_data)
            print("点击到了", object_id, element_data, "元素")
            return
        print("元素不存在，没有进行点击")

    # 尝试点击
    # 如果点击失败就看是否有弹窗遮挡
    # 关闭弹窗后会再次点击
    def try_click_element(self, object_id: int = 0, element_data: dict = None):
        try:
            self.click_element(object_id=object_id, element_data=element_data)
        except PluralElementError:
            print("请检查元素的定位信息")
        except FindNoElementError:
            print("正在检查是否有弹窗遮挡")
            for pop_window in self.pop_window_dict:
                if self.exist(element_data=self.pop_window_dict[pop_window]):
                    self.close_pop_window(self.pop_window_dict[pop_window], self.pop_window_close_dict[pop_window])
                    print("关闭弹窗")
                    self.try_click_element(object_id=object_id, element_data=element_data)
                    print("尝试重新点击该元素")
                    return

    # 关闭弹窗
    def close_pop_window(self, element_pop_window, element_pop_window_close):
        while self.exist(element_data=element_pop_window):
            self.click_element_safe(element_data=element_pop_window_close)
            self.sleep(0.1)


    # 元素滑动
    def swipe(self, object_id: int = 0, element_data: dict = None, point_start=None, point_end=None, t: float = 0.05):
        if point_start is not None:
            self.poco.swipe(p1=point_start, p2=point_end, duration=t)  # direction可以填'left','right','up','down'
            return
        if object_id != 0:
            point_start = rpcMethod.get_position_by_id(self, object_id)
            self.poco.swipe(p1=point_start, p2=point_end, duration=t)
            return
        point_start = self.get_position(element_data=element_data)
        self.poco.swipe(p1=point_start, p2=point_end, duration=t)

    # 截取整个屏幕
    def get_screen_shoot(self):
        img_b64encode, fmt = self.poco.snapshot(self.screen_w * 0.5, self.screen_h * 0.5, self.screen_w, self.screen_h)
        img_b64decode = base64.b64decode(img_b64encode)  # base64解码
        # open('screen.{}'.format(fmt), 'wb').write(img_b64decode)
        img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
        img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
        # cv2.rectangle(img, (ui_l, ui_t), (ui_r, ui_b), (255, 0, 0), 3)
        path = "C:/Users/TU/Desktop/screenshot_result"  # 输入文件夹地址
        num_png = len(os.listdir(path))  # 读入文件夹,统计文件夹中的文件个数
        cur = num_png
        cv2.imwrite(path + f'/{cur}.jpg', img)
        # cv2.imshow('img',img)
        # cv2.waitKey(0)

    # 对指定元素进行截取
    def get_element_shoot(self, element_data: dict):
        ui_x, ui_y = self.get_position(element_data=element_data)
        ui_w, ui_h = self.get_size(element_data=element_data)
        print(ui_x, ui_y)
        print(ui_w, ui_h)
        ui_x, ui_y = int(ui_x * self.screen_w), int(ui_y * self.screen_h)
        ui_w, ui_h = int(ui_w * self.screen_w), int(ui_h * self.screen_h)
        print(ui_x, ui_y)
        print(ui_w, ui_h)
        img_b64encode, fmt = self.poco.snapshot(ui_x, ui_y, ui_w, ui_h)
        # ui_l = int((ui_x - ui_w / 2) * self.screen_w)
        # ui_r = int((ui_x + ui_w / 2) * self.screen_w)
        # ui_t = int((ui_y - ui_h / 2) * self.screen_h)
        # ui_b = int((ui_y + ui_h / 2) * self.screen_h)
        img_b64decode = base64.b64decode(img_b64encode)  # base64解码
        # open('screen.{}'.format(fmt), 'wb').write(img_b64decode)
        img_array = np.fromstring(img_b64decode, np.uint8)  # 转换np序列
        img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
        # cv2.rectangle(img, (ui_l, ui_t), (ui_r, ui_b), (255, 0, 0), 3)
        cv2.imshow('img', img)
        cv2.waitKey(0)

    def get_item_count(self, item_name: str = "", item_icon_name: str = "", item_tpid: str = ""):
        book_list = self.excelTools.get_book_list()
        if item_tpid != "":
            return rpcMethod.get_item_count(self, item_tpid)
        for book_dict in book_list:
            worksheet = self.excelTools.get_worksheet(book_dict["book_name"], "模板数据")
            if item_name != "":
                res = self.excelTools.same_row_different_column_convert(worksheet, book_dict["name"], book_dict["id"], item_name)
                if res is not None:
                    item_tpid = res
                    break
            if item_icon_name != "":
                res = self.excelTools.same_row_different_column_convert(worksheet, book_dict["icon"], book_dict["id"], item_icon_name)
                if res is not None:
                    item_tpid = res
                    break
        item_count = rpcMethod.get_item_count(self, item_tpid)
        return item_count

    def set_item_count(self, target_count, item_name: str = "", item_icon_name: str = "", item_tpid: str = ""):
        book_list = self.excelTools.get_book_list()
        if item_tpid != "":
            item_count = self.get_item_count(item_tpid=item_tpid)
            rpcMethod.cmd(self, f"add {item_tpid[0]} {item_tpid} {target_count - item_count}")
            return
        # 参数给的是icon_name或item_name就转换为tpid
        for book_dict in book_list:
            worksheet = self.excelTools.get_worksheet(book_dict["book_name"], "模板数据")
            if item_name != "":
                res = self.excelTools.same_row_different_column_convert(worksheet, book_dict["name"], book_dict["id"],item_name)
                if res is not None:
                    item_tpid = res
                    break
            if item_icon_name != "":
                res = self.excelTools.same_row_different_column_convert(worksheet, book_dict["icon"], book_dict["id"], item_icon_name)
                if res is not None:
                    item_tpid = res
                    break
        item_count = self.get_item_count(item_tpid=item_tpid)
        rpcMethod.cmd(self, f"add {item_tpid[0]} {item_tpid} {target_count - item_count}")

    def is_resource_enough(self, icon_list, value_list):
        cur = 0
        while cur < len(icon_list):
            item_count = self.get_item_count(item_icon_name=icon_list[cur])
            if item_count < value_list[cur]:
                return False
            cur += 1
        return True

    # 根据图标得到物品数量列表
    def get_item_count_list(self, icon_list):
        cur = 0
        item_count_list = []
        while cur < len(icon_list):
            item_count = self.get_item_count(item_icon_name=icon_list[cur])
            item_count_list.append(item_count)
            cur += 1
        return item_count_list

    # 得到消耗后的物品数量列表
    def get_cosumed_item_count_list(self, icon_list, value_list):
        item_count_list = self.get_item_count_list(icon_list)
        cur = 0
        while cur < len(item_count_list):
            item_count_list[cur] -= value_list[cur]
            cur += 1
        return item_count_list


    # 休息t秒
    @staticmethod
    def sleep(t: float):
        time.sleep(t)

    # 键盘输入
    @staticmethod
    def send_key(key: str):
        pyautogui.typewrite(key)
