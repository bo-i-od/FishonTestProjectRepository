from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource
from common.viewport import Viewport
from tools.commonTools import *

class NewbieTaskPanel(BasePage):
    # 面板是否存在
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.NewbieTaskPanel.NewbieTaskPanel)

    # 点击关闭按钮
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.NewbieTaskPanel.btn_close)

    def get_remain_day(self):
        remain_time = self.get_text(element_data=ElementsData.NewbieTaskPanel.remain_time)
        return int(remain_time.split('D')[0])

    # 关闭tips
    def click_tap_to_close(self):
        self.click_element(element_data=ElementsData.NewbieTaskPanel.tap_to_close)

    # 点击派对促销
    def click_btn_sale(self):
        self.click_element(element_data=ElementsData.NewbieTaskPanel.btn_sale)

    # 点击排行榜
    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.NewbieTaskPanel.btn_leaderboard)

    # 得到3天活动代币数量
    def get_coin(self):
        coin = resource.str_to_int(self.get_text(element_data=ElementsData.NewbieTaskPanel.coin))
        item_count = self.get_item_count(item_tpid="209012")
        compare(coin, item_count)
        return coin

    def get_progress_reward_viewport(self, progress_reward_id_list):
        size = self.get_size(object_id=progress_reward_id_list[0])
        progress_reward_viewport = Viewport(self, element_viewport=ElementsData.NewbieTaskPanel.viewport_progress, item_id_list=progress_reward_id_list, viewport_edge=[0, 2 * size[0]])
        return progress_reward_viewport

    def get_progress_reward_position_list(self, progress_reward_id_list):
        position_list = self.get_position_list(object_id_list=progress_reward_id_list, offspring_path="item>item_model_mini(Clone)>icon")
        position_list = merge_list(position_list)
        progress_reward_position_list = []
        cur = 0
        while cur < len(position_list):
            if not position_list[cur]:
                cur += 1
                continue
            progress_reward_position_list.append(position_list[cur])
            cur += 1
        return progress_reward_position_list

    # 得到进度条奖励图标
    def get_progress_reward_icon_list(self, progress_reward_id_list):
        icon_list = self.get_icon_list(object_id_list=progress_reward_id_list, offspring_path="item>item_model_mini(Clone)>icon")
        icon_list = merge_list(icon_list)
        return icon_list


    # 得到进度条奖励数量
    def get_progress_reward_quantity_list(self, progress_reward_id_list):
        quantity_list = self.get_text_list(object_id_list=progress_reward_id_list, offspring_path="item>item_model_mini(Clone)>quantity>value")
        quantity_list = merge_list(quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    # 得到进度条奖励领取状态
    def get_progress_reward_status(self):
        locked_list = []
        collectable_list = []
        collected_list = []
        progress_reward_item_id_list = self.get_object_id_list(element_data=ElementsData.NewbieTaskPanel.reward_list_progress, offspring_path="item")
        progress_reward_id_list = self.get_parent_id_list(object_id_list=progress_reward_item_id_list)
        progress_reward_id_list = merge_list(progress_reward_id_list)
        coin = NewbieTaskPanel.get_coin(self)
        cur = 0
        while cur < len(progress_reward_id_list):
            coin_threshold = int(self.get_text(object_id=progress_reward_id_list[cur], offspring_path="value"))
            collectable_id_list = self.get_offspring_id_list(object_id=progress_reward_id_list[cur], offspring_path="btn")
            if collectable_id_list:
                if coin_threshold > coin:
                    raise CompareError
                collectable_list.append(progress_reward_id_list[cur])
                cur += 1
                continue
            collected_id_list = self.get_offspring_id_list(object_id=progress_reward_id_list[cur], offspring_path="item>item_model_mini(Clone)>collected")
            if collected_id_list:
                if coin_threshold > coin:
                    raise CompareError
                collected_list.append(progress_reward_id_list[cur])
                cur += 1
                continue
            if coin_threshold <= coin:
                raise CompareError
            locked_list.append(progress_reward_id_list[cur])
            cur += 1
        return locked_list, collectable_list, collected_list

    def get_max_reward_icon(self):
        max_reward_icon = self.get_icon(element_data=ElementsData.NewbieTaskPanel.reward_max, offspring_path="item>item_model_mini(Clone)>icon")
        return max_reward_icon

    def get_max_reward_position(self):
        max_reward_position = self.get_position(element_data=ElementsData.NewbieTaskPanel.reward_max,
                                                offspring_path="item>item_model_mini(Clone)>icon")
        return max_reward_position

    def get_max_reward_quantity(self):
        max_reward_quantity = int(self.get_text(element_data=ElementsData.NewbieTaskPanel.reward_max, offspring_path="item>item_model_mini(Clone)>quantity>value"))
        return max_reward_quantity

    def get_max_reward_threshold(self):
        max_reward_threshold = int(self.get_text(element_data=ElementsData.NewbieTaskPanel.reward_max, offspring_path="value"))
        return max_reward_threshold

    # 切换页签
    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieTaskPanel.tab_list, index=index)

    def get_task_viewport(self, task_id_list):
        size = self.get_size_list(object_id=task_id_list[0])[0]
        task_viewport = Viewport(self, element_viewport=ElementsData.NewbieTaskPanel.task_viewport, item_id_list=task_id_list, viewport_direction="column", viewport_edge=[0, 2 * size[1]])
        return task_viewport

    # 得到任务的instance id
    def get_task_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.NewbieTaskPanel.task_list)

    # 得到每个任务对应的图标及其数量的字典
    def get_task_reward_dict_list(self, task_id_list):
        reward_dict_list = []
        for task_id in task_id_list:
            icon_list = self.get_icon_list(object_id=task_id, offspring_path="rewards>>icon")
            quantity_list = self.get_text_list(object_id=task_id, offspring_path="rewards>>quantity>value")
            resource.str_to_int_list(quantity_list)
            item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
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
                go_list.append(task_id_list[cur])
                cur += 1
                continue
            btn_collect_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="list_right>btn_collect")
            if btn_collect_id_list:
                collect_list.append(task_id_list[cur])
                cur += 1
                continue
            btn_lock_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="list_right>btn_lock")
            if btn_lock_id_list:
                lock_list.append(task_id_list[cur])
                cur += 1
                continue
            completed_id_list = self.get_offspring_id_list(object_id=task_id_list[cur], offspring_path="completed")
            if completed_id_list:
                completed_list.append(task_id_list[cur])
                cur += 1
                continue
        return lock_list, go_list, collect_list, completed_list

    # 得到按钮位置
    def get_task_position_list(self, task_id_list):
        position_list = self.get_position_list(object_id_list=task_id_list, offspring_path="list_right")
        position_list = merge_list(position_list)
        task_position_list = []
        cur = 0
        while cur < len(position_list):
            if not position_list[cur]:
                cur += 1
                continue
            task_position_list.append(position_list[cur])
            cur += 1
        return task_position_list

    # 得到挑战的instance id
    def get_challenge_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.NewbieTaskPanel.challenge_list)

    def get_challenge_viewport(self, challenge_id_list):
        size = self.get_size_list(object_id=challenge_id_list[0])[0]
        challenge_viewport = Viewport(self, element_viewport=ElementsData.NewbieTaskPanel.challenge_viewport, item_id_list=challenge_id_list, viewport_direction="column", viewport_edge=[0, 0.75 * size[1]])
        return challenge_viewport

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
        challenge_position_list = []
        cur = 0
        while cur < len(challenge_id_list):
            position_list = self.get_position_list(object_id=challenge_id_list[cur], offspring_path="fish_info>right")
            if position_list:
                challenge_position_list.append(position_list[0])
                cur += 1
                continue
            position_list = self.get_position_list(object_id=challenge_id_list[cur], offspring_path="no_records>btn_go")
            if position_list:
                challenge_position_list.append(position_list[0])
                cur += 1
                continue

        return challenge_position_list

    def click_btn_task(self, index=-1):
        size = self.get_size_list(element_data=ElementsData.NewbieTaskPanel.task_list)[0]
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieTaskPanel.btn_task_list, element_viewport=ElementsData.NewbieTaskPanel.task_viewport, viewport_direction="column", viewport_edge=[0, 2 * size[1]], index=index)

    def click_btn_collect(self, index=-1):
        size = self.get_size_list(element_data=ElementsData.NewbieTaskPanel.challenge_list)[0]
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieTaskPanel.btn_collect_list, element_viewport=ElementsData.NewbieTaskPanel.challenge_viewport, viewport_direction="column", viewport_edge=[0, 0.75 * size[1]], index=index)

    def click_btn_go(self, index=-1):
        size = self.get_size_list(element_data=ElementsData.NewbieTaskPanel.challenge_list)[0]
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieTaskPanel.btn_go_list, element_viewport=ElementsData.NewbieTaskPanel.challenge_viewport, viewport_direction="column", viewport_edge=[0, 0.75 * size[1]], index=index)

    def click_item_progress(self, index=-1):
        size = self.get_size_list(element_data=ElementsData.NewbieTaskPanel.item_list_progress)[0]
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieTaskPanel.item_list_progress, element_viewport=ElementsData.NewbieTaskPanel.viewport_progress, viewport_edge=[0, 2 * size[0]],index=index)

    def click_item_max(self):
        self.click_element(element_data=ElementsData.NewbieTaskPanel.item_max)

    def click_item(self, index=-1):
        size = self.get_size_list(element_data=ElementsData.NewbieTaskPanel.task_list)[0]
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieTaskPanel.item_list, element_viewport=ElementsData.NewbieTaskPanel.task_viewport, viewport_direction="column", viewport_edge=[0, 2 * size[1]], index=index)


    operation_pool = [
        {"element_data": ElementsData.NewbieTaskPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.btn_collect_list, "func": click_btn_collect, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.btn_go_list, "func": click_btn_go, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.btn_leaderboard, "func": click_btn_leaderboard, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.btn_sale, "func": click_btn_sale, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.btn_task_list, "func": click_btn_task, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.item_list, "func": click_item, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.item_max, "func": click_item_max, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.item_list_progress, "func": click_item_progress, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.tap_to_close, "func": click_tap_to_close, "weight": 1},
        {"element_data": ElementsData.NewbieTaskPanel.tab_list, "func": switch_tab, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # NewbieTaskPanel.click_btn_close(bp)
    # NewbieTaskPanel.click_btn_collect(bp)
    # NewbieTaskPanel.click_btn_go(bp)
    # NewbieTaskPanel.click_btn_leaderboard(bp)
    # NewbieTaskPanel.click_btn_sale(bp)
    # NewbieTaskPanel.click_btn_task(bp)
    # NewbieTaskPanel.click_item(bp)
    NewbieTaskPanel.click_item_max(bp)
    # NewbieTaskPanel.click_item_progress(bp, 4)
    # NewbieTaskPanel.click_tap_to_close(bp)
    # NewbieTaskPanel.get_challenge_id_list(bp)
    # NewbieTaskPanel.get_challenge_point_list(bp)
    # NewbieTaskPanel.get_challenge_position_list(bp)
    # NewbieTaskPanel.get_challenge_viewport(bp)
    # NewbieTaskPanel.get_coin(bp)
    # NewbieTaskPanel.get_max_reward_icon(bp)
    # NewbieTaskPanel.get_max_reward_position(bp)
    # NewbieTaskPanel.get_max_reward_quantity(bp)
    # NewbieTaskPanel.get_max_reward_threshold(bp)
    # NewbieTaskPanel.get_progress_reward_icon_list(bp)
    # NewbieTaskPanel.get_progress_reward_position_list(bp)
    # NewbieTaskPanel.get_progress_reward_quantity_list(bp)
    # NewbieTaskPanel.get_progress_reward_status(bp)
    # NewbieTaskPanel.get_progress_reward_viewport(bp)
    # NewbieTaskPanel.get_remain_day(bp)
    # NewbieTaskPanel.get_task_id_list(bp)
    # NewbieTaskPanel.get_task_position_list(bp)
    # NewbieTaskPanel.get_task_reward_dict_list(bp)
    # NewbieTaskPanel.get_task_status(bp)
    # NewbieTaskPanel.get_task_viewport(bp)
    # NewbieTaskPanel.is_panel_active(bp)
    # NewbieTaskPanel.switch_tab(bp)
    bp.connect_close()

