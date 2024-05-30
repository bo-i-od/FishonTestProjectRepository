import random
import time
import traceback

from common import gameInit
from netMsg import csMsgAll, fishingMsg
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



def logout(bp:BasePage):
    # while not HomePanel.is_panel_active(bp):
    #     pass
    # HomePanel.go_to_panel(bp, "PlayerInfoPanel")
    PlayerInfoPanel.click_btn_setting(bp)
    bp.sleep(0.5)
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
    bp.sleep(2.5)
    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    while not PlayerEditNamePanel.is_panel_active(bp):
        bp.sleep(0.5)
    bp.cmd("guideskip")
    PlayerEditNamePanel.set_player_name(bp, name)

    bp.sleep(0.5)
    PlayerEditNamePanel.click_confirm(bp)

def go_leaderborad(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.click_btn_leaderboard(bp)
    bp.sleep(1)




def fish(bp:BasePage):
    pass
    # bp.cmd_list(["levelupto 20"])
    # bp.sleep(0.1)
    # fishingMsg.fish(bp, [{"spot_id": f"40030213", "times": 1, "energy_cost": 50}])
    # bp.sleep(0.1)
    # bp.cmd("mode 400302 390018")
    # fishingMsg.fish(bp, [{"spot_id": f"40030213", "times": 1, "energy_cost": 50}])
    # bp.sleep(0.1)
    # bp.cmd("mode 400302 390019")
    # fishingMsg.fish(bp, [{"spot_id": f"40030213", "times": 1, "energy_cost": 50}])
    # bp.sleep(0.1)


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

def hidden_treasure(bp:BasePage):
    bp.cmd_list([f"levelupto 20", "add 1 101500 20"])
    bp.sleep(0.2)
    dy = "{[1] = 1,}"
    dx = "{[1] = 1,}"
    lua_code = csMsgAll.get_CSHiddenTreasureDigMsg(digYs=dy, roomId=2000298, groupId=6000001, stageId=1, digXs=dx)
    print(lua_code)
    bp.lua_console(lua_code)


def ndays(bp:BasePage, count):
    # bp.cmd(f"setPlayerLayer {count}000")
    bp.cmd(f"levelupto 16")
    bp.sleep(0.1)
    guildSimpleId = 10000001
    lua_code = csMsgAll.get_CSGuildApplyMsg(source=0, guildSimpleId=guildSimpleId)
    bp.lua_console(lua_code)

    # bp.cmd_list([f"levelupto 20", "add 1 100100 2000"])
    # bp.sleep(0.2)
    # r = random.randint(4, 7)
    # lua_code = csMsgAll.get_CSGameGuildCreateMsg(flag=5, joinType=(count % 2 + 1), joinLv=(r * 5), color=3, name=f"club{count}", introduce="欢迎大家加入俱乐部，一起欢乐钓鱼吧！", pattern=1)
    # print(lua_code)
    # bp.lua_console(lua_code)


    # bp.cmd(f"add 1 100400 {count}")
    # bp.cmd(f"add 1 101200 {count}")
    # bp.cmd(f"monopolyscore {count}")
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
    cur = 1
    limit = 10
    while cur < limit:
        name = "qwe" + str(cur)
        login(bp, name)
        # bp.sleep(2)
        # bp.clear_popup()
        # go_leaderborad(bp)
        bp.lua_console('PanelMgr:OpenPanel("PlayerInfoPanel")')
        # bp.go_home()
        fish(bp)
        # hidden_treasure(bp)
        # ndays(bp, cur)
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
    bp = BasePage("192.168.111.80:20038")

    main(bp)
    bp.connect_close()


    # pass