import random
from panelObjs.battlePassPanel import BattlePassPanel
from panelObjs.battlePassBuyLevelPanel import BattlePassBuyLevelPanel
from panelObjs.homePanel import HomePanel
from panelObjs.battlePassRewardPanel import BattlePassRewardPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.battlePassPopPanel import BattlePassPopPanel
from panelObjs.battlePassBuyLicensePanel import BattlePassBuyLicensePanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.taskPanel import TaskPanel
from panelObjs.battlePassIntroPanel import BattlePassIntroPanel
from panelObjs.storePanel import StorePanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.rodMoreToOnePanel import RodMoreToOnePanel
from common.resource import *
from common.basePage import BasePage
from common.viewport import Viewport


def swipe_test(bp:BasePage):
    viewport = BattlePassPanel.get_viewport(bp)
    x_0 = bp.get_position(object_id=viewport.item_id_list[0])[0]
    point_end = [viewport.viewport_position[0] - viewport.viewport_size[0] * 0.1, viewport.viewport_position[1]]
    bp.swipe(point_start=viewport.viewport_position, point_end=point_end)
    x_1 = bp.get_position(object_id=viewport.item_id_list[0])[0]
    if x_0 - x_1 < viewport.viewport_size[0] * 0.05:
        raise MoveError
    # point_end = [viewport.viewport_position[0] + viewport.viewport_size[0] * 0.1, viewport.viewport_position[1]]
    # bp.swipe(point_start=viewport.viewport_position, point_end=point_end)
    # x_0 = bp.get_position(viewport.child_id_list[0])[0]
    # if x_0 - x_1 < viewport.viewport_size[0] * 0.05:
    #     raise MoveError
    print("swipe_test滑动测试通过")


