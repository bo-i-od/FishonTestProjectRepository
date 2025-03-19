from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.AchievementWantedPanel import AchievementWantedPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.GearLevelupPanel import GearLevelupPanel
from panelObjs.GearPanel import GearPanel
from panelObjs.PVEMultiRoomFriendPanel import PVEMultiRoomFriendPanel
from tools.commonTools import *
from panelObjs.BaitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.TreasureChestPanel import TreasureChestPanel
from threading import Thread
from panelObjs.BattlePanel import BattlePanel


class NewbieGuidePanel(BasePage):
    guide_perform_dict = {
        "guide_album": [
            ElementsData.NewbieGuidePanel.NBG_prepare_2_album_01, ElementsData.NewbieGuidePanel.NBG_prepare_2_album_02,
            ElementsData.NewbieGuidePanel.NBG_prepare_2_album_03, ElementsData.NewbieGuidePanel.NBG_album_01,
            ElementsData.NewbieGuidePanel.NBG_album_02, ElementsData.NewbieGuidePanel.NBG_album_03,
            ElementsData.NewbieGuidePanel.NBG_prepare_weak_01
        ],
        "guide_aquarium_1": [
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_1_1, ElementsData.NewbieGuidePanel.NBG_aquarium_new_1_2,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_1_3
        ],
        "guide_aquarium_2": [
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_2_1, ElementsData.NewbieGuidePanel.NBG_aquarium_new_2_2,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_2_3, ElementsData.NewbieGuidePanel.NBG_aquarium_new_2_4,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_2_5, ElementsData.NewbieGuidePanel.NBG_aquarium_new_3_1,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_3_2, ElementsData.NewbieGuidePanel.NBG_aquarium_new_3_3,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_3_4, ElementsData.NewbieGuidePanel.NBG_aquarium_new_4_1,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_4_2, ElementsData.NewbieGuidePanel.NBG_aquarium_new_4_3,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_4_4, ElementsData.NewbieGuidePanel.NBG_aquarium_new_4_5,
            ElementsData.NewbieGuidePanel.NBG_aquarium_new_4_6
        ],
        "guide_fish_card": [
            ElementsData.NewbieGuidePanel.NBG_fishcard_1, ElementsData.NewbieGuidePanel.NBG_fishcard_2,
            ElementsData.NewbieGuidePanel.NBG_fishcard_5, ElementsData.NewbieGuidePanel.NBG_fishcard_3,
            ElementsData.NewbieGuidePanel.NBG_fishcard_4
        ],
        "guide_club": [
            ElementsData.NewbieGuidePanel.NBG_system_click_Club, ElementsData.NewbieGuidePanel.NBG_system_club_apply
        ],
        "guide_hook": [
            ElementsData.NewbieGuidePanel.NBG_hook_1, ElementsData.NewbieGuidePanel.NBG_hook_2,
            ElementsData.NewbieGuidePanel.NBG_hook_3, ElementsData.NewbieGuidePanel.NBG_hook_5
        ],
        "guide_fish_photo": [
            ElementsData.NewbieGuidePanel.NBG_fishphoto_2, ElementsData.NewbieGuidePanel.NBG_fishphoto_3
        ],
        "guide_fishing_fail": [
            ElementsData.NewbieGuidePanel.NBG_fishing_fail_0, ElementsData.NewbieGuidePanel.NBG_fishing_fail_1,
            ElementsData.NewbieGuidePanel.NBG_fishing_fail_2, ElementsData.NewbieGuidePanel.NBG_fishing_fail_3,
            ElementsData.NewbieGuidePanel.NBG_fishing_fail_4, ElementsData.NewbieGuidePanel.NBG_fishing_fail_5,
            ElementsData.NewbieGuidePanel.NBG_fishing_fail_6, ElementsData.NewbieGuidePanel.NBG_fishing_fail_7
        ],
        "guide_multi_room": [
            ElementsData.NewbieGuidePanel.NBG_multiRoom_0, ElementsData.NewbieGuidePanel.NBG_multiRoom_1,
            ElementsData.NewbieGuidePanel.NBG_multiRoom_2
        ],
        "guide_friend_duel": [
            ElementsData.NewbieGuidePanel.NBG_friend_duel_1_1
        ],
        "guide_fishing_cast": [
            ElementsData.NewbieGuidePanel.NBG_fishingcast_1, ElementsData.NewbieGuidePanel.NBG_fishingcast_2
        ],
        "guide_fish_point": [
            ElementsData.NewbieGuidePanel.NBG_fishpoint_1, ElementsData.NewbieGuidePanel.NBG_fishpoint_2,
            ElementsData.NewbieGuidePanel.NBG_fishpoint_3, ElementsData.NewbieGuidePanel.NBG_fishpoint_4,
            ElementsData.NewbieGuidePanel.NBG_fishpoint_5, ElementsData.NewbieGuidePanel.NBG_fishpoint_6,
            ElementsData.NewbieGuidePanel.NBG_fishpoint_7, ElementsData.NewbieGuidePanel.NBG_fishpoint_8
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
        return self.exist(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel)

    def wait_for_panel_appear(self, timeout=10):
        self.wait_for_appear(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel, timeout=timeout)

    def get_start_page(self):
        if self.exist(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel_1):
            return 4
        elif self.exist(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel_2):
            return 3
        elif self.exist(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel_3):
            return 2
        elif self.exist(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel_4):
            return 1
        else:
            raise FindNoElementError

    def guide_rookie_1(self):
        perform_list = [ElementsData.NewbieGuidePanel.NBG_rookie_1, ElementsData.NewbieGuidePanel.NBG_rookie_2,
                        ElementsData.NewbieGuidePanel.NBG_rookie_3, ElementsData.NewbieGuidePanel.NBG_rookie_4,
                        ElementsData.NewbieGuidePanel.NBG_rookie_5, ElementsData.NewbieGuidePanel.NBG_rookie_6,
                        ElementsData.NewbieGuidePanel.NBG_rookie_7]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(ElementsData.NewbieGuidePanel.NBG_rookie_7)
        self.ray_input(element_data=ElementsData.BattlePanel.btn_reel, kind="down")
        self.click_until_disappear(element_data=ElementsData.NewbieGuidePanel.NBG_rookie_8)
        self.ray_input(element_data=ElementsData.BattlePanel.btn_reel, kind="up")
        self.custom_cmd("autofish")

    def guide_rookie_2(self):
        perform_list = [ElementsData.NewbieGuidePanel.NBG_rookie_9,
                        ElementsData.NewbieGuidePanel.NBG_rookie_10]
        self.click_a_until_b_appear_list(perform_list)

    def guide_rookie_3(self):
        perform_list = [ElementsData.NewbieGuidePanel.NBG_rookie_10, ElementsData.NewbieGuidePanel.NBG_rookie_11,
                        ElementsData.NewbieGuidePanel.NBG_rookie_12, ElementsData.NewbieGuidePanel.NBG_rookie_13_1]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuidePanel.NBG_rookie_13_1)
        qteThread = Thread(target=BattlePanel.qte, args=[self])
        qteThread.start()
        self.click_until_disappear(element_data=ElementsData.NewbieGuidePanel.NBG_rookie_13_Guide_ULTUp)
        self.custom_cmd("autofish")

    def guide_rookie_4(self):
        perform_list = [ElementsData.NewbieGuidePanel.NBG_rookie_13_Guide_ULTInfoCloseBtn, ElementsData.NewbieGuidePanel.NBG_rookie_14, ElementsData.NewbieGuidePanel.NBG_rookie_15]
        self.click_a_until_b_appear_list(perform_list)

    def guide_rookie_5(self):
        perform_list = [ElementsData.NewbieGuidePanel.NBG_rookie_15, ElementsData.NewbieGuidePanel.NBG_rookie_16,
                        ElementsData.RookiePanel.btn_close, ElementsData.NewbieGuidePanel.NBG_rookie_18,
                        ElementsData.NewbieGuidePanel.NBG_system_1]
        self.click_a_until_b_appear_list(perform_list)

    def guide_rookie_6(self):
        perform_list = [ElementsData.NewbieGuidePanel.NBG_system_1, ElementsData.NewbieGuidePanel.NBG_system_2,
                        ElementsData.NewbieGuidePanel.NBG_system_click_Pve,
                        ElementsData.NewbieGuidePanel.NBG_system_click_TreasureChest,
                        ElementsData.NewbieGuidePanel.NBG_system_get_reward_TreasureChest_01]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuidePanel.NBG_system_get_reward_TreasureChest_01)
        self.go_home(target_panel="TournamentsPanel")
        self.click_until_disappear(element_data=ElementsData.NewbieGuidePanel.NBG_system_selectFishery_weakGuide)

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

    def click_NewbieGuidePanel(self):
        self.click_element(element_data=ElementsData.NewbieGuidePanel.NewbieGuidePanel)

    def click_NBG_1(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieGuidePanel.NBG_1)

    def click_NBG_2(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieGuidePanel.NBG_2)

    def click_NBG_3(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieGuidePanel.NBG_3)

    def click_btn_text_051(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieGuidePanel.btn_text_051)

    def click_NBG_multiRoom_1(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieGuidePanel.NBG_multiRoom_1)

    def click_NBG_system_click_Club(self):
        self.click_object_of_plural_objects(element_data=ElementsData.NewbieGuidePanel.NBG_system_click_Club)

    operation_pool = [
        {"element_data": ElementsData.NewbieGuidePanel.NBG_1, "func": click_NBG_1, "weight": 1},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_2, "func": click_NBG_2, "weight": 1},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_3, "func": click_NBG_3, "weight": 1},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_multiRoom_1, "func": click_NBG_multiRoom_1, "weight": 1},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_system_click_Club, "func": click_NBG_system_click_Club, "weight": 1},
        {"element_data": ElementsData.NewbieGuidePanel.NewbieGuidePanel, "func": click_NewbieGuidePanel, "weight": 1},
        {"element_data": ElementsData.NewbieGuidePanel.btn_text_051, "func": click_btn_text_051, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    NewbieGuidePanel.click_NBG_1(bp)
    NewbieGuidePanel.click_NBG_2(bp)
    NewbieGuidePanel.click_NBG_3(bp)
    NewbieGuidePanel.click_NBG_multiRoom_1(bp)
    NewbieGuidePanel.click_NBG_system_click_Club(bp)
    NewbieGuidePanel.click_NewbieGuidePanel(bp)
    NewbieGuidePanel.click_btn_text_051(bp)

    bp.connect_close()