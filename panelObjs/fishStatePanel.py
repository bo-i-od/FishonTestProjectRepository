from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishStatePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishState.FishStatePanel)

    def click_btn_icon(self):
        self.click_element(element_data=ElementsData.FishState.btn_icon)