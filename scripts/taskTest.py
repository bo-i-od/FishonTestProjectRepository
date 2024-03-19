import random
from common.resource import *
from panelObjs.taskPanel import TaskPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from common.viewport import Viewport
from common.basePage import BasePage
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.loadingPanel import LoadingPanel


def click_icon_test(bp:BasePage,task_id_list:list, viewport:Viewport):
    # 点击可点击范围的随机图标
    task_award_icon_list = TaskPanel.get_task_award_icon_list(bp)
    r = random.randint(0, len(task_id_list) - 1)
    viewport.move_until_appear(task_id_list[r])
    bp.sleep(1)
    task_award_position_list = TaskPanel.get_task_award_position_list(bp)
    r = r * 2 + random.randint(0,1)
    bp.click_position(task_award_position_list[r])
    # 对照奖励和浮窗的图标
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, task_award_icon_list[r])
    bp.click_position([0.5, 0.1])
    # 点击宝箱 请确保没有可领取的宝箱
    box_position_list = TaskPanel.get_box_position_list(bp)
    box_status = TaskPanel.get_box_status(bp)
    uncollectable_list = box_status[0] + box_status[2]
    if not uncollectable_list:
        # img = bp.get_full_screen_shot()
        # bp.save_img(img, "跳过click_icon_test期望状态为箱子全部可领取")
        return
    # 随机点一个不可领奖的箱子
    r = random.randint(0, len(uncollectable_list) - 1)
    position = box_position_list[uncollectable_list[r] - 1]
    TaskPanel.make_award_detail_appear(bp, position=position)
    # 点击宝箱
    award_icon_list = TaskPanel.get_box_award_icon_list(bp)
    award_position_list = TaskPanel.get_box_award_position_list(bp)
    # 随机点击一个宝箱奖励的图标并对比浮窗的图标
    r = random.randint(0, len(award_position_list) - 1)
    position = award_position_list[r]
    TaskPanel.make_ItemTipsPanel_appear(bp, position=position)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, award_icon_list[r])
    bp.click_position([0.5, 0.1])


def jump_once_test(bp:BasePage, task_id_list:list, viewport:Viewport, index:int):
    viewport.move_until_appear(task_id_list[index])
    bp.sleep(1)
    # 得到按钮状态 并检查是否可领奖
    status = TaskPanel.get_btn_status(bp, task_id_list)
    # 不是可领取状态
    if index not in status[0]:
        # img = bp.get_full_screen_shot()
        # bp.save_img(img, "跳过jump_once_test期望状态为任务处于不可跳转状态")
        print("无法领取，跳过jump_once_test按钮领取测试")
        return
    position_list = TaskPanel.get_btn_position_list(bp, task_id_list)
    bp.click_position(position_list[index])
    # 等待跳转后的场景加载
    bp.sleep(0.2)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp)
    # # 跳转到相应界面后截图
    # img = bp.get_full_screen_shot()
    # bp.save_img(img, "task_jump_once_test")
    # 返回任务系统
    bp.go_to_panel("TaskPanel")

def jump_all_test(bp:BasePage, tab_index):
    TaskPanel.switch_tab(bp, tab_index)
    task_id_list = TaskPanel.get_task_id_list(bp)
    viewport = TaskPanel.get_viewport(bp)
    click_icon_test(bp, task_id_list, viewport)
    btn_status = TaskPanel.get_btn_status(bp, task_id_list)
    cur = 0
    while cur < len(btn_status[0]):
        jump_once_test(bp, task_id_list, viewport, btn_status[0][cur])
        TaskPanel.switch_tab(bp, tab_index)
        task_id_list = TaskPanel.get_task_id_list(bp)
        viewport = TaskPanel.get_viewport(bp)
        cur += 1

def jump_test(bp:BasePage):
    bp.go_to_panel("TaskPanel")
    jump_all_test(bp, 0)
    jump_all_test(bp, 1)
    jump_all_test(bp, 2)


