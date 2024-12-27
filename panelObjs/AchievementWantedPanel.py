from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.AchievementPanel import AchievementPanel
from panelObjs.BattlePanel import BattlePanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.TournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *

class AchievementWantedPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementWantedPanel.btn_close)


    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AchievementWantedPanel.AchievementWantedPanel)

    # 悬赏图位置
    def get_wanted_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementWantedPanel.item_list)

    # 图标列表
    def get_reward_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.AchievementWantedPanel.reward_icon_list)

    def get_reward_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementWantedPanel.reward_icon_list)

    # 数量列表
    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.AchievementWantedPanel.reward_quantity_list)
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
            if table_data["order"][cur] % 2 == 0:
                cur += 1
                continue
            open_index_list.append(cur)
            cur += 1
        return open_index_list

    # 去渔场钓悬赏鱼
    def do_wanted(self, table_data_object):
        # 进入指定渔场
        fishery = table_data_object["fishery"]
        self.go_to_panel("TournamentsPanel")
        TournamentsPanel.go_to_fishery_by_tpid(self, fishery_tpid=fishery)


        target_list = table_data_object["target"]
        cur = 0
        while cur < len(target_list):
            target = target_list[cur]
            if target == "0" or target == 0:
                cur += 1
                continue
            battleTest.fish_once(self, fishery_id=fishery, fish_id=target, is_quick=True)
            # battleTest.fish_once(self, fishery_id=fishery, fish_id=target, is_quick=False)
            cur += 1

    def click_btn_rewards(self):
        self.click_element(element_data=ElementsData.AchievementWantedPanel.btn_rewards)




if __name__ == '__main__':
    bp = BasePage("192.168.111.78:20009")


