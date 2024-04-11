from common.basePage import BasePage
from configs.elementsData import ElementsData
from threading import Thread
from tools.commonTools import *
class BattlePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Battle.BattlePanel):
            return True
        return False

    def is_reel_active(self):
        if self.exist(element_data=ElementsData.Battle.btn_reel):
            return True
        return False

    def qte(self):
        qte_flag_left = False
        qte_flag_right = False
        while not self.exist(element_data=ElementsData.Result.ResultPanel):
            if self.exist(element_data=ElementsData.Battle.tip_slide):
                BattlePanel.unleash_power(self)
                continue
            if self.exist(element_data=ElementsData.Battle.qte_left) or self.exist(element_data=ElementsData.Battle.qte_jump_left):
                if not qte_flag_left:
                    BattlePanel.slide(self,"left")
                    continue
            else:
                qte_flag_left = False
            if self.exist(element_data=ElementsData.Battle.qte_right) or self.exist(element_data=ElementsData.Battle.qte_jump_right):
                if not qte_flag_right:
                    BattlePanel.slide(self,"right")
                    continue
            else:
                qte_flag_right = False



    def slide(self, dir):
        if dir == "left":
            self.swipe(point_start=[0.3, 0.7], point_end=[0.2, 0.7], t=0.1)
        if dir == "right":
            self.swipe(point_start=[0.3, 0.7], point_end=[0.4, 0.7], t=0.1)




    def click_btn_reel(self):
        self.click_element(element_data=ElementsData.Battle.btn_reel)

    # unity上才能用
    def reel_quick(self):
        while not self.exist(element_data=ElementsData.Result.ResultPanel):
            self.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            self.sleep(1)


    def unleash_power(self):
        # 得到reel按钮的位置
        pos_start = self.get_position(element_data=ElementsData.Battle.btn_reel)
        pos_end = []
        pos_end.append(pos_start[0])
        pos_end.append(pos_start[1] - 0.3)
        # while self.exist(element_data=ElementsData.Battle.tip_slide):
        self.swipe(point_start=pos_start, point_end=pos_end, t=0.05)
        self.sleep(0.5)

    def hook(self):
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False, timeout=20)
        # 如果没有刺鱼就跳过
        progress_position = self.get_position_list(element_data=ElementsData.Battle.progress)
        if not progress_position:
            return
        progress_size = self.get_size(element_data=ElementsData.Battle.progress)
        h = progress_size[1]
        range = [progress_position[0][1] - 0.5 * h, progress_position[0][1] + 0.5 * h]
        arrow_position = self.get_position(element_data=ElementsData.Battle.arrow)
        progress = (arrow_position[1] - range[0]) / h
        while progress < 0.7:
            arrow_position = self.get_position(element_data=ElementsData.Battle.arrow)
            progress = (arrow_position[1] - range[0]) / h
            self.sleep(0.05)
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="down")
        # self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="up")
        # self.click_position_base(position_btn_reel)

    def hook_guide(self):
        perform_list = [ElementsData.NewbieGuide.NBG_hook_1, ElementsData.NewbieGuide.NBG_hook_2, ElementsData.NewbieGuide.NBG_hook_3, ElementsData.NewbieGuide.NBG_hook_5]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(ElementsData.NewbieGuide.NBG_hook_5)



if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21593")
    a = BattlePanel.reel_quick(bp)
