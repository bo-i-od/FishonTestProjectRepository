from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource

class LeaderBoardPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.LeaderBoard.LeaderBoardPanel):
            return True
        return False
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.LeaderBoard.btn_close)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.LeaderBoard.btn_i)

    def click_tap_to_close(self):
        self.click_element(element_data=ElementsData.LeaderBoard.tap_to_close)

    def get_coin(self):
        coin = resource.str_to_int(self.get_text(element_data=ElementsData.LeaderBoard.coin))
        return coin

    def get_top_100_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.LeaderBoard.top_100_rewards_icon_list)
        return icon_list

    def get_top_100_rewards_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.LeaderBoard.top_100_rewards_icon_list)
        return position_list

    def get_top_100_rewards_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.LeaderBoard.top_100_rewards_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    def get_ranking(self):
        return int(self.get_text(element_data=ElementsData.LeaderBoard.ranking))

    def get_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.LeaderBoard.rewards_icon_list)
        return icon_list

    def get_rewards_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.LeaderBoard.rewards_icon_list)
        return position_list

    def get_rewards_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.LeaderBoard.rewards_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list