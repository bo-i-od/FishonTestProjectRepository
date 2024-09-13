import random

from common import resource, gameInit
from panelObjs.playerLevelupPanel import PlayerLevelupPanel

from tools.commonTools import *
from common.basePage import BasePage
from panelObjs.newbieTaskPanel import NewbieTaskPanel
from panelObjs.partySalePanel import PartySalePanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.leaderBoardPanel import LeaderBoardPanel
from panelObjs.leaderBoardPopResultPanel import LeaderBoardPopResultPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel


def party_sale_test(bp: BasePage):
    # 打开付费页面
    NewbieTaskPanel.click_btn_sale(bp)
    bp.sleep(1)

    # 点击鱼竿进行预览后退出
    item_position_list = PartySalePanel.get_item_position_list(bp)
    bp.click_position(item_position_list[0], ignore_set={"PartySalePanel"})
    bp.sleep(1)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.sleep(1)

    # 点击道具图标
    item_icon_list = PartySalePanel.get_item_icon_list(bp)
    item_quantity_list = PartySalePanel.get_item_quantity_list(bp)
    r = random.randint(1, len(item_position_list) - 1)
    bp.click_position(item_position_list[r], ignore_set={"PartySalePanel"})
    bp.sleep(1)
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, item_icon_list[r])
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        compare(item_icon, item_icon_list[r])
    bp.click_position([0.5, 0.1], ignore_set={"PartySalePanel"})

    if not bp.is_pay:
        return

    # 之后需要补充装备的数量测试
    gear_icon = item_icon_list[0]
    gear_quantity = item_quantity_list[0]
    item_icon_list = item_icon_list[-(len(item_icon_list) - 1):]
    item_quantity_list = item_quantity_list[-(len(item_quantity_list) - 1):]
    item_dict = resource.make_item_dict(item_icon_list=item_icon_list, item_quantity_list=item_quantity_list)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)

    # 点卷数量
    cost_icon = PartySalePanel.get_cost_icon(bp)
    cost_quantity = PartySalePanel.get_cost_quantity(bp)
    cost_expect = bp.get_item_count(item_icon_name=cost_icon) - cost_quantity

    # 点击购买
    PartySalePanel.click_btn_buy(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_dict, reward_dict)
    cur = 0
    while cur < len(stock_expect_list):
        stock_expect_list[cur] += item_quantity_list[cur]
        cur += 1

    stock_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)
    print(stock_expect_list, stock_list)
    # compare_list(stock_expect_list, stock_list)

    # 对比点券数量变化
    cost = bp.get_item_count(item_icon_name=cost_icon)
    compare(cost_expect, cost)

    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)


