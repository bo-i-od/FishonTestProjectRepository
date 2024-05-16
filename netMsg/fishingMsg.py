from common.basePage import BasePage
from common import rpcMethod

# def get_CSFishingSaveLimitedSpotEnergyCostIdMsg(bp:BasePage, energy_cost:int):
#     table_data = bp.excelTools.get_table_data("FISH_ACTIVITY_SPOT_ENERGY.xlsm")
#     energyCost_list = table_data['energyCost']
#     tpId_list = table_data['tpId']
#     index = energyCost_list.index(energy_cost)
#     luaCode = ('local cmd = NetworkMgr:NewMsg("CSFishingSaveLimitedSpotEnergyCostIdMsg")\n'
#                f'cmd.chooseEnergyCostId = {tpId_list[index]}\n'
#                'NetworkMgr:Send(cmd)')
#     return luaCode


def fish(bp: BasePage, arg_list):
    scene_to_rod = {"400301": "500001",
                    "400302": "500002",
                    "400303": "500001",
                    "400304": "500004",
                    "400305": "500003",
                    "400306": "500006",
                    "400307": "500005",
                    "400308": "500008",
                    "400309": "500004",
                    "400310": "500005",
                    "400311": "500008",
                    "400312": "500008",
                    "400317": "500004",
                    }
    execute_list = []
    cur = 0
    while cur < len(arg_list):
        spot_id = arg_list[cur]["spot_id"]
        scene_id = spot_id[:6]
        rod_id = scene_to_rod[scene_id]
        times = arg_list[cur]["times"]
        execute_dict = {"spotId": spot_id, "times": times, "rodId": rod_id}
        if "targetIdList" in arg_list[cur]:
            execute_dict["targetIdList"] = arg_list[cur]["targetIdList"]
        if "ignoreIdList" in arg_list[cur]:
            execute_dict["ignoreIdList"] = arg_list[cur]["ignoreIdList"]
        if "energy_cost" in arg_list[cur]:
            energy_cost =arg_list[cur]["energy_cost"]
            table_data = bp.excelTools.get_table_data("FISH_ACTIVITY_SPOT_ENERGY.xlsm")
            energyCost_list = table_data['energyCost']
            tpId_list = table_data['tpId']
            index = energyCost_list.index(energy_cost)
            execute_dict["energyCostId"] = tpId_list[index]
        execute_list.append(execute_dict)
        cur += 1
    rpcMethod.fish(bp.poco, execute_list)

