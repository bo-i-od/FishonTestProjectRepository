from activities.decl.COOPERATION_SYS_FINAL_REWARD_WITH_TIME import COOPERATION_SYS_FINAL_REWARD_WITH_TIME
from activities.decl.TIMER_MAIN import TIMER_MAIN
from configs.pathConfig import EXCEL_PATH
from tools import baseDataRead
from tools.commonTools import *
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities

def cooperation_sys_final_reward_with_time(excel_tool: ExcelToolsForActivities, time_start, fishery_id):
    table_data_detail = excel_tool.get_table_data_detail(book_name="COOPERATION_SYS_FINAL_REWARD_WITH_TIME.xlsm")
    table_data_object_list, structs, prefix = table_data_detail
    json_object = table_data_object_list[-1]

    # 复制最后一条
    instance_object: COOPERATION_SYS_FINAL_REWARD_WITH_TIME
    instance_object = json_to_instance(json_object=json_object, cls=COOPERATION_SYS_FINAL_REWARD_WITH_TIME)
    instance_object.tpId = instance_object.tpId + 1
    instance_object.id = instance_object.tpId
    instance_object.openTime = time_start
    instance_object.fisheriesId = fishery_id
    print(f"----------------{prefix} 正在新增----------------")
    print(instance_to_block(instance_object=instance_object, name=prefix.lower()))
    print("- - - - - - - - - - - - - - - -")
    res = excel_tool.add_object(key="openTime", value=instance_object.openTime, table_data_detail=table_data_detail, instance_object=instance_object)

    if res:
        print(f"----------------{prefix} 新增完成----------------\n")
    else:
        print(f"----------------{prefix} 新增终止----------------\n")

def timer_main(excel_tool: ExcelToolsForActivities, time_start, timer_id=102037):
    time_end = get_time(time=time_start, days=7, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)


def main():
    time_start = "2025-04-18 00:00:00"
    group_id = 6006666
    fishery_id = 500302
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    cooperation_sys_final_reward_with_time(excel_tool=excel_tool, time_start=time_start, fishery_id=fishery_id)
    timer_main(excel_tool=excel_tool, time_start=time_start, timer_id=timer_id)



if __name__ == '__main__':
    main()