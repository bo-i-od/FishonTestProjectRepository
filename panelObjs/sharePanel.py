from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class SharePanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.Share.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Share.SharePanel):
            return True
        return False