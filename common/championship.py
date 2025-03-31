import traceback
from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll
from panelObjs.AquariumFishNewPanel import AquariumFishNewPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.ChampionshipInfoNewPanel import ChampionshipInfoNewPanel
from panelObjs.ChampionshipNewPanel import ChampionshipNewPanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.LoginPanel import LoginPanel
from panelObjs.TournamentsInfoPanel import TournamentsInfoPanel
from panelObjs.TournamentsPanel import TournamentsPanel
from scripts.battleTest import circulate_fish, fish_once
from scripts.duelTest import duel_once


def check_reward(bp, overflow_factor: float = 1):
    # 鱼情不管当前到没到积分
    if BattlePreparePanel.get_btn_icon_warning_position(bp):
        return False

    # 旧锦标赛待加入
    if BattlePreparePanel.panel_pve_prepare.is_wait_for_join(bp):
        return False

    if not BattlePreparePanel.panel_pve_prepare.click_btn_tournaments(bp):
        return True

    TournamentsInfoPanel.switch_tab(bp, index=2)
    bp.sleep(0.5)
    if not TournamentsInfoPanel.is_checked(bp):
        TournamentsInfoPanel.click_btn_close(bp)
        return False

    progress_cur, progress_max = TournamentsInfoPanel.get_progress(bp)
    if progress_cur > progress_max * overflow_factor:
        TournamentsInfoPanel.click_btn_close(bp)
        return True
    TournamentsInfoPanel.click_btn_close(bp)
    return False


def check_reward_new(bp, overflow_factor: float = 1):
    BattlePreparePanel.panel_MainStage_daily_prepare.click_btn_tournaments(bp)
    bp.sleep(1)

    # 还没打
    if ChampionshipNewPanel.is_progress_active(bp):
        ChampionshipNewPanel.click_btn_close(bp)
        return False

    # 已经打了
    if ChampionshipNewPanel.is_panel_active(bp):
        ChampionshipNewPanel.click_btn_close(bp)
        return True

    ChampionshipInfoNewPanel.switch_tab(bp, index=2)
    bp.sleep(1)
    if not ChampionshipInfoNewPanel.is_checked(bp):
        ChampionshipInfoNewPanel.click_btn_close(bp)
        return False

    progress_cur, progress_max = ChampionshipInfoNewPanel.get_progress(bp)
    if progress_cur > progress_max * overflow_factor:
        ChampionshipInfoNewPanel.click_btn_close(bp)
        return True
    ChampionshipInfoNewPanel.click_btn_close(bp)
    return False






def handle_game_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            print(e)
            bp = args[0]  # 假设第一个参数是 bp
            is_monitor = kwargs.get('is_monitor', True)  # 从 kwargs 获取 is_monitor 参数
            bp = gameInit.reset_bp(bp.dev, is_monitor=is_monitor)
            return bp
    return wrapper


# cost=1是x1, cost=2是x3, cost=3是x10
@handle_game_exception
def championship(bp,  times, index=None, fishery_id=None, energy_cost=50, is_monitor=True, overflow_factor: float = 1, is_treasure_map=False):
    """
        times (int) 钓几次
        fishery_id或index二选一，控制进入的渔场
        is_monitor (bool) 是否启动监视器报错自重启
        overflow_factor (float) 分数溢出多少后停止值大于等于1
    """
    gameInit.set_joystick(bp)
    bp.clear_popup()
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    if fishery_id:
        bp.go_to_fishery(fishery_id=fishery_id)
    else:
        tournaments_index_list = TournamentsPanel.get_tournaments_index_list(bp)
        if len(tournaments_index_list) < 1:
            entrance_index = 0
        elif len(tournaments_index_list) < 2:
            entrance_index = tournaments_index_list[0]
        else:
            entrance_index = tournaments_index_list[index]

        fishery_id_list = TournamentsPanel.get_fishery_tpid_list(bp)
        fishery_id = fishery_id_list[entrance_index]
        TournamentsPanel.go_to_fishery_by_id(bp, fishery_id=fishery_id)

    spot_id_list, is_in_double_week, is_new_plot = bp.get_spot_id_list(fishery_id=fishery_id)
    if energy_cost < 3:
        spot_id_index = 0
    elif energy_cost < 10:
        spot_id_index = 1
    else:
        spot_id_index = 2
    spot_id = spot_id_list[spot_id_index]
    lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id), source=0, isInDoubleWeek=is_in_double_week)
    bp.lua_console(lua_code)
    bp.sleep(0.5)
    BattlePreparePanel.wait_for_panel_appear(bp)

    if check_reward(bp, overflow_factor=overflow_factor):
        bp.go_home()
        return bp

    if is_treasure_map:
        BattlePreparePanel.panel_pve_prepare.try_go_to_treasure_map(bp, fishery_id=fishery_id)
        lua_code = csMsgAll.get_CSFishingSaveLimitedSpotEnergyCostIdMsg(chooseEnergyCostId=bp.energy_cost_to_id(energy_cost=energy_cost), newPlot=0)
        bp.lua_console(lua_code)
        bp.sleep(1)

    circulate_fish(bp, times=times, is_quick=False)

    while BattlePreparePanel.get_btn_icon_warning_position(bp):
        fish_once(bp, is_quick=False)

    bp.go_home()

    return bp

