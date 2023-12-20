
from common.basePage import BasePage
import random
from tools.commonTools import *

from panelObjs.achievementPanel import AchievementPanel
from panelObjs.achievementGroupPanel import AchievementGroupPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.rewardsPreviewPanel import RewardsPreviewPanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.loadingPanel import LoadingPanel
from common import resource

# 点击页面介绍测试
def AchievementPanel_test_0(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    print("点击页面介绍开始")
    bp.sleep(0.5)
    AchievementPanel.click_btn_i(bp)
    if not AchievementPanel.is_tips_active(bp):
        raise FindNoElementError
    bp.click_position([0.5, 0.1])


# 随机点击未解锁成就测试
def AchievementPanel_test_1(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    bp.debug_log(f"locked_set, unlockable_set, unlocked_set:{locked_set, unlockable_set, unlocked_set}")
    locked_list = list(locked_set)
    viewport = AchievementPanel.get_viewport(bp)
    print("点击未解锁成就开始")
    # 点击未解锁成就
    if not locked_list:
        print("点击未解锁成就跳过")
        return
    cur = 0
    while cur < len(locked_list):
        viewport.move_until_appear(viewport.item_id_list[locked_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[locked_list[cur]])
        if not AchievementPanel.is_unlock_tips_active(bp):
            raise FindNoElementError
        bp.click_position([0.5, 0.1])
        cur += 1
    print("点击未解锁成就完成")




# 点击可解锁成就测试
def AchievementPanel_test_2(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    print("改变等级使成就可解锁")
    exp = 10000000
    # 升级后返回出进下刷新界面
    bp.set_item_count(exp, item_tpid="100200")
    bp.debug_log(f"exp:{exp}")
    bp.go_home()
    bp.sleep(3)
    bp.go_to_panel("AchievementPanel")
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    bp.debug_log(f"locked_set, unlockable_set, unlocked_set:{locked_set, unlockable_set, unlocked_set}")
    viewport = AchievementPanel.get_viewport(bp)
    # 点击可解锁成就 将它们都解锁使task mini出现
    unlockable_list = list(unlockable_set)
    bp.debug_log("点击可解锁成就开始")
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
        bp.debug_log(f"locked_set, unlockable_set, unlocked_set:{locked_set, unlockable_set, unlocked_set}")
        bp.debug_log(f"unlocked_expect_set, unlocked_set:{unlocked_expect_set, unlocked_set}")
        bp.debug_log(f"unlockable_expect_set, unlockable_set:{unlockable_expect_set, unlockable_set}")
        compare(unlocked_expect_set, unlocked_set)
        compare(unlockable_expect_set, unlockable_set)
        print("点击可解锁成就完成")
    else:
        print("点击可解锁成就跳过")


def AchievementPanel_test_3(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    print("minitask跳转开始")
    # 从任务导航进入成就 看进的成就组名称是否正确
    group_name = AchievementPanel.get_task_mini_group_name(bp)
    AchievementPanel.click_task_mini(bp)
    title = AchievementGroupPanel.get_title(bp)
    bp.debug_log(f"group_name, title：{group_name, title}")
    compare(group_name, title)
    bp.sleep(0.5)
    AchievementGroupPanel.click_btn_close(bp)
    bp.sleep(0.5)

# 随机点击已解锁成就测试
def AchievementGroupPanel_test_0(bp:BasePage):
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    # 点击可解锁成就 将它们都解锁使task mini出现
    print("随机点击已解锁成就开始")
    # 点击已解锁成就
    unlocked_list = list(unlocked_set)
    # if unlocked_list:
    #     r = random.randint(0, len(unlocked_list) - 1)
    #     viewport.move_until_appear(viewport.item_id_list[unlocked_list[r]])
    #     group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[r]])
    #     position_list = AchievementPanel.get_achievement_position_list(bp)
    #     bp.click_position(position_list[unlocked_list[r]])
    #     bp.sleep(1)
    #     title = AchievementGroupPanel.get_title(bp)
    #     compare(group_name, title)
    #     bp.debug_log("随机点击已解锁成就完成")
    # else:
    #     bp.debug_log("随机点击已解锁成就跳过")
    cur = 0
    while cur < len(unlocked_list):
        viewport.move_until_appear(viewport.item_id_list[unlocked_list[cur]])
        group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlocked_list[cur]])
        bp.sleep(0.5)
        title = AchievementGroupPanel.get_title(bp)
        bp.debug_log(f"group_name, title：{group_name, title}")
        compare(group_name, title)
        achievement_jump_test(bp)
        bp.sleep(0.5)
        cur += 1


def achievement_jump_test(bp: BasePage):
    print("随机成就跳转开始")
    achievement_position_list = AchievementGroupPanel.get_achievement_position_list(bp)
    achievement_bg_icon_list = AchievementGroupPanel.get_achievement_bg_icon_list(bp)
    go_index_list, collect_index_list, uncollect_index_list = AchievementGroupPanel.get_go_collect_and_uncollect_index_list(bp)
    bp.debug_log(f"go_index_list, collect_index_list, uncollect_index_list:{go_index_list, collect_index_list, uncollect_index_list}")
    if not go_index_list:
        AchievementGroupPanel.click_btn_close(bp)
        print("随机成就跳转跳过")
        return
    r = random.randint(0, len(go_index_list) - 1)
    if "achv_item_icon_bg_1" in achievement_bg_icon_list[go_index_list[r]]:
        AchievementGroupPanel.click_btn_close(bp)
        print("网页跳转直接跳过")
        return
    bp.click_position(achievement_position_list[go_index_list[r]])
    bp.sleep(1)
    select_test(bp, go_index_list[r])
    cur = 0
    while cur < 10:
        if AchievementGroupPanel.is_panel_active(bp):
            AchievementGroupPanel.click_btn_go(bp)
        cur += 1
    bp.sleep(0.2)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp)
    img = bp.get_full_screen_shot()
    bp.save_img(img, "achievementGroupPanel_jump_test")
    bp.go_to_panel("AchievementPanel")

def AchievementGroupPanel_test_1(bp: BasePage):
    bp.cmd("missiondone 10")
    bp.go_to_panel("AchievementPanel")
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    # 点击可解锁成就 将它们都解锁使task mini出现
    print("随机点击已解锁成就开始")
    # 点击已解锁成就
    unlocked_list = list(unlocked_set)
    # 随机一个进行图标点击测试
    r = random.randint(0, len(unlocked_list) - 1)
    cur = 4
    while cur < len(unlocked_list):
        viewport.move_until_appear(viewport.item_id_list[unlocked_list[cur]])
        group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlocked_list[cur]])
        bp.sleep(0.5)
        title = AchievementGroupPanel.get_title(bp)
        bp.debug_log(f"group_name, title：{group_name, title}")
        compare(group_name, title)
        if r == cur:
            click_icon_test(bp)
        collect_all_test(bp)
        AchievementGroupPanel.click_btn_close(bp)
        cur += 1

