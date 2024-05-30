from common.basePage import BasePage
from common.resource import make_item_dict
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *


class ClubApplyPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ClubApply.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ClubApply.ClubApplyPanel)

    def guide(self):
        perform_list = [ElementsData.NewbieGuide.NBG_system_click_Club, ElementsData.NewbieGuide.NBG_system_club_apply]
        self.click_a_until_b_appear_list(perform_list=perform_list)
        self.click_until_disappear(element_data=ElementsData.NewbieGuide.NBG_system_club_apply)
