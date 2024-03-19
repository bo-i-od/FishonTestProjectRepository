from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *
from common.viewport import Viewport

class AchievementCategoryPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementCategory.btn_close)
        if AchievementCategoryPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.AchievementCategory.AchievementCategoryPanel):
            return True
        return False

    def get_category_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementCategory.item_list)

    # 图标列表
    def get_reward_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.AchievementCategory.reward_icon_list)

    def get_reward_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementCategory.reward_icon_list)

    # 数量列表
    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.AchievementCategory.reward_quantity_list)
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

    # 获得表数据
    def get_category_table_data(self):
        table_data = self.excelTools.get_table_data("ACHIEVEMENT_CATEGORY.xlsm")
        return table_data

    # 去渔场钓悬赏鱼GGG
    def do_category(self, table_data, index):
        data_list = table_data["fishList"]
        cur = 0
        while cur < len(data_list):
            fishery = str(table_data["fishList"][cur]["source"][index])
            if fishery == "0":
                break
            # 进入指定渔场
            self.go_to_panel("TournamentsPanel")
            TournamentsPanel.go_to_fishery_by_tpid(self, fishery_tpid=fishery)
            fish = str(table_data["fishList"][cur]["fish"][index])
            battleTest.fish_once(self, fishery_id=fishery, fish_id=fish)
            self.go_home()
            cur += 1

    def get_category_viewport(self):
        category_viewport = Viewport(self, element_viewport=ElementsData.AchievementCategory.category_viewport, element_item_list=ElementsData.AchievementCategory.item_list,viewport_direction="column")
        return category_viewport


    def click_btn_rewards(self):
        self.click_element(element_data=ElementsData.AchievementCategory.btn_rewards)