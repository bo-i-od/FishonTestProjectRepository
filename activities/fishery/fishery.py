import os
import sys

from openpyxl.reader.excel import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from activities.decl.BATTLE_PASS import BATTLE_PASS
from activities.decl.BATTLE_PASS_MAIN_2024 import BATTLE_PASS_MAIN_2024
from activities.decl.FISH import FISH
from activities.decl.FISHERIES import FISHERIES
from activities.decl.FISH_GOLDEN_SHOW import FISH_GOLDEN_SHOW
from activities.decl.FISH_STATE import FISH_STATE
from activities.decl.FISH_WEIGHT_NEW import FISH_WEIGHT_NEW
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MULTIPLAYER_ROOM_ENUM import MULTIPLAYER_ROOM_ENUM
from activities.decl.NEW_PLOT_CLUE_REWARD import NEW_PLOT_CLUE_REWARD
from activities.decl.NEW_PLOT_FISH_SPOT import *
from activities.decl.NEW_PLOT_FISH_TYPE_DROP import NEW_PLOT_FISH_TYPE_DROP
from activities.decl.NEW_PLOT_MAP_MAIN import NEW_PLOT_MAP_MAIN
from activities.decl.NEW_PLOT_MAP_POINT import NEW_PLOT_MAP_POINT
from activities.decl.NEW_PLOT_MAP_POINT_LANGUAGE import NEW_PLOT_MAP_POINT_LANGUAGE
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.fishery.load_tools import get_spot_fish_type_detail, get_fishery_info, get_exclude_info, \
    get_cfg_fishery, get_cfg_ndays, get_quest_info
from activities.fishery.temp.main_id import load_main_id, save_main_id
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *


"""
    新主线渔场配置模板
"""


