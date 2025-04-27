from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_MAIN import MISSION_MAIN
from tools import baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    新主线ndays配置模板
"""


def mission_group(excel_tool: ExcelToolsForActivities, fishery_id, activityName, imgNameInner, missionType, openArg, groupId=None):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    key = "groupId"
    template_groupId = 5100039
    id = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_group_detail, start=template_groupId)
    if groupId is None:
        mode = 1
        groupId = max(excel_tool.get_min_value_more_than_start(key=key, table_object_detail=mission_group_detail, start=template_groupId), id)
    else:
        mode = 0
        template_groupId = groupId

    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_groupId, table_data_detail=mission_group_detail)
    instance_object: MISSION_GROUP
    instance_object = json_to_instance(json_object=json_object_list[0], cls=MISSION_GROUP)
    if mode == 1:
        instance_object.id = groupId
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}-配套活动"
    instance_object.groupId =groupId
    instance_object.openArg = openArg
    instance_object.extArgs[5] = fishery_id
    instance_object.extArgs[6] = fishery_id
    instance_object.activityName = activityName
    instance_object.imgNameInner = imgNameInner
    instance_object.missionType = missionType
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, instance_object=instance_object, table_data_detail=mission_group_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, instance_object=instance_object, table_data_detail=mission_group_detail)
    return groupId

def item_main(excel_tool: ExcelToolsForActivities, fishery_id, tokenID):
    # 活动代币
    template_itemTpId = 290042
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_detail)
    if table_data_object_list:
        mode = 0
        template_itemTpId = table_data_object_list[0]["itemTpId"]
    else:
        mode = 1
    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}活动代币"
    instance_object.itemTpId = tokenID
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)

def item_main_language(excel_tool: ExcelToolsForActivities,fishery_id, tokenID):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"
    # 活动代币
    template_tpId = 290042
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 0
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    instance_object.name = f"{fishery_id}双周返场活动代币"
    instance_object.tpId = tokenID
    instance_object.t_description = f"在{excel_tool.get_fishery_name(fishery_id=fishery_id)}活动中收集活动积分，赢取额外奖励。"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
def mission_condition(excel_tool: ExcelToolsForActivities, fishery_id,fishery_index, mission_cfg,spot_id_start, missionConditionID_start=None):
    def apply_cfg(mission_condition_object:MISSION_CONDITION , cfg):
        if "spot_language" in cfg:
            value = cfg["spot_language"]
            mission_condition_object.numDisplay[0] = f"panel_static_language|t_panellanguage|{value}"
        if "spot_index" in cfg:
            value = cfg["spot_index"]
            mission_condition_object.triggerKeyM= spot_id_start + value
        if "challenge" in cfg:
            value = cfg["challenge"]
            mission_condition_object.triggerKeyM = value + 999900 + fishery_index * 100
            mission_condition_object.numDisplay[0] = str(fishery_index)
            mission_condition_object.numDisplay[1] = str(value)

        if "fishery_id" in cfg:
            value = cfg["fishery_id"]
            mission_condition_object.numDisplay[0] = f"fisheries_language|t_name|{value}"
            mission_condition_object.triggerKeyM = str(value)
        if "new_plot_quest" in cfg:
            value = cfg["new_plot_quest"]
            mission_condition_object.numDisplay[0] = f"new_plot_quest_language|Questname|{value}"
            mission_condition_object.triggerKeyM = str(value)
        if "tower_lv" in cfg:
            value = cfg["tower_lv"]
            mission_condition_object.triggerValue = value
            mission_condition_object.numDisplay[0] = str(value)
        if "gear_lv" in cfg:
            value = cfg["gear_lv"]
            mission_condition_object.triggerValue = value
            mission_condition_object.numDisplay[2] = str(value)
        if "tower_star" in cfg:
            value = cfg["tower_star"]
            mission_condition_object.triggerValue = value
            mission_condition_object.numDisplay[0] = str(value)

    cfg_dict = {
        0: {"spot_language": mission_cfg["spot_language_list"][0], "spot_index": 0},
        2: {"challenge": 1},
        5: {"fishery_id": fishery_id},
        8: {"new_plot_quest": mission_cfg["new_plot_quest_list"][0]},
        10: {"spot_language": mission_cfg["spot_language_list"][0], "spot_index": 1},
        12: {"fishery_id": fishery_id},
        13: {"fishery_id": fishery_id},
        14: {"challenge": 3},
        15: {"challenge": 6},
        16: {"challenge": 10},
        18: {"new_plot_quest": mission_cfg["new_plot_quest_list"][1]},
        20: {"spot_language": mission_cfg["spot_language_list"][1], "spot_index": 2},
        22: {"fishery_id": fishery_id},
        28: {"new_plot_quest": mission_cfg["new_plot_quest_list"][2]},
        30: {"spot_language": mission_cfg["spot_language_list"][1], "spot_index": 3},
        31: {"fishery_id": fishery_id},
        32: {"fishery_id": fishery_id},
        37: {"tower_lv": mission_cfg["tower_lv_list"][0]},
        38: {"new_plot_quest": mission_cfg["new_plot_quest_list"][3]},
        40: {"fishery_id": fishery_id},
        41: {"fishery_id": fishery_id},
        42: {"fishery_id": fishery_id},
        43: {"gear_lv": mission_cfg["gear_lv"]},
        44: {"gear_lv": mission_cfg["gear_lv"]},
        45: {"gear_lv": mission_cfg["gear_lv"]},
        47: {"tower_lv": mission_cfg["tower_lv_list"][1]},
        50: {"spot_language": mission_cfg["spot_language_list"][0], "spot_index": 4},
        52: {"fishery_id": fishery_id},
        53: {"challenge": 15},
        54: {"challenge": 20},
        55: {"challenge": 25},
        56: {"challenge": 30},
        57: {"tower_lv": mission_cfg["tower_lv_list"][2]},
        58: {"new_plot_quest": mission_cfg["new_plot_quest_list"][4]},
        60: {"fishery_id": fishery_id},
        61: {"fishery_id": fishery_id},
        62: {"fishery_id": fishery_id},
        63: {"tower_star": mission_cfg["tower_star_list"][0]},
        64: {"tower_star": mission_cfg["tower_star_list"][1]},
        65: {"tower_star": mission_cfg["tower_star_list"][2]},
        66: {"tower_star": mission_cfg["tower_star_list"][3]},
        67: {"tower_lv": mission_cfg["tower_lv_list"][3]},
    }
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    key = "missionConditionID"
    template_missionConditionID_start = 6011951
    if missionConditionID_start is None:
        mode = 1
        missionConditionID_start = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=mission_condition_detail, start=template_missionConditionID_start)
    else:
        mode = 0
        template_missionConditionID_start = missionConditionID_start
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_condition_detail, start=134845, long=70)
    cur = 0
    while cur < 70:
        instance_object: MISSION_CONDITION
        json_object, instance_object = excel_tool.get_object(key=key, value=template_missionConditionID_start + cur, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.missionConditionID = missionConditionID_start + cur
        name_split = instance_object.name.split("卡多湖")
        if len(name_split) > 1:
            instance_object.name = name_split[0] + excel_tool.get_fishery_name(fishery_id=fishery_id) + name_split[1]
        if cur in cfg_dict:
            apply_cfg(instance_object, cfg_dict[cur])
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, instance_object=instance_object, table_data_detail=mission_condition_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, instance_object=instance_object, table_data_detail=mission_condition_detail)
        cur += 1
    return missionConditionID_start


def mission_main(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID, missionConditionID_start, missionType):
    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    fish_bag_detail = baseDataRead.convert_to_json(path=excel_tool.root_dir + "/activities/customTables/", prefix="FISH_BAG")
    template_groupId = 5100039
    key = "missionID"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=mission_main_detail)
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_main_detail, start=134181, long=70)
    if json_object_list:
        mode = 0
        missionID_start = json_object_list[0]["missionID"]
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=mission_main_detail)
        missionID_start = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=mission_main_detail, start=json_object_list[0]["missionID"], long=69)
    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    key = "missionID"
    cur = 0
    while cur < len(json_object_list):
        instance_object: MISSION_MAIN
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=MISSION_MAIN)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.missionID = missionID_start + cur
        instance_object.missionType = missionType
        instance_object.groupId = groupId
        name_split = instance_object.name.split("卡多湖")
        if len(name_split) > 1:
            instance_object.name = name_split[0] + fishery_name + name_split[1]
        name_split = instance_object.missionName.split("卡多湖")
        if len(name_split) > 1:
            instance_object.missionName = name_split[0] + fishery_name + name_split[1]
        name_split = instance_object.missionDes.split("卡多湖")
        if len(name_split) > 1:
            instance_object.missionDes = name_split[0] + fishery_name + name_split[1]
        instance_object.missionConditionIDs[0] = missionConditionID_start + cur
        instance_object.awards[0].itemId = tokenID
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.awards[1].itemId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
        if not fish_bag:
            instance_object.awards[1].itemId = fish_bag
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.missionID, instance_object=instance_object, table_data_detail=mission_main_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionID, instance_object=instance_object, table_data_detail=mission_main_detail)
        cur += 1

def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID, big_reward):
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    template_groupId = 5100039
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=event_n_day_tasks_milestone_detail)
    key = "autoId"
    if json_object_list:
        mode = 0
        autoId_start = json_object_list[0][key]
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=event_n_day_tasks_milestone_detail)
        autoId_start = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=event_n_day_tasks_milestone_detail, start=json_object_list[0][key], long=len(json_object_list))
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=event_n_day_tasks_milestone_detail, start=json_object_list[0]["id"], long=len(json_object_list))
    cur = 0
    while cur < len(json_object_list):
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        instance_object = json_to_instance(json_object=json_object_list[cur],  cls=EVENT_N_DAY_TASKS_MILESTONE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = excel_tool.get_fishery_name(fishery_id=fishery_id) + "配套"
        instance_object.autoId = autoId_start + cur
        instance_object.tokenID = tokenID
        instance_object.groupId = groupId
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.milestoneRewards[0].itemId, fishery_id=fishery_id)
        if fish_bag:
            instance_object.milestoneRewards[0].itemId = fish_bag
        if cur == len(json_object_list) - 1:
            instance_object.milestoneRewards[0].itemType = big_reward["itemType"]
            instance_object.milestoneRewards[0].itemId = big_reward["itemId"]
            instance_object.milestoneRewards[0].itemCount = big_reward["itemCount"]
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        cur += 1


def main():

    fishery_id = 500302
    activityName = 19960937
    imgNameInner = "ActivityTasks_banner_bg_70"
    missionType = 84
    tokenID = 260071
    big_reward = {"itemId": 1700020, "itemType": 17, "itemCount": 1}
    openArg = 6012129
    mission_cfg = {
        "spot_language_list": [42256, 42257],
        "new_plot_quest_list": [80000108, 80000112, 80000125, 80000131, 80000145],
        "tower_lv_list": [7, 8, 9, 9],
        "tower_star_list": [40, 50, 60, 75],
        "gear_lv": 130,
    }
    groupId = 5200180  # None为新增
    missionConditionID_start = None # None为新增
    fishery_index = fishery_id - 500300
    spot_id_start = 10001 + 100 * fishery_index

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    groupId = mission_group(excel_tool=excel_tool, groupId=groupId, fishery_id=fishery_id, activityName=activityName, imgNameInner=imgNameInner, missionType=missionType, openArg=openArg)
    item_main(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    item_main_language(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    missionConditionID_start = mission_condition(excel_tool=excel_tool,  fishery_id=fishery_id, fishery_index=fishery_index, mission_cfg=mission_cfg,spot_id_start=spot_id_start, missionConditionID_start=missionConditionID_start)
    mission_main(excel_tool=excel_tool,  fishery_id=fishery_id, groupId=groupId, missionType=missionType, tokenID=tokenID, missionConditionID_start=missionConditionID_start)
    event_n_day_tasks_milestone(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID, big_reward=big_reward)

if __name__ == '__main__':
    main()
