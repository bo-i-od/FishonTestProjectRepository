from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class Recharge1And1Panel(BasePage):
    def close_Recharge1And1Panel(self):
        self.click_element(element_data=ElementsData.Recharge1And1.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Recharge1And1.Recharge1And1Panel)

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.Recharge1And1.btn_buy)
    def is_btn_buy_clickable(self):
        if self.get_offspring_id_list("btn_disabled", element_data=ElementsData.Recharge1And1.btn_buy):
            return False
        return True

    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.Recharge1And1.icon_list)
        # check_icon_list(icon_list)
        return icon_list

    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.Recharge1And1.icon_list)
        return position_list

if __name__ == '__main__':
    bp = Recharge1And1Panel()
    a = bp.is_btn_buy_clickable()

    print(a)