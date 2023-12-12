import random
from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from panelObjs.homePanel import HomePanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rechargeBlack5Panel import RechargeBlack5Panel
from panelObjs.rewardsPanel import RewardsPanel
from items import resource
from common.pay import wait_for_pay_result
def click_icon_test(bp: BasePage):
    item_position_list = RechargeBlack5Panel.get_item_position_list(bp)
    item_icon_list = RechargeBlack5Panel.get_item_icon_list(bp)
    r = random.randint(0, len(item_position_list) - 1)
    bp.click_position(item_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, item_icon_list[r])
    bp.click_position([0.5, 0.1])
    print("click_icon_test图标点击测试通过")

def buy_test(bp: BasePage):
    RechargeBlack5Panel.click_btn_buy(bp)
    print("buy_test购买测试通过")

def collect_test(bp: BasePage):
    day = 1
    day_icon_list = RechargeBlack5Panel.get_day_icon_list(bp, day)
    day_quantity_list = RechargeBlack5Panel.get_day_quantity_list(bp, day)
    day_dict = resource.make_item_dict(day_icon_list, day_quantity_list)
    item_count_expect_list = bp.get_item_count_list(day_icon_list)
    cur = 0
    while cur < len(day_icon_list):
        item_count_expect_list[cur] += day_quantity_list[cur]
        cur += 1
    RechargeBlack5Panel.click_btn_collect(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    item_count_list = bp.get_item_count_list(day_icon_list)
    print(day_dict,reward_dict)
    compare_dict(day_dict, reward_dict)
    print(item_count_expect_list, item_count_list)
    compare_list(item_count_expect_list, item_count_list)
    RewardsPanel.click_tap_to_continue(bp)
    if RechargeBlack5Panel.is_btn_collect_clickable(bp):
        raise FindElementError
    print("collect_test领取测试通过")

def RechargeBlack5Panel_test(bp:BasePage):
    HomePanel.go_to_RechargeBlack5Panel(bp)
    click_icon_test(bp)
    buy_test(bp)
    collect_test(bp)
    RechargeBlack5Panel.close_Recharge1And1Panel(bp)

if __name__ == '__main__':
    bp = BasePage()
    RechargeBlack5Panel_test(bp)
