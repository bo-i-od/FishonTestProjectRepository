from common.basePage import BasePage
from configs.elementsData import ElementsData


class PlayerLevelupPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerLevelup.PlayerLevelupPanel)

    def wait_for_panel_appear(self):
        while not self.exist(element_data=ElementsData.PlayerLevelup.PlayerLevelupPanel):
            self.clear_popup_once(ignore_set={"PlayerLevelupPanel"})
            self.sleep(0.5)

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.PlayerLevelup.tap_to_continue)


if __name__ == '__main__':
    bp = BasePage()
    PlayerLevelupPanel.wait_for_panel_appear(bp)