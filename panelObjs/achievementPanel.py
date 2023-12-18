from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport

class AchievementPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Achievement.btn_close)
        if AchievementPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Achievement.AchievementPanel):
            return True
        return False

    def is_unlock_tips_active(self):
        return self.exist(element_data=ElementsData.Achievement.tips_unlock)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.Achievement.btn_i)

    def is_tips_active(self):
        return self.exist(element_data=ElementsData.Achievement.tips)

    def click_task_mini(self):
        self.click_element(element_data=ElementsData.Achievement.task_mini_icon)

    def get_task_mini_group_name(self):
        task_mini_icon = self.get_icon(element_data=ElementsData.Achievement.task_mini_icon)
        achievement_icon_list = self.get_icon_list(element_data=ElementsData.Achievement.achievement_icon_list)
        achievement_group_name_list = self.get_text_list(element_data=ElementsData.Achievement.achievement_group_name_list)
        index = -1
        cur = 0
        while cur < len(achievement_icon_list):
            if achievement_icon_list[cur] == task_mini_icon:
                index = cur
                break
            cur += 1
        return achievement_group_name_list[index]

    def get_achievement_status_set(self):
        achievement_id_list = self.get_object_id_list(element_data=ElementsData.Achievement.achievement_list)
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

    def get_achievement_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.Achievement.achievement_list, offspring_path="particle")
        return position_list

    def get_viewport(self):
        vp = Viewport(self, element_viewport=ElementsData.Achievement.viewport, element_item_list=ElementsData.Achievement.achievement_list)
        return vp

    def get_group_name(self, achievement_id):
        group_name_id = self.get_offspring_id(offspring_path="group_com>groupbg>groupname", object_id=achievement_id)
        group_name = self.get_text(object_id=group_name_id)
        return group_name






if __name__ == '__main__':
    bp = BasePage()
    # locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    # print(locked_set)
    # b = AchievementPanel.get_achievement_position_list(bp)
    # print(b)
    achievement_id_list = bp.get_object_id_list(element_data=ElementsData.Achievement.achievement_list)
    viewport = AchievementPanel.get_viewport(bp)
    viewport.move_until_appear(target_id=achievement_id_list[0])



