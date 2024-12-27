from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPRoomInvitePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPRoomInvitePanel.PVPRoomInvitePanel)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.btn_confirm)

    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.btn_cancel)