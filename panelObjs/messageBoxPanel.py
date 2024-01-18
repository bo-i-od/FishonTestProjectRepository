from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class MessageBoxPanel(BasePage):
    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.MessageBox.btn_cancel, ignore_set={"MessageBoxPanel"})

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.MessageBox.btn_confirm, ignore_set={"MessageBoxPanel"})

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.MessageBox.MessageBoxPanel):
            return True
        return False