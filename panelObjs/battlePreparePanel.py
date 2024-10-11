import common.resource
from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.rewardsPanel import RewardsPanel
from tools.commonTools import *

class BattlePreparePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePrepare.BattlePreparePanel)

    # 点击关闭
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_close)
        self.sleep(1)
        if not RewardsPanel.is_panel_active(self):
            return
        RewardsPanel.click_tap_to_claim(self)
        self.sleep(1)
        self.click_element(element_data=ElementsData.BattlePrepare.btn_close)
        self.sleep(1)
        if not MessageBoxPanel.is_panel_active(self):
            return
        MessageBoxPanel.click_btn_confirm(self)
        self.sleep(1)
        self.click_element(element_data=ElementsData.BattlePrepare.btn_close)


    def get_rod_position_list(self):
        return self.get_position_list(element_data=ElementsData.BattlePrepare.rod_model_list)


    # 点击抛竿
    def cast(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.btn_cast, is_click=False)
        position = self.get_position(element_data=ElementsData.BattlePrepare.btn_cast)
        while position and (not self.exist(element_data=ElementsData.BuyEnergy.BuyEnergyPanel)):
            self.click_position(position)
            self.sleep(0.2)

    # 点击抛竿
    def click_btn_cast(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.btn_cast, is_click=False)
        self.click_until_disappear(element_data=ElementsData.BattlePrepare.btn_cast, ignore_set={"BattlePreparePanel"})

    # 点击快速换装
    def click_btn_quick_switch(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.quick_switch, is_click=True)

    #
    def click_rod_model(self):
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.rod_model, is_click=True)

    def get_location(self):
        return self.get_text(element_data=ElementsData.BattlePrepare.location)

    def click_btn_apply(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_apply)

    # 得到下一档奖励的图标
    def get_next_reward_icon(self):
        icon = self.get_icon(element_data=ElementsData.BattlePrepare.GlobalProgress.next_reward_icon)
        return icon


    # 得到下一档奖励的数量
    def get_next_reward_quantity(self):
        quantity = resource.str_to_int(self.get_text(element_data=ElementsData.BattlePrepare.GlobalProgress.next_reward_quantity))
        return quantity

    # 得到进度条的值
    def get_progress(self):
        progress_cur = int(self.get_text(element_data=ElementsData.BattlePrepare.GlobalProgress.progress_cur))
        progress_max = int(self.get_text(element_data=ElementsData.BattlePrepare.GlobalProgress.progress_max))
        return progress_cur, progress_max

    # 得到当前累计奖励的图标列表
    def get_current_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.BattlePrepare.GlobalProgress.current_rewards_icon_list)
        return icon_list

    # 得到当前累计奖励的数量列表
    def get_current_rewards_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.BattlePrepare.GlobalProgress.current_rewards_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    # 点击mini板 打开全局进度条面板
    def click_progress_info(self):
        self.click_element(element_data=ElementsData.BattlePrepare.GlobalProgress.progress_info)

    def is_progress_finish(self):
        return self.exist(element_data=ElementsData.BattlePrepare.GlobalProgress.progress_finish)

    def click_progress_finish(self):
        self.click_element(element_data=ElementsData.BattlePrepare.GlobalProgress.progress_finish)

    def click_btn_tournaments(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_tournaments)

    # 得到钓点状态
    def get_location_status(self):
        location_id_list = self.get_object_id_list(element_data=ElementsData.BattlePrepare.location_list)
        treasure_id_list = self.get_object_id_list(element_data=ElementsData.BattlePrepare.treasure_list)
        select_list = []
        selectable_list = []
        cur = 0
        while cur < len(location_id_list):
            select_id_list = self.get_offspring_id_list(object_id=location_id_list[cur], offspring_path="select")
            if select_id_list:
                select_list.append(cur)
                cur += 1
                continue
            selectable_list.append(cur)
            cur += 1
        bias = cur
        cur = 0
        while cur < len(treasure_id_list):
            select_id_list = self.get_offspring_id_list(object_id=treasure_id_list[cur], offspring_path="select")
            if select_id_list:
                select_list.append(cur + bias)
                cur += 1
                continue
            selectable_list.append(cur + bias)
            cur += 1
        return select_list, selectable_list

    def get_location_position_list(self):
        location_position_list = self.get_position_list(element_data=ElementsData.BattlePrepare.location_list)

        location_position_list += self.get_position_list(element_data=ElementsData.BattlePrepare.treasure_list)
        return location_position_list


    def get_energy_list(self):
        location_energy_list = self.get_text_list(element_data=ElementsData.BattlePrepare.location_energy_list)
        str_to_int_list(location_energy_list)
        treasure_energy_list = self.get_text_list(element_data=ElementsData.BattlePrepare.treasure_energy_list)
        str_to_int_list(treasure_energy_list)
        return location_energy_list + treasure_energy_list

    def click_btn_add_100500(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_add_100500)

    def click_btn_location(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_location)

    def click_btn_collection(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_collection)

    def click_gears(self):
        self.click_element(element_data=ElementsData.BattlePrepare.gears)

    def click_panel_tip_location_newtreasure(self):
        self.click_element(element_data=ElementsData.BattlePrepare.panel_tip_location_newtreasure)

    def is_panel_tip_location_active(self):
        return self.exist(element_data=ElementsData.BattlePrepare.panel_tip_location_newtreasure)

    def click_btn_icon_warning(self):
        self.click_element(element_data=ElementsData.BattlePrepare.PanelPrepareWarning.btn_icon)

    def get_value_cost(self):
        value_cost = self.get_text(element_data=ElementsData.BattlePrepare.value_cost)
        return int(value_cost)

    class Minitask(BasePage):
        def click_btn_recommend(self):
            self.click_element(element_data=ElementsData.BattlePrepare.Minitask.btn_recommend)

        def click_btn_go(self):
            self.click_element(element_data=ElementsData.BattlePrepare.Minitask.btn_go)

        def click_btn_gift(self):
            self.click_element(element_data=ElementsData.BattlePrepare.Minitask.btn_gift)

        def get_progress(self):
            progress = self.get_text(element_data=ElementsData.BattlePrepare.Minitask.progress)
            res = progress.split("/")
            numerator = int(res[0])
            denominator = int(res[1])
            return numerator, denominator

        def click_btn_claim(self):
            self.click_element(element_data=ElementsData.BattlePrepare.Minitask.btn_claim)

        def get_text_task(self):
            return self.get_text(element_data=ElementsData.BattlePrepare.Minitask.text_task)

        def click_btn_collection(self):
            self.click_element(element_data=ElementsData.BattlePrepare.btn_collection)



if __name__ == '__main__':
    bp = BasePage()

    a = BattlePreparePanel.get_current_rewards_icon_list(bp)
    b= BattlePreparePanel.get_current_rewards_quantity_list(bp)
    c = common.resource.make_item_dict(item_icon_list=a, item_quantity_list=b)
    print(c)
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



