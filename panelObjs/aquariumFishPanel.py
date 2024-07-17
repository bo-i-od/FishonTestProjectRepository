from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class AquariumFishPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumFish.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumFish.AquariumFishPanel)

    def click_btn_add_100100(self):
        self.click_element(element_data=ElementsData.AquariumFish.btn_add_100100)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.AquariumFish.btn_i)

    def switch_tab(self, index):
        tab_position_list = self.get_position_list(element_data=ElementsData.AquariumFish.tab_list)
        self.click_position(tab_position_list[index])