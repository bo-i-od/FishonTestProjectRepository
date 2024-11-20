import traceback
from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel
from panelObjs.tournamentsInfoPanel import TournamentsInfoPanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts.battleTest import circulate_fish, fish_once
from scripts.duelTest import duel_once


def check_reward(bp, overflow_factor: float = 1):
    BattlePreparePanel.wait_for_panel_appear(bp)

    # 鱼情不管当前到没到积分
    if BattlePreparePanel.get_btn_icon_warning_position(bp):
        return False

    if BattlePreparePanel.is_wait_for_join(bp):
        return False
    if not BattlePreparePanel.click_btn_tournaments(bp):
        return True

    TournamentsInfoPanel.switch_tab(bp, 2)
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


# cost=1是x1, cost=2是x3, cost=3是x10
def championship(bp, index, times, cost=1, is_monitor=False, overflow_factor: float = 1):
    try:
        gameInit.set_joystick(bp)
        bp.clear_popup()
        bp.go_to_panel("TournamentsPanel")
        bp.sleep(1)

        tournaments_index_list = TournamentsPanel.get_tournaments_index_list(bp)

        if len(tournaments_index_list) < 1:
            entrance_index = 0
        elif len(tournaments_index_list) < 2:
            entrance_index = tournaments_index_list[0]
        else:
            entrance_index = tournaments_index_list[index]
        fishery_id_list = TournamentsPanel.get_fishery_tpid_list(bp)
        fishery_id = fishery_id_list[entrance_index]
        TournamentsPanel.go_to_fishery_by_index(bp, index=entrance_index)

        spot_id_list, is_in_double_week = bp.get_spot_id_list(fishery_id=fishery_id)
        if cost < 1:
            cost = 1
        if cost > 4:
            cost = 1
        spot_id = spot_id_list[cost - 1]
        lua_code = csMsgAll.get_CSFishingSaveFishSpotMsg(fishSpotId=int(spot_id), fishSceneTpId=int(fishery_id), source=0, isInDoubleWeek=is_in_double_week)
        bp.lua_console(lua_code)
        bp.sleep(0.5)

        if check_reward(bp, overflow_factor=overflow_factor):
            bp.go_home()
            return bp

        circulate_fish(bp, times=times, is_quick=False)

        while BattlePreparePanel.get_btn_icon_warning_position(bp):
            fish_once(bp, is_quick=False)

        bp.go_home()
    except Exception as e:
        print(e)
        # bp.connect_close()
        bp = gameInit.reset_bp(bp.dev, is_monitor=is_monitor)
    return bp


if __name__ == '__main__':
    serial_number = "127.0.0.1:21503"
    base_page = BasePage(serial_number=serial_number, is_mobile_device=False, is_monitor=True)
    print(serial_number)
    # base_page.set_send_log_flag(False)
    gameInit.set_joystick(base_page)
    base_page.custom_cmd("setTension 0.95")
    # cur = 0
    # while cur < 5:
    #     duel_once(base_page, 0)
    #     cur += 1
    #     print(f"第{cur}次钓鱼")
    # circulate_fish(bp=base_page, is_quick=False, times=30)
    # base_page.sleep(3600)
    while True:
        base_page = championship(base_page, 0, 5, cost=2, overflow_factor=1, is_monitor=True)
        # base_page.sleep(60)
        base_page = championship(base_page, 1, 5, cost=1, overflow_factor=1, is_monitor=True)
        # base_page.sleep(60)