def collect_all_test(bp: BasePage):
    achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
    if achievement_point == progress_denominator:
        return
    while AchievementGroupPanel.is_box_clickable(bp):
        AchievementGroupPanel.click_box(bp)
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(0.5)
        # 防止鱼卡弹窗
        bp.clear_popup()
        achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)

    reward_icon_list, reward_quantity_list = AchievementGroupPanel.get_box_reward(bp)
    item_dict = resource.make_item_dict(item_coin_list=reward_icon_list, item_quantity_list= reward_quantity_list)

    while achievement_point != progress_denominator:
        achievement_point, progress_denominator = collect_once_test(bp)
        if not AchievementGroupPanel.is_box_clickable(bp):
            continue
        item_stock_expect_list = bp.get_item_count_list(reward_icon_list)
        cur = 0
        while cur < len(reward_icon_list):
            item_stock_expect_list[cur] += item_dict[reward_icon_list[cur]]
            cur += 1
        AchievementGroupPanel.click_box(bp)
        reward_dict = RewardsPanel.get_reward_dict(bp)
        bp.debug_log(f"item_dict, reward_dict:{item_dict, reward_dict}")
        compare_dict(item_dict, reward_dict)
        item_stock_list = bp.get_item_count_list(reward_icon_list)
        bp.debug_log(f"item_stock_expect_list, item_stock_list:{item_stock_expect_list, item_stock_list}")
        compare_list(item_stock_expect_list, item_stock_list)
        RewardsPanel.click_tap_to_claim(bp)
        # bp.sleep(0.5)
        # 防止鱼卡弹窗
        bp.clear_popup()
        achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
        if achievement_point == progress_denominator:
            break
        reward_icon_list, reward_quantity_list = AchievementGroupPanel.get_box_reward(bp)
        item_dict = resource.make_item_dict(item_coin_list=reward_icon_list, item_quantity_list=reward_quantity_list)
    complete_numerator, complete_denominator = AchievementGroupPanel.get_complete(bp)
    bp.debug_log(f"complete_numerator, complete_denominator:{complete_numerator, complete_denominator}")
    bp.debug_log(f"achievement_point, progress_denominator:{achievement_point, progress_denominator}")
    compare(complete_numerator, complete_denominator)



