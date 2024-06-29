from netMsg import csMsgAll, fishingMsg
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from scripts import battleTest
import json


def init(bp: BasePage):
    if LoginPanel.is_panel_active(bp):
        return
    logout(bp)


# def sdk(accountName):
#     response = requests.get(f'http://{ip}:{port_autosdk}/autoRegisterLogin?accountName={accountName}&password=123')
#     data = json.loads(response.text)
#     accountId = data["accountId"]
#     sessionId = data["sessionId"]
#     return accountId, sessionId

# _G.NetworkMgr.registerSDKRetInfo.accountId = "{accountId}"
# _G.NetworkMgr.registerSDKRetInfo.sessionId = "{token}"
# _G.NetworkMgr.registerSDKRetInfo.accountName = "{accountName}"
# local Login_Token_Key = "Login_Token"
# _G.SettingMgr:Write(Login_Token_Key, "{token}")
# _G.NetworkMgr:Connect("{ip}", {port}, function() _G.NetworkMgr:NetworkConnectCallback() end)

def connect(bp: BasePage, accountName):
    lua_code = f"""
_G.NetworkMgr:SDKLogin("{accountName}")
    """
    bp.lua_console(lua_code)


def disconnect(bp: BasePage):
    lua_code = f"""
_G.CURRENT_SDK_MANUAL_LOGIN = true
PanelMgr:CloseAllOpend()
Global_ClearCacheData()
Global_SendLogout()
_G.NetworkMgr:StopTimeOutTimer()
_G.NetworkMgr:Disconnect()
UIFacade.Reset()
--Util.GoToLogin()
EventMgr:SendEvent(GameMsg.CHANGE_GAME_STATE, GAME_STATE_ENUM.Login, true)
        """
    bp.lua_console(lua_code)


def login(bp: BasePage, name):
    LoginPanel.wait_for_panel_appear(bp)
    connect(bp, name)
    LoadingPanel.wait_until_panel_disappear(bp)
    bp.cmd("guideskip")


def logout(bp: BasePage):
    bp.sleep(1)
    disconnect(bp)



def go_leaderborad(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.click_btn_leaderboard(bp)
    bp.sleep(1)

def fish(bp: BasePage):
    bp.cmd_list(["levelupto 30"])
    bp.sleep(0.1)
    bp.cmd("mode 400309 390087")
    fishingMsg.fish(bp, [{"spot_id": f"40030913", "times": 1, "energy_cost": 50}])
    bp.sleep(0.1)
    bp.cmd("mode 400309 390088")
    fishingMsg.fish(bp, [{"spot_id": f"40030913", "times": 1, "energy_cost": 50}])
    bp.sleep(0.1)
    bp.cmd("mode 400309 390089")
    fishingMsg.fish(bp, [{"spot_id": f"40030913", "times": 1, "energy_cost": 50}])
    bp.sleep(0.1)

def dragon_boat(bp: BasePage, index):
    bp.cmd_list(["levelupto 20", "add 1 100500 100000", "add 1 100100 3000"])
    bp.sleep(0.2)
    lua_code = csMsgAll.get_CSGameGuildCreateMsg(flag=5, joinType=1, joinLv=0, color=3, name=f"d_{index}", introduce="一起欢乐钓鱼吧！", pattern=1)
    bp.lua_console(lua_code)
    # fishingMsg.fish(bp, [
    #     {"spot_id": f"40030103", "times": index}
    # ])
    # bp.sleep(index * 0.2)



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
    lua_code = csMsgAll.get_CSHiddenTreasureDigMsg(digYs=dy, roomId=1000298, groupId=6000001, stageId=1, digXs=dx)
    print(lua_code)
    bp.lua_console(lua_code)


def apply_guild(bp:BasePage):
    bp.cmd(f"levelupto 21")
    bp.sleep(1)
    guildSimpleId = 10000009
    lua_code = csMsgAll.get_CSGuildApplyMsg(source=0, guildSimpleId=guildSimpleId)
    bp.lua_console(lua_code)

    # # 领公会红包
    # bp.sleep(0.5)
    # lua_code = csMsgAll.get_CSGameGuildRewardRedEnvelopeMsg(source=0, guildSimpleId=guildSimpleId, redEnvelopeId=1)
    # bp.lua_console(lua_code)
    # bp.sleep(0.5)


def ndays(bp:BasePage, count):
    # bp.cmd(f"setPlayerLayer {count}000")
    bp.cmd(f"levelupto 16")
    bp.sleep(0.1)
    guildSimpleId = 10000082
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

def add_gu(bp: BasePage, index):
    bp.cmd(f"globalgm dragonAddPoint {index}")

def championshipsclear(bp: BasePage):

    bp.go_to_panel("TournamentsPanel")
    bp.sleep(0.5)
    bp.cmd("championshipsclear")
    icon_list = TournamentsPanel.get_tournaments_info_icon_list(bp)
    with open("../statistics/log.txt", "a") as file:
        for icon in icon_list:
            file.write(icon)
            print(icon)
        file.write("\n")
    bp.sleep(2)


def main(bp):
    # 登录号前缀
    prefix = "a"
    init(bp)
    cur = 0
    limit = 100
    while cur < limit:
        name = prefix + str(cur)
        login(bp, name)

        # 你要执行的初始化账号操作
        # add_gu(bp, cur)
        # dragon_boat(bp, cur)
        # apply_guild(bp)
        fish(bp)

        logout(bp)
        cur += 1

def main2(bp):
    cur = 3
    limit = 15
    while cur < limit:
        name = "1000002002"
        login(bp, name)
        championshipsclear(bp)
        # apply_guild(bp)
        bp.lua_console('PanelMgr:OpenPanel("PlayerInfoPanel")')
        logout(bp)
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
    bp = BasePage("127.0.0.1:21503")
    main(bp)
    bp.connect_close()