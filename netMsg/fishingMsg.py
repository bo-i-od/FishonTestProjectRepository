from common.basePage import BasePage


def get_CSFishingSaveLimitedSpotEnergyCostIdMsg(bp:BasePage, energy_cost:int):
    table_data = bp.excelTools.get_table_data("FISH_ACTIVITY_SPOT_ENERGY.xlsm")
    energyCost_list = table_data['energyCost']
    tpId_list = table_data['tpId']
    index = energyCost_list.index(energy_cost)
    luaCode = ('local cmd = NetworkMgr:NewMsg("CSFishingSaveLimitedSpotEnergyCostIdMsg")\n'
               f'cmd.chooseEnergyCostId = {tpId_list[index]}\n'
               'NetworkMgr:Send(cmd)')
    return luaCode


if __name__ == '__main__':
    bp = BasePage()
    get_CSFishingSaveLimitedSpotEnergyCostIdMsg(bp, 30)