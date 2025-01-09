from common.basePage import BasePage
from configs.elementsData import ElementsData


class AquariumNewActivityPopupPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumNewActivityPopupPanel.btn_close, ignore_set={"AquariumNewActivityPopupPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumNewActivityPopupPanel.AquariumNewActivityPopupPanel)

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumNewActivityPopupPanel.item_list, index=index, ignore_set={"AquariumNewActivityPopupPanel"})

    def click_btn_enter(self):
        self.click_element(element_data=ElementsData.AquariumNewActivityPopupPanel.btn_enter, ignore_set={"AquariumNewActivityPopupPanel"})

    operation_pool = [
        {"element_data": ElementsData.AquariumNewActivityPopupPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumNewActivityPopupPanel.btn_enter, "func": click_btn_enter, "weight": 1},
        {"element_data": ElementsData.AquariumNewActivityPopupPanel.item_list, "func": click_item, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    # AquariumNewActivityPopupPanel.click_btn_close(bp)
    AquariumNewActivityPopupPanel.click_btn_enter(bp)
    # AquariumNewActivityPopupPanel.click_item(bp)
    # AquariumNewActivityPopupPanel.is_panel_active(bp)
    bp.connect_close()