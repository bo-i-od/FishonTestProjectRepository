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

def collect_all_test(bp:BasePage):
    collectable_free_data = BattlePassPanel.get_free_collectable_icon_quantity_and_position_list(bp)
    collectable_premium_data = BattlePassPanel.get_premium_collectable_icon_quantity_and_position_list(bp)
    icon_list, quantity_list, position_list = collectable_free_data
    item_dict = make_item_dict(item_coin_list=icon_list, item_quantity_list=quantity_list)
    icon_list, quantity_list, position_list = collectable_premium_data
    item_dict = make_item_dict(item_coin_list=icon_list, item_quantity_list=quantity_list, item_dict=item_dict)
    stock_icon_list = []
    for item in item_dict:
        stock_icon_list.append(item)
    stock_quantity_list = bp.get_item_count_list(stock_icon_list)
    if not BattlePassPanel.click_btn_collect_all(bp):
        if collectable_free_data[0]:
            raise FindElementError
        if collectable_premium_data[0]:
            raise FindElementError
        print("没有可领取项，collect_all_test测试跳过")
        return
    stock_expect_dict = item_dict.copy()
    stock_expect_dict = make_item_dict(item_coin_list=stock_icon_list, item_quantity_list=stock_quantity_list, item_dict=stock_expect_dict)
    stock_quantity_list = bp.get_item_count_list(stock_icon_list)
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


def swipe_test(bp:BasePage):
    viewport = BattlePassPanel.get_viewport(bp)
    x_0 = bp.get_position(viewport.item_id_list[0])[0]
    point_end = [viewport.viewport_position[0] - viewport.viewport_size[0] * 0.1, viewport.viewport_position[1]]
    bp.swipe(point_start=viewport.viewport_position, point_end=point_end)
    x_1 = bp.get_position(viewport.item_id_list[0])[0]
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
    is_cash_enough = BattlePassBuyLevelPanel.is_cash_enough(bp)
    BattlePassBuyLevelPanel.click_btn_buy(bp)
    if is_cash_enough:
        BattlePassRewardPanel.click_tap_to_continue(bp)
        print("购买成功，buy_level_test正面测试通过")
        return
    BattlePassBuyLevelPanel.click_btn_close(bp)
    print("购买成功，buy_level_test反面测试通过")

def BattlePassBuyLevelPanel_test(bp:BasePage):
    BattlePassPanel.click_btn_buy_levels(bp)
    bp.sleep(0.5)
    change_level_test(bp)
    click_icon_buy_level_test(bp)
    BattlePassBuyLevelPanel.go_to_RechargeStorePanel(bp)
    StorePanel.click_btn_close(bp)
    buy_level_test(bp)

def jump_test(bp:BasePage):
    BattlePassPanel.click_btn_detail(bp)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.sleep(0.5)
    BattlePassPanel.click_btn_task(bp)
    TaskPanel.click_btn_close(bp)
    if not BattlePassPanel.is_panel_active(bp):
        raise FindNoElementError
    BattlePassPanel.click_btn_unlock_premium(bp)
    BattlePassBuyLicensePanel.click_btn_close(bp)
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
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    compare(icon_free_list[r0], item_icon)
    bp.click_position(position_premium_list[r1])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
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

def click_icon_test(bp:BasePage):
    # 获得可点击的信息列表
    viewport = BattlePassPanel.get_viewport(bp)
    clickable_icon_list, clickable_position_list = viewport.get_clickable_icon_and_position_list()
    del clickable_position_list[len(clickable_icon_list) - 1]
    del clickable_position_list[len(clickable_position_list) - 1]
    # 在免费可领取中点击一个
    collectable_data = BattlePassPanel.get_free_collectable_icon_quantity_and_position_list(bp)
    random_collect_test(bp, collectable_data, clickable_position_list)
    # 在付费可领取中点击一个
    collectable_data = BattlePassPanel.get_premium_collectable_icon_quantity_and_position_list(bp)
    random_collect_test(bp, collectable_data, clickable_position_list)
    # 随机点击图标
    r = random.randint(0, len(clickable_position_list) - 1)
    bp.click_position(clickable_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, clickable_icon_list[r])
    bp.click_position([0.5, 0.1])
    # 获得预览图标及位置
    res = BattlePassPanel.get_preview_icon_and_position_list(bp)
    preview_item_icon_list, preview_item_position_list, preview_gear_icon_list, preview_gear_position_list = res
    # 点击图标并对比弹窗图标
    preview_item_position_list_len = len(preview_item_position_list)
    if preview_item_position_list_len > 0:
        r = random.randint(0, len(preview_item_position_list) - 1)
        bp.click_position(preview_item_position_list[r])
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, preview_item_icon_list[r])
        bp.click_position([0.5, 0.1])
    cur = 0
    while cur < len(preview_gear_position_list):
        bp.click_position(preview_gear_position_list[cur])
        BaitAndRodShowPanel.click_tap_to_continue(bp)
        cur += 1


