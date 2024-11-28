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


