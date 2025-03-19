from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.TournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *
from common.viewport import Viewport

class AchievementCategoryPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementCategoryPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AchievementCategoryPanel.AchievementCategoryPanel)


    def get_category_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementCategoryPanel.item_list)

    # 图标列表
    def get_reward_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.AchievementCategoryPanel.reward_icon_list)

    def get_reward_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementCategoryPanel.reward_icon_list)

    # 数量列表
    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.AchievementCategoryPanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    # 看哪些悬赏是表中打开的
    def get_table_open_index_list(self, table_data):
        open_index_list = []
        cur = 0
        while cur < len(table_data["isOpen"]):
            if table_data["isOpen"][cur] != 1:
                cur += 1
                continue
            open_index_list.append(cur)
            cur += 1
        return open_index_list


    # 去渔场钓悬赏鱼GGG
    def do_category(self, table_data, index):
        data_list = table_data["fishList"]
        fishery_pre = None
        cur = 0
        while cur < len(data_list):
            fishery = str(table_data["fishList"][cur]["source"][index])
            if fishery == "0":
                cur += 1
                continue

            # 更换渔场
            if fishery != fishery_pre:
                fishery_pre = fishery
                # 进入指定渔场
                self.go_to_panel("TournamentsPanel")
                TournamentsPanel.go_to_fishery_by_tpid(self, fishery_tpid=fishery)

            fish = str(table_data["fishList"][cur]["fish"][index])
            battleTest.fish_once(self, fish_id=fish, is_quick=True)

            cur += 1

    def get_category_viewport(self):
        size_list = self.get_size_list(element_data=ElementsData.AchievementCategoryPanel.item_list)
        size = [0, 0]
        if size_list:
            size = size_list[0]

        category_viewport = Viewport(self, element_viewport=ElementsData.AchievementCategoryPanel.category_viewport, element_item_list=ElementsData.AchievementCategoryPanel.item_list, viewport_direction="column", viewport_edge=[0, 0.5 * size[1]])
        return category_viewport

    def click_btn_rewards(self):
        self.click_element(element_data=ElementsData.AchievementCategoryPanel.btn_rewards)

    def click_reward_icon(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AchievementCategoryPanel.reward_icon_list, index=index)

    def click_category(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AchievementCategoryPanel.item_list, index=index, element_viewport=ElementsData.AchievementCategoryPanel.category_viewport, viewport_direction="column")

    operation_pool = [
        {"element_data": ElementsData.AchievementCategoryPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AchievementCategoryPanel.reward_icon_list, "func": click_reward_icon, "weight": 2},
        {"element_data": ElementsData.AchievementCategoryPanel.item_list, "func": click_category, "weight": 2},
        ]

if __name__ == '__main__':
    bp = BasePage()

    # AchievementCategoryPanel.click_reward_icon(bp)
    #
    AchievementCategoryPanel.click_category(bp, index=6)

    bp.connect_close()
