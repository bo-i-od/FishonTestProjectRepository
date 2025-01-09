from common.basePage import BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData

class FriendPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FriendPanel.FriendPanel)

    def add_friend(self, id):
        self.click_element(element_data=ElementsData.FriendPanel.btn_add_friend)
        FriendPanel.input_search(text=id)
        self.sleep(1)
        self.click_element(element_data=ElementsData.FriendPanel.btn_search)
        self.sleep(4)
        self.click_element(element_data=ElementsData.FriendPanel.btn_search)
        self.sleep(1)
        FriendPanel.click_btn_add(self)

    def get_player_name_list(self):
        player_name_list = self.get_text_list(element_data=ElementsData.FriendPanel.player_name_list)
        return player_name_list

    def input_search(self, text=None):
        if text is None:
            player_name_list = FriendPanel.get_player_name_list(self)
            if player_name_list:
                text = player_name_list[0]
        self.click_element(element_data=ElementsData.FriendPanel.input_search)
        self.set_text(element_data=ElementsData.FriendPanel.input_search, text=text)

    def click_btn_add(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_add_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column",  index=index)

    def click_btn_cancel(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_cancel_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column",  index=index)

    def click_btn_confirm(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_confirm_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column",  index=index)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_close)

    def click_btn_close_search(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_close_search)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.tab_list, index=index)

    def switch_tab_sub(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.tab_list_sub, index=index)

    def click_btn_edit(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_edit_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column",  index=index)

    def click_btn_power(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_power_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column",  index=index)

    def click_btn_chat(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_chat_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column",  index=index)

    def click_btn_playercard(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btn_playercard_list, element_viewport=ElementsData.FriendPanel.viewport, viewport_direction="column", index=index)

    def click_btn_fastgive(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_fastgive)

    def click_btn_receive(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_receive)

    def click_btn_refresh(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_refresh)

    def click_btn_invite(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_invite)

    def click_btn_delete(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_delete)

    def click_toggle_online(self):
        self.click_element(element_data=ElementsData.FriendPanel.toggle_online)

    def click_toggle_receive(self):
        self.click_element(element_data=ElementsData.FriendPanel.toggle_receive)

    def click_btn_tips(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FriendPanel.btns_tips, index=index)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.FriendPanel.btn_close_tips)

    operation_pool = [
        {"element_data": ElementsData.FriendPanel.btn_add_list, "func": click_btn_add, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_cancel_list, "func": click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_chat_list, "func": click_btn_chat, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_close_search, "func": click_btn_close_search, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_confirm_list, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_delete, "func": click_btn_delete, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_edit_list, "func": click_btn_edit, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_fastgive, "func": click_btn_fastgive, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_invite, "func": click_btn_invite, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_power_list, "func": click_btn_power, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_receive, "func": click_btn_receive, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_refresh, "func": click_btn_refresh, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_playercard_list, "func": click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.FriendPanel.tab_list, "func": switch_tab, "weight": 1},
        {"element_data": ElementsData.FriendPanel.tab_list_sub, "func": switch_tab_sub, "weight": 1},
        {"element_data": ElementsData.FriendPanel.toggle_online, "func": click_toggle_online, "weight": 1},
        {"element_data": ElementsData.FriendPanel.toggle_receive, "func": click_toggle_receive, "weight": 1},
        {"element_data": ElementsData.FriendPanel.input_search, "func": input_search, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btns_tips, "func": click_btn_tips, "weight": 1},
        {"element_data": ElementsData.FriendPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # FriendPanel.click_btn_add(bp)
    # FriendPanel.click_btn_cancel(bp)
    # FriendPanel.click_btn_chat(bp)
    # FriendPanel.click_btn_close(bp)
    # FriendPanel.click_btn_confirm(bp)
    # FriendPanel.click_btn_delete(bp)
    # FriendPanel.click_btn_edit(bp)
    # FriendPanel.click_btn_fastgive(bp)
    # FriendPanel.click_btn_invite(bp)
    # FriendPanel.click_btn_power(bp)
    # FriendPanel.click_btn_receive(bp)
    # FriendPanel.click_btn_refresh(bp)
    # FriendPanel.click_player_info(bp)
    # FriendPanel.is_panel_active(bp)
    # FriendPanel.switch_tab(bp)
    # FriendPanel.switch_tab_sub(bp)
    # FriendPanel.click_toggle_online(bp)
    # FriendPanel.click_toggle_receive(bp)
    # FriendPanel.input_search(bp)
    # FriendPanel.click_btn_close_search(bp)
    # FriendPanel.click_btn_tips(bp)
    FriendPanel.click_btn_close_tips(bp)
    bp.connect_close()