def new_plot_fish_spot(excel_tool: ExcelToolsForActivities, fishery_id, tpId_start, fishery_cfg_list, fishery_info,exclude_info, bgm_name,fishery_name, scene_name_list, mapPointId_list, cfg_ndays):
    def get_quest_id(fish_id):
        # return excel_tool.get_table_data_object_by_key_value(key="triggerKeyS", value=fish_id, table_data_detail=new_plot_quest_detail)["tpId"]
        index = quest_info.index(fish_id)
        new_plot_quest_list = cfg_ndays["mission_cfg"]["new_plot_quest_list"]
        quest_id = new_plot_quest_list[index]
        return quest_id

    new_plot_fish_spot_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_FISH_SPOT.xlsm")
    # new_plot_quest_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_QUEST.xlsm")
    quest_info = get_quest_info(excel_tool=excel_tool, fishery_id=fishery_id)
    template_tpId_start = 10101
    key = "tpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId_start, table_data_detail=new_plot_fish_spot_detail)
    if table_data_object_list:
        mode = 2
        template_tpId_start = tpId_start
    else:
        mode = 1

    spot_fish_type_detail = get_spot_fish_type_detail()
    last_weight = {
        0: 0,
        1: 1000,
        2: 500,
        3: 334,
        4: 250,
        5: 200,
        6: 170,
     }
    cur = 0
    while cur < 8:
        exclude_list = exclude_info[cur]
        fishery_cfg = fishery_cfg_list[cur]
        counter = {"small": 0, "medium": 0, "large": 0, "hidden": 0, "boss": 0, "rare": 0, "elite": 0, "monster": 0, }
        instance_object: NEW_PLOT_FISH_SPOT
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail=new_plot_fish_spot_detail, cls=NEW_PLOT_FISH_SPOT)
        instance_object.id = tpId_start + cur
        instance_object.tpId = instance_object.id
        instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}-{instance_object.name.split('-')[1]}"
        instance_object.newPlotFisheriesId = fishery_id
        instance_object.multipleRoomId = fishery_id * 100 + cur % 4 + 1
        instance_object.needChapterLv = fishery_cfg["needChapterLv"]
        instance_object.needPlotQuestId = fishery_cfg["needPlotQuestId"]
        instance_object.needDay = fishery_cfg["needDay"]
        instance_object.smallInfo = []
        instance_object.mediumInfo = []
        instance_object.largeInfo = []
        instance_object.hugeInfo = []
        instance_object.giantInfo = []
        instance_object.rareInfo = []
        instance_object.eliteInfo = []
        instance_object.monsterInfo = []
        fish_type_detail = spot_fish_type_detail[cur]
        i = 0
        while i < 30:
            fish_info = fishery_info[i]
            if cur not in fish_info["fishSpot"]:
                i += 1
                continue
            fish_class = fish_info["fishClass"]

            if fish_class == 2:
                info = RAREINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["rare"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["rare"]
                if info.fishId in exclude_list:
                    info.excludeType = 1
                    info.excludeArgs = get_quest_id(fish_id=info.fishId)
                if counter["rare"] == 0:
                    info.weight = last_weight[fish_type_detail["rare"]]
                counter["rare"] += 1
                instance_object.rareInfo.append(info)
                i += 1
                continue
            if fish_class == 3:
                info = ELITEINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["elite"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["elite"]
                if info.fishId in exclude_list:
                    info.excludeType = 1
                    info.excludeArgs = get_quest_id(fish_id=info.fishId)
                if counter["elite"] == 0:
                    info.weight = last_weight[fish_type_detail["elite"]]
                counter["elite"] += 1
                instance_object.eliteInfo.append(info)
                i += 1
                continue
            if fish_class == 4:
                info = MONSTERINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["monster"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["monster"]
                if info.fishId in exclude_list:
                    info.excludeType = 1
                    info.excludeArgs = get_quest_id(fish_id=info.fishId)
                if counter["monster"] == 0:
                    info.weight = last_weight[fish_type_detail["monster"]]
                counter["monster"] += 1
                instance_object.monsterInfo.append(info)
                i += 1
                continue

            fish_type = fish_info["fishType"]
            if fish_type == 1:
                info = SMALLINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["small"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["small"]
                if counter["small"] == 0:
                    info.weight = last_weight[fish_type_detail["small"]]
                counter["small"] += 1
                instance_object.smallInfo.append(info)
                i += 1
                continue
            if fish_type == 2:
                info = MEDIUMINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["medium"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["medium"]
                if counter["medium"] == 0:
                    info.weight = last_weight[fish_type_detail["medium"]]
                counter["medium"] += 1
                instance_object.mediumInfo.append(info)
                i += 1
                continue
            if fish_type == 3:
                info = LARGEINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["large"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["large"]
                if counter["large"] == 0:
                    info.weight = last_weight[fish_type_detail["large"]]
                counter["large"] += 1
                instance_object.largeInfo.append(info)
                i += 1
                continue
            if fish_type == 4:
                info = HUGEINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["hidden"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["hidden"]
                if counter["hidden"] == 0:
                    info.weight = last_weight[fish_type_detail["hidden"]]
                counter["hidden"] += 1
                instance_object.hugeInfo.append(info)
                i += 1
                continue
            if fish_type == 5:
                info = GIANTINFO()
                info.fishId = fish_info["tpId"]
                if fish_type_detail["boss"] == 0:
                    info.weight = 0
                else:
                    info.weight = 1000 // fish_type_detail["boss"]
                if counter["boss"] == 0:
                    info.weight = last_weight[fish_type_detail["boss"]]
                counter["boss"] += 1
                instance_object.giantInfo.append(info)
                i += 1
                continue
            i += 1
        while len(instance_object.smallInfo) < 4:
            instance_object.smallInfo.append(SMALLINFO())
        while len(instance_object.mediumInfo) < 4:
            instance_object.mediumInfo.append(MEDIUMINFO())
        while len(instance_object.largeInfo) < 4:
            instance_object.largeInfo.append(LARGEINFO())
        while len(instance_object.hugeInfo) < 4:
            instance_object.hugeInfo.append(HUGEINFO())
        while len(instance_object.giantInfo) < 4:
            instance_object.giantInfo.append(GIANTINFO())
        while len(instance_object.rareInfo) < 6:
            instance_object.rareInfo.append(RAREINFO())
        while len(instance_object.eliteInfo) < 6:
            instance_object.eliteInfo.append(ELITEINFO())
        while len(instance_object.monsterInfo) < 6:
            instance_object.monsterInfo.append(MONSTERINFO())
        locate = instance_object.condition[1]
        scene_name = scene_name_list[locate - 1]
        time = instance_object.condition[0]
        instance_object.battleScene = f"{scene_name}_{fishery_name}_{time}"
        instance_object.backgroundPic = f"loading_fisheries_{scene_name}_{time}"
        if time == 1:
            instance_object.AmbScene = f"Amb_{bgm_name}_Day_Loop"
            instance_object.BgmScene = f"Bgm_{bgm_name}_Day"
        else:
            instance_object.AmbScene = f"Amb_{bgm_name}_Night_Loop"
            instance_object.BgmScene = f"Bgm_{bgm_name}_Night"
        instance_object.BgmBattle = f"Bgm_{bgm_name}_Monster"
        instance_object.BgmWin = f"Bgm_{bgm_name}_Win"
        instance_object.BgmFail = f"Bgm_{bgm_name}_Fail"
        instance_object.mapPointId = mapPointId_list[locate - 1]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=new_plot_fish_spot_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=new_plot_fish_spot_detail)
        cur += 1

def new_plot_fish_type_drop(excel_tool: ExcelToolsForActivities, fishery_id, ChapterId):
    new_plot_fish_type_drop_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_FISH_TYPE_DROP.xlsm")
    key = "tpId"
    template_tpId_start = 50030101
    tpId_start = fishery_id * 100 + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId_start, table_data_detail=new_plot_fish_type_drop_detail)
    if json_object_list:
        mode = 2
        template_tpId_start = tpId_start
    else:
        mode = 1
    cur = 0
    while cur < 2:
        instance_object: NEW_PLOT_FISH_TYPE_DROP
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail=new_plot_fish_type_drop_detail, cls=NEW_PLOT_FISH_TYPE_DROP)
        instance_object.tpId = tpId_start + cur
        instance_object.id = instance_object.tpId
        if cur == 0:
            instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}-无藏宝图"
        else:
            instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}-藏宝图"
        instance_object.ChapterId = ChapterId
        instance_object.newPlotFisheriesId = fishery_id
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_fish_type_drop_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_fish_type_drop_detail, instance_object=instance_object)
        cur += 1

def fish_golden_show(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index):
    fish_golden_show_detail = excel_tool.get_table_data_detail(book_name="FISH_GOLDEN_SHOW.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fish_golden_show_detail) + 1
    key = "tpId"
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id, fisheries_detail=fisheries_detail)
    cur = 0
    for fish_id in fish_id_list:
        if cur < 15:
            cur += 1
            continue
        instance_object: FISH_GOLDEN_SHOW
        json_object, instance_object = excel_tool.get_object(key=key, value=fish_id, table_data_detail=fish_golden_show_detail, cls=FISH_GOLDEN_SHOW)
        if instance_object:
            mode = 2
        else:
            mode = 1
            instance_object = FISH_GOLDEN_SHOW()
            instance_object.id = id_start + cur
        instance_object.tpId = fish_id
        instance_object.name = f"渔场{fishery_index}-{cur - 15 + 1}-改"
        asset_name = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_id, table_data_detail=fish_detail)["assetName"]
        instance_object.goldenShowImage = asset_name.split("/")[-1]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fish_golden_show_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fish_golden_show_detail, instance_object=instance_object)
        cur += 1

