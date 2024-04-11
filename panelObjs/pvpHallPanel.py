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
        size_list = self.get_size_list(element_data=ElementsData.PVPHall.btn_play_list)
        edge_left = size_list[0][0]
        edge_right = 0.8 * size_list[0][0]
        # print(edge_right)
        viewport = Viewport(self, element_viewport=ElementsData.PVPHall.Viewport, element_item_list=ElementsData.PVPHall.btn_play_list, viewport_edge=[edge_left, edge_right])
        while PVPHallPanel.is_panel_active(self):
            try:
                viewport.move_until_appear(viewport.item_id_list[index])
            except:
                print("viewport有问题")
            position_list = self.get_position_list(element_data=ElementsData.PVPHall.btn_play_list)
            if not position_list:
                return
            self.click_position(position_list[index])
            self.sleep(0.5)

    def click_btn_turntable(self):
        self.click_element(element_data=ElementsData.PVPHall.btn_turntable)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.PVPHall.btn_i)

if __name__ == '__main__':
    bp = BasePage()
    PVPHallPanel.click_btn_play(bp, 0)
