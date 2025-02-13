from tools.commonTools import lua_dict_to_python_dict
import json

def deal_with_msg(msg):
    # if '<==== [Lua] Receive Net Msg "SC' in msg:
    #     print(msg)

    # print(msg)
    if '<==== [Lua] Receive Net Msg "SCFishingHookMsg" ====>' in msg:
        deal_with_SCFishingHookMsg_new(msg)
        return

    if '<==== [Lua] Receive Net Msg "SCFishingCastMsg" ====>' in msg:
        deal_with_SCFishingCastMsg_new(msg)
        return

    if '<==== [Lua] Receive Net Msg "SCHiddenTreasureFreeShovelProgressChangedMsg" ====>' in msg:
        deal_with_SCHiddenTreasureFreeShovelProgressChangedMsg(msg)
        return

    if '<==== [Lua] Receive Net Msg "SCMonopolyFreeDiceProgressChangedMsg" ====>' in msg:
        deal_with_SCMonopolyFreeDiceProgressChangedMsg(msg)
        return

    if '<==== [Lua] Receive Net Msg "SCCooperateSpinMsg" ====>' in msg:
        deal_with_SCCooperateSpinMsg(msg)
        return

    # if '<==== [Lua] Receive Net Msg "SCEnterGameMsg" ====>' in msg:
    #     print(msg)
    #     return


def deal_with_SCFishingCastMsg_new(msg):
    # print(msg)
    msg_data=lua_dict_to_python_dict(msg)
    f = open("../statistics/new_cast_log.txt", "a")
    f.write(json.dumps(msg_data)+"\n")
    f.close()


def deal_with_SCFishingHookMsg_new(msg):
    # print(msg)
    msg_data = lua_dict_to_python_dict(msg)
    f = open("../statistics/new_hook_log.txt", "a")
    f.write(json.dumps(msg_data)+"\n")
    f.close()

def deal_with_SCHiddenTreasureFreeShovelProgressChangedMsg(msg):
    key1 = "addProgress"
    value1 = get_value(msg, key1, False)
    key2 = "addShovelCount"
    value2 = get_value(msg, key2, False)
    f = open("../statistics/log.txt", "a")
    res = f"{key1}:{value1}, {key2}:{value2}, "
    # print(res)
    f.write(res)
    f.close()

def deal_with_SCMonopolyFreeDiceProgressChangedMsg(msg):
    key1 = "addProgress"
    value1 = get_value(msg, key1, False)
    key2 = "addDiceCount"
    value2 = get_value(msg, key2, False)
    f = open("../statistics/log.txt", "a")
    res = f"{key1}:{value1}, {key2}:{value2}, "
    # print(res)
    f.write(res)
    f.close()

def deal_with_SCCooperateSpinMsg(msg):
    key1 = "spinIndex"
    value1 = get_value(msg, key1, False)
    f = open("../statistics/spin_log.txt", "a")
    res = f"{key1}:{value1}\n"
    f.write(res)
    f.close()



def get_value(msg:str, key: str, is_str: bool):
    detail_list = msg.split(',')
    value = ""
    cur = 0
    while cur < len(detail_list):
        if key not in detail_list[cur]:
            cur += 1
            continue
        target_detail_list = detail_list[cur].split(" ")
        value = target_detail_list[len(target_detail_list) - 1]
        if is_str:
            value = value.replace("\"", "")
        break
    return value

def get_dict(msg: str, key:str):
    left = msg.find(key)
    right = left
    cur = left
    first_flag = True
    count = 0
    while cur < len(msg):
        if msg[cur] == '{':
            if first_flag:
                left = cur
                first_flag = False
            count += 1
            cur += 1
            continue
        if msg[cur] != '}':
            cur += 1
            continue
        count -= 1
        if count > 0:
            cur += 1
            continue
        cur += 1
        right = cur
        break
    res = msg[left:right]
    return res


    