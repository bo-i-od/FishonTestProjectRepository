from activities.decl.MISSION_GROUP import MISSION_GROUP
from configs.pathConfig import EXCEL_PATH
from tools import commonTools
from tools.excelRead import ExcelToolsForActivities

"""
    1+1礼包配置模板
"""

def mission_group(excel_tool: ExcelToolsForActivities, timer_id):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    event_special_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_SPECIAL_SALE.xlsm")
    event_id = excel_tool.get_max_value(key="eventId", table_object_detail=event_special_sale_detail) + 1
    key = "groupId"
    template_groupId = 3030101
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_groupId, table_data_detail=mission_group_detail)
    json_object["id"] = excel_tool.get_max_value(key="id", table_object_detail=mission_group_detail) + 1
    json_object[key] = excel_tool.get_max_value(key=key, table_object_detail=mission_group_detail) + 1
    json_object["openArg"] = timer_id
    json_object["closeArg"] = timer_id
    json_object["extArgs"][0] =event_id
    print(json_object)
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    excel_tool.add_object(key=key, value=json_object[key], table_data_detail=mission_group_detail, json_object=json_object)
    return json_object[key]


def timer_main(excel_tool: ExcelToolsForActivities, time_open,  duration):
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    key = "timerID"
    template_timerID = 103003
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_timerID, table_data_detail=timer_main_detail)
    json_object["id"] = excel_tool.get_max_value(key="id", table_object_detail=timer_main_detail) + 1
    json_object[key] = excel_tool.get_max_value(key=key, table_object_detail=timer_main_detail) + 1
    json_object["openTime"] = time_open
    time_end = commonTools.get_time(time=time_open, days=duration, seconds=-1)
    json_object["endTime"] = time_end
    print(json_object)
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    excel_tool.add_object(key=key, value=json_object[key], table_data_detail=timer_main_detail, json_object=json_object)
    return json_object[key]

def payment_gift(excel_tool: ExcelToolsForActivities, priceCount, pay_item_list, free_item_list, goodsOff):
    payment_gift_detail = excel_tool.get_table_data_detail(book_name="PAYMENT_GIFT.xlsm")
    key = "giftId"
    template_giftId = 20030009
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_giftId, table_data_detail=payment_gift_detail)
    json_object["id"] = excel_tool.get_max_value(key="id", table_object_detail=payment_gift_detail) + 1
    json_object[key] = excel_tool.get_max_value(key=key, table_object_detail=payment_gift_detail) + 1
    json_object["priceCount"] = priceCount
    json_object["goodsOff"] = goodsOff
    json_object["textId"] = json_object[key]
    cur = 0
    while cur < 6:
        # 有值的填入 没值的用{}
        if cur < len(pay_item_list):
            json_object["itemGroups"][0]["items"][cur]["ioIdType"] = pay_item_list[cur]["ioIdType"]
            json_object["itemGroups"][0]["items"][cur]["tpId"] = pay_item_list[cur]["tpId"]
            json_object["itemGroups"][0]["items"][cur]["count"] = pay_item_list[cur]["count"]
        else:
            json_object["itemGroups"][0]["items"][cur] = {}
        if cur < len(free_item_list):
            json_object["itemGroups"][1]["items"][cur]["ioIdType"] = free_item_list[cur]["ioIdType"]
            json_object["itemGroups"][1]["items"][cur]["tpId"] = free_item_list[cur]["tpId"]
            json_object["itemGroups"][1]["items"][cur]["count"] = free_item_list[cur]["count"]
        else:
            json_object["itemGroups"][1]["items"][cur] = {}
        cur += 1
    print(json_object)
    payment_gift_detail = excel_tool.get_table_data_detail(book_name="PAYMENT_GIFT.xlsm")
    excel_tool.add_object(key=key, value=json_object[key], table_data_detail=payment_gift_detail, json_object=json_object)
    return json_object[key]


def event_special_sale(excel_tool: ExcelToolsForActivities, group_id, gift_id):
    event_special_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_SPECIAL_SALE.xlsm")
    key = "eventId"
    template_eventId = 1
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_eventId, table_data_detail=event_special_sale_detail).copy()
    json_object["id"] = excel_tool.get_max_value(key="id", table_object_detail=event_special_sale_detail) + 1
    json_object[key] = excel_tool.get_max_value(key=key, table_object_detail=event_special_sale_detail) + 1
    json_object["groupId"] = group_id
    json_object["giftId"] = gift_id
    print(json_object)
    event_special_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_SPECIAL_SALE.xlsm")
    excel_tool.add_object(key=key, value=json_object[key], table_data_detail=event_special_sale_detail, json_object=json_object)




def main():
    time_open = "2025-05-09 00:00:00"
    duration = 2
    priceCount = 2880
    goodsOff = 20
    pay_item_list = [
        {"ioIdType": 17, "tpId": 1700019, "count": 1},
        {"ioIdType": 1, "tpId": 102700, "count": 10},
        {"ioIdType": 1, "tpId": 102800, "count": 50000},
        {"ioIdType": 1, "tpId": 102900, "count": 1000},
    ]

    free_item_list = [
        {"ioIdType": 17, "tpId": 1700020, "count": 1},
        {"ioIdType": 1, "tpId": 100100, "count": 2000},
        {"ioIdType": 1, "tpId": 102800, "count": 50000},
        {"ioIdType": 1, "tpId": 102900, "count": 1000},
    ]

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = timer_main(excel_tool=excel_tool, time_open=time_open, duration=duration)
    group_id = mission_group(excel_tool=excel_tool, timer_id=timer_id)
    gift_id = payment_gift(excel_tool=excel_tool, priceCount=priceCount, pay_item_list=pay_item_list, free_item_list=free_item_list, goodsOff=goodsOff)
    event_special_sale(excel_tool=excel_tool, group_id=group_id, gift_id=gift_id)


if __name__ == '__main__':
    main()