# 一个任务页面的领取测试
def collect_all_test(bp:BasePage, task_id_list:list, viewport:Viewport):
    box_status = TaskPanel.get_box_status(bp)
    box_position_list = TaskPanel.get_box_position_list(bp)
    progress_value = TaskPanel.get_progress_value(bp)
    # 将可领取的箱子一领取
    while box_status[1]:
        box_position = box_position_list[box_status[1][0] - 1]
        bp.click_position(box_position)
        box_status[2].append(box_status[1].pop(0))
        box_status_now = TaskPanel.get_box_status(bp)
        compare_list(box_status_now[0], box_status[0])
        compare_list(box_status_now[1], box_status[1])
        compare_list(box_status_now[2], box_status[2])
        RewardsPanel.wait_for_panel_appear(bp)
        bp.sleep(1)
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(0.5)
        if progress_value < 0.99 and progress_value < TaskPanel.get_progress_value(bp) is False:
            raise CompareError
    # 如果没有未领取的箱子就跳过
    if not box_status[0]:
        print("奖励已领取跳过collect_test")
        # img = bp.get_full_screen_shot()
        # bp.save_img(img, "跳过collect_test期望状态为箱子全部领取完毕")
        btn_status = TaskPanel.get_btn_status(bp, task_id_list)
        if not btn_status[1]:
            # img = bp.get_full_screen_shot()
            # bp.save_img(img, "跳过btn_collect_once_test期望状态为任务全部领取完毕")
            return
        while btn_status[1]:
            btn_collect_once_test(bp,task_id_list, viewport, btn_status[1][0])
            btn_status = TaskPanel.get_btn_status(bp, task_id_list)
        # img = bp.get_full_screen_shot()
        # bp.save_img(img, "进行btn_collect_once_test期望状态为任务全部领取完毕")
        return
    # 点击箱子得到下一个箱子的奖励图标和数量
    box_position = box_position_list[box_status[0][0] - 1]
    item_dict = TaskPanel.get_award_detail(bp, position=box_position)
    btn_status = TaskPanel.get_btn_status(bp, task_id_list)
    # 当有可领取的按钮时 循环领取
    while btn_status[1]:
        progress_value = TaskPanel.get_progress_value(bp)
        # 领取一次
        btn_collect_once_test(bp, task_id_list, viewport, btn_status[1][0])
        # 判断进度条是否增长
        if progress_value < 0.99 and progress_value < TaskPanel.get_progress_value(bp) is False:
            raise CompareError
        box_status = TaskPanel.get_box_status(bp)
        btn_status = TaskPanel.get_btn_status(bp, task_id_list)
        # 没有可领取的宝箱就直接下轮循环
        if not box_status[1]:
            continue
        # 领取宝箱查看新宝箱的奖励
        box_collect_test(bp, box_status[1][0] - 1, item_dict)
        if box_status[0]:
            box_position = box_position_list[box_status[0][0] - 1]
            item_dict = TaskPanel.get_award_detail(bp, position=box_position)


# 任务的奖励领取测试
def btn_collect_once_test(bp:BasePage, task_id_list:list, viewport:Viewport, index:int):
    viewport.move_until_appear(task_id_list[index])
    bp.sleep(1)
    # 得到按钮状态 并检查是否可领奖
    status = TaskPanel.get_btn_status(bp, task_id_list)
    # 不是可领取状态
    if index not in status[1]:
        # img = bp.get_full_screen_shot()
        # bp.save_img(img, "跳过collect_once_test期望状态为任务处于不可领取状态")
        print("无法领取，跳过collect_once_test按钮领取测试")
        return
    # 记录库存道具数量
    reward_dict = TaskPanel.get_task_award_dict(bp, task_id_list, index)
    stock_expect_dict = reward_dict.copy()
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        stock_expect_dict[stock_icon] += count
    # 记录进度条
    progress_value = TaskPanel.get_progress_value(bp)
    # 点击领取
    position_list = TaskPanel.get_btn_position_list(bp, task_id_list)
    bp.click_position(position_list[index])
    bp.sleep(0.2)
    # 对比奖励图标和数量
    reward_expect_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(reward_expect_dict, reward_dict)
    # 对比库存和期望库存
    for reward_icon in reward_expect_dict:
        count = bp.get_item_count(item_icon_name=reward_icon)
        compare(count, stock_expect_dict[reward_icon])
    # 看按钮状态是否改为complete
    status = TaskPanel.get_btn_status(bp, task_id_list)
    if index not in status[2]:
        raise FindNoElementError
    # 看进度条是否增长
    if progress_value < 0.99 and progress_value < TaskPanel.get_progress_value(bp) is False:
        raise CompareError
    # 关闭领奖弹窗
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