def leaderboard_test(bp: BasePage):
    # 打开排行榜面板
    NewbieTaskPanel.click_btn_leaderboard(bp)
    bp.sleep(1)

    # 代币数量前后端一致
    coin_stock = bp.get_item_count(item_tpid="209012")
    coin = LeaderBoardPanel.get_coin(bp)
    compare(coin_stock, coin)

    # 开关tips
    LeaderBoardPanel.click_btn_i(bp)
    bp.sleep(1)
    LeaderBoardPanel.click_tap_to_close(bp)

    # # 得到排名奖励
    # rewards_icon_list = LeaderBoardPanel.get_rewards_icon_list(bp)
    # # rewards_quantity_list = LeaderBoardPanel.get_rewards_quantity_list(bp)
    # rewards_position_list = LeaderBoardPanel.get_rewards_position_list(bp)
    # # rewards_dict = resource.make_item_dict(item_icon_list=rewards_icon_list, item_quantity_list=rewards_quantity_list)
    #
    # # 点击图标
    # r = random.randint(0, len(rewards_position_list) - 1)
    # bp.click_position(rewards_position_list[r])
    # bp.sleep(1)
    # if ItemTipsPanel.is_panel_active(bp):
    #     item_icon = ItemTipsPanel.get_item_icon(bp)
    #     compare(rewards_icon_list[r], item_icon)
    # elif FishCardPackTipsPanel.is_panel_active(bp):
    #     item_icon = FishCardPackTipsPanel.get_item_icon(bp)
    #     compare(rewards_icon_list[r], item_icon)
    #     bp.click_position([0.5, 0.9])

    # # 得到前100奖励
    # top_100_rewards_icon_list = LeaderBoardPanel.get_top_100_rewards_icon_list(bp)
    # # top_100_rewards_quantity_list = LeaderBoardPanel.get_top_100_rewards_quantity_list(bp)
    # top_100_rewards_position_list = LeaderBoardPanel.get_top_100_rewards_position_list(bp)
    #
    # # 点击图标
    # r = random.randint(0, len(top_100_rewards_position_list) - 1)
    # bp.click_position(top_100_rewards_position_list[r])
    # bp.sleep(1)
    # if ItemTipsPanel.is_panel_active(bp):
    #     item_icon = ItemTipsPanel.get_item_icon(bp)
    #     compare(top_100_rewards_icon_list[r], item_icon)
    # elif FishCardPackTipsPanel.is_panel_active(bp):
    #     item_icon = FishCardPackTipsPanel.get_item_icon(bp)
    #     compare(top_100_rewards_icon_list[r], item_icon)
    #     bp.click_position([0.5, 0.9])
    LeaderBoardPanel.click_btn_close(bp)
    #
    # ranking = LeaderBoardPanel.get_ranking(bp)
    # if ranking <= 100:
    #     rewards_dict = resource.make_item_dict(item_icon_list=top_100_rewards_icon_list, item_quantity_list=top_100_rewards_quantity_list, item_dict=rewards_dict)
    # rewards_icon_list = list(rewards_dict)
    # stock_expect_list = bp.get_item_count_list(item_icon_name_list=rewards_icon_list)
    # cur = 0
    # while cur < len(stock_expect_list):
    #     stock_expect_list[cur] += rewards_dict[rewards_icon_list[cur]]
    #     cur += 1
    # print(stock_expect_list)
    # LeaderBoardPanel.click_btn_close(bp)
    # bp.sleep(1)
    # NewbieTaskPanel.click_btn_close(bp)
    #
    # # 领取奖励
    # LeaderBoardPopResultPanel.wait_for_LeaderBoardPopResultPanel(bp)
    # result_rewards_position_list = LeaderBoardPopResultPanel.get_reward_position_list(bp)
    # result_rewards_icon_list = LeaderBoardPopResultPanel.get_reward_icon_list(bp)
    # result_rewards_quantity_list = LeaderBoardPopResultPanel.get_reward_quantity_list(bp)
    # result_rewards_dict = resource.make_item_dict(item_icon_list=result_rewards_icon_list, item_quantity_list=result_rewards_quantity_list)
    # compare_dict(rewards_dict, result_rewards_dict)
    # r = random.randint(0, len(result_rewards_position_list) - 1)
    # bp.click_position(result_rewards_position_list[r])
    # bp.sleep(1)
    # if ItemTipsPanel.is_panel_active(bp):
    #     item_icon = ItemTipsPanel.get_item_icon(bp)
    #     compare(result_rewards_icon_list[r], item_icon)
    #     bp.click_position([0.5, 0.9])
    # elif FishCardPackTipsPanel.is_panel_active(bp):
    #     item_icon = FishCardPackTipsPanel.get_item_icon(bp)
    #     compare(result_rewards_icon_list[r], item_icon)
    #     bp.click_position([0.5, 0.9])
    # LeaderBoardPopResultPanel.click_btn_claim(bp)
    # stock_list = bp.get_item_count_list(item_icon_name_list=list(rewards_dict))
    # compare_list(stock_expect_list, stock_list)

