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
    for json_object in json_object_list:
        json_object_origin, _ = excel_tool.get_object(key=key, value=json_object[key], table_data_detail=table_data_detail)
        print(json_object)
        excel_tool.change_object(key=key, value=json_object[key], table_data_detail=table_data_detail, json_object=json_object)

    print("涉及到的表：", list(excel_tool.data_txt_changed))


if __name__ == '__main__':
    main()
