import time
import traceback

from common import gameInit
from panelObjs.battlePanel import BattlePanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.playerInfoPanel import PlayerInfoPanel
from panelObjs.playerSettingPanel import PlayerSettingPanel
from panelObjs.loginPanel import LoginPanel
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest
from configs.elementsData import ElementsData
import json

from scripts.duelTest import clear_duelcup, random_duelcup


def logout(bp:BasePage):
    while not HomePanel.is_panel_active(bp):
        pass
    HomePanel.go_to_panel(bp, "PlayerInfoPanel")
    PlayerInfoPanel.click_btn_setting(bp)
    bp.sleep(1)
    # PlayerSettingPanel.click_tab_settings(bp)


    # if FisheryGiftPackPanel.is_panel_active(bp):
    #     FisheryGiftPackPanel.click_btn_close(bp)
    PlayerInfoPanel.click_btn_logout(bp)

def login(bp:BasePage, name:str):
    # name = name + str(index)
    while not LoginPanel.is_panel_active(bp):
        pass
    LoginPanel.set_login_name(bp, name)
    LoginPanel.click_btn_login(bp)
    bp.sleep(3)
    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    while not PlayerEditNamePanel.is_panel_active(bp):
        bp.sleep(1)
    bp.cmd("guideskip")
    PlayerEditNamePanel.set_player_name(bp, name)

    bp.sleep(1)
    PlayerEditNamePanel.click_confirm(bp)

def go_leaderborad(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.click_btn_leaderboard(bp)
    bp.sleep(1)




def fish(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    TournamentsPanel.go_to_first_location(bp)
    battleTest.fish_once(bp, fishery_id="400301", fish_id="301001")
    bp.go_home()

def tournament(bp:BasePage):
    bp.sleep(3)
    bp.click_position([0.5, 0.5])
    HomePanel.go_to_panel(bp, "TournamentsPanel")
    bp.cmd("add 1 100200 1234567")
    bp.sleep(1)
    TournamentsPanel.go_to_fishery_by_index(bp, 0)
    bp.clear_popup()
    battleTest.circulate_fish(bp)
    BattlePreparePanel.click_btn_close(bp)
    TournamentsPanel.go_to_fishery_by_index(bp, 1)
    bp.clear_popup()
    battleTest.circulate_fish(bp)
    bp.sleep(1)
    bp.go_home()

def ndays(bp:BasePage, count):
    # bp.cmd(f"setPlayerLayer {count}000")
    bp.cmd("levelupto 30")
    # bp.cmd(f"add 1 101200 {count}")
    # bp.cmd(f"add 2 209017 {2 * count}")
    bp.cmd(f"monopolyscore {count}")
    # bp.cmd(f"add 2 209002 {count}")
    # bp.cmd(f"add 2 209006 {count}")
    # bp.cmd(f"add 2 209008 {count}")
    # bp.cmd(f"add 2 209010 {count}")

def clone(bp:BasePage, name):
    bp.sleep(2)
    bp.clear_popup()
    cmd = f"clone {name}"
    print(cmd)
    bp.cmd(cmd)



def main(bp):
    cur = 109
    limit = 160
    while cur < limit:
        name = "monopoly" + str(cur)
        login(bp, name)
        bp.sleep(2)
        bp.clear_popup()
        # go_leaderborad(bp)
        bp.go_home()
        # fish(bp)
        ndays(bp, limit - cur)
        logout(bp)
        cur += 1




def main2(column_data):
    cur = 62
    retry_times = 0
    while cur < len(column_data):
        if retry_times > 2:
            retry_times = 0
            cur += 1
            continue

        # 重启
        bp = gameInit.restart_to_login("com.xuejing.smallfish.official")
        try:
            get_player_data(bp, cur, column_data)
        except:
            retry_times += 1
            continue
        retry_times = 0
        cur += 1






def get_player_data(bp:BasePage, index, column_data):

    name = column_data[index]
    login(bp, str(name), index)
    # fish(bp)
    bp.sleep(2)
    bp.clear_popup()
    level = HomePanel.get_level(bp)
    rating = HomePanel.get_rating(bp)
    points, weight = logout(bp, index)
    res = {"level": level, "rating": rating, "points": points, "weight": weight}
    with open('C:/Users/TU/Desktop/log.txt', 'a') as f:
        # 使用write()函数追加内容
        r = f"当前序号{index}" + "id:"+ f"{name}" + f"--{res}"
        print(r)
        f.write(r)
        f.close()

def read_data():
    res = []
    with open('C:/Users/TU/Desktop/log.txt', 'r') as f:
        data_all = f.read()
        f.close()
        data_list = data_all.split("当前序号")
        for data in data_list:
            a = data.split("--")
            if len(a) > 1:
                res.append(a[1])
    cur = 0
    l = len(res)
    while cur < l - 1:
        j = 0
        while j < l - cur - 1:
            json_object_0 = json.loads(res[j].replace("'", "\""))
            json_object_1 = json.loads(res[j + 1].replace("'", "\""))
            if int(json_object_0["level"]) > int(json_object_1["level"]):
                temp = res[j]
                res[j] = res[j + 1]
                res[j + 1] = temp
            j += 1
        cur += 1
    cur = 0
    while cur < len(res):
        print(res[cur])
        cur += 1

if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20230")
    # worksheet = bp.excelTools.get_worksheet(book_name="玩家信息采样.xlsx", sheet_name="Sheet1")
    # column_data = []
    # # 第六行开始
    # b = 3
    # column_index = 3
    # while worksheet.cell(b, 2).value is not None:
    #     index = column_index - 1
    #     column_data.append(worksheet.cell(b, column_index).value)
    #     b += 1
    # # auto_export()
    # # time.sleep(100)
    main(bp)
    # pass