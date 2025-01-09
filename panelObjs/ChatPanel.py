import uuid

import six

from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.RewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *
from common.viewport import Viewport

class ChatPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ChatPanel.ChatPanel)

    def input_text(self, text=None):
        if text is None:
            text = six.text_type(uuid.uuid4())
        self.set_text(element_data=ElementsData.ChatPanel.Input_enter, text=text)

    def get_input(self):
        return self.get_text(element_data=ElementsData.ChatPanel.Input_enter)

    def click_btn_enter(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_enter)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChatPanel.tab_list, element_viewport=ElementsData.ChatPanel.viewport_tab,  viewport_direction="column", index=index)

    def click_btn_nothing(self):
        self.click_element(element_data=ElementsData.ChatPanel.btns_nothing)

    def click_btn_emoji(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_emoji)

    def click_btn_share(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_share)

    def click_btn_close_share(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_close_share)

    def click_btn_fisheries(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_fisheries)

    def click_toggle(self):
        self.click_element(element_data=ElementsData.ChatPanel.toggle)

    def switch_tab_list_emoji(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChatPanel.tab_list_emoji, element_viewport=ElementsData.ChatPanel.viewport_tab_list_emoji,  viewport_direction="row",index=index)

    def click_emoji(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChatPanel.emoji_list, element_viewport=ElementsData.ChatPanel.viewport_emoji, viewport_direction="column", index=index)

    def click_btn_close_emoji(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_close_emoji)

    def click_object_of_btn_share_list(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChatPanel.btn_share_list, element_viewport=ElementsData.ChatPanel.viewport_share, viewport_direction="column",index=index)

    def click_head(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChatPanel.head_list, element_viewport=ElementsData.ChatPanel.viewport_info, viewport_direction="column", index=index)

    def click_btn_edit(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_edit)

    def click_btn_close_tips_title_edit(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_close_tips_title_edit)

    def click_btn_tips_title_edit(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChatPanel.btns_tips_title_edit, index=index)

    def click_btn_fast(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_fast)

    def click_btn_send(self):
        self.click_element(element_data=ElementsData.ChatPanel.btn_send)

    operation_pool = [
        {"element_data": ElementsData.ChatPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.ChatPanel.tab_list, "func": switch_tab, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btns_nothing, "func": click_btn_nothing, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_enter, "func": click_btn_enter, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_emoji, "func": click_btn_emoji, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_close_emoji, "func": click_btn_close_emoji, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_share, "func": click_btn_share, "weight": 1},
        {"element_data": ElementsData.ChatPanel.toggle, "func": click_toggle, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_fisheries, "func": click_btn_fisheries, "weight": 1},
        {"element_data": ElementsData.ChatPanel.Input_enter, "func": input_text, "weight": 2},
        {"element_data": ElementsData.ChatPanel.tab_list_emoji, "func": switch_tab_list_emoji, "weight": 1},
        {"element_data": ElementsData.ChatPanel.emoji_list, "func": click_emoji, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_share_list, "func": click_object_of_btn_share_list, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_close_share, "func": click_btn_close_share, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_edit, "func": click_btn_edit, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_close_tips_title_edit, "func": click_btn_close_tips_title_edit, "weight": 10},
        {"element_data": ElementsData.ChatPanel.btns_tips_title_edit, "func": click_btn_tips_title_edit, "weight": 20},
        {"element_data": ElementsData.ChatPanel.btn_fast, "func": click_btn_fast, "weight": 1},
        {"element_data": ElementsData.ChatPanel.btn_send, "func": click_btn_send, "weight": 10},
        # {"element_data": ElementsData.ChatPanel.item_list, "func": click_item, "weight": 1},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21523", is_mobile_device=False)
    # ChatPanel.input_text(bp)

    # ChatPanel.switch_tab_list_emoji(bp)

    # ChatPanel.click_emoji(bp)

    # ChatPanel.click_btn_fisheries(bp)

    # ChatPanel.click_head(bp, 2)

    # ChatPanel.click_btn_close_share(bp)

    # ChatPanel.click_object_of_btn_share_list(bp)

    # ChatPanel.click_btn_edit(bp)

    # ChatPanel.click_btn_close_tips_title_edit(bp)

    # ChatPanel.click_btn_tips_title_edit(bp)
    #
    # ChatPanel.click_btn_fast(bp)

    ChatPanel.click_btn_close_emoji(bp)

    bp.connect_close()