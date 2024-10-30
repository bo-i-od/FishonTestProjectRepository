import traceback
from common import gameInit
from common.basePage import BasePage
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts.battleTest import circulate_fish
from scripts.duelTest import duel_once


def get_bp(dev):
    bp = gameInit.restart_to_login(dev, package_list=["com.xuejing.smallfish.official", "com.arkgame.fishingmaster"])
    if not LoginPanel.is_panel_active(bp):
        return bp
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


def championship(bp, index, times):
    try:
        gameInit.set_joystick(bp)
        bp.clear_popup()
        bp.go_to_panel("TournamentsPanel")
        bp.sleep(1)
        while True:
            tournaments_info_position_list = TournamentsPanel.get_tournaments_info_position_list(bp)
            if not tournaments_info_position_list:
                break
            if len(tournaments_info_position_list) < 2:
                index = 0
            bp.click_position(tournaments_info_position_list[index])
            bp.sleep(0.5)
        circulate_fish(bp, times=times, is_quick=False)
        bp.go_home()
    except Exception as e:
        print(e)
        # bp.connect_close()
        bp = reset_bp(bp.dev)
    return bp


if __name__ == '__main__':
    serial_number = "127.0.0.1:21503"
    base_page = BasePage(serial_number=serial_number, is_mobile_device=True)
    print(serial_number)
    base_page.set_send_log_flag(False)
    gameInit.set_joystick(base_page)
    base_page.custom_cmd("setTension 0.95")
    # cur = 0
    # while cur < 5:
    #     duel_once(base_page, 0)
    #     cur += 1
    #     print(f"第{cur}次钓鱼")
    # circulate_fish(bp=base_page, is_quick=False, times=30)
    while True:
        base_page = championship(base_page, 0, 20)
        # base_page.sleep(60)
        base_page = championship(base_page, 1, 20)
        # base_page.sleep(60)