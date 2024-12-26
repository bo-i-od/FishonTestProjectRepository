from common.basePage import BasePage
from configs.elementsData import ElementsData

class FishCardMultipleLevelUpPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardMultipleLevelUpPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardMultipleLevelUpPanel.FishCardMultipleLevelUpPanel)

    def click_btn_draw(self):
        self.click_element(element_data=ElementsData.FishCardMultipleLevelUpPanel.btn_draw)