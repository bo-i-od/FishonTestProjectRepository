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
    lua_code = """
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
#     lua_code = """
# ---@type TYSDK.LoginSDK
# local loginSdkInst = TYSDK.LoginSDK.Instanc
# --FIXME:兼容C#部分
# local function pcallloginSdkInstLogOutfunc()
#     if loginSdkInst.LogOut then
#         loginSdkInst:LogOut(true)
#     end
# end
# xpcall(pcallloginSdkInstLogOutfunc, function() end)
# local Login_Token_Key = "Login_Token"
# SettingMgr:Write(Login_Token_Key, "")
# _G.GAME_SDK_AUTHDATA_CACHE = nil
# local NetworkMgr = UIFacade.Get('NetworkMgr')
# _G.CURRENT_SDK_MANUAL_LOGIN = true
# PanelMgr:CloseAllOpend()
# GameRoot:GetFishingCamera().fsm:ChangeState(FishingCamera_FSM_STATE.GAME)
#
# Global_ClearCacheData()
# Global_SendLogout()
# NetworkMgr.channelPurl = nil
# NetworkMgr:StopTimeOutTimer()
# NetworkMgr:Disconnect()
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
    bp.cmd("guideskip")
    bp.sleep(1)
    while True:
        PlayerEditNamePanel.set_player_name(bp, name)
        PlayerEditNamePanel.click_confirm(bp)
        bp.sleep(1)
        if not PlayerEditNamePanel.is_panel_active(bp):
            break
        name = "t" + str(time.time()).split('.')[0]

    # # 随机选择性别
    # r = 0
    # gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    # bp.click_position(gender_icon_position_list[r])
    # bp.sleep(0.5)
    #
    # AvatarSelectPanel.click_btn_start(bp)





def logout(bp: BasePage):
    bp.sleep(1)
    disconnect(bp)



def go_leaderborad(bp:BasePage):
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.click_btn_leaderboard(bp)
    bp.sleep(1)

def fish(bp: BasePage, index):
    bp.cmd_list(["levelupto 61", f"add 1 100500 {index * 500}"])
    fishingMsg.fish(bp, [{"spot_id": f"40030103", "times": index}, {"spot_id": f"40030203", "times": index}, {"spot_id": f"40030303", "times": index}, {"spot_id": f"40030403", "times": index}, {"spot_id": f"40030503", "times": index}, {"spot_id": f"40030603", "times": index}, {"spot_id": f"40030703", "times": index}, {"spot_id": f"40030803", "times": index}, {"spot_id": f"40030903", "times": index}, {"spot_id": f"40031003", "times": index}, {"spot_id": f"40031103", "times": index}, {"spot_id": f"40031203", "times": index}, {"spot_id": f"40031703", "times": index}])
    bp.sleep(index * 4)



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
    bp.cmd_list([f"levelupto 20", "add 1 101500 20"])
    bp.sleep(0.2)
    dy = "{[1] = 1,}"
    dx = "{[1] = 1,}"
    lua_code = csMsgAll.get_CSHiddenTreasureDigMsg(digYs=dy, roomId=1000340, groupId=6000001, stage=1, digXs=dx)
    print(lua_code)
    bp.lua_console(lua_code)


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
    # bp.cmd(f"setPlayerLayer {count}000")
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
    prefix = "v"
    # prefix_list = ["a", "b", "c", "d", "e"]
    init(bp)
    cur = 71
    limit = 120
    while cur < limit:
        name = prefix + str(cur)
        login(bp, name)
        bp.cmd("selfranksetip 12.34.56.78")
        bp.cmd("levelupto 61")
        # 你要执行的初始化账号操作
        # add_gu(bp, cur)
        # dragon_boat(bp, cur)
        # apply_guild(bp)
        # friend(bp)
        # ndays(bp, cur)
        rank(bp)
        # hidden_treasure(bp)
        logout(bp)
        cur += 1


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21513", is_android=False)
    relogin(bp)
    # main(bp)
    bp.connect_close()