import os
import sys

from activities.decl.ENUM_MAPPING import ENUM_MAPPING
from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_MAIN import MISSION_MAIN
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.fishery.load_tools import get_cfg_ndays
from activities.fishery.temp.main_id import load_main_id, save_main_id
from tools import baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    新主线ndays配置模板
"""

def panel_static_language(excel_tool: ExcelToolsForActivities, title, title_id=None):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    key = "templateID"
    if title_id is None:
        mode = 1
        instance_object = PANEL_STATIC_LANGUAGE()
        title_id = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=panel_static_language_detail, start=1998237)
        instance_object.templateID = title_id
        instance_object.id = instance_object.templateID

    else:
        mode = 2
        instance_object: PANEL_STATIC_LANGUAGE
        json_object, instance_object = excel_tool.get_object(key=key, value=title_id, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)
    instance_object.name = "新鱼场活动"
    instance_object.t_panellanguage = title
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.templateID, instance_object=instance_object, table_data_detail=panel_static_language_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, instance_object=instance_object, table_data_detail=panel_static_language_detail)
    return title_id


def mission_group(excel_tool: ExcelToolsForActivities, fishery_id, title_id, imgNameInner, groupId=None, openArg=None):
    # 在mission_condition中新增章节开启
    def get_openArg():
        mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
        instance_obj = MISSION_CONDITION()
        instance_obj.id = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_condition_detail, start=135054)
        instance_obj.missionConditionID = excel_tool.get_min_value_more_than_start(key="missionConditionID", table_object_detail=mission_condition_detail, start=6011950)
        instance_obj.enabled = 1
        instance_obj.triggerTypeId = 9800100
        instance_obj.triggerDataMode = 1
        instance_obj.triggerKeyM = fishery_id
        instance_obj.triggerValue = 1
        instance_obj.numDisplay = ["0", "0", "0"]
        instance_obj.numDisplay_Title = ["0", "0", "0"]
        excel_tool.add_object(key="missionConditionID", value=instance_obj.missionConditionID, instance_object=instance_obj, table_data_detail=mission_condition_detail)
        return instance_obj.missionConditionID

    if openArg is None:
        openArg = get_openArg()



    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    key = "groupId"
    template_groupId = 5100039
    if groupId is None:
        mode = 1
        groupId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=mission_group_detail, start=template_groupId)
    else:
        mode = 2
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
    instance_object.activityName = title_id
    instance_object.imgNameInner = imgNameInner
    instance_object.missionType = 82
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, instance_object=instance_object, table_data_detail=mission_group_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, instance_object=instance_object, table_data_detail=mission_group_detail)
    return groupId, openArg

def item_main(excel_tool: ExcelToolsForActivities, fishery_id, tokenID=None):
    # 活动代币
    template_itemTpId = 290042
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
    if mode == 1:
        instance_object.itemTpId = tokenID
        instance_object.id = instance_object.itemTpId
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}活动代币"
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
    template_tpId = 290042
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 2
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}活动代币"
    instance_object.tpId = tokenID
    instance_object.t_description = f"活动积分，积累进度赢取额外奖励"
    print(instance_object)
    if mode == 2:
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
        if "point" in cfg:
            value = cfg["point"]
            mission_condition_object.triggerTypeId = 9800005
            mission_condition_object.triggerValue = value * 10000
            mission_condition_object.triggerDataMode=2
            mission_condition_object.name = "在xx渔场的累计鱼获分数达到yyy"
            mission_condition_object.numDisplay[1] = f"{value}W"
            mission_condition_object.numDisplay_Title = ["0", "0", "0"]
            mission_condition_object.triggerKeyM=None

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
        if "order" in cfg:
            value = cfg["order"]
            mission_condition_object.name = f"累计完成{value}个订单"
            mission_condition_object.triggerTypeId=9800220
            mission_condition_object.triggerDataMode=2
            mission_condition_object.triggerValue=value
            mission_condition_object.numDisplay = [f"{value}", "0", "0"]
            mission_condition_object.numDisplay_Title = ["0", "0", "0"]
            mission_condition_object.triggerKeyM=None


    cfg_dict = {
        0: {"spot_language": mission_cfg["spot_language_list"][0], "spot_index": 0},
        2: {"order": 2},
        3: {"fishery_id": fishery_id},
        5: {"fishery_id": fishery_id},
        8: {"new_plot_quest": mission_cfg["new_plot_quest_list"][0]},
        10: {"spot_language": mission_cfg["spot_language_list"][0], "spot_index": 1},
        12: {"fishery_id": fishery_id},
        13: {"fishery_id": fishery_id},
        14: {"point": 200, "fishery_id": fishery_id},
        15: {"point": 500, "fishery_id": fishery_id},
        16: {"point": 1000, "fishery_id": fishery_id},
        17: {"order": 4},
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
        53: {"point": 1500, "fishery_id": fishery_id},
        54: {"point": 2000, "fishery_id": fishery_id},
        55: {"point": 2500, "fishery_id": fishery_id},
        56: {"point": 3000, "fishery_id": fishery_id},
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
        missionConditionID_start = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=mission_condition_detail, start=template_missionConditionID_start, long=70)
    else:
        mode = 2
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
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, instance_object=instance_object, table_data_detail=mission_condition_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, instance_object=instance_object, table_data_detail=mission_condition_detail)
        cur += 1
    return missionConditionID_start


def mission_main(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID, missionConditionID_start):
    cfg = {
        2: {"order": 2},
        14: {"point": 200},
        15: {"point": 500},
        16: {"point": 1000},
        17: {"order": 4},
        53: {"point": 1500},
        54: {"point": 2000},
        55: {"point": 2500},
        56: {"point": 3000},
    }
    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    template_groupId = 5100039
    key = "missionID"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=mission_main_detail)
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=mission_main_detail, start=134181, long=70)
    if json_object_list:
        mode = 2
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
        instance_object.missionType = 82
        instance_object.groupId = groupId
        if cur in cfg:
            if "order" in cfg[cur]:
                instance_object.name = f"累计完成{cfg[cur]['order']}个订单"
                instance_object.mission_language = 6011712
                instance_object.missionName = instance_object.name
                instance_object.missionDes = instance_object.name
            if "point" in cfg[cur]:
                instance_object.name = f"累计得到{cfg[cur]['point']}w分"
                instance_object.mission_language = 6011720
                instance_object.missionName = instance_object.name
                instance_object.missionDes = instance_object.name

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
        if fish_bag:
            instance_object.awards[1].itemId = fish_bag
        print(instance_object)
        if mode == 2:
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
        mode = 2
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

        # 金币碳布1.5倍
        if mode == 1 and instance_object.milestoneRewards[0].itemId in [102800, 102900]:

            instance_object.milestoneRewards[0].itemCount = int(1.5 * instance_object.milestoneRewards[0].itemCount)


        if fish_bag:
            instance_object.milestoneRewards[0].itemId = fish_bag
        if cur == len(json_object_list) - 1:
            instance_object.milestoneRewards[0].itemType = big_reward["itemType"]
            instance_object.milestoneRewards[0].itemId = big_reward["itemId"]
            instance_object.milestoneRewards[0].itemCount = big_reward["itemCount"]
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        cur += 1

# def enum_mapping(excel_tool: ExcelToolsForActivities, missionType, fishery_id):
#     enum_mapping_detail = excel_tool.get_table_data_detail(book_name="ENUM_MAPPING.xlsm")
#     template_value = 84
#     key = "value"
#     json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="value", value=missionType, table_data_detail=enum_mapping_detail)
#     if json_object_list:
#         mode = 2
#     else:
#         mode = 1
#         json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="value", value=template_value, table_data_detail=enum_mapping_detail)
#     instance_object: ENUM_MAPPING
#     instance_object = json_to_instance(json_object=json_object_list[0], cls=ENUM_MAPPING)
#     if mode == 1:
#         instance_object.id = excel_tool.get_min_value_more_than_start(table_object_detail=enum_mapping_detail, start=493, key_list=["id", "enumAutoID"])
#         instance_object.enumAutoID = instance_object.id
#         instance_object.name = instance_object.id
#     instance_object.enumName = "MissionTypeEnum"
#     instance_object.key = f"FISH_SCENE_N_DAYS_NEW_{instance_object.enumAutoID}"
#     instance_object.value = missionType
#     instance_object.desc = f"任务类型-{excel_tool.get_fishery_name(fishery_id=fishery_id)}十天乐"
#     print(instance_object)
#     if mode == 2:
#         excel_tool.change_object(key=key, value=instance_object.value, table_data_detail=enum_mapping_detail, instance_object=instance_object)
#     else:
#         excel_tool.add_object(key=key, value=instance_object.value, table_data_detail=enum_mapping_detail, instance_object=instance_object)



def main(excel_tool: ExcelToolsForActivities, mode=1):
    """
        读写方式：新增/修改
        mode=1 新增   mode=2 修改
    """

    file_name = os.path.basename(__file__).split('.')[0]

    cfg = get_cfg_ndays()
    print("cfg:", cfg)
    fishery_id = cfg["fishery_id"]
    title = cfg["title"]
    imgNameInner = cfg["imgNameInner"]  # 活动左侧背景
    big_reward = cfg["big_reward"]

    mission_cfg = cfg["mission_cfg"]

    # 该区域参数为None则新增
    if mode == 1:
        groupId = None  # mission_group的groupId
        title_id = None    # panel_static_language中templateID 活动标题
        missionConditionID_start = None  # mission_condition的missionConditionID 系列任务的起始
        openArg = None  # mission_condition的missionConditionID 解锁该渔场
        tokenID = None  # item_main的itemTpId 活动代币
    else:
        id_dict = load_main_id(file_name=file_name)
        print("id_dict:", id_dict)
        groupId = id_dict["groupId"]
        title_id = id_dict["title_id"]
        missionConditionID_start = id_dict["missionConditionID_start"]
        openArg = id_dict["openArg"]
        tokenID = id_dict["tokenID"]


    # 根据偏移算中间值，当渔场id不按顺序新增时可能有问题
    fishery_index = fishery_id - 500300
    spot_id_start = 10001 + 100 * fishery_index

    # 配置修改区结束
    title_id = panel_static_language(excel_tool=excel_tool, title=title, title_id=title_id)
    groupId, openArg = mission_group(excel_tool=excel_tool, groupId=groupId, fishery_id=fishery_id, title_id=title_id, imgNameInner=imgNameInner, openArg=openArg)
    tokenID = item_main(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    item_main_language(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    missionConditionID_start = mission_condition(excel_tool=excel_tool,  fishery_id=fishery_id, fishery_index=fishery_index, mission_cfg=mission_cfg, spot_id_start=spot_id_start, missionConditionID_start=missionConditionID_start)
    mission_main(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID, missionConditionID_start=missionConditionID_start)
    event_n_day_tasks_milestone(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID, big_reward=big_reward)

    save_main_id(file_name=file_name, id_dict={"groupId": groupId, "title_id": title_id, "missionConditionID_start": missionConditionID_start, "openArg": openArg, "tokenID": tokenID})
    print("涉及到的表：", list(excel_tool.data_txt_changed))

if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool, mode=2)
