import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *


class AquariumFishNewPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumFishNewPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumFishNewPanel.AquariumFishNewPanel)

    def get_reddot_position_list(self):
        return self.get_position_list(element_data=ElementsData.AquariumFishNewPanel.btn_sell_reddot_list) + self.get_position_list(element_data=ElementsData.AquariumFishNewPanel.btn_accelerate_reddot_list)

    def switch_tab(self, index=-1):
        position_list = self.get_position_list(element_data=ElementsData.AquariumFishNewPanel.tab_list)
        if index < 0:
            index = random.randint(0, len(position_list) - 1)
        self.click_position(position_list[index])

    def click_btn_change(self):
        self.click_element(element_data=ElementsData.AquariumFishNewPanel.btn_change)

    def click_btn_fast(self):
        self.click_element(element_data=ElementsData.AquariumFishNewPanel.btn_fast)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.AquariumFishNewPanel.btn_i)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.AquariumFishNewPanel.btn_close_tips)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumFishNewPanel.top_res_btns, index=index)

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumFishNewPanel.btns, index=index)

    def click_btn_operate(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumFishNewPanel.btns_operate, index=index)

    def click_aquarium_fish(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumFishNewPanel.aquarium_fish_list, index=index)

    operation_pool = [
        {"element_data": ElementsData.AquariumFishNewPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumFishNewPanel.tab_list, "func": switch_tab, "weight": 2},
        {"element_data": ElementsData.AquariumFishNewPanel.btn_fast, "func": click_btn_fast, "weight": 1},
        {"element_data": ElementsData.AquariumFishNewPanel.btn_change, "func": click_btn_change, "weight": 2},
        {"element_data": ElementsData.AquariumMainPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
        {"element_data": ElementsData.AquariumFishNewPanel.btn_i, "func": click_btn_i, "weight": 2},
        {"element_data": ElementsData.AquariumFishNewPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 2},
        {"element_data": ElementsData.AquariumFishNewPanel.btns, "func": click_btn, "weight": 4},
        {"element_data": ElementsData.AquariumFishNewPanel.btns_operate, "func": click_btn_operate, "weight": 2},
        {"element_data": ElementsData.AquariumFishNewPanel.aquarium_fish_list, "func": click_aquarium_fish, "weight": 4},
        ]

if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    # AquariumFishNewPanel.switch_tab(bp)

    # AquariumFishNewPanel.click_btn_fast(bp)

    # AquariumFishNewPanel.click_btn_change(bp)
    #
    # AquariumFishNewPanel.click_top_res_btn(bp)
    #
    # AquariumFishNewPanel.click_btn(bp)
    #
    # AquariumFishNewPanel.click_btn_operate(bp)
    #
    # AquariumFishNewPanel.click_aquarium_fish(bp)

    AquariumFishNewPanel.click_btn_i(bp)

    AquariumFishNewPanel.click_btn_close_tips(bp)


    bp.connect_close()



