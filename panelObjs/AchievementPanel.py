import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport


class AchievementPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AchievementPanel.AchievementPanel)

    def is_unlock_tips_active(self):
        return self.exist(element_data=ElementsData.AchievementPanel.tips_unlock)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.AchievementPanel.btn_i)

    def is_tips_active(self):
        return self.exist(element_data=ElementsData.AchievementPanel.tips)

    def get_achievement_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.AchievementPanel.achievement_icon_list)

    def get_achievement_icon_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.AchievementPanel.achievement_icon_list)

    def click_task_mini(self):
        self.click_element(element_data=ElementsData.AchievementPanel.task_mini_icon)

    def get_task_mini_group_name(self):
        task_mini_icon = self.get_icon(element_data=ElementsData.AchievementPanel.task_mini_icon)
        achievement_icon_list = self.get_icon_list(element_data=ElementsData.AchievementPanel.achievement_icon_list)
        achievement_group_name_list = self.get_text_list(element_data=ElementsData.AchievementPanel.achievement_group_name_list)
        index = -1
        cur = 0
        while cur < len(achievement_icon_list):
            if achievement_icon_list[cur] == task_mini_icon:
                index = cur
                break
            cur += 1
        return achievement_group_name_list[index]

    def get_achievement_status_set(self):
        achievement_id_list = AchievementPanel.get_achievement_id_list(self)
        locked_set = set()
        unlockable_set = set()
        unlocked_set = set()
        cur = 0
        while cur < len(achievement_id_list):
            if self.get_offspring_id_list(offspring_path="particle>loop", object_id=achievement_id_list[cur]):
                unlockable_set.add(cur)
                cur += 1
                continue
            if self.get_offspring_id_list(offspring_path="group_com", object_id=achievement_id_list[cur]):
                unlocked_set.add(cur)
                cur += 1
                continue
            locked_set.add(cur)
            cur += 1
        return [locked_set, unlockable_set, unlocked_set]

    def get_achievement_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.AchievementPanel.achievement_list)

    def get_achievement_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.AchievementPanel.achievement_list)
        return position_list

    def get_viewport(self):
        size = self.get_size_list(element_data=ElementsData.AchievementPanel.achievement_list)[0]
        viewport = Viewport(self, element_viewport=ElementsData.AchievementPanel.viewport, element_item_list=ElementsData.AchievementPanel.achievement_list, viewport_direction="row")
        viewport.viewport_range = [viewport.viewport_range[0], 1]
        edge = [0.01, 0.01]
        viewport.viewport_edge = edge
        viewport.viewport_range_shift()
        return viewport

    def get_group_name(self, achievement_id):
        group_name_id = self.get_offspring_id(offspring_path="group_com>groupbg>groupname", object_id=achievement_id)
        group_name = self.get_text(object_id=group_name_id)
        return group_name

    def switch_tab(self, index=-1):
        position_list = self.get_position_list(element_data=ElementsData.AchievementPanel.tab_list)
        if index < 0:
            index = random.randint(0, len(position_list) - 1)
        self.click_position(position_list[index])

    def click_achievement(self, index=-1):
        viewport = AchievementPanel.get_viewport(self)
        self.click_object_of_plural_objects(element_data=ElementsData.AchievementPanel.achievement_list, index=index, viewport=viewport)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.AchievementPanel.btn_close_tips)

    operation_pool = [
        {"element_data": ElementsData.AchievementPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AchievementPanel.tab_list, "func": switch_tab, "weight": 2},
        {"element_data": ElementsData.AchievementPanel.achievement_list, "func": click_achievement, "weight": 4},
        {"element_data": ElementsData.AchievementPanel.task_mini_icon, "func": click_task_mini, "weight": 2},
        {"element_data": ElementsData.AchievementPanel.btn_i, "func": click_btn_i, "weight": 2},
        {"element_data": ElementsData.AchievementPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 4},
        ]




if __name__ == '__main__':
    bp = BasePage("R5CT22NJ44H")
    # AchievementPanel.click_achievement(bp, index=0)
    AchievementPanel.click_btn_close_tips(bp)
    bp.connect_close()