def click_icon_buy_level_test(bp:BasePage):
    res = BattlePassBuyLevelPanel.get_clickable_icon_and_position_list(bp)
    icon_free_list, position_free_list, icon_premium_list, position_premium_list = res
    r = random.randint(0, len(icon_free_list) - 1)
    bp.click_position(position_free_list[r])
    bp.sleep(0.2)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    compare(item_icon, icon_free_list[r])
    bp.click_position([0.5, 0.1])
    r = random.randint(0, len(icon_premium_list) - 1)
    bp.click_position(position_premium_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    compare(item_icon, icon_premium_list[r])
    bp.click_position([0.5, 0.1])
    gear_position = BattlePassBuyLevelPanel.get_gear_position(bp)
    if gear_position is None:
        print("click_icon_buy_level_test购买等级页面点击图标测试通过")
        return
    bp.click_position(gear_position)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    print("click_icon_buy_level_test购买等级页面点击图标测试通过")


def change_level_test(bp:BasePage):
    slider = BattlePassBuyLevelPanel.get_slider(bp)
    bp.swipe(point_start=[slider.slider_range[0] + slider.slider_size[0] * 0.1, slider.slider_position[1]], point_end=[slider.slider_range[0] - slider.slider_size[0] * 0.3, slider.slider_position[1]])
    buy_level_0, new_level_0 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    BattlePassBuyLevelPanel.click_sub_level(bp)
    buy_level_1, new_level_1 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    if buy_level_0 > 1:
        new_level_0 -= 1
    compare(new_level_0, new_level_1)
    bp.sleep(0.5)
    bp.swipe(point_start=[slider.slider_range[1] - slider.slider_size[0] * 0.1, slider.slider_position[1]], point_end=[slider.slider_range[1] + slider.slider_size[0] * 0.3, slider.slider_position[1]])
    buy_level_0, new_level_0 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    BattlePassBuyLevelPanel.click_add_level(bp)
    buy_level_1, new_level_1 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    if new_level_0 < 60:
        new_level_0 += 1
    compare(new_level_0, new_level_1)
    print("change_level_test改变购买等级测试通过")


def buy_level_test(bp:BasePage):
    cost = BattlePassBuyLevelPanel.get_cost(bp)
    cash_expect = BattlePassBuyLevelPanel.get_cash(bp)
    BattlePassBuyLevelPanel.click_btn_buy(bp)
    bp.sleep(0.5)
    if cost > cash_expect:
        cash = BattlePassBuyLevelPanel.get_cash(bp)
        compare(cash_expect, cash)
        BattlePassBuyLevelPanel.click_btn_close(bp)
        print("购买失败，buy_level_test反面测试通过")
        return
    cash_expect = cash_expect - cost
    cash = BattlePassBuyLevelPanel.get_cash(bp)
    compare(cash_expect, cash)
    BattlePassRewardPanel.click_tap_to_continue(bp)
    print("购买成功，buy_level_test正面测试通过")


def BattlePassBuyLevelPanel_test(bp:BasePage):
    BattlePassPanel.click_btn_buy_levels(bp)
    bp.sleep(0.5)
    change_level_test(bp)
    click_icon_buy_level_test(bp)
    BattlePassBuyLevelPanel.go_to_RechargeStorePanel(bp)
    bp.sleep(0.5)
    StorePanel.click_btn_close(bp)
    bp.sleep(0.5)
    buy_level_test(bp)

def jump_test(bp:BasePage):
    BattlePassPanel.click_btn_detail(bp)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.sleep(0.5)
    BattlePassPanel.click_btn_task(bp)
    bp.sleep(0.5)
    TaskPanel.click_btn_close(bp)
    bp.sleep(0.5)
    if not BattlePassPanel.is_panel_active(bp):
        raise FindNoElementError
    BattlePassPanel.click_btn_unlock_premium(bp)
    bp.sleep(0.5)
    BattlePassBuyLicensePanel.click_btn_close(bp)
    bp.sleep(0.5)
    BattlePassPanel.click_btn_i(bp)
    BattlePassIntroPanel.close_battlePassIntroPanel(bp)
    print("jump_test跳转测试通过")

def buy_premium_test(bp:BasePage, index):
    BattlePassPanel.click_btn_get_premium(bp)
    bp.sleep(0.5)
    if index == 0:
        BattlePassBuyLicensePanel.click_btn_buy_standard(bp)
    else:
        BattlePassBuyLicensePanel.click_btn_buy_pro(bp)
    BattlePassBuyLicensePanel.wait_for_pay_result(bp)


def BattlePassRewardPanel_test(bp:BasePage):
    # 随机选择图标
    res = BattlePassRewardPanel.get_clickable_icon_and_position_list(bp)
    icon_free_list, position_free_list, icon_premium_list, position_premium_list = res
    r0 = random.randint(0,len(icon_free_list) - 1)
    r1 = random.randint(0,len(icon_premium_list) - 1)
    # 点击并对照图标
    bp.click_position(position_free_list[r0])
    bp.sleep(0.2)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon_free_list[r0], item_icon)
    bp.click_position(position_premium_list[r1])
    bp.sleep(0.2)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon_premium_list[r1], item_icon)
    # 关闭页面
    BattlePassRewardPanel.click_tap_to_continue(bp)
    if BattlePassRewardPanel.is_panel_active(bp):
        raise FindElementError
    print("BattlePassRewardPanel_test测试通过")

def BattlePassPopPanel_test(bp:BasePage):
    if not BattlePassPopPanel.is_panel_active(bp):
        print("bp倒计时七日弹窗未弹出，BattlePassPopPanel_test跳过")
        return
    icon_list, position_list = BattlePassPopPanel.get_clickable_icon_and_position_list(bp)
    r = random.randint(0, len(icon_list) - 1)
    bp.click_position(position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon_list[r], item_icon)
    BattlePassPopPanel.click_get_premium(bp)
    BattlePassBuyLicensePanel.click_btn_close(bp)

