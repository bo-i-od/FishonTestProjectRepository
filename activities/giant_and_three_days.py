from tools.excelRead import ExcelToolsForActivities



def timer_main():
    table_data_object = excel_tool.get_table_data_object_by_key_value(key="id", value=150252, book_name="TIMER_MAIN.xlsm")
    print(table_data_object)



if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities("C:/Dev/datapool/策划模板导出工具/")
    timer_main()
    # print(table_data_detail)
    # print(table_data_object_list)
