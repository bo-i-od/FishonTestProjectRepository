from panelObjs.playerSettingPanel import PlayerSettingPanel
from panelObjs.loginPanel import LoginPanel
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel

def logout(bp:BasePage, index):
    while not HomePanel.is_panel_active(bp):
        pass
    HomePanel.go_to_PlayerSettingPanel(bp)
    PlayerSettingPanel.click_tab_settings(bp)
    if index > 0:
        count = int(600 - index)
        c = f"add 1 101200 {count}"
        bp.cmd(c)
        bp.sleep(0.5)
    print(index)
    # if FisheryGiftPackPanel.is_panel_active(bp):
    #     FisheryGiftPackPanel.click_btn_close(bp)
    PlayerSettingPanel.click_btn_logout(bp)

def login(bp:BasePage, name:str, index):
    name = name + str(index)
    while not LoginPanel.is_panel_active(bp):
        pass
    LoginPanel.set_login_name(bp, name)
    LoginPanel.click_btn_login(bp)
    bp.sleep(3)
    while not PlayerEditNamePanel.is_panel_active(bp):
        pass
    PlayerEditNamePanel.set_player_name(bp, name)
    bp.cmd("guideskip")
    bp.sleep(1)
    PlayerEditNamePanel.click_confirm(bp)





if __name__ == '__main__':
    bp = BasePage()
    cur = 551
    while cur <= 600:
        name = f"dr0"
        login(bp, name, cur)
        logout(bp, cur)
        cur += 1
