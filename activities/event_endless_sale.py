from configs.pathConfig import EXCEL_PATH
from tools.commonTools import get_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities
from activities.decl.EVENT_ENDLESS_SALE import EVENT_ENDLESS_SALE

event_endless_sale_cfg = [
    {"groupId": 3010102,"autoId": 20020583, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020584, "fishBagType": 1, "fishCardCount": 100},
    {"groupId": 3010102,"autoId": 20020585, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020586, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020587, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020588, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020589, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020590, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020591, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020592, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020593, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020594, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020595, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020596, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020597, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020598, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020599, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020600, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010102,"autoId": 20020601, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020602, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010102,"autoId": 20020603, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020604, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020605, "fishBagType": 2, "fishCardCount": 100},
    {"groupId": 3010102,"autoId": 20020606, "fishBagType": 3, "fishCardCount": 100},
    {"groupId": 3010102,"autoId": 20020607, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020608, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020609, "fishBagType": 2, "fishCardCount": 100},
    {"groupId": 3010102,"autoId": 20020610, "fishBagType": 3, "fishCardCount": 100},
    {"groupId": 3010102,"autoId": 20020611, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020612, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010102,"autoId": 20020613, "fishBagType": 2, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020614, "fishBagType": 3, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020800, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020801, "fishBagType": 1, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020802, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020803, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020804, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020805, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020806, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020807, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020808, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020809, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020810, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020811, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020812, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020813, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020814, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020815, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020816, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020817, "fishBagType": 1, "fishCardCount": 200},
    {"groupId": 3010103, "autoId": 20020818, "fishBagType": 2, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020819, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 3010103, "autoId": 20020820, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020821, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020822, "fishBagType": 2, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020823, "fishBagType": 3, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020824, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020825, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020826, "fishBagType": 2, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020827, "fishBagType": 3, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020828, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020829, "fishBagType": 1, "fishCardCount": 1000},
    {"groupId": 3010103, "autoId": 20020830, "fishBagType": 2, "fishCardCount": 100},
    {"groupId": 3010103, "autoId": 20020831, "fishBagType": 3, "fishCardCount": 100},
]


def event_endless_sale(excel_tool: ExcelToolsForActivities, fishery_id, group_id):
    # 读取ITEM_MAIN表
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    print(f"----------------{event_endless_sale_detail[2]} 正在修改----------------")
    for cfg in event_endless_sale_cfg:
        if group_id != cfg["groupId"]:
            continue
        json_object, instance_object = excel_tool.get_object(key="autoId", value=cfg["autoId"], table_data_detail=event_endless_sale_detail, cls=EVENT_ENDLESS_SALE)
        print(json_to_block(json_object=json_object, name=event_endless_sale_detail[2].lower()))
        print("\n        ⬇⬇⬇⬇⬇⬇        \n")
        fish_bag_type = cfg["fishBagType"]
        fish_card_count = cfg["fishCardCount"]

        # 查鱼卡包
        instance_object.specialItem.tpId = excel_tool.get_fish_bag(fishery_id=fishery_id, fish_bag_type=fish_bag_type, fish_card_count=fish_card_count)
        table_data_object = excel_tool.get_table_data_object_by_key_value(key="itemTpId", value=instance_object.specialItem.tpId, table_data_detail=item_main_detail)
        icon_name = table_data_object["iconName"]
        instance_object.specialItemIcon = 'icon_fishbag/' + icon_name
        print(json_to_block(json_object=instance_to_json(instance_object=instance_object), name=event_endless_sale_detail[2].lower()))
        print("- - - - - - - - - - - - - - - -")
        excel_tool.change_object(key="id", value=instance_object.id, table_data_detail=event_endless_sale_detail, instance_object=instance_object)
    print(f"----------------{event_endless_sale_detail[2]} 修改完成----------------\n")

def timer_main(excel_tool: ExcelToolsForActivities, time_start, timer_id):
    time_end = get_time(time=time_start, days=6, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)


def main():
    # fishery_id = 500302
    # group_id = 3010103
    # time_start ="2025-04-18 00:00:00"

    fishery_id = 400318
    group_id = 3010102
    time_start = "2025-04-25 00:00:00"
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    event_endless_sale(excel_tool, fishery_id=fishery_id, group_id=group_id)
    timer_main(excel_tool=excel_tool, time_start=time_start, timer_id=timer_id)





if __name__ == '__main__':
    main()

