from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class LeaderBoardPopResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LeaderBoardPopResultPanel.LeaderBoardPopResultPanel)

    def wait_for_LeaderBoardPopResultPanel(self):
        while not LeaderBoardPopResultPanel.is_panel_active(self):
            self.clear_popup(ignore_set={"LeaderBoardPopResultPanel"})
            self.sleep(0.1)

    def click_btn_claim(self):
        self.click_element(element_data=ElementsData.LeaderBoardPopResultPanel.btn_claim)

    def get_reward_position_list(self):
        reward_position_list = self.get_position_list(element_data=ElementsData.LeaderBoardPopResultPanel.reward_icon_list)
        return reward_position_list

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.LeaderBoardPopResultPanel.reward_icon_list)
        return reward_icon_list

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.LeaderBoardPopResultPanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list