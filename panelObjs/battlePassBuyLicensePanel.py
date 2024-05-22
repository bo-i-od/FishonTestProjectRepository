from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class BattlePassBuyLicensePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePassBuyLicense.BattlePassBuyLicensePanel):
            return True
        return False

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLicense.btn_close)

    def click_btn_buy_pro(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLicense.btn_buy_pro)

    def click_btn_buy_standard(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLicense.btn_buy_standard)

    def wait_for_pay_result(self):
        while True:
            if self.exist(element_data=ElementsData.FlashTips.FlashTipsPanel):
                return False
            if not BattlePassBuyLicensePanel.is_panel_active(self):
                return True
            self.sleep(0.1)