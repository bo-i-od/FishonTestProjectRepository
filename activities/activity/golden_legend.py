from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_LANGUAGE import MISSION_LANGUAGE
from activities.decl.MISSION_MAIN import MISSION_MAIN
from tools import baseDataRead
from tools.commonTools import get_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities


"""
    国内金色传说配置模板
"""

def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, group_id: int, fishery_id: int):
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=group_id, table_data_detail=event_n_day_tasks_milestone_detail)
    for json_object in json_object_list:
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        instance_object = json_to_instance(json_object=json_object, cls=EVENT_N_DAY_TASKS_MILESTONE)
        fish_bag_id = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.milestoneRewards[0].itemId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
        if fish_bag_id:
            instance_object.milestoneRewards[0].itemId = fish_bag_id
        print(instance_object)
        excel_tool.change_object(key="autoId", value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)


def mission_condition(excel_tool: ExcelToolsForActivities, mission_condition_id: int, fishery_id: int=None, new_fishery_id: int=None, mission_condition_detail=None):
    if not mission_condition_detail:
        mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    instance_object: MISSION_CONDITION
    json_object, instance_object = excel_tool.get_object(key="missionConditionID", value=mission_condition_id, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
    if fishery_id:
        instance_object.triggerKeyM = fishery_id
    print(instance_object)
    excel_tool.change_object(key="missionConditionID", value=mission_condition_id, instance_object=instance_object, table_data_detail=mission_condition_detail)

def mission_language(excel_tool: ExcelToolsForActivities,  mission_language_id, fishery_id: int=None, new_fishery_id: int=None, mission_language_detail=None, fisheries_language_detail=None):
    if not mission_language_detail:
        mission_language_detail = excel_tool.get_table_data_detail(book_name="MISSION_LANGUAGE.xlsm")
    if not fisheries_language_detail:
        fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    instance_object: MISSION_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key="mission_language", value=mission_language_id,table_data_detail= mission_language_detail, cls=MISSION_LANGUAGE)
    if not fishery_id:
        return
    original_str = instance_object.t_missiondes
    # 定义定位标记
    start_marker = "在"
    end_marker_list = ["钓上", "捕获", "达成", "收集", "获得"]

    # 查找标记位置
    start_pos = original_str.find(start_marker)
    end_pos = -1
    for end_marker in end_marker_list:
        end_pos = original_str.find(end_marker)
        if end_pos < 0:
            continue
        break
    if end_pos >= 0:
        replace_start = start_pos + len(start_marker)
        replace_end = end_pos

        table_data_object = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_language_detail)
        instance_object.t_missiondes = original_str[:replace_start] + table_data_object["t_name"] + original_str[replace_end:]
    print(instance_object)
    excel_tool.change_object(key="mission_language", value=mission_language_id, instance_object=instance_object, table_data_detail=mission_language_detail)


def mission_main(excel_tool: ExcelToolsForActivities, group_id: int, fishery_id: int):
    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    mission_language_detail = excel_tool.get_table_data_detail(book_name="MISSION_LANGUAGE.xlsm")
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=group_id, table_data_detail=mission_main_detail)
    for json_object in json_object_list:
        instance_object: MISSION_MAIN
        instance_object = json_to_instance(json_object=json_object, cls=MISSION_MAIN)
        mission_condition_id = instance_object.missionConditionIDs[0]
        mission_language_id = instance_object.mission_language
        fishery_detail = excel_tool.get_fishery_detail(fishery_id=instance_object.redirectionParams[0], fisheries_detail=fisheries_detail)
        if fishery_detail:
            instance_object.redirectionParams[0] = fishery_id
            mission_condition(excel_tool=excel_tool, fishery_id=fishery_id,  mission_condition_id=mission_condition_id, mission_condition_detail=mission_condition_detail)
            mission_language(excel_tool=excel_tool, fishery_id=fishery_id, mission_language_id=mission_language_id, mission_language_detail=mission_language_detail, fisheries_language_detail=fisheries_language_detail)
        print(instance_object)
        excel_tool.change_object(key="missionID", value=json_object["missionID"], instance_object=instance_object, table_data_detail=mission_main_detail)



def mission_group(excel_tool: ExcelToolsForActivities, group_id:int, fishery_id: int):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key="groupId", value=group_id, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    instance_object.fisheriesId = fishery_id
    instance_object.openArg = timer_id
    instance_object.closeArg = timer_id

    # instance_object.extArgs[6] = get_fisheries()
    print(instance_object)
    excel_tool.change_object(key="groupId", value=group_id, table_data_detail=mission_group_detail, instance_object=instance_object)

    group_id = group_id + 1
    json_object, instance_object = excel_tool.get_object(key="groupId", value=group_id, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    instance_object.fisheriesId = fishery_id
    instance_object.openArg = timer_id
    instance_object.closeArg = timer_id

    print(instance_object)
    excel_tool.change_object(key="groupId", value=group_id, table_data_detail=mission_group_detail, instance_object=instance_object)


def timer_main(excel_tool: ExcelToolsForActivities, group_id, time_start):
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    time_end = get_time(time=time_start, days=7, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)


def main():
    """
        读写方式：修改

    """
    # 配置修改区起始
    time_start = "2025-05-02 00:00:00"
    group_id = 2010807
    fishery_id = 400318      # 旧主线活动渔场
    new_fishery_id = 500302  # 新主线渔场

    # 配置修改区结束
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_main(excel_tool=excel_tool, group_id=group_id,  time_start=time_start)
    mission_group(excel_tool=excel_tool, group_id=group_id, fishery_id=new_fishery_id)
    event_n_day_tasks_milestone(excel_tool=excel_tool, group_id=group_id, fishery_id=fishery_id)
    mission_main(excel_tool=excel_tool, group_id=group_id, fishery_id=fishery_id)

    print("涉及到的表：", list(excel_tool.data_txt_changed))

if __name__ == '__main__':
    main()

