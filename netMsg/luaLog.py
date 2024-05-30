

def deal_with_msg(msg):
    if "SCFishingHookMsg" in msg:
        deal_with_SCFishingHookMsg(msg)
        return

    if "SCFishingCastMsg" in msg:
        deal_with_SCFishingCastMsg(msg)
        return

    if "SCHiddenTreasureFreeShovelProgressChangedMsg" in msg:
        deal_with_SCHiddenTreasureFreeShovelProgressChangedMsg(msg)
        return

    if "SCMonopolyFreeDiceProgressChangedMsg" in msg:
        deal_with_SCMonopolyFreeDiceProgressChangedMsg(msg)
        return




def deal_with_SCFishingHookMsg(msg):
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
    string=f"fish_id:{value1}, color:{value2}, flash_card_num:{value3_1}, flash_card_id:{value3_2}"
    print(string)
    f = open("../statistics/log.txt", "a")
    f.write(string+"\n")
    f.close()


def deal_with_SCFishingCastMsg(msg):
    pass

def deal_with_SCHiddenTreasureFreeShovelProgressChangedMsg(msg):
    key1 = "addProgress"
    value1 = get_value(msg, key1, False)
    key2 = "addShovelCount"
    value2 = get_value(msg, key2, False)
    f = open("../statistics/log.txt", "a")
    res = f"{key1}:{value1}, {key2}:{value2}, "
    print(res)
    f.write(res)
    f.close()

def deal_with_SCMonopolyFreeDiceProgressChangedMsg(msg):
    key1 = "addProgress"
    value1 = get_value(msg, key1, False)
    key2 = "addDiceCount"
    value2 = get_value(msg, key2, False)
    f = open("../statistics/log.txt", "a")
    res = f"{key1}:{value1}, {key2}:{value2}, "
    print(res)
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


    