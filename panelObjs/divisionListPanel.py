from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *

class DivisionListPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DivisionList.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DivisionList.DivisionListPanel):
            return True
        return False
