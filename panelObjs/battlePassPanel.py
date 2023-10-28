from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class BattlePassPanel(BasePage):
    def close_BattlePassPanel(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_close)
        if BattlePassPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePass.BattlePassPanel):
            return True
        return False

    # 点击鱼竿进入预览
    def click_btn_detail(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_detail)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_i)

    def click_btn_task(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_task)

    def click_btn_buy_levels(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_buy)

    def click_btn_get_premium(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_premium)

    def click_btn_unlock_premium(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_unlock)

    def click_btn_collect_all(self):
        self.click_element(element_data=ElementsData.BattlePass.btn_collect)

    


