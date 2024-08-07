import random
import traceback
from threading import Thread

import common
from common import gameInit
from common.basePage import BasePage
from common.error import FindNoElementError
from panelObjs.commonWebViewPanel import CommonWebViewPanel
from panelObjs.divisionLeaderboardPanel import DivisionLeaderboardPanel
from panelObjs.divisionListPanel import DivisionListPanel
from panelObjs.loadingFisheryPanel import LoadingFisheryPanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.pvpBattleHUDPanel import PVPBattleHUDPanel
from panelObjs.pvpHallPanel import PVPHallPanel
from panelObjs.homePanel import HomePanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.pvpMatchPanel import PVPMatchPanel
from panelObjs.pvpResultPanel import PVPResultPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.playerSettingPanel import PlayerSettingPanel
from panelObjs.loginPanel import LoginPanel
from panelObjs.battleFailedPanel import BattleFailedPanel
from panelObjs.roulettePanel import RoulettePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest, createUsers
from scripts.battleTest import circulate_fish

# 0-7分别对应 0新手 1青铜 2白银 3黄金 4白金 5钻石 6冠军 7传奇
def random_duelcup(bp:BasePage, rank):
    duelcup = random.randint(0,5)
    bp.cmd(f"duelcup 1001 {duelcup}")
    duelcup_all = duelcup
    if rank > 0:
        bp.cmd(f"duelcup 1001 {5}")
        duelcup_all = 5
        duelcup = random.randint(15 - duelcup_all, 20)
        bp.cmd(f"duelcup 1002 {duelcup}")
        duelcup_all += duelcup
    if rank > 1:
        duelcup = random.randint(80 - duelcup_all, 80)
        bp.cmd(f"duelcup 1003 {duelcup}")
        duelcup_all += duelcup
    if rank > 2:
        duelcup = random.randint(200 - duelcup_all, 160)
        bp.cmd(f"duelcup 1004 {duelcup}")
        duelcup_all += duelcup
    if rank > 3:
        duelcup = random.randint(600 - duelcup_all, 480)
        bp.cmd(f"duelcup 1005 {duelcup}")
        duelcup_all += duelcup
    if rank > 4:
        duelcup = random.randint(1200 - duelcup_all, 960)
        bp.cmd(f"duelcup 1006 {duelcup}")
        duelcup_all += duelcup
    if rank > 5:
        duelcup = random.randint(2100 - duelcup_all, 1920)
        bp.cmd(f"duelcup 1007 {duelcup}")
        duelcup_all += duelcup
    if rank > 6:
        duelcup = random.randint(0, 3000)
        bp.cmd(f"duelcup 1008 {duelcup}")
        duelcup_all += duelcup
    return duelcup_all


def clear_duelcup(bp:BasePage):
    cur = 0
    while cur < 8:
        bp.cmd(f"duelcup 100{8-cur} 0")
        cur += 1

def pvp_fish(bp, is_quick=False):
    while True:
        BattlePreparePanel.click_btn_cast(bp)
        bp.sleep(3)
        if PVPResultPanel.is_panel_active(bp):
            bp.sleep(3)
            break
        BattlePanel.hook(bp)
        bp.sleep(1)
        if BattlePanel.is_reel_active(bp):
            bp.custom_cmd("autofish")
            qteThread = Thread(target=BattlePanel.qte, args=[bp])
            qteThread.start()
        if is_quick:
            BattlePanel.reel_quick(bp)
        element_btn = ResultPanel.wait_for_result(bp)
        ResultPanel.automatic_settlement(bp, element_btn)
        if PVPResultPanel.is_panel_active(bp):
            bp.sleep(3)
            break

def fish_once(bp: BasePage):
    BattlePreparePanel.click_btn_quick_switch(bp)
    BattlePreparePanel.click_rod_model(bp)
    bp.sleep(1)
    location = BattlePreparePanel.get_location(bp)
    print(location)
    BattlePreparePanel.click_btn_apply(bp)
    bp.sleep(1)
    BattlePreparePanel.click_btn_cast(bp)
    bp.sleep(15)
    BattleFailedPanel.click_cast_again(bp)
    bp.sleep(1)
    BattlePreparePanel.click_btn_cast(bp)
    bp.sleep(15)
    BattleFailedPanel.click_cast_again(bp)
    bp.sleep(1)
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.reel_quick(bp)
    ResultPanel.wait_for_result(bp)
    bp.sleep(130)
    ResultPanel.click_btn_claim(bp)


