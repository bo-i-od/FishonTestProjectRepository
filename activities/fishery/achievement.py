from activities.decl.ACHIEVEMENT_WANTED import ACHIEVEMENT_WANTED
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from configs.pathConfig import EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities

"""
    新主线照片墙配置模板
"""


def item_main(excel_tool: ExcelToolsForActivities, fishery_id,  itemTpId_start, achievement_icon_list):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    template_itemTpId_start = 260058
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=itemTpId_start, table_data_detail=item_main_detail)
    if table_data_object_list:
        mode = 0
        template_itemTpId_start = itemTpId_start
    else:
        mode = 1
    # id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    cur = 0
    while cur < 2:
        instance_object: ITEM_MAIN
        json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId_start + cur, table_data_detail=item_main_detail, cls=ITEM_MAIN)
        instance_object.itemTpId = itemTpId_start + cur
        if mode == 1:
            instance_object.id = instance_object.itemTpId
        instance_object.name = f"鱼场{excel_tool.get_fishery_name(fishery_id=fishery_id)}-6鱼"
        if cur == 0:
            instance_object.name += "徽章"
        else:
            instance_object.name += "黄金徽章"

        instance_object.iconName = achievement_icon_list[cur]
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.itemTpId, instance_object=instance_object,  table_data_detail=item_main_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.itemTpId, instance_object=instance_object,  table_data_detail=item_main_detail)
        cur += 1

def item_main_language(excel_tool: ExcelToolsForActivities, fishery_id,  itemTpId_start, name, description, description_gold):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    template_tpId_start = 260058
    key = "tpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=itemTpId_start, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 0
        template_tpId_start = itemTpId_start
    else:
        mode = 1
    # id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    cur = 0
    while cur < 2:
        instance_object: ITEM_MAIN_LANGUAGE
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
        instance_object.tpId = itemTpId_start + cur
        if mode == 1:
            instance_object.id = instance_object.tpId
        instance_object.name = f"鱼场{excel_tool.get_fishery_name(fishery_id=fishery_id)}-6鱼"
        instance_object.t_name = name
        if cur == 0:
            instance_object.name += "徽章"
            instance_object.t_description = description
        else:
            instance_object.name += "黄金徽章"
            instance_object.t_name += "[黄金]"
            instance_object.t_description = description_gold

        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=item_main_language_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=item_main_language_detail)
        cur += 1



def achievement_wanted(excel_tool: ExcelToolsForActivities, fishery_id, itemTpId_start, achievement_icon_list):
    achievement_wanted_detail = excel_tool.get_table_data_detail(book_name="ACHIEVEMENT_WANTED.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    TPID_start = fishery_id * 100 + 1
    template_TPID_start = 50030101
    key = "TPID"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=TPID_start, table_data_detail=achievement_wanted_detail)
    if table_data_object_list:
        mode = 0
        template_TPID_start = TPID_start
    else:
        mode = 1

    monster_list = []
    pics_list = [[], []]
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)

    for fish_id in fish_id_list:
        json_object = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_id, table_data_detail=fish_detail)
        fish_class = json_object["fishClass"]
        if fish_class != 4:
            continue
        monster_list.append(fish_id)
        asset_name_split = json_object["assetName"].split("/")
        achievements_fishphoto = f"achievements_fishphoto/{asset_name_split[0]}/achv_fishphoto_{asset_name_split[1]}"
        icon_goldenlegend = f"icon_goldenlegend/{asset_name_split[1]}"
        pics_list[0].append(achievements_fishphoto)
        pics_list[1].append(icon_goldenlegend)
    order_start = excel_tool.get_max_value(key="order", table_object_detail=achievement_wanted_detail) + 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=achievement_wanted_detail) + 1
    cur = 0
    while cur < 2:
        instance_object: ACHIEVEMENT_WANTED
        json_object, instance_object = excel_tool.get_object(key=key, value=template_TPID_start + cur, table_data_detail=achievement_wanted_detail, cls=ACHIEVEMENT_WANTED)
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.order = order_start + cur
        instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}_{cur + 1}"
        instance_object.TPID = TPID_start + cur
        fishery_detail = excel_tool.get_fishery_detail(fishery_id=fishery_id, fisheries_detail=fisheries_detail)
        instance_object.achievementName = instance_object.TPID
        instance_object.icon = achievement_icon_list[cur]
        instance_object.target = monster_list
        instance_object.fishery = fishery_id
        instance_object.pics = pics_list[cur]
        instance_object.reward[2].tpId = itemTpId_start + cur
        if cur > 0:
            instance_object.unlock_achi = TPID_start
            instance_object.isGolden = 1
        else:
            instance_object.unlock = fishery_detail["needPlayerLv"]
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.TPID, instance_object=instance_object,  table_data_detail=achievement_wanted_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.TPID, instance_object=instance_object,  table_data_detail=achievement_wanted_detail)
        cur += 1



def main():
    fishery_id = 500303
    achievement_icon_list = ["achv_fishphoto_group_icon_22", "achv_fishphoto_group_icon_g22"]
    name = "地中海诗境"
    description = "蔚蓝褶皱里沉睡着千年的盐粒，古船龙骨在珊瑚间拼写楔形文字。"
    description_gold = "神话的碎片在波纹里流转，每朵浪花都盛着奥林匹斯的星屑。"
    fishery_index = fishery_id - 500300
    itemTpId_start = 260056 + fishery_index * 2
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    item_main(excel_tool=excel_tool,  fishery_id=fishery_id, itemTpId_start=itemTpId_start, achievement_icon_list=achievement_icon_list)
    item_main_language(excel_tool=excel_tool,  fishery_id=fishery_id, itemTpId_start=itemTpId_start, name=name, description=description, description_gold=description_gold)
    achievement_wanted(excel_tool=excel_tool, fishery_id=fishery_id, itemTpId_start=itemTpId_start, achievement_icon_list=achievement_icon_list)














if __name__ == '__main__':
    main()