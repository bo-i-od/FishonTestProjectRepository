from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource

class ProgressRewardsPanel(BasePage):
    # 面板是否存在
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ProgressRewardsPanel.ProgressRewardsPanel)


    # 点击关闭按钮
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ProgressRewardsPanel.btn_close)

    def is_btn_go_active(self):
        return self.exist(element_data=ElementsData.ProgressRewardsPanel.btn_go)

    # 点击跳转按钮
    def click_btn_go(self):
        self.click_element(element_data=ElementsData.ProgressRewardsPanel.btn_go)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.ProgressRewardsPanel.btn_i)

    # 点击领取按钮
    def click_btn_claim(self):
        self.click_element(element_data=ElementsData.ProgressRewardsPanel.btn_claim)

    # 得到大奖图标
    def get_big_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.ProgressRewardsPanel.big_rewards_icon_list)
        return icon_list

    # 得到大奖图标位置
    def get_big_rewards_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.ProgressRewardsPanel.big_rewards_icon_list)
        return position_list

    # 得到进度条分子和分母
    def get_progress(self):
        progress_cur = int(self.get_text(element_data=ElementsData.ProgressRewardsPanel.progress_cur))
        progress_max = int(self.get_text(element_data=ElementsData.ProgressRewardsPanel.progress_max))
        return progress_cur, progress_max

    # 得到下一档奖励的图标
    def get_next_reward_icon(self):
        icon = self.get_icon(element_data=ElementsData.ProgressRewardsPanel.next_reward_icon)
        return icon

    # 得到下一档奖励的图标的位置
    def get_next_reward_position(self):
        position = self.get_position(element_data=ElementsData.ProgressRewardsPanel.next_reward_icon)
        return position

    # 得到下一档奖励的数量
    def get_next_reward_quantity(self):
        quantity = resource.str_to_int(self.get_text(element_data=ElementsData.ProgressRewardsPanel.next_reward_quantity))
        return quantity

    # 得到当前累计奖励的图标列表
    def get_current_rewards_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.ProgressRewardsPanel.current_rewards_icon_list)
        return icon_list

    # 得到当前累计奖励的数量列表
    def get_current_rewards_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.ProgressRewardsPanel.current_rewards_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    def is_progress_finish(self):
        return self.exist(element_data=ElementsData.ProgressRewardsPanel.progress_finish)

if __name__ == '__main__':
    bp = BasePage("b6h65hd64p5pxcyh")
    bp.cmd("setPlayerLayer 5000")