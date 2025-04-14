from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_LANGUAGE import MISSION_LANGUAGE
from activities.decl.MISSION_MAIN import MISSION_MAIN
from common.error import FindNoElementError
from configs.pathConfig import EXCEL_PATH
from tools.commonTools import get_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities


fishing_king_cfg = [
    # event_n_day_tasks_milestone
    {"groupId": 2010801,"autoId": 246, "fishBagType": 1, "fishCardCount": 50},
    {"groupId": 2010801,"autoId": 252, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 2010801,"autoId": 254, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 2010803,"autoId": 262, "fishBagType": 1, "fishCardCount": 50},
    {"groupId": 2010803,"autoId": 268, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 2010803,"autoId": 270, "fishBagType": 1, "fishCardCount": 200},

    # mission_main
    {"groupId": 2010801, "missionConditionID": 2130321, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 2130322, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 2130323, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 2130324, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 2130325, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 2130326, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 2130327, "is_new_fishery": False},
    {"groupId": 2010801, "missionConditionID": 6012115, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012116, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012117, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012118, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012119, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012120, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012121, "is_new_fishery": True},
    {"groupId": 2010801, "missionConditionID": 6012122, "is_new_fishery": True},


    {"groupId": 2010803, "missionConditionID": 2130314, "is_new_fishery": False},
    {"groupId": 2010803, "missionConditionID": 2130315, "is_new_fishery": False},
    {"groupId": 2010803, "missionConditionID": 2130316, "is_new_fishery": False},
    {"groupId": 2010803, "missionConditionID": 2130317, "is_new_fishery": False},
    {"groupId": 2010803, "missionConditionID": 2130318, "is_new_fishery": False},
    {"groupId": 2010803, "missionConditionID": 2130319, "is_new_fishery": False},
    {"groupId": 2010803, "missionConditionID": 2130320, "is_new_fishery": False},

    {"groupId": 2010803, "missionConditionID": 6012115, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012116, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012117, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012118, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012119, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012120, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012121, "is_new_fishery": True},
    {"groupId": 2010803, "missionConditionID": 6012122, "is_new_fishery": True},
]


def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, group_id:int, fishery_id: int):
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    for cfg in fishing_king_cfg:
        if "autoId" not in cfg:
            continue
        if group_id != cfg["groupId"]:
            continue
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        json_object, instance_object = excel_tool.get_object(key="autoId", value=cfg["autoId"], table_data_detail=event_n_day_tasks_milestone_detail, cls=EVENT_N_DAY_TASKS_MILESTONE)
        fish_bag_type = cfg["fishBagType"]
        fish_card_count = cfg["fishCardCount"]
        print(instance_object)
        # 查鱼卡包
        instance_object.milestoneRewards[0].itemId = excel_tool.get_fish_bag(fishery_id=fishery_id, fish_bag_type=fish_bag_type, fish_card_count=fish_card_count)
        excel_tool.change_object(key="id", value=instance_object.id, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)


def mission_condition(excel_tool: ExcelToolsForActivities, mission_condition_id: int, fishery_id: int=None, new_fishery_id: int=None, mission_condition_detail=None):
    if not mission_condition_detail:
        mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    instance_object: MISSION_CONDITION
    json_object, instance_object = excel_tool.get_object(key="missionConditionID", value=mission_condition_id,table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
    if fishery_id:
        instance_object.triggerKeyM = fishery_id
    if new_fishery_id:
        instance_object.triggerKeyM = new_fishery_id
        instance_object.numDisplay = f"fisheries_language|t_name|{new_fishery_id}"
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
    end_marker = "钓上"

    # 查找标记位置
    start_pos = original_str.find(start_marker)
    end_pos = original_str.find(end_marker)

    replace_start = start_pos + len(start_marker)
    replace_end = end_pos

    table_data_object = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_language_detail)
    instance_object.t_missiondes = original_str[:replace_start] + table_data_object["t_name"] + original_str[replace_end:]
    print(instance_object)
    excel_tool.change_object(key="mission_language", value=mission_language_id, instance_object=instance_object, table_data_detail=mission_language_detail)


