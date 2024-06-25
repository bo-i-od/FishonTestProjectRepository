from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class FishCardMultipleLevelUpPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardMultipleLevelUp.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FishCardMultipleLevelUp.FishCardMultipleLevelUpPanel):
            return True
        return False