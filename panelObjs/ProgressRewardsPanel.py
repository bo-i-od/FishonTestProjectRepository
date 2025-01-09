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


    def click_btn_i(self):
        self.click_element(element_data=ElementsData.ProgressRewardsPanel.btn_i)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.ProgressRewardsPanel.btn_close_tips)

    def click_item_tips(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ProgressRewardsPanel.item_list_tips, index=index)

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ProgressRewardsPanel.item_list, index=index)
    # 点击领取按钮

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


    operation_pool = [
        {"element_data": ElementsData.ProgressRewardsPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.ProgressRewardsPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
        {"element_data": ElementsData.ProgressRewardsPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.ProgressRewardsPanel.item_list, "func": click_item, "weight": 1},
        {"element_data": ElementsData.ProgressRewardsPanel.item_list_tips, "func": click_item_tips, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # ProgressRewardsPanel.click_btn_close(bp)
    # ProgressRewardsPanel.click_btn_i(bp)
    # ProgressRewardsPanel.click_item_tips(bp)
    # ProgressRewardsPanel.click_btn_close_tips(bp)
    ProgressRewardsPanel.click_item(bp)

    bp.connect_close()


if __name__ == '__main__':
    bp = BasePage("b6h65hd64p5pxcyh")
    bp.cmd("setPlayerLayer 5000")