# coding=utf-8

from common.basePage import BasePage
from common.rpcMethod import *
from netMsg import fishingMsg


if __name__ == '__main__':
    bp = BasePage()
    # 设置体力
    # bp.set_item_count(target_count=10000000, item_tpid="100500")
    # # bp.lua_console(lua_code)
    fishingMsg.fish(bp, [{"spot_id": "40030304", "times": 10, "energy_cost": 20}, {"spot_id": "40030304", "times": 10, "energy_cost": 30}])











