from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class AchievementPopupPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AchievementPopup.AchievementPopupPanel)

    def wait_for_panel_disappear(self):
        while AchievementPopupPanel.is_panel_active(self):
            self.sleep(0.1)