def fish_weight_new(excel_tool: ExcelToolsForActivities, fishery_info, fishery_index):
    #
    cfg = {
        1: {"minweight": 227, "firstRate": 597, "secondStar":78000, "secondRate": 426},
        2: {"minweight": 681, "firstRate": 1790, "secondStar":78000, "secondRate": 1276},
        3: {"minweight": 1134, "firstRate": 2983, "secondStar":78000, "secondRate": 2127},
        4: {"minweight": 4536, "firstRate": 11929, "secondStar":78000, "secondRate": 8505},
        5: {"minweight": 22680, "firstRate": 59645, "secondStar":78000, "secondRate": 42525},
        6: {"minweight": 23400, "firstRate": 2340, "secondStar":78000, "secondRate": 1661},
        7: {"minweight": 31200, "firstRate": 3120, "secondStar":78000, "secondRate": 2215},
        8: {"minweight": 39000, "firstRate": 3900, "secondStar":78000,"secondRate": 2769},
    }
    fish_weight_new_detail = excel_tool.get_table_data_detail(book_name="FISH_WEIGHT_NEW.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fish_weight_new_detail) + 1

    key = "fishId"
    cur = 0
    while cur < len(fishery_info):
        fish_info = fishery_info[cur]
        fish_id =fish_info["tpId"]
        instance_object: FISH_WEIGHT_NEW
        json_object, instance_object = excel_tool.get_object(key=key, value=fish_id, table_data_detail=fish_weight_new_detail, cls=FISH_WEIGHT_NEW)
        if instance_object:
            mode = 2
        else:
            mode = 1
            instance_object = FISH_WEIGHT_NEW()
            instance_object.id = id_start + cur
        instance_object.fishId = fish_id
        instance_object.name = f"渔场{fishery_index}-{cur % 15 + 1}"
        if cur > 14:
            instance_object.name += "-改"
        if fish_info["fishClass"] == 1:
            fish_kind = fish_info["fishType"]
        else:
            fish_kind = fish_info["fishClass"] + 4
        instance_object.minweight = cfg[fish_kind]["minweight"]
        instance_object.firstRate = cfg[fish_kind]["firstRate"]
        instance_object.secondRate = cfg[fish_kind]["secondRate"]
        instance_object.secondStar = cfg[fish_kind]["secondStar"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.fishId, table_data_detail=fish_weight_new_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.fishId, table_data_detail=fish_weight_new_detail, instance_object=instance_object)
        cur += 1

def fish(excel_tool: ExcelToolsForActivities, fishery_info, fishery_index, living):
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    key = "tpId"
    template_tpId_start = 350101
    cur = 0
    while cur < len(fishery_info):
        fish_info = fishery_info[cur]
        fish_id = fish_info["tpId"]
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fish_id, table_data_detail=fish_detail)
        if json_object_list:
            mode = 2
        else:
            mode = 1
            json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_tpId_start + cur, table_data_detail=fish_detail)
        instance_object: FISH
        instance_object = json_to_instance(json_object=json_object_list[0], cls=FISH)
        instance_object.tpId = fish_id
        instance_object.id = instance_object.tpId
        instance_object.name = f"渔场{fishery_index}-{cur % 15 + 1}"
        if cur > 14:
            instance_object.name += "-改"
            instance_object.boneId = 380001 + (fishery_index - 1) * 15 + cur % 15
            instance_object.glodBoneId = 385001 + (fishery_index - 1) * 15 + cur % 15
        else:
            instance_object.subspecies = [fish_id + 10000, 0]
        instance_object.fishType = fish_info["fishType"]
        instance_object.fishClass = fish_info["fishClass"]
        instance_object.fishcardId = 1010001 + (fishery_index - 1) * 15 + cur % 15
        asset_name_split = instance_object.assetName.split("/")
        instance_object.displayicon = asset_name_split[0] + "/" +asset_name_split[1]
        instance_object.newPlotBattleType = fish_info["newPlotBattleType"]
        instance_object.living = living
        instance_object.fishAI = fish_info["fishAI"]

        if fish_info["fishClass"] == 1 and fish_info["fishType"] < 4:
            instance_object.fishCardRoute = None
        else:
            instance_object.fishCardRoute = asset_name_split[-1]

        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fish_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fish_detail, instance_object=instance_object)
        cur += 1

def fisheries(excel_tool: ExcelToolsForActivities, fishery_id, icon_name, scene_name, fishery_info):
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    key = "tpId"
    template_tpId = 500301
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="tpId", value=template_tpId, table_data_detail=fisheries_detail)
    instance_object = json_to_instance(json_object=json_object_list[0], cls=FISHERIES)
    instance_object: FISHERIES
    if mode == 1:
        instance_object.id = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=fisheries_detail, start=instance_object.id)
    instance_object.name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    instance_object.tpId = fishery_id
    instance_object.displayicon = f"icon_fisheries_{icon_name}"
    instance_object.displayBlurBG = f"bg_fisheries_blur_{icon_name}"
    instance_object.displayBanner = f"home_banner_{icon_name}"
    instance_object.displayLoadingPic = f"loading_fisheries_{scene_name}_1"
    instance_object.cardPackIcon = f"FishCard_fisheries_{icon_name}"
    instance_object.battleScene = f"{icon_name}_NanaoIsland"
    instance_object.unlockKeyCost = 10000
    instance_object.unlockByFishing = 20
    fish_id_list = []
    for fish_info in fishery_info:
        fish_id_list.append(fish_info["tpId"])
    instance_object.fish = fish_id_list
    # 替换卡包奖励
    for totalPointAward in instance_object.totalPointAward:
        totalPointAward.tpId = excel_tool.change_fish_bag_fishery(fish_bag_id=totalPointAward.tpId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fisheries_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fisheries_detail, instance_object=instance_object)

