import random
import re

from common.basePage import BasePage
from common.error import InvalidOperationError
from configs.elementsData import ElementsData
from configs.jumpData import JumpData


class HomePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.HomePanel.HomePanel)

    def get_head_img(self):
        head_img = self.get_icon(element_data=ElementsData.HomePanel.head_img)
        return head_img

    def get_flag(self):
        flag = self.get_icon(element_data=ElementsData.HomePanel.flag)
        return flag

    def get_player_name(self):
        player_name = self.get_text(element_data=ElementsData.HomePanel.player_name)
        return player_name

    def get_rating(self):
        rating = self.get_text(element_data=ElementsData.HomePanel.rating)
        return rating

    def is_btn_questionnaire_exist(self):
        return self.exist(element_data=ElementsData.HomePanel.btn_questionnaire)

    def get_level(self):
        player_lv = self.get_text(element_data=ElementsData.HomePanel.player_lv)
        return player_lv

    def get_player_info(self):
        lv = int(self.get_text(element_data=ElementsData.HomePanel.player_lv))
        rating = int(self.get_text(element_data=ElementsData.HomePanel.rating))
        player_info = {
            "player_name": self.get_text(element_data=ElementsData.HomePanel.player_name),
            "head_img": self.get_icon(element_data=ElementsData.HomePanel.head_img),
            "lv": lv,
            "rating": rating,
            "head_frame": self.get_icon(element_data=ElementsData.HomePanel.head_frame),
        }
        return player_info

    def click_player_info(self):
        self.click_element(element_data=ElementsData.HomePanel.player_info)

    def click_panel_player_info_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.HomePanel.panel_player_info_btns, index=index)

    def click_panel_left_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.HomePanel.panel_left_btns, index=index)

    def click_btn_chat(self):
        self.click_element(element_data=ElementsData.HomePanel.btn_chat)

    def click_panel_giftpack_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.HomePanel.panel_giftpack_btns, index=index)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.HomePanel.top_res_btns, index=index)

    def click_navbar_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.HomePanel.navbar_btns, index=index)






    class Minitask(BasePage):
        def click_btn_recommend(self):
            self.click_element(element_data=ElementsData.HomePanel.Panel_mini_task.btn_recommend)

        def click_btn_go(self):
            self.click_element(element_data=ElementsData.HomePanel.Panel_mini_task.btn_go)

        def get_progress(self):
            progress = self.get_text(element_data=ElementsData.HomePanel.Panel_mini_task.progress)
            res = progress.split("/")
            numerator = int(res[0])
            denominator = int(res[1])
            return numerator, denominator

        def click_btn_claim(self):
            self.click_element(element_data=ElementsData.HomePanel.Panel_mini_task.btn_claim)

        def get_text_task(self):
            return self.get_text(element_data=ElementsData.HomePanel.Panel_mini_task.text_task)

    operation_pool = [
        {"element_data": ElementsData.HomePanel.player_info, "func": click_player_info, "weight": 1},
        {"element_data": ElementsData.HomePanel.panel_player_info_btns, "func": click_panel_player_info_btn, "weight": 1},
        {"element_data": ElementsData.HomePanel.panel_left_btns, "func": click_panel_left_btn, "weight": 1},
        {"element_data": ElementsData.HomePanel.btn_chat, "func": click_btn_chat, "weight": 1},
        {"element_data": ElementsData.HomePanel.panel_giftpack_btns, "func": click_panel_giftpack_btn, "weight": 1},
        {"element_data": ElementsData.HomePanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
        {"element_data": ElementsData.HomePanel.navbar_btns, "func": click_navbar_btn, "weight": 1},
        {"element_data": ElementsData.HomePanel.Panel_mini_task.btn_recommend, "func": Minitask.click_btn_recommend, "weight": 1},
        {"element_data": ElementsData.HomePanel.Panel_mini_task.btn_go, "func": Minitask.click_btn_go, "weight": 1},
        {"element_data": ElementsData.HomePanel.Panel_mini_task.btn_claim, "func": Minitask.click_btn_claim, "weight": 1},
        ]





if __name__ == '__main__':
    bp = BasePage()
    name_list = bp.get_name_list(element_data_list=JumpData.panel_list)
    print(name_list)
    operation_pool = HomePanel.operation_pool
    element_data_list = []
    for operation in operation_pool:
        element_data_list.append(operation["element_data"])
    object_id_list = bp.get_object_id_list(element_data_list=element_data_list)
    weight_list = []
    weight_total = 0

    cur = 0
    while cur < len(object_id_list):
        if not object_id_list[cur]:
            weight_list.append(0)
            cur += 1
            continue
        weight = operation_pool[cur]["weight"]
        weight_list.append(weight)
        weight_total += weight
        cur += 1
    print(object_id_list)
    print(weight_list)
    operation_random = random.choices(operation_pool, weights=weight_list, k=1)[0]
    try:
        operation_random['func'](bp)
    except InvalidOperationError:
        pass


    # print(object_id_list)
    # print(weight_list)
    # print(weight_total)
    # print(operation_random)

    # HomePanel.click_panel_player_info_btn(bp, index=-1)

    # HomePanel.click_panel_left_btn(bp, index=-1)

    # HomePanel.click_btn_chat(bp)

    # HomePanel.click_panel_giftpack_btn(bp)

    # HomePanel.click_panel_entrance_btn(bp)

    # HomePanel.click_top_res_btn(bp)

    # HomePanel.click_navbar_btn(bp)

    # HomePanel.click_btn_avatar(bp)

    # HomePanel.click_btn_chest(bp)

    bp.connect_close()



