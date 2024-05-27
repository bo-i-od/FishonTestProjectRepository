from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class FisheryGiftPackPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FisheryGiftPack.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FisheryGiftPack.FisheryGiftPackPanel):
            return True
        return False

    def get_item_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.FisheryGiftPack.quantity_list)
        return quantity_list

    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.FisheryGiftPack.icon_list)
        return icon_list

    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.FisheryGiftPack.icon_list)
        return position_list

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.FisheryGiftPack.btn_buy)