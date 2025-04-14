from configs.pathConfig import EXCEL_PATH
from tools import baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    prefix = "TIMER_MAIN"
    key = "timerID"
    json_object_list, _, _ = baseDataRead.convert_to_json(path=excel_tool.root_dir + "/activities/prepare/", prefix=prefix)
    table_data_detail = excel_tool.get_table_data_detail(book_name=f"{prefix}.xlsm")
    print(f"----------------{prefix} 正在修改----------------")
    for json_object in json_object_list:
        json_object_origin, _ = excel_tool.get_object(key=key, value=json_object[key], table_data_detail=table_data_detail)
        print(json_to_block(json_object=json_object_origin, name=prefix.lower()))
        print("\n        ⬇⬇⬇⬇⬇⬇        \n")
        print(json_to_block(json_object=json_object, name=prefix.lower()))
        print("- - - - - - - - - - - - - - - -")
        excel_tool.change_object(key=key, value=json_object[key], table_data_detail=table_data_detail, json_object=json_object)


if __name__ == '__main__':
    main()
