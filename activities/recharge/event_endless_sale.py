import sys

from activities.decl.EVENT_ENDLESS_SALE_CONTAINER import EVENT_ENDLESS_SALE_CONTAINER
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.TIMER_MAIN import TIMER_MAIN
from tools.commonTools import get_time, time_to_timestamp_ms, timestamp_ms_to_time
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities
from activities.decl.EVENT_ENDLESS_SALE import EVENT_ENDLESS_SALE

def mission_group(excel_tool: ExcelToolsForActivities, group_id, event_endless_sale_cfg_list):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    event_endless_sale_container_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE_CONTAINER.xlsm")
    key = "groupId"
    template_groupId = 3010103
    if group_id is None:
        mode = 1
        group_id = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=mission_group_detail, start=template_groupId)
        timer_id, timer_id_list = timer_main(excel_tool=excel_tool, event_endless_sale_cfg_list=event_endless_sale_cfg_list)
    else:
        mode = 0
        template_groupId = group_id
        timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
        timer_id_list = []
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=group_id, table_data_detail=event_endless_sale_container_detail)
        for json_object in json_object_list:
            timer_id_list.append(json_object["timerId"])
        timer_id, timer_id_list = timer_main(excel_tool=excel_tool, event_endless_sale_cfg_list=event_endless_sale_cfg_list, timer_id=timer_id, timer_id_list=timer_id_list)
    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    instance_object.groupId = group_id
    instance_object.id = instance_object.groupId
    instance_object.openArg = timer_id
    instance_object.closeArg = timer_id
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    return instance_object.groupId, timer_id_list



def event_endless_sale(excel_tool: ExcelToolsForActivities, group_id):
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    key = "autoId"
    template_groupId = 3010103

    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=group_id, table_data_detail=event_endless_sale_detail)
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=event_endless_sale_detail)
    autoId_start = excel_tool.get_min_value_more_than_start(key="autoId", table_object_detail=event_endless_sale_detail, start=json_object_list[0]["autoId"], long=len(json_object_list))
    id_start = excel_tool.get_max_value(key="id", table_object_detail=event_endless_sale_detail) + 1
    cur = 0
    while cur < len(json_object_list):
        instance_object: EVENT_ENDLESS_SALE
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=EVENT_ENDLESS_SALE)
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.autoId = autoId_start + cur
        instance_object.groupId = group_id
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_endless_sale_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_endless_sale_detail, instance_object=instance_object)
        cur += 1




def event_endless_sale_container(excel_tool: ExcelToolsForActivities, event_endless_sale_cfg_list, group_id, timer_id_list):
    def event_endless_sale_container_add():
        tpId_start = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=event_endless_sale_container_detail, start=1, long=len(timer_id_list))
        cur = 0
        while cur < len(timer_id_list):
            instance_object = EVENT_ENDLESS_SALE_CONTAINER()
            instance_object.tpId = tpId_start + cur
            instance_object.id = instance_object.tpId
            instance_object.name = f"无尽礼包{group_id}-{cur + 1}期"
            instance_object.timerId = timer_id_list[cur]
            instance_object.fisheriesId = event_endless_sale_cfg_list[cur]["fishery_id"]
            instance_object.iconName = event_endless_sale_cfg_list[cur]["iconName"]
            instance_object.panelName = event_endless_sale_cfg_list[cur]["panelName"]
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=event_endless_sale_container_detail, instance_object=instance_object)
            cur += 1

    def event_endless_sale_container_change():
        cur = 0
        while True:
            if cur >= len(instance_object_list):
                break
            instance_object: EVENT_ENDLESS_SALE_CONTAINER
            instance_object = instance_object_list[cur]
            if cur >= len(event_endless_sale_cfg_list):
                cur += 1
                continue
            instance_object.fisheriesId = event_endless_sale_cfg_list[cur]["fishery_id"]
            instance_object.iconName = event_endless_sale_cfg_list[cur]["iconName"]
            instance_object.panelName = event_endless_sale_cfg_list[cur]["panelName"]
            print(instance_object)
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=event_endless_sale_container_detail, instance_object=instance_object)
            cur += 1
    key = "tpId"
    event_endless_sale_container_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE_CONTAINER.xlsm")
    json_object_list, instance_object_list = excel_tool.get_object(key="groupId", value=group_id, table_data_detail=event_endless_sale_container_detail, cls=EVENT_ENDLESS_SALE_CONTAINER, is_plural=True)
    if instance_object_list:
        event_endless_sale_container_change()
    else:
        event_endless_sale_container_add()


