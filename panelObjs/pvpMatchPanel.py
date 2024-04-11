from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport

class PVPMatchPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PVPMatch.PVPMatchPanel):
            return True
        return False

    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.PVPMatch.btn_cancel)