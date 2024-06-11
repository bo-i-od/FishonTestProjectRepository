import time

from common.basePage import BasePage
import luaLog
from importlib import import_module

from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel


class NetMsgTest():
    def __init__(self, bp: BasePage):
        self.bp = bp
        self.username = ""
        self.charSimpleId = 0
        self.charId = ""
        self.userId = ""
        self.roomId_division = 0
        self.login()
        self.msg_data = {
            "AchieveCategoryRewardMsg": {"msg_arg": {"categoryTpId": 10001}, "expect_reply": ["success", "成就点数没有达到领奖要求", "没有获得这个成就鱼种"]},
            "AchieveCategoryFishLightMsg": {"msg_arg": {"categoryTpId": 10001, "fishTpId": 301004}, "expect_reply": ["success"]},
            "AchieveCategoryUnlockMsg": {"msg_arg": {"categoryTpId": 10001}, "expect_reply": ["success", "没有获得这个成就鱼种"]},
            "AchieveWantedRewardMsg": {"msg_arg": {"wantedTpId": 40030101}, "expect_reply": ["success", "成就点数没有达到领奖要求", "没有获得这个成就鱼种"]},
            "AchieveWantedFishLightMsg": {"msg_arg": {"wantedTpId": 40030101, "fishTpId": 390001}, "expect_reply": ["success"]},
            "AchieveWantedUnlockMsg": {"msg_arg": {"wantedTpId": 40030101}, "expect_reply": ["success", "没有获得这个成就鱼种"]},
            "AchieveGroupUnlockMsg": {"msg_arg": {"achieveGroupTpId": 201}, "expect_reply": ["success", "没有解锁成就组"]},
            "AchieveGroupRewardMsg": {"msg_arg": {"achieveGroupTpId": 201, "num": 50}, "expect_reply": ["success", "已经领奖了", "成就点数没有达到领奖要求"]},
            "ActivationCodeUseMsg": {"msg_arg": {"code": "123"}, "expect_reply": ["激活码不存在"]},
            "AquariumProsperityLvUpMsg": {"msg_arg": {"tpId": 101, "lv": 2}, "expect_reply": ["success", "水族箱等级错误", "不存在此水族箱"]},
            "AquariumBuildingUpLvMsg": {"msg_arg": {"buildingTpId": 101003, "tpId": 101}, "expect_reply": ["success", "资源点不足！", "不存在此水族箱"]},
            "AquariumPutFishMsg": {"msg_arg": {"ornamentalFishTpId": 10101, "tpId": 101}, "expect_reply": ["success", "水族箱不存在此观赏鱼", "不存在此水族箱","水族箱鱼已满"]},
            "AquariumRemoveFishMsg": {"msg_arg": {"ornamentalFishTpId": 10101, "tpId": 101}, "expect_reply": ["success", "水族箱不存在此观赏鱼", "不存在此水族箱"]},
            "AquariumBuyOrnamentalFishMsg": {"msg_arg": {"ornamentalFishTpId": 10101, "tpId": 101}, "expect_reply": ["success", "资源点不足！", "不存在此水族箱"]},
            "AquariumRemoveAllFishMsg": {"msg_arg": {"tpId": 101}, "expect_reply": ["success", "不存在此水族箱"]},
            "AquariumSeeHangUpRewardMsg": {"msg_arg": {}, "expect_reply": ["success"]},
            "AquariumHangUpRewardMsg": {"msg_arg": {}, "expect_reply": ["success"]},
            "AquariumSurpriseRewardMsg": {"msg_arg": {"tpId": 101}, "expect_reply": ["success", "不存在此水族箱", "不存在惊喜奖励"]},
            "AquariumSeeFishChangeMsg": {"msg_arg": {"tpId": 101}, "expect_reply": ["success", "不存在此水族箱"]},
            "UseItemMsg": {"msg_arg": {"useTimes": 1, "itemType": 2, "itemTpId": 211001}, "expect_reply": ["success"]},
            "BuyItemMsg": {"msg_arg": {"itemTpId": 100300, "priceTpId": 100100, "count": 1000, "itemType": 1, "source": 0}, "expect_reply": ["success", "资源点不足！"]},
            "BaitAndRodLevelUpToMsg": {"msg_arg": {"targetLevel": 2, "ioIdType": 5, "tpId": 500001}, "expect_reply": ["success", "资源点不足！"]},
            "BaitAndRodStarLevelUpMsg": {"msg_arg": {"source": 1, "ioIdType": 5, "tpId": 500001}, "expect_reply": ["success", "资源点不足！"]},
            "BattlePassGetRewardMsg": {"msg_arg": {"lv": 1, "groupId": 4, "pay": False}, "expect_reply": ["success", "free奖励已经被领取了!"]},
            "BattlePassGetAllRewardMsg": {"msg_arg": {"groupId": 4}, "expect_reply": ["success"]},
            "ChampionshipsGetUnGetRewardsMsg": {"msg_arg": {"championshipsId": 1, "source": 0, "road": 2}, "expect_reply": ["success", "锦标赛轮次已经结束！"]},
            "CharaRenameMsg": {"msg_arg": {"newName": self.username}, "expect_reply": ["success", "改名系统维护中"]},
            "CharaSetIconMsg": {"msg_arg": {"icon": 1}, "expect_reply": ["success"]},
            # "QueryCharInfoMsg": {"msg_arg": {"source": 1, "charId": 10008507}, "expect_reply": ["success"]},
            "QueryPlayerCardInfoMsg": {"msg_arg": {"source": 1, "icon": 1, "charId": self.charId, "name": self.username}, "expect_reply": ["success"]},
            "SetPlayerBadgeAllMsg": {"msg_arg": {"indexToBadge": {}}, "expect_reply": ["success"]},
            "GetChestRewardsMsg": {"msg_arg": {"chestPointId": 5}, "expect_reply": ["success"]},
            "OpenChestMsg": {"msg_arg": {"itemTpId": 207004, "count": 1}, "expect_reply": ["success"]},
            "CommonExchangeMsg": {"msg_arg": {"exchangeId": 102, "buyTimes": 1}, "expect_reply": ["success"]},
            "QueryDivisionRankMsg": {"msg_arg": {"fromRank": 1,"roomId": self.roomId_division, "count": 1}, "expect_reply": ["success"]},
        }

    def login(self):
        while not LoginPanel.is_btn_login_active(self.bp):
            self.bp.sleep(0.5)
        self.username = str(time.time()).split('.')[0]
        LoginPanel.set_login_name(self.bp, self.username)

        # 清空消息列表 开始收消息
        self.bp.log_list.clear()
        self.bp.log_list_flag = True

        LoginPanel.click_btn_login(self.bp)
        self.bp.sleep(2)

        # 直到读条消失
        LoadingPanel.wait_until_panel_disappear(self.bp, is_wait_for_appear=False)

        # 停止接收消息
        self.bp.sleep(0.5)
        self.bp.log_list_flag = False

        # 在最近收集的消息列表中筛出目标消息
        key_sc = '<==== [Lua] Receive Net Msg "SC'
        msg_name = "LoginMsg"
        msg_key = key_sc + msg_name
        target_log = self.get_target_log(msg_key)
        if target_log != "":
            # 根据键拿到值
            self.charSimpleId = luaLog.get_value(msg=target_log, key="charSimpleId", is_str=False)
            self.charId = luaLog.get_value(msg=target_log, key="charId", is_str=True)
            self.userId = luaLog.get_value(msg=target_log, key="userId", is_str=True)
        msg_name = "DivisionBatchDataMsg"
        msg_key = key_sc + msg_name
        target_log = self.get_target_log(msg_key)
        if target_log != "":
            self.roomId_division = luaLog.get_value(msg=target_log, key="roomId", is_str=False)



    def check_sc_msg(self, msg_name: str, expect_key):
        expect_value_list = self.msg_data[msg_name]["expect_reply"]
        # 在最近收集的消息列表中筛出目标消息
        key_sc = '<==== [Lua] Receive Net Msg "SC'
        msg_key = key_sc + msg_name
        target_log = self.get_target_log(msg_key)
        if target_log == "":
            return False

        # 根据期望键拿到值
        value = luaLog.get_value(msg=target_log, key=expect_key, is_str=True)

        # 看值是否在期望的值列表中
        if value not in expect_value_list:
            return False
        return True

    # 根据消息键查找值
    def get_target_log(self, msg_key):
        target_log = ""
        for log in self.bp.log_list:
            if msg_key not in log:
                continue
            target_log = log
            break
        return target_log

    def call_function(self, module_name, function_name, *args, **kwargs):
        # 动态导入模块
        module = import_module(module_name)
        # 获取函数
        function = getattr(module, function_name)
        # 调用函数并返回结果
        return function(*args, **kwargs)

    def msg_test(self, msg_name, expect_key="msg"):
        res = {}
        # 清空消息列表 开始收消息
        self.bp.log_list.clear()
        self.bp.log_list_flag = True

        # 发送cs请求
        lua_code = self.call_function(module_name="csMsgAll", function_name=f"get_CS{msg_name}", **self.msg_data[msg_name]["msg_arg"])
        print(lua_code)
        self.bp.lua_console(lua_code)

        # 停止接收消息
        self.bp.sleep(0.5)
        self.bp.log_list_flag = False

        # 判断结果是否正确
        res[msg_name] = self.check_sc_msg(msg_name, expect_key)
        return res

    def achieve_test(self):
        res = {}
        # 成就解锁
        res.update(self.msg_test("AchieveGroupUnlockMsg"))

        # 完成所有成就
        # bp.cmd("missiondone 10")
        # bp.sleep(0.1)

        # 成就领奖
        res.update(self.msg_test("AchieveGroupReward"))

        return res

    def achieveCategory_test(self):
        res = {}
        # 鱼种成就解锁
        res.update(self.msg_test("AchieveCategoryUnlockMsg"))

        # 完成所有成就
        self.bp.cmd("categoryComplete 10001")
        self.bp.sleep(0.1)

        # 鱼种点亮
        res.update(self.msg_test("AchieveCategoryFishLightMsg"))

        # 鱼种领奖
        res.update(self.msg_test("AchieveCategoryRewardMsg"))

        return res

    def achieveWanted_test(self, bp: BasePage):
        res = {}
        # 鱼种成就解锁
        res.update(self.msg_test("AchieveWantedUnlockMsg"))

        # 完成成就
        wantedTpId = self.msg_data["AchieveWantedFishLightMsg"]["msg_arg"]["wantedTpId"]
        bp.cmd(f"wantedComplete {wantedTpId}")
        bp.sleep(0.1)

        # 鱼种点亮
        res.update(self.msg_test("AchieveWantedFishLightMsg"))

        # 鱼种领奖
        res.update(self.msg_test("AchieveWantedRewardMsg"))

        return res

    def activationCode_test(self):
        res = {}
        res.update(self.msg_test("ActivationCodeUseMsg"))
        return res

    def aquarium_test(self):
        res = {}
        self.bp.set_item_count(target_count=2000, item_tpid="101000")
        self.bp.cmd_list(["levelupto 30"])
        # 繁荣度提升
        res.update(self.msg_test("AquariumProsperityLvUpMsg"))

        # 等级提升
        res.update(self.msg_test("AquariumBuildingUpLvMsg"))

        # 放鱼
        res.update(self.msg_test("AquariumPutFishMsg"))

        # 收鱼
        res.update(self.msg_test("AquariumRemoveFishMsg"))

        # 买鱼
        res.update(self.msg_test("AquariumBuyOrnamentalFishMsg"))

        # 收全鱼
        res.update(self.msg_test("AquariumRemoveAllFishMsg"))

        # 查看挂机奖励
        res.update(self.msg_test("AquariumSeeHangUpRewardMsg"))

        # 领取挂机奖励
        res.update(self.msg_test("AquariumHangUpRewardMsg"))

        # 领取挂机奖励
        res.update(self.msg_test("AquariumSurpriseRewardMsg"))

        # 刷新鱼
        res.update(self.msg_test("AquariumSeeFishChangeMsg"))

        return res

    def backPack_test(self):
        res = {}

        # 使用道具
        self.bp.set_item_count(target_count=1, item_tpid=str(self.msg_data["UseItemMsg"]["msg_arg"]["itemTpId"]))
        res.update(self.msg_test("UseItemMsg"))

        # 买道具
        self.bp.set_item_count(target_count=self.msg_data["BuyItemMsg"]["msg_arg"]["count"], item_tpid=str(self.msg_data["BuyItemMsg"]["msg_arg"]["priceTpId"]))
        res.update(self.msg_test("BuyItemMsg"))

        return res

    def baitAndRod_test(self):
        res = {}

        self.bp.set_item_count(target_count=1000, item_tpid="100000")
        res.update(self.msg_test("BaitAndRodLevelUpToMsg"))

        self.bp.set_item_count(target_count=2, item_tpid=str(self.msg_data["BaitAndRodStarLevelUpMsg"]["msg_arg"]["tpId"]))
        res.update(self.msg_test("BaitAndRodStarLevelUpMsg"))

        return res

    def battlePass_test(self):
        res = {}
        res.update(self.msg_test("BattlePassGetRewardMsg"))

        res.update(self.msg_test("BattlePassGetAllRewardMsg"))
        return res

    def championships_test(self):
        res = {}

        res.update(self.msg_test("ChampionshipsGetUnGetRewardsMsg"))

        return res

    def chara_test(self):
        res = {}

        # 改名
        res.update(self.msg_test("CharaRenameMsg"))

        # 改头像
        res.update(self.msg_test("CharaSetIconMsg"))

        # 查询信息
        res.update(self.msg_test("QueryPlayerCardInfoMsg"))

        # 设置徽章
        res.update(self.msg_test("SetPlayerBadgeAllMsg"))

        return res

    def chest_test(self):
        res = {}

        self.bp.set_item_count(target_count=1, item_tpid="207004")

        # 开箱
        res.update(self.msg_test("OpenChestMsg"))

        # 箱子点
        res.update(self.msg_test("GetChestRewardsMsg"))

        return res

    def commonExchange_test(self):
        res = {}

        self.bp.set_item_count(target_count=1, item_tpid="200600")

        # 用饮料
        res.update(self.msg_test("CommonExchangeMsg"))

        return res

    def division_test(self):
        res = {}

        # 用饮料
        res.update(self.msg_test("QueryDivisionRankMsg"))

        return res

    def main(self):
        res = self.division_test()
        print(res)


if __name__ == '__main__':
    bp = BasePage()
    netMsgTest = NetMsgTest(bp)
    netMsgTest.main()
    bp.connect_close()

    # a = chara_test(bp)
    # print(a)

    # guildSimpleId = 10000012
    # lua_code = csMsgAll.get_CSHiddenTreasureSetMultipleMsg(multiple=50, stageId=1, groupId=6000001, roomId=1000298)
    # bp.lua_console(lua_code)
    # bp.connect_close()
