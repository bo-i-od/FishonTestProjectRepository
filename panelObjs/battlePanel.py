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

    # unity上才能用
    def reel_quick(self):
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False)
        while not self.exist(element_data=ElementsData.Result.ResultPanel):
            self.send_key("G")
            self.sleep(0.5)

    def reel_without_sleep(self):
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False)
        position = self.get_position(element_data=ElementsData.Battle.btn_reel)
        print(position)
        hold_reel_thread = Thread(target=BattlePanel.hold_reel, args=[self, position])
        hold_reel_thread.start()
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False)
        print("张力超限")
        # stop_thread(hold_reel_thread)

    def hold_reel(self, position):
        print("开始按")
        try:
            self.press_position(position=position, duration=5)
        except:
            pass
        print("结束按")

    def unleash_power(self):
        # 得到reel按钮的位置
        pos_start = self.get_position(element_data=ElementsData.Battle.btn_reel)
        pos_end = []
        pos_end.append(pos_start[0])
        pos_end.append(pos_start[1] - 0.3)
        # while self.exist(element_data=ElementsData.Battle.tip_slide):
        self.swipe(point_start=pos_start, point_end=pos_end)
        self.sleep(0.5)