def collect_once_test(bp: BasePage):
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
    AchievementGroupPanel.click_btn_collect(bp)
    # bp.sleep(0.5)
    achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
    bp.debug_log(f"achievement_point_expect, achievement_point:{achievement_point_expect, achievement_point}")
    compare(achievement_point_expect, achievement_point)
    item_count_list = bp.get_item_count_list(item_icon_list)
    bp.debug_log(f"item_quantity_list, item_count_list:{item_quantity_list, item_count_list}")
    compare_list(item_quantity_list, item_count_list)
    return achievement_point, progress_denominator


def select_test(bp: BasePage, index):
    achievement_icon_list = AchievementGroupPanel.get_achievement_icon_list(bp)
    icon_main = AchievementGroupPanel.get_icon_main(bp)
    selected_status_list = AchievementGroupPanel.get_selected_status_list(bp)
    selected_index = AchievementGroupPanel.get_selected_index(selected_status_list)
    bp.debug_log(f"index, selected_index:{index, selected_index}")
    bp.debug_log(f"achievement_icon_list[index], icon_main:{achievement_icon_list[index], icon_main}")
    compare(index, selected_index)
    compare(achievement_icon_list[index], icon_main)


def click_icon_test(bp: BasePage):
    item_icon_list = AchievementGroupPanel.get_item_icon_list(bp)
    item_position_list = AchievementGroupPanel.get_item_position_list(bp)
    r = random.randint(0, len(item_position_list) - 1)
    bp.debug_log(f"r:{r}")
    item_icon_expect = item_icon_list[r]
    bp.click_position(item_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    bp.debug_log(f"item_icon_expect, item_icon:{item_icon_expect, item_icon}")
    compare(item_icon_expect, item_icon)
    bp.click_position([0.5, 0.1])
    # 点击宝箱
    AchievementGroupPanel.click_box(bp)
    cur = 0
    while not RewardsPreviewPanel.is_panel_active(bp):
        # 防止没点上
        AchievementGroupPanel.click_box(bp)
        cur += 1
        if cur > 10:
            raise FindNoElementError
    reward_icon_list = RewardsPreviewPanel.get_reward_icon_list(bp)
    reward_position_list = RewardsPreviewPanel.get_reward_position_list(bp)
    r = random.randint(0, len(reward_position_list) - 1)
    bp.debug_log(f"r:{r}")
    bp.click_position(reward_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    bp.debug_log(f"reward_icon_list[r], item_icon:{reward_icon_list[r], item_icon}")
    compare(reward_icon_list[r], item_icon)
    bp.click_position([0.5, 0.1])
    print("click_icon_test图标点击测试通过")

def achievement_test(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    # click_tips_test(bp)
    # achievement_status_test(bp)
    # collect_test(bp)
    # select_test(bp)
    click_icon_test(bp)
    AchievementGroupPanel.click_btn_close(bp)
    AchievementPanel.click_btn_close(bp)
    print("achievement_test成就系统测试通过")




if __name__ == '__main__':
    bp = BasePage()
    # AchievementPanel_test_0(bp)
    # AchievementPanel_test_1(bp)
    # AchievementPanel_test_2(bp)
    # AchievementPanel_test_3(bp)
    # AchievementGroupPanel_test_0(bp)
    AchievementGroupPanel_test_1(bp)
    # print(bp.get_item_count(item_tpid="100000"))
