from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class SharePanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.SharePanel.btn_close, ignore_set={"SharePanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.SharePanel.SharePanel)