from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource

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
        self.wait_for_appear(element_data=ElementsData.BattlePrepare.btn_cast, is_click=True)

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



if __name__ == '__main__':
    bp = BasePage()
    BattlePreparePanel.click_btn_cast(bp)



