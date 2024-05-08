from common.basePage import BasePage
from configs.elementsData import ElementsData


class PlayerLevelupPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PlayerLevelup.PlayerLevelupPanel):
            return True
        return False

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.PlayerLevelup.PlayerLevelupPanel, is_click=False)

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.PlayerLevelup.tap_to_continue)

if __name__ == '__main__':
    bp = BasePage()
    PlayerLevelupPanel.wait_for_panel_appear(bp)