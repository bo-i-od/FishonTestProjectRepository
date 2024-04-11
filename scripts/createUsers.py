from panelObjs.battlePanel import BattlePanel
from panelObjs.playerSettingPanel import PlayerSettingPanel
from panelObjs.loginPanel import LoginPanel
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest


def logout(bp:BasePage, index):
    while not HomePanel.is_panel_active(bp):
        pass
    HomePanel.go_to_panel(bp, "PlayerSettingPanel")
    PlayerSettingPanel.click_tab_settings(bp)
    if index > 0:
        bp.sleep(0.5)
    # c = f"add 1 100200 12345678"
    # bp.cmd(c)

    # if FisheryGiftPackPanel.is_panel_active(bp):
    #     FisheryGiftPackPanel.click_btn_close(bp)
    PlayerSettingPanel.click_btn_logout(bp)

def login(bp:BasePage, name:str, index):
    name = name + str(index)
    while not LoginPanel.is_panel_active(bp):
        pass
    LoginPanel.set_login_name(bp, name)
    LoginPanel.click_btn_login(bp)
    # bp.sleep(3)
    # while not PlayerEditNamePanel.is_panel_active(bp):
    #     pass
    # PlayerEditNamePanel.set_player_name(bp, name)
    # bp.cmd("guideskip")
    # bp.sleep(1)
    # PlayerEditNamePanel.click_confirm(bp)



def fish(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    TournamentsPanel.go_to_first_location(bp)
    battleTest.fish_once(bp, fishery_id="400301", fish_id="301001")
    bp.go_home()

def action(bp:BasePage, index):
    bp.sleep(3)
    bp.click_position([0.5, 0.5])
    count = 0
    if index < 40:
        count = 40 - index
    # bp.cmd(f"add 2 209012 {count}")
    bp.cmd(f"add 1 100200 123456")
    bp.sleep(1)
    # count = 40 - index
    bp.cmd(f"add 2 209002 {count}")
    bp.cmd(f"add 2 209010 {count * 2}")



if __name__ == '__main__':
    bp = BasePage()

    cur = 2
    while cur < 50:
        name = f"x0"
        login(bp, name, cur)
        # fish(bp)
        action(bp, cur)
        logout(bp, cur)
        cur += 1