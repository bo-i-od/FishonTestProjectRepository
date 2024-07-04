from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.achievementPanel import AchievementPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *

class AchievementWantedPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AchievementWanted.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.AchievementWanted.AchievementWantedPanel):
            return True
        return False

    # 悬赏图位置
    def get_wanted_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementWanted.item_list)

    # 图标列表
    def get_reward_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.AchievementWanted.reward_icon_list)

    def get_reward_position_list(self):
        return self.get_position_list(element_data=ElementsData.AchievementWanted.reward_icon_list)

    # 数量列表
    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.AchievementWanted.reward_quantity_list)
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

    # 获得表数据
    def get_achievement_wanted_table_data(self):
        table_data = self.excelTools.get_table_data("ACHIEVEMENT_WANTED.xlsm")
        return table_data

    # 去渔场钓悬赏鱼
    def do_wanted(self, table_data, index):
        # 进入指定渔场
        fishery = str(table_data["fishery"][index])
        self.go_to_panel("TournamentsPanel")
        TournamentsPanel.go_to_fishery_by_tpid(self, fishery_tpid=fishery)


        target_list = table_data["target"]
        cur = 0
        while cur < len(target_list):
            target = str(target_list[cur][index])
            battleTest.fish_once(self, fishery_id=fishery, fish_id=target)
            cur += 1

    def click_btn_rewards(self):
        self.click_element(element_data=ElementsData.AchievementWanted.btn_rewards)

    def guide(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.NewbieGuide.NBG_fishphoto_2, element_data_b=ElementsData.NewbieGuide.NBG_fishphoto_3)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_fishphoto_3)
        self.sleep(1)
        AchievementWantedPanel.click_btn_close(self)
        self.sleep(1)
        AchievementPanel.click_btn_close(self)


if __name__ == '__main__':
    bp = BasePage("192.168.111.78:20009")
    a = AchievementWantedPanel.get_achievement_wanted_table_data(bp)
    print(a)

