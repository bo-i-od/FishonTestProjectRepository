from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *
from common.viewport import Viewport

class ChatPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Chat.btn_close)
        if ChatPanel.is_panel_active(self):
            return FindElementError

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Chat.ChatPanel)

    def input_text(self, text):
        self.set_text(element_data=ElementsData.Chat.Input_enter, text=text)

    def get_input(self):
        return self.get_text(element_data=ElementsData.Chat.Input_enter)

    def click_btn_enter(self):
        self.click_element(element_data=ElementsData.Chat.btn_enter)
