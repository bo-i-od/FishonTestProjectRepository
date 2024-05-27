from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class AquariumBuildPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumBuild.btn_close)

    def switch_tab(self, index):
        tab_position_list = self.get_position_list(element_data=ElementsData.AquariumBuild.tab_list)
        self.click_position(tab_position_list[index])

    def click_btn_add_100100(self):
        self.click_element(element_data=ElementsData.AquariumBuild.btn_add_100100)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.AquariumBuild.AquariumBuildPanel):
            return True
        return False