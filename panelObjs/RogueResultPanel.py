from common.basePage import BasePage
from configs.elementsData import ElementsData


class RogueResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RogueResultPanel.RogueResultPanel)

    def click_btn_orange(self):
        self.click_element(element_data=ElementsData.RogueResultPanel.btn_orange)