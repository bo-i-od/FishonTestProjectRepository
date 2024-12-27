from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *


class AquariumFishNewPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumFishNewPanel.AquariumFishNewPanel)

    def get_reddot_position_list(self):
        return self.get_position_list(element_data=ElementsData.AquariumFishNewPanel.btn_sell_reddot_list) + self.get_position_list(element_data=ElementsData.AquariumFishNewPanel.btn_accelerate_reddot_list)

    def switch_tab(self, index):
        position_list = self.get_position_list(element_data=ElementsData.AquariumFishNewPanel.tab_list)
        self.click_position(position_list[index])

    def click_btn_change(self):
        self.click_element(element_data=ElementsData.AquariumFishNewPanel.btn_change)

if __name__ == '__main__':
    serial_number = "127.0.0.1:21503"
    bp = BasePage(serial_number=serial_number, is_mobile_device=False, is_monitor=True)

