from common.basePage import BasePage
from common import rpcMethodRequest


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
                    "400320": "500001",
                    "400321": "500001",
                    "400322": "500004",
                    "500301": "500001",
                    "500302": "500001",
                    }
    rod_id = scene_to_rod[scene_id]
    return rod_id


def fish(bp: BasePage, arg_list):
    execute_list = []
    cur = 0
    while cur < len(arg_list):
        spot_id = arg_list[cur]["spot_id"]
        scene_id = bp.spot_id_to_fishery_id(spot_id=spot_id)
        rod_id = get_rod_id(scene_id)

        times = arg_list[cur]["times"]
        execute_dict = {"spotId": spot_id, "sceneId": scene_id, "times": times, "rodId": rod_id, "isActivitySpot": False, "isLimitedSpot": False}
        if "target_id_list" in arg_list[cur]:
            execute_dict["targetIdList"] = arg_list[cur]["target_id_list"]
        if "ignore_id_list" in arg_list[cur]:
            execute_dict["ignoreIdList"] = arg_list[cur]["ignore_id_list"]
        execute_dict["isActivitySpot"] = False
        if "is_activity_spot" in arg_list[cur]:
            execute_dict["isActivitySpot"] = arg_list[cur]["is_activity_spot"]
        if "is_limited_spot" in arg_list[cur]:
            execute_dict["isLimitedSpot"] = arg_list[cur]["is_limited_spot"]
        if "energy_cost" in arg_list[cur]:
            energy_cost = arg_list[cur]["energy_cost"]
            table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="energyCost", value=energy_cost, book_name="FISH_ACTIVITY_SPOT_ENERGY.xlsm")
            tpId = table_data_object["tpId"]
            execute_dict["energyCostId"] = tpId

            # table_data = bp.excelTools.get_table_data("FISH_ACTIVITY_SPOT_ENERGY.xlsm")
            # energyCost_list = table_data['energyCost']
            # tpId_list = table_data['tpId']
            # try:
            #     index = energyCost_list.index(energy_cost)
            #     execute_dict["energyCostId"] = tpId_list[index]
            # except ValueError:
            #     pass
        execute_list.append(execute_dict)
        cur += 1
    rpcMethodRequest.fish(bp.poco, execute_list)

def fish_all(bp: BasePage):
    bp.cmd("add 1 100500 1000000")
    fishery_id_list = bp.get_fishery_id_list()

    cur = 0
    while cur < len(fishery_id_list):
        fishery_id = fishery_id_list[cur]
        fish_id_list = bp.get_fish_id_list(fishery_id)
        spot_id_list, is_in_double_week, _ = bp.get_spot_id_list(fishery_id=fishery_id)
        spot_id = spot_id_list[0]
        for fish_id in fish_id_list:
            cmd = f"mode {fishery_id} {fish_id}"
            print(cmd)
            bp.cmd(cmd)
            bp.sleep(0.1)
            fish(bp, [
                 {"spot_id": f"{spot_id}", "times": 1, "is_activity_spot": is_in_double_week}])
            bp.sleep(0.4)
        cur += 1

if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533", is_mobile_device=True)
    fish_all(bp)
    bp.connect_close()


