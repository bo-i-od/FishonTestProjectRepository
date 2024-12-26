from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport

class AquariumPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumPanel.AquariumPanel)

    def click_btn_add_100100(self):
        self.click_element(element_data=ElementsData.AquariumPanel.btn_add_100100)

    def click_rewards(self):
        self.click_element(element_data=ElementsData.AquariumPanel.Rewards)

    def click_btn_build(self):
        self.click_element(element_data=ElementsData.AquariumPanel.btn_build)

    def click_btn_fish(self):
        self.click_element(element_data=ElementsData.AquariumPanel.btn_fish)

