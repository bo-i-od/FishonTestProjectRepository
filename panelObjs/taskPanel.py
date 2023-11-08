from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
class TaskPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Task.btn_close)
        if TaskPanel.is_panel_active(self):
            raise FindElementError
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Task.TaskPanel):
            return True
        return False

    def get_button_position(self):
        btn_completed_list = self.get_position_list(element_data=ElementsData.Task.btn_completed_list)


