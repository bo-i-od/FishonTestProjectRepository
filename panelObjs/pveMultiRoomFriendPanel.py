from common.basePage import BasePage
from configs.elementsData import ElementsData


class PVEMultiRoomFriendPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVEMultiRoomFriend.PVEMultiRoomFriendPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVEMultiRoomFriend.btn_close)