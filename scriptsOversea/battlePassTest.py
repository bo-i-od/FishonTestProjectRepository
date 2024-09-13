import random

from common import gameInit
from panelObjs.battlePassPanel import BattlePassPanel
from panelObjs.battlePassBuyLevelPanel import BattlePassBuyLevelPanel
from panelObjs.homePanel import HomePanel
from panelObjs.battlePassRewardPanel import BattlePassRewardPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.battlePassPopPanel import BattlePassPopPanel
from panelObjs.battlePassBuyLicensePanel import BattlePassBuyLicensePanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.taskPanel import TaskPanel
from panelObjs.battlePassIntroPanel import BattlePassIntroPanel
from panelObjs.storePanel import StorePanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.rodMoreToOnePanel import RodMoreToOnePanel
from common.resource import *
from common.basePage import BasePage
from common.viewport import Viewport


def click_icon_buy_level_test(bp:BasePage):
    # 购买等级页面点击图标
    res = BattlePassBuyLevelPanel.get_clickable_icon_and_position_list(bp)
    icon_free_list, position_free_list, icon_premium_list, position_premium_list = res
    # 随机点击免费的图标
    r = random.randint(0, len(icon_free_list) - 1)
    bp.click_position(position_free_list[r])
    bp.sleep(1)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    compare(item_icon, icon_free_list[r])
    bp.click_position([0.5, 0.9])
    # 随机点击付费的图标
    r = random.randint(0, len(icon_premium_list) - 1)
    bp.click_position(position_premium_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    compare(item_icon, icon_premium_list[r])
    bp.click_position([0.5, 0.9])
    gear_position = BattlePassBuyLevelPanel.get_gear_position(bp)
    if gear_position is None:
        return
    bp.click_position(gear_position)
    BaitAndRodShowPanel.click_tap_to_continue(bp)


def change_level_test(bp:BasePage):
    # 购买等级测试
    # 滑到最小
    slider = BattlePassBuyLevelPanel.get_slider(bp)
    bp.swipe(point_start=[slider.slider_range[0] + slider.slider_size[0] * 0.2, slider.slider_position[1]], point_end=[slider.slider_range[0] - slider.slider_size[0] * 0.2, slider.slider_position[1]])
    buy_level_0, new_level_0 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    # 点击-号
    BattlePassBuyLevelPanel.click_sub_level(bp)
    # 检查数值
    buy_level_1, new_level_1 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    if buy_level_0 > 1:
        new_level_0 -= 1
    compare(new_level_0, new_level_1)
    bp.sleep(1)

    # 滑到最大
    bp.swipe(point_start=[slider.slider_range[1] - slider.slider_size[0] * 0.2, slider.slider_position[1]], point_end=[slider.slider_range[1] + slider.slider_size[0] * 0.2, slider.slider_position[1]])
    buy_level_0, new_level_0 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    # 点击+号
    BattlePassBuyLevelPanel.click_add_level(bp)
    # 检查数值
    buy_level_1, new_level_1 = BattlePassBuyLevelPanel.get_buy_level_and_new_level(bp)
    if new_level_0 < 60:
        new_level_0 += 1
    compare(new_level_0, new_level_1)


def buy_level_test(bp:BasePage):
    cost = BattlePassBuyLevelPanel.get_cost(bp)
    cash_expect = BattlePassBuyLevelPanel.get_cash(bp)
    BattlePassBuyLevelPanel.click_btn_buy(bp)
    bp.sleep(1)
    if RewardsPanel.is_panel_active(bp):
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(1)
    # 钻石不足情况下验证数值
    if cost > cash_expect:
        cash = BattlePassBuyLevelPanel.get_cash(bp)
        compare(cash_expect, cash)
        BattlePassBuyLevelPanel.click_btn_close(bp)
        return
    # 钻石充足情况下验证数值
    cash_expect = cash_expect - cost
    cash = BattlePassBuyLevelPanel.get_cash(bp)
    compare(cash_expect, cash)
    BattlePassRewardPanel.click_tap_to_continue(bp)


# 购买等级页面的测试
def BattlePassBuyLevelPanel_test(bp:BasePage):
    BattlePassPanel.click_btn_buy_levels(bp)
    bp.sleep(1)
    change_level_test(bp)
    click_icon_buy_level_test(bp)
    BattlePassBuyLevelPanel.go_to_RechargeStorePanel(bp)
    bp.sleep(1)
    StorePanel.click_btn_close(bp)
    bp.sleep(1)
    buy_level_test(bp)


# 通行证界面往其它界面的跳转测试
def jump_test(bp:BasePage):
    BattlePassPanel.click_btn_detail(bp)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.sleep(1)
    BattlePassPanel.click_btn_task(bp)
    bp.sleep(1)
    TaskPanel.click_btn_close(bp)
    bp.sleep(1)
    if not BattlePassPanel.is_panel_active(bp):
        raise FindNoElementError
    BattlePassPanel.click_btn_unlock_premium(bp)
    bp.sleep(1)
    BattlePassBuyLicensePanel.click_btn_close(bp)
    bp.sleep(1)
    BattlePassPanel.click_btn_i(bp)
    BattlePassIntroPanel.close_battlePassIntroPanel(bp)


def buy_premium_test(bp:BasePage):
    # 买付费通行证
    r = random.randint(0, 1)
    BattlePassPanel.click_btn_get_premium(bp)
    bp.sleep(1)

    # 获得价格信息
    cost_icon_list = BattlePassBuyLicensePanel.get_cost_icon_list(bp)
    cost_quantity_list = BattlePassBuyLicensePanel.get_cost_quantity_list(bp)
    cost_icon = cost_icon_list[r]
    cost_quantity = cost_quantity_list[r]
    cost_expect = bp.get_item_count(item_icon_name=cost_icon) - cost_quantity

    # 随机点一个
    btn_buy_list = BattlePassBuyLicensePanel.get_btn_buy_list(bp)
    bp.click_position(btn_buy_list[r])

    BattlePassBuyLicensePanel.wait_for_pay_result(bp)
    bp.sleep(1)

    # 对比点券数量变化
    cost = bp.get_item_count(item_icon_name=cost_icon)
    compare(cost_expect, cost)
    # if r == 1:
    #     RewardsPanel.wait_for_panel_appear(bp)
    #     bp.sleep(1)
    #     RewardsPanel.click_tap_to_claim(bp)


def BattlePassRewardPanel_test(bp:BasePage):
    # 随机选择图标
    res = BattlePassRewardPanel.get_clickable_icon_and_position_list(bp)
    icon_free_list, position_free_list, icon_premium_list, position_premium_list = res
    r0 = random.randint(0,len(icon_free_list) - 1)
    r1 = random.randint(0,len(icon_premium_list) - 1)
    # 点击并对照图标
    bp.click_position(position_free_list[r0])
    bp.sleep(1)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon_free_list[r0], item_icon)
    bp.click_position(position_premium_list[r1])
    bp.sleep(1)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon_premium_list[r1], item_icon)
    # 关闭页面
    BattlePassRewardPanel.click_tap_to_continue(bp)
    if BattlePassRewardPanel.is_panel_active(bp):
        raise FindElementError