def wait_for_ResultPanel(bp):
    while not PVPResultPanel.is_panel_active(bp):
        bp.sleep(1)


def point_cal(duelcup):
    if duelcup < 15:
        start = 20 * duelcup + 300
        end = 30 * duelcup + 400
        return int(start), int(end)
    if duelcup < 150:
        start = 3 * duelcup + 500
        end = 5 * duelcup + 700
        return int(start), int(end)
    if duelcup < 300:
        start = 3 * duelcup + 700
        end = 5 * duelcup + 900
        return int(start), int(end)
    if duelcup < 600:
        start = 2 * duelcup + 1300
        end = 4 * duelcup + 1600
        return int(start), int(end)
    if duelcup < 2100:
        start = duelcup + 1300
        end = duelcup + 2500
        return int(start), int(end)
    if duelcup < 4000:
        start = 0.5 * duelcup + 2000
        end = 0.5 * duelcup + 2800
        return int(start), int(end)
    start = 0.2 * duelcup + 2800
    end = 0.2 * duelcup + 3600
    return int(start), int(end)

def duel_once(bp:BasePage, rank):
    # rank = random.randint(4, 5)
    # # rank = 0
    # clear_duelcup(bp)
    # random_duelcup(bp, rank)
    # rank = 0
    # print(rank)
    # bp.set_item_count(target_count=250000, item_tpid="100200")
    PVPHallPanel.click_btn_play(bp, rank)
    # s, e = point_cal(dc)
    # print(f"当前杯数：{dc},预期分数范围:{s,e}")
    # action_list = [lambda: PVPHallPanel.click_btn_close(bp)]
    # bp.try_actions(action_list=action_list)
    # action_list = [
    #     lambda: bp.go_to_panel("PVPHallPanel"),
    #     lambda: PVPHallPanel.click_btn_play(bp, rank)]
    # bp.try_actions(action_list=action_list)
    pvp_fish(bp)
    bp.sleep(5)
    # PVPResultPanel.click_btn_open(bp)
    # bp.sleep(1)
    # result_right = PVPResultPanel.get_result_right(bp)
    # print("钓了：",len(result_right),"条鱼")
    # print(result_right)
    # img = bp.get_full_screen_shot()
    # bp.save_img(img)

    # points_enemy = PVPResultPanel.get_points_enemy(bp)
    # points_mine = PVPResultPanel.get_points_mine(bp)
    PVPResultPanel.click_tap_to_click(bp)
    bp.sleep(1)
    # print(f"玩家分数：{points_mine}，机器人分数：{points_enemy}")
    # n = "符合预期"
    # if points_enemy < s or points_enemy > e:
    #     n = "不符合预期"
    # print(f"{points_enemy},{n}")

def get_pd(rank):
    if rank < 1:
        return 0.8
    if rank < 4:
        return 0.7
    if rank < 6:
        return 0.65
    if rank < 7:
        return 0.6
    return 0.55

def get_k(r0):
    if r0 < 2000:
        return 32
    if r0 < 2400:
        return 112 - 0.04 * r0
    return 16

def get_bp(dev):
    bp = gameInit.restart_to_login(dev,"com.xuejing.smallfish.official")
    bp.sleep(7)
    LoginPanel.wait_for_btn_login(bp)
    LoginPanel.click_btn_login(bp)
    bp.sleep(2)
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)
    bp.sleep(5)
    return bp

def reset_bp(dev):
    try:
        bp = get_bp(dev)
    except:
        traceback.print_exc()
        bp = reset_bp(dev)
    return bp

def champointship(bp, index, times):
    try:
        gameInit.set_joystick(bp)
        bp.clear_popup()
        bp.go_to_panel("TournamentsPanel")
        bp.sleep(1)

        # if not tournaments_info_position_list:
        #     raise FindNoElementError

        while True:
            tournaments_info_position_list = TournamentsPanel.get_tournaments_info_position_list(bp)
            if not tournaments_info_position_list:
                break
            if len(tournaments_info_position_list) < 2:
                index = 0
            bp.click_position(tournaments_info_position_list[index])
            bp.sleep(0.5)
        # LoadingFisheryPanel.wait_until_panel_disappear(bp)
        circulate_fish(bp, times=times, is_quick=False)
        bp.go_home()
    except Exception as e:
        print(e)
        # bp.connect_close()
        bp = reset_bp(bp.dev)
    return bp

