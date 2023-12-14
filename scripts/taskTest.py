import random
from items.resource import *
from panelObjs.taskPanel import TaskPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from tools.viewport import Viewport
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.pvpBattleHUDPanel import PVPBattleHUDPanel
from panelObjs.pvpResultPanel import PVPResultPanel
from panelObjs.pvpHallPanel import PVPHallPanel
from panelObjs.messageBoxPanel import MessageBoxPanel
def click_icon_test(bp:BasePage, viewport:Viewport):
    # 点击可点击范围的随机图标
    clickable_icon_list, clickable_position_list = TaskPanel.get_clickable_icon_and_position_list(bp, viewport)
    r = random.randint(0, len(clickable_icon_list) - 1)
    bp.click_position(clickable_position_list[r])
    # 对照奖励和浮窗的图标
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    # check_icon_list(clickable_icon_list)
    compare(item_icon, clickable_icon_list[r])
    bp.click_position([0.5, 0.1])
    # 点击宝箱 请确保没有可领取的宝箱
    box_status_list, box_position_list = TaskPanel.get_box_status_and_position_list(bp)
    r = random.randint(0, len(box_position_list) - 1)
    bp.click_position(box_position_list[r])
    # 点击宝箱
    award_icon_list = TaskPanel.get_box_award_icon_list(bp)
    award_position_list = TaskPanel.get_box_award_position_list(bp)
    cur = 0
    while not award_icon_list:
        # 防止没点上
        bp.click_position(box_position_list[r])
        award_icon_list = TaskPanel.get_box_award_icon_list(bp)
        award_position_list = TaskPanel.get_box_award_position_list(bp)
        cur += 1
        if cur > 10:
            raise FindNoElementError
    # check_icon_list(award_icon_list)
    # 随机点击一个宝箱奖励的图标并对比浮窗的图标
    r = random.randint(0, len(award_position_list) - 1)
    bp.click_position(award_position_list[r])
    cur = 0
    while not ItemTipsPanel.is_panel_active(bp):
        # 防止没点上
        bp.click_position(award_position_list[r])
        cur += 1
        if cur > 10:
            raise FindNoElementError
    item_icon = ItemTipsPanel.get_item_icon(bp)
    # item_icon = check_icon(item_icon)
    compare(item_icon, award_icon_list[r])
    bp.click_position([0.5, 0.1])

# def swipe_test(task_id_list:list, viewport:Viewport):
#     r = random.randint(0, len(task_id_list) - 1)
#     viewport.move_until_appear(task_id_list[r])
#     print("swipe_test滑动测试通过")

def btn_collect_test(bp:BasePage, task_id_list:list, viewport:Viewport, index:int):
    viewport.move_until_appear(task_id_list[index])
    # 得到按钮状态 并检查是否可领奖
    status_list, position_list = TaskPanel.get_btn_status_and_position_list(bp, task_id_list)
    if status_list[index] != 1:
        print("无法领取，跳过btn_collect_test按钮领取测试")
        return
    # 记录库存道具数量
    reward_dict = TaskPanel.get_award_dict(bp, task_id_list, index)
    stock_expect_dict = reward_dict.copy()
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        stock_expect_dict[stock_icon] += count
    # 记录进度条
    progress_value = TaskPanel.get_progress_value(bp)
    # 点击领取
    bp.click_position(position_list[index])
    # 对比奖励图标和数量
    reward_expect_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(reward_expect_dict, reward_dict)
    # 对比库存和期望库存
    for reward_icon in reward_expect_dict:
        count = bp.get_item_count(item_icon_name=reward_icon)
        compare(count, stock_expect_dict[reward_icon])
    status_list, position_list = TaskPanel.get_btn_status_and_position_list(bp, task_id_list)
    # 看按钮状态是否改为complete
    compare(status_list[index], 2)
    # 看进度条是否增长
    if progress_value < TaskPanel.get_progress_value(bp) is False:
        raise CompareError
    # 关闭领奖弹窗
    RewardsPanel.click_tap_to_continue(bp)

