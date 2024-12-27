from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class PVPHallPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPHallPanel.PVPHallPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_close)


    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPHallPanel.PVPHallPanel, ignore_set={"PVPHallPanel"})

    def click_btn_play(self, index=0):
        size_list = self.get_size_list(element_data=ElementsData.PVPHallPanel.btn_play_list)
        edge_left = size_list[0][0] * 1.2
        edge_right = size_list[0][0]
        # edge_right = 0.8 * size_list[0][0]
        # print(edge_right)
        viewport = Viewport(self, element_viewport=ElementsData.PVPHallPanel.Viewport, element_item_list=ElementsData.PVPHallPanel.btn_play_list, viewport_edge=[edge_left, edge_right], viewport_direction="row")
        while PVPHallPanel.is_panel_active(self):
            try:
                viewport.move_until_appear(viewport.item_id_list[index])
            except:
                print("viewport有问题")
            position_list = PVPHallPanel.get_btn_play_position_list(self)
            if not position_list:
                return
            self.click_position(position_list[index])
            self.sleep(1)

    def get_btn_play_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PVPHallPanel.btn_play_list)
        return position_list

    def click_btn_turntable(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_turntable)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_i)

    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_leaderboard)

if __name__ == '__main__':
    bp = BasePage(serial_number="127.0.0.1:21553", is_mobile_device=True)
    # position_list = bp.get_position_list(element_data=ElementsData.PVPHall.btn_play_list)
    # print(position_list)
    # bp.connect_close()
    # size_list = bp.get_size_list(element_data=ElementsData.PVPHall.btn_play_list)
    # edge_left = size_list[0][0]
    # edge_right = size_list[0][0]
    # # edge_right = 0.8 * size_list[0][0]
    # # print(edge_right)
    # viewport = Viewport(bp, element_viewport=ElementsData.PVPHall.Viewport,
    #                     element_item_list=ElementsData.PVPHall.btn_play_list, viewport_edge=[edge_left, edge_right])
    # while PVPHallPanel.is_panel_active(bp):
    #     try:
    #         viewport.move_until_appear(viewport.item_id_list[index])
    #     except:
    #         print("viewport有问题")
    #     position_list = self.get_position_list(element_data=ElementsData.PVPHall.btn_play_list)
    #     if not position_list:
    #         return
    PVPHallPanel.click_btn_play(bp, 0)
    bp.connect_close()