def collect_test(bp:BasePage):
    # 获得可点击的信息列表
    viewport_free, viewport_premium = BattlePassPanel.get_viewport(bp)
    free_icon_list = BattlePassPanel.get_free_icon_list(bp)
    premium_icon_list = BattlePassPanel.get_premium_icon_list(bp)
    free_quantity_list = BattlePassPanel.get_free_quantity_list(bp)
    premium_quantity_list = BattlePassPanel.get_premium_quantity_list(bp)
    # 在免费可领取中点击一个
    free_status = BattlePassPanel.get_free_status(bp)
    random_collect_test(bp, free_icon_list, free_quantity_list, free_status, viewport_free)
    # 在付费可领取中点击一个
    premium_status = BattlePassPanel.get_premium_status(bp)
    random_collect_test(bp, premium_icon_list,premium_quantity_list, premium_status, viewport_premium)
    icon_list = []
    quantity_list = []
    cur = 0
    while cur < len(free_status[1]):
        free_icon_index = free_status[1][cur]
        icon_list.append(free_icon_list[free_icon_index])
        quantity_list.append(free_quantity_list[free_icon_index])
        cur += 1
    cur = 0
    while cur < len(premium_status[1]):
        premium_icon_index = premium_status[1][cur]
        icon_list.append(premium_icon_list[premium_icon_index])
        quantity_list.append(premium_quantity_list[premium_icon_index])
        cur += 1
    collect_all_test(bp, icon_list, quantity_list)

def random_collect_test(bp:BasePage, icon_list, quantity_list, status, viewport:Viewport):
    collectable_list = status[1]
    collectable_list_len = len(collectable_list)
    if not collectable_list_len > 0:
        print("没有可领取的奖励，random_collect_test跳过")
        return
    r = random.randint(0, collectable_list_len - 1)
    icon_selected = icon_list[collectable_list[r]]
    icon_selected_id = viewport.item_id_list[collectable_list[r]]
    item_count = bp.get_item_count(item_icon_name=icon_selected)
    item_count_expect = item_count + quantity_list[collectable_list[r]]
    viewport.move_until_appear(icon_selected_id)
    bp.sleep(0.5)
    icon_position = BattlePassPanel.get_collectable_icon_position(bp, icon_selected_id)
    bp.click_position(icon_position)
    bp.sleep(0.2)
    reward_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    reward_icon = reward_icon_list[0]
    reward_quantity = RewardsPanel.get_reward_quantity_list(bp)[0]
    item_count = bp.get_item_count(item_icon_name=icon_selected)
    RewardsPanel.click_tap_to_claim(bp)
    # 验证图标和数量变化是否正确
    compare(reward_icon, icon_list[collectable_list[r]])
    compare(reward_quantity, quantity_list[collectable_list[r]])
    compare(item_count, item_count_expect)
    bp.click_position(icon_position)
    bp.sleep(0.2)
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(icon_selected, item_icon)
        bp.click_position([0.5, 0.1])
    if BaitAndRodShowPanel.is_panel_active(bp):
        BaitAndRodShowPanel.click_tap_to_continue(bp)
    collected = status[1].pop(r)
    status[2].append(collected)
    print("random_collect_test随机领取测试通过")


def collect_all_test(bp: BasePage, icon_list, quantity_list):
    item_dict = make_item_dict(item_coin_list=icon_list, item_quantity_list=quantity_list)
    stock_icon_list = []
    for item in item_dict:
        stock_icon_list.append(item)
    stock_quantity_list = bp.get_item_count_list(item_icon_name_list=stock_icon_list)
    if not BattlePassPanel.click_btn_collect_all(bp):
        if icon_list:
            raise FindElementError
        print("没有可领取项，collect_all_test测试跳过")
        return
    stock_expect_dict = item_dict.copy()
    stock_expect_dict = make_item_dict(item_coin_list=stock_icon_list, item_quantity_list=stock_quantity_list, item_dict=stock_expect_dict)
    stock_quantity_list = bp.get_item_count_list(item_icon_name_list=stock_icon_list)
    stock_dict = make_item_dict(item_coin_list=stock_icon_list, item_quantity_list=stock_quantity_list)
    compare(stock_dict, stock_expect_dict)
    reward_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    reward_quantity_list = RewardsPanel.get_reward_quantity_list(bp)
    compare(len(reward_quantity_list), len(item_dict))
    cur = 0
    while cur < len(reward_quantity_list):
        compare(reward_quantity_list[cur], item_dict[reward_icon_list[cur]])
        cur += 1
    RewardsPanel.click_tap_to_claim(bp)
    print("collect_all_test全部获取测试通过")


