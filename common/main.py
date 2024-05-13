# coding=utf-8

from common.basePage import BasePage
from common.rpcMethod import *
from netMsg.fishingMsg import *


if __name__ == '__main__':
    bp = BasePage()
    # 设置体力
    # bp.set_item_count(target_count=10000000, item_tpid="100500")
    # 设置藏宝图体力
    # # lua_code = get_CSFishingSaveLimitedSpotEnergyCostIdMsg(bp, energy_cost=100)
    # # bp.lua_console(lua_code)
    fish(bp.poco, [{"spotId": "40031101", "times": 10}, {"spotId": "40030102", "times": 10}])











