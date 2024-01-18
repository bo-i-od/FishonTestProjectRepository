from common.basePage import BasePage
from configs.elementsData import ElementsData
from threading import Thread
from tools.commonTools import *
class BattlePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Battle.BattlePanel):
            return True
        return False
    def reel(self):
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False)
        position = self.get_position(element_data=ElementsData.Battle.btn_reel)
        while self.exist(element_data=ElementsData.Battle.btn_reel):
            self.press_position(position, duration=2.5)
            self.sleep(0.1)
        # self.send_key("G")

    def click_btn_reel(self):
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=True)

    # unity上才能用
    def reel_quick(self):
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False)
        self.sleep(2)
        self.click_element(element_data=ElementsData.Battle.btn_reel)
        while not self.exist(element_data=ElementsData.Result.ResultPanel):
            self.send_key("G")
            self.sleep(0.5)


    def unleash_power(self):
        # 得到reel按钮的位置
        pos_start = self.get_position(element_data=ElementsData.Battle.btn_reel)
        pos_end = []
        pos_end.append(pos_start[0])
        pos_end.append(pos_start[1] - 0.3)
        # while self.exist(element_data=ElementsData.Battle.tip_slide):
        self.swipe(point_start=pos_start, point_end=pos_end)
        self.sleep(0.5)