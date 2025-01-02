from common.basePage import BasePage
from configs.elementsData import ElementsData

class AquariumFishGuardSideBarPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_close)

    def click_tab_1(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.tab_1)

    def click_tab_2(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.tab_2)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_i)

    def click_btn_aquarium(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_aquarium)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumFishGuardSideBarPanel.AquariumFishGuardSideBarPanel)