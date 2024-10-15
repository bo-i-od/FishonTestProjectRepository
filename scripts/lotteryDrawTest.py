import re
import sys

from netMsg import csMsgAll, luaLog
from common.basePage import BasePage

from collections import OrderedDict

def sort_dict_recursively(d):
    if isinstance(d, dict):
        return {k: sort_dict_recursively(v) for k, v in sorted(d.items(), key=lambda item: item[0])}
    elif isinstance(d, list):
        return [sort_dict_recursively(item) for item in d]
    else:
        return d

def get_price(bp: BasePage):
    msg_name = "LotteryBatchDataMsg"
    target_log = bp.receive_until_get_msg(msg_name=msg_name)
    # print(target_log)
    high_prize_list = lua_list_to_python_list(target_log, 'highPrizeList')
    return high_prize_list


def get_small_reward_dict(bp: BasePage, price_list,wave):
    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="roundId", value=wave, book_name="OUT_DRAW_SMALL_REWARD.xlsm")
    cur = 0
    reward_dict = {}
    while cur < len(price_list):

        price = int(price_list[cur])
        tpid = table_data_object["smallReward"][price]["tpId"]
        count = table_data_object["smallReward"][price]["count"]
        if tpid in reward_dict:
            reward_dict[tpid] += count
            cur += 1
            continue
        reward_dict[tpid] = count
        cur += 1
    return sort_dict_recursively(reward_dict)



def lottery_draw(bp: BasePage, target_index=None):
    count_init = 10000
    bp.set_item_count(item_tpid="102200", target_count=count_init)
    lua_code = csMsgAll.get_CSLotteryDrawOnceMsg(groupId=4000103)
    wave = 1
    count_last = count_init
    res = {}
    price_list = []
    reward_all_dict = {}
    while True:

        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True

        # 发送消息
        bp.lua_console(lua_code)

        msg_name = "LotteryDrawOnceMsg"

        target_log = bp.receive_until_get_msg(msg_name=msg_name)

        if target_log is None:
            continue

        key2 = "type"
        type = luaLog.get_value(msg=target_log, key=key2, is_str=False)
        if type == "2":
            reward_dict = get_small_reward_dict(bp, price_list, wave)
            price_list = []
            res[f"第{wave}轮奖励"] = reward_dict
            count_cur = bp.get_item_count(item_tpid="102200")
            res[f"第{wave}轮消耗"] = count_last - count_cur
            count_last = count_cur
            wave += 1
            for reward in reward_dict:
                if reward in reward_all_dict:
                    reward_all_dict[reward] += reward_dict[reward]
                    continue
                reward_all_dict[reward] = reward_dict[reward]
            p = get_price(bp)
            # print(p[-1], target_index)
            if p[-1] == target_index:
                res["总大奖"] = p
                break
        else:
            # 根据期望键拿到值
            key1 = "prize"
            prize = luaLog.get_value(msg=target_log, key=key1, is_str=False)
            price_list.append(prize)

        key3 = "isFinal"
        isFinal = luaLog.get_value(msg=target_log, key=key3, is_str=False)
        if isFinal == "true":
            price_list = get_price(bp)
            res["总大奖"] = price_list
            break
    count_cur = bp.get_item_count(item_tpid="102200")
    cost = count_init - count_cur
    res["总奖励"] = sort_dict_recursively(reward_all_dict)
    res["总消耗"] = cost
    return res


def lua_list_to_python_list(lua_str, list_name):
    # 使用正则表达式匹配列表内容
    start = lua_str.find(f'["{list_name}"] =')
    if start == -1:
        return []

    end = lua_str.find('},', start)
    if end == -1:
        return []

    list_content = lua_str[start:end]
    numbers = []
    for line in list_content.split('\n'):
        if '=' in line:
            try:
                number = int(line.split('=')[1].strip().rstrip(','))
                numbers.append(number)
            except ValueError:
                continue
    return numbers


def main(bp: BasePage):
    cur = 0
    # 实验次数
    times = 100
    cost_max = 0
    cost_min = sys.maxsize
    small_reward_all = {}
    big_reward_all = {}
    cost_all = 0
    while cur < times:
        # 重置
        bp.cmd("Lottery reset")
        bp.sleep(0.5)

        # target_index代表目标是1-5哪个大奖
        res = lottery_draw(bp)
        print(res)
        if res["总消耗"] > cost_max:
            cost_max = res["总消耗"]
        if res["总消耗"] < cost_min:
            cost_min = res["总消耗"]
        cost_all += res["总消耗"]
        for reward in res["总奖励"]:
            if reward in small_reward_all:
                small_reward_all[reward] += res["总奖励"][reward]
                continue
            small_reward_all[reward] = res["总奖励"][reward]

        for reward in res["总大奖"]:
            if reward in big_reward_all:
                big_reward_all[reward] += 1
                continue
            big_reward_all[reward] = 1
        # 不填的话就不设目标
        # lottery_draw(bp)
        cur += 1
        if cur % 10 == 0:
            print("---------------------------")
            print(f"{cur}次实验,总计消耗{cost_all}，总计奖励{small_reward_all},总计大奖{sort_dict_recursively(big_reward_all)}")
            print(f"总消耗最小{cost_min}，最大{cost_max}")
            print("---------------------------")


if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20052")
    main(bp)
    bp.connect_close()
