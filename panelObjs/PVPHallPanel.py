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

    def click_btn_play(self, index=-1):
        size_list = self.get_size_list(element_data=ElementsData.PVPHallPanel.btn_play_list)
        edge_left = size_list[0][0]
        self.click_object_of_plural_objects(element_data=ElementsData.PVPHallPanel.btn_play_list, element_viewport=ElementsData.PVPHallPanel.Viewport,  viewport_edge=[edge_left, 0], viewport_direction="row", index=index)

    def get_btn_play_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PVPHallPanel.btn_play_list)
        return position_list

    def click_btn_turntable(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_turntable)

    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_leaderboard)

    def click_crown(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.crown)

    def click_btn_friendly(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_friendly)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPHallPanel.top_res_btns, index=index)

    def click_btn_create(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_create)

    def click_btn_join(self):
        self.click_element(element_data=ElementsData.PVPHallPanel.btn_join)

    def click_rule(self, index=-1):
        size_list = self.get_size_list(element_data=ElementsData.PVPHallPanel.btn_play_list)
        edge_left = size_list[0][0] * 1.2
        edge_right = size_list[0][0]
        self.click_object_of_plural_objects(element_data=ElementsData.PVPHallPanel.rule_list, element_viewport=ElementsData.PVPHallPanel.Viewport,  viewport_edge=[edge_left, edge_right], index=index)

    def click_btn_close_tips(self):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPHallPanel.btn_close_tips)

    operation_pool = [
        {"element_data": ElementsData.PVPHallPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_create, "func": click_btn_create, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_friendly, "func": click_btn_friendly, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_join, "func": click_btn_join, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_leaderboard, "func": click_btn_leaderboard, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_play_list, "func": click_btn_play, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.btn_turntable, "func": click_btn_turntable, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.crown, "func": click_crown, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.rule_list, "func": click_rule, "weight": 1},
        {"element_data": ElementsData.PVPHallPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21593", is_mobile_device=True)
    # PVPHallPanel.click_btn_close(bp)
    # PVPHallPanel.click_btn_close_tips(bp)
    # PVPHallPanel.click_btn_create(bp)
    # PVPHallPanel.click_btn_friendly(bp)
    # PVPHallPanel.click_btn_join(bp)
    # PVPHallPanel.click_btn_leaderboard(bp)
    PVPHallPanel.click_btn_play(bp, 0)
    # PVPHallPanel.click_btn_turntable(bp)
    # PVPHallPanel.click_crown(bp)
    # PVPHallPanel.click_rule(bp)
    # PVPHallPanel.click_top_res_btn(bp)
    bp.connect_close()

