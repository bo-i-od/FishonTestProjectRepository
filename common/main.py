# coding=utf-8

from common.basePage import BasePage
from netMsg import fishingMsg
import sys

if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20030")
    # bp.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
    bp.cmd("mode 0 0")
    bp.set_item_count(target_count=10000000, item_tpid="100500")
    fishingMsg.fish(bp, [{"spot_id": f"40030803", "times": 8, "energy_cost": 50, "targetIdList":["399001"]}])

    # index =2
    # fishingMsg.fish(bp, [{"spot_id": f"40030203", "times": 3000, "energy_cost": 50, "targetIdList":[f"391011",f"391012", f"391013", f"391014", f"391015", f"391016"]}])
    # # [f"370{index}01",f"370{index}02", f"370{index}03", f"370{index}04"]
    # arg_list = []
    # cur = 11
    # while cur < 13:
    #     scene_id = str(cur).zfill(2)
    #     i = 1
    #     while i < 4:
    #         arg = {"spot_id": f"4003{scene_id}0{i}", "times": 3000, "energy_cost": 50}
    #         arg_list.append(arg)
    #         i += 1
    #     cur += 1
    # i = 1
    # while i < 4:
    #     arg = {"spot_id": f"4003170{i}", "times": 3000, "energy_cost": 50}
    #     arg_list.append(arg)
    #     i += 1
    # print(arg_list)
    # fishingMsg.fish(bp, arg_list=arg_list)
    # ["370401","370402","370403","370404"]
    # ["390033", "390034", "390035", "390036"]
    # spot_id = sys.argv[1]
    # times = sys.argv[2]
    # energy_cost = sys.argv[3]
    # 设置体力
    # bp.set_item_count(target_count=1000000, item_tpid="100500")
    # fishingMsg.fish(bp, [{"spot_id": spot_id, "times": int(times), "energy_cost": int(energy_cost)}])
    # bp.cmd("mode 0 0")
    # cur = 0
    # while cur < int(times):
    #     fishingMsg.fish(bp, [{"spot_id": spot_id, "times": 1, "energy_cost": int(energy_cost)}])
    #     bp.sleep(0.5)
    #     cur += 1












