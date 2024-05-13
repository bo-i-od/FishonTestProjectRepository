# coding=utf-8

from common.basePage import BasePage
from common.rpcMethod import *
from netMsg.fishingMsg import *


if __name__ == '__main__':
    bp = BasePage()
    fish(bp.poco, [{"spotId": "40031101", "times": 10}, {"spotId": "40030102", "times": 10}])
    # bp.set_item_count(target_count=100000, item_tpid="100500")
    # # lua_code = get_CSFishingSaveLimitedSpotEnergyCostIdMsg(bp, energy_cost=100)
    # # bp.lua_console(lua_code)
    # cur = 0
    # while cur < 10000:
    #     fish(bp.poco, [{"spot_id":"40031101", "times":1}])
    #     bp.sleep(0.35)
    #     cur += 1
    # bp.lua_console(luaCode)










