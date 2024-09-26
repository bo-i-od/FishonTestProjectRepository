import random
import time

import scripts
from netMsg import csMsgAll, fishingMsg, luaLog
from panelObjs.avatarSelectPanel import AvatarSelectPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.tournamentsPanel import TournamentsPanel
from panelObjs.friendPanel import FriendPanel
from scripts import battleTest
import json

from tools import commonTools


def set_duelcup_random(bp:BasePage, rank):
    duelcup = random.randint(0,5)
    bp.cmd(f"duelcup 1001 {duelcup}")
    duelcup_all = duelcup
    if rank > 0:
        bp.cmd(f"duelcup 1001 {5}")
        duelcup_all = 5
        duelcup = random.randint(15 - duelcup_all, 20)
        bp.cmd(f"duelcup 1002 {duelcup}")
        duelcup_all += duelcup
    if rank > 1:
        duelcup = random.randint(80 - duelcup_all, 80)
        bp.cmd(f"duelcup 1003 {duelcup}")
        duelcup_all += duelcup
    if rank > 2:
        duelcup = random.randint(200 - duelcup_all, 160)
        bp.cmd(f"duelcup 1004 {duelcup}")
        duelcup_all += duelcup
    if rank > 3:
        duelcup = random.randint(600 - duelcup_all, 480)
        bp.cmd(f"duelcup 1005 {duelcup}")
        duelcup_all += duelcup
    if rank > 4:
        duelcup = random.randint(1200 - duelcup_all, 960)
        bp.cmd(f"duelcup 1006 {duelcup}")
        duelcup_all += duelcup
    if rank > 5:
        duelcup = random.randint(2100 - duelcup_all, 1920)
        bp.cmd(f"duelcup 1007 {duelcup}")
        duelcup_all += duelcup
    if rank > 6:
        duelcup = random.randint(0, 3000)
        bp.cmd(f"duelcup 1008 {duelcup}")
        duelcup_all += duelcup
    return duelcup_all

def set_duelcup(bp:BasePage, duelcup):
    if duelcup <= 5:
        bp.cmd(f"duelcup 1001 {duelcup}")
        return
    bp.cmd(f"duelcup 1001 {5}")

    if duelcup <= 25:
        bp.cmd(f"duelcup 1002 {duelcup - 5}")
        return
    bp.cmd(f"duelcup 1002 {20}")

    if duelcup <= 105:
        bp.cmd(f"duelcup 1003 {duelcup - 25}")
        return
    bp.cmd(f"duelcup 1003 {80}")

    if duelcup <= 265:
        bp.cmd(f"duelcup 1004 {duelcup - 105}")
        return
    bp.cmd(f"duelcup 1004 {160}")

    if duelcup <= 745:
        bp.cmd(f"duelcup 1005 {duelcup - 265}")
        return
    bp.cmd(f"duelcup 1005 {480}")

    if duelcup <= 1705:
        bp.cmd(f"duelcup 1006 {duelcup - 745}")
        return
    bp.cmd(f"duelcup 1006 {960}")

    if duelcup <= 3625:
        bp.cmd(f"duelcup 1007 {duelcup - 1705}")
        return
    bp.cmd(f"duelcup 1007 {1920}")
    bp.cmd(f"duelcup 1008 {duelcup - 3625}")


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
    bp.clear_popup()
    lua_code = f"""
_G.NetworkMgr:SDKLogin("{accountName}")
    """
    bp.lua_console(lua_code)


def disconnect(bp: BasePage):
    lua_code = """---@type TYSDK.LoginSDK
local loginSdkInst = TYSDK.LoginSDK.Instance
--FIXME:兼容C#部分
local function pcallloginSdkInstLogOutfunc()
    if loginSdkInst.LogOut then
        loginSdkInst:LogOut(true)
    end
end
xpcall(pcallloginSdkInstLogOutfunc, function() end)
local Login_Token_Key = "Login_Token"
SettingMgr:Write(Login_Token_Key, "")
_G.CURRENT_SDK_MANUAL_LOGIN = true
PanelMgr:CloseAllOpend()
Global_ClearCacheData()
Global_SendLogout()
_G.NetworkMgr.channelPurl = nil
_G.NetworkMgr:StopTimeOutTimer()
_G.NetworkMgr:Disconnect()
UIFacade.Reset()
--Util.GoToLogin()
EventMgr:SendEvent(GameMsg.CHANGE_GAME_STATE, GAME_STATE_ENUM.Login, true)
    """
