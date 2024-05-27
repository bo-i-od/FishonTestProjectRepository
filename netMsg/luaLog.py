import json
import time


def deal_with_msg(msg):
    if "SCFishingHookMsg" in msg:
        deal_with_SCFishingHookMsg(msg)
        return

    if "SCFishingCastMsg" in msg:
        deal_with_SCFishingCastMsg(msg)
        return


def deal_with_SCFishingHookMsg(msg):
    key1 = "tpId"
    value1 = get_value(msg, key1, False)
    key2 = "color"
    value2 = get_value(msg, key2, False)
    f = open("log.txt", "a")
    f.write(f"{value1}  {value2}")
    f.close()


def deal_with_SCFishingCastMsg(msg):
    pass


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

    