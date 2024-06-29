import time

from common.basePage import BasePage
from configs.elementsData import ElementsData
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
        while True:
            qte_id_list = self.get_parent_id_list(element_data=ElementsData.Battle.qte_list)
            name_list = self.get_name_list(object_id_list=qte_id_list)
            if not name_list:
                hud_power_list = self.get_object_id_list(element_data=ElementsData.Battle.hud_power_list)
                if len(hud_power_list) > 2:
                    BattlePanel.unleash_power(self)
                    # self.sleep(0.5)
                    continue
                if self.exist(element_data=ElementsData.Result.ResultPanel):
                    break
                continue
            if "left" in name_list[0]:
                BattlePanel.slide(self, "left")
                continue
            if "right" in name_list[0]:
                BattlePanel.slide(self, "right")
                continue
            if "up" in name_list[0]:
                BattlePanel.slide(self, "up")
                continue

    # def qte(self):
    #     while True:
    #         try:
    #             if self.qte_queue is None:
    #                 self.sleep(0.1)
    #                 continue
    #             item = self.qte_queue.get_nowait()
    #             if item == 0:
    #                 BattlePanel.slide(self, "up")
    #             elif item == 1:
    #                 BattlePanel.slide(self, "left")
    #             elif item == 2:
    #                 BattlePanel.slide(self, "right")
    #             elif item == 3:
    #                 BattlePanel.slide(self, "left")
    #             elif item == 4:
    #                 BattlePanel.slide(self, "right")
    #             elif item == 5:
    #                 BattlePanel.unleash_power(self)
    #             self.sleep(0.2)
    #             # self.qte_check = item
    #         except:
    #             try:
    #                 if self.exist(element_data=ElementsData.Result.ResultPanel):
    #                     break
    #             except:
    #                 break

    def slide(self, dir):
        if dir == "left":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.2, 0.6], t=0.1)
            return
        if dir == "right":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.6, 0.6], t=0.1)
            return
        if dir == "up":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.4, 0.4], t=0.1)
            return
        if dir == "down":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.4, 0.8], t=0.1)
            return

    def release_btn_reel(self):
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="up")

    def hold_btn_reel(self):
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="down")


    def click_btn_reel(self):
        self.click_element(element_data=ElementsData.Battle.btn_reel)

    # unity上才能用
    def reel_quick(self):
        while not self.exist(element_data=ElementsData.Result.ResultPanel):
            self.clear_popup_once()
            self.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            self.sleep(1)


    def unleash_power(self):
        # 得到reel按钮的位置
        try:
            pos_start = self.get_position(element_data=ElementsData.Battle.btn_reel)
            pos_end = []
            pos_end.append(pos_start[0])
            pos_end.append(pos_start[1] - 0.3)
            # while self.exist(element_data=ElementsData.Battle.tip_slide):
            self.swipe(point_start=pos_start, point_end=pos_end, t=0.05)
            self.sleep(0.5)
        except:
            pass

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


    def get_distance(self):
        m_value = self.get_text_list(element_data=ElementsData.Battle.m_value)
        if not m_value:
            return None
        pattern = r'\d+\.\d+|\d+'
        match = re.search(pattern, m_value)
        m = match.group()
        return float(m)

    def is_warning_active(self):
        if self.exist(element_data=ElementsData.Battle.warning):
            return True
        return False



if __name__ == '__main__':
    bp = BasePage()
    bp.set_object_active(element_data=ElementsData.Login.LoginPanel, active=True)
