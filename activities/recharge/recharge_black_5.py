from configs.pathConfig import EXCEL_PATH
from tools import commonTools
from tools.excelRead import ExcelToolsForActivities

"""
    三日礼包配置模板
"""

def timer_main(excel_tool: ExcelToolsForActivities, time_open,  duration):
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    key = "timerID"
    template_timerID = 103002
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_timerID, table_data_detail=timer_main_detail)
    json_object["id"] = excel_tool.get_max_value(key="id", table_object_detail=timer_main_detail) + 1
    json_object[key] = excel_tool.get_max_value(key=key, table_object_detail=timer_main_detail) + 1
    json_object["openTime"] = time_open
    time_end = commonTools.get_time(time=time_open, days=duration, seconds=-1)
    json_object["endTime"] = time_end
    print(json_object)
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    excel_tool.add_object(key=key, value=json_object[key], table_data_detail=timer_main_detail, json_object=json_object)
    return json_object[key]


def mission_group(excel_tool: ExcelToolsForActivities, timer_id, icon_name):
    # 购买期
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    template_groupId = 3020101
    key = "groupId"
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_groupId, table_data_detail=mission_group_detail)
    json_object["id"] = excel_tool.get_max_value(key="id", table_object_detail=mission_group_detail) + 1
    json_object[key] = excel_tool.get_max_value(key=key, table_object_detail=mission_group_detail) + 1
    json_object["openArg"] = timer_id
    json_object["closeArg"] = timer_id
    json_object["iconName"] = icon_name
    print(json_object)
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    excel_tool.add_object(key=key, value=json_object[key], table_data_detail=mission_group_detail, json_object=json_object)

    # 登录领奖





def main():
    """
        读写方式：修改
        home_btn_events_time_e1001 常规
        home_btn_icon_black5       黑五
        home_btn_icon_3day         三天
    """
    time_open = "2025-04-26 00:00:00"
    duration = 3
    icon_name = "home_btn_events_time_e1001"
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = timer_main(excel_tool=excel_tool, time_open=time_open, duration=duration)
    mission_group(excel_tool=excel_tool, timer_id=timer_id, icon_name=icon_name)





if __name__ == '__main__':
    main()