def new_plot_map_main(excel_tool: ExcelToolsForActivities, fishery_id,fishery_index, sectionNameID, icon_name, clue_reward, scene_name, bgm_name, point_list):
    new_plot_map_main_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_MAP_MAIN.xlsm")
    template_tpId = 500301
    key = "tpId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fishery_id, table_data_detail=new_plot_map_main_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_tpId, table_data_detail=new_plot_map_main_detail)
    instance_object: NEW_PLOT_MAP_MAIN
    instance_object = json_to_instance(json_object=json_object_list[0], cls=NEW_PLOT_MAP_MAIN)
    instance_object.tpId = fishery_id
    instance_object.id = instance_object.tpId
    instance_object.sectionNameID = sectionNameID
    instance_object.fisheryNameID = fishery_id
    instance_object.backGroundPic = f"MainStageBG_00{fishery_index}"
    instance_object.backGroundEffect = f"ep_Panel_MainStage_Home_0{fishery_index}"
    instance_object.openTimer = 102100 + fishery_index - 1
    instance_object.point = point_list
    instance_object.completeImg = f"icon_mainstage_clue_{icon_name}_{clue_reward[-1]['CollectCount']}"
    instance_object.loadingImg = f"loading_fisheries_{scene_name}_1"
    instance_object.cluePanelName = f"Panel_MS_clue_info_{icon_name}"
    instance_object.endPicture = instance_object.backGroundPic
    instance_object.firstSpot = 10001 + 100 * fishery_index
    instance_object.resultIcon = f"t_result_{icon_name}"
    instance_object.listFisheriesIcon = f"icon_fisheries_{icon_name}"
    instance_object.blurFisheriesIcon = f"bg_fisheries_blur_{icon_name}"
    instance_object.tournamentLogo = f"tournament_logo_{icon_name}"
    instance_object.orderNPC = f"NPC_00{fishery_index}"
    instance_object.AmbMain = f"Amb_{bgm_name}_Day_Loop"
    instance_object.BgmMain = f"Bgm_{bgm_name}_Map"
    instance_object.displayLoadingPic = instance_object.loadingImg
    instance_object.foreshow[0].waitingIcon = f"icon_mainstage_clue_{icon_name}_{clue_reward[-1]['CollectCount'] + 1}"
    instance_object.foreshow[1].waitingIcon = f"icon_mainstage_clue_{icon_name}_{clue_reward[-1]['CollectCount'] + 2}"
    instance_object.challengeIcon = f"challenge_point_0{fishery_index * 2 - 1}"
    instance_object.challengeIcon2 = f"challenge_point_0{fishery_index * 2}"
    instance_object.challengeBg = f"ChallengeBG_00{fishery_index}"
    instance_object.nextFisheryUnlockDialog = None
    instance_object.questLimit = excel_tool.get_last_quest_id(fishery_id=fishery_id - 1)
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_map_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_map_main_detail, instance_object=instance_object)

def multiplayer_room_enum(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index):
    multiplayer_room_enum_detail = excel_tool.get_table_data_detail(book_name="MULTIPLAYER_ROOM_ENUM.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    fishSpotId_start = fishery_index * 100 + 10001
    template_fisheriesId = 500301
    key = "tpId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fisheriesId", value=fishery_id, table_data_detail=multiplayer_room_enum_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fisheriesId", value=template_fisheriesId, table_data_detail=multiplayer_room_enum_detail)
    cur = 0
    while cur < len(json_object_list):
        instance_object: MULTIPLAYER_ROOM_ENUM
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=MULTIPLAYER_ROOM_ENUM)
        instance_object.id = fishery_id * 100 + cur + 1
        instance_object.name = f"{fishery_name}-钓点{cur//2 + 1}"
        if cur % 2 == 0:
            instance_object.name += "白天"
        else:
            instance_object.name += "晚上"
        instance_object.tpId = instance_object.id
        instance_object.multiType = 2
        instance_object.fisheriesId = fishery_id
        instance_object.fishSpotIds = [fishSpotId_start + cur, fishSpotId_start + cur + 4, 0, 0]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=multiplayer_room_enum_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=multiplayer_room_enum_detail, instance_object=instance_object)
        cur += 1



def new_plot_clue_reward(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index, clue_reward):
    new_plot_clue_reward_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_CLUE_REWARD.xlsm")
    template_newPlotFisheries = 500302
    key = "tpid"
    tpid_start = excel_tool.get_max_value(key=key, table_object_detail=new_plot_clue_reward_detail) + 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=new_plot_clue_reward_detail) + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="newPlotFisheries", value=fishery_id, table_data_detail=new_plot_clue_reward_detail)
    if json_object_list:
        mode = 2
        tpid_start = json_object_list[0][key]
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="newPlotFisheries", value=template_newPlotFisheries, table_data_detail=new_plot_clue_reward_detail)

    cur = 0
    while cur < len(json_object_list):
        instance_object: NEW_PLOT_CLUE_REWARD
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=NEW_PLOT_CLUE_REWARD)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.tpid = tpid_start + cur
        instance_object.name = f"第{fishery_index}节词条收集奖励{cur + 1}"
        instance_object.newPlotFisheries = fishery_id
        instance_object.CollectCount = clue_reward[cur]["CollectCount"]
        instance_object.RewardType = clue_reward[cur]["RewardType"]
        instance_object.RewardId = clue_reward[cur]["RewardId"]
        instance_object.RewardCount = clue_reward[cur]["RewardCount"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpid, table_data_detail=new_plot_clue_reward_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpid, table_data_detail=new_plot_clue_reward_detail, instance_object=instance_object)
        cur += 1