# 锁定应该无法跳转和领取
def locked_test(bp: BasePage):
    task_id_list = NewbieTaskPanel.get_task_id_list(bp)
    task_status = NewbieTaskPanel.get_task_status(bp, task_id_list)
    go_list = task_status[1]
    collect_list = task_status[2]

    if go_list:
        raise FindElementError
    if collect_list:
        raise FindElementError
    if task_status[3]:
        raise FindElementError


def go_test(bp: BasePage):
    task_id_list = NewbieTaskPanel.get_task_id_list(bp)
    task_status = NewbieTaskPanel.get_task_status(bp, task_id_list)
    task_viewport = NewbieTaskPanel.get_task_viewport(bp, task_id_list)

    lock_list = task_status[0]
    go_list = task_status[1]
    # 第一天不应该存在未解锁
    if lock_list:
        raise FindElementError


    # 随机选取一个可跳转的任务
    r = random.randint(0, len(go_list) - 1)
    task_id = go_list[r]

    # 移动到可点击范围 点击go按钮
    task_viewport.move_until_appear(target_id=task_id)
    btn_go_position = NewbieTaskPanel.get_task_position_list(bp, task_id_list=[task_id])[0]
    bp.click_position(btn_go_position)
    bp.sleep(1)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)
    bp.go_to_panel("NewbieTaskPanel")



def collect_test(bp:BasePage):
    task_id_list = NewbieTaskPanel.get_task_id_list(bp)
    task_status = NewbieTaskPanel.get_task_status(bp, task_id_list)
    task_viewport = NewbieTaskPanel.get_task_viewport(bp, task_id_list)
    lock_list = task_status[0]
    collect_list = task_status[2]
    if lock_list:
        raise FindElementError

    r = random.randint(0, len(collect_list) - 1)
    task_id = collect_list[r]

    # 代币数量前后端一致
    NewbieTaskPanel.get_coin(bp)

    # 计算预期库存
    task_reward_dict = NewbieTaskPanel.get_task_reward_dict_list(bp, task_id_list=[task_id])[0]
    task_reward_icon_list = list(task_reward_dict)
    # 将活动代币图标转换的tpid替换为209012
    task_reward_tpid_list = bp.get_tpid_list(item_icon_name_list=task_reward_icon_list)
    cur = 0
    while cur < len(task_reward_tpid_list):
        item_tpid_list = bp.get_item_tpid_list(icon=task_reward_icon_list[cur])
        if 209012 not in item_tpid_list:
            task_reward_tpid_list[cur] = task_reward_tpid_list[cur]
            cur += 1
            continue
        task_reward_tpid_list[cur] = "209012"
        cur += 1


    stock_expect_list = bp.get_item_count_list(item_tpid_list=task_reward_tpid_list)
    cur = 0
    while cur < len(stock_expect_list):
        stock_expect_list[cur] += task_reward_dict[task_reward_icon_list[cur]]
        cur += 1

    # 移动到可点击范围 点击claim按钮
    task_viewport.move_until_appear(target_id=task_id)
    btn_claim_position = NewbieTaskPanel.get_task_position_list(bp, task_id_list=[task_id])[0]
    bp.click_position(btn_claim_position)
    bp.sleep(1)

    # 代币数量前后端一致
    NewbieTaskPanel.get_coin(bp)

    # 对照奖励
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(task_reward_dict, reward_dict)

    # 关闭恭喜获得
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 对照库存
    stock_list = bp.get_item_count_list(item_tpid_list=task_reward_tpid_list)
    compare_list(stock_expect_list, stock_list)

    # 检测状态改变
    task_status = NewbieTaskPanel.get_task_status(bp, task_id_list)
    completed_list = task_status[3]
    if task_id not in completed_list:
        raise FindNoElementError

