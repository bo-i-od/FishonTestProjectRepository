from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport

class AquariumPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Aquarium.btn_close)
        if AquariumPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Aquarium.AquariumPanel):
            return True
        return False

    def guide(self):
        perform_list = [ElementsData.NewbieGuide.NBG_aquarium_2_1, ElementsData.NewbieGuide.NBG_aquarium_2_2,
                        ElementsData.NewbieGuide.NBG_aquarium_2_3, ElementsData.NewbieGuide.NBG_aquarium_2_4,
                        ElementsData.NewbieGuide.NBG_aquarium_2_5, ElementsData.NewbieGuide.NBG_aquarium_2_6,
                        ElementsData.NewbieGuide.NBG_aquarium_2_7, ElementsData.NewbieGuide.NBG_aquarium_3_1,
                        ElementsData.NewbieGuide.NBG_aquarium_3_2, ElementsData.NewbieGuide.NBG_aquarium_3_3,
                        ElementsData.NewbieGuide.NBG_aquarium_3_4, ElementsData.NewbieGuide.NBG_aquarium_3_5]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_aquarium_3_5)