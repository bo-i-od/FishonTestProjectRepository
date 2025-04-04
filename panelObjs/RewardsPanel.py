from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *

class RewardsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RewardsPanel.RewardsPanel)

    def click_tap_to_claim(self, ignore_set=None):
        if ignore_set is None:
            ignore_set = {"RewardsPanel"}
        self.click_element(element_data=ElementsData.RewardsPanel.tap_to_claim, ignore_set=ignore_set)


    def wait_for_panel_appear(self, ignore_set=None):
        if ignore_set is None:
            ignore_set = {"RewardsPanel"}
        self.wait_for_appear(element_data=ElementsData.RewardsPanel.tap_to_claim, is_click=False, ignore_set=ignore_set)

    def get_reward_dict(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.RewardsPanel.reward_icon_list)
        item_icon_list, gear_icon_list = divide_item_and_gear_icon(reward_icon_list)
        reward_quantity_list = self.get_text_list(element_data=ElementsData.RewardsPanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return make_item_dict(item_icon_list, reward_quantity_list)

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.RewardsPanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    def get_reward_icon_list(self, is_divide=True):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.RewardsPanel.reward_icon_list)
        # check_icon_list(reward_icon_list)
        if is_divide:
            item_icon_list, gear_icon_list = divide_item_and_gear_icon(reward_icon_list)
            return item_icon_list, gear_icon_list
        return reward_icon_list

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.RewardsPanel.reward_icon_list)
        return reward_position_list

    def click_item(self, index=-1, ignore_set=None):
        if ignore_set is None:
            ignore_set = {"RewardsPanel"}
        self.click_object_of_plural_objects(element_data=ElementsData.RewardsPanel.item_list,element_viewport=ElementsData.RewardsPanel.viewport, viewport_direction="row", index=index, ignore_set=ignore_set)



if __name__ == '__main__':
    bp = RewardsPanel()
    RewardsPanel.click_item(bp, 0)
    bp.connect_close()