def fish_state(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index,  fishery_info):
    dropMultiple2_dict = {4: 1500000, 3: 400000, 2: 75000}
    dropMultiple2_dict_gold = {4: 3000000, 3: 820000, 2: 100000}
    fish_state_detail = excel_tool.get_table_data_detail(book_name="FISH_STATE.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    key = "tpId"
    template_tpId_bone_start = 6010001
    template_tpId_bone_glod_start = template_tpId_bone_start + 5000
    template_tpId_fail_start = template_tpId_bone_start + 10000
    template_tpId_fail_glod_start = template_tpId_bone_start + 15000
    tpId_bone_start = 6010001 + (fishery_index-1) * 15
    tpId_bone_glod_start = tpId_bone_start + 5000
    tpId_fail_start = tpId_bone_start + 10000
    tpId_fail_glod_start = tpId_bone_start + 15000

    # 鱼骨
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fish_state_detail) + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId_bone_start, table_data_detail=fish_state_detail)
    if json_object_list:
        mode = 2
        template_tpId_bone_start = tpId_bone_start
    else:
        mode = 1

    cur = 0
    while cur < 15:
        fish_info = fishery_info[cur + 15]
        instance_object: FISH_STATE
        json_object, instance_object = excel_tool.get_object(key="tpId", value=template_tpId_bone_start + cur, table_data_detail=fish_state_detail, cls=FISH_STATE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur+1}-鱼骨"
        instance_object.tpId = tpId_bone_start + cur
        instance_object.stateType = 1
        instance_object.startConditionId = instance_object.tpId + 900000
        instance_object.endConditionId = instance_object.tpId + 910000
        instance_object.endTime = 30
        instance_object.fisheriesId = fishery_id
        instance_object.fishChange[0].fish = fish_info["tpId"]
        instance_object.fishChange[0].dropMultiple2 = dropMultiple2_dict[fish_info["fishClass"]]
        instance_object.iconShow = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_info["tpId"], table_data_detail=fish_detail)["displayicon"]
        instance_object.bgShow = "btn_warning_icon_bg_"
        if fish_info["fishClass"] == 2:
            instance_object.bgShow += "b"
        elif fish_info["fishClass"] == 3:
            instance_object.bgShow += "y"
        elif fish_info["fishClass"] == 4:
            instance_object.bgShow += "r"
        instance_object.warningPrefeb = 5 - fish_info["fishClass"]
        instance_object.descBgPicture = f"item_info_title_bg_0{fish_info['fishClass'] + 2}"
        instance_object.isGolden = None
        instance_object.textId = 6010001
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        cur += 1

    # 黄金鱼骨
    fish_state_detail = excel_tool.get_table_data_detail(book_name="FISH_STATE.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fish_state_detail) + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId_bone_glod_start, table_data_detail=fish_state_detail)
    if json_object_list:
        mode = 2
        template_tpId_bone_glod_start = tpId_bone_glod_start
    else:
        mode = 1
    cur = 0
    while cur < 15:
        fish_info = fishery_info[cur + 15]
        json_object, instance_object = excel_tool.get_object(key="tpId", value=template_tpId_bone_glod_start + cur, table_data_detail=fish_state_detail, cls=FISH_STATE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur + 1}-黄金鱼骨"
        instance_object.tpId = tpId_bone_glod_start + cur
        instance_object.stateType = 1
        instance_object.startConditionId = instance_object.tpId + 900000
        instance_object.endConditionId = instance_object.tpId + 905000
        instance_object.endTime = 30
        instance_object.fisheriesId = fishery_id
        instance_object.fishChange[0].fish = fish_info["tpId"]
        instance_object.fishChange[0].dropMultiple2 = dropMultiple2_dict_gold[fish_info["fishClass"]]
        instance_object.iconShow = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_info["tpId"], table_data_detail=fish_detail)["displayicon"]
        instance_object.iconShow += "_gold"
        instance_object.bgShow = "btn_warning_icon_bg_"
        if fish_info["fishClass"] == 2:
            instance_object.bgShow += "b"
        elif fish_info["fishClass"] == 3:
            instance_object.bgShow += "y"
        elif fish_info["fishClass"] == 4:
            instance_object.bgShow += "r"
        instance_object.warningPrefeb = 5 - fish_info["fishClass"]
        instance_object.descBgPicture = f"item_info_title_bg_0{fish_info['fishClass'] + 2}"
        instance_object.isGolden = 1
        instance_object.textId = 6015001
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        cur += 1

    # 失败鱼情
    fish_state_detail = excel_tool.get_table_data_detail(book_name="FISH_STATE.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fish_state_detail) + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId_fail_start, table_data_detail=fish_state_detail)
    if json_object_list:
        mode = 2
        template_tpId_fail_start = tpId_fail_start
    else:
        mode = 1

    cur = 0
    while cur < 15:
        fish_info = fishery_info[cur + 15]
        json_object, instance_object = excel_tool.get_object(key="tpId", value=template_tpId_fail_start + cur, table_data_detail=fish_state_detail, cls=FISH_STATE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur+1}-失败"
        instance_object.tpId = tpId_fail_start + cur
        instance_object.stateType = 2
        instance_object.endConditionId = instance_object.tpId + 900000
        instance_object.endTime = 10
        instance_object.fisheriesId = fishery_id
        instance_object.fishChange[0].fish = fish_info["tpId"]
        instance_object.fishChange[0].dropMultiple2 = dropMultiple2_dict[fish_info["fishClass"]]
        instance_object.iconShow = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_info["tpId"], table_data_detail=fish_detail)["displayicon"]
        instance_object.bgShow = "btn_warning_icon_bg_"
        if fish_info["fishClass"] == 2:
            instance_object.bgShow += "b"
        elif fish_info["fishClass"] == 3:
            instance_object.bgShow += "y"
        elif fish_info["fishClass"] == 4:
            instance_object.bgShow += "r"
        instance_object.warningPrefeb = 5 - fish_info["fishClass"]
        instance_object.descBgPicture = f"item_info_title_bg_0{fish_info['fishClass'] + 2}"
        instance_object.textId = 6020001
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        cur += 1

    # 黄金失败鱼情
    fish_state_detail = excel_tool.get_table_data_detail(book_name="FISH_STATE.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fish_state_detail) + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId_fail_glod_start, table_data_detail=fish_state_detail)
    if json_object_list:
        mode = 2
        template_tpId_fail_glod_start = tpId_fail_glod_start
    else:
        mode = 1
    cur = 0
    while cur < 15:
        fish_info = fishery_info[cur + 15]
        json_object, instance_object = excel_tool.get_object(key="tpId", value=template_tpId_fail_glod_start + cur, table_data_detail=fish_state_detail, cls=FISH_STATE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur + 1}-黄金失败"
        instance_object.tpId = tpId_fail_glod_start + cur
        instance_object.stateType = 2
        instance_object.endConditionId = instance_object.tpId + 895000
        instance_object.endTime = 10
        instance_object.fisheriesId = fishery_id
        instance_object.fishChange[0].fish = fish_info["tpId"]
        instance_object.fishChange[0].dropMultiple2 = dropMultiple2_dict_gold[fish_info["fishClass"]]
        instance_object.iconShow = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_info["tpId"], table_data_detail=fish_detail)["displayicon"]
        instance_object.iconShow += "_gold"
        instance_object.bgShow = "btn_warning_icon_bg_"
        if fish_info["fishClass"] == 2:
            instance_object.bgShow += "b"
        elif fish_info["fishClass"] == 3:
            instance_object.bgShow += "y"
        elif fish_info["fishClass"] == 4:
            instance_object.bgShow += "r"
        instance_object.warningPrefeb = 5 - fish_info["fishClass"]
        instance_object.descBgPicture = f"item_info_title_bg_0{fish_info['fishClass'] + 2}"
        instance_object.isGolden = 1
        instance_object.textId = 6025001
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=fish_state_detail, instance_object=instance_object)
        cur += 1

