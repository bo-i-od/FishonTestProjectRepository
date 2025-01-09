from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPRoomInvitePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPRoomInvitePanel.PVPRoomInvitePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.btn_close, ignore_set={"PVPRoomInvitePanel"})

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.btn_confirm, ignore_set={"PVPRoomInvitePanel"})

    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.btn_cancel, ignore_set={"PVPRoomInvitePanel"})

    def click_toggle(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.toggle, ignore_set={"PVPRoomInvitePanel"})

    def click_btn_playercard(self):
        self.click_element(element_data=ElementsData.PVPRoomInvitePanel.btn_playercard, ignore_set={"PVPRoomInvitePanel"})


    operation_pool = [
        {"element_data": ElementsData.PVPRoomInvitePanel.btn_cancel, "func": click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.PVPRoomInvitePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PVPRoomInvitePanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.PVPRoomInvitePanel.btn_playercard, "func": click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.PVPRoomInvitePanel.toggle, "func": click_toggle, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # PVPRoomInvitePanel.click_btn_cancel(bp)
    # PVPRoomInvitePanel.click_btn_close(bp)
    # PVPRoomInvitePanel.click_btn_confirm(bp)
    PVPRoomInvitePanel.click_btn_playercard(bp)
    PVPRoomInvitePanel.click_toggle(bp)
    bp.connect_close()
