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
        self.wait_for_appear(element_data=ElementsData.PVPBattleHUD.PVPBattleHUDPanel)

    def wait_for_btn_chat_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPBattleHUD.btn_chat)


    def get_emoji_position_list(self):
        return self.get_position_list(element_data=ElementsData.PVPBattleHUD.emoji_list)