def mission_condition(excel_tool:ExcelToolsForActivities,fishery_id, fishery_index):
    tpId_bone_start = 6010001 + (fishery_index-1) * 15
    bone_start_condition = tpId_bone_start + 900000
    bone_glod_start_condition = tpId_bone_start + 905000
    end_condition = tpId_bone_start + 910000
    key = "missionConditionID"

    # 鱼情开启条件
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_condition_detail, start=134189, long=15)
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=bone_start_condition, table_data_detail=mission_condition_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: MISSION_CONDITION
        if mode == 1:
            instance_object = MISSION_CONDITION()
            instance_object.id = id_start + cur
            instance_object.missionConditionID = bone_start_condition + cur
        else:
            json_object, instance_object = excel_tool.get_object(key=key, value=bone_start_condition + cur, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur + 1}-鱼情开启条件"
        instance_object.enabled = 1
        instance_object.triggerTypeId = 9800145
        instance_object.triggerDataMode = 2
        instance_object.triggerKeyM = fishery_id
        instance_object.triggerKeyS = 380000 + (fishery_index - 1) * 15 + cur + 1
        instance_object.triggerValue = 1
        instance_object.numDisplay = ["0", "0", "0"]
        instance_object.numDisplay_Title = ["0", "0", "0"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        cur += 1

    # 黄金鱼情开启条件
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_condition_detail, start=134189, long=15)
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=bone_glod_start_condition, table_data_detail=mission_condition_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: MISSION_CONDITION
        if mode == 1:
            instance_object = MISSION_CONDITION()
            instance_object.id = id_start + cur
            instance_object.missionConditionID = bone_glod_start_condition + cur
        else:
            json_object, instance_object = excel_tool.get_object(key=key, value=bone_glod_start_condition + cur, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur + 1}-黄金鱼情开启条件"
        instance_object.enabled = 1
        instance_object.triggerTypeId = 9800145
        instance_object.triggerDataMode = 2
        instance_object.triggerKeyM = fishery_id
        instance_object.triggerKeyS = 385000 + (fishery_index - 1) * 15 + cur + 1
        instance_object.triggerValue = 1
        instance_object.numDisplay = ["0", "0", "0"]
        instance_object.numDisplay_Title = ["0", "0", "0"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID,
                                     table_data_detail=mission_condition_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID,
                                  table_data_detail=mission_condition_detail, instance_object=instance_object)
        cur += 1

    # 鱼情结束条件
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_condition_detail, start=134189, long=15)
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=end_condition, table_data_detail=mission_condition_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < 15:
        instance_object: MISSION_CONDITION
        if mode == 1:
            instance_object = MISSION_CONDITION()
            instance_object.id = id_start + cur
            instance_object.missionConditionID = end_condition + cur
        else:
            json_object, instance_object = excel_tool.get_object(key=key, value=end_condition + cur, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
        instance_object.name = f"新主线渔场{fishery_index}-称号鱼{cur + 1}-鱼情结束条件"
        instance_object.enabled = 1
        instance_object.triggerTypeId = 9800061
        instance_object.triggerDataMode = 2
        instance_object.triggerKeyM = fishery_id
        instance_object.triggerKeyS = 360000 + fishery_index * 100 + cur + 1
        instance_object.triggerValue = 1
        instance_object.numDisplay = ["0", "0", "0"]
        instance_object.numDisplay_Title = ["0", "0", "0"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        cur += 1


def panel_static_language(excel_tool: ExcelToolsForActivities, activityBP, activityBPId=None):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    key = "templateID"
    instance_object: PANEL_STATIC_LANGUAGE
    if activityBPId is None:
        mode = 1
        instance_object = PANEL_STATIC_LANGUAGE()
        instance_object.templateID = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=panel_static_language_detail, start=19960945)
        instance_object.id = instance_object.templateID
    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=activityBPId, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)
    instance_object.name = "BP名称"
    instance_object.t_panellanguage = activityBP
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    return instance_object.templateID

def battle_pass_main_2024(excel_tool: ExcelToolsForActivities, fishery_id, icon_name, activityBPId, battle_pass_main_2024_tpId=None):
    battle_pass_main_2024_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS_MAIN_2024.xlsm")
    key = "tpId"
    template_tpId = 1030028
    if battle_pass_main_2024_tpId is None:
        mode = 1
        battle_pass_main_2024_tpId = excel_tool.get_max_value(key=key, table_object_detail=battle_pass_main_2024_detail) + 1
    else:
        mode = 2
        template_tpId = battle_pass_main_2024_tpId
    instance_object: BATTLE_PASS_MAIN_2024
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=battle_pass_main_2024_detail, cls=BATTLE_PASS_MAIN_2024)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=battle_pass_main_2024_detail) + 1
        instance_object.groupId = excel_tool.get_max_value(key="groupId", table_object_detail=battle_pass_main_2024_detail) + 1
    instance_object.tpId = battle_pass_main_2024_tpId
    instance_object.name = "新主线-" + excel_tool.get_fishery_name(fishery_id=fishery_id) + "BP"
    for itemReward in instance_object.itemReward:
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=itemReward.tpId, fishery_id=fishery_id)
        if not fish_bag:
            continue
        itemReward.tpId =fish_bag
    instance_object.activityBPName = f"Assets/InBundle/UI/Texture/activity_ndays/Bp_MS_banner_{icon_name}.png"
    instance_object.activityBPId = activityBPId
    instance_object.tabBPName = f"Assets/InBundle/UI/Texture/icon_fisheries/icon_fisheries_{icon_name}.png"
    instance_object.cardBPName = f"Assets/InBundle/UI/Texture/fish_bag/FishCard_fisheries_{icon_name}.png"
    instance_object.bgBPName = f"Assets/InBundle/UI/Texture/icon_fisheries/bg_fisheries_blur_{icon_name}.png"
    instance_object.fisheriesId = fishery_id
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)
    return instance_object.groupId, battle_pass_main_2024_tpId


