from common import gameInit

from common.basePage import BasePage
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.homePanel import HomePanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *




def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    bp.click_position([0, 0])

    # 推荐切换
    recommend_test(bp)

    # 跳转
    HomePanel.Minitask.click_btn_go(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 推荐切换
    recommend_test(bp)

    BattlePreparePanel.Minitask.click_btn_gift(bp)

    # 钓一次鱼
    battleTest.fish_once(bp, fishery_id="400301", fish_id="301013", is_quick=True)

    # 推荐切换
    text_task_1 = recommend_test(bp)

    # 领取奖励
    BattlePreparePanel.Minitask.click_btn_claim(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    # 看任务是否切换
    text_task_0 = recommend_test(bp)
    if text_task_0 == text_task_1:
        bp.debug_log(text_task_0)
        raise SameError

    # 回大厅
    bp.go_home()

    # 领取奖励
    HomePanel.Minitask.click_btn_claim(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)


    # 升级测试
    bp.cmd_list(["missiondone 10", "add 1 100200 123456"])
    bp.sleep(1)

    # 领取跳转应该不在主界面了
    HomePanel.Minitask.click_btn_claim(bp)
    bp.sleep(1)
    if HomePanel.is_panel_active(bp):
        raise FindElementError

    # 回到主界面
    bp.go_home()

    # 去渔场
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.go_to_fishery_by_index(bp, 0)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 领取跳转应该不在备战界面了
    BattlePreparePanel.Minitask.click_btn_claim(bp)
    bp.sleep(1)
    if BattlePreparePanel.is_panel_active(bp):
        raise FindElementError

    # 回到主界面
    bp.go_home()




def recommend_test(bp: BasePage):
    # 主界面刷新任务
    if HomePanel.is_panel_active(bp):
        text_task_0 = HomePanel.Minitask.get_text_task(bp)
        HomePanel.Minitask.click_btn_recommend(bp)
        bp.sleep(1)
        text_task_1 = HomePanel.Minitask.get_text_task(bp)
        if text_task_0 == text_task_1:
            raise SameError
        return text_task_1

    # 备战界面刷新任务
    text_task_0 = BattlePreparePanel.Minitask.get_text_task(bp)
    BattlePreparePanel.Minitask.click_btn_recommend(bp)
    bp.sleep(1)
    text_task_1 = BattlePreparePanel.Minitask.get_text_task(bp)
    if text_task_0 == text_task_1:
        raise SameError
    return text_task_1

if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20012")
    main(bp)