from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVERuleTipsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVERuleTipsPanel.btn_close)