@handle_game_exception
def championship_new(bp: BasePage, spot_id, times, is_monitor=True, overflow_factor: float = 1, is_treasure_map=False, energy_cost=50):
    gameInit.set_joystick(bp)
    bp.clear_popup()
    bp.go_to_panel("HomePanelNew")
    bp.sleep(1)
    bp.go_to_spot(spot_id=spot_id)
    BattlePreparePanel.wait_for_panel_appear(bp)

    if check_reward_new(bp, overflow_factor=overflow_factor):
        bp.go_home()
        return bp

    if is_treasure_map:
        BattlePreparePanel.panel_MainStage_challenge_prepare.try_go_to_treasure_map(bp, spot_id=spot_id)
        lua_code = csMsgAll.get_CSFishingSaveLimitedSpotEnergyCostIdMsg(chooseEnergyCostId=bp.energy_cost_to_id(energy_cost=energy_cost), newPlot=1)
        bp.lua_console(lua_code)
        bp.sleep(1)

    BattlePreparePanel.panel_MainStage_daily_prepare.click_btn_btn_receive(bp)
    bp.sleep(1)
    circulate_fish(bp, times=times, is_quick=False)

    while BattlePreparePanel.get_btn_icon_warning_position(bp):
        fish_once(bp, is_quick=False)

    bp.go_home()
    return bp


def duel_with_fish(bp: BasePage):
    # 出售或放入
    while True:
        position_list = AquariumFishNewPanel.get_reddot_position_list(bp)
        if not position_list:
            break
        bp.click_position(position_list[0])
        bp.sleep(2)


def sell_and_put_fish(bp: BasePage):
    # 卖鱼
    AquariumFishNewPanel.switch_tab(bp, 0)
    bp.sleep(1)
    duel_with_fish(bp)

    # 放鱼
    AquariumFishNewPanel.switch_tab(bp, 1)
    bp.sleep(1)
    duel_with_fish(bp)


@handle_game_exception
def aquarium(bp: BasePage, is_monitor=True):
    bp.go_to_panel("AquariumFishNewPanel")

    bp.sleep(1)
    sell_and_put_fish(bp)

    # 切另一个
    AquariumFishNewPanel.click_btn_change(bp)
    bp.sleep(3)

    sell_and_put_fish(bp)

    bp.go_home()
    return bp


if __name__ == '__main__':
    serial_number = "127.0.0.1:21503"
    base_page = BasePage(serial_number=serial_number, is_mobile_device=True, is_monitor=True)
    print(serial_number)

    # 设置摇杆浮动
    gameInit.set_joystick(base_page)

    # 设定张力
    base_page.set_tension_default(tension_default=0.9)
    base_page.set_hook_progress(hook_progress=0.85)



    # 设定log输出
    # base_page.lua_console("DebugLog=true")
    # cur = 0
    # while cur < 2:
    #     duel_once(base_page, 0)
    #     cur += 1
    #     print(f"第{cur}次钓鱼")

    # 备战界面钓指定次数
    # circulate_fish(bp=base_page, is_quick=False, times=250)
    # while True:
    #     fish_once(bp=base_page, is_quick=False)
    #     base_page.go_to_panel("TournamentsPanel")
    #     base_page.sleep(1)
    #     base_page.go_to_fishery(fishery_id=400314)

    # base_page.sleep(3600)
    # aquarium(bp=base_page)
    # base_page.clear_popup()
    # 循环进行水族箱/新主线/旧主线 直到打满
    cur = 0
    while True:
        if cur > 10:
            base_page = aquarium(base_page, is_monitor=True)
            cur = 0
        base_page = championship_new(base_page, spot_id=10103, times=10, is_treasure_map=False)
        # base_page = championship(base_page, index=0, times=20, cost=2, overflow_factor=1, is_monitor=True)
        # # base_page.sleep(60)

        base_page = championship(base_page, times=20, index=0, energy_cost=1, is_treasure_map=False)
        base_page = championship(base_page, times=20, index=1, energy_cost=1, is_treasure_map=False)
        cur += 1

