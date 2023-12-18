from common.basePage import BasePage
from configs.elementsData import ElementsData


class RewardsPreviewPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.RewardsPreview.RewardsPreviewPanel):
            return True
        return False

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.RewardsPreview.reward_icon_list)
        return reward_icon_list

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.RewardsPreview.reward_icon_list)
        return reward_position_list