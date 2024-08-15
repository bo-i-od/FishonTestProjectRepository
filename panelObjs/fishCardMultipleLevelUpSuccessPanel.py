from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishCardMultipleLevelUpSuccessPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardMultipleLevelUpSuccess.FishCardMultipleLevelUpSuccessPanel)

    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.FishCardMultipleLevelUpSuccess.btn_close)