from activities.decl.EVENT_SPECIAL_SALE import EVENT_SPECIAL_SALE
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.PAYMENT_GIFT import PAYMENT_GIFT, PAYMENT_GIFT_ITEM_GROUP, PAYMENT_GIFT_ITEM
from activities.decl.TIMER_MAIN import TIMER_MAIN
from configs.pathConfig import EXCEL_PATH
from tools import commonTools
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    1+1礼包配置模板
"""

def mission_group(excel_tool: ExcelToolsForActivities, timer_id,title, groupId=None,eventId=None):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    event_special_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_SPECIAL_SALE.xlsm")
    if eventId is None:
        eventId = excel_tool.get_max_value(key="eventId", table_object_detail=event_special_sale_detail) + 1
    key = "groupId"
    template_groupId = 3030101
    if groupId is None:
        mode = 1
    else:
        mode = 0
        template_groupId = groupId
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_groupId, table_data_detail=mission_group_detail)
    instance_object: MISSION_GROUP
    instance_object = json_to_instance(json_object=json_object, cls=MISSION_GROUP)
    if mode == 1:
        instance_object.groupId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=mission_group_detail, start=5200102)
        instance_object.id = instance_object.groupId
    instance_object.name= title
    instance_object.openArg= timer_id
    instance_object.closeArg= timer_id
    instance_object.extArgs[0] =eventId
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    return instance_object.groupId


def timer_main(excel_tool: ExcelToolsForActivities, time_open,  duration, title, timerID=None):
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    key = "timerID"
    template_timerID = 103003
    if timerID is None:
        mode = 1
    else:
        mode = 0
        template_timerID = timerID
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_timerID, table_data_detail=timer_main_detail)
    instance_object: TIMER_MAIN
    instance_object = json_to_instance(json_object=json_object, cls=TIMER_MAIN)
    if mode == 1:
        instance_object.timerID = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=timer_main_detail, start=160047)
        instance_object.id = instance_object.timerID
    instance_object.openTime = time_open
    instance_object.name = title
    time_end = commonTools.get_time(time=time_open, days=duration, seconds=-1)
    instance_object.endTime = time_end
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    return instance_object.timerID

def payment_gift(excel_tool: ExcelToolsForActivities, priceCount, pay_item_list, free_item_list, goodsOff,title, giftId=None):
    payment_gift_detail = excel_tool.get_table_data_detail(book_name="PAYMENT_GIFT.xlsm")
    key = "giftId"
    template_giftId = 20030009
    if giftId is None:
        mode = 1
    else:
        mode = 0
        template_giftId = giftId
    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_giftId, table_data_detail=payment_gift_detail)
    instance_object: PAYMENT_GIFT
    instance_object = json_to_instance(json_object=json_object, cls=PAYMENT_GIFT)
    if mode == 1:
        instance_object.giftId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=payment_gift_detail, start=20040228)
        instance_object.id = instance_object.giftId
    instance_object.name = title
    instance_object.priceCount = priceCount
    instance_object.goodsOff = goodsOff
    instance_object.textId = instance_object.giftId
    cur = 0
    while cur < 6:
        item = instance_object.itemGroups[0].items[cur]
        # 有值的填入 没值的用{}
        if cur < len(pay_item_list):
            item.ioIdType = pay_item_list[cur]["ioIdType"]
            item.tpId = pay_item_list[cur]["tpId"]
            item.count = pay_item_list[cur]["count"]

        item = instance_object.itemGroups[1].items[cur]
        if cur < len(free_item_list):
            item.ioIdType = free_item_list[cur]["ioIdType"]
            item.tpId = free_item_list[cur]["tpId"]
            item.count = free_item_list[cur]["count"]
        cur += 1
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.giftId, table_data_detail=payment_gift_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.giftId, table_data_detail=payment_gift_detail, instance_object=instance_object)
    return instance_object.giftId


def event_special_sale(excel_tool: ExcelToolsForActivities, groupId, giftId, title):
    event_special_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_SPECIAL_SALE.xlsm")
    key = "eventId"
    template_eventId = 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="giftId", value=giftId, table_data_detail=event_special_sale_detail)
    if json_object_list:
        mode = 0
        template_eventId = json_object_list[0][key]
    else:
        mode = 1

    json_object = excel_tool.get_table_data_object_by_key_value(key=key, value=template_eventId, table_data_detail=event_special_sale_detail)
    instance_object: EVENT_SPECIAL_SALE
    instance_object = json_to_instance(json_object=json_object, cls=EVENT_SPECIAL_SALE)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=event_special_sale_detail) + 1
        instance_object.eventId = excel_tool.get_max_value(key=key, table_object_detail=event_special_sale_detail) + 1
    instance_object.name = title
    instance_object.groupId= groupId
    instance_object.giftId= giftId
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.eventId, table_data_detail=event_special_sale_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.eventId, table_data_detail=event_special_sale_detail, instance_object=instance_object)





def main():
    """
        读写方式：新增/修改
        timerID=None, groupId=None, giftId=None, eventId=None时为新增
        有值则修改对应timerID, groupId, giftId, eventId的配置
        {"ioIdType": 17, "tpId": 1700015, "count": 1},  # 力线
        {"ioIdType": 17, "tpId": 1700016, "count": 1},  # 力饵

        {"ioIdType": 17, "tpId": 1700017, "count": 1},  # 敏线
        {"ioIdType": 17, "tpId": 1700018, "count": 1},  # 敏饵

        {"ioIdType": 17, "tpId": 1700019, "count": 1},  # 智线
        {"ioIdType": 17, "tpId": 1700020, "count": 1},  # 智饵
    """

    # 配置修改区起始
    time_open = "2025-05-30 00:00:00"
    duration = 3       # 持续天数
    priceCount = 2880  # 价格
    goodsOff = 20      # 返比
    title = f"买1送1-多变套-{time_open.split(' ')[0]}"  # 标题为了发行可以知道什么时间开的什么礼包

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

    # 该区域参数为None则新增
    timerID = None  # timer_main的timerID
    groupId = None  # mission_group的groupId
    giftId = None   # payment_gift的giftId
    eventId = None  # event_special_sale的eventId

    # 配置修改区结束

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timerID = timer_main(excel_tool=excel_tool, time_open=time_open, duration=duration, title=title, timerID=timerID)
    groupId = mission_group(excel_tool=excel_tool, timer_id=timerID,title=title, groupId=groupId, eventId=eventId)
    giftId = payment_gift(excel_tool=excel_tool, priceCount=priceCount, pay_item_list=pay_item_list, free_item_list=free_item_list, goodsOff=goodsOff,title=title, giftId=giftId)
    event_special_sale(excel_tool=excel_tool, groupId=groupId, giftId=giftId, title=title)

    print("涉及到的表：", list(excel_tool.data_txt_changed))

if __name__ == '__main__':
    main()
