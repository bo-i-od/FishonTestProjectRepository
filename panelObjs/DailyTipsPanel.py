from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *

class DailyTipsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DailyTipsPanel.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DailyTipsPanel.DailyTipsPanel):
            return True
        return False

    def get_do_not_show_today(self):
        return self.get_toggle_is_on(element_data=ElementsData.DailyTipsPanel.toggle)

    def click_do_not_show_today(self):
        self.click_element(element_data=ElementsData.DailyTipsPanel.toggle)