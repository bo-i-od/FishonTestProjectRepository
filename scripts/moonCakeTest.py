import sys
import time

from common.basePage import BasePage
from netMsg import fishingMsg
from netMsg import csMsgAll
from scripts import createUsers
from tools import commonTools


def energy_cost_once_test(bp: BasePage, energy_cost, step=10):
    bp.set_item_count(target_count=100000, item_tpid="100500")
    bp.set_item_count_list(target_count_list=[0, 0, 0], item_tpid_list=["290014", "290015", "290016"])
    if energy_cost == 1:
        spot_id = "40030101"
    elif energy_cost == 3:
        spot_id = "40030102"
    elif energy_cost == 10:
        spot_id = "40030103"
    else:
        spot_id = "40030104"

    if energy_cost > 10:
        # bp.cmd("mode 400301 399001")
        # bp.sleep(1)
        # fishingMsg.fish(bp, [{"spot_id": "40030103", "times": 1, "energy_cost": energy_cost, "is_activity_spot": False}])
        # bp.sleep(1)
        # bp.cmd("mode 0 0")
        # bp.sleep(1)
        bp.sleep(1)
        bp.set_item_count(target_count=energy_cost * 110, item_tpid="100500")
        bp.sleep(2)
        fishingMsg.fish(bp, [
            {"spot_id": "40030103", "times": 30, "energy_cost": energy_cost, "is_activity_spot": False, "target_id_list": ["399001"]}])
        bp.sleep(5)
        bp.set_item_count(target_count=100000, item_tpid="100500")

    energy_cost_total = 0
    while True:
        fishingMsg.fish(bp, [
            {"spot_id": spot_id, "times": step, "energy_cost": energy_cost, "is_activity_spot": False, "target_id_list": []}])
        energy_cost_total += energy_cost * step
        bp.sleep(0.2 * step)
        item_count_list = bp.get_item_count_list(item_tpid_list=["290014", "290015", "290016"])
        output = f"当前体力消耗：{energy_cost_total}，月饼材料数量：{item_count_list}"
        # 打印并刷新 stdio
        sys.stdout.write(f"\r{output}")
        sys.stdout.flush()

        is_collect_completed = True
        for item_count in item_count_list:
            if item_count < 60:
                is_collect_completed = False
                break
        if not is_collect_completed:
            continue
        return energy_cost_total


def energy_cost_test(bp: BasePage):
    start = 380
    end = 390
    times = end - start
    energy_cost = 2000
    prefix = "w"
    cur = start
    energy_cost_total_list = []
    while cur < end:
        name = prefix + str(cur)
        createUsers.login(bp, name)
        bp.cmd("levelupto 16")
        energy_cost_total = energy_cost_once_test(bp, energy_cost=energy_cost, step=1)
        energy_cost_total_list.append(energy_cost_total)
        print(f"第{cur}次实验结果为：{energy_cost_total}")
        createUsers.logout(bp)
        cur += 1
    res = 0
    for energy_cost_total in energy_cost_total_list:
        res += energy_cost_total
    energy_ave = res // times
    print(f"总试验次数为{times}, 实验结果为{energy_cost_total_list}, 平均消耗体力{energy_ave}")


def exchange_once_test(bp: BasePage, exchange_id):
    bp.set_item_count_list(target_count_list=[60, 60, 60], item_tpid_list=["290014", "290015", "290016"])
    lua_code = csMsgAll.get_CSExchangeItemsMsg(exchangeId=exchange_id, num=60)

    # 清空消息列表 开始收消息
    bp.log_list.clear()
    bp.log_list_flag = True

    # 发送消息
    bp.lua_console(lua_code)

    msg_name = "ExchangeItemsMsg"
    target_log = bp.receive_until_get_msg(msg_name=msg_name)
    python_dict = commonTools.lua_dict_to_python_dict(target_log)
    items = python_dict["items"]["tiacs"]
    res = {}
    for index in items:
        item = items[index]
        id = item["id"]
        count = item["count"]
        if id in res:
            res[id] += count
            continue
        res[id] = count
    return res


def exchange_test(bp):
    start = 0
    end = 20
    times = end - start
    exchange_id = 2003
    res = {}
    prefix = "w"
    cur = start
    while cur < end:
        name = prefix + str(cur)
        createUsers.login(bp, name)
        bp.cmd("levelupto 16")
        res_once = exchange_once_test(bp, exchange_id=exchange_id)
        print(f"第{cur}次实验结果为：{res_once}")
        for r in res_once:
            if r in res:
                res[r] += res_once[r]
                continue
            res[r] = res_once[r]
        cur += 1
        createUsers.logout(bp)
    moon_cake_list = [0, 0, 0]

    if 290011 in res:
        moon_cake_list[0] = res[290011] * 20
    if 290012 in res:
        moon_cake_list[1] = res[290012] * 80
    if 290013 in res:
        moon_cake_list[2] = res[290013] * 200
    energy_ave = (moon_cake_list[0] + moon_cake_list[1] + moon_cake_list[2]) // times
    print(f"总试验次数为{times}, 实验结果为{res}, 平均获得体力{energy_ave}")


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523", is_mobile_device=True)
    energy_cost_test(bp)

    bp.connect_close()