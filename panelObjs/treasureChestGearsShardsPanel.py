import random

from common.basePage import BasePage
from configs.elementsData import ElementsData

class TreasureChestGearsShardsPanel(BasePage):
    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.TreasureChestGearsShardsPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.TreasureChestGearsShardsPanel.TreasureChestGearsShardsPanel)

    def get_btn_enhance_position_list(self):
        btn_enhance_position_list = self.get_position_list(element_data=ElementsData.TreasureChestGearsShardsPanel.btn_enhance_list)
        return btn_enhance_position_list