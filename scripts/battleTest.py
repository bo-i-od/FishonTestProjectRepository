import time

from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll, fishingMsg
from netMsg.luaLog import get_value

from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.FlashCardReceivePanel import FlashCardReceivePanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.LoginPanel import LoginPanel
from panelObjs.ResultPanel import ResultPanel
from panelObjs.BattlePanel import BattlePanel
from threading import Thread
from panelObjs.TournamentsPanel import TournamentsPanel



def fish_once(bp: BasePage, fish_id="", is_quick=False):
    bp.set_time_scale()
    if fish_id != "":
        fishery_id = bp.fish_id_to_fishery_id(fish_id=fish_id)
        c = f"mode {fishery_id} {fish_id}"
        print(c)
        bp.cmd(c)
    BattlePreparePanel.click_btn_cast(bp)
    if bp.is_monitor:
        bp.monitor.add_task("schedule_next_check", cur=0)
    BattlePanel.hook(bp)
    start_time = time.time()

    bp.set_time_scale()
    if BattlePanel.is_reel_active(bp):
        bp.custom_cmd("autofish")
        # qteThread = Thread(target=BattlePanel.qte, args=[bp])
        # qteThread.start()
    if is_quick:
        reel_quick_thread = Thread(target=BattlePanel.reel_quick, args=[bp])
        reel_quick_thread.start()
    BattlePanel.qte(bp, start_time=start_time)

    # BattlePanel.reel_quick(bp)
    # bp.set_time_scale()
    # element_btn = ResultPanel.wait_for_result(bp)
    # ResultPanel.automatic_settlement(bp, element_btn=element_btn)

    if fish_id != "":
        bp.cmd("mode 0 0")

# mode=0是超距失败
# mode!=0是超张力失败
def fail_once(bp: BasePage, fishery_id="", fish_id="", mode=0):
    bp.set_time_scale()
    if fish_id != "":
        c = f"mode {fishery_id} {fish_id}"
        print(c)
        bp.cmd(c)
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    if mode != 0:
        BattlePanel.hold_btn_reel(bp)
    bp.set_time_scale()
    element_btn = ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp, element_btn=element_btn)

    if fish_id != "":
        bp.cmd("mode 0 0")


def circulate_fish(bp: BasePage, fishery_id=None, is_quick=False, times=500, start=0):
    fish_list = []
    cur = start
    if fishery_id is not None:
        fish_list = bp.get_fish_id_list(fishery_id)
        times = len(fish_list)
    while cur < times:
        # go_to_treasure_map(bp, fishery_id="400306", is_double_week=True, is_in_double_week=True)
        fish_id = ""
        # 指定鱼
        if fish_list:
            fish_id = fish_list[cur]
            if fish_id == "0" or fish_id == 0:
                cur += 1
                continue
        # bp.sleep(1)
        bp.clear_popup()
        # if cur == 1:
        #     select_rod(bp, 3)
        # if cur == 5:
        #     select_rod(bp, 3)
        # if cur == 9:
        #     select_rod(bp, 2)
        fish_once(bp, fish_id=fish_id, is_quick=is_quick)
        # print(f"第{cur}次钓鱼")
        cur += 1


def select_rod(bp: BasePage, index):
    BattlePreparePanel.click_gears(bp)
    bp.sleep(1)
    rod_position_list = BattlePreparePanel.get_rod_position_list(bp)
    bp.click_position(rod_position_list[index - 1])
    bp.sleep(1)
    BattlePreparePanel.click_btn_apply(bp)
    bp.sleep(1)


def select_location(bp: BasePage, index):
    BattlePreparePanel.click_btn_location(bp)
    bp.sleep(1)
    # BattlePreparePanel


def fish_all(bp: BasePage, is_quick=False):
    fishery_id_list = bp.get_fishery_id_list()
    cur = 1
    while cur < len(fishery_id_list):
        fishery_id = fishery_id_list[cur]
        bp.go_to_panel("TournamentsPanel")
        TournamentsPanel.go_to_fishery_by_tpid(bp, fishery_id)
        circulate_fish(bp, fishery_id=fishery_id, is_quick=is_quick)
        cur += 1


