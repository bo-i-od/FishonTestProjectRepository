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


    def get_progress_label_update(self):
        progress_label_update = self.get_text_list(element_data=ElementsData.EntryUpdateLoading.progress_label_update)
        if not progress_label_update:
            return
        return progress_label_update[0]

    def click_tap_to_start(self):
        self.click_until_disappear(element_data=ElementsData.EntryUpdateLoading.tap_to_start)