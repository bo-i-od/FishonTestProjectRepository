import random
from tools.commonTools import *
from common.basePage import BasePage
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rechargeEndlessPanel import RechargeEndlessPanel
from configs.elementsData import ElementsData


def click_icon_test(bp: BasePage):
    clickable_icon_list, clickable_position_list = RechargeEndlessPanel.get_clickable_icon_and_position_list(bp, 0)
    # 随机选中一个图标
    r = random.randint(0, len(clickable_icon_list) - 1)
    bp.click_position(clickable_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # 对比物品图标和浮窗物品图标
    compare(item_icon, clickable_icon_list[r])
    bp.click_position([0.5, 0.1])
    if ItemTipsPanel.is_panel_active(bp):
        raise FindElementError
    print("点击图标测试通过")

def buy_test(bp: BasePage, index):
    icon_list, quantity_list = RechargeEndlessPanel.get_select_icon_and_quantity_list(bp, index)
    item_count_list = bp.get_item_count_list(icon_list)
    price = RechargeEndlessPanel.click_btn_buy(bp, index)
    if price != "FREE":
        pass  # 手机加支付和取消支付逻辑
    # if wait_for_pay_result(bp) is False:  # 支付失败
    #     print("1+1礼包，支付失败，跳过测试")
    #     return False
    reward_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    compare_list(reward_icon_list, icon_list)
    cur = 0
    while cur < len(item_count_list):
        quantity_list[cur] += item_count_list[cur]
        cur += 1
    item_count_list = bp.get_item_count_list(icon_list)
    compare(item_count_list, quantity_list)
    RewardsPanel.click_tap_to_claim(bp)
    if RewardsPanel.is_panel_active(bp):
        raise FindElementError
    print("购买测试成功")
    return True

def buy_many_test(bp: BasePage):
    bp.go_to_panel("RechargeEndlessPanel")
    click_icon_test(bp)
    # 随机点击锁定的buy按钮位置
    r = random.randint(1, 3)
    RechargeEndlessPanel.click_btn_buy(bp, r)
    # 若干次购买
    cur = 0
    while cur < 5:
        if buy_test(bp, cur) is False:
            break
        bp.sleep(1)
        cur += 1
    RechargeEndlessPanel.close_RechargeEndlessPanel(bp)
    if RechargeEndlessPanel.is_panel_active(bp):
        raise FindElementError
    print("多次购买测试成功")

if __name__ == '__main__':
    bp = BasePage()
    buy_many_test(bp)


