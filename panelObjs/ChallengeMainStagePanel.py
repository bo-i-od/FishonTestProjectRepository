from common.basePage import BasePage
from configs.elementsData import ElementsData


class ChallengeMainStagePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ChallengeMainStagePanel.ChallengeMainStagePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ChallengeMainStagePanel.btn_close)

    def click_btn_orange(self):
        self.click_element(element_data=ElementsData.ChallengeMainStagePanel.btn_orange)
