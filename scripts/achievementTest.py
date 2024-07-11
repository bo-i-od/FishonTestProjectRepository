from common.basePage import BasePage
import random

from panelObjs.fishBagPanel import FishBagPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from tools.commonTools import *

from panelObjs.achievementPanel import AchievementPanel
from panelObjs.achievementGroupPanel import AchievementGroupPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.rewardsPreviewPanel import RewardsPreviewPanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.loadingPanel import LoadingPanel
from common import resource, gameInit


# 点击页面介绍测试
def tips_test(bp:BasePage):
    bp.debug_log("点击页面介绍开始")

    bp.sleep(0.5)
    AchievementPanel.click_btn_i(bp)
    bp.sleep(0.5)
    if not AchievementPanel.is_tips_active(bp):
        bp.debug_log("erro_if not AchievementPanel.is_tips_active(bp)")
    bp.sleep(0.5)
    AchievementPanel.click_btn_i(bp)
    bp.sleep(0.5)


# 点击未解锁成就测试
def locked_test(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    bp.sleep(0.5)
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    bp.debug_log(f"locked_set, unlockable_set, unlocked_set:{locked_set, unlockable_set, unlocked_set}")
    locked_list = list(locked_set)
    viewport = AchievementPanel.get_viewport(bp)
    bp.debug_log("点击未解锁成就开始")
    # 点击未解锁成就
    if not locked_list:
        bp.debug_log("点击未解锁成就跳过")
        return
    cur = 0
    while cur < len(locked_list):
        viewport.move_until_appear(viewport.item_id_list[locked_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[locked_list[cur]])
        bp.sleep(0.5)
        if not AchievementPanel.is_unlock_tips_active(bp):
            bp.debug_log("erro_if not AchievementPanel.is_unlock_tips_active(bp)")
        cur += 1
    bp.debug_log("点击未解锁成就完成")




# 点击可解锁成就测试
def unlock_test(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    bp.debug_log("改变等级使成就可解锁")
    exp = 123456789
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
            bp.sleep(0.5)
            cur += 1

        locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
        bp.debug_log(f"locked_set, unlockable_set, unlocked_set:{locked_set, unlockable_set, unlocked_set}")
        compare(unlocked_expect_set, unlocked_set)
        compare(unlockable_expect_set, unlockable_set)
        bp.debug_log("点击可解锁成就完成")
    else:
        bp.debug_log("点击可解锁成就跳过")

# minitask跳转测试
def minitask_test(bp:BasePage):
    bp.go_to_panel("AchievementPanel")
    bp.debug_log("minitask跳转开始")
    # 从任务导航进入成就 看进的成就组名称是否正确
    group_name = AchievementPanel.get_task_mini_group_name(bp)
    AchievementPanel.click_task_mini(bp)
    title = AchievementGroupPanel.get_title(bp)
    compare(group_name, title)
    bp.sleep(0.5)
    click_icon_test(bp)
    AchievementGroupPanel.click_btn_close(bp)
    bp.sleep(0.5)

# 点击已解锁成就并进行跳转测试
def jump_all_test(bp:BasePage):
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    # 点击可解锁成就 将它们都解锁使task mini出现
    bp.debug_log("随机点击已解锁成就开始")
    # 点击已解锁成就
    unlocked_list = list(unlocked_set)
    if unlocked_list:
        r = random.randint(0, len(unlocked_list) - 1)
        viewport = AchievementPanel.get_viewport(bp)
        viewport.move_until_appear(viewport.item_id_list[unlocked_list[r]])
        group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[r]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlocked_list[r]])
        bp.sleep(0.5)
        title = AchievementGroupPanel.get_title(bp)
        compare(group_name, title)
        jump_test(bp)
        bp.debug_log("随机点击已解锁成就完成")
    else:
        bp.debug_log("随机点击已解锁成就跳过")
    # cur = 0
    # while cur < len(unlocked_list):
    #     viewport = AchievementPanel.get_viewport(bp)
    #     viewport.move_until_appear(viewport.item_id_list[unlocked_list[cur]])
    #     group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[cur]])
    #     position_list = AchievementPanel.get_achievement_position_list(bp)
    #     bp.click_position(position_list[unlocked_list[cur]])
    #     bp.sleep(0.5)
    #     title = AchievementGroupPanel.get_title(bp)
    #     compare(group_name, title)
    #     jump_test(bp)
    #     bp.sleep(0.5)
    #     cur += 1


# 成就跳转测试
def jump_test(bp: BasePage):
    bp.debug_log("随机成就跳转开始")
    achievement_position_list = AchievementGroupPanel.get_achievement_position_list(bp)
    achievement_bg_icon_list = AchievementGroupPanel.get_achievement_bg_icon_list(bp)
    go_index_list, collect_index_list, uncollect_index_list = AchievementGroupPanel.get_go_collect_and_uncollect_index_list(bp)
    bp.debug_log(f"go_index_list, collect_index_list, uncollect_index_list:{go_index_list, collect_index_list, uncollect_index_list}")
    if not go_index_list:
        AchievementGroupPanel.click_btn_close(bp)
        bp.debug_log("随机成就跳转跳过")
        return
    r = random.randint(0, len(go_index_list) - 1)
    if "achv_item_icon_bg_1" in achievement_bg_icon_list[go_index_list[r]]:
        AchievementGroupPanel.click_btn_close(bp)
        bp.debug_log("网页跳转直接跳过")
        return
    bp.click_position(achievement_position_list[go_index_list[r]])
    bp.sleep(0.5)
    select_test(bp, go_index_list[r])
    cur = 0
    while cur < 10:
        if AchievementGroupPanel.is_panel_active(bp):
            AchievementGroupPanel.click_btn_go(bp)
        cur += 1
    bp.sleep(0.5)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)
    # img = bp.get_full_screen_shot()
    # bp.save_img(img, "achievementGroupPanel_jump_test")
    bp.go_to_panel("AchievementPanel")