def box_collect_test(bp:BasePage, index:int, box_award_dict:dict):
    status_list, position_list = TaskPanel.get_box_status_and_position_list(bp)
    if status_list[index] != 1:
        print("无法领取，跳过box_collect_test宝箱领取测试")
        return
    # 计算库存
    stock_expect_dict = box_award_dict.copy()
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        stock_expect_dict[stock_icon] += count
    # 点击宝箱
    bp.click_position(position_list[index])
    cur = 0
    while not RewardsPanel.is_panel_active(bp):
        bp.click_position(position_list[index])
        cur += 1
        if cur > 10:
            raise FindNoElementError
    # 对照奖励
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(box_award_dict, reward_dict)
    # 对照库存
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        compare(count, stock_expect_dict[stock_icon])
    status_list, position_list = TaskPanel.get_box_status_and_position_list(bp)
    if status_list[index] != 2:
        raise FindNoElementError
    # 关闭弹窗
    RewardsPanel.click_tap_to_continue(bp)
    print("box_collect_test宝箱领取测试通过")

def switch_tab_test(bp:BasePage):
    task_kind = TaskPanel.get_task_kind(bp)
    compare(task_kind, "Daily")
    TaskPanel.switch_tab(bp, 1)
    task_kind = TaskPanel.get_task_kind(bp)
    compare(task_kind, "Weekly")
    TaskPanel.switch_tab(bp, 2)
    task_kind = TaskPanel.get_task_kind(bp)
    compare(task_kind, "Monthly")
    print("switch_tab_test切换页签测试通过")

def daily_task_test(bp:BasePage):
    task_id_list = TaskPanel.get_task_id_list(bp)
    viewport = TaskPanel.get_viewport(bp)
    click_icon_test(bp, viewport)
    box_status_list, box_position_list = TaskPanel.get_box_status_and_position_list(bp)
    # 点击箱子查看奖励
    bp.click_position(box_position_list[0])
    box_award_dict = TaskPanel.get_box_award_dict(bp)
    cur = 0
    while not box_award_dict:
        # 防止没点上
        bp.click_position(box_position_list[0])
        box_award_dict = TaskPanel.get_box_award_dict(bp)
        cur += 1
        if cur > 10:
            raise FindNoElementError
    bp.click_position([0.5, 0.1])
    # 点击go 去对决界面
    duel_task_index = TaskPanel.get_duel_task_index(bp)
    viewport.move_until_appear(task_id_list[duel_task_index])
    btn_status_list, btn_position_list = TaskPanel.get_btn_status_and_position_list(bp, task_id_list)
    bp.click_position(btn_position_list[duel_task_index])
    # 加上对决投降的测试
    bp.sleep(2)
    PVPHallPanel.click_btn_play(bp)
    PVPBattleHUDPanel.wait_for_panel_appear(bp)
    PVPBattleHUDPanel.click_btn_give_up(bp)
    MessageBoxPanel.click_btn_cancel(bp)
    PVPBattleHUDPanel.click_btn_give_up(bp)
    MessageBoxPanel.click_btn_confirm(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)
    bp.sleep(0.5)
    PVPHallPanel.click_btn_close(bp)
    bp.sleep(0.5)
    HomePanel.go_to_TaskPanel(bp)
    # 加上对决投降的测试
    index = 0
    btn_collect_test(bp, task_id_list, viewport, index)
    index = 1
    btn_collect_test(bp, task_id_list, viewport, index)
    index = 0
    box_collect_test(bp, index, box_award_dict)


def TaskPanel_test(bp:BasePage):
    HomePanel.go_to_TaskPanel(bp)
    daily_task_test(bp)
    switch_tab_test(bp)
    TaskPanel.click_btn_close(bp)

if __name__ == '__main__':
    bp = BasePage()