def random_collect_test(bp:BasePage, collectable_data, clickable_position_list):
    collectable_icon_list, collectable_quantity_list, collectable_position_list = collectable_data
    collectable_position_list_len = len(collectable_position_list)
    if collectable_position_list_len > 0:
        r = random.randint(0, collectable_position_list_len - 1)
    if collectable_position_list and collectable_position_list[r] in clickable_position_list:
        item_count = bp.get_item_count(item_icon_name=collectable_icon_list[r])
        item_count_expect = item_count + collectable_quantity_list[r]
        bp.click_position(collectable_position_list[r])
        reward_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
        reward_icon = reward_icon_list[0]
        reward_quantity = RewardsPanel.get_reward_quantity_list(bp)[0]
        item_count = bp.get_item_count(item_icon_name=collectable_icon_list[r])
        RewardsPanel.click_tap_to_claim(bp)
        # 验证图标和数量变化是否正确
        compare(reward_icon, collectable_icon_list[r])
        compare(reward_quantity, collectable_quantity_list[r])
        compare(item_count, item_count_expect)
    print("random_collect_test随机领取测试通过")


def BattlePass_rookie_test(bp:BasePage):
    # HomePanel.go_to_BattlePassPanel(bp)
    bp.go_to_panel("BattlePassPanel")
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
    swipe_test(bp)
    jump_test(bp)
    if not BattlePassRewardPanel_completed:
        BattlePassPanel.click_btn_close(bp)
        # HomePanel.go_to_BattlePassPanel(bp)
        bp.go_to_panel("BattlePassPanel")
        if BattlePassRewardPanel.is_panel_active(bp):
            BattlePassRewardPanel_test(bp)
        if BattlePassPopPanel.is_panel_active(bp):
            BattlePassPopPanel_test(bp)

    BattlePassPanel.click_btn_buy_levels(bp)
    buy_level_test(bp)
    buy_premium_test(bp, 0)
    click_icon_test(bp)
    BattlePassPanel.click_btn_close(bp)
    print("BattlePass_rookie_test新手号的通行证测试通过")

def BattlePass_veteran_test(bp:BasePage):
    # HomePanel.go_to_BattlePassPanel(bp)
    bp.go_to_panel("BattlePassPanel")
    bp.set_item_count(target_count=10000,item_tpid="100100")
    bp.sleep(1)
    if BattlePassIntroPanel.is_panel_active(bp):
        BattlePassIntroPanel.close_battlePassIntroPanel(bp, is_test=False)
    elif BattlePassRewardPanel.is_panel_active(bp):
        BattlePassRewardPanel.click_tap_to_continue(bp)
    if BattlePassPopPanel.is_panel_active(bp):
        BattlePassPopPanel.click_btn_close(bp)
    buy_premium_test(bp, 1)
    bp.sleep(0.5)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(0.5)
    BattlePassBuyLevelPanel_test(bp)
    glod_bank_test(bp)
    collect_all_test(bp)
    BattlePassPanel.click_btn_close(bp)
    bp.sleep(0.5)
    RodMoreToOnePanel_test(bp)
    print("BattlePass_rookie_test老号的通行证测试通过")

def BattlePass_test(bp:BasePage):
    # HomePanel.go_to_BattlePassPanel(bp)
    bp.go_to_panel("BattlePassPanel")
    if BattlePassIntroPanel.is_panel_active(bp):
        BattlePassIntroPanel.close_battlePassIntroPanel(bp, is_test=False)
    elif BattlePassRewardPanel.is_panel_active(bp):
        BattlePassRewardPanel.click_tap_to_continue(bp)
    if BattlePassPopPanel.is_panel_active(bp):
        BattlePassPopPanel.click_btn_close(bp)
    buy_premium_test(bp, 1)
    RewardsPanel.click_tap_to_claim(bp)
    BattlePassBuyLevelPanel_test(bp)
    glod_bank_test(bp)
    collect_all_test(bp)
    BattlePassPanel.click_btn_close(bp)
    RodMoreToOnePanel_test(bp)
def glod_bank_test(bp:BasePage):
    BattlePassPanel.click_btn_i_gold_band(bp)
    if not BattlePassPanel.is_Tip_goldbank_active(bp):
        raise FindNoElementError
    bp.click_position([0.5, 0.1])
    print("glod_bank_test金库测试通过")

def RodMoreToOnePanel_test(bp:BasePage):
    # 随机一个进行预览与确定
    btn_preview_position_list = RodMoreToOnePanel.get_btn_preview_position_list(bp)
    rod_icon_list, rod_position_list = RodMoreToOnePanel.get_rod_icon_and_position_list(bp)
    r = random.randint(0, len(btn_preview_position_list) - 1)
    bp.click_position(btn_preview_position_list[r])
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.click_position(rod_position_list[r])
    RodMoreToOnePanel.click_confirm(bp)
    item_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    compare(gear_icon_list[0], rod_icon_list[r])
    RewardsPanel.click_tap_to_claim(bp)
    RodMoreToOnePanel.click_btn_close(bp)
    if RodMoreToOnePanel.is_panel_active(bp):
        raise FindElementError
    # HomePanel.go_to_BattlePassPanel(bp)
    # BattlePassPanel.click_btn_close(bp)
    # r = random.randint(0, len(btn_preview_position_list) - 1)
    # bp.click_position(rod_position_list[r])
    # RodMoreToOnePanel.click_confirm(bp)
    # item_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    # compare(gear_icon_list[0], rod_icon_list[r])
    print("RodMoreToOnePanel_test鱼竿三选一测试通过")






if __name__ == '__main__':
    bp = BasePage()
    BattlePass_veteran_test(bp)

