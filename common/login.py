from panelObjs.entryUpdateLoadind import EntryUpdateLoading
from panelObjs.loginPanel import LoginPanel
from panelObjs.homePanel import HomePanel
from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
import time
from tools.commonTools import *
import random


def login(bp: BasePage, username):
    if not LoginPanel.is_panel_active(bp):
        EntryUpdateLoading.wait_for_EntryUpdateLoading(bp)
    # 在登录界面出现前，点击tap to start
    while not LoginPanel.is_panel_active(bp):
        EntryUpdateLoading.click_tap_to_start(bp)
    LoginPanel.set_login_name(bp,username)
    # 选服务器
    LoginPanel.set_server(bp, 1)
    LoginPanel.click_btn_login(bp)


def account_init(bp: BasePage, player_name, cmd_list):
    while not PlayerEditNamePanel.is_panel_active(bp):
        bp.sleep(0.1)
    PlayerEditNamePanel.set_player_name(bp, player_name)
    for cmd in cmd_list:
        bp.cmd(cmd)

    PlayerEditNamePanel.click_confirm(bp)
    bp.sleep(1)

def login_to_hall(bp: BasePage, cmd_list):
    if HomePanel.is_panel_active(bp):
        for cmd in cmd_list:
            bp.cmd(cmd)
        return
    username = str(time.time()).split('.')[0]
    login(bp, username)
    account_init(bp, username, cmd_list)
    bp.sleep(4)





if __name__ == '__main__':
    bp = BasePage()
    cmd_l = ["guideskip", "add 1 100200 100000"]
    login_to_hall(bp, cmd_l)



