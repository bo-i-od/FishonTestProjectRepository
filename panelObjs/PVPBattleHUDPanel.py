from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPBattleHUDPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPBattleHUDPanel.PVPBattleHUDPanel)

    def click_btn_chat(self):
        self.click_element(element_data=ElementsData.PVPBattleHUDPanel.btn_chat)

    def click_btn_surrender(self):
        self.click_element(element_data=ElementsData.PVPBattleHUDPanel.btn_surrender)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPBattleHUDPanel.PVPBattleHUDPanel, ignore_set={"PVPBattleHUDPanel"})

    def wait_for_btn_chat_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPBattleHUDPanel.btn_chat, ignore_set={"PVPBattleHUDPanel"})


    def get_emoji_position_list(self):
        return self.get_position_list(element_data=ElementsData.PVPBattleHUDPanel.emoji_list)