from common.basePage import BasePage
from configs.elementsData import ElementsData


class FlashCardReceivePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FlashCardReceive.FlashCardReceivePanel)