def mission_main(excel_tool: ExcelToolsForActivities, group_id: int, fishery_id: int, new_fishery_id: int):
    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    mission_language_detail = excel_tool.get_table_data_detail(book_name="MISSION_LANGUAGE.xlsm")
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    print(f"----------------{mission_main_detail[2]} {mission_language_detail[2]} {mission_condition_detail[2]}正在修改----------------")
    for cfg in fishing_king_cfg:
        if "missionConditionID" not in cfg:
            continue
        if group_id != cfg["groupId"]:
            continue
        # key = "missionConditionID", value = cfg["missionConditionID"],
        json_object_list, _, _ = mission_main_detail
        for json_object in json_object_list:
            if "missionConditionIDs" not in json_object:
                continue
            if cfg["missionConditionID"] not in json_object["missionConditionIDs"]:
                continue
            instance_object: MISSION_MAIN
            instance_object = json_to_instance(json_object=json_object, cls=MISSION_MAIN)
            mission_condition_id = instance_object.missionConditionIDs[0]
            mission_language_id = instance_object.mission_language
            if cfg["is_new_fishery"]:
                instance_object.missionRedirection = 30

                mission_condition(excel_tool=excel_tool, new_fishery_id=new_fishery_id, mission_condition_id=mission_condition_id, mission_condition_detail=mission_condition_detail)
                mission_language(excel_tool=excel_tool, new_fishery_id=new_fishery_id, mission_language_id=mission_language_id, mission_language_detail=mission_language_detail, fisheries_language_detail=fisheries_language_detail)

            else:
                instance_object.missionRedirection = 8
                # 新主线渔场跳转到新主线界面
                instance_object.redirectionParams[0] = fishery_id
                mission_condition(excel_tool=excel_tool, fishery_id=fishery_id, mission_condition_id=mission_condition_id, mission_condition_detail=mission_condition_detail)
                mission_language(excel_tool=excel_tool, fishery_id=fishery_id, mission_language_id=mission_language_id, mission_language_detail=mission_language_detail, fisheries_language_detail=fisheries_language_detail)

            print(instance_object)
            excel_tool.change_object(key="missionID", value=json_object["missionID"], instance_object=instance_object, table_data_detail=mission_main_detail)




        print(f"----------------{mission_main_detail[2]} {mission_language_detail[2]} {mission_condition_detail[2]}修改完成----------------")


def mission_group(excel_tool: ExcelToolsForActivities, group_id:int, fishery_id: int):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    prefix = mission_group_detail[2]
    print(f"----------------{prefix} 正在修改----------------")
    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key="groupId", value=group_id, table_data_detail=mission_group_detail, cls=MISSION_GROUP)

    print(json_to_block(json_object=json_object, name=prefix.lower()))
    print("\n        ⬇⬇⬇⬇⬇⬇        \n")

    instance_object.fisheriesId = fishery_id

    print(instance_to_block(instance_object=instance_object, name=prefix.lower()))
    print("- - - - - - - - - - - - - - - -")

    excel_tool.change_object(key="groupId", value=group_id, table_data_detail=mission_group_detail, instance_object=instance_object)
    print(f"----------------{prefix} 修改完成----------------\n")


def timer_main(excel_tool: ExcelToolsForActivities, time_start, timer_id):
    time_end = get_time(time=time_start, days=7, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)



def main():
    time_start = "2025-04-25 00:00:00"
    group_id = 2010801
    fishery_id = 400318
    new_fishery_id = 500302
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    timer_main(excel_tool=excel_tool, time_start=time_start, timer_id=timer_id)
    event_n_day_tasks_milestone(excel_tool=excel_tool, group_id=group_id, fishery_id=fishery_id)
    mission_main(excel_tool=excel_tool,group_id=group_id, fishery_id=fishery_id, new_fishery_id=new_fishery_id)




if __name__ == '__main__':
    main()
