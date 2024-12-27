from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *

class GearNewPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePreparePanel.gears)

    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.BattlePreparePanel.btn_cancel)

    def click_btn_go(self):
        self.click_element(element_data=ElementsData.BattlePreparePanel.btn_go)



