from common.basePage import BasePage
import csMsgAll
import luaLog


def check_sc_msg(bp: BasePage, msg_name: str, expect_key, expect_value_list):
    target_log = ""

    # 在最近收集的消息列表中筛出目标消息
    for log in bp.log_list:
        if key_sc + msg_name not in log:
            continue
        target_log = log
        break
    if target_log == "":
        return False

    # 根据期望键拿到值
    value = luaLog.get_value(msg=target_log, key=expect_key, is_str=True)

    # 看值是否在期望的值列表中
    if value not in expect_value_list:
        return False
    return True


def achieve_test(bp: BasePage):
    res = {}
    # bp.cmd("levelupto 5")
    bp.sleep(0.1)

    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    # 发送cs请求
    lua_code = csMsgAll.get_CSAchieveGroupUnlockMsg(achieveGroupTpId=201)
    bp.lua_console(lua_code)

    # 停止接收消息
    bp.sleep(0.5)
    bp.log_list_flag = False

    # 判断结果是否正确
    res['AchieveGroupUnlockMsg'] = check_sc_msg(bp, "AchieveGroupUnlockMsg", "msg", ["success", "没有解锁成就组"])

    # 完成所有成就
    bp.cmd("missiondone 10")
    bp.sleep(0.1)

    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    # 发送cs请求
    lua_code = csMsgAll.get_CSAchieveGroupRewardMsg(num=50, achieveGroupTpId=101)
    bp.lua_console(lua_code)

    # 停止接收消息
    bp.sleep(0.5)
    bp.log_list_flag = False

    # 判断结果是否正确
    res['AchieveGroupRewardMsg'] = check_sc_msg(bp, "AchieveGroupRewardMsg", "msg", ["success", "已经领奖了"])
    print(res)
    return res


# def achieveCategory_test(bp: BasePage):




if __name__ == '__main__':
    bp = BasePage()
    key_sc = '<==== [Lua] Receive Net Msg "SC'
    achieve_test(bp)
    bp.connect_close()
    # guildSimpleId = 10000012
    # lua_code = csMsgAll.get_CSGuildApplyMsg(source=0, guildSimpleId=guildSimpleId)
    # bp.lua_console(lua_code)