#     lua_code = """_G.CURRENT_SDK_MANUAL_LOGIN = true
# PanelMgr:CloseAllOpend()
# Global_ClearCacheData()
# Global_SendLogout()
# _G.NetworkMgr:StopTimeOutTimer()
# _G.NetworkMgr:Disconnect()
# UIFacade.Reset()
# --Util.GoToLogin()
# EventMgr:SendEvent(GameMsg.CHANGE_GAME_STATE, GAME_STATE_ENUM.Login, true)
# """
    bp.lua_console(lua_code)


def login(bp: BasePage, name):
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    LoginPanel.wait_for_panel_appear(bp)
    connect(bp, name)
    LoadingPanel.wait_until_panel_disappear(bp)
    bp.log_list_flag = False

    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    bp.cmd_list(["guideskip"])
    bp.sleep(1)
    while True:
        # PlayerEditNamePanel.set_player_name(bp, name)
        PlayerEditNamePanel.click_confirm(bp)
        bp.sleep(1)
        if not PlayerEditNamePanel.is_panel_active(bp):
            break
        # name = "t" + str(time.time()).split('.')[0]

    bp.sleep(1)
    if not AvatarSelectPanel.is_panel_active(bp):
        return
    # # 随机选择性别
    # r = 0
    gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    bp.click_position(gender_icon_position_list[0])
    bp.sleep(0.5)

    AvatarSelectPanel.click_btn_start(bp)





def logout(bp: BasePage):
    bp.sleep(1)
    disconnect(bp)



