from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class RechargeStorePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Store.btn_close)
        if RechargeStorePanel.is_panel_active(self):
            raise FindElementError
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Store.StorePanel):
            return True
        return False