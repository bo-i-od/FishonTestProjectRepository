import random
from common.basePage import BasePage
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.progressRewardsPanel import ProgressRewardsPanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from common import resource
from scripts import battleTest
from tools.commonTools import *

def collect_next_test(bp: BasePage):
    # 把进度条设为马上可以领下一档奖励
    progress_numerator,  progress_denominator = BattlePreparePanel.get_progress(bp)
    BattlePreparePanel.click_btn_close(bp)
    cmd_list = [f"progressSetPoint {progress_denominator - 1}"]
    bp.cmd_list(cmd_list)
    TournamentsPanel.go_to_first_location(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp)
    bp.sleep(0.2)

    # 得到期望奖励
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    current_rewards_quantity_list = BattlePreparePanel.get_current_rewards_quantity_list(bp)
    next_reward_icon = BattlePreparePanel.get_next_reward_icon(bp)
    next_reward_quantity = BattlePreparePanel.get_next_reward_quantity(bp)
    current_rewards_expect_dict = resource.make_item_dict(item_icon_list=current_rewards_icon_list, item_quantity_list=current_rewards_quantity_list, item_dict={next_reward_icon: next_reward_quantity})

    # 钓一条鱼
    battleTest.fish_once(bp, fishscene_id="400301", fish_id="301001")
    bp.sleep(3)

    # 对照奖励
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    current_rewards_quantity_list = BattlePreparePanel.get_current_rewards_quantity_list(bp)
    current_rewards_dict = resource.make_item_dict(item_icon_list=current_rewards_icon_list, item_quantity_list=current_rewards_quantity_list)
    compare_dict(current_rewards_expect_dict, current_rewards_dict)

    # 计算期望库存
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=current_rewards_icon_list)
    cur = 0
    while cur < len(current_rewards_icon_list):
        stock_expect_list[cur] += current_rewards_quantity_list[cur]
        cur += 1

    # 领取奖励
    BattlePreparePanel.click_progress_info(bp)
    bp.sleep(0.2)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(current_rewards_dict, reward_dict)

    # 计算库存是否正确
    stock_list = bp.get_item_count_list(item_icon_name_list=current_rewards_icon_list)
    compare_list(stock_expect_list, stock_list)

    # 关闭恭喜获得
    RewardsPanel.click_tap_to_claim(bp)



def mini_panel_test(bp: BasePage):
    # 保证没有可领取的奖励
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    if current_rewards_icon_list:
        BattlePreparePanel.click_progress_info(bp)
        bp.sleep(0.2)
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(0.2)
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    if current_rewards_icon_list:
        raise FindElementError

    # 记录mini板信息
    progress_mini = BattlePreparePanel.get_progress(bp)
    icon_mini = BattlePreparePanel.get_next_reward_icon(bp)
    quantity_mini = BattlePreparePanel.get_next_reward_quantity(bp)

    # 打开面板
    BattlePreparePanel.click_progress_info(bp)

    # 应该没有可领取奖励
    current_rewards_icon_list = ProgressRewardsPanel.get_current_rewards_icon_list(bp)
    if current_rewards_icon_list:
        raise FindElementError

    # 记录面板信息
    progress = ProgressRewardsPanel.get_progress(bp)
    icon = ProgressRewardsPanel.get_next_reward_icon(bp)
    quantity = ProgressRewardsPanel.get_next_reward_quantity(bp)

    # 看是否一致
    compare(progress_mini, progress)
    compare(icon_mini, icon)
    compare(quantity_mini, quantity)

    # 点击图标
    big_rewards_position_list = ProgressRewardsPanel.get_big_rewards_position_list(bp)
    big_rewards_icon_list = ProgressRewardsPanel.get_big_rewards_icon_list(bp)
    r = random.randint(0, len(big_rewards_position_list) - 1)
    bp.click_position(big_rewards_position_list[r])
    bp.sleep(0.2)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, big_rewards_icon_list[r])
    bp.click_position([0.5, 0.2])

    next_reward_position = ProgressRewardsPanel.get_next_reward_position(bp)
    bp.click_position(next_reward_position)
    bp.sleep(0.2)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon, item_icon)
    bp.click_position([0.5, 0.2])

    # 关闭界面
    ProgressRewardsPanel.click_btn_close(bp)



def complete_test(bp: BasePage):
    # 把进度条设为马上可以领下一档奖励
    BattlePreparePanel.click_btn_close(bp)
    cmd_list = [f"progressSetPoint 10000000"]
    bp.cmd_list(cmd_list)
    TournamentsPanel.go_to_first_location(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp)
    bp.sleep(0.2)

    # 得到期望奖励
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    current_rewards_quantity_list = BattlePreparePanel.get_current_rewards_quantity_list(bp)
    current_rewards_dict = resource.make_item_dict(item_icon_list=current_rewards_icon_list, item_quantity_list=current_rewards_quantity_list)

    # 计算期望库存
    stock_icon_list = list(current_rewards_dict)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=stock_icon_list)
    cur = 0
    while cur < len(stock_icon_list):
        stock_expect_list[cur] += current_rewards_dict[stock_icon_list[cur]]
        cur += 1


    # 点击领奖
    BattlePreparePanel.click_btn_close(bp)
    bp.sleep(0.2)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(current_rewards_dict, reward_dict)

    # 计算库存是否正确
    stock_list = bp.get_item_count_list(item_icon_name_list=stock_icon_list)
    compare(stock_expect_list, stock_list)

    # 关闭恭喜获得
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(0.2)

    # 查看面板是否改为完成状态
    if not BattlePreparePanel.is_progress_finish(bp):
        raise FindNoElementError
    BattlePreparePanel.click_progress_info(bp)
    bp.sleep(0.2)
    if not ProgressRewardsPanel.is_progress_finish(bp):
        raise FindNoElementError
    ProgressRewardsPanel.click_btn_close(bp)





def progressRewards_test(bp: BasePage):
    # 进入渔场
    bp.lua_console('PanelMgr:OpenPanel("TournamentsPanel")')
    bp.sleep(0.2)
    TournamentsPanel.go_to_first_location(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp)
    bp.sleep(0.2)

    # 领取下一项奖励的测试
    collect_next_test(bp)

    # mini板的测试
    mini_panel_test(bp)

    # 完成进度条测试
    complete_test(bp)

if __name__ == '__main__':
    bp = BasePage()
    progressRewards_test(bp)