from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.ITEM_MAIN import ITEM_MAIN, complimentary_item_main
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_MAIN import MISSION_MAIN
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.decl.TIMER_MAIN import TimeStruct, TIMER_MAIN
from configs.pathConfig import EXCEL_PATH
from tools import commonTools
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities


def panel_static_language(excel_tool: ExcelToolsForActivities,fishery_id, t_panellanguage, activityNameId):
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
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}鱼场的3天乐活动"
    instance_object.t_panellanguage = t_panellanguage
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    return activityNameId

def item_main(excel_tool: ExcelToolsForActivities,fishery_id, tokenID):
    # 活动代币
    template_itemTpId = 290076
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    if tokenID is None:
        mode = 1
        tokenID = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=item_main_detail, start=template_itemTpId)
    else:
        mode = 2
        template_itemTpId = tokenID

    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    instance_object.name = f"{fishery_id}{excel_tool.get_fishery_name(fishery_id=fishery_id)}渔场3天乐_代币"
    instance_object.itemTpId = tokenID
    instance_object.id = tokenID
    instance_object.quality = 4
    instance_object.maxAmount = 999999999
    instance_object.priceDiamond = 1
    instance_object.priceDivisor = 1
    instance_object.description = instance_object.name
    instance_object.iconName = "coin_rookieTasks"
    instance_object.values = ["0", "0", "0", "0"]
    instance_object.useArgs = ["0", "0"]
    instance_object.awards = complimentary_item_main()
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)

    return tokenID

def item_main_language(excel_tool: ExcelToolsForActivities,fishery_id, tokenID):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"
    # 活动代币
    template_tpId = 290076
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 2
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    instance_object.name = f"{fishery_id}{excel_tool.get_fishery_name(fishery_id=fishery_id)}渔场3天乐_代币"
    instance_object.tpId = tokenID
    instance_object.id = instance_object.tpId
    instance_object.t_name = "活动积分"
    instance_object.t_description = f"收集活动积分，赢取额外奖励。"

    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)

def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID):
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    template_groupId = 5400321
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=event_n_day_tasks_milestone_detail)
    key = "autoId"
    if json_object_list:
        mode = 2
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=event_n_day_tasks_milestone_detail)
    autoId_start = excel_tool.get_min_value_more_than_start(key=key, start=2205, long=len(json_object_list),table_object_detail=event_n_day_tasks_milestone_detail)
    cur = 0
    while cur < len(json_object_list):
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=EVENT_N_DAY_TASKS_MILESTONE)
        if mode == 1:
            instance_object.autoId = autoId_start + cur
            instance_object.name = instance_object.name.replace("琵琶湖", fishery_name)
            instance_object.name = instance_object.name.replace("400321", str(fishery_id))
        instance_object.id = instance_object.autoId
        instance_object.tokenID = tokenID
        instance_object.groupId = groupId
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        cur += 1

def mission_condition_open(excel_tool, fishery_id, missionConditionID):
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="missionConditionID", value=missionConditionID, table_data_detail=mission_condition_detail)
    fisher_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    key = "missionConditionID"
    instance_object: MISSION_CONDITION
    if json_object_list:
        mode = 2
        instance_object = json_to_instance(json_object=json_object_list[0], cls=MISSION_CONDITION)
    else:
        mode = 1
        missionConditionID = excel_tool.get_min_value_more_than_start(key=key, start=6012759, long=1, table_object_detail=mission_condition_detail)
        instance_object = MISSION_CONDITION()
    instance_object.name = f"{fishery_id}{fisher_name}渔场3天乐触发"
    instance_object.missionConditionID = missionConditionID
    instance_object.id = instance_object.missionConditionID
    instance_object.enabled = 1
    instance_object.triggerTypeId = 9800181
    instance_object.triggerDataMode = 1
    instance_object.triggerKeyM = fishery_id
    instance_object.triggerValue = 1
    instance_object.numDisplay = ["0", "0", "0"]
    instance_object.numDisplay_Title = ["0", "0", "0"]
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
    return instance_object.missionConditionID

