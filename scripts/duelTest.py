import random
from common.basePage import BasePage
from panelObjs.pvpHallPanel import PVPHallPanel
from panelObjs.homePanel import HomePanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.pvpResultPanel import PVPResultPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.playerSettingPanel import PlayerSettingPanel
from panelObjs.loginPanel import LoginPanel
from panelObjs.battleFailedPanel import BattleFailedPanel
from configs.elementsData import ElementsData

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

def fish(bp):
    BattlePreparePanel.click_btn_quick_switch(bp)
    while True:
        BattlePreparePanel.click_btn_cast(bp)
        bp.sleep(3)
        if PVPResultPanel.is_panel_active(bp):
            bp.sleep(3)
            break
        # BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        ResultPanel.click_btn_claim(bp)
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

def circulate_duel(bp:BasePage):
    rank = random.randint(4, 5)
    # rank = 0
    clear_duelcup(bp)
    random_duelcup(bp, rank)
    bp.set_item_count(target_count=250000, item_tpid="100200")
    # s, e = point_cal(dc)
    # print(f"当前杯数：{dc},预期分数范围:{s,e}")
    action_list = [lambda: PVPHallPanel.click_btn_close(bp)]
    bp.try_actions(action_list=action_list)
    action_list = [
        lambda: bp.go_to_panel("PVPHallPanel"),
        lambda: PVPHallPanel.click_btn_play(bp, rank)]
    bp.try_actions(action_list=action_list)
    fish(bp)
    bp.sleep(2)
    # PVPResultPanel.click_btn_open(bp)
    img = bp.get_full_screen_shot()
    bp.save_img(img)
    bp.sleep(1)
    points_enemy = PVPResultPanel.get_points_enemy(bp)
    points_mine = PVPResultPanel.get_points_mine(bp)
    PVPResultPanel.click_tap_to_click(bp)
    print(f"玩家分数：{points_mine}，机器人分数：{points_enemy}")
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

def zhanbao_test(bp:BasePage):
    login_name = f"ms0{1}"
    while not LoginPanel.is_panel_active(bp):
        pass
    LoginPanel.set_login_name(bp, login_name=login_name)
    LoginPanel.click_btn_login(bp)
    bp.sleep(3)
    while not PlayerEditNamePanel.is_panel_active(bp):
        pass
    PlayerEditNamePanel.set_player_name(bp, login_name)
    bp.cmd("guideskip")
    bp.cmd("add 1 100200 50000")
    bp.sleep(1)
    PlayerEditNamePanel.click_confirm(bp)
    rank = 6
    clear_duelcup(bp)
    dc = random_duelcup(bp, rank)
    print(login_name, dc)
    bp.sleep(2)
    bp.lua_console('PanelMgr:OpenPanel("HomePanel")')
    action_list = [
        lambda: bp.go_to_panel("PVPHallPanel"),
        lambda:PVPHallPanel.click_btn_play(bp, rank)]
    bp.try_actions(action_list=action_list)
    fish(bp)
    bp.sleep(2)
    bp.get_full_screen_shot()
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)
    # PVPHallPanel.click_btn_close(bp)
    # HomePanel.go_to_PlayerSettingPanel(bp)
    # PlayerSettingPanel.click_tab_setting(bp)
    # PlayerSettingPanel.click_btn_logout(bp)


if __name__ == '__main__':
    bp = BasePage()
    # zhanbao_test(bp)
    # bp.set_item_count(target_count=250000, item_tpid="100200")
    bp.set_item_count(target_count=25000000, item_tpid="100200")
    clear_duelcup(bp)
    dc = random_duelcup(bp, 7)
    # print(dc)
    # area = point_cal(210)
    # bp.cmd("duelcup 1008 27000")
    # print(f"当前杯数:{0}，分数范围:{area}")
    # bp.cmd("add 5 500021 1")
    # bp.cmd("guideskip")
    # PlayerEditNamePanel.click_confirm(bp)
    # bp.sleep(3)
    # bp.go_to_panel("PVPHallPanel")
    # cur = 0
    # while cur < 2:
    #     circulate_duel(bp)
    #     cur += 1
    #     print(f"第{cur}次钓鱼")


    # # rank = random.randint(0, 7)
    # print(dc)




