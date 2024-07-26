import multiprocessing
import random

from airtest.core.api import connect_device

from common.basePage import BasePage
from netMsg import csMsgAll, luaLog


def get_CSCooperateSpinMsg(spinLevel=1, index=1):
    lua_code = csMsgAll.get_CSGlobalCooperateSpinMsg(spinLevel=spinLevel, index=index)
    lua_code = lua_code.replace("Global", "")
    return lua_code


def spin_test(bp: BasePage):
    lua_code = get_CSCooperateSpinMsg()

    # 实验次数
    times = 500

    # 增加相应的共建代币
    bp.cmd(f"add 1 101700 {times * 10}")

    # with open("../statistics/spin_log.txt", "w") as file:
    #     pass  # 不做任何操作,关闭文件即可清空内容

    cur = 0
    while cur < times:
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        cur += 1

    # 等待消息接收完毕
    bp.sleep(10)
    print("转盘模拟结束")

def worker(serial_number):
    dev = connect_device(f"android://127.0.0.1:5037/{serial_number}")
    bp = BasePage(dev=dev)
    bp.set_item_count(target_count=50000, item_tpid="101700")
    r2cost = {0: 1, 1: 2, 2: 3, 3: 5, 4: 10, 5: 20, 6: 50}
    success_count = 0
    cur = 0
    while cur < 500:
        cur += 1
        print(f"{serial_number}第{cur}次转")
        # 清空消息列表 开始收消息
        bp.log_list.clear()
        bp.log_list_flag = True
        r = random.randint(0, 6)
        r = 0
        cost = r2cost[r]
        lua_code = get_CSCooperateSpinMsg(spinLevel=cost)
        # 发送消息
        bp.lua_console(lua_code)
        r = random.randint(0, 9)
        sleep_time = 1.5 + r/10
        print(sleep_time)
        bp.sleep(sleep_time)

        # 在最近收集的消息列表中筛出目标消息
        key_sc = '<==== [Lua] Receive Net Msg "SC'
        msg_name = "CooperateSpinMsg"
        msg_key = key_sc + msg_name
        target_log = get_target_log(bp, msg_key)
        print(target_log)
        if target_log != "":
            # 根据键拿到值
            res = luaLog.get_value(msg=target_log, key="msg", is_str=True)
            if res == "success":
                success_count += 1
                continue
            print(target_log)
    print(f"{serial_number}:{success_count}")

def get_target_log(bp, msg_key):
    target_log = ""
    for log in bp.log_list:
        if msg_key not in log:
            continue
        target_log = log
        break
    return target_log
def spin_together_test():
    # 设备列表
    serial_number_list = ["127.0.0.1:21503", "127.0.0.1:21653"]

    process_list = []
    for serial_number in serial_number_list:
        p = multiprocessing.Process(target=worker,
                                    args=(serial_number, ))
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()





if __name__ == '__main__':
    bp = BasePage()
    spin_test(bp)
    bp.connect_close()