def BattlePassPopPanel_test(bp:BasePage):
    # bp倒计时七日弹窗
    if not BattlePassPopPanel.is_panel_active(bp):
        return
    bp.sleep(1)
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
    # 获取可领取列表
    collectable_list = status[1]
    collectable_list_len = len(collectable_list)
    if not collectable_list_len > 0:
        return

    # 随机选择一个进行领取
    r = random.randint(collectable_list_len - 10, collectable_list_len - 1)
    icon_selected = icon_list[collectable_list[r]]
    icon_selected_id = viewport.item_id_list[collectable_list[r]]
    item_count = bp.get_item_count(item_icon_name=icon_selected)
    item_count_expect = item_count + quantity_list[collectable_list[r]]
    viewport.move_until_appear(icon_selected_id)
    bp.sleep(1)
    icon_position = BattlePassPanel.get_collectable_icon_position(bp, icon_selected_id)
    bp.click_position(icon_position)
    RewardsPanel.wait_for_panel_appear(bp)
    reward_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    reward_icon = reward_icon_list[0]
    reward_quantity = RewardsPanel.get_reward_quantity_list(bp)[0]
    item_count = bp.get_item_count(item_icon_name=icon_selected)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)
    # 验证图标和数量变化是否正确
    compare(reward_icon, icon_list[collectable_list[r]])
    compare(reward_quantity, quantity_list[collectable_list[r]])
    compare(item_count, item_count_expect)
    bp.click_position(icon_position)
    bp.sleep(1)
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(icon_selected, item_icon)
        bp.click_position([0.5, 0.9])
    if BaitAndRodShowPanel.is_panel_active(bp):
        BaitAndRodShowPanel.click_tap_to_continue(bp)
    collected = status[1].pop(r)
    status[2].append(collected)


