from common.basePage import BasePage
from configs.elementsData import ElementsData


class PlayerLevelupPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerLevelupPanel.PlayerLevelupPanel)

    def wait_for_panel_appear(self):
        cur = 0
        while not self.exist(element_data=ElementsData.PlayerLevelupPanel.PlayerLevelupPanel):
            self.clear_popup_once(ignore_set={"PlayerLevelupPanel"})
            self.sleep(1)
            cur += 1
            if cur > 10:
                break

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.PlayerLevelupPanel.tap_to_continue, ignore_set={"PlayerLevelupPanel"})

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerLevelupPanel.item_list, index=index, ignore_set={"PlayerLevelupPanel"})


    operation_pool = [
        {"element_data": ElementsData.PlayerLevelupPanel.tap_to_continue, "func": click_tap_to_continue, "weight": 1},
        {"element_data": ElementsData.PlayerLevelupPanel.item_list, "func":  click_item, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # PlayerLevelupPanel.click_tap_to_continue(bp)
    PlayerLevelupPanel.click_item(bp)

    bp.connect_close()