from common.basePage import BasePage
import luaLog
from importlib import import_module

from netMsg import csMsgAll

msg_data = {
    "AchieveCategoryRewardMsg": {"msg_arg": {"categoryTpId": 10001}, "expect_reply": ["success", "成就点数没有达到领奖要求", "没有获得这个成就鱼种"]},
    "AchieveCategoryFishLightMsg": {"msg_arg": {"categoryTpId": 10001, "fishTpId": 301004}, "expect_reply": ["success"]},
    "AchieveCategoryUnlockMsg": {"msg_arg": {"categoryTpId": 10001}, "expect_reply": ["success", "没有获得这个成就鱼种"]},
    "AchieveWantedRewardMsg": {"msg_arg": {"wantedTpId": 40030101}, "expect_reply": ["success", "成就点数没有达到领奖要求", "没有获得这个成就鱼种"]},
    "AchieveWantedFishLightMsg": {"msg_arg": {"wantedTpId": 40030101, "fishTpId": 390001}, "expect_reply": ["success"]},
    "AchieveWantedUnlockMsg": {"msg_arg": {"wantedTpId": 40030101}, "expect_reply": ["success", "没有获得这个成就鱼种"]},
    "AchieveGroupUnlockMsg": {"msg_arg": {"achieveGroupTpId": 201}, "expect_reply": ["success", "没有解锁成就组"]},
    "AchieveGroupRewardMsg": {"msg_arg": {"achieveGroupTpId": 201, "num": 50}, "expect_reply": ["success", "已经领奖了", "成就点数没有达到领奖要求"]},

}


def check_sc_msg(bp: BasePage, msg_name: str, expect_key):
    expect_value_list = msg_data[msg_name]["expect_reply"]
    # 在最近收集的消息列表中筛出目标消息
    key_sc = '<==== [Lua] Receive Net Msg "SC'
    msg_key = key_sc + msg_name
    target_log = get_target_log(bp, msg_key)
    if target_log == "":
        return False

    # 根据期望键拿到值
    value = luaLog.get_value(msg=target_log, key=expect_key, is_str=True)

    # 看值是否在期望的值列表中
    if value not in expect_value_list:
        return False
    return True


# 根据消息键查找值
def get_target_log(bp: BasePage, msg_key):
    target_log = ""
    for log in bp.log_list:
        if msg_key not in log:
            continue
        target_log = log
        break
    return target_log


def call_function(module_name, function_name, *args, **kwargs):
    # 动态导入模块
    module = import_module(module_name)
    # 获取函数
    function = getattr(module, function_name)
    # 调用函数并返回结果
    return function(*args, **kwargs)


def msg_test(msg_name):
    res = {}
    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    # 发送cs请求
    lua_code = call_function(module_name="csMsgAll", function_name=f"get_CS{msg_name}", **msg_data[msg_name]["msg_arg"])
    bp.lua_console(lua_code)

    # 停止接收消息
    bp.sleep(0.5)
    bp.log_list_flag = False

    # 判断结果是否正确
    res[msg_name] = check_sc_msg(bp, msg_name, "msg")
    return res


def achieve_test(bp: BasePage):
    res = {}
    # 成就解锁
    res.update(msg_test("AchieveGroupUnlockMsg"))

    # 完成所有成就
    # bp.cmd("missiondone 10")
    # bp.sleep(0.1)

    # 成就领奖
    res.update(msg_test("AchieveGroupReward"))

    return res


def achieveCategory_test(bp: BasePage):
    res = {}
    # 鱼种成就解锁
    res.update(msg_test("AchieveCategoryUnlockMsg"))

    # 完成所有成就
    bp.cmd("categoryComplete 10001")
    bp.sleep(0.1)

    # 鱼种点亮
    res.update(msg_test("AchieveCategoryFishLightMsg"))

    # 鱼种领奖
    res.update(msg_test("AchieveCategoryRewardMsg"))

    return res


def achieveWanted_test(bp: BasePage):
    res = {}
    # 鱼种成就解锁
    res.update(msg_test("AchieveWantedUnlockMsg"))

    # 完成成就
    wantedTpId = msg_data["AchieveWantedFishLightMsg"]["msg_arg"]["wantedTpId"]
    bp.cmd(f"wantedComplete {wantedTpId}")
    bp.sleep(0.1)

    # 鱼种点亮
    res.update(msg_test("AchieveWantedFishLightMsg"))

    # 鱼种领奖
    res.update(msg_test("AchieveWantedRewardMsg"))

    return res


def activationCode_test(bp: BasePage):
    pass


if __name__ == '__main__':
    bp = BasePage()
    # achieve_test(bp)

    # a = achieveWanted_test(bp)
    # print(a)

    # guildSimpleId = 10000012
    lua_code = csMsgAll.get_CSHiddenTreasureSetMultipleMsg(multiple=50, stageId=1, groupId=6000001, roomId=1000298)
    bp.lua_console(lua_code)
    bp.connect_close()
