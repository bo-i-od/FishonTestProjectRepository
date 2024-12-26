from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from tools.commonTools import *
from common import resource
from panelObjs.rewardsPreviewPanel import RewardsPreviewPanel


class AchievementGroupPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementGroupPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AchievementGroupPanel.AchievementGroupPanel)


    @staticmethod
    def get_panel_element():
        return ElementsData.AchievementGroupPanel.AchievementGroupPanel

    def get_title(self):
        title = self.get_text(element_data=ElementsData.AchievementGroupPanel.title)
        return title

    def get_item_icon_list(self):
        item_icon_list = self.get_icon_list(element_data=ElementsData.AchievementGroupPanel.item_icon_list)
        return item_icon_list

    def get_item_quantity_list(self):
        item_quantity_list = self.get_text_list(element_data=ElementsData.AchievementGroupPanel.item_quantity_list)
        str_to_int_list(item_quantity_list)
        return item_quantity_list

    def get_item_position_list(self):
        item_position_list = self.get_position_list(element_data=ElementsData.AchievementGroupPanel.item_icon_list)
        return item_position_list

    def get_achievement_point(self):
        progress = self.get_text(element_data=ElementsData.AchievementGroupPanel.progress).split('/')
        progress_numerator = int(progress[0])
        progress_denominator = int(progress[1])
        return progress_numerator, progress_denominator

    def click_btn_collect(self):
        self.click_element(element_data=ElementsData.AchievementGroupPanel.btn_collect)


    def click_btn_go(self):
        self.click_element(element_data=ElementsData.AchievementGroupPanel.btn_go)


    def get_icon_main(self):
        icon_main = self.get_icon(element_data=ElementsData.AchievementGroupPanel.icon_main)
        return icon_main

    def get_achievement_icon_list(self):
        achievement_icon_list = self.get_icon_list(element_data=ElementsData.AchievementGroupPanel.achievement_icon_list)
        return achievement_icon_list

    def get_selected_status_list(self):
        return self.get_toggle_is_on_list(element_data=ElementsData.AchievementGroupPanel.achievement_list)

    def get_achievement_bg_icon_list(self):
        achievement_bg_icon_list = self.get_icon_list(element_data=ElementsData.AchievementGroupPanel.achievement_bg_icon_list)
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

    def click_box_until_not_collectable(self):
        while AchievementGroupPanel.is_box_clickable(self):
            AchievementGroupPanel.click_box(self)
            RewardsPanel.wait_for_panel_appear(self)
            self.sleep(0.5)
            RewardsPanel.click_tap_to_claim(self)
            self.sleep(0.5)
            # 防止鱼卡弹窗
            self.clear_popup_until_appear(element_data=AchievementGroupPanel.get_panel_element())



    def click_box(self):
        self.click_element(element_data=ElementsData.AchievementGroupPanel.box)

    def is_box_clickable(self):
        return self.exist(element_data=ElementsData.AchievementGroupPanel.box_collectable)


    def get_resource_100000(self):
        return resource.get_resource(self, item_tpid="100000", element_data=ElementsData.AchievementGroupPanel.text_100000)

    def get_achievement_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.AchievementGroupPanel.achievement_icon_list)
        return position_list

    def get_status_list(self):
        achievement_bg_icon_list = AchievementGroupPanel.get_achievement_bg_icon_list(bp)
        achievement_id_list = self.get_object_id_list(element_data=ElementsData.AchievementGroupPanel.achievement_list)
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
        achievement_id_list = self.get_object_id_list(element_data=ElementsData.AchievementGroupPanel.achievement_list)
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

    def get_box_reward(self):
        # 点击宝箱
        AchievementGroupPanel.click_box(self)
        cur = 0
        while not RewardsPreviewPanel.is_panel_active(self):
            # 防止没点上
            AchievementGroupPanel.click_box(self)
            cur += 1
            if cur > 10:
                raise FindNoElementError
        reward_icon_list = RewardsPreviewPanel.get_reward_icon_list(self)
        reward_quantity_list = RewardsPreviewPanel.get_reward_quantity_list(self)
        self.click_position([0.5, 0.1])
        return reward_icon_list, reward_quantity_list

    def get_complete(self):
        complete = self.get_text(element_data=ElementsData.AchievementGroupPanel.complete)
        complete = complete.split('>')
        complete_numerator = int(complete[1].split('<')[0])
        complete_denominator = int(complete[2].split('/')[1])
        return complete_numerator, complete_denominator






if __name__ == '__main__':
    bp = BasePage()
    a = bp.click_element(element_data=ElementsData.FlashCardReceivePanel.btn_close)
    # a = AchievementGroupPanel.get_status_list(bp)
    print(a)