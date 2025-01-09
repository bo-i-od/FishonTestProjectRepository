import random

from tools import commonTools
from common.basePage import BasePage
from configs.elementsData import ElementsData


class PVEMultiRoomFriendPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVEMultiRoomFriendPanel.PVEMultiRoomFriendPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_close)

    def click_btn_invite(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_invite_list, element_viewport=ElementsData.PVEMultiRoomFriendPanel.viewport, viewport_direction="column",index=index)

    def click_btn_playercard(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_playercard_list, element_viewport=ElementsData.PVEMultiRoomFriendPanel.viewport, viewport_direction="column", index=index)

    def get_player_name_list(self):
        return self.get_text_list(element_data=ElementsData.PVEMultiRoomFriendPanel.player_name_list)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVEMultiRoomFriendPanel.tab_list, index=index)

    def click_toggle(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriendPanel.toggle)

    def input_search(self, text=None):
        if text is None:
            player_name_list = PVEMultiRoomFriendPanel.get_player_name_list(self)
            if player_name_list:
                text = player_name_list[0]
            else:
                text = commonTools.generate_random_string(random.randint(0, 15))
        self.set_text(element_data=ElementsData.PVEMultiRoomFriendPanel.Input_search, text=text)

    def click_btn_search(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_search)

    def click_btn_close_search(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_close_search)

    def click_btn_buff_all(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_buff_all)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriendPanel.btn_close_tips)


    operation_pool = [
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_buff_all, "func": click_btn_buff_all, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 10},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_invite_list, "func": click_btn_invite, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_playercard_list, "func": click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_search, "func": click_btn_search, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.btn_close_search, "func": click_btn_close_search, "weight": 5},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.toggle, "func": click_toggle, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.Input_search, "func": input_search, "weight": 1},
        {"element_data": ElementsData.PVEMultiRoomFriendPanel.tab_list, "func": switch_tab, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # PVEMultiRoomFriendPanel.click_btn_buff_all(bp)
    # PVEMultiRoomFriendPanel.click_btn_close(bp)
    # PVEMultiRoomFriendPanel.click_btn_close_tips(bp)
    # PVEMultiRoomFriendPanel.click_btn_invite(bp)
    # PVEMultiRoomFriendPanel.click_btn_playercard(bp)
    # PVEMultiRoomFriendPanel.click_btn_search(bp)
    # PVEMultiRoomFriendPanel.click_btn_close_search(bp)
    # PVEMultiRoomFriendPanel.click_toggle(bp)
    # PVEMultiRoomFriendPanel.input_search(bp)
    # PVEMultiRoomFriendPanel.is_panel_active(bp)
    PVEMultiRoomFriendPanel.switch_tab(bp)
    bp.connect_close()