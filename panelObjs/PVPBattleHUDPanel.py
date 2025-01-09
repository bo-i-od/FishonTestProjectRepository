from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPBattleHUDPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPBattleHUDPanel.PVPBattleHUDPanel)

    def click_btn_chat(self):
        self.click_element(element_data=ElementsData.PVPBattleHUDPanel.btn_chat)

    def click_btn_surrender(self):
        self.click_element(element_data=ElementsData.PVPBattleHUDPanel.btn_surrender)

    def click_btn_close_chat_list(self):
        self.click_element(element_data=ElementsData.PVPBattleHUDPanel.btn_close_chat_list)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPBattleHUDPanel.PVPBattleHUDPanel, ignore_set={"PVPBattleHUDPanel"})

    def wait_for_btn_chat_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPBattleHUDPanel.btn_chat, ignore_set={"PVPBattleHUDPanel"})


    def get_emoji_position_list(self):
        return self.get_position_list(element_data=ElementsData.PVPBattleHUDPanel.emoji_list)

    def click_emoji(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPBattleHUDPanel.emoji_list, index=index)

    def click_fish(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPBattleHUDPanel.fish_list, index=index)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.PVPBattleHUDPanel.btn_close_tips)


    operation_pool = [
        {"element_data": ElementsData.PVPBattleHUDPanel.btn_chat, "func": click_btn_chat, "weight": 1},
        {"element_data": ElementsData.PVPBattleHUDPanel.btn_close_chat_list, "func": click_btn_close_chat_list, "weight": 1},
        {"element_data": ElementsData.PVPBattleHUDPanel.btn_surrender, "func": click_btn_surrender, "weight": 1},
        {"element_data": ElementsData.PVPBattleHUDPanel.emoji_list, "func": click_emoji, "weight": 1},
        {"element_data": ElementsData.PVPBattleHUDPanel.fish_list, "func": click_fish, "weight": 1},
        {"element_data": ElementsData.PVPBattleHUDPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # PVPBattleHUDPanel.click_btn_chat(bp)
    # PVPBattleHUDPanel.click_btn_close_chat_list(bp)
    # PVPBattleHUDPanel.click_btn_surrender(bp)
    # PVPBattleHUDPanel.click_emoji(bp)
    # PVPBattleHUDPanel.click_fish(bp, 0)
    PVPBattleHUDPanel.click_btn_close_tips(bp)
    bp.connect_close()