def division_test(bp:BasePage):
    # 进排行榜
    bp.go_to_panel("PVPHallPanel")
    bp.sleep(1)
    PVPHallPanel.click_btn_leaderboard(bp)
    bp.sleep(1)

    # 切到传奇排行榜
    DivisionLeaderboardPanel.switch_tab(bp, 1)
    bp.sleep(1)

    # 切到传奇排行榜
    DivisionLeaderboardPanel.switch_tab(bp, 0)
    bp.sleep(1)

    # 所有段位
    DivisionLeaderboardPanel.click_btn_alldivisions(bp)
    bp.sleep(1)
    DivisionListPanel.click_btn_close(bp)
    bp.sleep(1)

    # 返回主界面
    bp.go_home()



def main(bp:BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "levelupto 56"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 将所有对决解锁
    random_duelcup(bp, 7)

    # division面板测试
    division_test(bp)

    # 进入对决大厅
    bp.go_to_panel("PVPHallPanel")

    r = random.randint(0, 7)
    bp.debug_log(r)
    # 战斗
    PVPHallPanel.click_btn_play(bp, r)

    # 取消对决
    PVPMatchPanel.wait_for_panel_appear(bp)
    PVPMatchPanel.click_btn_cancel(bp)
    PVPHallPanel.wait_for_panel_appear(bp)
    r = random.randint(0, 7)
    bp.debug_log(r)
    PVPHallPanel.click_btn_play(bp, r)

    # 随机点击表情
    PVPBattleHUDPanel.wait_for_btn_chat_appear(bp)
    PVPBattleHUDPanel.click_btn_chat(bp)
    bp.sleep(1)
    emoji_position_list = PVPBattleHUDPanel.get_emoji_position_list(bp)
    r = random.randint(0, len(emoji_position_list) - 1)
    bp.click_position(emoji_position_list[r])
    bp.sleep(1)

    # 点击投降
    PVPBattleHUDPanel.wait_for_btn_chat_appear(bp)
    PVPBattleHUDPanel.click_btn_chat(bp)
    bp.sleep(1)
    PVPBattleHUDPanel.click_btn_surrender(bp)
    bp.sleep(1)
    MessageBoxPanel.click_btn_confirm(bp)

    # 打开战绩
    bp.sleep(3)
    PVPResultPanel.click_btn_open(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)
    bp.sleep(1)

    r = random.randint(0, 7)
    bp.debug_log(r)
    PVPHallPanel.click_btn_play(bp, r)
    pvp_fish(bp)
    bp.sleep(2)
    PVPResultPanel.click_btn_open(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)

    bp.go_home()






if __name__ == '__main__':
    base_page = BasePage("127.0.0.1:21533")
    base_page.set_send_log_flag(False)
    # cur = 0
    # while cur < 3:
    #     duel_once(base_page, 1)
    #     cur += 1
    #     print(f"第{cur}次钓鱼")
    # circulate_fish(base_page, is_quick=False, times=90)
    while True:
        base_page = champointship(base_page, 1, 15)
        base_page = champointship(base_page, 0, 15)

    # clear_duelcup(base_page)
    # while True:
    #     base_page.go_home()
    #     # r = random.randint(0, 7)
    #     r = 0
    #     print(r)
    #     clear_duelcup(base_page)
    #     dc = random_duelcup(base_page, rank=r)
    #     base_page.go_to_panel("PVPHallPanel")
    #     base_page.sleep(1)
    #     duel_once(base_page, r)






    #
    # dc = random_duelcup(base_page, 7)

    # main(bp)

    # circulate_fish(bp, fishery_id="400301",is_quick=True, is_monster=True)
    # zhanbao_test(bp)
    # bp.set_item_count(target_count=10000, item_tpid="100500")
    # # bp.set_item_count(target_count=25000000, item_tpid="100200")
    # createUsers.main(bp)
    # clear_duelcup(bp)
    # bp.cmd("mode 400302 390015")
    # bp.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
    # bp.cmd("mode 400303 390025")
    # base_page.cmd("levelupto 56")
    # dc = random_duelcup(base_page, 7)
    # print(dc)
    # area = point_cal(210)
    # bp.cmd("duelcup 1008 27000")
    # print(f"当前杯数:{0}，分数范围:{area}")
    # bp.cmd("add 5 500021 1")

    # PlayerEditNamePanel.click_confirm(bp)
    # bp.sleep(3)
    # bp.go_to_panel("PVPHallPanel")
    # bp.cmd("autofish")
    # common.gameInit.set_joystick(bp)
    # while True:
    #     battleTest.tournament(bp)
    # bp.set_item_count(target_count=72000,item_tpid="209013")




    # # rank = random.randint(0, 7)
    # print(dc)




