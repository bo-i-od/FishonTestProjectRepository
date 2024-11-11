from poco.utils.simplerpc.utils import RemoteError
from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.flashCardReceivePanel import FlashCardReceivePanel
from panelObjs.resultPanel import ResultPanel
from tools.commonTools import *
class BattlePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Battle.BattlePanel)

    def is_reel_active(self):
        return self.exist(element_data=ElementsData.Battle.btn_reel)

    def qte0(self):
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

    def qte(self):
        element_data_list = [ElementsData.Battle.qte_left, ElementsData.Battle.qte_right, ElementsData.Battle.qte_up, ElementsData.Battle.qte_jump_left, ElementsData.Battle.qte_jump_right, ElementsData.Battle.hud_power_list, ElementsData.Battle.hud_power_list_old, ElementsData.Result.btn_claim, ElementsData.Result.btn_claim_token_fish, ElementsData.BattleFailed.btn_again, ElementsData.FlashCardReceive.FlashCardReceivePanel]
        qte_left_index = element_data_list.index(ElementsData.Battle.qte_left)
        qte_right_index = element_data_list.index(ElementsData.Battle.qte_right)
        qte_up_index = element_data_list.index(ElementsData.Battle.qte_up)
        qte_jump_left_index = element_data_list.index(ElementsData.Battle.qte_jump_left)
        qte_jump_right_index = element_data_list.index(ElementsData.Battle.qte_jump_right)
        hud_power_list_index = element_data_list.index(ElementsData.Battle.hud_power_list)
        hud_power_list_old_index = element_data_list.index(ElementsData.Battle.hud_power_list_old)
        btn_claim_index = element_data_list.index(ElementsData.Result.btn_claim)
        btn_claim_token_fish_index = element_data_list.index(ElementsData.Result.btn_claim_token_fish)
        btn_again_index = element_data_list.index(ElementsData.BattleFailed.btn_again)
        FlashCardReceivePanel_index = element_data_list.index(ElementsData.FlashCardReceive.FlashCardReceivePanel)

        while True:
            object_id_list = self.get_object_id_list(element_data_list=element_data_list)
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
            if object_id_list[btn_claim_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.Result.btn_claim)
                break
            if object_id_list[btn_claim_token_fish_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.Result.btn_claim_token_fish)
                break
            if object_id_list[btn_again_index]:
                ResultPanel.automatic_settlement(self, element_btn=ElementsData.BattleFailed.btn_again)
                break
            if object_id_list[FlashCardReceivePanel_index]:
                self.clear_popup()
                continue


    def slide(self, dir):
        if dir == "left":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.2, 0.6], t=0.15)
            return
        if dir == "right":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.6, 0.6], t=0.15)
            return
        if dir == "up":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.4, 0.4], t=0.15)
            return
        if dir == "down":
            self.swipe(point_start=[0.4, 0.6], point_end=[0.4, 0.8], t=0.15)
            return

    def release_btn_reel(self):
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="up")

    def hold_btn_reel(self):
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="down")


    def click_btn_reel(self):
        self.click_element(element_data=ElementsData.Battle.btn_reel)


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
        self.wait_for_appear(element_data=ElementsData.Battle.btn_reel, is_click=False, timeout=25)
        # 如果没有刺鱼就跳过
        progress_position = self.get_position_list(element_data=ElementsData.Battle.progress)
        if not progress_position:
            return
        progress_size = self.get_size(element_data=ElementsData.Battle.progress)
        h = progress_size[1]
        range = [progress_position[0][1] - 0.5 * h, progress_position[0][1] + 0.5 * h]
        arrow_position = self.get_position_list(element_data=ElementsData.Battle.arrow)
        if not arrow_position:
            return
        progress = (arrow_position[0][1] - range[0]) / h
        while progress < 0.7:
            arrow_position = self.get_position_list(element_data=ElementsData.Battle.arrow)
            if not arrow_position:
                return
            progress = (arrow_position[0][1] - range[0]) / h
            self.sleep(0.05)
        try:
            self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="down")
        except RemoteError:
            pass

        # self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="up")
        # self.click_position_base(position_btn_reel)

    def hook_guide(self):
        perform_list = [ElementsData.NewbieGuide.NBG_hook_1, ElementsData.NewbieGuide.NBG_hook_2, ElementsData.NewbieGuide.NBG_hook_3, ElementsData.NewbieGuide.NBG_hook_5]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(ElementsData.NewbieGuide.NBG_hook_5)

    def hook_guide_oversea(self):
        perform_list_oversea = [ElementsData.NewbieGuide.NBG_hook_4, ElementsData.NewbieGuide.NBG_hook_5]
        self.click_a_until_b_appear_list(perform_list_oversea)
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
        return self.exist(element_data=ElementsData.Battle.warning)



if __name__ == '__main__':
    bp = BasePage()
    while True:
        hud_escaping = bp.get_text_list(element_data=ElementsData.Battle.hud_escaping)
        if not hud_escaping:
            bp.sleep(0.1)
            continue
        print(hud_escaping[0][:-1])
        bp.sleep(0.1)
