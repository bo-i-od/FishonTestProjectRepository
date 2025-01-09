from common.basePage import BasePage
from configs.elementsData import ElementsData


class QuestionnairePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.QuestionnairePanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.QuestionnairePanel.QuestionnairePanel)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.QuestionnairePanel.btn_confirm)

    operation_pool = [
        {"element_data": ElementsData.QuestionnairePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.QuestionnairePanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # QuestionnairePanel.click_btn_close(bp)
    QuestionnairePanel.click_btn_confirm(bp)
    # QuestionnairePanel.is_panel_active(bp)
    bp.connect_close()

