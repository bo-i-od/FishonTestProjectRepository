from common.basePage import BasePage
from configs.elementsData import ElementsData


class QuestionnairePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Questionnaire.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Questionnaire.QuestionnairePanel):
            return True
        return False