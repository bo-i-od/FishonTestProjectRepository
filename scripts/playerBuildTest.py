from common.basePage import BasePage
from netMsg import csMsgAll


def get_CSCooperateSpinMsg():
    lua_code = csMsgAll.get_CSGlobalCooperateSpinMsg(spinLevel=1, index=1)
    lua_code = lua_code.replace("Global", "")
    return lua_code


def spin_test(bp: BasePage):
    lua_code = get_CSCooperateSpinMsg()

    # 实验次数
    times = 5000

    # 增加相应的共建代币
    bp.cmd(f"add 1 101700 {times}")

    with open("../statistics/spin_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容

    cur = 0
    while cur < times:
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        cur += 1

    # 等待消息接收完毕
    bp.sleep(10)





if __name__ == '__main__':
    bp = BasePage()
    spin_test(bp)
    bp.connect_close()