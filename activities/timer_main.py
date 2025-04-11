from configs.pathConfig import EXCEL_PATH
from tools import baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    json_object_list, _, _ = baseDataRead.convert_to_json(path=excel_tool.root_dir + "/activities/prepare/", prefix="TIMER_MAIN")
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    print(f"----------------{timer_main_detail[2]} 正在修改----------------")
    for json_object in json_object_list:
        json_object_origin, _ = excel_tool.get_object(key="timerID", value=json_object["timerID"], table_data_detail=timer_main_detail)
        print(json_to_block(json_object=json_object_origin, name=timer_main_detail[2].lower()))
        print("\n        ⬇⬇⬇⬇⬇⬇        \n")
        print(json_to_block(json_object=json_object, name=timer_main_detail[2].lower()))
        print("- - - - - - - - - - - - - - - -")
        excel_tool.change_object(key="timerID", value=json_object["timerID"], table_data_detail=timer_main_detail, json_object=json_object)


if __name__ == '__main__':
    main()