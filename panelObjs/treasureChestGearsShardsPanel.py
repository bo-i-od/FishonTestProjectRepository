import random

from common.basePage import BasePage
from configs.elementsData import ElementsData

class TreasureChestGearsShardsPanel(BasePage):
    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.TreasureChestGearsShards.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.TreasureChestGearsShards.TreasureChestGearsShardsPanel):
            return True
        return False