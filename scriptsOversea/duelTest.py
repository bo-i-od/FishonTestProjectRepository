import ast
import random
import re
import traceback
from threading import Thread

from pywinauto import keyboard

import common
from common import gameInit
from common.basePage import BasePage
from common.error import FindNoElementError
from netMsg import luaLog
from panelObjs.CommonWebViewPanel import CommonWebViewPanel
from panelObjs.DivisionLeaderboardPanel import DivisionLeaderboardPanel
from panelObjs.DivisionListPanel import DivisionListPanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.MessageBoxPanel import MessageBoxPanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from panelObjs.PVPBattleHUDPanel import PVPBattleHUDPanel
from panelObjs.PVPHallPanel import PVPHallPanel
from panelObjs.HomePanel import HomePanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.PVPMatchPanel import PVPMatchPanel
from panelObjs.PVPResultPanel import PVPResultPanel
from panelObjs.BattlePanel import BattlePanel
from panelObjs.PVPRoomPanel import PVPRoomPanel
from panelObjs.ResultPanel import ResultPanel
from panelObjs.PlayerEditNamePanel import PlayerEditNamePanel
from panelObjs.LoginPanel import LoginPanel
from panelObjs.BattleFailedPanel import BattleFailedPanel
from panelObjs.RoulettePanel import RoulettePanel
from panelObjs.TournamentsPanel import TournamentsPanel
from scripts import battleTest, createUsers
from scripts.battleTest import circulate_fish


# 0-7分别对应 0新手 1青铜 2白银 3黄金 4白金 5钻石 6冠军 7传奇
def set_duelcup_random(bp: BasePage, rank):
    duelcup = random.randint(0, 5)
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


def set_duelcup(bp: BasePage, duelcup):
    if duelcup <= 5:
        bp.cmd(f"duelcup 1001 {duelcup}")
        return
    bp.cmd(f"duelcup 1001 {5}")

    if duelcup <= 25:
        bp.cmd(f"duelcup 1002 {duelcup - 5}")
        return
    bp.cmd(f"duelcup 1002 {20}")

    if duelcup <= 105:
        bp.cmd(f"duelcup 1003 {duelcup - 25}")
        return
    bp.cmd(f"duelcup 1003 {80}")

    if duelcup <= 265:
        bp.cmd(f"duelcup 1004 {duelcup - 105}")
        return
    bp.cmd(f"duelcup 1004 {160}")

    if duelcup <= 745:
        bp.cmd(f"duelcup 1005 {duelcup - 265}")
        return
    bp.cmd(f"duelcup 1005 {480}")

    if duelcup <= 1705:
        bp.cmd(f"duelcup 1006 {duelcup - 745}")
        return
    bp.cmd(f"duelcup 1006 {960}")

    if duelcup <= 3625:
        bp.cmd(f"duelcup 1007 {duelcup - 1705}")
        return
    bp.cmd(f"duelcup 1007 {1920}")
    bp.cmd(f"duelcup 1008 {duelcup - 3625}")


def clear_duelcup(bp: BasePage):
    cur = 0
    while cur < 8:
        bp.cmd(f"duelcup 100{8 - cur} 0")
        cur += 1


def get_toDrops(bp, is_print_id=True):
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    bp.cmd("duel queryFish")
    bp.sleep(1)
    # 提取hook消息
    target_log = bp.get_target_log(msg_key="SCGmCommandMsg")
    if is_print_id:
        fishBalanceTpId = luaLog.get_value(msg=target_log, key="fishBalanceTpId", is_str=False)
        print(fishBalanceTpId)
    output_match = re.search(r'toDrops=(\[.*?\])', target_log)
    if not output_match:
        bp.log_list_flag = False
        return
    output_str = output_match.group(1)
    # 使用ast.literal_eval将字符串转换为列表
    output_list = ast.literal_eval(output_str)
    print(f"预期体型列表：{output_list}")
    bp.log_list_flag = False


def pvp_fish(bp, is_quick=False):
    tpid_list = []
    while not BattlePreparePanel.is_panel_active(bp):
        bp.sleep(1)
    # 获取掉落列表
    get_toDrops(bp, is_print_id=True)

    while True:
        # try:
        #     emoji(bp)
        # except:
        #     pass
        BattlePreparePanel.click_btn_cast(bp)
        # get_toDrops(bp, is_print_id=False)
        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True
        bp.sleep(3)
        if PVPResultPanel.is_panel_active(bp):
            bp.log_list_flag = False
            print(f"出鱼列表：{tpid_list}")
            fish_type_list = bp.get_fish_type_list(fish_list=tpid_list)
            print(f"体型列表：{fish_type_list}")
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
        # try:
        #     emoji(bp)
        # except:
        #     pass
        element_btn = ResultPanel.wait_for_result(bp)
        bp.sleep(1)
        ResultPanel.automatic_settlement(bp, element_btn)

        # 提取hook消息
        target_log = bp.get_target_log(msg_key="SCFishingHookMsg")
        tpid = luaLog.get_value(msg=target_log, key="tpId", is_str=False)
        tpid_list.append(tpid)

        bp.log_list_flag = False
        if PVPResultPanel.is_panel_active(bp):
            print(f"出鱼列表：{tpid_list}")
            fish_type_list = bp.get_fish_type_list(fish_list=tpid_list)
            print(f"体型列表：{fish_type_list}")
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
    ResultPanel.click_btn_claim_pvp(bp)


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


def duel_once(bp: BasePage, rank):
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


def division_test(bp: BasePage):
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


def duel_once_friend(bp: BasePage, is_quick=False):
    while PVPRoomPanel.is_panel_active(bp):
        PVPRoomPanel.click_btn_start(bp)
        bp.sleep(2)
    pvp_fish(bp, is_quick=is_quick)
    bp.sleep(5)
    PVPResultPanel.click_tap_to_click(bp)
    bp.sleep(1)


def emoji(bp: BasePage):
    PVPBattleHUDPanel.wait_for_btn_chat_appear(bp)
    PVPBattleHUDPanel.click_btn_chat(bp)
    bp.sleep(1)
    emoji_position_list = PVPBattleHUDPanel.get_emoji_position_list(bp)
    r = random.randint(0, len(emoji_position_list) - 1)
    bp.click_position(emoji_position_list[r])
    bp.sleep(1)


def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "levelupto 56"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 将所有对决解锁
    set_duelcup_random(bp, 7)

    # division面板测试
    division_test(bp)

    # 进入对决大厅
    bp.go_to_panel("PVPHallPanel")

    r = random.randint(0, 7)
    bp.debug_log(f"点击第{r}个对决")
    # 战斗
    PVPHallPanel.click_btn_play(bp, r)

    # 取消对决
    PVPMatchPanel.wait_for_panel_appear(bp)
    PVPMatchPanel.click_btn_cancel(bp)
    PVPHallPanel.wait_for_panel_appear(bp)
    r = random.randint(0, 7)
    bp.debug_log(f"点击第{r}个对决")
    PVPHallPanel.click_btn_play(bp, r)

    # 随机点击表情
    emoji(bp)

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

    # 正常对决
    r = random.randint(0, 7)
    bp.debug_log(f"点击第{r}个对决")
    PVPHallPanel.click_btn_play(bp, r)
    pvp_fish(bp)
    bp.sleep(2)
    PVPResultPanel.click_btn_open(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)

    bp.go_home()


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533", is_mobile_device=False)
    main(bp)
    bp.connect_close()









