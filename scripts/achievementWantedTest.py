from common.basePage import BasePage
import random

from panelObjs.AchievementWantedPanel import AchievementWantedPanel
from panelObjs.FlashTipsPanel import FlashTipsPanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from tools.commonTools import *

from panelObjs.AchievementPanel import AchievementPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.RewardsPreviewPanel import RewardsPreviewPanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.LoadingPanel import LoadingPanel
from common import resource, gameInit


def unlock_test(bp: BasePage):
    bp.go_to_panel("AchievementPanel")
    bp.sleep(0.5)


    # 切换到悬赏鱼页面
    AchievementPanel.switch_tab(bp, 1)
    bp.sleep(0.5)

    # 解锁
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    unlockable_list = list(unlockable_set)
    r = random.randint(0, len(unlockable_list) - 1)
    viewport.move_until_appear(viewport.item_id_list[unlockable_list[r]])
    position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(position_list[unlockable_list[r]])
    bp.sleep(1)
    # cur = 0
    # while cur < len(unlockable_list):
    #     viewport.move_until_appear(viewport.item_id_list[unlockable_list[cur]])
    #     position_list = AchievementPanel.get_achievement_position_list(bp)
    #     bp.click_position(position_list[unlockable_list[cur]])
    #     bp.sleep(0.5)
    #     cur += 1
    #     if cur < len(unlockable_list):
    #         continue
    #     bp.sleep(0.5)

    # 随机点击一个
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    unlocked_list = list(unlocked_set)
    r = random.randint(0, len(unlocked_list) - 1)
    viewport.move_until_appear(viewport.item_id_list[unlocked_list[r]])
    achievement_position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(achievement_position_list[unlocked_list[r]])
    bp.sleep(0.5)

    # 点击解锁
    wanted_position_list = AchievementWantedPanel.get_wanted_position_list(bp)
    r = random.randint(0, len(wanted_position_list) - 1)
    bp.click_position(wanted_position_list[r])
    bp.sleep(0.5)
    if not FlashTipsPanel.is_panel_active(bp):
        bp.debug_log("if not FlashTipsPanel.is_panel_active(bp)")

    # 点击奖励图标
    reward_position_list = AchievementWantedPanel.get_reward_position_list(bp)
    reward_icon_list = AchievementWantedPanel.get_reward_icon_list(bp)
    r = random.randint(0, len(reward_position_list) - 1)
    bp.click_position(reward_position_list[r])
    bp.sleep(0.5)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(reward_icon_list[r], item_icon)
    bp.click_position([0.5, 0.9])
    bp.sleep(0.5)

    AchievementWantedPanel.click_btn_close(bp)

def wanted_test(bp: BasePage):
    achievement_icon_list = AchievementPanel.get_achievement_icon_list(bp)
    r = random.randint(0, len(achievement_icon_list) - 1)
    achievement_icon = achievement_icon_list[r]
    # 读表格数据
    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="icon", value=achievement_icon, book_name="ACHIEVEMENT_WANTED.xlsm")
    tpid = table_data_object["TPID"]
    # table_data = bp.excelTools.get_table_data("ACHIEVEMENT_WANTED.xlsm")
    #
    # index = table_data["icon"].index(achievement_icon)
    # tpid = table_data["TPID"][index]
    bp.cmd(f'wantedComplete {tpid}')
    # AchievementWantedPanel.do_wanted(bp, table_data=table_data, index=r)
    bp.go_home()

    # 去悬赏界面
    bp.go_to_panel("AchievementPanel")
    bp.sleep(0.5)

    AchievementPanel.switch_tab(bp, 1)
    bp.sleep(0.5)

    # 选择对应的渔场
    # target_icon = table_data["icon"][r]
    # achievement_icon_list = AchievementPanel.get_achievement_icon_list(bp)
    # index = achievement_icon_list.index(target_icon)
    achievement_icon_id_list = AchievementPanel.get_achievement_icon_id_list(bp)
    viewport = AchievementPanel.get_viewport(bp)
    viewport.move_until_appear(achievement_icon_id_list[r])
    achievement_icon_position = bp.get_position(object_id=achievement_icon_id_list[r])
    bp.click_position(achievement_icon_position)
    bp.sleep(1)

    # 解锁
    wanted_position_list = AchievementWantedPanel.get_wanted_position_list(bp)
    cur = 0
    while cur < len(wanted_position_list):
        bp.click_position(wanted_position_list[cur])
        bp.sleep(0.5)
        if FlashTipsPanel.is_panel_active(bp):
            bp.debug_log("error:if FlashTipsPanel.is_panel_active(bp)")
        cur += 1

    # 计算期望奖励
    reward_icon_list = AchievementWantedPanel.get_reward_icon_list(bp)
    reward_quantity_list = AchievementWantedPanel.get_reward_quantity_list(bp)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=reward_icon_list)
    cur = 0
    while cur < len(reward_icon_list):
        stock_expect_list[cur] += reward_quantity_list[cur]
        cur += 1


    # 领取奖励 对比奖励数量
    AchievementWantedPanel.click_btn_rewards(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    cur = 0
    while cur < len(reward_icon_list):
        compare(reward_dict[reward_icon_list[cur]], reward_quantity_list[cur])
        cur += 1
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(0.5)
    RewardsPanel.click_tap_to_claim(bp)

    # 对照库存数量
    stock_list = bp.get_item_count_list(item_icon_name_list=reward_icon_list)
    compare_list(stock_expect_list, stock_list)

    bp.go_home()

def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["levelupto 90", "add 1 100500 1000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # # 关闭升级弹窗
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    unlock_test(bp)
    wanted_test(bp)

if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21553", is_mobile_device=True)
    main(bp)
    bp.connect_close()