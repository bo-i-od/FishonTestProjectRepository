import sys

from common.basePage import BasePage
from netMsg import csMsgAll, luaLog
from panelObjs.commonWebViewPanel import CommonWebViewPanel
from panelObjs.playerLevelupPanel import PlayerLevelupPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.roulettePanel import RoulettePanel
from tools.commonTools import *
from common import resource, gameInit


def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip", "levelupto 21", "add 2 201001 10000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()

    bp.go_to_panel("RoulettePanel")
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
    bp.set_item_count(target_count=times * 500, item_tpid="201001")
    bp.cmd(f"roulettesetlv {lv}")
    lua_code = csMsgAll.get_CSRouletteDrawMsg(lv=lv, groupId=1)
    cur = 0
    n = 0
    count_list = []
    res_list = []
    while cur < times:
        p = format(cur / times, ".1%")
        sys.stdout.write(f"\r进度: {p}")
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

        n += 1
        if newLv != "-1":
            count_list.append(n)
            bp.cmd(f"roulettesetlv {lv}")
            n = 0
        res_list.append(gotIndex)
        cur += 1
    print(f"\ncount_list:{count_list}")
    print(f"res_list:{res_list}")
    result_dict = {}
    cur = 0
    while cur < len(res_list):
        if res_list[cur] not in result_dict:
            result_dict[res_list[cur]] = 1
            cur += 1
            continue
        result_dict[res_list[cur]] += 1
        cur += 1
    # 按键的数值部分排序并生成新字典
    sorted_dict = dict(sorted(result_dict.items(), key=lambda item: extract_number(item[0])))
    print(f"result_dict:{sorted_dict}")
    # 转成百分比结果
    result_percentage = {}
    for r in sorted_dict:
        result_percentage[r] = format(sorted_dict[r] / times, ".2%")
    print(f"result_percentage:{result_percentage}")







if __name__ == '__main__':
    bp = BasePage()
    draw_msg_test(bp, 8, 10)

