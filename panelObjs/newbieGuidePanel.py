from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.treasureChestPanel import TreasureChestPanel

class NewbieGuidePanel(BasePage):
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

    def do_guide_1(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_1, ElementsData.NewbieGuide.NBG_rookie_2,
                        ElementsData.NewbieGuide.NBG_rookie_3, ElementsData.NewbieGuide.NBG_rookie_4,
                        ElementsData.NewbieGuide.NBG_rookie_5, ElementsData.NewbieGuide.NBG_rookie_6,
                        ElementsData.NewbieGuide.NBG_rookie_7]
        self.click_a_until_b_appear_list(perform_list)
        self.click_until_disappear(ElementsData.NewbieGuide.NBG_rookie_7)

    def do_guide_2(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_8, ElementsData.NewbieGuide.NBG_rookie_9,
                        ElementsData.NewbieGuide.NBG_rookie_10]
        self.click_a_until_b_appear_list(perform_list)

    def do_guide_3(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_10, ElementsData.NewbieGuide.NBG_rookie_11,
                        ElementsData.NewbieGuide.NBG_rookie_12, ElementsData.NewbieGuide.NBG_rookie_13_1]
        self.click_a_until_b_appear_list(perform_list)
        self.debug_log("NBG_rookie_13_1")
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_rookie_13_1)
        self.debug_log("NBG_rookie_13_Guide_ULTUp")
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_rookie_13_Guide_ULTUp)
        # self.debug_log("NBG_rookie_13_Guide_QTEInfo")
        # self.click_a_until_b_disappear(element_data_a=ElementsData.NewbieGuide.NBG_rookie_13_2, element_data_b=ElementsData.NewbieGuide.NBG_rookie_13_Guide_QTEInfo)
        # self.click_a_until_b_disappear(element_data_a=ElementsData.NewbieGuide.NBG_rookie_13_2, element_data_b=ElementsData.NewbieGuide.NBG_rookie_13_Guide_QTE_left)
        self.debug_log("swipe")
        position_start = self.get_position(element_data=ElementsData.Battle.btn_reel)
        position_end = [position_start[0], position_start[1] - 0.2]
        self.swipe(point_start=position_start,point_end=position_end)
        self.debug_log("NBG_rookie_13_Guide_ULTInfoCloseBtn")
        self.click_a_until_b_appear(element_data_a=ElementsData.NewbieGuide.NBG_rookie_13_2, element_data_b=ElementsData.NewbieGuide.NBG_rookie_13_Guide_ULTInfoCloseBtn)


    def do_guide_4(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.NewbieGuide.NBG_rookie_14,
                                    element_data_b=ElementsData.NewbieGuide.NBG_rookie_15)

    def do_guide_5(self):
        perform_list = [ElementsData.NewbieGuide.NBG_rookie_15, ElementsData.NewbieGuide.NBG_rookie_16,
                        ElementsData.Rookie.btn_close, ElementsData.NewbieGuide.NBG_rookie_18,
                        ElementsData.NewbieGuide.NBG_system_1]
        self.click_a_until_b_appear_list(perform_list)


    def do_guide_6(self):
        perform_list = [ElementsData.NewbieGuide.NBG_system_1, ElementsData.NewbieGuide.NBG_system_2,
                        ElementsData.NewbieGuide.NBG_system_click_TreasureChest,
                        ElementsData.NewbieGuide.NBG_system_get_reward_TreasureChest_01,
                        ElementsData.BaitAndRodShow.BaitAndRodShowPanel]
        self.click_a_until_b_appear_list(perform_list)
        BaitAndRodShowPanel.click_tap_to_continue(self)
        self.click_until_disappear(ElementsData.TreasureChestRewards.btn_close)
        TreasureChestPanel.click_btn_close(self)