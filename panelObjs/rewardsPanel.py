from common.basePage import BasePage
from configs.elementsData import ElementsData
from items.resource import *

class RewardsPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Rewards.RewardsPanel):
            return True
        return False

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.Rewards.tap_to_continue)

    def wait_for_RewardsPanel(self):
        self.wait_for_appear(element_data=ElementsData.Rewards.tap_to_continue, is_click=False)

    def get_reward_dict(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.Rewards.reward_icon_list)
        reward_quantity_list = self.get_text_list(element_data=ElementsData.Rewards.reward_quantity_list)
        return self.make_item_dict(reward_icon_list, reward_quantity_list)

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.Rewards.reward_icon_list)
        check_icon_list(reward_icon_list)
        return reward_icon_list

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.Rewards.reward_icon_list)
        return reward_position_list

if __name__ == '__main__':
    bp = RewardsPanel()
    print(bp.get_reward_icon_list())