def progress_test(bp:BasePage):
    # 让刚好有三个奖励可领取
    bp.set_item_count(target_count=3000, item_tpid="209012")

    # 拿到除鱼竿外的奖励及数量
    reward_status = NewbieTaskPanel.get_progress_reward_status(bp)
    collectable_list = reward_status[1]
    progress_reward_icon_list = NewbieTaskPanel.get_progress_reward_icon_list(bp, progress_reward_id_list=collectable_list)
    progress_reward_quantity_list = NewbieTaskPanel.get_progress_reward_quantity_list(bp, progress_reward_id_list=collectable_list)
    progress_reward_position_list = NewbieTaskPanel.get_progress_reward_position_list(bp, progress_reward_id_list=collectable_list)
    item_dict = resource.make_item_dict(item_icon_list=progress_reward_icon_list, item_quantity_list=progress_reward_quantity_list)
    rod_icon = ""
    for item in item_dict:
        if "rod" in item:
            rod_icon = item
    if rod_icon in item_dict:
        item_dict.pop(rod_icon)

    # 拿到库存
    item_icon_list = list(item_dict)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)
    cur = 0
    while cur < len(stock_expect_list):
        stock_expect_list[cur] += item_dict[item_icon_list[cur]]
        cur += 1

    # 随机点击奖励位置进行领取
    r = random.randint(0, len(progress_reward_position_list) - 1)
    bp.click_position(progress_reward_position_list[r])
    bp.sleep(1)

    # 对照奖励数量
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_dict, reward_dict)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 对照库存
    stock_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)
    compare_list(stock_expect_list, stock_list)

    # 对照领取状态
    reward_status = NewbieTaskPanel.get_progress_reward_status(bp)
    collected_list = reward_status[2]
    compare_list(collectable_list, collected_list)

    # 点击图标
    locked_list = reward_status[0]
    progress_reward_icon_list = NewbieTaskPanel.get_progress_reward_icon_list(bp, progress_reward_id_list=locked_list)
    progress_reward_position_list = NewbieTaskPanel.get_progress_reward_position_list(bp, progress_reward_id_list=locked_list)
    progress_reward_viewport = NewbieTaskPanel.get_progress_reward_viewport(bp, progress_reward_id_list=locked_list)
    r = random.randint(0, len(progress_reward_position_list) - 1)
    reward_icon = progress_reward_icon_list[r]
    progress_reward_viewport.move_until_appear(target_id=locked_list[r])
    bp.sleep(1)
    bp.click_position(progress_reward_position_list[r])
    bp.sleep(1)
    if 'rod' in reward_icon:
        BaitAndRodShowPanel.click_tap_to_continue(bp)
    elif ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon)
        bp.click_position([0.5, 0.9])
        bp.sleep(1)
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon)
        bp.click_position([0.5, 0.9])
        bp.sleep(1)

    # 让刚好无法领取大奖
    max_reward_threshold = NewbieTaskPanel.get_max_reward_threshold(bp)
    bp.set_item_count(target_count=max_reward_threshold - 1, item_tpid="209012")
    bp.sleep(1)
    bp.click_position(progress_reward_position_list[r])
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 只领取大奖
    # 求期望大奖数量和库存
    bp.set_item_count(target_count=max_reward_threshold, item_tpid="209012")
    max_reward_icon = NewbieTaskPanel.get_max_reward_icon(bp)
    max_reward_quantity = NewbieTaskPanel.get_max_reward_quantity(bp)
    item_dict = resource.make_item_dict(item_icon_list=[max_reward_icon], item_quantity_list=[max_reward_quantity])
    stock_expect = bp.get_item_count(item_icon_name=max_reward_icon) + max_reward_quantity

    # 点击领取
    max_reward_position = NewbieTaskPanel.get_max_reward_position(bp)
    bp.click_position(max_reward_position)
    bp.sleep(1)

    # 对照奖励
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare(item_dict, reward_dict)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 对照库存
    stock = bp.get_item_count(item_icon_name=max_reward_icon)
    compare(stock_expect, stock)


