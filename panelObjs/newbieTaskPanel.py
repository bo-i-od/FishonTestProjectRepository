from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource

class NewbieTaskPanel(BasePage):
    # 面板是否存在
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.NewbieTask.NewbieTaskPanel):
            return True
        return False

    # 点击关闭按钮
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.NewbieTask.btn_close)

    # 点击左上角问号弹出tips
    def click_btn_i(self):
        self.click_element(element_data=ElementsData.NewbieTask.btn_i)

    # 关闭tips
    def click_tap_to_close(self):
        self.click_element(element_data=ElementsData.NewbieTask.tap_to_close)

    # 点击派对促销
    def click_btn_sale(self):
        self.click_element(element_data=ElementsData.NewbieTask.btn_sale)

    # 点击排行榜
    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.NewbieTask.btn_leaderboard)

    # 得到3天活动代币数量
    def get_coin(self):
        coin = resource.str_to_int(self.get_text(element_data=ElementsData.NewbieTask.coin))
        return coin

    # 得到进度条奖励图标
    def get_common_reward_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.NewbieTask.common_reward_list, offspring_path="item>item_model_mini(Clone)>icon")
        return icon_list

    # 得到进度条奖励数量
    def get_common_reward_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.NewbieTask.common_reward_list, offspring_path="item>item_model_mini(Clone)>quantity>value")
        resource.str_to_int_list(quantity_list)
        return quantity_list

    # 得到进度条奖励领取状态
    def get_common_reward_status(self):
        locked_list = []
        collectable_list = []
        collected_list = []
        common_reward_item_id_list = self.get_object_id_list(element_data=ElementsData.NewbieTask.common_reward_list, offspring_path="item")
        common_reward_id_list = self.get_parent_id_list(object_id_list=common_reward_item_id_list)
        cur = 0
        while cur < len(common_reward_id_list):
            collectable_id_list = self.get_offspring_id_list(object_id=common_reward_id_list[cur], offspring_path="btn")
            if collectable_id_list:
                collectable_list.append(cur)
                cur += 1
                continue
            collected_id_list = self.get_offspring_id_list(object_id=common_reward_id_list[cur], offspring_path="item>item_model_mini(Clone)>collected")
            if collected_id_list:
                collected_list.append(cur)
                cur += 1
                continue
            locked_list.append(cur)
            cur += 1
        return locked_list, collectable_list, collected_list

    # 切换页签
    def switch_tab(self, index):
        position_list = self.get_position_list(element_data=ElementsData.NewbieTask.tab_list)
        position = position_list[index]
        self.click_position(position)

    # 得到任务的instance id
    def get_task_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.NewbieTask.task_list)

    # 得到每个任务对应的图标及其数量的字典
    def get_task_reward_dict_list(self, task_id_list):
        reward_dict_list = []
        for task_id in task_id_list:
            icon_list = self.get_icon_list(object_id=task_id, offspring_path="rewards>>icon")
            quantity_list = self.get_text_list(object_id=task_id, offspring_path="rewards>>quantity>value")
            resource.str_to_int_list(quantity_list)
            item_dict = resource.make_item_dict(item_coin_list=icon_list, item_quantity_list=quantity_list)
            reward_dict_list.append(item_dict)
        return reward_dict_list

    # 得到任务领取状态
    def get_task_status(self, task_id_list):
        go_list = []
        lock_list = []
        collect_list = []
        completed_list = []
        cur = 0
        while cur < len(task_id_list):
            btn_go_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="list_right>btn_go")
            if btn_go_id_list:
                go_list.append(cur)
                cur += 1
                continue
            btn_collect_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="list_right>btn_collect")
            if btn_collect_id_list:
                collect_list.append(cur)
                cur += 1
                continue
            btn_lock_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="list_right>btn_lock")
            if btn_lock_id_list:
                lock_list.append(cur)
                cur += 1
                continue
            completed_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="completed")
            if completed_id_list:
                completed_list.append(cur)
                cur += 1
                continue
        return lock_list, go_list, collect_list, completed_list

    # 得到按钮位置
    def get_task_position_list(self, task_id_list):
        position_list = self.get_position_list(object_id_list=task_id_list, offspring_path="list_right")
        return position_list

    # 得到挑战的instance id
    def get_challenge_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.NewbieTask.challenge_list)

    # 得到分数 go转换为0分
    def get_challenge_point_list(self, challenge_id_list):
        point_list = []
        cur = 0
        while cur < len(challenge_id_list):
            btn_collect_text_list = self.get_text_list(object_id=challenge_id_list[cur], offspring_path="fish_info>right>btn_collect>text")
            if btn_collect_text_list:
                point = int(btn_collect_text_list[0][1:])
                point_list.append(point)
                cur += 1
                continue
            point_list.append(0)
            cur += 1
        return point_list

    # 得到按钮位置
    def get_challenge_position_list(self, challenge_id_list):
        position_list = self.get_position_list(object_id_list=challenge_id_list, offspring_path="fish_info>right")
        return position_list







if __name__ == '__main__':
    bp = BasePage()
    challenge_id_list = NewbieTaskPanel.get_challenge_id_list(bp)
    a = NewbieTaskPanel.get_challenge_point_list(bp, challenge_id_list)
    print(a)
    b = NewbieTaskPanel.get_challenge_position_list(bp, challenge_id_list)
    print(b)

