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

    operation_pool = [
        {"element_data": ElementsData.DailyTipsPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.DailyTipsPanel.toggle, "func": click_do_not_show_today, "weight": 1},
        ]

if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)

    bp.connect_close()