def mission_group(excel_tool: ExcelToolsForActivities, missionConditionID, fishery_id, activityNameId,imgNameInner, groupId):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    key = "groupId"

    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId, table_data_detail=mission_group_detail)
    # ndays
    template_groupId = 5400321
    if json_object_list:
        mode = 2
        template_groupId = groupId
    else:
        mode = 1

    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    instance_object.name = f"{fishery_id}{excel_tool.get_fishery_name(fishery_id=fishery_id)}渔场3天乐"
    instance_object.groupId = groupId
    instance_object.id = instance_object.groupId
    instance_object.enabled = 1
    instance_object.gConditions = []
    instance_object.fisheriesId = fishery_id
    instance_object.key = "N_DAYS"
    instance_object.subType = 6
    instance_object.keyDesc = "n天活动"
    instance_object.openType = 3
    instance_object.openArg = missionConditionID
    instance_object.closeType = 3
    instance_object.closeArg = 3
    instance_object.otherOpenConditions = [0, 0]
    instance_object.extArgs[0] = "0"
    instance_object.extArgs[1] = "2200"
    instance_object.extArgs[2] = "0"
    instance_object.extArgs[3] = "0"
    instance_object.extArgs[4] = "3"
    instance_object.extArgs[5] = f"{fishery_id}"
    instance_object.extArgs[6] = instance_object.extArgs[5]
    instance_object.extArgs[7] = "0"
    instance_object.extArgs[8] = "0"
    instance_object.extArgs[9] = "0"
    instance_object.imgName = "ActivityCenter_banner_bg_29"
    instance_object.activityName = activityNameId
    instance_object.imgNameInner = imgNameInner
    instance_object.iconName = "prepare_activity_RookieTasks_2"
    instance_object.tabOrder = 35
    instance_object.missionType = 54

    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

