from common.basePage import BasePage
from netMsg import fishingMsg


if __name__ == '__main__':
    bp = BasePage()
    # 设置体力
    bp.set_item_count(target_count=1000000, item_tpid="100500")
    bp.cmd("mode 400302 390011")
    # 重置清空log
    with open("../statistics/log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容
    fishingMsg.fish(bp, [
        # {"spot_id": f"40030203", "times": 1000, "energy_cost": 50, "targetIdList": ["391011"]},
        {"spot_id": f"40030213", "times": 10},
        #
    ])

    # 等待时间，视前面的操作累计时长而定，主要用于保持连接打log
    bp.sleep(3)
    bp.connect_close()






















