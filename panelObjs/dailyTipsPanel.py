from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *

class DailyTipsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DailyTips.btn_close)
        if DailyTipsPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DailyTips.DailyTipsPanel):
            return True
        return False

    def get_do_not_show_today(self):
        return self.get_toggle_is_on(element_data=ElementsData.DailyTips.toggle)

    def click_do_not_show_today(self):
        self.click_element(element_data=ElementsData.DailyTips.toggle)