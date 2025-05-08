from configs.pathConfig import EXCEL_PATH
from tools import commonTools
from tools.excelRead import ExcelToolsForActivities

"""
    集字配置模板
"""

def activity_center(excel_tool: ExcelToolsForActivities, tab_design):
    activity_center_detail = excel_tool.get_table_data_detail(book_name="ACTIVITY_CENTER.xlsm")
    key = "name"
    value = "奥运会集字"
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=value, table_data_detail=activity_center_detail)
    json_object["tabDesign"] = f"EventsHall/{tab_design}"
    print(json_object)
    excel_tool.change_object(key=key, value=value,table_data_detail=activity_center_detail, json_object=json_object)

def timer_main(excel_tool: ExcelToolsForActivities, time_open, group_id_drop):
    group_id_exchange = group_id_drop + 1
    time_id_drop = excel_tool.group_id_to_timer_id(group_id=group_id_drop)
    time_id_exchange = excel_tool.group_id_to_timer_id(group_id=group_id_exchange)
    time_end_drop = commonTools.get_time(time=time_open, days=6, seconds=-1)
    time_end_exchange = commonTools.get_time(time=time_open, days=7, seconds=-1)
    excel_tool.timer_main(timer_id=time_id_drop, time_start=time_open, time_end=time_end_drop)
    excel_tool.timer_main(timer_id=time_id_exchange, time_start=time_open, time_end=time_end_exchange)

def item_main(excel_tool: ExcelToolsForActivities, icon_prefix):
    item_id_start = 290001
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    cur = 0
    while cur < 6:
        json_object = excel_tool.get_table_data_object_by_key_value(key="itemTpId", value=item_id_start + cur, table_data_detail=item_main_detail)
        cur += 1
        json_object["iconName"] = f"{icon_prefix}{cur}"
        print(json_object)
        excel_tool.change_object(key="itemTpId", value=json_object["itemTpId"], table_data_detail=item_main_detail, json_object=json_object)




def main():
    """
        读写方式：修改
        EventsHall_tab_time_2      常规tab皮
        EventsHall_tab_events_13   周年庆tab皮

        coin_51flower_ 常规花型字前缀
        coin_51cake_   蛋糕字前缀
        coin__olympic_sticker  奥运字前缀

    """
    # 配置修改区起始
    group_id_drop = 2020001
    time_open = "2025-04-29 00:00:00"
    tab_design = "EventsHall_tab_time_2"
    icon_prefix = "coin_51flower_"

    # 配置修改区结束
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    activity_center(excel_tool=excel_tool, tab_design=tab_design)
    timer_main(excel_tool=excel_tool, time_open=time_open, group_id_drop=group_id_drop)
    item_main(excel_tool=excel_tool, icon_prefix=icon_prefix)

    print("涉及到的表：", list(excel_tool.data_txt_changed))

if __name__ == '__main__':
    main()