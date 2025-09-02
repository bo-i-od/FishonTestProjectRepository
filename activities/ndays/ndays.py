import os
from activities.decl.BATTLE_PASS import BATTLE_PASS
from activities.decl.BATTLE_PASS_MAIN_2024 import BATTLE_PASS_MAIN_2024, BATTLE_PASS_SPECIAL_ITEM_REWARD
from activities.decl.EVENT_N_DAY_TASKS_LEADERBOARD import EVENT_N_DAY_TASKS_LEADERBOARD
from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.ITEM_MAIN import ITEM_MAIN, complimentary_item_main
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_MAIN import MISSION_MAIN
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.decl.REPEATABLE_CHALLENGE import REPEATABLE_CHALLENGE
from activities.decl.REPEATABLE_CHALLENGE_LANGUAGE import REPEATABLE_CHALLENGE_LANGUAGE
from activities.decl.TIMER_MAIN import TIMER_MAIN, TimeStruct
from tools import commonTools, baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    这个是没有开过双周活动的单周配置模板
"""


def battle_pass_main_2024(excel_tool: ExcelToolsForActivities, fishery_id, TimerId, newNDaysImgName, activityNameId, groupId_battle_pass):
    battle_pass_main_2024_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS_MAIN_2024.xlsm")
    template_groupId = 42
    instance_object: BATTLE_PASS_MAIN_2024
    key = "tpId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_battle_pass, table_data_detail=battle_pass_main_2024_detail)
    if json_object_list:
        mode = 2
        instance_object = json_to_instance(json_object=json_object_list[0], cls=BATTLE_PASS_MAIN_2024)
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=battle_pass_main_2024_detail)
        instance_object = json_to_instance(json_object=json_object_list[0], cls=BATTLE_PASS_MAIN_2024)
        instance_object.tpId = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=battle_pass_main_2024_detail, start=1030042)


    instance_object.id = instance_object.tpId
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}ndaysBP"
    instance_object.groupId = groupId_battle_pass
    instance_object.enabled = 1
    instance_object.mainId = 102
    instance_object.resId = 102000
    instance_object.firstOpenTimerId = TimerId
    instance_object.payLevelId = 1101
    instance_object.advancePayLevelId = 1201
    instance_object.payCoupon = 120
    instance_object.payCouponPost = 480
    instance_object.bounsRate = 3000
    instance_object.advanceCoupon = 300
    instance_object.advanceCouponPost = 680
    instance_object.bounsRateAdvance = 3000
    instance_object.promoteCoupon = 180
    instance_object.bounsRatePromote = 3000
    instance_object.itemReward = [BATTLE_PASS_SPECIAL_ITEM_REWARD(), BATTLE_PASS_SPECIAL_ITEM_REWARD()]
    instance_object.itemReward[0].RewardLogicType = 1
    instance_object.itemReward[0].ioIdType = 1
    instance_object.itemReward[0].tpId = 100500
    instance_object.itemReward[0].count = 300
    instance_object.itemReward[1].RewardLogicType = 2
    instance_object.itemReward[1].tpId = 10005
    instance_object.itemReward[1].count = 2
    instance_object.activityBPName = f"Assets/InBundle/UI/Texture/activity_ndays/{newNDaysImgName}.png"
    instance_object.activityBPId = activityNameId
    instance_object.fisheriesId = fishery_id

    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)

def battle_pass(excel_tool: ExcelToolsForActivities, fishery_id, groupId_battle_pass):
    battle_pass_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    template_groupId = 42
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_battle_pass, table_data_detail=battle_pass_detail)
    key = "tpId"
    if table_data_object_list:
        mode = 2
        tpId_start = table_data_object_list[0]["tpId"]
    else:
        mode = 1
        table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=battle_pass_detail)
        tpId_start = excel_tool.get_min_value_more_than_start(key=key, start=200280, table_object_detail=battle_pass_detail, long=len(table_data_object_list))
    cur = 0
    while cur < len(table_data_object_list):
        json_object = table_data_object_list[cur]
        instance_object: BATTLE_PASS
        instance_object = json_to_instance(json_object=json_object, cls=BATTLE_PASS)
        instance_object.name = f"{fishery_name}BP等级{cur + 1}奖励"
        instance_object.tpId = tpId_start + cur
        instance_object.id = instance_object.tpId
        instance_object.enabled = 1
        instance_object.mainId = 102
        instance_object.groupId = groupId_battle_pass
        instance_object.level = cur + 1

        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_detail, instance_object=instance_object)

        cur += 1

def event_n_day_tasks_leaderboard(excel_tool: ExcelToolsForActivities, fishery_id, groupId):
    event_n_day_tasks_leaderboard_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_LEADERBOARD.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    template_groupId = 5100104
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=event_n_day_tasks_leaderboard_detail)
    key = "autoId"
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=event_n_day_tasks_leaderboard_detail)
    autoId_start = excel_tool.get_min_value_more_than_start(key=key, start=490, long=len(json_object_list), table_object_detail=event_n_day_tasks_leaderboard_detail)
    cur = 0
    while cur < len(json_object_list):
        instance_object: EVENT_N_DAY_TASKS_LEADERBOARD
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=EVENT_N_DAY_TASKS_LEADERBOARD)
        if mode == 1:
            instance_object.autoId = autoId_start + cur
            instance_object.name = instance_object.name.replace("伏尔加河", fishery_name)
        instance_object.id = instance_object.autoId
        instance_object.groupId = groupId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_leaderboard_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_leaderboard_detail, instance_object=instance_object)
        cur += 1

def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID):
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    template_groupId = 5100104
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=event_n_day_tasks_milestone_detail)
    key = "autoId"
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=event_n_day_tasks_milestone_detail)
    autoId_start = excel_tool.get_min_value_more_than_start(key=key, start=3202, long=len(json_object_list),table_object_detail=event_n_day_tasks_milestone_detail)
    cur = 0
    while cur < len(json_object_list):
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=EVENT_N_DAY_TASKS_MILESTONE)
        if mode == 1:
            instance_object.autoId = autoId_start + cur
            instance_object.name = instance_object.name.replace("伏尔加河", fishery_name)
        instance_object.id = instance_object.autoId
        instance_object.tokenID = tokenID
        instance_object.groupId = groupId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        cur += 1


def item_main(excel_tool: ExcelToolsForActivities, activityName, tokenID):
    # 活动代币
    template_itemTpId = 261103
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    if tokenID is None:
        mode = 1
        tokenID = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=item_main_detail, start=template_itemTpId)
    else:
        mode = 2
        template_itemTpId = tokenID

    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    instance_object.name = f"{activityName}ndays活动代币"
    instance_object.itemTpId = tokenID
    instance_object.id = tokenID
    instance_object.quality = 4
    instance_object.maxAmount = 999999999
    instance_object.priceDiamond = 1
    instance_object.priceDivisor = 1
    instance_object.description = instance_object.name
    instance_object.iconName = "coin_rookieTasks_ndays"
    instance_object.values = ["0", "0", "0", "0"]
    instance_object.useArgs = ["0", "0"]
    instance_object.awards = complimentary_item_main()
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)

    return tokenID

def item_main_language(excel_tool: ExcelToolsForActivities, tokenID, activityName):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"
    # 活动代币
    template_tpId = 261103
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 2
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    instance_object.name = f"{activityName}ndays活动代币"
    instance_object.tpId = tokenID
    instance_object.id = instance_object.tpId
    instance_object.t_name = "活动积分"
    instance_object.t_description = f"收集活动积分，赢取额外奖励。"

    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)

def mission_group(excel_tool: ExcelToolsForActivities, TimerId, fishery_id,activityName, activityNameId, imgNameInner,  newNDaysImgName, groupId):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    key = "groupId"

    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId, table_data_detail=mission_group_detail)
    # ndays
    template_groupId = 5100104
    if json_object_list:
        mode = 2
        template_groupId = groupId
    else:
        mode = 1


    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}ndays-{activityName}"
    instance_object.groupId = groupId
    instance_object.id = instance_object.groupId
    instance_object.enabled = 1
    instance_object.fisheriesId = fishery_id
    instance_object.key = "N_DAYS"
    instance_object.subType = 8
    instance_object.keyDesc = "n天活动"
    instance_object.openType = 2
    instance_object.openArg = TimerId
    instance_object.closeType = 2
    instance_object.closeArg = instance_object.openArg
    instance_object.extArgs[0] = "1000"
    instance_object.extArgs[1] = "30"
    instance_object.extArgs[3] = "1"
    instance_object.extArgs[5] = f"{fishery_id}"
    instance_object.extArgs[6] = instance_object.extArgs[5]
    instance_object.extArgs[7] = "0"
    instance_object.extArgs[8] = "0"
    instance_object.extArgs[9] = "0"
    instance_object.serverCharaLevel = 21
    instance_object.imgName = "ActivityCenter_banner_bg_30"
    instance_object.activityName = activityNameId
    instance_object.imgNameInner = imgNameInner
    instance_object.iconName = "prepare_activity_RookieTasks_2"
    instance_object.tabOrder = 1
    instance_object.tabImage = "EventsHall_tab_events_31"
    instance_object.rankHouseRulesId = 1001
    instance_object.missionType = 86
    instance_object.newNDaysImgName = newNDaysImgName

    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)


def mission_main(excel_tool: ExcelToolsForActivities,fishery_id, groupId, tokenID):
    missionID_template_start = 6030189
    missionConditionID_template_start = 6013213
    mission_cfg_list = [
        {"template_missionID": {missionID_template_start: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start:["fishery_id", "fisheries_language"], } },
        {"template_missionID": {missionID_template_start + 1: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 1: ["fishery_id", "fisheries_language"],} },
        {"template_missionID": {missionID_template_start + 2: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 2: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 3: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 3: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 4: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 4: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 5: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 5: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 6: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 6: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 7: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 7: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 8: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 8: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 9: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 9: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 10: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 10: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 11: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 11: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 12: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 12: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 13: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 13: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 14: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 14: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 15: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 15: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 43:["fishery_id"] }},
        {"template_missionID": {missionID_template_start + 16: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 16: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 44:["fishery_id"] }},
        {"template_missionID": {missionID_template_start + 17: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 17: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 45:["fishery_id"] }},
        {"template_missionID": {missionID_template_start + 18: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 18: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 46:["fishery_id"] }},
        {"template_missionID": {missionID_template_start + 19: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 19: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 47:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 20: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 20: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 48:["fishery_id"] }},
        {"template_missionID": {missionID_template_start + 21: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 21: ["fishery_id", "fisheries_language"], missionConditionID_template_start + 49:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 22: []}, "template_missionConditionIDs": {missionConditionID_template_start + 22: [], missionConditionID_template_start + 50:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 23: []}, "template_missionConditionIDs": {missionConditionID_template_start + 23: [], missionConditionID_template_start + 51:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 24: []}, "template_missionConditionIDs": {missionConditionID_template_start + 24: [], missionConditionID_template_start + 52:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 25: []}, "template_missionConditionIDs": {missionConditionID_template_start + 25: [], missionConditionID_template_start + 53:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 26: []}, "template_missionConditionIDs": {missionConditionID_template_start + 26: [], missionConditionID_template_start + 54:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 27: []}, "template_missionConditionIDs": {missionConditionID_template_start + 27: [], missionConditionID_template_start + 55:["fishery_id"]}},
        {"template_missionID": {missionID_template_start + 28: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 28: []}, },
        {"template_missionID": {missionID_template_start + 29: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 29: []}, },
        {"template_missionID": {missionID_template_start + 30: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 30: []}, },
        {"template_missionID": {missionID_template_start + 31: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 31: []}, },
        {"template_missionID": {missionID_template_start + 32: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 32: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 33: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 33: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 34: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 34: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 35: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 35: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 36: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 36: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 37: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 37: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 38: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 38: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 39: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 39: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 40: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 40: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 41: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 41: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": {missionID_template_start + 42: ["fishery_id"]}, "template_missionConditionIDs": {missionConditionID_template_start + 42: ["fishery_id", "fisheries_language"]} },
    ]

    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    missionConditionID_start = excel_tool.get_min_value_more_than_start(key="missionConditionID", start=missionConditionID_template_start, long=56, table_object_detail=mission_condition_detail)

    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=mission_main_detail)
    if table_data_object_list:
        mode = 2
    else:
        mode = 1
    missionID_start = excel_tool.get_min_value_more_than_start(key="missionID", start=missionID_template_start, long=len(mission_cfg_list),table_object_detail=mission_main_detail)
    missionConditionID_set = set()
    key = "missionID"
    cur = 0
    while cur < len(mission_cfg_list):
        mission_cfg = mission_cfg_list[cur]
        instance_object: MISSION_MAIN
        jump_list = list(mission_cfg["template_missionID"])
        if mode == 1:
            json_object, instance_object = excel_tool.get_object(key=key, value=jump_list[0], table_data_detail=mission_main_detail, cls=MISSION_MAIN)
            instance_object.missionID = missionID_start + cur
            instance_object.name = instance_object.name.replace("伏尔加河", fishery_name)
            instance_object.missionName = instance_object.missionName.replace("伏尔加河", fishery_name)
            instance_object.missionDes = instance_object.missionDes.replace("伏尔加河", fishery_name)
            missionConditionID = missionConditionID_start + cur
            while missionConditionID in missionConditionID_set:
                missionConditionID += 1
            instance_object.missionConditionIDs[0] = missionConditionID
            missionConditionID_set.add(instance_object.missionConditionIDs[0])
            if len(mission_cfg["template_missionConditionIDs"]) > 1:
                instance_object.missionConditionIDs[1] = instance_object.missionConditionIDs[0] + 28
                missionConditionID_set.add(instance_object.missionConditionIDs[1])
        else:
            instance_object = json_to_instance(json_object=table_data_object_list[cur], cls=MISSION_MAIN)
            missionConditionID_set.add(instance_object.missionConditionIDs[0])
            if len(mission_cfg["template_missionConditionIDs"]) > 1:
                missionConditionID_set.add(instance_object.missionConditionIDs[1])
        # missionConditionID_set有该值就加一直到无重复
        instance_object.id = instance_object.missionID
        instance_object.enabled = 1
        instance_object.groupId = groupId
        instance_object.missionType = 86
        instance_object.awards[0].itemId = tokenID
        if "fishery_id" in mission_cfg["template_missionID"][jump_list[0]]:
            instance_object.missionRedirection = 8
            instance_object.redirectionParams[0] = fishery_id
        else:
            instance_object.missionRedirection = 30
            instance_object.redirectionParams[0] = 0

        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionID, table_data_detail=mission_main_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionID, table_data_detail=mission_main_detail, instance_object=instance_object)
        cur += 1

    # 接着整mission_condition表
    missionConditionID_list = sorted(missionConditionID_set)
    mission_condition(excel_tool=excel_tool, fishery_id=fishery_id, mission_cfg_list=mission_cfg_list,  missionConditionID_list=missionConditionID_list)

def mission_condition(excel_tool: ExcelToolsForActivities,fishery_id, mission_cfg_list, missionConditionID_list):
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    mission_condition_cfg_dict = {}
    cur = 0
    while cur < len(mission_cfg_list):
        template_missionConditionIDs = mission_cfg_list[cur]["template_missionConditionIDs"]
        mission_condition_cfg_dict.update(template_missionConditionIDs)
        cur += 1
    template_missionConditionID_list = sorted(mission_condition_cfg_dict)
    template_missionConditionID_list_copy = template_missionConditionID_list
    id_start = excel_tool.get_max_value(key="id", table_object_detail=mission_condition_detail) + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="missionConditionID", value=missionConditionID_list[0], table_data_detail=mission_condition_detail)
    if table_data_object_list:
        mode = 2
        template_missionConditionID_list = missionConditionID_list
    else:
        mode = 1

    key = "missionConditionID"
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    cur = 0
    while cur < len(template_missionConditionID_list):
        missionConditionID = missionConditionID_list[cur]
        template_missionConditionID = template_missionConditionID_list[cur]
        mission_condition_cfg = mission_condition_cfg_dict[template_missionConditionID_list_copy[cur]]
        instance_object: MISSION_CONDITION
        json_object, instance_object = excel_tool.get_object(key=key, value=template_missionConditionID, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
        if mode == 1:
            instance_object.name = instance_object.name.replace("伏尔加河", fishery_name)
        instance_object.missionConditionID = missionConditionID
        instance_object.id = instance_object.missionConditionID
        if "fishery_id" in mission_condition_cfg:
            instance_object.triggerKeyM = fishery_id
        if "fisheries_language" in mission_condition_cfg:
            instance_object.numDisplay[0] = f"fisheries_language|t_name|{fishery_id}"

        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        cur += 1

def panel_static_language(excel_tool: ExcelToolsForActivities, t_panellanguage, activityNameId):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    key = "templateID"
    if activityNameId is None:
        mode = 1
        instance_object = PANEL_STATIC_LANGUAGE()
        instance_object.templateID = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=panel_static_language_detail, start=2030040)

    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=activityNameId, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)
    activityNameId = instance_object.templateID
    # 标题语言
    instance_object.id = instance_object.templateID
    instance_object.name = t_panellanguage
    instance_object.t_panellanguage = t_panellanguage
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    return activityNameId


def repeatable_challenge(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID):
    fish_class_list = ["大型鱼","特大型鱼", "超巨型鱼", "奇珍鱼", "超奇珍鱼", "典藏鱼"]
    repeatable_challenge_detail = excel_tool.get_table_data_detail(book_name="REPEATABLE_CHALLENGE.xlsm")
    repeatable_challenge_language_detail = excel_tool.get_table_data_detail(book_name="REPEATABLE_CHALLENGE_LANGUAGE.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    id_start = excel_tool.get_min_value_more_than_start(key="id",start=132822, long=6, table_object_detail=repeatable_challenge_detail)
    id_start_language = excel_tool.get_min_value_more_than_start(key="id",start=132822, long=6, table_object_detail=repeatable_challenge_language_detail)
    key = "autoId"
    autoId_start = excel_tool.get_min_value_more_than_start(key=key,start=498, long=6, table_object_detail=repeatable_challenge_detail)
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=repeatable_challenge_detail)
    template_groupId = 5100104
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=repeatable_challenge_detail)

    cur = 0
    while cur < 6:
        instance_object: REPEATABLE_CHALLENGE
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=REPEATABLE_CHALLENGE)
        if mode == 1:

            instance_object.autoId = autoId_start + cur
        instance_object.id = instance_object.autoId
        instance_object.name = f"{fishery_name}-ndays挑战-{fish_class_list[cur]}"
        instance_object.groupId = groupId
        instance_object.triggerKeyM = fishery_id
        instance_object.rewards[0].itemId = tokenID
        instance_object.redirectionParams = [fishery_id]

        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value= instance_object.autoId, table_data_detail=repeatable_challenge_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value= instance_object.autoId, table_data_detail=repeatable_challenge_detail, instance_object=instance_object)

        # 多语言
        instance_object_language: REPEATABLE_CHALLENGE_LANGUAGE
        json_object, instance_object_language = excel_tool.get_object(key="autoId", value=instance_object.autoId, table_data_detail=repeatable_challenge_language_detail, cls=REPEATABLE_CHALLENGE_LANGUAGE)
        if instance_object_language:
            mode_language = 2
        else:
            instance_object_language = REPEATABLE_CHALLENGE_LANGUAGE()
            instance_object_language.id = id_start_language + cur
            mode_language = 1
            instance_object_language.autoId = instance_object.autoId

        # fish_name = excel_tool.get_fish_name(fish_id=instance_object.triggerKeyS)
        instance_object_language.name = instance_object.name
        instance_object_language.t_missiontype = f"{fishery_name}的怪物"
        instance_object_language.t_missionname = fishery_name
        instance_object_language.t_missiondes = f"{fishery_name}最受青睐的{fish_class_list[cur]}"

        print(instance_object_language)
        if mode_language == 2:
            excel_tool.change_object(key=key, value= instance_object_language.autoId, table_data_detail=repeatable_challenge_language_detail, instance_object=instance_object_language)
        else:
            excel_tool.add_object(key=key, value= instance_object_language.autoId, table_data_detail=repeatable_challenge_language_detail, instance_object=instance_object_language)
        cur += 1

def timer_main(excel_tool: ExcelToolsForActivities, fishery_id, open_time,activityName, TimerId=None):
    key = "timerID"
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    if TimerId is None:
        mode = 1
        instance_object = TIMER_MAIN()
        TimerId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=timer_main_detail, start=150293)
    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=TimerId, table_data_detail=timer_main_detail, cls=TIMER_MAIN)

    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}ndays-{activityName}"
    instance_object.timerID = TimerId
    instance_object.id = instance_object.timerID
    instance_object.timerName = instance_object.name
    instance_object.cycleType = 1
    instance_object.openTime = open_time
    instance_object.endTime = commonTools.get_time(time=open_time, days=7, seconds=-1)
    instance_object.durationTime = TimeStruct()
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    return TimerId

def get_activityNameId(excel_tool: ExcelToolsForActivities, activityName):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="t_panellanguage", value=activityName, table_data_detail=panel_static_language_detail)
    if json_object_list:
        return json_object_list[0]["templateID"]
    return None

def get_tokenID(excel_tool: ExcelToolsForActivities, activityName):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="name", value=f"{activityName}ndays活动代币", table_data_detail=item_main_detail)
    if json_object_list:
        return json_object_list[0]["itemTpId"]
    return None



def main(excel_tool: ExcelToolsForActivities, mode, groupId, groupId_battle_pass, fishery_id, open_time, activityName, imgNameInner, newNDaysImgName):
    """
        读写方式：新增/修改
        mode=1 新增   mode=2 修改
    """

    # 该区域参数为None则新增
    if mode == 1:
        TimerId= None            # 返场时间id (activity_double_week, battle_pass_main_2024, mission_group, timer_main)
        activityNameId= None  # panel_static_language里的templateID 返场活动名templateID
        tokenID= None                   # ndays积分币(event_n_day_tasks_milestone, item_main, item_main_language, mission_main, repeatable_challenge)
    else:
        TimerId = excel_tool.group_id_to_timer_id(group_id=groupId)
        activityNameId = get_activityNameId(excel_tool=excel_tool, activityName=activityName)
        tokenID = get_tokenID(excel_tool=excel_tool, activityName=activityName)

    # 配置修改区结束
    TimerId = timer_main(excel_tool=excel_tool, open_time=open_time, fishery_id=fishery_id, activityName=activityName, TimerId=TimerId)
    activityNameId = panel_static_language(excel_tool=excel_tool, t_panellanguage=activityName, activityNameId=activityNameId)
    mission_group(excel_tool=excel_tool, TimerId=TimerId, fishery_id=fishery_id, activityName=activityName, activityNameId=activityNameId, imgNameInner=imgNameInner, newNDaysImgName=newNDaysImgName, groupId=groupId)
    tokenID = item_main(excel_tool=excel_tool, activityName=activityName, tokenID=tokenID)
    item_main_language(excel_tool=excel_tool, tokenID=tokenID, activityName=activityName)
    battle_pass_main_2024(excel_tool=excel_tool, fishery_id=fishery_id, groupId_battle_pass=groupId_battle_pass, TimerId=TimerId, newNDaysImgName=newNDaysImgName, activityNameId=activityNameId)
    battle_pass(excel_tool=excel_tool, fishery_id=fishery_id, groupId_battle_pass=groupId_battle_pass)
    event_n_day_tasks_leaderboard(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId)
    event_n_day_tasks_milestone(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)
    repeatable_challenge(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)
    mission_main(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)

    print("涉及到的表：", list(excel_tool.data_txt_changed))


