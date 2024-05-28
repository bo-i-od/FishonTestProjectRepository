# coding=utf-8

from common.basePage import BasePage
from netMsg import fishingMsg


if __name__ == '__main__':
    bp = BasePage()
    # 设置体力
    # bp.set_item_count(target_count=1000000, item_tpid="100500")
    fishingMsg.fish(bp, [{"spot_id": f"40030101", "times": 100, "energy_cost": 50}])
    while True:
        bp.sleep(10000)
    # fishingMsg.fish(bp, [{"spot_id": f"40030203", "times": 3000, "energy_cost": 50, "targetIdList":[f"391011",f"391012", f"391013", f"391014", f"391015", f"391016"],"ignoreIdList:[]"}])