def go_leaderborad(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.click_btn_leaderboard(bp)
    bp.sleep(1)

def fish(bp: BasePage, index):

    bp.cmd(f"setPlayerLayer 5000")
    bp.cmd_list(["levelupto 99", "add 1 100500 3000"])



    # bp.cmd("mode 400312 390116")
    # bp.sleep(1)
    # fishingMsg.fish(bp, [{"spot_id": f"40031213", "times": 96, "is_activity_spot": False}])
    # bp.sleep(13)
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True
    msg_name = "ActivityDoubleWeekBatchDataMsg"
    bp.cmd("mode 400319 390187")
    bp.sleep(0.5)
    fishingMsg.fish(bp, [{"spot_id": f"40031913", "times": 1, "is_activity_spot": True}])
    bp.sleep(0.5)
    bp.cmd("mode 400319 390188")
    bp.sleep(0.5)
    fishingMsg.fish(bp, [{"spot_id": f"40031913", "times": 1, "is_activity_spot": True}])
    bp.sleep(0.5)
    bp.cmd("mode 400319 390189")
    bp.sleep(0.5)
    fishingMsg.fish(bp, [{"spot_id": f"40031913", "times": 1, "is_activity_spot": True}])

    target_log = bp.receive_until_get_msg(msg_name=msg_name)
    python_dict = commonTools.lua_dict_to_python_dict(target_log)
    # print(python_dict)
    roomId = python_dict['activityDoubleWeekList'][1]["rankRoomId"]
    print(f"{index}:{roomId}")
    # bp.cmd("mode 400318 390177")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40031813", "times": 1, "is_activity_spot":True}])
    # bp.sleep(0.5)
    # bp.cmd("mode 400318 390178")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40031813", "times": 1, "is_activity_spot":True}])
    # bp.sleep(0.5)
    # bp.cmd("mode 400318 390179")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40031813", "times": 1, "is_activity_spot":True}])

    # bp.cmd("mode 400301 390005")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40030103", "times": 1, "is_activity_spot": False}])
    #
    # bp.cmd("mode 400303 390026")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40030303", "times": 1, "is_activity_spot": False}])
    #
    # bp.cmd("mode 400303 390025")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40030303", "times": 1, "is_activity_spot": False}])
    #
    # bp.cmd("mode 400302 390016")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40030203", "times": 1, "is_activity_spot": False}])
    #
    # bp.cmd("mode 400309 390086")
    # bp.sleep(0.5)
    # fishingMsg.fish(bp, [{"spot_id": f"40030903", "times": 1, "is_activity_spot": False}])






def dragon_boat(bp: BasePage, index):
    bp.cmd_list(["levelupto 20", "add 1 100500 100000", "add 1 100100 3000"])
    bp.sleep(0.2)
    lua_code = csMsgAll.get_CSGameGuildCreateMsg(flag=5, joinType=1, joinLv=0, color=3, name=f"d_{index}", introduce="一起欢乐钓鱼吧！", pattern=1)
    bp.lua_console(lua_code)
    # fishingMsg.fish(bp, [
    #     {"spot_id": f"40030103", "times": index}
    # ])
    # bp.sleep(index * 0.2)

def friend(bp: BasePage):
    # 在最近收集的消息列表中筛出目标消息
    key_sc = '<==== [Lua] Receive Net Msg "SC'
    msg_name = "LoginMsg"
    msg_key = key_sc + msg_name
    target_log = ""
    for log in bp.log_list:
        if msg_key not in log:
            continue
        target_log = log
        break
    charSimpleId = 0
    if target_log != "":
        # 根据键拿到值
        charSimpleId = int(luaLog.get_value(msg=target_log, key="charSimpleId", is_str=False))

    bp.cmd_list(["levelupto 20"])
    bp.sleep(0.2)
    lua_code = csMsgAll.get_CSGlobalFriendsApplyMsg(targetSimpleId=20018852, source=0, type=2, targetCharId="66a0ea35be3a1671c3c9fe59", simpleId=charSimpleId)
    bp.lua_console(lua_code)


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
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True
    bp.cmd(f"setPlayerLayer 2000")
    bp.cmd(f"levelupto 16")
    msg_name = "HiddenTreasureBatchDataMsg"
    target_log = bp.receive_until_get_msg(msg_name=msg_name)
    python_dict = commonTools.lua_dict_to_python_dict(target_log)
    roomId = python_dict['hiddenTreasureList'][1]['roomId']
    print(roomId)
    bp.cmd_list(["add 1 101500 20"])
    bp.sleep(0.2)
    dy = "{[1] = 1,}"
    dx = "{[1] = 1,}"
    lua_code = csMsgAll.get_CSHiddenTreasureDigMsg(digYs=dy, roomId=roomId, groupId=6000001, stage=1, digXs=dx)
    # print(lua_code)
    bp.lua_console(lua_code)


def monopoly(bp:BasePage, layer, index):
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True
    bp.cmd(f"setPlayerLayer {layer}")
    bp.cmd(f"levelupto 16")
    msg_name = "MonopolyBatchDataMsg"
    target_log = bp.receive_until_get_msg(msg_name=msg_name)
    python_dict = commonTools.lua_dict_to_python_dict(target_log)
    roomId = python_dict['monopolyList'][1]['roomId']
    print(roomId)
    bp.cmd(f"monopolyscore {layer + index}")




def apply_guild(bp:BasePage):
    bp.cmd(f"levelupto 21")
    bp.sleep(1)
    guildSimpleId = 10000001
    lua_code = csMsgAll.get_CSGuildApplyMsg(source=0, guildSimpleId=guildSimpleId)
    bp.lua_console(lua_code)

    # # 领公会红包
    # bp.sleep(0.5)
    # lua_code = csMsgAll.get_CSGameGuildRewardRedEnvelopeMsg(source=0, guildSimpleId=guildSimpleId, redEnvelopeId=1)
    # bp.lua_console(lua_code)
    # bp.sleep(0.5)


def ndays(bp:BasePage, count):
    bp.cmd(f"setPlayerLayer {count}000")
    bp.cmd(f"levelupto 16")


    # bp.cmd_list([f"levelupto 20", "add 1 100100 2000"])
    # bp.sleep(0.2)
    # r = random.randint(4, 7)
    # lua_code = csMsgAll.get_CSGameGuildCreateMsg(flag=5, joinType=(count % 2 + 1), joinLv=(r * 5), color=3, name=f"club{count}", introduce="欢迎大家加入俱乐部，一起欢乐钓鱼吧！", pattern=1)
    # print(lua_code)
    # bp.lua_console(lua_code)

    # bp.cmd(f"add 2 209001 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209002 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209003 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209004 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209005 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209006 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209007 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209008 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209009 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209010 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209011 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209012 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209013 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209101 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209102 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209103 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209104 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209105 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209106 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209107 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209108 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209014 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209015 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209016 {count}")
    # bp.sleep(0.1)
    # bp.cmd(f"add 2 209017 {count}")
    # bp.sleep(0.1)


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

def add_friend(bp: BasePage,target_id):
    bp.cmd(f"levelupto 10")
    HomePanel.go_to_panel(bp,"FriendPanel")
    # bp.sleep(1)
    FriendPanel.add_friend(bp,target_id)

def rank(bp: BasePage):
    bp.set_item_count(target_count=10000, item_tpid="100500")
    table_data = bp.excelTools.get_table_data("FISHERIES.xlsm")
    i = 0
    while i < 2:
        tpid_fishery = table_data["tpId"][i]
        cur = 0
        while cur < len(table_data["fish"]):
            tpid_fish = table_data["fish"][cur][i]
            if tpid_fish == 0 or tpid_fish == "0":
                cur += 1
                continue
            cmd = f"mode {tpid_fishery} {tpid_fish}"
            bp.cmd(cmd)
            bp.sleep(0.5)
            fishingMsg.fish(bp, [{"spot_id": f"{tpid_fishery}03", "times": 1}])
            cur += 1
        i += 1

def cup(bp, cur):
    set_duelcup(bp, duelcup=3625 + cur)

def relogin(bp):
    name = "1000002002"
    bp.cmd("clone 1000002002")
    logout(bp)
    login(bp, name)
    bp.go_to_panel("ActivityCenterPanel")
    position_list = bp.get_position_list(element_data={"locator": "UICanvas>Important>ActivityCenterPanel>panel>panel_tab>content>TabList>Viewport>Content>EventsHall_tab_list_4>items>>icon"})
    bp.click_position(position_list[1])
    bp.sleep(1)
    bp.click_element(element_data={"locator": "UICanvas>Default>HiddenTreasureCenterPopupPanel>panel>panel_info>panel_main>button", "focus": (0.5, 1)})



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


def main(bp: BasePage):
    # 登录号前缀
    prefix = "5000_"
    # prefix_list = ["a", "b", "c", "d", "e"]
    init(bp)
    cur = 1
    limit = 200
    while cur < limit:
        name = prefix + str(cur)
        login(bp, name)
        # bp.cmd("levelupto 69")
        # bp.cmd(f"selfranksetip 180.175.{cur}.{cur}")

        # init(bp)
        # fish(bp,cur)
        # 你要执行的初始化账号操作
        # add_gu(bp, cur)
        # dragon_boat(bp, cur)
        # apply_guild(bp)
        # friend(bp)
        # ndays(bp, cur)
        # rank(bp)
        # monopoly(bp, layer=3000, index=cur)
        # hidden_treasure(bp)
        # cup(bp, cur)
        # bp.sleep(2)
        # bp.cmd_list([f"add 1 101200 {cur}", f"add 2 209017 {cur}"])
        fish(bp, cur)
        logout(bp)
        cur += 1


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=True)
    main(bp)
    # relogin(bp)
    # fish(bp, 5)
    # fish(bp, 1)
    bp.connect_close()