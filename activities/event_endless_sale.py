from activities.decl.EVENT_ENDLESS_SALE_CONTAINER import EVENT_ENDLESS_SALE_CONTAINER
from configs.pathConfig import EXCEL_PATH
from tools.commonTools import get_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities
from activities.decl.EVENT_ENDLESS_SALE import EVENT_ENDLESS_SALE




def event_endless_sale(excel_tool: ExcelToolsForActivities, event_endless_sale_container_cfg_list, event_endless_sale_cfg_list, group_id):
    # 读取ITEM_MAIN表
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    prefix = event_endless_sale_detail[2]
    print(f"----------------{prefix} 正在修改----------------")
    for event_endless_sale_container_cfg in event_endless_sale_container_cfg_list:
        instance_object: EVENT_ENDLESS_SALE
        json_object, instance_object = excel_tool.get_object(key="autoId", value=event_endless_sale_container_cfg["autoId"], table_data_detail=event_endless_sale_detail, cls=EVENT_ENDLESS_SALE)
        print(json_to_block(json_object=json_object, name=prefix.lower()))
        print("\n        ⬇⬇⬇⬇⬇⬇        \n")
        fish_bag_type = event_endless_sale_container_cfg["fishBagType"]
        fish_card_count = event_endless_sale_container_cfg["fishCardCount"]

        # 查鱼卡包
        instance_object.specialItem.tpId = excel_tool.get_fish_bag(fishery_id=event_endless_sale_cfg_list[event_endless_sale_container_cfg["index"]]["fishery_id"], fish_bag_type=fish_bag_type, fish_card_count=fish_card_count)
        table_data_object = excel_tool.get_table_data_object_by_key_value(key="itemTpId", value=instance_object.specialItem.tpId, table_data_detail=item_main_detail)
        icon_name = table_data_object["iconName"]
        instance_object.specialItemIcon = 'icon_fishbag/' + icon_name
        instance_object.groupId = group_id
        print(instance_to_block(instance_object=instance_object, name=prefix.lower()))
        print("- - - - - - - - - - - - - - - -")
        excel_tool.change_object(key="id", value=instance_object.id, table_data_detail=event_endless_sale_detail, instance_object=instance_object)
    print(f"----------------{prefix} 修改完成----------------\n")

def event_endless_sale_container(excel_tool: ExcelToolsForActivities, event_endless_sale_cfg_list, group_id):
    event_endless_sale_container_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE_CONTAINER.xlsm")
    prefix = event_endless_sale_container_detail[2]
    print(f"----------------{prefix} 正在修改----------------")
    timer_id_list = []
    json_object_list, instance_object_list = excel_tool.get_object(key="groupId", value=group_id, table_data_detail=event_endless_sale_container_detail, cls=EVENT_ENDLESS_SALE_CONTAINER, is_plural=True)
    cur = 0
    while cur < len(instance_object_list):
        json_object = json_object_list[cur]
        print(json_to_block(json_object=json_object, name=prefix.lower()))
        print("\n        ⬇⬇⬇⬇⬇⬇        \n")
        instance_object: EVENT_ENDLESS_SALE_CONTAINER
        instance_object = instance_object_list[cur]
        instance_object.fisheriesId = event_endless_sale_cfg_list[cur]["fishery_id"]

        print(instance_to_block(instance_object=instance_object, name=prefix.lower()))
        print("- - - - - - - - - - - - - - - -")

        excel_tool.change_object(key="timerId", value=instance_object.timerId, table_data_detail=event_endless_sale_container_detail, instance_object=instance_object)
        print(f"----------------{prefix} 修改完成----------------\n")
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
    event_endless_sale_container_cfg_list = [
        {"autoId": 20020583, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020584, "index": 0, "fishBagType": 1, "fishCardCount": 100},
        {"autoId": 20020585, "index": 0, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020586, "index": 0, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020587, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020588, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020589, "index": 0, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020590, "index": 0, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020591, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020592, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020593, "index": 0, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020594, "index": 0, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020595, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020596, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020597, "index": 0, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020598, "index": 0, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020599, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020600, "index": 0, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020601, "index": 0, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020602, "index": 0, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020603, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020604, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020605, "index": 0, "fishBagType": 2, "fishCardCount": 100},
        {"autoId": 20020606, "index": 0, "fishBagType": 3, "fishCardCount": 100},
        {"autoId": 20020607, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020608, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020609, "index": 0, "fishBagType": 2, "fishCardCount": 100},
        {"autoId": 20020610, "index": 0, "fishBagType": 3, "fishCardCount": 100},
        {"autoId": 20020611, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020612, "index": 0, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020613, "index": 0, "fishBagType": 2, "fishCardCount": 100},
        {"autoId": 20020614, "index": 0, "fishBagType": 3, "fishCardCount": 100},
        {"autoId": 20020800, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020801, "index": 1, "fishBagType": 1, "fishCardCount": 100},
        {"autoId": 20020802, "index": 1, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020803, "index": 1, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020804, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020805, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020806, "index": 1, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020807, "index": 1, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020808, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020809, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020810, "index": 1, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020811, "index": 1, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020812, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020813, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020814, "index": 1, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020815, "index": 1, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020816, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020817, "index": 1, "fishBagType": 1, "fishCardCount": 200},
        {"autoId": 20020818, "index": 1, "fishBagType": 2, "fishCardCount": 20},
        {"autoId": 20020819, "index": 1, "fishBagType": 3, "fishCardCount": 20},
        {"autoId": 20020820, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020821, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020822, "index": 1, "fishBagType": 2, "fishCardCount": 100},
        {"autoId": 20020823, "index": 1, "fishBagType": 3, "fishCardCount": 100},
        {"autoId": 20020824, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020825, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020826, "index": 1, "fishBagType": 2, "fishCardCount": 100},
        {"autoId": 20020827, "index": 1, "fishBagType": 3, "fishCardCount": 100},
        {"autoId": 20020828, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020829, "index": 1, "fishBagType": 1, "fishCardCount": 1000},
        {"autoId": 20020830, "index": 1, "fishBagType": 2, "fishCardCount": 100},
        {"autoId": 20020831, "index": 1, "fishBagType": 3, "fishCardCount": 100},
    ]

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)

    event_endless_sale(excel_tool,event_endless_sale_container_cfg_list=event_endless_sale_container_cfg_list, event_endless_sale_cfg_list=event_endless_sale_cfg_list, group_id=group_id)
    timer_id_list = event_endless_sale_container(excel_tool, event_endless_sale_cfg_list=event_endless_sale_cfg_list, group_id=group_id)
    timer_main(excel_tool=excel_tool, timer_id_list=timer_id_list, event_endless_sale_cfg_list=event_endless_sale_cfg_list, group_id=group_id)






if __name__ == '__main__':
    main()

