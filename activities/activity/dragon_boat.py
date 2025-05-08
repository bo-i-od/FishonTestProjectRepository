# -*- coding: utf-8 -*-
from activities.decl.GLOBAL_VALUE import GLOBAL_VALUE
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.decl.TIMER_MAIN import TIMER_MAIN
from configs.pathConfig import EXCEL_PATH
from tools import baseDataRead
from tools.commonTools import *
from tools.decl2py import *
from tools.excelRead import ExcelToolsForActivities
"""
    龙舟配置模板
"""

def global_value(excel_tool:ExcelToolsForActivities, time_start):
    timestamp_start_1 = time_to_timestamp_ms(time=time_start)
    timestamp_end_1 = timestamp_start_1 + 338400000
    timestamp_start_2 = timestamp_end_1 + 7200000
    timestamp_end_2 = timestamp_start_2 + 252000000

    panel_static_language(excel_tool=excel_tool, timestamp_start_1=timestamp_start_1, timestamp_end_1=timestamp_end_1, timestamp_start_2=timestamp_start_2, timestamp_end_2=timestamp_end_2)

    # globalValueID
    dragon_boat_cfg = [
        {"globalValueID": 264, "value": f"{timestamp_start_1}"},
        {"globalValueID": 265, "value": f"{timestamp_end_1}"},
        {"globalValueID": 266, "value": f"{timestamp_start_2}"},
        {"globalValueID": 267, "value": f"{timestamp_end_2}"},
    ]

    global_value_detail = excel_tool.get_table_data_detail(book_name="GLOBAL_VALUE.xlsm")

    for cfg in dragon_boat_cfg:
        instance_object: GLOBAL_VALUE
        json_object, instance_object = excel_tool.get_object(key="globalValueID", value=cfg["globalValueID"], table_data_detail=global_value_detail, cls=GLOBAL_VALUE)
        instance_object.value = cfg["value"]
        print(instance_object)
        excel_tool.change_object(key="globalValueID", value=instance_object.globalValueID, table_data_detail=global_value_detail, instance_object=instance_object)



def panel_static_language(excel_tool:ExcelToolsForActivities, timestamp_start_1, timestamp_end_1, timestamp_start_2, timestamp_end_2):
    timestamp_start_1, timestamp_end_1, timestamp_start_2, timestamp_end_2 = timestamp_start_1 + 28800000, timestamp_end_1 + 28800000, timestamp_start_2 + 28800000, timestamp_end_2 + 28800000
    time_start_1 = timestamp_ms_to_time(timestamp_start_1)
    time_end_1 = timestamp_ms_to_time(timestamp_end_1)
    time_start_2 = timestamp_ms_to_time(timestamp_start_2)
    time_end_2 = timestamp_ms_to_time(timestamp_end_2)

    dt_start_1 = datetime.strptime(time_start_1, "%Y-%m-%d %H:%M:%S")
    dt_end_1 = datetime.strptime(time_end_1, "%Y-%m-%d %H:%M:%S")
    dt_start_2 = datetime.strptime(time_start_2, "%Y-%m-%d %H:%M:%S")
    dt_end_2 = datetime.strptime(time_end_2, "%Y-%m-%d %H:%M:%S")


    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")

    template_id = 2024216
    instance_object: PANEL_STATIC_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key="templateID", value=template_id, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)

    instance_object.t_panellanguage = f"{dt_start_1.month}月{dt_start_1.day}日{dt_start_1.hour}点-{dt_end_1.month}月{dt_end_1.day}日{dt_end_1.hour}点"
    excel_tool.change_object(key="templateID", value=template_id, table_data_detail=panel_static_language_detail, instance_object=instance_object)

    template_id = 2024217
    json_object, instance_object = excel_tool.get_object(key="templateID", value=template_id, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)

    instance_object.t_panellanguage = f"{dt_start_2.month}月{dt_start_2.day}日{dt_start_2.hour}点-{dt_end_2.month}月{dt_end_2.day}日{dt_end_2.hour}点"
    excel_tool.change_object(key="templateID", value=template_id, table_data_detail=panel_static_language_detail, instance_object=instance_object)

    template_id = 2024228
    json_object, instance_object = excel_tool.get_object(key="templateID", value=template_id, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)
    instance_object.t_panellanguage = rf"\n1.活动开启时已为您的俱乐部划分好了赛区，赛区内相邻的其他俱乐部龙舟会与您同屏显示。\n\n2.活动期间内根据赛区内所有俱乐部收集的鼓力值进行排名。\n\n3.活动分为积分赛和决赛两个赛段，积分赛阶段时间：{dt_start_1.month}月{dt_start_1.day}日{dt_start_1.hour}点-{dt_end_1.month}月{dt_end_1.day}日{dt_end_1.hour}点，决赛阶段时间：{dt_start_2.month}月{dt_start_2.day}日{dt_start_2.hour}点-{dt_end_2.month}月{dt_end_2.day}日{dt_end_2.hour}点。\n\n4.积分阶段结束后会进入2个小时结算时间，结算过程中无法进入活动，结算后根据各俱乐部在积分赛阶段的排名进行巅峰组决赛或荣誉组决赛的角逐。\n\n5.活动进行中不能解散俱乐部，也不能请离玩家。\n\n6.活动进行中可以主动退出俱乐部，但退出视为放弃本轮活动，保留原俱乐部中的积分贡献且之后无论是新加入其他俱乐部或回到原俱乐部都无法再进入活动，也不能再贡献积分。\n\n<color=#FC2020>7.*决赛阶段前新进入俱乐部的玩家或新创建的俱乐部可以参与活动，也可以领取活动奖励。决赛阶段后新进入俱乐部的玩家或新创建的俱乐部无法参与活动。</color>"
    print(instance_object)
    excel_tool.change_object(key="templateID", value=template_id, table_data_detail=panel_static_language_detail, instance_object=instance_object)


def timer_main(excel_tool:ExcelToolsForActivities, time_start, timer_id=102030):
    time_end = get_time(time=time_start, days=7, hours=-2, seconds=-1)
    excel_tool.timer_main(timer_id=timer_id, time_start=time_start, time_end=time_end)


def main():
    """
        读写方式：修改
    """
    # 配置修改区起始
    time_start = "2025-05-26 02:00:00"
    group_id = 2010111

    # 配置修改区结束

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    timer_id = excel_tool.group_id_to_timer_id(group_id=group_id)
    global_value(excel_tool, time_start=time_start)
    timer_main(excel_tool, time_start=time_start, timer_id=timer_id)

    print("涉及到的表：", list(excel_tool.data_txt_changed))


if __name__ == '__main__':
    main()
