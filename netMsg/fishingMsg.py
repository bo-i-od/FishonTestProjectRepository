from common.basePage import BasePage
from common import rpcMethodRequest
from netMsg.csMsg import fishing_cs


def get_CSFishingSaveLimitedSpotEnergyCostIdMsg(bp:BasePage, energy_cost:int):
    table_data = bp.excelTools.get_table_data("FISH_ACTIVITY_SPOT_ENERGY.xlsm")
    energyCost_list = table_data['energyCost']
    tpId_list = table_data['tpId']
    index = energyCost_list.index(energy_cost)
    chooseEnergyCostId = tpId_list[index]
    luaCode = fishing_cs.get_CSFishingSaveLimitedSpotEnergyCostIdMsg(chooseEnergyCostId=chooseEnergyCostId)
    return luaCode

def get_rod_id(scene_id):
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
                    "400313": "500007",
                    "400314": "500008",
                    "400315": "500007",
                    "400318": "500006",
                    "400319": "500003",
                    }
    rod_id = scene_to_rod[scene_id]
    return rod_id


def fish(bp: BasePage, arg_list):
    execute_list = []
    cur = 0
    while cur < len(arg_list):
        spot_id = arg_list[cur]["spot_id"]
        scene_id = spot_id[:6]
        rod_id = get_rod_id(scene_id)
        times = arg_list[cur]["times"]
        execute_dict = {"spotId": spot_id, "times": times, "rodId": rod_id}
        if "target_id_list" in arg_list[cur]:
            execute_dict["targetIdList"] = arg_list[cur]["target_id_list"]
        if "ignore_id_list" in arg_list[cur]:
            execute_dict["ignoreIdList"] = arg_list[cur]["ignore_id_list"]
        execute_dict["isActivitySpot"] = False
        if "is_activity_spot" in arg_list[cur]:
            execute_dict["isActivitySpot"] = arg_list[cur]["is_activity_spot"]
        if "energy_cost" in arg_list[cur]:
            energy_cost = arg_list[cur]["energy_cost"]
            table_data = bp.excelTools.get_table_data("FISH_ACTIVITY_SPOT_ENERGY.xlsm")
            energyCost_list = table_data['energyCost']
            tpId_list = table_data['tpId']
            try:
                index = energyCost_list.index(energy_cost)
                execute_dict["energyCostId"] = tpId_list[index]
            except ValueError:
                pass
        execute_list.append(execute_dict)
        cur += 1
    rpcMethodRequest.fish(bp.poco, execute_list)

