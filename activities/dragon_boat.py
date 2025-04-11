from activities.decl.GLOBAL_VALUE import GLOBAL_VALUE
from activities.decl.TIMER_MAIN import TIMER_MAIN
from tools import baseDataRead
from tools.commonTools import *
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities


def global_value(excel_tool:ExcelToolsForActivities, time_start):
    timestamp_start_1 = time_to_timestamp_ms(time=time_start)
    timestamp_end_1 = timestamp_start_1 + 338400000
    timestamp_start_2 = timestamp_end_1 + 7200000
    timestamp_end_2 = timestamp_start_2 + 252000000

    # globalValueID
    dragon_boat_cfg = [
        {"globalValueID": 264, "value": f"{timestamp_start_1}"},
        {"globalValueID": 265, "value": f"{timestamp_end_1}"},
        {"globalValueID": 266, "value": f"{timestamp_start_2}"},
        {"globalValueID": 267, "value": f"{timestamp_end_2}"},
    ]

    global_value_detail = excel_tool.get_table_data_detail(book_name="GLOBAL_VALUE.xlsm")
    print(f"----------------{global_value_detail[2]} 正在修改----------------")
    for cfg in dragon_boat_cfg:
        json_object, instance_object = excel_tool.get_object(key="globalValueID", value=cfg["globalValueID"], table_data_detail=global_value_detail, cls=GLOBAL_VALUE)
        print(json_to_block(json_object=json_object, name=global_value_detail[2].lower()))
        print("\n        ⬇⬇⬇⬇⬇⬇        \n")
        instance_object.value = cfg["value"]
        print(json_to_block(json_object=instance_to_json(instance_object=instance_object), name=global_value_detail[2].lower()))
        print("- - - - - - - - - - - - - - - -")
        excel_tool.change_object(key="globalValueID", value=instance_object.globalValueID, table_data_detail=global_value_detail, instance_object=instance_object)
    print(f"----------------{global_value_detail[2]} 修改完成----------------\n")


def timer_main(excel_tool:ExcelToolsForActivities, time_start, timer_id=102030):
    time_end = get_time(time=time_start, days=7, hours=-2, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)


def main():
    excel_tool = ExcelToolsForActivities("C:/Dev/datapool/策划模板导出工具/")
    time_start = "2025-04-21 02:00:00"
    group_id = 2010111
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    global_value(excel_tool, time_start=time_start)
    timer_main(excel_tool, time_start=time_start, timer_id=timer_id)




if __name__ == '__main__':
    main()
