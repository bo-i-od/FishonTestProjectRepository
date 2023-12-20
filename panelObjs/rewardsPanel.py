from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *

class RewardsPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Rewards.RewardsPanel):
            return True
        return False

    def click_tap_to_claim(self):
        self.click_element(element_data=ElementsData.Rewards.tap_to_claim)


    def wait_for_RewardsPanel(self):
        self.wait_for_appear(element_data=ElementsData.Rewards.tap_to_claim, is_click=False)

    def get_reward_dict(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.Rewards.reward_icon_list)
        item_icon_list, gear_icon_list = divide_item_and_gear_icon(reward_icon_list)
        reward_quantity_list = self.get_text_list(element_data=ElementsData.Rewards.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return make_item_dict(item_icon_list, reward_quantity_list)

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.Rewards.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    def get_reward_icon_list(self, is_divide=True):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.Rewards.reward_icon_list)
        # check_icon_list(reward_icon_list)
        if is_divide:
            item_icon_list, gear_icon_list = divide_item_and_gear_icon(reward_icon_list)
            return item_icon_list, gear_icon_list
        return reward_icon_list

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.Rewards.reward_icon_list)
        return reward_position_list



if __name__ == '__main__':
    bp = RewardsPanel()
    print(bp.click_tap_to_claim())
