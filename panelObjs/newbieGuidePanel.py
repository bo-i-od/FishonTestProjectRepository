from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.achievementWantedPanel import AchievementWantedPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.gearLevelupPanel import GearLevelupPanel
from panelObjs.gearPanel import GearPanel
from panelObjs.pveMultiRoomFriendPanel import PVEMultiRoomFriendPanel
from tools.commonTools import *
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.treasureChestPanel import TreasureChestPanel
from threading import Thread
from panelObjs.battlePanel import BattlePanel


class NewbieGuidePanel(BasePage):
    guide_perform_dict = {
        "guide_album": [
            ElementsData.NewbieGuide.NBG_prepare_2_album_01, ElementsData.NewbieGuide.NBG_prepare_2_album_02,
            ElementsData.NewbieGuide.NBG_prepare_2_album_03, ElementsData.NewbieGuide.NBG_album_01,
            ElementsData.NewbieGuide.NBG_album_02, ElementsData.NewbieGuide.NBG_album_03,
            ElementsData.NewbieGuide.NBG_prepare_weak_01
        ],
        "guide_aquarium_1": [
            ElementsData.NewbieGuide.NBG_aquarium_new_1_1, ElementsData.NewbieGuide.NBG_aquarium_new_1_2,
            ElementsData.NewbieGuide.NBG_aquarium_new_1_3
        ],
        "guide_aquarium_2": [
            ElementsData.NewbieGuide.NBG_aquarium_new_2_1, ElementsData.NewbieGuide.NBG_aquarium_new_2_2,
            ElementsData.NewbieGuide.NBG_aquarium_new_2_3, ElementsData.NewbieGuide.NBG_aquarium_new_2_4,
            ElementsData.NewbieGuide.NBG_aquarium_new_2_5, ElementsData.NewbieGuide.NBG_aquarium_new_3_1,
            ElementsData.NewbieGuide.NBG_aquarium_new_3_2, ElementsData.NewbieGuide.NBG_aquarium_new_3_3,
            ElementsData.NewbieGuide.NBG_aquarium_new_3_4, ElementsData.NewbieGuide.NBG_aquarium_new_4_1,
            ElementsData.NewbieGuide.NBG_aquarium_new_4_2, ElementsData.NewbieGuide.NBG_aquarium_new_4_3,
            ElementsData.NewbieGuide.NBG_aquarium_new_4_4, ElementsData.NewbieGuide.NBG_aquarium_new_4_5,
            ElementsData.NewbieGuide.NBG_aquarium_new_4_6
        ],
        "guide_fish_card": [
            ElementsData.NewbieGuide.NBG_fishcard_1, ElementsData.NewbieGuide.NBG_fishcard_2,
            ElementsData.NewbieGuide.NBG_fishcard_5, ElementsData.NewbieGuide.NBG_fishcard_3,
            ElementsData.NewbieGuide.NBG_fishcard_4
        ],
        "guide_club": [
            ElementsData.NewbieGuide.NBG_system_click_Club, ElementsData.NewbieGuide.NBG_system_club_apply
        ],
        "guide_hook": [
            ElementsData.NewbieGuide.NBG_hook_1, ElementsData.NewbieGuide.NBG_hook_2,
            ElementsData.NewbieGuide.NBG_hook_3, ElementsData.NewbieGuide.NBG_hook_5
        ],
        "guide_fish_photo": [
            ElementsData.NewbieGuide.NBG_fishphoto_2, ElementsData.NewbieGuide.NBG_fishphoto_3
        ],
        "guide_fishing_fail": [
            ElementsData.NewbieGuide.NBG_fishing_fail_0, ElementsData.NewbieGuide.NBG_fishing_fail_1,
            ElementsData.NewbieGuide.NBG_fishing_fail_2, ElementsData.NewbieGuide.NBG_fishing_fail_3,
            ElementsData.NewbieGuide.NBG_fishing_fail_4, ElementsData.NewbieGuide.NBG_fishing_fail_5,
            ElementsData.NewbieGuide.NBG_fishing_fail_6, ElementsData.NewbieGuide.NBG_fishing_fail_7
        ],
        "guide_multi_room": [
            ElementsData.NewbieGuide.NBG_multiRoom_0, ElementsData.NewbieGuide.NBG_multiRoom_1,
            ElementsData.NewbieGuide.NBG_multiRoom_2
        ],
        "guide_friend_duel": [
            ElementsData.NewbieGuide.NBG_friend_duel_1_1
        ],
        "guide_fishing_cast": [
            ElementsData.NewbieGuide.NBG_fishingcast_1, ElementsData.NewbieGuide.NBG_fishingcast_2
        ],
        "guide_fish_point": [
            ElementsData.NewbieGuide.NBG_fishpoint_1, ElementsData.NewbieGuide.NBG_fishpoint_2,
            ElementsData.NewbieGuide.NBG_fishpoint_3, ElementsData.NewbieGuide.NBG_fishpoint_4,
            ElementsData.NewbieGuide.NBG_fishpoint_5, ElementsData.NewbieGuide.NBG_fishpoint_6,
            ElementsData.NewbieGuide.NBG_fishpoint_7, ElementsData.NewbieGuide.NBG_fishpoint_8
        ]
    }

    def guide_common(self, guide_name):
        perform_list = NewbieGuidePanel.guide_perform_dict[guide_name]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(perform_list[-1])

    @staticmethod
    def get_first_perform_list(guide_list):
        first_perform_list = []
        cur = 0
        while cur < len(guide_list):
            guide = guide_list[cur]
            first_perform_list.append(NewbieGuidePanel.guide_perform_dict[guide][0])
            cur += 1
        return first_perform_list


    def is_panel_active(self):
        return self.exist(element_data=ElementsData.NewbieGuide.NewbieGuidePanel)

    def wait_for_panel_appear(self, timeout=10):
        self.wait_for_appear(element_data=ElementsData.NewbieGuide.NewbieGuidePanel, timeout=timeout)

    def get_start_page(self):
        if self.exist(element_data=ElementsData.NewbieGuide.NewbieGuidePanel_1):
            return 4
        elif self.exist(element_data=ElementsData.NewbieGuide.NewbieGuidePanel_2):
            return 3
        elif self.exist(element_data=ElementsData.NewbieGuide.NewbieGuidePanel_3):
            return 2
        elif self.exist(element_data=ElementsData.NewbieGuide.NewbieGuidePanel_4):
            return 1
        else:
            raise FindNoElementError

    def guide_rookie_1(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_1, ElementsData.NewbieGuide.NBG_rookie_2,
                        ElementsData.NewbieGuide.NBG_rookie_3, ElementsData.NewbieGuide.NBG_rookie_4,
                        ElementsData.NewbieGuide.NBG_rookie_5, ElementsData.NewbieGuide.NBG_rookie_6,
                        ElementsData.NewbieGuide.NBG_rookie_7]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(ElementsData.NewbieGuide.NBG_rookie_7)
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="down")
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_rookie_8)
        self.ray_input(element_data=ElementsData.Battle.btn_reel, target_name="btn_cast", kind="up")
        self.custom_cmd("autofish")

    def guide_rookie_2(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_9,
                        ElementsData.NewbieGuide.NBG_rookie_10]
        self.click_a_until_b_appear_list(perform_list)

    def guide_rookie_3(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_10, ElementsData.NewbieGuide.NBG_rookie_11,
                        ElementsData.NewbieGuide.NBG_rookie_12, ElementsData.NewbieGuide.NBG_rookie_13_1]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_rookie_13_1)
        qteThread = Thread(target=BattlePanel.qte, args=[self])
        qteThread.start()
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_rookie_13_Guide_ULTUp)
        self.custom_cmd("autofish")
        # self.debug_log("NBG_rookie_13_Guide_QTEInfo")
        # self.click_a_until_b_disappear(element_data_a=ElementsData.NewbieGuide.NBG_rookie_13_2, element_data_b=ElementsData.NewbieGuide.NBG_rookie_13_Guide_QTEInfo)
        # self.click_a_until_b_disappear(element_data_a=ElementsData.NewbieGuide.NBG_rookie_13_2, element_data_b=ElementsData.NewbieGuide.NBG_rookie_13_Guide_QTE_left)
        # position_start = self.get_position(element_data=ElementsData.Battle.btn_reel)
        # position_end = [position_start[0], position_start[1] - 0.2]
        # self.swipe(point_start=position_start,point_end=position_end)

    def guide_rookie_4(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_13_Guide_ULTInfoCloseBtn, ElementsData.NewbieGuide.NBG_rookie_14, ElementsData.NewbieGuide.NBG_rookie_15]
        self.click_a_until_b_appear_list(perform_list)

    def guide_rookie_5(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_15, ElementsData.NewbieGuide.NBG_rookie_16,
                        ElementsData.Rookie.btn_close, ElementsData.NewbieGuide.NBG_rookie_18,
                        ElementsData.NewbieGuide.NBG_system_1]
        self.click_a_until_b_appear_list(perform_list)

    def guide_rookie_6(self):
        perform_list = [ElementsData.NewbieGuide.NBG_system_1, ElementsData.NewbieGuide.NBG_system_2,
                        ElementsData.NewbieGuide.NBG_system_click_TreasureChest,
                        ElementsData.NewbieGuide.NBG_system_get_reward_TreasureChest_01]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_system_get_reward_TreasureChest_01)
        self.go_home()

    def guide_album(self):
        pass

    def guide_aquarium(self):
        pass

    def guide_fish_card_1(self):
        pass

    def guide_fish_card_2(self):
        # self.sleep(1)
        # self.clear_popup()
        pass

    def guide_club(self):
        pass

    def guide_hook(self):
        pass

    def guide_fish_photo(self):
        pass
        # self.sleep(1)
        # AchievementWantedPanel.click_btn_close(self)
        # self.sleep(1)
        # AchievementPanel.click_btn_close(self)

    def guide_fishing_fail(self):
        pass
        # self.sleep(1)
        # GearLevelupPanel.click_btn_close(self)
        # self.sleep(1)
        # GearPanel.click_btn_close(self)
        # self.sleep(1)
        # BattlePreparePanel.click_btn_apply(self)

    def guide_multi_room(self):
        pass
        # PVEMultiRoomFriendPanel.click_btn_close(self)

    def guide_friend_duel(self):
        pass

    def guide_fishing_cast(self):
        pass

    def guide_fish_point(self):
        pass
