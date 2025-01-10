import random
from common.basePage import BasePage
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.TournamentsPanel import TournamentsPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.ProgressRewardsPanel import ProgressRewardsPanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from common import resource, gameInit
from scripts import battleTest
from tools.commonTools import *

def collect_test(bp: BasePage):
    # 得到期望奖励图标
    next_reward_icon = BattlePreparePanel.get_next_reward_icon(bp)

    # 钓一条鱼
    battleTest.fish_once(bp, fish_id="390001", is_quick=True)

    bp.sleep(10)

    # 下一奖励应在奖励列表里
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)

    if next_reward_icon not in current_rewards_icon_list:
        raise FindNoElementError

    BattlePreparePanel.click_btn_close(bp)
    bp.sleep(1)

    # 把进度条设为马上可以领下几档奖励
    cmd_list = [f"progressSetPoint 100"]
    bp.cmd_list(cmd_list)
    TournamentsPanel.go_to_fishery_by_tpid(bp, "400301")
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)
    bp.sleep(1)

    # 计算期望库存
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    current_rewards_quantity_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    current_rewards_dict = resource.make_item_dict(item_icon_list=current_rewards_icon_list, item_quantity_list=current_rewards_quantity_list)
    rewards_icon_list = list(current_rewards_dict)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=rewards_icon_list)
    cur = 0
    while cur < len(rewards_icon_list):
        stock_expect_list[cur] += current_rewards_dict[rewards_icon_list[cur]]
        cur += 1

    # 领取奖励
    BattlePreparePanel.click_progress_info(bp)
    bp.sleep(1)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(current_rewards_dict, reward_dict)

    # 计算库存是否正确
    stock_list = bp.get_item_count_list(item_icon_name_list=rewards_icon_list)
    compare_list(stock_expect_list, stock_list)

    # 关闭恭喜获得
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)



def mini_panel_test(bp: BasePage):
    # 保证没有可领取的奖励
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    if current_rewards_icon_list:
        BattlePreparePanel.click_progress_info(bp)
        RewardsPanel.wait_for_panel_appear(bp)
        bp.sleep(1)
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(1)
    current_rewards_icon_list = BattlePreparePanel.get_current_rewards_icon_list(bp)
    if current_rewards_icon_list:
        raise FindElementError

    # 记录mini板信息
    progress_mini = BattlePreparePanel.get_progress(bp)
    icon_mini = BattlePreparePanel.get_next_reward_icon(bp)
    quantity_mini = BattlePreparePanel.get_next_reward_quantity(bp)

    # 打开面板
    BattlePreparePanel.click_progress_info(bp)

    # # 应该没有可领取奖励
    # current_rewards_icon_list = ProgressRewardsPanel.get_current_rewards_icon_list(bp)
    # if current_rewards_icon_list:
    #     raise FindElementError

    # 记录面板信息
    progress = ProgressRewardsPanel.get_progress(bp)
    icon = ProgressRewardsPanel.get_next_reward_icon(bp)
    quantity = ProgressRewardsPanel.get_next_reward_quantity(bp)

    # 看是否一致
    compare(progress_mini, progress)
    compare(icon_mini, icon)
    compare(quantity_mini, quantity)

    # 关闭tips
    ProgressRewardsPanel.click_btn_i(bp)

    # 点击图标
    next_reward_position = ProgressRewardsPanel.get_next_reward_position(bp)
    bp.click_position(next_reward_position)
    bp.sleep(1)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(icon, item_icon)
    bp.click_position([0.5, 0.9])

    # 关闭界面
    ProgressRewardsPanel.click_btn_close(bp)



def main(bp: BasePage):
    # 进入渔场
    # 登录到大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)


    TournamentsPanel.go_to_fishery_by_tpid(bp, "400301")
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)
    bp.sleep(1)

    # 领取下一项奖励的测试
    collect_test(bp)

    # mini板的测试
    mini_panel_test(bp)

    # 回到大厅
    bp.go_home()

if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=False)
    main(bp)
    bp.connect_close()
