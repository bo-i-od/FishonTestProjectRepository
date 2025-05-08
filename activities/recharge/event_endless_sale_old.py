from tools import baseDataRead
from tools.commonTools import get_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities
from activities.decl.EVENT_ENDLESS_SALE import EVENT_ENDLESS_SALE

"""
    海外蛇形礼包配置模板
"""

def event_endless_sale(excel_tool: ExcelToolsForActivities, group_id, fishery_id):
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=group_id, table_data_detail=event_endless_sale_detail)
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    for json_object in json_object_list:
        instance_object: EVENT_ENDLESS_SALE
        instance_object = json_to_instance(json_object=json_object, cls=EVENT_ENDLESS_SALE)
        fish_bag_id = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.specialItem.tpId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
        if fish_bag_id:
            instance_object.specialItem.tpId = fish_bag_id
            table_data_object = excel_tool.get_table_data_object_by_key_value(key="itemTpId", value=instance_object.specialItem.tpId, table_data_detail=item_main_detail)
            icon_name = table_data_object["iconName"]
            instance_object.specialItemIcon = 'icon_fishbag/' + icon_name
        print(instance_object)
        excel_tool.change_object(key="autoId", value=instance_object.autoId, table_data_detail=event_endless_sale_detail, instance_object=instance_object)

def timer_main(excel_tool: ExcelToolsForActivities, group_id, time_start, time_last):
    timer_id = excel_tool.get_table_data_object_by_key_value(key="groupId", value=group_id, book_name="MISSION_GROUP.xlsm")["openArg"]
    time_end = get_time(time=time_start, days=time_last, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)

def main():
    """
        读写方式：修改
        海外的无尽促销
    """
    # 配置修改区起始
    group_id = 3010102                     # 无尽促销的groupId
    fishery_id = 400302                    # 无尽促销的渔场
    time_start = "2025-04-25 00:00:00"     # 无尽促销的起始时间
    time_last = 6                          # 无尽促销的持续天数

    # 配置修改区结束
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    event_endless_sale(excel_tool=excel_tool, group_id=group_id, fishery_id=fishery_id)
    timer_main(excel_tool=excel_tool, group_id=group_id, time_start=time_start, time_last=time_last)


if __name__ == '__main__':
    main()

