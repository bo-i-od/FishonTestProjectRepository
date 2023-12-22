from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *


class EntryUpdateLoading(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.EntryUpdateLoading.EntryUpdateLoading):
            return True
        return False

    def wait_for_EntryUpdateLoading(self):
        while not EntryUpdateLoading.is_panel_active(self):
            self.sleep(0.1)

    def click_tap_to_start(self):
        self.click_element_safe(element_data=ElementsData.EntryUpdateLoading.tap_to_start)