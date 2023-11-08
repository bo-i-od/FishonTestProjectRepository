from common.basePage import BasePage
from configs.elementsData import ElementsData
from items.resource import *

class RodMoreToOnePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.RodMoreToOne.RodMoreToOnePanel):
            return True
        return False

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RodMoreToOne.btn_close)

    def click_confirm(self):
        self.click_element(element_data=ElementsData.RodMoreToOne.btn_confirm)

    def get_rod_icon_and_position_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.RodMoreToOne.icon_list)
        position_list = self.get_position_list(element_data=ElementsData.RodMoreToOne.icon_list)
        return icon_list, position_list

    def get_btn_preview_position_list(self):
        btn_preview_position_list = self.get_position_list(element_data=ElementsData.RodMoreToOne.tipsBtn_list)
        return btn_preview_position_list
