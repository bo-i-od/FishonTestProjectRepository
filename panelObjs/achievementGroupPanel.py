from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common import resource


class AchievementGroupPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementGroup.btn_close)
        if AchievementGroupPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.AchievementGroup.AchievementGroupPanel):
            return True
        return False

    def get_title(self):
        title = self.get_text(element_data=ElementsData.AchievementGroup.title)
        return title

    def get_item_icon_list(self):
        item_icon_list = self.get_icon_list(element_data=ElementsData.AchievementGroup.item_icon_list)
        return item_icon_list

    def get_item_quantity_list(self):
        item_quantity_list = self.get_text_list(element_data=ElementsData.AchievementGroup.item_quantity_list)
        str_to_int_list(item_quantity_list)
        return item_quantity_list

    def get_item_position_list(self):
        item_position_list = self.get_position_list(element_data=ElementsData.AchievementGroup.item_icon_list)
        return item_position_list

    def get_achievement_point(self):
        progress = self.get_text(element_data=ElementsData.AchievementGroup.progress).split('/')
        progress_numerator = int(progress[0])
        progress_denominator = int(progress[1])
        return progress_numerator, progress_denominator

    def click_btn_collect(self):
        self.click_element(element_data=ElementsData.AchievementGroup.btn_collect)

    def click_btn_go(self):
        self.click_element(element_data=ElementsData.AchievementGroup.btn_go)


    def get_icon_main(self):
        icon_main = self.get_icon(element_data=ElementsData.AchievementGroup.icon_main)
        return icon_main

    def get_achievement_icon_list(self):
        achievement_icon_list = self.get_icon_list(element_data=ElementsData.AchievementGroup.achievement_icon_list)
        return achievement_icon_list

    def get_selected_status_list(self):
        return self.get_toggle_is_on_list(element_data=ElementsData.AchievementGroup.achievement_list)

    def get_achievement_bg_icon_list(self):
        achievement_bg_icon_list = self.get_icon_list(element_data=ElementsData.AchievementGroup.achievement_bg_icon_list)
        return achievement_bg_icon_list

    # 看第几个是选中的
    @staticmethod
    def get_selected_index(selected_status_list):
        cur = 0
        while cur < len(selected_status_list):
            if selected_status_list[cur]:
                break
            cur += 1
        return cur

    def click_box(self):
        self.click_element(element_data=ElementsData.AchievementGroup.box)

    def get_resource_100000(self):
        return resource.get_resource(self, item_tpid="100000", element_data=ElementsData.AchievementGroup.text_100000)

    def get_achievement_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.AchievementGroup.achievement_icon_list)
        return position_list

    def get_status_list(self):
        achievement_bg_icon_list = AchievementGroupPanel.get_achievement_bg_icon_list(bp)
        achievement_id_list = self.get_object_id_list(element_data=ElementsData.AchievementGroup.achievement_list)
        status_list = []
        cur = 0
        while cur < len(achievement_bg_icon_list):
            if "lock" in achievement_bg_icon_list[cur]:
                status_list.append(0)
                cur += 1
                continue
            achievement_collectable_list = self.get_offspring_id_list(offspring_path="tip_reward_bubble>bg>arrow", object_id=achievement_id_list[cur])
            if achievement_collectable_list:
                status_list.append(1)
                cur += 1
                continue
            status_list.append(2)
            cur += 1
        return status_list

    def get_go_collect_and_uncollect_index_list(self):
        achievement_bg_icon_list = AchievementGroupPanel.get_achievement_bg_icon_list(self)
        achievement_id_list = self.get_object_id_list(element_data=ElementsData.AchievementGroup.achievement_list)
        go_index_list = []
        collect_index_list = []
        uncollect_index_list = []
        cur = 0
        while cur < len(achievement_bg_icon_list):
            if "lock" in achievement_bg_icon_list[cur]:
                go_index_list.append(cur)
                cur += 1
                continue
            achievement_collectable_list = self.get_offspring_id_list(offspring_path="tip_reward_bubble>bg>arrow", object_id=achievement_id_list[cur])
            if achievement_collectable_list:
                collect_index_list.append(cur)
                cur += 1
                continue
            uncollect_index_list.append(cur)
            cur += 1
        return go_index_list, collect_index_list, uncollect_index_list







if __name__ == '__main__':
    bp = BasePage()
    a = AchievementGroupPanel.get_status_list(bp)
    print(a)