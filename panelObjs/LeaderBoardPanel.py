from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource

class LeaderBoardPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LeaderBoardPanel.LeaderBoardPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.LeaderBoardPanel.btn_close)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.LeaderBoardPanel.btn_i)

    def click_tap_to_close(self):
        self.click_element(element_data=ElementsData.LeaderBoardPanel.tap_to_close)

    def get_coin(self):
        coin = resource.str_to_int(self.get_text(element_data=ElementsData.LeaderBoardPanel.coin))
        return coin

    def get_top_100_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.LeaderBoardPanel.top_100_rewards_icon_list)
        return icon_list

    def get_top_100_rewards_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.LeaderBoardPanel.top_100_rewards_icon_list)
        return position_list

    def get_top_100_rewards_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.LeaderBoardPanel.top_100_rewards_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    def get_ranking(self):
        return int(self.get_text(element_data=ElementsData.LeaderBoardPanel.ranking))

    def get_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.LeaderBoardPanel.rewards_icon_list)
        return icon_list

    def get_rewards_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.LeaderBoardPanel.rewards_icon_list)
        return position_list

    def get_rewards_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.LeaderBoardPanel.rewards_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    def click_btn_playercard(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.LeaderBoardPanel.btn_playercard_list, element_viewport=ElementsData.LeaderBoardPanel.viewport, viewport_direction="column", index=index)

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.LeaderBoardPanel.item_list, element_viewport=ElementsData.LeaderBoardPanel.viewport, viewport_direction="column", index=index)

    def click_btn_playercard_myself(self):
        self.click_element(element_data=ElementsData.LeaderBoardPanel.btn_playercard_myself)

    def click_item_myself(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.LeaderBoardPanel.item_list_myself, index=index)


    operation_pool = [
        {"element_data": ElementsData.LeaderBoardPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.LeaderBoardPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.LeaderBoardPanel.btn_playercard_list, "func": click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.LeaderBoardPanel.btn_playercard_myself, "func": click_btn_playercard_myself, "weight": 1},
        {"element_data": ElementsData.LeaderBoardPanel.item_list, "func": click_item, "weight": 1},
        {"element_data": ElementsData.LeaderBoardPanel.item_list_myself, "func": click_item_myself, "weight": 1},
        {"element_data": ElementsData.LeaderBoardPanel.tap_to_close, "func": click_tap_to_close, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # LeaderBoardPanel.click_btn_close(bp)
    # LeaderBoardPanel.click_btn_i(bp)
    # LeaderBoardPanel.click_btn_playercard(bp, 5)
    # LeaderBoardPanel.click_btn_playercard_myself(bp)
    LeaderBoardPanel.click_item(bp, 18)
    # LeaderBoardPanel.click_item_myself(bp)
    # LeaderBoardPanel.click_tap_to_close(bp)
    bp.connect_close()