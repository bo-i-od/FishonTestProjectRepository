# coding=utf-8

from common.basePage import BasePage
from netMsg import fishingMsg


if __name__ == '__main__':
    bp = BasePage()
    # 设置体力
    # bp.set_item_count(target_count=1000000, item_tpid="100500")
    # setSceneType x (x=1是pve，x=2是pvp, x=4是新主线)
    bp.custom_cmd("setSceneType 4")
    # 重置清空log
    with open("../statistics/hook_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容
    with open("../statistics/cast_log.txt", "w") as file:
        pass  # 不做任何操作,关闭文件即可清空内容
    fishingMsg.fish(bp, [
        {"spot_id": "10106", "times": 500, "energy_cost": 500, "is_activity_spot": False},
        # {"spot_id": f"40030214", "times": 1000, "energy_cost": 50},
    ])

    # 等待时间，视前面的操作累计时长而定，主要用于保持连接打log
    bp.sleep(2000)
    bp.connect_close()
    # fishingMsg.fish(bp, [{"spot_id": f"40030203", "times": 3000, "energy_cost": 50, "targetIdList":[f"391011",f"391012", f"391013", f"391014", f"391015", f"391016"],"ignoreIdList:[]"}])













