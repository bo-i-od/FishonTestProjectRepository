import time
from poco.utils.simplerpc.utils import RemoteError
from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.FlashCardReceivePanel import FlashCardReceivePanel
from panelObjs.ResultPanel import ResultPanel
from tools.commonTools import *


class BattlePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePanel.BattlePanel)

    def is_reel_active(self):
        return self.exist(element_data=ElementsData.BattlePanel.btn_reel)

    def qte(self, start_time=None):
        element_data_list = [
            ElementsData.BattlePanel.qte_left,
            ElementsData.BattlePanel.qte_right,
            ElementsData.BattlePanel.qte_up,
            ElementsData.BattlePanel.qte_jump_left,
            ElementsData.BattlePanel.qte_jump_right,
            ElementsData.BattlePanel.hud_power_list,
            ElementsData.BattlePanel.hud_power_list_old,
            ElementsData.ResultPanel.btn_claim_pve,
            ElementsData.ResultPanel.btn_claim_pvp,
            ElementsData.ResultPanel.btn_claim_token_fish,
            ElementsData.BattleFailedPanel.btn_again,
            ElementsData.FlashCardReceivePanel.FlashCardReceivePanel,
            ElementsData.BattlePanel.BattlePanel,
            ElementsData.BattlePanel.crt,
        ]
        qte_left_index = element_data_list.index(ElementsData.BattlePanel.qte_left)
        qte_right_index = element_data_list.index(ElementsData.BattlePanel.qte_right)
        qte_up_index = element_data_list.index(ElementsData.BattlePanel.qte_up)
        qte_jump_left_index = element_data_list.index(ElementsData.BattlePanel.qte_jump_left)
        qte_jump_right_index = element_data_list.index(ElementsData.BattlePanel.qte_jump_right)
        hud_power_list_index = element_data_list.index(ElementsData.BattlePanel.hud_power_list)
        hud_power_list_old_index = element_data_list.index(ElementsData.BattlePanel.hud_power_list_old)
        btn_claim_pve_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_pve)
        btn_claim_pvp_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_pvp)
        btn_claim_token_fish_index = element_data_list.index(ElementsData.ResultPanel.btn_claim_token_fish)
        btn_again_index = element_data_list.index(ElementsData.BattleFailedPanel.btn_again)
        FlashCardReceivePanel_index = element_data_list.index(ElementsData.FlashCardReceivePanel.FlashCardReceivePanel)
        BattlePanel_index = element_data_list.index(ElementsData.BattlePanel.BattlePanel)
        crt_index = element_data_list.index(ElementsData.BattlePanel.crt)
        size_tension = None
        is_in_crt_pre = False
        # False且当前在张力区间代表首次进入，变为True
        # True且当前在张力区间代表非首次进入
        # True且不在张力区间代表非首次退出， 变为False
        end_time = None
        while True:
            object_id_list = self.get_object_id_list(element_data_list=element_data_list)

            if object_id_list[crt_index]:
                if size_tension is None:
                    size_tension = self.get_size(element_data=ElementsData.BattlePanel.hud_tension)
                if not is_in_crt_pre:
                    is_in_crt_pre = True
                crt_center = BattlePanel.get_crt_center(self, size_tension=size_tension)
                self.custom_cmd(f"setTension {crt_center}")
            else:
                if is_in_crt_pre:
                    is_in_crt_pre = False
                    self.custom_cmd(f"setTension {self.tension_default}")

            if not self.quick_qte:
                if len(object_id_list[hud_power_list_index]) > 2:
                    BattlePanel.unleash_power(self)
                    continue
                if len(object_id_list[hud_power_list_old_index]) > 2:
                    BattlePanel.unleash_power(self)
                    continue
                if object_id_list[qte_up_index]:
                    BattlePanel.slide(self, "up")
                    continue
                if object_id_list[qte_jump_left_index]:
                    BattlePanel.slide(self, "left")
                    continue
                if object_id_list[qte_jump_right_index]:
                    BattlePanel.slide(self, "right")
                    continue
                if object_id_list[qte_left_index]:
                    BattlePanel.slide(self, "left")
                    continue
                if object_id_list[qte_right_index]:
                    BattlePanel.slide(self, "right")
                    continue

            if (not object_id_list[BattlePanel_index]) and (end_time is None) and (start_time is not None):
                end_time = time.time()
                print(f"战斗用时{end_time - start_time}s")
            if object_id_list[btn_claim_pve_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.ResultPanel.btn_claim_pve)
                break
            if object_id_list[btn_claim_pvp_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.ResultPanel.btn_claim_pvp)
                break
            if object_id_list[btn_claim_token_fish_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.ResultPanel.btn_claim_token_fish)
                break
            if object_id_list[btn_again_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.BattleFailedPanel.btn_again)
                break
            if object_id_list[FlashCardReceivePanel_index]:
                self.clear_popup()
                continue

    def slide(self, dir):
        if dir == "left":
            self.swipe_base(point_start=[0.4, 0.6], point_end=[0.2, 0.6], t=0.1)
            return
        if dir == "right":
            self.swipe_base(point_start=[0.4, 0.6], point_end=[0.6, 0.6], t=0.1)
            return
        if dir == "up":
            self.swipe_base(point_start=[0.4, 0.6], point_end=[0.4, 0.4], t=0.1)
            return
        if dir == "down":
            self.swipe_base(point_start=[0.4, 0.6], point_end=[0.4, 0.8], t=0.1)
            return

    def release_btn_reel(self):
        self.ray_input(element_data=ElementsData.BattlePanel.btn_reel, kind="up")

    def hold_btn_reel(self):
        self.ray_input(element_data=ElementsData.BattlePanel.btn_reel, kind="down")

    def click_btn_reel(self):
        self.click_element(element_data=ElementsData.BattlePanel.btn_reel)

    def reel_quick(self):
        while not ResultPanel.is_panel_active(self):
            # if FlashCardReceivePanel.is_panel_active(self):
            #     self.sleep(6)
            #     img = self.get_full_screen_shot()
            #     self.save_img(img)
            #     self.clear_popup()
            #     self.cur += 1
            self.clear_popup()
            # 国内
            self.lua_console(command="GameRoot:GetFishingMatch():GetPlayer().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            # # 海外
            # self.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            self.sleep(1)

    def unleash_power(self):
        # 得到reel按钮的位置
        try:
            pos_start = self.get_position(element_data=ElementsData.BattlePanel.btn_reel)
            pos_end = []
            pos_end.append(pos_start[0])
            pos_end.append(pos_start[1] - 0.3)
            # while self.exist(element_data=ElementsData.Battle.tip_slide):
            self.swipe(point_start=pos_start, point_end=pos_end, t=0.05)
            self.sleep(0.5)
        except:
            pass

    def hook(self):
        self.wait_for_appear(element_data_list=[ElementsData.BattlePanel.btn_reel, ElementsData.ResultPanel.btn_claim_pve, ElementsData.ResultPanel.btn_claim_pvp], is_click=False, timeout=25)
        # 如果没有刺鱼就跳过
        progress_position, arrow_position = self.get_position_list(element_data_list=[ElementsData.BattlePanel.progress, ElementsData.BattlePanel.arrow])
        if not progress_position:
            return
        if not arrow_position:
            return
        progress_size_list = self.get_size_list(element_data=ElementsData.BattlePanel.progress)
        if not progress_size_list:
            return
        progress_size = progress_size_list[0]
        h = progress_size[1]
        progress_range = [progress_position[0][1] - 0.5 * h, progress_position[0][1] + 0.5 * h]

        progress = (arrow_position[0][1] - progress_range[0]) / h
        while progress < 0.8:
            arrow_position = self.get_position_list(element_data=ElementsData.BattlePanel.arrow)
            if not arrow_position:
                return
            progress = (arrow_position[0][1] - progress_range[0]) / h
            self.sleep(0.05)
        try:
            BattlePanel.hold_btn_reel(self)
            self.sleep(0.1)
            BattlePanel.release_btn_reel(self)
        except RemoteError:
            pass

    def hook_guide_oversea(self):
        perform_list_oversea = [ElementsData.NewbieGuidePanel.NBG_hook_4, ElementsData.NewbieGuidePanel.NBG_hook_5]
        self.click_a_until_b_appear_list(perform_list_oversea)
        self.click_until_disappear(ElementsData.NewbieGuidePanel.NBG_hook_5)

    def get_distance(self):
        m_value = self.get_text_list(element_data=ElementsData.BattlePanel.m_value)
        if not m_value:
            return None
        pattern = r'\d+\.\d+|\d+'
        match = re.search(pattern, m_value)
        m = match.group()
        return float(m)

    def is_warning_active(self):
        return self.exist(element_data=ElementsData.BattlePanel.warning)

    def get_crt_center(self, size_tension):
        position_list_tension, position_list_crt = self.get_position_list(
            element_data_list=[ElementsData.BattlePanel.hud_tension, ElementsData.BattlePanel.crt])
        position_crt = position_list_crt[0]
        position_tension = position_list_tension[0]
        return 0.5 + (position_crt[0] - position_tension[0]) / size_tension[0]



if __name__ == '__main__':
    bp = BasePage()
    ResultPanel.automatic_settlement(bp, element_btn=ElementsData.ResultPanel.btn_claim_token_fish)

    # bp.ray_input(kind="click", element_data=ElementsData.ResultPanel.btn_claim_token_fish)
    bp.connect_close()
    # while True:
    #     hud_escaping = bp.get_text_list(element_data=ElementsData.Battle.hud_escaping)
    #     if not hud_escaping:
    #         bp.sleep(0.1)
    #         continue
    #     print(hud_escaping[0][:-1])
    #     bp.sleep(0.1)
