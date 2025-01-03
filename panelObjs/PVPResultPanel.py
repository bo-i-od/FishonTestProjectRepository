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

    def get_result_right(self):
        name_list = self.get_text_list(element_data=ElementsData.PVPResultPanel.right_list, offspring_path="text")
        point_list = self.get_text_list(element_data=ElementsData.PVPResultPanel.right_list, offspring_path="points>value_1")
        res = dict(zip(name_list, point_list))
        return res

if __name__ == '__main__':
    bp = BasePage()
    a = PVPResultPanel.get_result_right(bp)
    print(a)