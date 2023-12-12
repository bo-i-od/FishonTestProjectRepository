
from common.basePage import BasePage
import random
from tools.commonTools import *
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.homePanel import HomePanel
from panelObjs.achievementPanel import AchievementPanel
from panelObjs.achievementGroupPanel import AchievementGroupPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPreviewPanel import RewardsPreviewPanel

def achievement_status_test(bp:BasePage):
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    locked_list = list(locked_set)
    viewport = AchievementPanel.get_viewport(bp)
    # 点击未解锁成就
    if locked_list:
        r = random.randint(0, len(locked_list) - 1)
        viewport.move_until_appear(viewport.item_id_list[locked_list[r]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[locked_list[r]])
        if not AchievementPanel.is_unlock_tips_active(bp):
            raise FindNoElementError
        bp.click_position([0.5, 0.1])
    # 点击可解锁成就 将它们都解锁使task mini出现
    unlockable_list = list(unlockable_set)
    if unlockable_list:
        unlockable_expect_set = unlockable_set
        unlocked_expect_set = unlocked_set
        cur = 0
        while cur < len(unlockable_list):
            unlockable_expect_set.remove(unlockable_list[cur])
            unlocked_expect_set.add(unlockable_list[cur])
            viewport.move_until_appear(viewport.item_id_list[unlockable_list[cur]])
            position_list = AchievementPanel.get_achievement_position_list(bp)
            bp.click_position(position_list[unlockable_list[cur]])
            cur += 1
        locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
        compare(unlocked_expect_set, unlocked_set)
        compare(unlockable_expect_set, unlockable_set)
    # 点击已解锁成就
    unlocked_list = list(unlocked_set)
    r = random.randint(0, len(unlocked_list) - 1)
    viewport.move_until_appear(viewport.item_id_list[unlocked_list[r]])
    group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[r]])
    position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(position_list[unlocked_list[r]])
    title = AchievementGroupPanel.get_title(bp)
    compare(group_name, title)
    AchievementGroupPanel.click_btn_close(bp)
    print("achievement_status_test解锁状态测试通过")

def click_tips_test(bp:BasePage):
    AchievementPanel.click_btn_i(bp)
    if not AchievementPanel.is_tips_active(bp):
        raise FindNoElementError
    bp.click_position([0.5, 0.1])
    print("click_tips_test点击说明测试通过")

def collect_test(bp:BasePage):
    # 从任务导航进入成就 看进的成就组名称是否正确
    group_name = AchievementPanel.get_task_mini_group_name(bp)
    AchievementPanel.click_task_mini(bp)
    title = AchievementGroupPanel.get_title(bp)
    compare(group_name, title)
    # 对比选中的成就项和显示的是否一致
    selected_status_list = AchievementGroupPanel.get_selected_status_list(bp)
    selected_index = AchievementGroupPanel.get_selected_index(bp, selected_status_list)
    achievement_icon_list = AchievementGroupPanel.get_achievement_icon_list(bp)
    icon_main = AchievementGroupPanel.get_icon_main(bp)
    compare(icon_main, achievement_icon_list[selected_index])
    # 记录奖励数量
    item_icon_list = AchievementGroupPanel.get_item_icon_list(bp)
    item_quantity_list = AchievementGroupPanel.get_item_quantity_list(bp)
    achievement_point_expect, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
    cur = 0
    while cur < len(item_icon_list):
        if item_icon_list[cur] == "coin_achv":
            achievement_point_expect += item_quantity_list[cur]
            item_quantity_list[cur] = 0
            cur += 1
            continue
        item_count = bp.get_item_count(item_icon_name=item_icon_list[cur])
        item_quantity_list[cur] += item_count
        cur += 1
    # 点击领取
    if not AchievementGroupPanel.click_btn_collect(bp):
        return
    bp.sleep(0.5)
    achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
    compare(achievement_point_expect, achievement_point)
    item_count_list = bp.get_item_count_list(item_icon_list)
    compare_list(item_quantity_list, item_count_list)

def select_test(bp:BasePage):
    achievement_position_list = AchievementGroupPanel.get_achievement_position_list(bp)
    achievement_icon_list = AchievementGroupPanel.get_achievement_icon_list(bp)
    r = random.randint(0, len(achievement_position_list) - 1)
    bp.click_position(achievement_position_list[r])
    icon_main = AchievementGroupPanel.get_icon_main(bp)
    selected_status_list = AchievementGroupPanel.get_selected_status_list(bp)
    selected_index = AchievementGroupPanel.get_selected_index(bp, selected_status_list)
    compare(r, selected_index)
    compare(achievement_icon_list[r], icon_main)

def click_icon_test(bp:BasePage):
    item_icon_list = AchievementGroupPanel.get_item_icon_list(bp)
    item_position_list = AchievementGroupPanel.get_item_position_list(bp)
    r = random.randint(0, len(item_position_list) - 1)
    item_icon_expect = item_icon_list[r]
    bp.click_position(item_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon_expect, item_icon)
    bp.click_position([0.5, 0.1])
    # 点击宝箱
    AchievementGroupPanel.click_box(bp)
    cur = 0
    while not RewardsPreviewPanel.is_panel_active(bp):
        # 防止没点上
        AchievementGroupPanel.click_box(bp)
        cur += 1
        if cur > 2:
            raise FindNoElementError
    reward_icon_list = RewardsPreviewPanel.get_reward_icon_list(bp)
    reward_position_list = RewardsPreviewPanel.get_reward_position_list(bp)
    r = random.randint(0, len(reward_position_list) - 1)
    bp.click_position(reward_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(reward_icon_list[r], item_icon)
    bp.click_position([0.5, 0.1])
    print("click_icon_test图标点击测试通过")

def achievement_test(bp:BasePage):
    HomePanel.go_to_AchievementPanel(bp)
    click_tips_test(bp)
    achievement_status_test(bp)
    collect_test(bp)
    select_test(bp)
    click_icon_test(bp)
    AchievementGroupPanel.click_btn_close(bp)
    AchievementPanel.click_btn_close(bp)
    print("achievement_test成就系统测试通过")




if __name__ == '__main__':
    bp = BasePage()
    achievement_test(bp)
    # print(bp.get_item_count(item_tpid="100000"))