# 宝箱的奖励领取测试
def box_collect_test(bp:BasePage, index:int, box_award_dict:dict):
    status = TaskPanel.get_box_status(bp)
    position_list = TaskPanel.get_box_position_list(bp)
    if not status[1]:
        print("无法领取，跳过box_collect_test宝箱领取测试")
        return
    # 计算库存
    stock_expect_dict = box_award_dict.copy()
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        stock_expect_dict[stock_icon] += count
    # 点击宝箱
    bp.click_position(position_list[index])
    bp.sleep(0.2)
    # 对照奖励
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(box_award_dict, reward_dict)
    # 对照库存
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        compare(count, stock_expect_dict[stock_icon])
    status = TaskPanel.get_box_status(bp)
    if index + 1 not in status[2]:
        raise FindNoElementError
    # 关闭弹窗
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    print("box_collect_test宝箱领取测试通过")




def collect_test(bp:BasePage):
    bp.cmd("missiondone 2")
    bp.go_to_panel("TaskPanel")
    bp.sleep(1)

    task_id_list = TaskPanel.get_task_id_list(bp)
    viewport = TaskPanel.get_viewport(bp)
    collect_all_test(bp, task_id_list, viewport)
    # 周常
    bp.cmd("missiondone 3")
    TaskPanel.switch_tab(bp, 1)
    task_kind = TaskPanel.get_task_kind(bp)
    compare(task_kind, "Weekly")
    task_id_list = TaskPanel.get_task_id_list(bp)
    viewport.change_item(object_id_list=task_id_list)
    collect_all_test(bp, task_id_list, viewport)
    # 月常
    bp.cmd("missiondone 4")
    TaskPanel.switch_tab(bp, 2)
    task_kind = TaskPanel.get_task_kind(bp)
    compare(task_kind, "Monthly")
    box_position = TaskPanel.get_month_box_position(bp)
    box_award_dict = TaskPanel.get_month_award_detail(bp, box_position)
    print(box_award_dict)
    task_id_list = TaskPanel.get_task_id_list(bp)
    viewport.change_item(object_id_list=task_id_list)
    collect_all_test(bp, task_id_list, viewport)
    # 判断箱子是否可领取
    month_box_status = TaskPanel.get_month_box_status(bp)
    if month_box_status != 1:
        raise FindNoElementError
    # 计算库存
    stock_expect_dict = box_award_dict.copy()
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        stock_expect_dict[stock_icon] += count
    # 点击宝箱
    bp.click_position(box_position)
    bp.sleep(0.2)
    # 对照奖励
    reward_dict = RewardsPanel.get_reward_dict(bp)
    print(box_award_dict, reward_dict)
    compare_dict(box_award_dict, reward_dict)
    # 对照库存
    for stock_icon in stock_expect_dict:
        count = bp.get_item_count(item_icon_name=stock_icon)
        compare(count, stock_expect_dict[stock_icon])
    month_box_status = TaskPanel.get_month_box_status(bp)
    if month_box_status != 2:
        raise FindNoElementError
    # 关闭弹窗
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    # 切换到日常标签
    TaskPanel.switch_tab(bp, 0)
    task_kind = TaskPanel.get_task_kind(bp)
    compare(task_kind, "Daily")
    TaskPanel.click_btn_close(bp)

def main(bp: BasePage):
    jump_test(bp)
    collect_test(bp)


if __name__ == '__main__':
    bp = BasePage()
    # bp.set_item_count(target_count=60000, item_tpid="100200")
    main(bp)





