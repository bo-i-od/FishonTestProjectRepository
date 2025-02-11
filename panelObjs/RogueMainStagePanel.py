from common.basePage import BasePage
from configs.elementsData import ElementsData


class RogueMainStagePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RogueMainStagePanel.RogueMainStagePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RogueMainStagePanel.btn_close)

    def click_btn_challenge(self):
        self.click_element(element_data=ElementsData.RogueMainStagePanel.btn_challenge)

    class panel_tips_up(BasePage):
        def click_btn_close(self):
            self.click_element(element_data=ElementsData.RogueMainStagePanel.panel_tips_up.btn_close)

