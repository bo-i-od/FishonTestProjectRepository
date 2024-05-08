from common.basePage import BasePage
import random

from panelObjs.achievementCategoryPanel import AchievementCategoryPanel
from panelObjs.flashTipsPanel import FlashTipsPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from tools.commonTools import *

from panelObjs.achievementPanel import AchievementPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from common import gameInit


def unlock_test(bp: BasePage):
    bp.go_to_panel("AchievementPanel")
    bp.sleep(1)

    # 切换到悬赏鱼页面
    AchievementPanel.switch_tab(bp, 2)
    bp.sleep(1)

    # 解锁
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    unlockable_list = list(unlockable_set)
    cur = 0
    while cur < len(unlockable_list):
        viewport.move_until_appear(viewport.item_id_list[unlockable_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlockable_list[cur]])
        cur += 1
        bp.sleep(0.5)
        if cur < len(unlockable_list):
            continue
        bp.sleep(1)

    # 随机点击一个
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    unlocked_list = list(unlocked_set)
    r = random.randint(0, len(unlocked_list) - 1)
    print(viewport.item_id_list)
    viewport.move_until_appear(viewport.item_id_list[unlocked_list[r]])
    achievement_position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(achievement_position_list[unlocked_list[r]])
    bp.sleep(1)

    # 点击解锁
    category_viewport = AchievementCategoryPanel.get_category_viewport(bp)
    r = random.randint(0, len(category_viewport.item_id_list) - 1)
    category_viewport.move_until_appear(target_id=category_viewport.item_id_list[r])
    bp.sleep(1)
    category_position_list = AchievementCategoryPanel.get_category_position_list(bp)
    bp.click_position(category_position_list[r])
    bp.sleep(1)
    if not FlashTipsPanel.is_panel_active(bp):
        raise FindNoElementError

    # 点击奖励图标
    reward_position_list = AchievementCategoryPanel.get_reward_position_list(bp)
    reward_icon_list = AchievementCategoryPanel.get_reward_icon_list(bp)
    r = random.randint(0, len(reward_position_list) - 1)
    bp.click_position(reward_position_list[r])
    bp.sleep(1)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(reward_icon_list[r], item_icon)
    # bp.click_position([0.9, 0.1])
    # bp.sleep(1)

    # 关闭
    bp.go_home()

def category_test(bp: BasePage):
    # 读表格数据
    table_data = AchievementCategoryPanel.get_category_table_data(bp)

    # 随机选一个鱼种完成
    table_open_index_list = AchievementCategoryPanel.get_table_open_index_list(bp, table_data=table_data)
    print(table_open_index_list)
    # r = random.randint(0, len(table_open_index_list) - 1)
    r = 7
    AchievementCategoryPanel.do_category(bp, table_data=table_data, index=r)
    bp.go_home()

    # 去悬赏界面
    bp.go_to_panel("AchievementPanel")
    bp.sleep(1)
    AchievementPanel.switch_tab(bp, 2)
    bp.sleep(1)

    # 选择对应的渔场
    target_icon = table_data["icon"][r]
    achievement_icon_list = AchievementPanel.get_achievement_icon_list(bp)
    achievement_position_list = AchievementPanel.get_achievement_position_list(bp)
    index = achievement_icon_list.index(target_icon)
    bp.click_position(achievement_position_list[index])

    # 解锁
    category_viewport = AchievementCategoryPanel.get_category_viewport(bp)
    cur = 0
    while cur < len(category_viewport.item_id_list):
        # 移动到可点击位置点击
        category_viewport.move_until_appear(category_viewport.item_id_list[cur])
        category_position_list = AchievementCategoryPanel.get_category_position_list(bp)
        bp.click_position(category_position_list[cur])
        bp.sleep(1)
        if FlashTipsPanel.is_panel_active(bp):
            raise FindElementError
        cur += 1

    # 计算期望奖励
    reward_icon_list = AchievementCategoryPanel.get_reward_icon_list(bp)
    reward_quantity_list = AchievementCategoryPanel.get_reward_quantity_list(bp)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=reward_icon_list)
    cur = 0
    while cur < len(reward_icon_list):
        stock_expect_list[cur] += reward_quantity_list[cur]
        cur += 1


    # 领取奖励 对比奖励数量
    AchievementCategoryPanel.click_btn_rewards(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    cur = 0
    while cur < len(reward_icon_list):
        compare(reward_dict[reward_icon_list[cur]], reward_quantity_list[cur])
        cur += 1
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 对照库存数量
    stock_list = bp.get_item_count_list(item_icon_name_list=reward_icon_list)
    compare_list(stock_expect_list, stock_list)

    bp.go_home()

def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["guideskip", "add 1 100200 123456789", "add 1 100500 1234"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # # 关闭升级弹窗
    # PlayerLevelupPanel.wait_for_panel_appear(bp)

    # 升级
    unlock_test(bp)
    category_test(bp)

if __name__ == '__main__':
    bp = BasePage("b6h65hd64p5pxcyh")
    main(bp)

