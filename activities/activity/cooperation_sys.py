from activities.decl.COOPERATION_SYS_FINAL_REWARD_WITH_TIME import COOPERATION_SYS_FINAL_REWARD_WITH_TIME
from tools.commonTools import *
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities

"""
    共建配置模板
"""

def cooperation_sys_final_reward_with_time(excel_tool: ExcelToolsForActivities, time_start, fishery_id):
    cooperation_sys_final_reward_with_time_detail = excel_tool.get_table_data_detail(book_name="COOPERATION_SYS_FINAL_REWARD_WITH_TIME.xlsm")
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    json_object_list, structs, prefix = cooperation_sys_final_reward_with_time_detail
    json_object = json_object_list[-1]
    if excel_tool.get_table_data_object_list_by_key_value(key="openTime", value=time_start, table_data_detail=cooperation_sys_final_reward_with_time_detail):
        mode = 0
    else:
        mode = 1

    # 复制最后一条
    instance_object: COOPERATION_SYS_FINAL_REWARD_WITH_TIME
    instance_object = json_to_instance(json_object=json_object, cls=COOPERATION_SYS_FINAL_REWARD_WITH_TIME)
    if mode == 1:
        instance_object.tpId = excel_tool.get_max_value(key="tpId", table_object_detail=cooperation_sys_final_reward_with_time_detail) + 1
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=cooperation_sys_final_reward_with_time_detail) + 1
    instance_object.name = f"奖励{instance_object.tpId%1000}"
    instance_object.openTime = time_start
    instance_object.fisheriesId = fishery_id
    for itemReward in instance_object.itemRewards:
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=itemReward.itemId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
        if not fish_bag:
            continue
        itemReward.itemId = fish_bag

    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key="openTime", value=instance_object.openTime, table_data_detail=cooperation_sys_final_reward_with_time_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key="openTime", value=instance_object.openTime, table_data_detail=cooperation_sys_final_reward_with_time_detail, instance_object=instance_object)


def timer_main(excel_tool: ExcelToolsForActivities, time_start, timer_id=102037):
    time_end = get_time(time=time_start, days=7, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)


def main():
    """
        读写方式：修改
        目前的大奖是渔场鱼卡1000，改大奖需要去COOPERATION_SYS_FINAL_REWARD_WITH_TIME.xlsm中改
    """

    # 配置修改区起始
    time_start = "2025-05-09 00:00:00"
    fishery_id = 500303
    group_id = 6006666

    # 配置修改区结束

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    cooperation_sys_final_reward_with_time(excel_tool=excel_tool, time_start=time_start, fishery_id=fishery_id)
    timer_main(excel_tool=excel_tool, time_start=time_start, timer_id=timer_id)

    print("涉及到的表：", list(excel_tool.data_txt_changed))



if __name__ == '__main__':
    main()
