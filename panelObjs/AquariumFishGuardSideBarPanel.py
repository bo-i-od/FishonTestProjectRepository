from common.basePage import BasePage
from configs.elementsData import ElementsData

class AquariumFishGuardSideBarPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_close)

    def click_tab_1(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.tab_1)

    def click_tab_2(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.tab_2)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumFishGuardSideBarPanel.tab_list, index=index)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_i)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_close_tips)

    def click_btn_aquarium(self):
        self.click_element(element_data=ElementsData.AquariumFishGuardSideBarPanel.btn_aquarium)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumFishGuardSideBarPanel.AquariumFishGuardSideBarPanel)


    operation_pool = [
        {"element_data": ElementsData.AquariumFishGuardSideBarPanel.btn_aquarium, "func": click_btn_aquarium, "weight": 1},
        {"element_data": ElementsData.AquariumFishGuardSideBarPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumFishGuardSideBarPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
        {"element_data": ElementsData.AquariumFishGuardSideBarPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.AquariumFishGuardSideBarPanel.tab_list, "func": switch_tab, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # AquariumFishGuardSideBarPanel.click_btn_aquarium(bp)
    # AquariumFishGuardSideBarPanel.click_btn_close(bp)
    # AquariumFishGuardSideBarPanel.click_btn_close_tips(bp)
    # AquariumFishGuardSideBarPanel.click_btn_i(bp)
    AquariumFishGuardSideBarPanel.switch_tab(bp)
    bp.connect_close()