def tournament(bp: BasePage):
    bp.go_home()
    bp.go_to_panel("TournamentsPanel")
    TournamentsPanel.go_to_fishery_by_index(bp, 0)
    circulate_fish(bp, is_quick=False, times=10)
    bp.go_home()
    bp.go_to_panel("TournamentsPanel")
    TournamentsPanel.go_to_fishery_by_index(bp, 1)
    circulate_fish(bp, is_quick=False, times=18)


def fishery_to_spot(fishery_id, is_gold, is_double_week):
    fishery_id = str(fishery_id)
    if is_double_week:
        spot_id = fishery_id + "1"
    else:
        spot_id = fishery_id + "0"

    if is_gold:
        # 黄金钓点
        spot_id = spot_id + "4"
    else:
        # 普通x10钓点
        spot_id = spot_id + "3"
    return spot_id


def go_to_treasure_map(bp, fishery_id, is_double_week, is_in_double_week):
    if BattlePreparePanel.get_value_cost(bp) > 10:
        return
    if BattlePreparePanel.is_panel_tip_location_active(bp):
        spot_id = fishery_to_spot(fishery_id, is_gold=True, is_double_week=is_double_week)
        lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id),
                                                         source=0, isInDoubleWeek=is_double_week)
        bp.lua_console(lua_code)
        bp.sleep(1)
        return
    fish_once(bp, fish_id="399001", is_quick=True)
    spot_id = fishery_to_spot(fishery_id, is_gold=True, is_double_week=is_double_week)
    lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id), source=0, isInDoubleWeek=is_in_double_week)
    bp.lua_console(lua_code)
    bp.sleep(1)


def leave_treasure_map(bp, fishery_id, is_double_week, is_in_double_week):
    if BattlePreparePanel.get_value_cost(bp) < 20:
        return
    spot_id = fishery_to_spot(fishery_id, is_gold=False, is_double_week=is_double_week)
    lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id), source=0,
                                                     isInDoubleWeek=is_in_double_week)
    bp.lua_console(lua_code)
    bp.sleep(1)


def goldfish_all(bp: BasePage, fishery_id, is_double_week=False, is_in_double_week=False):
    fish_list = bp.get_fish_id_list(fishery_id)
    cur = 0
    while cur < len(fish_list):
        # 藏宝图消失就钓藏宝图
        go_to_treasure_map(bp, fishery_id=fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)
        fish_id = fish_list[cur]
        c = f"mode {fishery_id} {fish_id}"
        print(c)
        bp.cmd(c)
        BattlePreparePanel.click_btn_cast(bp)
        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True

        BattlePanel.hook(bp)
        if BattlePanel.is_reel_active(bp):
            bp.custom_cmd("autofish")
            qteThread = Thread(target=BattlePanel.qte, args=[bp])
            qteThread.start()
        BattlePanel.reel_quick(bp)
        element_btn = ResultPanel.wait_for_result(bp)
        bp.log_list_flag = False
        target_log = bp.get_target_log(msg_key="SCFishingHookMsg")
        color = get_value(msg=target_log, key="color", is_str=False)

        # 如果是黄金鱼就截图
        if color == "11":
            img = bp.get_full_screen_shot()
            bp.save_img(img)
            bp.sleep(1)
            cur += 1
        ResultPanel.automatic_settlement(bp, element_btn=element_btn)
        if fish_id != "":
            bp.cmd("mode 0 0")


