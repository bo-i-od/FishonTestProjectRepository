from common.basePage import BasePage
from configs.elementsData import ElementsData

class TreasureChestGearsShardsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.TreasureChestGearsShardsPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.TreasureChestGearsShardsPanel.TreasureChestGearsShardsPanel)

    def get_btn_enhance_position_list(self):
        btn_enhance_position_list = self.get_position_list(element_data=ElementsData.TreasureChestGearsShardsPanel.btn_enhance_list)
        return btn_enhance_position_list

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.TreasureChestGearsShardsPanel.item_list, element_viewport=ElementsData.TreasureChestGearsShardsPanel.viewport, viewport_edge=[0, -0.2],viewport_direction="row", index=index)

    def click_btn_enhance(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.TreasureChestGearsShardsPanel.btn_enhance_list, element_viewport=ElementsData.TreasureChestGearsShardsPanel.viewport, viewport_edge=[0, -0.2],viewport_direction="row", index=index)


    operation_pool = [
        {"element_data": ElementsData.TreasureChestGearsShardsPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.TreasureChestGearsShardsPanel.btn_enhance_list, "func": click_btn_enhance, "weight": 1},
        {"element_data": ElementsData.TreasureChestGearsShardsPanel.item_list, "func": click_item, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    # TreasureChestGearsShardsPanel.click_btn_close(bp)
    # TreasureChestGearsShardsPanel.click_btn_enhance(bp, 0)
    TreasureChestGearsShardsPanel.click_item(bp, 0)
    bp.connect_close()