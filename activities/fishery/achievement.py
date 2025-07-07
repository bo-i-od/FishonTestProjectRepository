from activities.decl.ACHIEVEMENT_GROUP_REWARDS_LANGUAGE import ACHIEVEMENT_GROUP_REWARDS_LANGUAGE
from activities.decl.ACHIEVEMENT_WANTED import ACHIEVEMENT_WANTED
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.fishery.load_tools import get_cfg_achievement
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    新主线照片墙配置模板
"""


def item_main(excel_tool: ExcelToolsForActivities, fishery_id,  itemTpId_start, achievement_icon_list):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    template_itemTpId_start = 260058
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=itemTpId_start, table_data_detail=item_main_detail)
    if table_data_object_list:
        mode = 2
        template_itemTpId_start = itemTpId_start
    else:
        mode = 1
    # id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    cur = 0
    while cur < 2:
        instance_object: ITEM_MAIN
        json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId_start + cur, table_data_detail=item_main_detail, cls=ITEM_MAIN)
        instance_object.itemTpId = itemTpId_start + cur
        instance_object.id = instance_object.itemTpId
        instance_object.name = f"鱼场{excel_tool.get_fishery_name(fishery_id=fishery_id)}-6鱼"
        if cur == 0:
            instance_object.name += "徽章"
        else:
            instance_object.name += "黄金徽章"

        instance_object.iconName = achievement_icon_list[cur]
        print(instance_object)
        if mode == 2:
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
        mode = 2
        template_tpId_start = itemTpId_start
    else:
        mode = 1
    # id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    cur = 0
    while cur < 2:
        instance_object: ITEM_MAIN_LANGUAGE
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
        instance_object.tpId = itemTpId_start + cur
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
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=item_main_language_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=item_main_language_detail)
        cur += 1



def achievement_wanted(excel_tool: ExcelToolsForActivities, fishery_id, itemTpId_start, achievement_icon_list, order):
    achievement_wanted_detail = excel_tool.get_table_data_detail(book_name="ACHIEVEMENT_WANTED.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    TPID_start = fishery_id * 100 + 1
    template_TPID_start = 50030101
    key = "TPID"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=TPID_start, table_data_detail=achievement_wanted_detail)
    if table_data_object_list:
        mode = 2
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
    order_list = []
    cur = 0
    while cur < 2:
        instance_object: ACHIEVEMENT_WANTED
        json_object, instance_object = excel_tool.get_object(key=key, value=template_TPID_start + cur, table_data_detail=achievement_wanted_detail, cls=ACHIEVEMENT_WANTED)
        if mode == 1:
            instance_object.order = order_start + cur
        order_list.append(instance_object.order)
        instance_object.name = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}_{cur + 1}"
        instance_object.TPID = TPID_start + cur
        instance_object.id = instance_object.TPID
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
            instance_object.unlock = 6
        print(instance_object)
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.TPID, instance_object=instance_object,  table_data_detail=achievement_wanted_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.TPID, instance_object=instance_object,  table_data_detail=achievement_wanted_detail)
        cur += 1

    # 将成就移到指定序号处
    if order_list[0] > order:
        change_order(excel_tool=excel_tool, order_old=order_list[0], order_new=order)
        change_order(excel_tool=excel_tool, order_old=order_list[1], order_new=order + 1)
    else:
        change_order(excel_tool=excel_tool, order_old=order_list[1], order_new=order + 1)
        change_order(excel_tool=excel_tool, order_old=order_list[0], order_new=order)



def achievement_group_rewards_language(excel_tool: ExcelToolsForActivities, fishery_id,  name):
    achievement_group_rewards_language_detail = excel_tool.get_table_data_detail(book_name="ACHIEVEMENT_GROUP_REWARDS_LANGUAGE.xlsm")
    achievementGroupId = fishery_id * 100 + 1
    key = "achievementGroupId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=achievementGroupId, table_data_detail=achievement_group_rewards_language_detail)
    if table_data_object_list:
        mode = 2
        instance_object = json_to_instance(json_object=table_data_object_list[0], cls=ACHIEVEMENT_GROUP_REWARDS_LANGUAGE)
    else:
        mode = 1
        instance_object = ACHIEVEMENT_GROUP_REWARDS_LANGUAGE()

    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    instance_object.name = f"成就{fishery_name}6鱼"
    instance_object.achievementGroupId = achievementGroupId
    instance_object.id= instance_object.achievementGroupId
    instance_object.title = name
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.achievementGroupId, instance_object=instance_object, table_data_detail=achievement_group_rewards_language_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.achievementGroupId, instance_object=instance_object, table_data_detail=achievement_group_rewards_language_detail)

    achievement_group_rewards_language_detail = excel_tool.get_table_data_detail(book_name="ACHIEVEMENT_GROUP_REWARDS_LANGUAGE.xlsm")
    achievementGroupId_gold = achievementGroupId + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=achievementGroupId_gold, table_data_detail=achievement_group_rewards_language_detail)
    if table_data_object_list:
        mode = 2
        instance_object = json_to_instance(json_object=table_data_object_list[0], cls=ACHIEVEMENT_GROUP_REWARDS_LANGUAGE)
    else:
        mode = 1
        instance_object = ACHIEVEMENT_GROUP_REWARDS_LANGUAGE()

    fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
    instance_object.name = f"成就{fishery_name}6鱼黄金"
    instance_object.achievementGroupId = achievementGroupId_gold
    instance_object.id = instance_object.achievementGroupId
    instance_object.title = name + "[黄金]"
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.achievementGroupId, instance_object=instance_object, table_data_detail=achievement_group_rewards_language_detail)
    else:
        excel_tool.add_object(key=key, value=instance_object.achievementGroupId, instance_object=instance_object, table_data_detail=achievement_group_rewards_language_detail)



def change_order(excel_tool: ExcelToolsForActivities, order_old, order_new):
    """
        将order_old和order_old+1处的成就顺序移动到order_new和order_new+1处
        大于order_new的序号依次+2
    """
    def change_order_ascending():
        instance_object_target = ACHIEVEMENT_WANTED()
        cur = 0
        while cur < len(json_object_list):
            instance_object: ACHIEVEMENT_WANTED
            instance_object = json_to_instance(json_object=json_object_list[cur], cls=ACHIEVEMENT_WANTED)
            if instance_object.order is None:
                cur += 1
                continue
            if instance_object.order < order_new:
                cur += 1
                continue
            if instance_object.order > order_old:
                cur += 1
                continue
            if instance_object.order == order_old:
                instance_object_target = instance_object
            instance_object.order += 1
            print(instance_object)
            excel_tool.change_object(key="TPID", value=instance_object.TPID, table_data_detail=achievement_wanted_detail, instance_object=instance_object)
            cur += 1
        instance_object_target.order = order_new
        print(instance_object_target)
        excel_tool.change_object(key="TPID", value=instance_object_target.TPID, table_data_detail=achievement_wanted_detail, instance_object=instance_object_target)

    def change_order_descending():
        instance_object_target = ACHIEVEMENT_WANTED()
        cur = 0
        while cur < len(json_object_list):
            instance_object: ACHIEVEMENT_WANTED
            instance_object = json_to_instance(json_object=json_object_list[cur], cls=ACHIEVEMENT_WANTED)
            if instance_object.order is None:
                cur += 1
                continue
            if instance_object.order > order_new:
                cur += 1
                continue
            if instance_object.order < order_old:
                cur += 1
                continue
            if instance_object.order == order_old:
                instance_object_target = instance_object
            instance_object.order -= 1
            print(instance_object)
            excel_tool.change_object(key="TPID", value=instance_object.TPID, table_data_detail=achievement_wanted_detail, instance_object=instance_object)
            cur += 1
        instance_object_target.order = order_new
        print(instance_object_target)
        excel_tool.change_object(key="TPID", value=instance_object_target.TPID, table_data_detail=achievement_wanted_detail, instance_object=instance_object_target)

    achievement_wanted_detail = excel_tool.get_table_data_detail(book_name="ACHIEVEMENT_WANTED.xlsm")
    json_object_list = achievement_wanted_detail[0]
    if order_old > order_new:
        change_order_ascending()
    if order_old < order_new:
        change_order_descending()


def main(excel_tool: ExcelToolsForActivities):
    """
        读写方式：新增/修改
        该渔场没出现过就是新增
        出现过就是修改
    """
    # 配置修改区起始
    cfg = get_cfg_achievement()
    print("cfg:", cfg)
    fishery_id = cfg["fishery_id"]
    achievement_icon_list = cfg["achievement_icon_list"]
    name = cfg["name"]
    description = cfg["description"]
    description_gold = cfg["description_gold"]
    order = cfg["order"]  # 一般填奇数 控制显示顺序，该序号后的会依次+2

    # 根据偏移算中间值，当渔场id不按顺序新增时可能有问题
    fishery_index = fishery_id - 500300
    itemTpId_start = 260056 + fishery_index * 2

    # 配置修改区结束
    item_main(excel_tool=excel_tool,  fishery_id=fishery_id, itemTpId_start=itemTpId_start, achievement_icon_list=achievement_icon_list)
    item_main_language(excel_tool=excel_tool,  fishery_id=fishery_id, itemTpId_start=itemTpId_start, name=name, description=description, description_gold=description_gold)
    achievement_wanted(excel_tool=excel_tool, fishery_id=fishery_id, itemTpId_start=itemTpId_start, achievement_icon_list=achievement_icon_list, order=order)
    achievement_group_rewards_language(excel_tool=excel_tool,  fishery_id=fishery_id, name=name)

    print("涉及到的表：", list(excel_tool.data_txt_changed))


if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool)
