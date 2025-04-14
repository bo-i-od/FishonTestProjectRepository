from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from tools.excelRead import ExcelToolsForActivities

golden_legend_cfg = [
    {"groupId": 2010805,"autoId": 278, "fishBagType": 1, "fishCardCount": 50},
    {"groupId": 2010805,"autoId": 284, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 2010805,"autoId": 286, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 2010807,"autoId": 294, "fishBagType": 1, "fishCardCount": 50},
    {"groupId": 2010807,"autoId": 300, "fishBagType": 3, "fishCardCount": 20},
    {"groupId": 2010807,"autoId": 302, "fishBagType": 3, "fishCardCount": 20},
]


def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, group_id:int, fishery_id: int):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    for cfg in golden_legend_cfg:
        if group_id != cfg["groupId"]:
            continue
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        json_object, instance_object = excel_tool.get_object(key="autoId", value=cfg["autoId"], table_data_detail=event_n_day_tasks_milestone_detail, cls=EVENT_N_DAY_TASKS_MILESTONE)
        fish_bag_type = cfg["fishBagType"]
        fish_card_count = cfg["fishCardCount"]
        print(instance_object)
        # 查鱼卡包
        instance_object.specialItem.tpId = excel_tool.get_fish_bag(fishery_id=fishery_id, fish_bag_type=fish_bag_type, fish_card_count=fish_card_count)
        table_data_object = excel_tool.get_table_data_object_by_key_value(key="itemTpId", value=instance_object.specialItem.tpId, table_data_detail=item_main_detail)
        icon_name = table_data_object["iconName"]
        instance_object.specialItemIcon = 'icon_fishbag/' + icon_name

        excel_tool.change_object(key="id", value=instance_object.id, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)