def challenge_test(bp:BasePage):
    NewbieTaskPanel.switch_tab(bp, 4)
    bp.sleep(1)

    # # 随机选择go fishing跳转
    # challenge_id_list = NewbieTaskPanel.get_challenge_id_list(bp)
    # challenge_viewport = NewbieTaskPanel.get_challenge_viewport(bp, challenge_id_list=challenge_id_list)
    # r = random.randint(0, len(challenge_id_list) - 1)
    # challenge_viewport.move_until_appear(target_id=challenge_id_list[r])
    # btn_go_position_list = NewbieTaskPanel.get_challenge_position_list(bp, challenge_id_list=[challenge_id_list[r]])
    # btn_go_position = btn_go_position_list[0]
    # bp.click_position(btn_go_position)
    # bp.sleep(1)
    # LoadingFisheryPanel.wait_until_panel_disappear(bp)
    # # battleTest.fish_once(bp, fishery_id="400301", fish_id="301013")
    # # battleTest.fish_once(bp, fishery_id="400301", fish_id="301012")
    # # battleTest.fish_once(bp, fishery_id="400301", fish_id="301010")
    #
    # # 返回挑战页面
    # bp.go_to_panel("NewbieTaskPanel")
    # bp.sleep(1)
    # NewbieTaskPanel.switch_tab(bp, 5)
    # bp.sleep(1)
    #
    # # 记录币数量
    # challenge_id_list = NewbieTaskPanel.get_challenge_id_list(bp)
    # challenge_point_list = NewbieTaskPanel.get_challenge_point_list(bp, challenge_id_list)
    # challenge_viewport = NewbieTaskPanel.get_challenge_viewport(bp, challenge_id_list=challenge_id_list)
    #
    # cur = 0
    # while cur < len(challenge_id_list):
    #     if challenge_point_list[cur] == 0:
    #         cur += 1
    #         continue
    #     coin_expect = NewbieTaskPanel.get_coin(bp) + challenge_point_list[cur]
    #     challenge_viewport.move_until_appear(target_id=challenge_id_list[r])
    #     btn_point_position = NewbieTaskPanel.get_challenge_position_list(bp, challenge_id_list=[challenge_id_list[r]])[0]
    #     bp.click_position(btn_point_position)
    #     bp.sleep(1)
    #     coin = NewbieTaskPanel.get_coin(bp)
    #     compare(coin_expect, coin)
    #     cur += 1

def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "add 1 101900 10000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # # 去新手三天界面
    bp.go_to_panel("NewbieTaskPanel")

    bp.sleep(1)

    # 派对礼包测试
    party_sale_test(bp)


    # 排行榜测试
    leaderboard_test(bp)

    # 锁定状态测试
    NewbieTaskPanel.switch_tab(bp, 1)
    bp.sleep(1)
    locked_test(bp)
    NewbieTaskPanel.switch_tab(bp, 2)
    bp.sleep(1)
    locked_test(bp)
    NewbieTaskPanel.switch_tab(bp, 3)
    bp.sleep(1)
    locked_test(bp)

    # 升级重进界面
    bp.cmd("levelupto 31")
    bp.go_home()
    bp.go_to_panel("NewbieTaskPanel")

    # 跳转测试
    NewbieTaskPanel.switch_tab(bp, 0)
    bp.sleep(1)
    go_test(bp)
    NewbieTaskPanel.switch_tab(bp, 2)
    bp.sleep(1)
    go_test(bp)
    NewbieTaskPanel.switch_tab(bp, 3)
    bp.sleep(1)
    go_test(bp)

    bp.go_home()
    bp.cmd("missiondone 22")
    bp.go_to_panel("NewbieTaskPanel")

    # 领取测试
    NewbieTaskPanel.switch_tab(bp, 0)
    bp.sleep(1)
    collect_test(bp)
    NewbieTaskPanel.switch_tab(bp, 2)
    bp.sleep(1)
    collect_test(bp)
    NewbieTaskPanel.switch_tab(bp, 3)
    bp.sleep(1)
    collect_test(bp)

    # 挑战测试
    challenge_test(bp)

    # 进度条测试
    progress_test(bp)

    # 返回大厅界面
    bp.go_home()

if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=False)
    main(bp)
    bp.connect_close()

