from common.basePage import BasePage
from configs.elementsData import ElementsData


class LocationPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LocationPanel.LocationPanel)

    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.LocationPanel.btn_cancel, ignore_set={"LocationPanel"})

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.LocationPanel.btn_confirm, ignore_set={"LocationPanel"})

    def click_item(self, index=-1):
        size = self.get_size_list(element_data=ElementsData.LocationPanel.item_list)[0]
        viewport_range = [0.5 - 1.5 * size[1], 0.5 - 0.5 * size[1]]
        self.click_object_of_plural_objects(element_data=ElementsData.LocationPanel.item_list, element_viewport=ElementsData.LocationPanel.viewport, viewport_direction="column", viewport_range=viewport_range, delta_len=2 * size[1],index=index,ignore_set={"LocationPanel"})

    operation_pool = [
        {"element_data": ElementsData.LocationPanel.btn_cancel, "func": click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.LocationPanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.LocationPanel.item_list, "func": click_item, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # LocationPanel.click_btn_cancel(bp)
    # LocationPanel.click_btn_confirm(bp)
    LocationPanel.click_item(bp, 1)
    # bp.get_object_id_list(element_data=ElementsData.LocationPanel.item_list)
    # LocationPanel.is_panel_active(bp)
    bp.connect_close()