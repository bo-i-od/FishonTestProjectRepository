from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class PVPBattleHUDPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PVPBattleHUD.PVPBattleHUDPanel):
            return True
        return False
    def click_btn_chat(self):
        self.click_element(element_data=ElementsData.PVPBattleHUD.btn_chat)

    def click_btn_surrender(self):
        self.click_element(element_data=ElementsData.PVPBattleHUD.btn_surrender)

    def wait_for_panel_appear(self):
        while not PVPBattleHUDPanel.is_panel_active(self):
            self.sleep(0.1)