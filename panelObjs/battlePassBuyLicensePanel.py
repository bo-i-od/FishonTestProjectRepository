from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class BattlePassBuyLicensePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassBuyLicense.BattlePassBuyLicensePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLicense.btn_close)

    def get_btn_buy_list(self):
        return self.get_position_list(element_data=ElementsData.BattlePassBuyLicense.btn_buy_list)

    def get_cost_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.BattlePassBuyLicense.cost_icon_list)

    def get_cost_quantity_list(self):
        cost_quantity_list = self.get_text_list(element_data=ElementsData.BattlePassBuyLicense.cost_quantity_list)
        str_to_int_list(cost_quantity_list)
        str_to_int_list_oversea(cost_quantity_list)
        return cost_quantity_list

    def wait_for_pay_result(self):
        while True:
            self.clear_popup()
            if self.exist(element_data=ElementsData.FlashTips.FlashTipsPanel):
                return False
            if not BattlePassBuyLicensePanel.is_panel_active(self):
                return True
            self.sleep(1)

if __name__ == '__main__':
    bp = BasePage()
    position_list = BattlePassBuyLicensePanel.get_btn_buy_list(bp)
    bp.click_position(position_list[0])