def timer_main(excel_tool: ExcelToolsForActivities, event_endless_sale_cfg_list, timer_id=None, timer_id_list=None):
    def get_time_start_and_time_end():
        time_min = sys.maxsize
        time_max = 0
        for event_endless_sale_cfg in event_endless_sale_cfg_list:
            t = time_to_timestamp_ms(event_endless_sale_cfg["time_start"])
            if t > time_max:
                time_max = t
            if t < time_min:
                time_min = t
        return timestamp_ms_to_time(time_min), get_time(time=timestamp_ms_to_time(time_max), days=7, seconds=-1)

    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    time_start, time_end = get_time_start_and_time_end()
    key = "timerID"
    template_timerID = 150253
    if timer_id is None:
        mode = 1
        timer_id = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=timer_main_detail, start=template_timerID)
    else:
        mode = 0
        template_timerID = timer_id
    instance_object: TIMER_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_timerID, table_data_detail=timer_main_detail, cls=TIMER_MAIN)
    instance_object.timerID = timer_id
    instance_object.id = instance_object.timerID
    instance_object.name = f"无尽促销{event_endless_sale_cfg_list[0]['time_start'].split(' ')[0]}"
    instance_object.timerName = instance_object.name
    instance_object.cycleType = 1
    instance_object.openTime = time_start
    instance_object.endTime = time_end
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)

    # event_endless_sale_container对应的timerId配置
    if timer_id_list is None:
        mode = 1
        timer_id_list = []
    else:
        mode = 0

    def timer_main_add():
        instance_obj = TIMER_MAIN()
        instance_obj.timerID = timerID_start + cur
        instance_obj.id = instance_obj.timerID
        instance_obj.name = f"无尽促销活动-渔场{cur + 1}活动时间"
        instance_obj.timerName = instance_obj.name
        instance_obj.cycleType = 1
        instance_obj.openTime = time_start
        instance_obj.endTime = time_end
        excel_tool.add_object(key=key, value=instance_obj.timerID, table_data_detail=timer_main_detail, instance_object=instance_obj)
        timer_id_list.append(instance_obj.timerID)


    def timer_main_change():
        instance_obj: TIMER_MAIN
        json_obj, instance_obj = excel_tool.get_object(key=key, value=timer_id_list[cur], table_data_detail=timer_main_detail, cls=TIMER_MAIN)
        instance_obj.name = f"无尽促销活动-渔场{cur + 1}活动时间"
        instance_obj.timerName = instance_obj.name
        instance_obj.cycleType = 1
        instance_obj.openTime = time_start
        instance_obj.endTime = time_end
        excel_tool.change_object(key=key, value=instance_obj.timerID, table_data_detail=timer_main_detail, instance_object=instance_obj)


    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    timerID_start = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=timer_main_detail, start=instance_object.timerID, long=len(event_endless_sale_cfg_list))
    cur = 0
    while cur < len(event_endless_sale_cfg_list):
        time_start = event_endless_sale_cfg_list[cur]["time_start"]
        time_end = get_time(time=event_endless_sale_cfg_list[cur]["time_start"], days=7, seconds=-1)
        if mode == 1:
            timer_main_add()
        else:
            timer_main_change()
        cur += 1
    while cur < len(timer_id_list):
        time_start = "2025-01-01 00:00:00"
        time_end = "2025-01-06 23:59:59"
        timer_main_change()
        # 修改大timer的开始时间
        instance_object.openTime = time_start
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
        cur += 1
    return timer_id, timer_id_list


def main():
    """
        读写方式：新增/修改
        当 group_id=None 时为新增
        否则改对应 group_id 的活动数据
        常规   home_btn_icon_events_endless_com, RechargeEndlessAddOnPanel
        新年   home_btn_icon_events_endless_newyear, RechargeEndlessNewYearPanel
        感恩节 home_btn_icon_events_endless_thanksgiving, RechargeEndlessThanksPanel

    """

    # 配置修改区起始
    event_endless_sale_cfg_list = [
        {"time_start": "2025-04-18 00:00:00", "fishery_id": 500302, "iconName": "home_btn_icon_events_endless_com", "panelName":"RechargeEndlessAddOnPanel"},
        {"time_start": "2025-04-25 00:00:00",  "fishery_id": 400318, "iconName": "home_btn_icon_events_endless_com", "panelName":"RechargeEndlessAddOnPanel"},
        {"time_start": "2025-05-02 00:00:00", "fishery_id": 400319, "iconName": "home_btn_icon_events_endless_com", "panelName":"RechargeEndlessAddOnPanel"},
    ]

    # 该区域参数为None则新增
    group_id = 3010103

    # 配置修改区结束

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    group_id, timer_id_list = mission_group(excel_tool=excel_tool, group_id=group_id, event_endless_sale_cfg_list=event_endless_sale_cfg_list)
    event_endless_sale(excel_tool=excel_tool, group_id=group_id)
    event_endless_sale_container(excel_tool=excel_tool, event_endless_sale_cfg_list=event_endless_sale_cfg_list, group_id=group_id, timer_id_list=timer_id_list)

    print("涉及到的表：", list(excel_tool.data_txt_changed))




if __name__ == '__main__':
    main()

