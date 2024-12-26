from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPRoomPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPRoomPanel.PVPRoomPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVPRoomPanel.btn_close)

    def click_btn_start(self):
        position_list = self.get_position_list(element_data=ElementsData.PVPRoomPanel.btn_start)
        if not position_list:
            return
        self.click_position(position_list[0])
