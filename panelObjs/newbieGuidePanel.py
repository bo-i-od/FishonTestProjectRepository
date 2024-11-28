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
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.NewbieGuide.NewbieGuidePanel)

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
                        ElementsData.NewbieGuide.NBG_system_get_reward_TreasureChest_01,
                        ElementsData.BaitAndRodShow.BaitAndRodShowPanel]
        self.click_a_until_b_appear_list(perform_list)
        BaitAndRodShowPanel.click_tap_to_continue(self)
        self.click_until_disappear(ElementsData.TreasureChestRewards.btn_close)
        TreasureChestPanel.click_btn_close(self)

    def guide_album(self):
        perform_list = [ElementsData.NewbieGuide.NBG_album_01, ElementsData.NewbieGuide.NBG_album_02, ElementsData.NewbieGuide.NBG_album_03,ElementsData.Home.HomePanel]
        self.click_a_until_b_appear_list(perform_list=perform_list)

    def guide_aquarium(self):
        perform_list = [ElementsData.NewbieGuide.NBG_aquarium_2_1, ElementsData.NewbieGuide.NBG_aquarium_2_2,
                        ElementsData.NewbieGuide.NBG_aquarium_2_3, ElementsData.NewbieGuide.NBG_aquarium_2_4,
                        ElementsData.NewbieGuide.NBG_aquarium_2_5, ElementsData.NewbieGuide.NBG_aquarium_2_6,
                        ElementsData.NewbieGuide.NBG_aquarium_2_7, ElementsData.NewbieGuide.NBG_aquarium_3_1,
                        ElementsData.NewbieGuide.NBG_aquarium_3_2, ElementsData.NewbieGuide.NBG_aquarium_3_3,
                        ElementsData.NewbieGuide.NBG_aquarium_3_4, ElementsData.NewbieGuide.NBG_aquarium_3_5]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_aquarium_3_5)

    def guide_fish_card(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.NewbieGuide.NBG_fishcard_1, element_data_b=ElementsData.NewbieGuide.NBG_fishcard_2)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_fishcard_2)
        self.sleep(1)
        self.clear_popup()
        perform_list = [ElementsData.NewbieGuide.NBG_fishcard_5, ElementsData.NewbieGuide.NBG_fishcard_3,
                        ElementsData.NewbieGuide.NBG_fishcard_4]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_fishcard_4)

    def guide_club(self):
        perform_list = [ElementsData.NewbieGuide.NBG_system_click_Club, ElementsData.NewbieGuide.NBG_system_club_apply]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_system_club_apply)

    def guide_hook(self):
        perform_list = [ElementsData.NewbieGuide.NBG_hook_1, ElementsData.NewbieGuide.NBG_hook_2, ElementsData.NewbieGuide.NBG_hook_3, ElementsData.NewbieGuide.NBG_hook_5]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(ElementsData.NewbieGuide.NBG_hook_5)

    def guide_fish_photo(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.NewbieGuide.NBG_fishphoto_2, element_data_b=ElementsData.NewbieGuide.NBG_fishphoto_3)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_fishphoto_3)
        self.sleep(1)
        AchievementWantedPanel.click_btn_close(self)
        # self.sleep(1)
        # AchievementPanel.click_btn_close(self)

    def guide_fishing_fail(self):
        perform_list = [ElementsData.NewbieGuide.NBG_fishing_fail_0, ElementsData.NewbieGuide.NBG_fishing_fail_1,
                        ElementsData.NewbieGuide.NBG_fishing_fail_2, ElementsData.NewbieGuide.NBG_fishing_fail_3,
                        ElementsData.NewbieGuide.NBG_fishing_fail_4, ElementsData.NewbieGuide.NBG_fishing_fail_5,
                        ElementsData.NewbieGuide.NBG_fishing_fail_6, ElementsData.NewbieGuide.NBG_fishing_fail_7]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_fishing_fail_7)
        self.sleep(1)
        GearLevelupPanel.click_btn_close(self)
        self.sleep(1)
        GearPanel.click_btn_close(self)
        self.sleep(1)
        BattlePreparePanel.click_btn_apply(self)

    def guide_multi_room(self):
        perform_list = [ElementsData.NewbieGuide.NBG_multiRoom_0, ElementsData.NewbieGuide.NBG_multiRoom_1,
                        ElementsData.NewbieGuide.NBG_multiRoom_2, ElementsData.PVEMultiRoomFriend.PVEMultiRoomFriendPanel]
        self.click_a_until_b_appear_list(perform_list)
        PVEMultiRoomFriendPanel.click_btn_close(self)

    def guide_friend_duel(self):
        perform_list = [ElementsData.NewbieGuide.NBG_multiRoom_0, ElementsData.NewbieGuide.NBG_multiRoom_1,
                        ElementsData.NewbieGuide.NBG_multiRoom_2, ElementsData.PVEMultiRoomFriend.PVEMultiRoomFriendPanel]
        self.click_a_until_b_appear_list(perform_list)