# def login(zhanghao,mima):

# 随机一个成就组全部领取测试
def collect_test(bp: BasePage):
    bp.cmd("missiondone 10")
    bp.go_to_panel("AchievementPanel")
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    # 点击可解锁成就 将它们都解锁使task mini出现
    bp.debug_log("随机点击已解锁成就开始")
    # 点击已解锁成就
    unlocked_list = list(unlocked_set)
    # 随机一个进行领取测试
    r = random.randint(1, len(unlocked_list) - 1)
    viewport.move_until_appear(viewport.item_id_list[unlocked_list[r]])
    group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[r]])
    position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(position_list[unlocked_list[r]])
    bp.sleep(0.5)
    title = AchievementGroupPanel.get_title(bp)
    compare(group_name, title)
    click_icon_test(bp)
    collect_all_test(bp)
    AchievementGroupPanel.click_btn_close(bp)

    # 所有进行领取
    # cur = 1
    # while cur < len(unlocked_list):
    #     viewport.move_until_appear(viewport.item_id_list[unlocked_list[cur]])
    #     group_name = AchievementPanel.get_group_name(bp, achievement_id=viewport.item_id_list[unlocked_list[cur]])
    #     position_list = AchievementPanel.get_achievement_position_list(bp)
    #     bp.click_position(position_list[unlocked_list[cur]])
    #     bp.sleep(0.5)
    #     title = AchievementGroupPanel.get_title(bp)
    #     compare(group_name, title)
    #     if r == cur:
    #         click_icon_test(bp)
    #     collect_all_test(bp)
    #     AchievementGroupPanel.click_btn_close(bp)
    #     cur += 1

def collect_all_test(bp: BasePage):
    achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
    if achievement_point == progress_denominator:
        img = bp.get_full_screen_shot()
        bp.save_img(img, "跳过collect_all_test期望状态为已经领取完成")
        return

    # 点击箱子查看奖励
    while AchievementGroupPanel.is_box_clickable(bp):
        AchievementGroupPanel.click_box(bp)
        RewardsPanel.wait_for_panel_appear(bp)
        bp.sleep(0.5)
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(0.5)
        # 防止鱼卡弹窗
        bp.clear_popup_until_appear(elements_data=AchievementGroupPanel.get_panel_element())
        achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)

    reward_icon_list, reward_quantity_list = AchievementGroupPanel.get_box_reward(bp)
    item_dict = resource.make_item_dict(item_icon_list=reward_icon_list, item_quantity_list= reward_quantity_list)
    # 在没领满之前一直领取
    while achievement_point != progress_denominator:
        achievement_point, progress_denominator = collect_once_test(bp)

        # 进度条宝箱不可领取就进行下次点击
        if not AchievementGroupPanel.is_box_clickable(bp):
            continue

        # 领取进度条宝箱 做数值方面验证
        item_stock_expect_list = bp.get_item_count_list(item_icon_name_list=reward_icon_list)
        cur = 0
        while cur < len(reward_icon_list):
            item_stock_expect_list[cur] += item_dict[reward_icon_list[cur]]
            cur += 1
        AchievementGroupPanel.click_box(bp)
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(item_dict, reward_dict)
        item_stock_list = bp.get_item_count_list(item_icon_name_list=reward_icon_list)
        compare_list(item_stock_expect_list, item_stock_list)
        RewardsPanel.wait_for_panel_appear(bp)
        bp.sleep(0.5)
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(0.5)
        # 防止鱼卡弹窗
        if FishBagPanel.is_panel_active(bp):
            bp.clear_popup()
            bp.sleep(0.5)
        achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
        if achievement_point == progress_denominator:
            break
        reward_icon_list, reward_quantity_list = AchievementGroupPanel.get_box_reward(bp)
        item_dict = resource.make_item_dict(item_icon_list=reward_icon_list, item_quantity_list=reward_quantity_list)
    complete_numerator, complete_denominator = AchievementGroupPanel.get_complete(bp)
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
    bp.sleep(1)
    achievement_point, progress_denominator = AchievementGroupPanel.get_achievement_point(bp)
    bp.debug_log(f"achievement_point_expect, achievement_point:{achievement_point_expect, achievement_point}")
    compare(achievement_point_expect, achievement_point)
    item_count_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)
    bp.debug_log(f"item_quantity_list, item_count_list:{item_quantity_list, item_count_list}")
    compare_list(item_quantity_list, item_count_list)
    return achievement_point, progress_denominator


def select_test(bp: BasePage, index:int):
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
    bp.click_position([0.5, 0.9])
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
    bp.sleep(0.5)
    # item_icon = ItemTipsPanel.get_item_icon(bp)
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon_list[r])
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon_list[r])
    bp.debug_log("click_icon_test图标点击测试通过")

def main(bp:BasePage):
    # 登录到大厅
    cmd_list = ["guideskip", "add 1 100200 12345"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # # 关闭升级弹窗
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    bp.go_to_panel("AchievementPanel")
    tips_test(bp)
    locked_test(bp)
    unlock_test(bp)
    minitask_test(bp)
    jump_all_test(bp)
    collect_test(bp)

    # 返回大厅
    bp.go_home()



if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20030")
    main(bp)

