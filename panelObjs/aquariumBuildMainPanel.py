from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class AquariumBuildMainPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumBuildMain.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumBuildMain.AquariumBuildMainPanel)

    def get_tip_levelup_bubble_position_list(self):
        return self.get_position_list(element_data=ElementsData.AquariumBuildMain.tip_levelup_bubble_list)

    def get_build_lv_position_list(self):
        return self.get_position_list(element_data=ElementsData.AquariumBuildMain.build_lv_list)