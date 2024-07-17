from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearEnhanceSuccesPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearEnhanceSucces.btn_close)
        if GearEnhanceSuccesPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.GearEnhanceSucces.GearEnhanceSuccesPanel)

    def wait_for_panel_appear(self):
        while not GearEnhanceSuccesPanel.is_panel_active(self):
            self.sleep(0.1)