# coding=utf-8

from common.basePage import BasePage
from netMsg import fishingMsg


if __name__ == '__main__':
    """
        必填项：
            "spot_id": 钓点id (str)
            "times": 钓鱼次数 (int)
        可选项
            "is_limited_spot": 新主线藏宝图标志 (bool), True为藏宝图，False或不填为非藏宝图 
            "is_activity_spot": 双周活动开启标志 (bool), True为双周活动渔场，False或不填为非双周活动渔场
            "energy_cost": 藏宝图设定体力 (int), 在藏宝图钓点不填则为一个默认体力, 非藏宝图钓点填不填都不生效 
            "target_id_list": 目标鱼id列表 (list[str]), 当钓到列表中的鱼时停止钓鱼
            "ignore_id_list": 忽略鱼id列表 (list[str]), 当钓到列表中的鱼时, 该鱼结果相当于拉断线
            
    """
    bp = BasePage()
    # 设置体力
    bp.set_item_count(target_count=1000000, item_tpid="100500")

    # setSceneType x (x=1是pve，x=2是pvp, x=3是钓者挑战, x=4是新主线, x=5是爬塔)
    bp.custom_cmd("setSceneType 4")
    # 重置清空log
    with open("../statistics/new_hook_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容
    with open("../statistics/new_cast_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容

    # 钓一张藏宝图
    bp.cmd("mode 500301 399002")
    bp.sleep(0.1)
    fishingMsg.fish(bp, [
        {"spot_id": "10106", "times": 1},
        # {"spot_id": f"40030214", "times": 1000, "energy_cost": 50},
    ])
    bp.sleep(0.1)

    # 钓鱼
    bp.cmd("mode 0 0")
    bp.sleep(0.1)
    fishingMsg.fish(bp, [
        {"spot_id": "10106", "times": 100, "energy_cost": 1000, "is_limited_spot": True},
        # {"spot_id": f"40030214", "times": 1000, "energy_cost": 50},
    ])

    # 等待时间，视前面的操作累计时长而定，主要用于保持连接打log
    bp.sleep(2000)
    bp.connect_close()
    # fishingMsg.fish(bp, [{"spot_id": f"40030203", "times": 3000, "energy_cost": 50, "targetIdList":[f"391011",f"391012", f"391013", f"391014", f"391015", f"391016"],"ignoreIdList:[]"}])