def battle_pass(excel_tool: ExcelToolsForActivities, fishery_id, battle_pass_groupId):
    battle_pass_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS.xlsm")
    key = "tpId"
    template_battle_pass_groupId = 28
    id_start = excel_tool.get_max_value(key="id", table_object_detail=battle_pass_detail) + 1
    tpId_start = excel_tool.get_min_value_more_than_start(key="tpId", table_object_detail=battle_pass_detail, start=100710, long=60)
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=battle_pass_groupId, table_data_detail=battle_pass_detail)
    if json_object_list:
        mode = 2
        tpId_start = json_object_list[0]["tpId"]
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_battle_pass_groupId, table_data_detail=battle_pass_detail)
    cur = 0
    while cur < len(json_object_list):
        instance_object: BATTLE_PASS
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=BATTLE_PASS)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}BP等级{cur+1}奖励"
        instance_object.tpId = tpId_start + cur
        instance_object.groupId = battle_pass_groupId
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.freeRewards[0].tpId, fishery_id=fishery_id)
        if fish_bag:
            instance_object.freeRewards[0].tpId = fish_bag
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.payRewards[0].tpId, fishery_id=fishery_id)
        if fish_bag:
            instance_object.payRewards[0].tpId = fish_bag
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_detail, instance_object=instance_object)
        cur += 1

def new_plot_map_point(excel_tool: ExcelToolsForActivities, fishery_id,fishery_index, fishery_cfg_list, map_point_position_list):
    cfg_dict = {
        "钓点1": {"type": 2, "showIcon": "diaodian", "spotConditionType": 2, "spotConditionArg": 1, "needChapterLv": fishery_cfg_list[0]["needChapterLv"], "needPlotQuestId": fishery_cfg_list[0]["needPlotQuestId"], "needDay": fishery_cfg_list[0]["needDay"], "minDeep": 10, "maxDeep": 30, "defaultDeep": 10, "defaultSpotId": 10001 + fishery_index * 100, "pointname": 1},
        "钓点2": {"type": 2, "showIcon": "diaodian", "spotConditionType": 2, "spotConditionArg": 2, "needChapterLv": fishery_cfg_list[2]["needChapterLv"], "needPlotQuestId": fishery_cfg_list[2]["needPlotQuestId"], "needDay": fishery_cfg_list[2]["needDay"], "minDeep": 15, "maxDeep": 35, "defaultDeep": 15, "defaultSpotId": 10003 + fishery_index * 100, "pointname": 2},
        "村庄1": {"type": 1, "showIcon": "cunzhuang"},
        "村庄2": {"type": 1, "showIcon": "cunzhuang"},
        "村庄3": {"type": 1, "showIcon": "cunzhuang"},
        "订单": {"type": 3, "showIcon": "dingdan"},
        "锦标赛": {"type": 5, "showIcon": "dingdan"}
    }
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    point_list = []
    new_plot_map_point_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_MAP_POINT.xlsm")
    key = "tpId"
    id_start = excel_tool.get_min_value_more_than_start(key_list=["id", key], table_object_detail=new_plot_map_point_detail, start=10000, long=len(map_point_position_list))
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fisheriesId", value=fishery_id, table_data_detail=new_plot_map_point_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    cur = 0
    while cur < len(map_point_position_list):
        cfg = cfg_dict[map_point_position_list[cur]["name"]]
        instance_object: NEW_PLOT_MAP_POINT
        if mode == 1:
            instance_object = NEW_PLOT_MAP_POINT()
            instance_object.id = id_start + cur
            instance_object.tpId = instance_object.id
        else:
            instance_object = json_to_instance(json_object=json_object_list[cur], cls=NEW_PLOT_MAP_POINT)
        if cur < 5:
            point_list.append(instance_object.tpId)
        instance_object.name = fishery_name + "-" + map_point_position_list[cur]["name"]
        instance_object.enabled = 1
        instance_object.fisheriesId = fishery_id
        instance_object.showIcon = cfg["showIcon"]
        instance_object.type = cfg["type"]
        instance_object.xPosition = map_point_position_list[cur]["xPosition"]
        instance_object.yPosition = map_point_position_list[cur]["yPosition"]
        if "spotConditionType" in cfg:
            instance_object.spotConditionType = cfg["spotConditionType"]
        if "spotConditionArg" in cfg:
            instance_object.spotConditionArg = cfg["spotConditionArg"]
        if "needChapterLv" in cfg:
            instance_object.needChapterLv = cfg["needChapterLv"]
        if "needPlotQuestId" in cfg:
            instance_object.needPlotQuestId = cfg["needPlotQuestId"]
        if "needDay" in cfg:
            instance_object.needDay = cfg["needDay"]
        if "minDeep" in cfg:
            instance_object.minDeep = cfg["minDeep"]
        if "maxDeep" in cfg:
            instance_object.maxDeep = cfg["maxDeep"]
        if "defaultDeep" in cfg:
            instance_object.defaultDeep = cfg["defaultDeep"]
        if "defaultSpotId" in cfg:
            instance_object.defaultSpotId = cfg["defaultSpotId"]
        if "pointname" in cfg:
            instance_object.pointname = cfg["pointname"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_map_point_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_map_point_detail, instance_object=instance_object)
        cur += 1
    return point_list

def new_plot_map_point_language(excel_tool: ExcelToolsForActivities,fishery_id, point_list, map_point_position_list, spot_language_list):
    new_plot_map_point_language_detail = excel_tool.get_table_data_detail(book_name="NEW_PLOT_MAP_POINT_LANGUAGE.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    key = "tpId"
    cur = 0
    while cur < len(point_list):
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=point_list[cur], table_data_detail=new_plot_map_point_language_detail)
        if json_object_list:
            mode = 2
            instance_object = json_to_instance(json_object=json_object_list[0], cls=NEW_PLOT_MAP_POINT_LANGUAGE)
        else:
            mode = 1
            instance_object = NEW_PLOT_MAP_POINT_LANGUAGE()
        instance_object.id = point_list[cur]
        instance_object.tpId = instance_object.id
        instance_object.name = fishery_name + "-" + map_point_position_list[cur]["name"]
        if instance_object.t_name is None:
            instance_object.t_name = fishery_name + "-" + map_point_position_list[cur]["name"]
        if cur < 2 and instance_object.t_desc is None:
            instance_object.t_desc = fishery_name + "-" + map_point_position_list[cur]["name"] + "描述"
            instance_object.name = spot_language_list[cur]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_map_point_language_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=new_plot_map_point_language_detail, instance_object=instance_object)
        cur += 1

