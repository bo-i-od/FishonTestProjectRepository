import common.resource
from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource
from netMsg import csMsgAll

from panelObjs.MessageBoxPanel import MessageBoxPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.TournamentsInfoPanel import TournamentsInfoPanel
from tools.commonTools import *

class BattlePreparePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePreparePanel.BattlePreparePanel)

    def wait_for_panel_appear(self):
        while not BattlePreparePanel.is_panel_active(self):
            self.sleep(1)

    # 点击关闭
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePreparePanel.btn_close)
        self.sleep(1)
        if not RewardsPanel.is_panel_active(self):
            return
        RewardsPanel.click_tap_to_claim(self)
        self.sleep(1)
        self.click_element(element_data=ElementsData.BattlePreparePanel.btn_close)
        self.sleep(1)
        if not MessageBoxPanel.is_panel_active(self):
            return
        MessageBoxPanel.click_btn_confirm(self)
        self.sleep(1)
        self.click_element(element_data=ElementsData.BattlePreparePanel.btn_close)


    # 点击抛竿
    def cast(self):
        self.wait_for_appear(element_data=ElementsData.BattlePreparePanel.btn_cast, is_click=False)
        position = self.get_position(element_data=ElementsData.BattlePreparePanel.btn_cast)
        while position and (not self.exist(element_data=ElementsData.BuyEnergyPanel.BuyEnergyPanel)):
            self.click_position(position)
            self.sleep(0.2)

    # 点击抛竿
    def click_btn_cast(self):
        element_data_list = [ElementsData.BattlePreparePanel.panel_MainStage_challenge_prepare.btn_cast, ElementsData.BattlePreparePanel.btn_cast, ElementsData.BattlePreparePanel.btn_start]
        position_list = self.wait_for_appear(element_data_list=element_data_list, is_click=False)
        cur = 0
        while cur < len(position_list):
            position = position_list[cur]
            if not position:
                cur += 1
                continue
            element_data = element_data_list[cur]
            if self.is_ray_input:
                self.ray_input(kind="click", element_data=element_data)

            else:
                self.click_element_safe(element_data=element_data)
            self.sleep(1)
            if self.exist(element_data=ElementsData.BattlePanel.BattlePanel):
                return
            cur += 1
        BattlePreparePanel.click_btn_cast(self)

    # 点击快速换装
    def click_btn_quick_switch(self):
        self.wait_for_appear(element_data=ElementsData.BattlePreparePanel.quick_switch, is_click=True)


    def get_location(self):
        return self.get_text(element_data=ElementsData.BattlePreparePanel.location)

    def click_btn_apply(self):
        self.click_element(element_data=ElementsData.BattlePreparePanel.btn_apply)

    def click_gears(self):
        self.click_element(element_data=ElementsData.BattlePreparePanel.gears)


    def get_btn_icon_warning_position(self):
        return self.get_position_list(element_data=ElementsData.BattlePreparePanel.PanelPrepareWarning.btn_icon)


    class panel_pve_prepare(BasePage):
        def click_btn_tournaments(self):
            while not TournamentsInfoPanel.is_panel_active(self):
                position_list = self.get_position_list(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.btn_tournaments)
                if not position_list:
                    return False
                self.click_position(position_list[0])
                self.sleep(1)
            return True
        # 得到钓点状态


        def get_location_position_list(self):
            location_position_list = self.get_position_list(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.location_list)

            location_position_list += self.get_position_list(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.treasure_list)
            return location_position_list

        def get_energy_list(self):
            location_energy_list = self.get_text_list(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.location_energy_list)
            str_to_int_list(location_energy_list)
            treasure_energy_list = self.get_text_list(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.treasure_energy_list)
            str_to_int_list(treasure_energy_list)
            return location_energy_list + treasure_energy_list

        def click_btn_add_100500(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.btn_add_100500)
        def click_btn_location(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.btn_location)

        def click_btn_collection(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.btn_collection)

        def click_panel_tip_location_newtreasure(self):
            self.click_element(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tip_location_newtreasure)

        def is_panel_tip_location_active(self):
            return self.exist(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tip_location_newtreasure)

        def get_value_cost(self):
            self.wait_for_appear(element_data=ElementsData.BattlePreparePanel.btn_cast, is_click=False)
            value_cost = self.get_text(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.value_cost)
            return int(value_cost)

        def is_wait_for_join(self):
            position_list = self.get_position_list(
                element_data_list=[ElementsData.BattlePreparePanel.panel_pve_prepare.wait_for_join,
                                   ElementsData.BattlePreparePanel.panel_pve_prepare.wait_for_join_new])
            position_list = merge_list(position_list)
            # position_list = self.get_position_list(element_data=ElementsData.BattlePreparePanel.wait_for_join)
            if position_list:
                return True
            return False
        def click_btn_menu(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.btn_menu)

        def get_location_status(self):
            location_id_list = self.get_object_id_list(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.location_list)
            treasure_id_list = self.get_object_id_list(
                element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.treasure_list)
            select_list = []
            selectable_list = []
            cur = 0
            while cur < len(location_id_list):
                select_id_list = self.get_offspring_id_list(object_id=location_id_list[cur],
                                                            offspring_path="select")
                if select_id_list:
                    select_list.append(cur)
                    cur += 1
                    continue
                selectable_list.append(cur)
                cur += 1
            bias = cur
            cur = 0
            while cur < len(treasure_id_list):
                select_id_list = self.get_offspring_id_list(object_id=treasure_id_list[cur],
                                                            offspring_path="select")
                if select_id_list:
                    select_list.append(cur + bias)
                    cur += 1
                    continue
                selectable_list.append(cur + bias)
                cur += 1
            return select_list, selectable_list

        def try_go_to_treasure_map(self, fishery_id):
            # 没有藏宝图直接返回
            if not BattlePreparePanel.panel_pve_prepare.is_panel_tip_location_active(self):
                return

            # 在藏宝图直接返回
            if BattlePreparePanel.panel_pve_prepare.get_value_cost(self) > 10:
                return
            spot_id_list, is_in_double_week, is_new_plot = self.get_spot_id_list(fishery_id=fishery_id)
            spot_id = spot_id_list[3]
            lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id),
                                                             source=0, isInDoubleWeek=is_in_double_week)
            self.lua_console(lua_code)



        class panel_tournaments_mini(BasePage):
            # 点击mini板 打开全局进度条面板
            def click_progress_info(self):
                self.click_element(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.progress_info)

            def is_progress_finish(self):
                return self.exist(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.progress_finish)

            def click_progress_finish(self):
                self.click_element(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.progress_finish)

            # 得到当前累计奖励的图标列表
            def get_current_rewards_icon_list(self):
                icon_list = self.get_icon_list(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.current_rewards_icon_list)
                return icon_list

            # 得到当前累计奖励的数量列表
            def get_current_rewards_quantity_list(self):
                quantity_list = self.get_text_list(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.current_rewards_quantity_list)
                resource.str_to_int_list(quantity_list)
                return quantity_list

            def get_progress(self):
                progress_cur = int(self.get_text(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.progress_cur))
                progress_max = int(self.get_text(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.progress_max))
                return progress_cur, progress_max

            # 得到下一档奖励的数量
            def get_next_reward_quantity(self):
                quantity = resource.str_to_int(self.get_text(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.next_reward_quantity))
                return quantity

            # 得到下一档奖励的图标
            def get_next_reward_icon(self):
                icon = self.get_icon(
                    element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.next_reward_icon)
                return icon



        class Panel_MiniTask(BasePage):
            def click_btn_recommend(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.Panel_MiniTask.btn_recommend)

            def click_btn_go(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.Panel_MiniTask.btn_go)

            def click_btn_gift(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.Panel_MiniTask.btn_gift)

            def get_progress(self):
                progress = self.get_text(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.Panel_MiniTask.progress)
                res = progress.split("/")
                numerator = int(res[0])
                denominator = int(res[1])
                return numerator, denominator

            def click_btn_claim(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.Panel_MiniTask.btn_claim)

            def get_text_task(self):
                return self.get_text(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.Panel_MiniTask.text_task)

        class panel_main_sidebar(BasePage):
            def click_btn_close(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_close)

            def click_btn_player(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.head_img)

            def click_btn_gears(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.gears)

            def click_btn_club(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_club)

            def click_btn_friend(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_friend)

            def click_btn_aquarium(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_aquarium)

            def click_btn_career(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_career)

            def click_btn_fishcard(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_fishcard)

            def click_btn_store(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_store)

            def click_btn_achievement(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_achievement)

            def click_btn_fishalbum(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_fishalbum)

            def click_btn_flashcard(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_flashcard)

            def click_btn_mail(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_mail)

            def click_btn_announcement(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_announcement)

            def click_btn_changeroom(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_changeroom)

            def click_btn_leaderboard(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_leaderboard)

            def click_btn_avatar(self):
                self.click_element(element_data=ElementsData.BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.btn_avatar)

    class panel_MainStage_daily_prepare(BasePage):
        def click_btn_tournaments(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.btn_tournaments)

        def click_btn_btn_receive(self):
            self.click_element_safe(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.btn_receive)

        def click_outboard_tip(self):
            self.click_element_safe(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.outboard_tip)

        def click_btn_gohome(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.btn_gohome)

    class panel_MainStage_challenge_prepare(BasePage):
        def click_btn_cast(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_MainStage_challenge_prepare.btn_cast)

        def try_go_to_treasure_map(self, spot_id):
            # 没有藏宝图直接返回
            if not BattlePreparePanel.panel_MainStage_challenge_prepare.is_panel_tip_location_active(self):
                return

            # 在藏宝图直接返回
            if BattlePreparePanel.panel_MainStage_challenge_prepare.get_value_cost(self) > 10:
                return
            fishery_id = self.spot_id_to_fishery_id(spot_id=spot_id)
            spot_id_list, is_in_double_week, is_new_plot = self.get_spot_id_list(fishery_id=fishery_id)
            lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id),
                                                             isLimitedFishSpot=True, isInDoubleWeek=is_in_double_week)
            self.lua_console(lua_code)

        def is_panel_tip_location_active(self):
            return self.exist(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.panel_tip_location_newtreasure)

        def get_value_cost(self):
            self.wait_for_appear(element_data=ElementsData.BattlePreparePanel.btn_cast, is_click=False)
            value_cost = self.get_text(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.value_cost)
            return int(value_cost)

        def click_btn_gohome(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_MainStage_daily_prepare.btn_gohome)

    class panel_gears_new(BasePage):
        def is_panel_active(self):
            return self.exist(element_data=ElementsData.BattlePreparePanel.gears)

        def click_btn_cancel(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_gears_new.btn_cancel)

        def click_btn_go(self):
            self.click_element(element_data=ElementsData.BattlePreparePanel.panel_gears_new.btn_go)



    # c = bp.excelTools.get_table_data("POINT_PROGRESS_REWARD.xlsm")["progressRewards"]
    # # c = bp.excelTools.get_table_data("POINT_PROGRESS_REWARD_ENDLESS.xlsm")["progressRewards"]
    # r = 8
    # res = {}
    # cur = 0
    # while cur < len(c):
    #     print(c[cur]["tpId"][r], c[cur]["count"][r])
    #     if c[cur]["isMultiple"][r] != 0:
    #         cur += 1
    #         continue
    #     res = common.resource.make_item_dict(item_dict=res, item_icon_list=[str(c[cur]["tpId"][r])], item_quantity_list=[str(c[cur]["count"][r])])
    #     print(res)
    #     cur += 1
    # print(res)

if __name__ == "__main__":
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21503")
    BattlePreparePanel.panel_MainStage_daily_prepare.click_outboard_tip(bp)
    # BattlePreparePanel.panel_MainStage_challenge_prepare.click_btn_cast(bp)
    bp.connect_close()



