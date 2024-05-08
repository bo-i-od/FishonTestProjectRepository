from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPRuleTipsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVPRuleTips.btn_close)