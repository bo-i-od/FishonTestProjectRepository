from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource
from tools.commonTools import *

class BattlePreparePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePrepare.BattlePreparePanel):
            return True
        return False

    # 点击关闭
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePrepare.btn_close)

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
        self.click_until_disappear(element_data=ElementsData.BattlePrepare.btn_cast)

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
        if self.exist(element_data=ElementsData.BattlePrepare.GlobalProgress.progress_finish):
            return True
        return False

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

    a = BattlePreparePanel.get_energy_list(bp)
    print(a)



