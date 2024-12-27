from common.basePage import BasePage
from configs.elementsData import ElementsData
class PlayerInteractPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerInteractPanel.PlayerInteractPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_close)

    def click_btn_aquarium(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_aquarium)

    def click_btn_changecamera(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_changecamera)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.player_rod_btn_i)

    def click_tab1(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.panel_tab1)

    def click_tab2(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.panel_tab2)

    def click_tab3(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.panel_tab3)

