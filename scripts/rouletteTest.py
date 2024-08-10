import sys

from common.basePage import BasePage
from netMsg import csMsgAll, luaLog
from panelObjs.commonWebViewPanel import CommonWebViewPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.pvpHallPanel import PVPHallPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.roulettePanel import RoulettePanel
from tools.commonTools import *
from common import resource, gameInit


def sort_dict_keys_single(d):
    if not isinstance(d, dict):
        raise ValueError("Input must be a dictionary.")

    # 对字典的键进行排序
    sorted_dict = dict(sorted(d.items()))
    return sorted_dict


def get_ave_dict(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list of dictionaries.")

    ave_dict = {}
    for d in data:
        if not isinstance(d, dict):
            raise ValueError("All elements in the list must be dictionaries.")
        for key, value in d.items():
            if key in ave_dict:
                ave_dict[key] += value
            else:
                ave_dict[key] = value
    for a in ave_dict:
        ave_dict[a] //= len(data)

    return ave_dict

def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "levelupto 21", "add 2 201001 10000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    # 去转盘界面
    bp.go_to_panel("PVPHallPanel")
    bp.sleep(1)
    PVPHallPanel.click_btn_turntable(bp)
    bp.sleep(1)

    # 点击玩法说明
    RoulettePanel.click_btn_i(bp)
    bp.sleep(1)
    RoulettePanel.click_btn_i(bp)

    # 点击公示
    RoulettePanel.click_btn_announcement(bp)
    CommonWebViewPanel.wait_for_btn_close_appear(bp)
    CommonWebViewPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点击旋转
    RoulettePanel.click_btn_spin(bp)
    bp.sleep(3)

    # 按压旋转
    RoulettePanel.press_btn_spin(bp, 1)
    bp.sleep(20)

    RoulettePanel.click_btn_spin(bp)
    bp.sleep(1)

    RoulettePanel.click_btn_close(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    bp.go_home()

# 自定义排序函数，以获取数字进行排序
def extract_number(text):
    if text.isdigit():
        return int(text)
    else:
        # 提取所有数字部分并转为整数，如果键中包含非数字部分，则保持不变，适合更复杂场景
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else text


def draw_msg_test(bp: BasePage, lv, times):
    # 初始化
    bp.set_item_count(target_count=times * 500, item_tpid="201001")
    bp.cmd(f"roulettesetlv {lv}")
    lua_code = csMsgAll.get_CSRouletteDrawMsg(lv=lv, groupId=1)
    table_data = bp.excelTools.get_table_data("ROULETTE.xlsm")


    # 进行times次实验
    cur = 0
    n = 0
    count_list = []
    res_list = []
    res_dict = {}
    p = format(cur / times, ".1%")
    sys.stdout.write(f"\r进度: {p}")
    while cur < times:
        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True

        # 发送消息
        bp.lua_console(lua_code)

        msg_name = "RouletteDrawMsg"

        target_log = bp.receive_until_get_msg(msg_name=msg_name)
        if target_log is None:
            continue

        # 根据期望键拿到值
        key1 = "newLv"
        newLv = luaLog.get_value(msg=target_log, key=key1, is_str=False)

        key2 = "gotIndex"
        gotIndex = luaLog.get_value(msg=target_log, key=key2, is_str=False)
        index = table_data["level"].index(lv)
        reward = table_data["rewards"][int(gotIndex)]
        tpid = reward["tpId"][index]
        count = reward["count"][index]
        n += 1
        if newLv != "-1":
            count_list.append(n)
            bp.cmd(f"roulettesetlv {lv}")
            n = 0
        res_list.append(gotIndex)
        if tpid in res_dict:
            res_dict[tpid] += int(count)
        else:
            res_dict[tpid] = int(count)

        cur += 1
        p = format(cur / times, ".1%")
        sys.stdout.write(f"\r进度: {p}")

    # 输出结果
    print(f"\ncount_list:{count_list}")
    print(f"res_list:{res_list}")
    print(f"res_dict:{res_dict}")




def draw_to_level_once(bp: BasePage, lv, table_data):
    bp.cmd(f"roulettesetlv 1")
    get_dict = {}
    bp.sleep(1)
    cur = 1
    while True:
        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True

        lua_code = csMsgAll.get_CSRouletteDrawMsg(lv=cur, groupId=1)
        bp.lua_console(lua_code)

        msg_name = "RouletteDrawMsg"

        target_log = bp.receive_until_get_msg(msg_name=msg_name)
        if target_log is None:
            continue
        # 根据期望键拿到值
        key1 = "newLv"
        newLv = luaLog.get_value(msg=target_log, key=key1, is_str=False)
        key2 = "gotIndex"
        gotIndex = luaLog.get_value(msg=target_log, key=key2, is_str=False)
        index = table_data["level"].index(lv)
        reward = table_data["rewards"][int(gotIndex)]
        tpid = reward["tpId"][index]
        count = reward["count"][index]
        if tpid in get_dict:
            get_dict[tpid] += int(count)
        else:
            get_dict[tpid] = int(count)
        if newLv != "-1":
            if cur >= lv:
                break
            cur = int(newLv)
    return sort_dict_keys_single(get_dict)


def draw_to_level(bp: BasePage, lv, n):
    table_data = bp.excelTools.get_table_data("ROULETTE.xlsm")
    count_init = 1000000
    res_list = []
    get_list = []
    cur = 0
    p = format(cur / n, ".1%")
    sys.stdout.write(f"\r进度: {p}")
    while cur < n:
        # 初始化
        bp.set_item_count(target_count=count_init, item_tpid="201001")
        get_dict = draw_to_level_once(bp, lv, table_data)
        get_list.append(get_dict)
        count_cur = bp.get_item_count(item_tpid="201001")
        res_list.append(count_init - count_cur)
        cur += 1
        p = format(cur / n, ".1%")
        sys.stdout.write(f"\r进度: {p}")

    cost_total = 0

    cur = 0
    while cur < len(res_list):
        cost_total += res_list[cur]
        cur += 1
    get_ave = get_ave_dict(get_list)

    print(f"\n拿到{lv}级大奖\n平均消耗{cost_total // n}转轮券")
    print(f"消耗数量为{res_list}")
    print(f"平均获得{get_ave}")
    print(f"获得奖励为{get_list}")









if __name__ == '__main__':
    bp = BasePage()
    # # 指定lv转times次的消耗
    # draw_msg_test(bp, 5, 1000)

    # 转到指定lv n次消耗和奖励
    draw_to_level(bp, 10, 5)

    bp.connect_close()

