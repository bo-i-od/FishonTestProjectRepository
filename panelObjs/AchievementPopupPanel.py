from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *


class AchievementPopupPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AchievementPopupPanel.AchievementPopupPanel)

    def wait_for_panel_disappear(self):
        while AchievementPopupPanel.is_panel_active(self):
            self.sleep(0.1)

    def click_btn_orange(self):
        self.click_element(element_data=ElementsData.AchievementPopupPanel.btn_orange)

    operation_pool = [
        {"element_data": ElementsData.AchievementPanel.btn_close, "func": click_btn_orange, "weight": 4},
        ]

if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    AchievementPopupPanel.click_btn_orange(bp)
    bp.connect_close()