def collect_all_test(bp: BasePage, icon_list, quantity_list):
    item_dict = make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
    stock_icon_list = []
    for item in item_dict:
        stock_icon_list.append(item)
    stock_quantity_list = bp.get_item_count_list(item_icon_name_list=stock_icon_list)
    if not BattlePassPanel.click_btn_collect_all(bp):
        if icon_list:
            raise FindElementError
        return
    stock_expect_dict = item_dict.copy()
    stock_expect_dict = make_item_dict(item_icon_list=stock_icon_list, item_quantity_list=stock_quantity_list, item_dict=stock_expect_dict)
    stock_quantity_list = bp.get_item_count_list(item_icon_name_list=stock_icon_list)
    stock_dict = make_item_dict(item_icon_list=stock_icon_list, item_quantity_list=stock_quantity_list)
    compare(stock_dict, stock_expect_dict)
    reward_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    reward_quantity_list = RewardsPanel.get_reward_quantity_list(bp)
    compare(len(reward_quantity_list), len(item_dict))
    cur = 0
    while cur < len(reward_quantity_list):
        compare(reward_quantity_list[cur], item_dict[reward_icon_list[cur]])
        cur += 1
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)




def glod_bank_test(bp:BasePage):
    BattlePassPanel.click_btn_i_gold_band(bp)
    if not BattlePassPanel.is_Tip_goldbank_active(bp):
        raise FindNoElementError
    bp.click_position([0.5, 0.9])


def RodMoreToOnePanel_test(bp:BasePage):
    cur = 0
    while not RodMoreToOnePanel.is_panel_active(bp):
        bp.clear_popup_once()
        bp.sleep(1)
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
    bp.sleep(1)
    item_icon_list, gear_icon_list = RewardsPanel.get_reward_icon_list(bp)
    compare(gear_icon_list[0], rod_icon_list[r])
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    if not bp.is_pay:
        return
    RodMoreToOnePanel.click_btn_close(bp)
    bp.sleep(1)
    if RodMoreToOnePanel.is_panel_active(bp):
        raise FindElementError


def main(bp:BasePage):
    # 登录到大厅
    cmd_list = ["guideskip", "levelupto 56", "add 1 101900 10000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)
    # # 关闭升级弹窗
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 进入BP界面
    bp.go_to_panel("BattlePassPanel")

    # 一系列的弹窗
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

    # 跳转相关测试
    jump_test(bp)

    # 关闭弹窗
    if not BattlePassRewardPanel_completed:
        BattlePassPanel.click_btn_close(bp)
        bp.go_to_panel("BattlePassPanel")
        bp.sleep(1)
        if BattlePassRewardPanel.is_panel_active(bp):
            bp.sleep(1)
            BattlePassRewardPanel_test(bp)
            bp.sleep(1)
        if BattlePassPopPanel.is_panel_active(bp):
            bp.sleep(1)
            BattlePassPopPanel_test(bp)
    bp.sleep(1)

    # 绿钞不足购买等级
    BattlePassPanel.click_btn_buy_levels(bp)
    buy_level_test(bp)

    # 购买通行证
    buy_premium_test(bp)

    # 绿钞足购买等级
    bp.set_item_count(target_count=10000, item_tpid="100100")
    BattlePassBuyLevelPanel_test(bp)
    bp.sleep(1)

    # 黄金银行测试
    glod_bank_test(bp)
    bp.sleep(1)

    # 领取测试
    collect_test(bp)
    bp.sleep(1)

    # 关闭界面
    BattlePassPanel.click_btn_close(bp)

    # 鱼竿包三选一
    RodMoreToOnePanel_test(bp)



if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533", is_mobile_device=False)
    main(bp)
    bp.connect_close()

