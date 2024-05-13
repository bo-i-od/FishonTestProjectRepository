from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *


class CareerPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Career.btn_close)
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Career.CareerPanel)

    def click_btn_enhance(self):
        self.click_element(element_data=ElementsData.Career.btn_enhance)