from common.basePage import BasePage
from configs.elementsData import ElementsData


class MainlineFlashCardReceivePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MainlineFlashCardReceivePanel.MainlineFlashCardReceivePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.MainlineFlashCardReceivePanel.btn_close, ignore_set={"MainlineFlashCardReceivePanel"})
