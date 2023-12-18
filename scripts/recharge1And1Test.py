import random
from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.homePanel import HomePanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.recharge1And1Panel import Recharge1And1Panel
from panelObjs.rewardsPanel import RewardsPanel
from common.resource import *
from common.pay import wait_for_pay_result
def click_icon_test(bp: BasePage):
    item_position_list = Recharge1And1Panel.get_item_position_list(bp)
    item_icon_list = Recharge1And1Panel.get_item_icon_list(bp)
    r = random.randint(0, 1)
    bp.click_position(item_position_list[r])
    if bp.exist(element_data=ElementsData.BaitAndRodShow.BaitAndRodShowPanel) is False:
        raise FindNoElementError
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    if bp.exist(element_data=ElementsData.Recharge1And1.Recharge1And1Panel) is False:
        raise FindNoElementError
    r = random.randint(2, 3)
    bp.click_position(item_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(icon=item_icon)
    compare(item_icon, item_icon_list[r])
    bp.click_position([0.5, 0.1])
    r = random.randint(4, 7)
    bp.click_position(item_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, item_icon_list[r])
    print("点击图标测试通过")

def buy_test(bp: BasePage):
    HomePanel.go_to(bp, element=ElementsData.Home.btn_1add1)
    if Recharge1And1Panel.is_btn_buy_clickable(bp) is False:
        Recharge1And1Panel.click_btn_buy(bp)
        Recharge1And1Panel.close_Recharge1And1Panel(bp)
        if Recharge1And1Panel.is_panel_active(bp):
            raise FindElementError
        return
    item_icon_list = Recharge1And1Panel.get_item_icon_list(bp)
    Recharge1And1Panel.click_btn_buy(bp)
    # 手机上要加支付逻辑
    if wait_for_pay_result(bp) is False:  # 支付失败
        print("1+1礼包，支付失败，跳过测试")
        return
    # 支付成功
    reward_icon_list = RewardsPanel.get_reward_icon_list(bp, is_divide=False)
    compare_list(item_icon_list, reward_icon_list)
    RewardsPanel.click_tap_to_continue(bp)
    print("1+1礼包，测试通过")


if __name__ == '__main__':
    bp = BasePage()
    buy_test(bp)