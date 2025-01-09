from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class PVPResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPResultPanel.PVPResultPanel)

    def click_tap_to_click(self):
        self.click_until_disappear(element_data=ElementsData.PVPResultPanel.tap_to_close, ignore_set={"PVPResultPanel"})

    def get_points_enemy(self):
        points_enemy = self.get_text(element_data=ElementsData.PVPResultPanel.points_enemy)
        return int(points_enemy)

    def get_points_mine(self):
        points_mine = self.get_text(element_data=ElementsData.PVPResultPanel.points_mine)
        return int(points_mine)

    def click_btn_open(self):
        self.click_element(element_data=ElementsData.PVPResultPanel.btn_open)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVPResultPanel.btn_close)

    def get_result_right(self):
        name_list = self.get_text_list(element_data=ElementsData.PVPResultPanel.right_list, offspring_path="text")
        point_list = self.get_text_list(element_data=ElementsData.PVPResultPanel.right_list, offspring_path="points>value_1")
        res = dict(zip(name_list, point_list))
        return res

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPResultPanel.item_list, index=index)

    def click_btn_gear(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPResultPanel.btn_gear_list, index=index)

    def click_btn_playercard(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVPResultPanel.btn_playercard_list, index=index)


    operation_pool = [
        {"element_data": ElementsData.PVPResultPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PVPResultPanel.btn_gear_list, "func": click_btn_gear, "weight": 1},
        {"element_data": ElementsData.PVPResultPanel.btn_open, "func": click_btn_open, "weight": 1},
        {"element_data": ElementsData.PVPResultPanel.btn_playercard_list, "func": click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.PVPResultPanel.item_list, "func": click_item, "weight": 1},
        {"element_data": ElementsData.PVPResultPanel.tap_to_close, "func": click_tap_to_click, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # PVPResultPanel.click_btn_open(bp)
    # PVPResultPanel.click_btn_close(bp)
    # PVPResultPanel.click_btn_gear(bp)
    # PVPResultPanel.click_item(bp)
    PVPResultPanel.click_btn_playercard(bp)
    # PVPResultPanel.click_tap_to_click(bp)
    bp.connect_close()