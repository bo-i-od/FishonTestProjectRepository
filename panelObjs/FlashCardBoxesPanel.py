from common.basePage import BasePage
from configs.elementsData import ElementsData


class FlashCardBoxesPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FlashCardBoxesPanel.FlashCardBoxesPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FlashCardBoxesPanel.FlashCardBoxes_btn_close)

