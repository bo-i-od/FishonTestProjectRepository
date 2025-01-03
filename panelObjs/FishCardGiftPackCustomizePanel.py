from common.basePage import BasePage
from configs.elementsData import ElementsData

from tools.commonTools import *


class FishCardGiftPackCustomizePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.EventsGiftCenterPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardGiftPackCustomizePanel.FishCardGiftPackCustomizePanel)

    def get_item_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.FishCardGiftPackCustomizePanel.quantity_list)
        return quantity_list

    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.FishCardGiftPackCustomizePanel.icon_list)
        return icon_list

    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.FishCardGiftPackCustomizePanel.icon_list)
        return position_list

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.FishCardGiftPackCustomizePanel.btn_buy)

if __name__ == "__main__":
    bp = BasePage()
    FishCardGiftPackCustomizePanel.click_btn_close(bp)