def flashcard_all(bp: BasePage, fishery_id, is_double_week, is_in_double_week):
    # 不是双周渔场就不钓闪卡
    if not is_double_week:
        return
    fish_list = bp.get_fish_id_list(fishery_id)
    # bp.cur = 0
    # while bp.cur < len(fish_list):
    #     go_to_treasure_map(bp, fishery_id=fishery_id, is_double_week=True)
    #     fish_id = fish_list[bp.cur]
    #     fish_once(bp, fishery_id=fishery_id, fish_id=fish_id, is_quick=True)
    cur = 0
    while cur < len(fish_list):
        # 藏宝图消失就钓藏宝图
        go_to_treasure_map(bp, fishery_id=fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)
        fish_id = fish_list[cur]
        c = f"mode {fishery_id} {fish_id}"
        print(c)
        bp.cmd(c)
        BattlePreparePanel.click_btn_cast(bp)

        BattlePanel.hook(bp)
        if BattlePanel.is_reel_active(bp):
            bp.custom_cmd("autofish")
            qteThread = Thread(target=BattlePanel.qte, args=[bp])
            qteThread.start()
        while not ResultPanel.is_panel_active(bp):
            if FlashCardReceivePanel.is_panel_active(bp):
                bp.sleep(6)
                img = bp.get_full_screen_shot()
                bp.save_img(img)
                bp.clear_popup()
                cur += 1
            bp.lua_console(command="GameRoot:GetFishingMatch():GetPlayer().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            # bp.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            bp.sleep(1)
        element_btn = ResultPanel.wait_for_result(bp)
        ResultPanel.automatic_settlement(bp, element_btn=element_btn)
        if fish_id != "":
            bp.cmd("mode 0 0")


def fishbone_all(bp: BasePage, fishery_id, is_gold=False, is_double_week=False, is_in_double_week=False):
    if not is_gold:
        leave_treasure_map(bp, fishery_id=fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)
    spot_id = fishery_to_spot(fishery_id, is_gold, is_double_week)
    drop_item_id_list = bp.get_drop_item_id_list(spot_id)
    for drop_item_id in drop_item_id_list:
        drop_item_id = str(drop_item_id)
        # 跳过藏宝图
        if drop_item_id == "399001":
            continue
        # 黄金钓点
        if is_gold:
            go_to_treasure_map(bp, fishery_id=fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)
        fish_once(bp, fish_id=drop_item_id, is_quick=True)
        bp.sleep(3)
        btn_icon_warning_position = BattlePreparePanel.get_btn_icon_warning_position(bp)[0]
        bp.click_position(btn_icon_warning_position)

        bp.sleep(1)
        img = bp.get_full_screen_shot()
        bp.save_img(img)
        fish_id = bp.fish_bone_id_to_fish_id(fish_bone_id=drop_item_id)
        fish_once(bp, fish_id=fish_id, is_quick=True)


def fail_all(bp: BasePage, fishery_id, is_gold=False, is_double_week=False, is_in_double_week=False):
    if not is_gold:
        leave_treasure_map(bp, fishery_id=fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)
    fish_id_list = bp.get_fish_id_list(fishery_id)
    fishery_id = str(fishery_id)
    cur = 0
    while cur < len(fish_id_list):
        fish_id = str(fish_id_list[cur])
        if fish_id[:3] == fishery_id[-3:]:
            cur += 1
            continue
        # 黄金钓点
        if not is_gold:
            # 触发失败鱼情
            fail_once(bp, fishery_id=fishery_id, fish_id=fish_id)

            # 点击图标截图
            bp.sleep(3)
            btn_icon_warning_position = BattlePreparePanel.get_btn_icon_warning_position(bp)[0]
            bp.click_position(btn_icon_warning_position)
            bp.sleep(1)
            img = bp.get_full_screen_shot()
            bp.save_img(img)

            # 钓上来
            fish_once(bp, fish_id=fish_id, is_quick=True)
            cur += 1
            continue

        # 黄金鱼情
        go_to_treasure_map(bp, fishery_id=fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)

        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True

        # 拉断线
        bp.set_time_scale()
        if fish_id != "":
            c = f"mode {fishery_id} {fish_id}"
            print(c)
            bp.cmd(c)
        BattlePreparePanel.click_btn_cast(bp)
        bp.sleep(1)
        bp.log_list_flag = False
        target_log = bp.get_target_log(msg_key="SCFishingCastMsg")
        color = get_value(msg=target_log, key="color", is_str=False)
        BattlePanel.hook(bp)
        # 如果不是黄金鱼就不要
        if color != "11":
            if BattlePanel.is_reel_active(bp):
                bp.custom_cmd("autofish")
                qteThread = Thread(target=BattlePanel.qte, args=[bp])
                qteThread.start()
            BattlePanel.reel_quick(bp)
            bp.set_time_scale()
            element_btn = ResultPanel.wait_for_result(bp)
            ResultPanel.automatic_settlement(bp, element_btn=element_btn)
            continue
        # 是黄金鱼就拉断线
        bp.set_time_scale()
        element_btn = ResultPanel.wait_for_result(bp)
        ResultPanel.automatic_settlement(bp, element_btn=element_btn)

        # 点击图标截图
        bp.sleep(3)
        btn_icon_warning_position = BattlePreparePanel.get_btn_icon_warning_position(bp)[0]
        bp.click_position(btn_icon_warning_position)
        bp.sleep(1)
        img = bp.get_full_screen_shot()
        bp.save_img(img)

        # 钓上来
        fish_once(bp, fish_id=fish_id, is_quick=True)
        cur += 1

# 体感抛竿
def vibration_cast(bp: BasePage):
    spot_id = "40030101"
    scene_id = spot_id[:6]
    rod_id = fishingMsg.get_rod_id(scene_id)
    otherArgMap103 = spot_id[len(spot_id) - 2]
    csMsgAll.get_CSFishingCastMsg()
    lua_code = ('local cmd = NetworkMgr:NewMsg("CSFishingCastMsg")\n'
                'local equipMap =NetworkMgr:NewMsg("SCFishEquip")\n'
                f'equipMap.rodTpId={rod_id}\n'
                'cmd.equip = equipMap\n'
                'cmd.castGType = 0\n'
                f'cmd.sceneArg1 = {scene_id}\n'
                f'local otherArgMap = {{[101] = 0, [102] = {spot_id}, [103]={otherArgMap103}}}\n'
                'cmd.otherArgMap = otherArgMap\n'
                'cmd.sceneType = 1\n'
                'cmd.castG = 2000\n'
                'cmd.castGType = 0\n'
                'NetworkMgr:Send(cmd)'
                )
    bp.lua_console(lua_code)


# is_double_week 历史的双周渔场
# is_in_double_week 当前的双周渔场
def main(bp: BasePage, fishery_id, is_double_week=False, is_in_double_week=False):
    # # # 渔场全部闪卡
    # flashcard_all(bp, fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)

    # 渔场全部普通鱼骨
    fishbone_all(bp, fishery_id, is_gold=False, is_double_week=is_double_week, is_in_double_week=is_in_double_week)

    # 渔场全部失败鱼情
    fail_all(bp, fishery_id, is_gold=False, is_double_week=is_double_week, is_in_double_week=is_in_double_week)

    # 渔场全部黄金鱼骨
    fishbone_all(bp, fishery_id, is_gold=True, is_double_week=is_double_week, is_in_double_week=is_in_double_week)

    # 渔场全部黄金失败鱼情
    fail_all(bp, fishery_id, is_gold=True, is_double_week=is_double_week, is_in_double_week=is_in_double_week)

    # 渔场全部黄金鱼
    goldfish_all(bp, fishery_id, is_double_week=is_double_week, is_in_double_week=is_in_double_week)



if __name__ == '__main__':
    # 连接设备号为127.0.0.1:21533的设备
    bp = BasePage("127.0.0.1:21523", is_mobile_device=False)
    bp.is_time_scale = False
    gameInit.set_joystick(bp)
    bp.custom_cmd("setTension 0.9")

    fishbone_all(bp, fishery_id=400302, is_gold=True, is_double_week=True, is_in_double_week=False)

    # 断开连接
    bp.connect_close()








