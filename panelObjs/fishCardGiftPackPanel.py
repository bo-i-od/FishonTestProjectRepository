from common.basePage import BasePage
from configs.elementsData import ElementsData

from tools.commonTools import *
from items import resource

class FishCardGiftPackPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardGiftPack.btn_close)
        if FishCardGiftPackPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FishCardGiftPack.FishCardGiftPackPanel):
            return True
        return False

    def get_item_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.FishCardGiftPack.quantity_list)
        return quantity_list

    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.FishCardGiftPack.icon_list)
        return icon_list

    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.FishCardGiftPack.icon_list)
        return position_list

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.FishCardGiftPack.btn_buy)

if __name__ == "__main__":
    bp = BasePage()

    print(a)
