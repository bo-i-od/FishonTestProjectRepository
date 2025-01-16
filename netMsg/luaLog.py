from tools.commonTools import lua_dict_to_python_dict
import json

def deal_with_msg(msg):
    # if '<==== [Lua] Receive Net Msg "SC' in msg:
    #     print(msg)

    # print(msg)
    if '<==== [Lua] Receive Net Msg "SCFishingHookMsg" ====>' in msg:
        deal_with_SCFishingHookMsg(msg)
        deal_with_SCFishingHookMsg_new(msg)
        return

    if '<==== [Lua] Receive Net Msg "SCFishingCastMsg" ====>' in msg:
        deal_with_SCFishingCastMsg(msg)
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

def check_msg_success(msg_data):
    if msg_data.get('notify',{}).get('code',-1)==0:
        return True
    else:
        return False

def deal_with_SCFishingCastMsg_new(msg):
    # print(msg)
    msg_data=lua_dict_to_python_dict(msg)
    if check_msg_success(msg_data):
        f = open("../statistics/new_cast_log.txt", "a")
        f.write(json.dumps(msg_data)+"\n")
        f.close()


def deal_with_SCFishingHookMsg_new(msg):
    # print(msg)
    msg_data = lua_dict_to_python_dict(msg)
    if check_msg_success(msg_data):
        f = open("../statistics/new_hook_log.txt", "a")
        f.write(json.dumps(msg_data)+"\n")
        f.close()

def deal_with_SCFishingHookMsg(msg):
    # print(msg)
    key1 = "tpId"
    value1 = get_value(msg, key1, False)
    key2 = "color"
    value2 = get_value(msg, key2, False)
    key3 = "otherItems"
    value3 = get_dict(msg, key3)
    key3_1 = "count"
    value3_1 = get_value(value3, key3_1, False)
    key3_2 = "id"
    value3_2 = get_value(value3, key3_2, False)
    key4 = "point"
    value4 = get_value(msg, key4, False)
    key5 = "weight"
    value5 = get_value(msg, key5, False)
    key6 = "star"
    value6 = get_value(msg, key6, False)
    string=f"fish_id:{value1}, color:{value2}, flash_card_num:{value3_1}, flash_card_id:{value3_2}, point:{value4}, weight:{value5}, star:{value6}"
    # print(value1)
    # if value3_1:
    #     print(msg)
    f = open("../statistics/hook_log.txt", "a")
    f.write(string+"\n")
    f.close()


def deal_with_SCFishingCastMsg(msg):
    # print(msg)
    key1 = "debugInfos"
    value1 = get_dict(msg, key1)
    key1_list=['isFishState','isTimeLimitedSpot','protectiveId','energyCostGroup','isInDoubleWeek','energyCost']

    string=''
    for i in key1_list:
        value = get_value(value1, i, False)
        string+=(i+':'+value+', ')
    f = open("../statistics/cast_log.txt", "a")
    f.write(string+"\n")
    f.close()
    pass

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


    