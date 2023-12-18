from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport

class PVPHallPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PVPHall.PVPHallPanel):
            return True
        return False

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVPHall.btn_close)
        if PVPHallPanel.is_panel_active(self):
            raise FindElementError

    def click_btn_play(self, index=0):
        viewport = Viewport(self, element_viewport=ElementsData.PVPHall.Viewport, element_item_list=ElementsData.PVPHall.entrance_list, viewport_edge=[0.35, 0])
        viewport.move_until_appear(viewport.item_id_list[index])
        position_list = self.get_position_list(element_data=ElementsData.PVPHall.btn_play_list)
        self.click_position(position_list[index])

    def click_btn_turntable(self):
        self.click_element(element_data=ElementsData.PVPHall.btn_turntable)

if __name__ == '__main__':
    bp = BasePage()
    PVPHallPanel.click_btn_play(bp)
