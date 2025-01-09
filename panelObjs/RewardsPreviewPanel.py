from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class RewardsPreviewPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RewardsPreviewPanel.RewardsPreviewPanel)

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.RewardsPreviewPanel.reward_icon_list)
        return reward_icon_list

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.RewardsPreviewPanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.RewardsPreviewPanel.reward_icon_list)
        return reward_position_list

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RewardsPreviewPanel.btn_close)

    operation_pool = [
        {"element_data": ElementsData.RewardsPreviewPanel.btn_close, "func": click_btn_close, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    RewardsPreviewPanel.click_btn_close(bp)
    # RewardsPreviewPanel.get_reward_icon_list(bp)
    # RewardsPreviewPanel.get_reward_position_list(bp)
    # RewardsPreviewPanel.get_reward_quantity_list(bp)
    # RewardsPreviewPanel.is_panel_active(bp)
    bp.connect_close()