def main(excel_tool: ExcelToolsForActivities, mode = 1):
    """
        读写方式：新增/修改
        需要先生成鱼卡包的配置
        mode=1 新增   mode=2 修改
    """

    file_name = os.path.basename(__file__).split('.')[0]

    # 配置修改区起始
    cfg = get_cfg_fishery()
    print("cfg:", cfg)
    cfg_ndays = get_cfg_ndays()
    fishery_id = cfg["fishery_id"]
    ChapterId = cfg["ChapterId"]  # 赛季id
    bgm_name = cfg["bgm_name"]  # new_plot_map_main和new_plot_fish_spot中区分渔场的字段
    fishery_name = cfg["fishery_name"]  # new_plot_fish_spot的battleScene字段用到
    icon_name = cfg["icon_name"]  # 区分渔场图标的后缀
    scene_name_list = cfg["scene_name_list"]  # 场景名
    living = cfg["living"]  # 1是淡水 2是咸水
    activityBP = cfg["activityBP"]
    # 钓点解锁条件
    fishery_cfg_list = cfg["fishery_cfg_list"]
    # 线索奖励需要的数量和奖励
    clue_reward = cfg["clue_reward"]
    spot_language_list = cfg_ndays["mission_cfg"]["spot_language_list"]
    map_point_position_list = [
        {"name": "钓点1", "xPosition": -338, "yPosition": 59},
        {"name": "钓点2", "xPosition": 479, "yPosition": 371},
        {"name": "村庄1", "xPosition": -507, "yPosition": 252},
        {"name": "村庄2", "xPosition": 118, "yPosition": 556},
        {"name": "村庄3", "xPosition": 487, "yPosition": 111},
        {"name": "订单", "xPosition": -73, "yPosition": 369},
        {"name": "锦标赛", "xPosition": 22, "yPosition": 412},
    ]
    # map_point_position_list = cfg["map_point_position_list"]


    cfg_ndays = get_cfg_ndays()
    # 该区域参数为None则新增
    if mode == 1:
        activityBPId = None       # bp标题对应的panel_static_language中templateID
        battle_pass_main_2024_tpId = None  # battle_pass_main_2024中tpId
    else:
        id_dict = load_main_id(file_name=file_name)
        print("id_dict:", id_dict)
        activityBPId = id_dict["activityBPId"]
        battle_pass_main_2024_tpId = id_dict["battle_pass_main_2024_tpId"]

    # 根据偏移算中间值，当渔场id不按顺序新增时可能有问题
    fishery_index = fishery_id - 500300
    new_plot_fish_spot_tpId_start = 10001 + fishery_index * 100
    mapPointId_list = [10001 + 5 * (fishery_index - 1), 10002 + 5 * (fishery_index - 1)]
    sectionNameID = 1998083 + fishery_index
    # 配置修改区结束

    fishery_info = get_fishery_info(excel_tool=excel_tool, fishery_id=fishery_id)
    exclude_info = get_exclude_info(excel_tool=excel_tool, fishery_id=fishery_id)
    fish(excel_tool=excel_tool, fishery_info=fishery_info, fishery_index=fishery_index, living=living)
    fisheries(excel_tool=excel_tool, fishery_id=fishery_id, icon_name=icon_name, scene_name=scene_name_list[0], fishery_info=fishery_info)
    point_list = new_plot_map_point(excel_tool=excel_tool, fishery_id=fishery_id,  fishery_index=fishery_index, fishery_cfg_list=fishery_cfg_list, map_point_position_list=map_point_position_list)
    new_plot_map_point_language(excel_tool=excel_tool, fishery_id=fishery_id, point_list=point_list, map_point_position_list=map_point_position_list, spot_language_list=spot_language_list)
    new_plot_map_main(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index, sectionNameID=sectionNameID, icon_name=icon_name, clue_reward=clue_reward, scene_name=scene_name_list[1], bgm_name=bgm_name, point_list=point_list)
    multiplayer_room_enum(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index)
    new_plot_fish_type_drop(excel_tool=excel_tool, fishery_id=fishery_id, ChapterId=ChapterId)
    new_plot_clue_reward(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index, clue_reward=clue_reward)
    fish_golden_show(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index)
    fish_weight_new(excel_tool=excel_tool, fishery_info=fishery_info, fishery_index=fishery_index)
    fish_state(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index, fishery_info=fishery_info)
    mission_condition(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index)
    activityBPId = panel_static_language(excel_tool=excel_tool, activityBP=activityBP, activityBPId=activityBPId)
    battle_pass_groupId, battle_pass_main_2024_tpId = battle_pass_main_2024(excel_tool=excel_tool, fishery_id=fishery_id, icon_name=icon_name, activityBPId=activityBPId, battle_pass_main_2024_tpId=battle_pass_main_2024_tpId)
    battle_pass(excel_tool=excel_tool, fishery_id=fishery_id, battle_pass_groupId=battle_pass_groupId)
    new_plot_fish_spot(excel_tool=excel_tool, fishery_id=fishery_id, tpId_start=new_plot_fish_spot_tpId_start, fishery_cfg_list=fishery_cfg_list, fishery_info=fishery_info, exclude_info=exclude_info, bgm_name=bgm_name, fishery_name=fishery_name, scene_name_list=scene_name_list, mapPointId_list=mapPointId_list, cfg_ndays=cfg_ndays)

    save_main_id(file_name=file_name, id_dict={"activityBPId": activityBPId, "battle_pass_main_2024_tpId": battle_pass_main_2024_tpId})
    print("涉及到的表：", list(excel_tool.data_txt_changed))


if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool, mode=1)
