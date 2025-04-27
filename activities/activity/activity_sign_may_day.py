from configs.pathConfig import EXCEL_PATH
from tools import commonTools
from tools.excelRead import ExcelToolsForActivities

"""
    七日签到配置模板
"""

def timer_main(excel_tool: ExcelToolsForActivities, group_id, open_time):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    table_data_object = excel_tool.get_table_data_object_by_key_value(key="groupId", value=group_id, table_data_detail=mission_group_detail)
    timer_id = table_data_object["openArg"]
    timer_id_limit = table_data_object["charaOpenTmDivision"]
    time_end = commonTools.get_time(time=open_time, days=7, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=open_time, time_end=time_end)
    excel_tool.timer_main(timer_id=timer_id_limit, time_start=open_time, time_end=time_end)


def activity_sign_may_day(excel_tool: ExcelToolsForActivities,group_id, big_reward):
    activity_sign_may_day_detail = excel_tool.get_table_data_detail(book_name="ACTIVITY_SIGN_MAY_DAY.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupid", value=group_id, table_data_detail=activity_sign_may_day_detail)
    json_object = json_object_list[-1]
    json_object["type"] = big_reward["itemType"]
    json_object["rewardid"] = big_reward["tpId"]
    json_object["count"] = big_reward["count"]
    print(json_object)
    excel_tool.change_object(key="activeid", value=json_object["activeid"], table_data_detail=activity_sign_may_day_detail, json_object=json_object)

def global_value(excel_tool: ExcelToolsForActivities, prefab):
    global_value_detail = excel_tool.get_table_data_detail(book_name="GLOBAL_VALUE.xlsm")
    key = "key"
    value = "ACTIVITY_SIGN_MAY_DAY_PREFAB"
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=value, table_data_detail=global_value_detail)
    json_object["value"] = prefab
    print(json_object)
    excel_tool.change_object(key=key, value=value, table_data_detail=global_value_detail, json_object=json_object)

def main():
    group_id = 2020003
    open_time = "2025-05-01 00:00:00"
    big_reward = {"tpId": 100500, "itemType": 1, "count": 800}
    prefab = "Panel_Events_singin_7day"
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_main(excel_tool=excel_tool, group_id=group_id, open_time=open_time)
    activity_sign_may_day(excel_tool=excel_tool, group_id=group_id, big_reward=big_reward)
    global_value(excel_tool=excel_tool, prefab=prefab)



if __name__ == '__main__':
    main()