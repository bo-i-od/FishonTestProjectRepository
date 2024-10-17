from common.basePage import BasePage
from configs.elementsData import ElementsData


class PlayerLevelupPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerLevelup.PlayerLevelupPanel)

    def wait_for_panel_appear(self):
        cur = 0
        while not self.exist(element_data=ElementsData.PlayerLevelup.PlayerLevelupPanel):
            self.clear_popup_once(ignore_set={"PlayerLevelupPanel"})
            self.sleep(1)
            cur += 1
            if cur > 10:
                break

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.PlayerLevelup.tap_to_continue)


if __name__ == '__main__':
    bp = BasePage()
    PlayerLevelupPanel.wait_for_panel_appear(bp)