from activities.decl.EVENT_ENDLESS_SALE_CONTAINER import EVENT_ENDLESS_SALE_CONTAINER
from configs.pathConfig import EXCEL_PATH
from tools.commonTools import get_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities
from activities.decl.EVENT_ENDLESS_SALE import EVENT_ENDLESS_SALE




def event_endless_sale(excel_tool: ExcelToolsForActivities, group_id):
    # 读取ITEM_MAIN表
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    for event_endless_sale_container_cfg in event_endless_sale_container_cfg_list:
        instance_object: EVENT_ENDLESS_SALE
        json_object, instance_object = excel_tool.get_object(key="autoId", value=event_endless_sale_container_cfg["autoId"], table_data_detail=event_endless_sale_detail, cls=EVENT_ENDLESS_SALE)
        # 查鱼卡包
        if event_endless_sale_container_cfg["convertId"] != 0:
            instance_object.specialItem.tpId = event_endless_sale_container_cfg["convertId"]
            instance_object.specialItem.ioIdType = 97
            instance_object.specialItemIcon = None
        instance_object.groupId = group_id
        excel_tool.change_object(key="id", value=instance_object.id, table_data_detail=event_endless_sale_detail, instance_object=instance_object)


def event_endless_sale_container(excel_tool: ExcelToolsForActivities, event_endless_sale_cfg_list, group_id):
    event_endless_sale_container_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE_CONTAINER.xlsm")
    prefix = event_endless_sale_container_detail[2]

    timer_id_list = []
    json_object_list, instance_object_list = excel_tool.get_object(key="groupId", value=group_id, table_data_detail=event_endless_sale_container_detail, cls=EVENT_ENDLESS_SALE_CONTAINER, is_plural=True)
    cur = 0
    while cur < len(instance_object_list):
        instance_object: EVENT_ENDLESS_SALE_CONTAINER
        instance_object = instance_object_list[cur]
        instance_object.fisheriesId = event_endless_sale_cfg_list[cur]["fishery_id"]

        print(instance_to_block(instance_object=instance_object, name=prefix.lower()))

        excel_tool.change_object(key="timerId", value=instance_object.timerId, table_data_detail=event_endless_sale_container_detail, instance_object=instance_object)
        timer_id_list.append(instance_object.timerId)
        cur += 1
    return timer_id_list



def timer_main(excel_tool: ExcelToolsForActivities, timer_id_list, event_endless_sale_cfg_list, group_id):
    container_timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    time_start = event_endless_sale_cfg_list[0]["time_start"]
    time_end = get_time(time=event_endless_sale_cfg_list[-1]["time_start"], days=7, seconds=-1)
    excel_tool.timer_main(timer_id=container_timer_id, time_start=time_start, time_end=time_end)
    cur = 0
    while cur < len(event_endless_sale_cfg_list):
        time_start = event_endless_sale_cfg_list[cur]["time_start"]
        time_end = get_time(time=event_endless_sale_cfg_list[cur]["time_start"], days=7, seconds=-1)
        excel_tool.timer_main(timer_id=timer_id_list[cur], time_start=time_start, time_end=time_end)
        cur += 1





def main():
    group_id = 3010103
    event_endless_sale_cfg_list = [
        {"time_start":  "2025-04-18 00:00:00", "fishery_id": 500302},
        {"time_start": "2025-04-25 00:00:00",  "fishery_id": 400318},

    ]

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)

    event_endless_sale(excel_tool, group_id=group_id)
    timer_id_list = event_endless_sale_container(excel_tool, event_endless_sale_cfg_list=event_endless_sale_cfg_list, group_id=group_id)
    timer_main(excel_tool=excel_tool, timer_id_list=timer_id_list, event_endless_sale_cfg_list=event_endless_sale_cfg_list, group_id=group_id)






if __name__ == '__main__':
    main()