def BattlePass_test(bp:BasePage):
    bp.go_to_panel("BattlePassPanel")
    bp.set_item_count(target_count=0,item_tpid="100100")
    BattlePassRewardPanel_completed = False
    bp.sleep(1)
    if BattlePassIntroPanel.is_panel_active(bp):
        BattlePassIntroPanel.close_battlePassIntroPanel(bp, is_test=False)
    elif BattlePassRewardPanel.is_panel_active(bp):
        BattlePassRewardPanel_test(bp)
        BattlePassRewardPanel_completed = True
    if BattlePassPopPanel.is_panel_active(bp):
        BattlePassPopPanel_test(bp)
        BattlePassRewardPanel_completed = True
    # swipe_test(bp)
    jump_test(bp)
    if not BattlePassRewardPanel_completed:
        BattlePassPanel.click_btn_close(bp)
        # HomePanel.go_to_BattlePassPanel(bp)
        bp.go_to_panel("BattlePassPanel")
        bp.sleep(1)
        if BattlePassRewardPanel.is_panel_active(bp):
            bp.sleep(0.5)
            BattlePassRewardPanel_test(bp)
            bp.sleep(1)
        if BattlePassPopPanel.is_panel_active(bp):
            bp.sleep(0.5)
            BattlePassPopPanel_test(bp)
    bp.sleep(0.5)
    BattlePassPanel.click_btn_buy_levels(bp)
    buy_level_test(bp)
    r = random.randint(0, 1)
    buy_premium_test(bp, r)
    bp.sleep(0.5)
    if r == 1:
        RewardsPanel.click_tap_to_claim(bp)
    bp.set_item_count(target_count=10000, item_tpid="100100")
    BattlePassBuyLevelPanel_test(bp)
    bp.sleep(0.5)
    glod_bank_test(bp)
    bp.sleep(0.5)
    collect_test(bp)
    bp.sleep(0.5)
    BattlePassPanel.click_btn_close(bp)
    RodMoreToOnePanel_test(bp)


def glod_bank_test(bp:BasePage):
    BattlePassPanel.click_btn_i_gold_band(bp)
    if not BattlePassPanel.is_Tip_goldbank_active(bp):
        raise FindNoElementError
    bp.click_position([0.5, 0.1])
    print("glod_bank_test金库测试通过")


def RodMoreToOnePanel_test(bp:BasePage):
    cur = 0
    while not RodMoreToOnePanel.is_panel_active(bp):
        bp.sleep(0.5)
        cur += 1
        if cur > 20:
            raise FindNoElementError
    # 随机一个进行预览与确定
    btn_preview_position_list = RodMoreToOnePanel.get_btn_preview_position_list(bp)
    rod_icon_list, rod_position_list = RodMoreToOnePanel.get_rod_icon_and_position_list(bp)
    r = random.randint(0, len(btn_preview_position_list) - 1)
    bp.click_position(btn_preview_position_list[r])
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.click_position(rod_position_list[r])
    RodMoreToOnePanel.click_confirm(bp)
    bp.sleep(0.2)
    item_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    compare(gear_icon_list[0], rod_icon_list[r])
    bp.sleep(0.3)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(0.5)
    RodMoreToOnePanel.click_btn_close(bp)
    if RodMoreToOnePanel.is_panel_active(bp):
        raise FindElementError
    print("RodMoreToOnePanel_test鱼竿三选一测试通过")



if __name__ == '__main__':
    bp = BasePage()
    BattlePass_test(bp)