def mission_main(excel_tool: ExcelToolsForActivities,fishery_id, groupId, tokenID):
    mission_cfg_list = [
        {"template_missionID": 6031030,"missionRedirection":8, "template_missionConditionIDs": {6012760:["fishery_id", "fisheries_language"], } },
        {"template_missionID": 6031031,"missionRedirection":8, "template_missionConditionIDs": {6012761: ["fishery_id", "fisheries_language"],} },
        {"template_missionID": 6031032,"missionRedirection":8, "template_missionConditionIDs": {6012762: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6031033,"missionRedirection":8, "template_missionConditionIDs": {6012763: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6031034,"missionRedirection":8, "template_missionConditionIDs": {6012764: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6031035,"missionRedirection":8, "template_missionConditionIDs": {6012765: ["fishery_id", "fisheries_language"]}, 6012824:["fishery_id","fisheries_language"], },
        {"template_missionID": 6031036,"missionRedirection":8, "template_missionConditionIDs": {6012766: ["fishery_id", "fisheries_language"]}, 6012825:["fishery_id","fisheries_language"], },
        {"template_missionID": 6031037,"missionRedirection":8, "template_missionConditionIDs": {6012767: ["fishery_id", "fisheries_language"]}, 6012826:["fishery_id","fisheries_language"], },
        {"template_missionID": 6031038,"missionRedirection":8, "template_missionConditionIDs": {6012768: ["fishery_id", "fisheries_language"]}, 6012827:["fishery_id","fisheries_language"], },
        {"template_missionID": 6031039,"missionRedirection":8, "template_missionConditionIDs": {6012769: ["fishery_id", "fisheries_language"]}, 6012828:["fishery_id","fisheries_language"],},
        {"template_missionID": 6031040,"missionRedirection":8, "template_missionConditionIDs": {6012770: []}, 6012829:[],},
        {"template_missionID": 6031141,"missionRedirection":8, "template_missionConditionIDs": {6012771: []}, 6012830:[],},
        {"template_missionID": 6031142, "missionRedirection": 8,  "template_missionConditionIDs": {6012772: []}, 6012831:[],},
        {"template_missionID": 6031143, "missionRedirection": 8,  "template_missionConditionIDs": {6012773: []}},
        {"template_missionID": 6031144, "missionRedirection": 8, "template_missionConditionIDs": {6012774: []}},
        {"template_missionID": 6031145, "missionRedirection": 8, "template_missionConditionIDs": {6012775: ["fishery_id", "fisheries_language"]} },
        {"template_missionID": 6031146,"missionRedirection":8, "template_missionConditionIDs": {6012776: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031147, "missionRedirection": 8,  "template_missionConditionIDs": {6012777: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031148, "missionRedirection": 8,  "template_missionConditionIDs": {6012778: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031149, "missionRedirection": 8, "template_missionConditionIDs": {6012779: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031150, "missionRedirection": 8, "template_missionConditionIDs": {6012780: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031151, "missionRedirection": 8,  "template_missionConditionIDs": {6012781: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031152, "missionRedirection": 8, "template_missionConditionIDs": {6012782: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031153, "missionRedirection": 8, "template_missionConditionIDs": {6012783: ["fishery_id", "fisheries_language"]} },
        {"template_missionID": 6031154,"missionRedirection":8, "template_missionConditionIDs": {6012784: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031155, "missionRedirection": 8,  "template_missionConditionIDs": {6012785: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031156, "missionRedirection": 8,  "template_missionConditionIDs": {6012786: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031157,"missionRedirection":8, "template_missionConditionIDs": {6012787: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031158, "missionRedirection": 8,  "template_missionConditionIDs": {6012788: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031159, "missionRedirection": 9,  "template_missionConditionIDs": {6012789: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031160, "missionRedirection": 9, "template_missionConditionIDs": {6012790: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031161, "missionRedirection": 9,  "template_missionConditionIDs": {6012791: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031162, "missionRedirection": 9, "template_missionConditionIDs": {6012792: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031163, "missionRedirection": 9, "template_missionConditionIDs": {6012793: ["fishery_id", "fisheries_language"]} },
        {"template_missionID": 6031164,"missionRedirection":9, "template_missionConditionIDs": {6012794: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031165, "missionRedirection": 9,  "template_missionConditionIDs": {6012795: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031166, "missionRedirection": 9,  "template_missionConditionIDs": {6012796: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031167,"missionRedirection":9, "template_missionConditionIDs": {6012797: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031168, "missionRedirection": 9,  "template_missionConditionIDs": {6012798: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031169, "missionRedirection": 9,  "template_missionConditionIDs": {6012799: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031170, "missionRedirection": 9, "template_missionConditionIDs": {6012800: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031171, "missionRedirection": 9,  "template_missionConditionIDs": {6012801: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031172, "missionRedirection": 9,  "template_missionConditionIDs": {6012802: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031173, "missionRedirection": 9, "template_missionConditionIDs": {6012803: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031174, "missionRedirection": 7,  "template_missionConditionIDs": {6012804: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031175, "missionRedirection": 7,  "template_missionConditionIDs": {6012805: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031176, "missionRedirection": 7, "template_missionConditionIDs": {6012806: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031177, "missionRedirection": 8, "template_missionConditionIDs": {6012807: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031178, "missionRedirection": 8, "template_missionConditionIDs": {6012808: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031179, "missionRedirection": 8, "template_missionConditionIDs": {6012809: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031180, "missionRedirection": 8, "template_missionConditionIDs": {6012810: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031181, "missionRedirection": 8, "template_missionConditionIDs": {6012811: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031182, "missionRedirection": 8, "template_missionConditionIDs": {6012812: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031183, "missionRedirection": 8, "template_missionConditionIDs": {6012813: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031184, "missionRedirection": 8, "template_missionConditionIDs": {6012814: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031185, "missionRedirection": 8, "template_missionConditionIDs": {6012815: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031186, "missionRedirection": 8, "template_missionConditionIDs": {6012816: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031187, "missionRedirection": 8, "template_missionConditionIDs": {6012817: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031188, "missionRedirection": 8, "template_missionConditionIDs": {6012818: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031189, "missionRedirection": 8, "template_missionConditionIDs": {6012819: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031190, "missionRedirection": 8, "template_missionConditionIDs": {6012820: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031191, "missionRedirection": 8, "template_missionConditionIDs": {6012821: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031192, "missionRedirection": 8, "template_missionConditionIDs": {6012822: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6031193, "missionRedirection": 8, "template_missionConditionIDs": {6012823: ["fishery_id", "fisheries_language"]}},


    ]

    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    missionConditionID_start = excel_tool.get_min_value_more_than_start(key="missionConditionID", start=6012760, long=72, table_object_detail=mission_condition_detail)
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=mission_main_detail)
    if table_data_object_list:
        mode = 2
    else:
        mode = 1
    missionID_start = excel_tool.get_min_value_more_than_start(key="missionID", start=6031030, long=len(mission_cfg_list),table_object_detail=mission_main_detail)
    missionConditionID_set = set()
    key = "missionID"
    cur = 0
    while cur < len(mission_cfg_list):
        mission_cfg = mission_cfg_list[cur]
        instance_object: MISSION_MAIN

        if mode == 1:
            json_object, instance_object = excel_tool.get_object(key=key, value=mission_cfg["template_missionID"], table_data_detail=mission_main_detail, cls=MISSION_MAIN)
            instance_object.missionID = missionID_start + cur
            instance_object.name = instance_object.name.replace("琵琶湖", fishery_name)
            instance_object.missionName = instance_object.missionName.replace("琵琶湖", fishery_name)
            instance_object.missionDes = instance_object.missionDes.replace("琵琶湖", fishery_name)
            missionConditionID = missionConditionID_start + cur
            while missionConditionID in missionConditionID_set:
                missionConditionID += 1
            instance_object.missionConditionIDs[0] = missionConditionID
            missionConditionID_set.add(instance_object.missionConditionIDs[0])
            if len(mission_cfg["template_missionConditionIDs"]) > 1:
                instance_object.missionConditionIDs[1] = instance_object.missionConditionIDs[0] + 59
                missionConditionID_set.add(instance_object.missionConditionIDs[1])
        else:
            instance_object = json_to_instance(json_object=table_data_object_list[cur], cls=MISSION_MAIN)
            missionConditionID_set.add(instance_object.missionConditionIDs[0])
            if len(mission_cfg["template_missionConditionIDs"]) > 1:
                missionConditionID_set.add(instance_object.missionConditionIDs[1])
        # missionConditionID_set有该值就加一直到无重复
        if mission_cfg["missionRedirection"] == 8:
            instance_object.redirectionParams[0] = fishery_id
        instance_object.id = instance_object.missionID
        instance_object.enabled = 1
        instance_object.groupId = groupId
        instance_object.missionType = 54
        instance_object.awards[0].itemId = tokenID

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
            instance_object.name = instance_object.name.replace("琵琶湖", fishery_name)
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

def get_activityNameId(excel_tool: ExcelToolsForActivities, activityName):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="t_panellanguage", value=activityName, table_data_detail=panel_static_language_detail)
    if json_object_list:
        return json_object_list[0]["templateID"]
    return None

def get_tokenID(excel_tool: ExcelToolsForActivities, fishery_id):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="name", value=f"{fishery_id}{excel_tool.get_fishery_name(fishery_id=fishery_id)}渔场3天乐_代币", table_data_detail=item_main_detail)
    if json_object_list:
        return json_object_list[0]["itemTpId"]
    return None


def main(excel_tool: ExcelToolsForActivities, mode, fishery_id, activityName, imgNameInner):
    """
        读写方式：新增/修改
        mode=1 新增   mode=2 修改
    """

    groupId = 5000000 + fishery_id
    # 该区域参数为None则新增
    if mode == 1:
        missionConditionID = None            # 返场时间id (activity_double_week, battle_pass_main_2024, mission_group, timer_main)
        activityNameId= None  # panel_static_language里的templateID 返场活动名templateID
        tokenID= None                   # ndays积分币(event_n_day_tasks_milestone, item_main, item_main_language, mission_main, repeatable_challenge)
    else:
        missionConditionID = excel_tool.group_id_to_timer_id(group_id=groupId)
        activityNameId = get_activityNameId(excel_tool=excel_tool, activityName=activityName)
        tokenID = get_tokenID(excel_tool=excel_tool, fishery_id=fishery_id)

    # 配置修改区结束
    missionConditionID = mission_condition_open(excel_tool=excel_tool, fishery_id=fishery_id, missionConditionID=missionConditionID)
    activityNameId = panel_static_language(excel_tool=excel_tool, fishery_id=fishery_id, t_panellanguage=activityName, activityNameId=activityNameId)
    mission_group(excel_tool=excel_tool, missionConditionID=missionConditionID, fishery_id=fishery_id, activityNameId=activityNameId,imgNameInner=imgNameInner, groupId=groupId)
    tokenID = item_main(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    item_main_language(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    event_n_day_tasks_milestone(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)
    mission_main(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)
    print("涉及到的表：", list(excel_tool.data_txt_changed))
