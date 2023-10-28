from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from panelObjs.rewardsPanel import RewardsPanel

def wait_for_pay_result(bp: BasePage):
    while True:
        if bp.exist(element_data=ElementsData.FlashTips.FlashTipsPanel):
            return False
        if RewardsPanel.is_panel_active(bp):
            return True
        bp.sleep(0.1)
