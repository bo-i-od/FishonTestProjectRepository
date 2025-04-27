from activities.decl.DROP_ENTITY import DROP_ENTITY
from activities.decl.DROP_MAIN import DROP_MAIN
from activities.decl.DROP_PACK import DROP_PACK
from activities.decl.FISHCARD import FISHCARD
from activities.decl.FISHCARD_PACK_INFO import FISHCARD_PACK_INFO
from activities.decl.FISHCARD_REWARD_GROUP import FISHCARD_REWARD_GROUP
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.PAYMENT_GIFT import PAYMENT_GIFT
from activities.decl.PAYMENT_GIFT_GROUP import PAYMENT_GIFT_GROUP
from common.error import DifferError
from configs.pathConfig import EXCEL_PATH
from tools import baseDataRead
from tools.excelRead import ExcelToolsForActivities

import re

"""
    新主线鱼卡包配置模板
"""

def replace_excluding_keywords(text, replacement, exclude_words):
    """
    替换两个下划线之间的内容，但排除指定关键字

    :param text: 原始字符串
    :param replacement: 替换文本
    :param exclude_words: 要排除的关键字列表
    :return: 处理后的字符串
    """

    def replacer(match):
        original = match.group(1)
        return f'_{original}_' if original in exclude_words else f'_{replacement}_'

    return re.sub(r'_([^_]+)_', replacer, text)


def replace_number_between_keywords(content, replacement, pre, next):
    """
    将实例对象名称中"鱼场"和"鱼卡"之间的数字替换为指定的 fishery_index

    参数:
    instance_object: 包含 name 属性的对象
    fishery_index (int): 要替换成的数字
    """
    # 使用原始字符串 r 前缀并使用格式化后的字符串
    pattern = rf'({pre})(\d+)({next})'


    # 方法 1：使用函数作为 sub 的第二个参数
    def replacer(match):
        return match.group(1) + replacement + match.group(3)

    return re.sub(pattern, replacer, content)


def item_main(excel_tool: ExcelToolsForActivities, fishery_index, icon_name,  drop_id_start, tpid_start):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpid_start, table_data_detail=item_main_detail)
    template_tpid_start = 211264
    if table_data_object_list:
        mode = 0
        template_tpid_start = tpid_start
    else:
        mode = 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    cur = 0
    while cur < 10:
        template_tpid = template_tpid_start + cur
        instance_object: ITEM_MAIN
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_tpid, table_data_detail=item_main_detail, cls=ITEM_MAIN)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.itemTpId = tpid_start + cur
        pattern = r'(.*新主线)\d+.*'
        match = re.match(pattern, instance_object.name)
        instance_object.name = f"{match.group(1)}{fishery_index}"
        original_str = instance_object.iconName
        # 定义定位标记
        instance_object.iconName = replace_excluding_keywords(text=original_str, replacement=icon_name, exclude_words=["boss", "hiddn"])
        instance_object.useArgs[1] = drop_id_start + cur * 100
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.itemTpId, instance_object=instance_object, table_data_detail=item_main_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.itemTpId, instance_object=instance_object, table_data_detail=item_main_detail)

        cur += 1
    return tpid_start

def item_main_language(excel_tool: ExcelToolsForActivities,fishery_index, fishery_id, pack_info_cfg_list, tpid_start):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    key = "tpId"
    id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    template_tpid_start = 211264
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpid_start, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 0
        template_tpid_start = tpid_start
    else:
        mode = 1
    print(mode)
    # id_start=133255

    cur = 0
    while cur < 10:
        template_tpid = template_tpid_start + cur
        instance_object: ITEM_MAIN_LANGUAGE
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_tpid, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"{instance_object.name.split('-')[0] }-渔场新主线{fishery_index}"
        instance_object.tpId = tpid_start + cur
        table_data_object = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_language_detail)
        fishery_name = table_data_object['t_name']
        instance_object.t_name = f"{fishery_name}卡包"
        pattern = r'^.*?(鱼卡)'
        match = re.search(pattern, instance_object.t_description, re.DOTALL)
        pack_info_cfg = pack_info_cfg_list[cur]
        item_count_list = pack_info_cfg["itemCount_list"]
        description = fishery_name + "鱼卡"
        if item_count_list[0] > 0:
            description += fr"\n小体型鱼 X {item_count_list[0]}"
        if item_count_list[1] > 0:
            description += fr"\n中体型鱼 X {item_count_list[1]}"
        if item_count_list[2] > 0:
            description += fr"\n大体型鱼 X {item_count_list[2]}"
        if item_count_list[3] > 0:
            description += fr"\n特大型鱼 X {item_count_list[3]}"
        if item_count_list[4] > 0:
            description += fr"\n超巨型鱼 X {item_count_list[4]}"
        if item_count_list[0] + item_count_list[1] +item_count_list[2] + item_count_list[3] +item_count_list[4] != item_count_list[5]:
            raise DifferError("鱼卡总数和各体型鱼卡和不一致")
        instance_object.t_description = description
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=item_main_language_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=item_main_language_detail)
        cur += 1

def drop_main(excel_tool: ExcelToolsForActivities, fishery_index, drop_id_start=None):
    drop_main_detail = excel_tool.get_table_data_detail(book_name="DROP_MAIN.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=drop_main_detail) + 1
    template_drop_id_start = 1010123
    if drop_id_start is None:
        mode = 1
        drop_id_start = 1010122 + fishery_index
    else:
        mode = 0
        template_drop_id_start = drop_id_start

    key = "dropId"
    cur = 0
    while cur < 10:
        template_drop_id = template_drop_id_start + cur * 100
        instance_object: DROP_MAIN
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_drop_id, table_data_detail=drop_main_detail, cls=DROP_MAIN)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"{instance_object.name.split('-')[0]}-鱼场新主线{fishery_index}"
        instance_object.dropId = drop_id_start + cur * 100
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.dropId, instance_object=instance_object, table_data_detail=drop_main_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.dropId, instance_object=instance_object, table_data_detail=drop_main_detail)
        cur += 1
    return drop_id_start


def drop_pack(excel_tool: ExcelToolsForActivities, fishery_index, pack_info_cfg_list, drop_id_start, drop_pack_id_start=None):
    drop_pack_detail = excel_tool.get_table_data_detail(book_name="DROP_PACK.xlsm")
    template_drop_pack_id_start = 412301
    if drop_pack_id_start is None:
        drop_pack_id_start = 412201 + fishery_index * 100
        mode = 1
    else:
        mode = 0
        template_drop_pack_id_start = drop_pack_id_start
    id_start = excel_tool.get_max_value(key="id", table_object_detail=drop_pack_detail) + 1
    formId_start = excel_tool.get_max_value(key="formId", table_object_detail=drop_pack_detail) + 1
    # id_start = 133711
    # formId_start = 10460

    key = "dropPackId"
    j = 0
    while j < 10:
        drop_id = drop_id_start + j * 100
        i = 0
        drop_turn_list = pack_info_cfg_list[j]["dropTurn_list"]
        while i < 5:
            delta_drop_pack_id = j * 10000 + i
            drop_pack_id = template_drop_pack_id_start + delta_drop_pack_id
            instance_object: DROP_PACK
            json_object_origin, instance_object = excel_tool.get_object(key=key, value=drop_pack_id, table_data_detail=drop_pack_detail, cls=DROP_PACK)
            delta = j * 5 + i
            if mode == 1:
                instance_object.id = id_start + delta
                instance_object.formId = formId_start + delta
            # 使用正则表达式定位并替换"鱼场"和"鱼卡"之间的数字
            # 执行替换
            instance_object.name = replace_number_between_keywords(content=instance_object.name, replacement=str(fishery_index), pre="场", next="鱼卡")
            instance_object.dropPackId = drop_pack_id_start + delta_drop_pack_id
            instance_object.dropId = drop_id
            drop_turn = drop_turn_list[i]
            instance_object.dropTurnMin = drop_turn
            instance_object.dropTurnMax = instance_object.dropTurnMin
            if drop_turn == 0:
                instance_object.dropTurnMin = None
                instance_object.dropTurnMax = None
            print(instance_object)
            if mode == 0:
                excel_tool.change_object(key=key, value=instance_object.dropPackId, instance_object=instance_object, table_data_detail=drop_pack_detail)
            else:
                excel_tool.add_object(key=key, value=instance_object.dropPackId, instance_object=instance_object, table_data_detail=drop_pack_detail)
            i += 1
        j += 1
    return drop_pack_id_start

def drop_entity(excel_tool: ExcelToolsForActivities, drop_pack_id_start, fishery_index, fishery_id, fish_card_tpid_start, pack_info_cfg_list, entity_id_start=None):

    drop_entity_detail = excel_tool.get_table_data_detail(book_name="DROP_ENTITY.xlsm")
    key = "entityId"
    id_start = excel_tool.get_max_value(key="id", table_object_detail=drop_entity_detail) + 1
    template_entity_id_start = 200901
    if entity_id_start is None:
        mode = 1
        entity_id_start = 200751 + 150 * fishery_index
    else:
        mode = 0
        template_entity_id_start = entity_id_start
    fish_card_fishery = 500300 + fishery_index
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fish_card_fishery)
    json_object_origin, _ = excel_tool.get_object(key=key, value=template_entity_id_start, table_data_detail=drop_entity_detail)
    i = 0
    for pack_info_cfg in pack_info_cfg_list:
        cur = 0
        while cur < 15:
            instance_object = DROP_ENTITY()
            if mode == 1:
                instance_object.id = id_start + 15 * i + cur
            else:
                instance_object.id = json_object_origin["id"] + 15 * i + cur
            fish_id = int(fish_id_list[cur])
            fish_type = excel_tool.get_fish_type(fish_id=fish_id)
            instance_object.name = f"新主线鱼场{fishery_index}鱼卡包{pack_info_cfg['name']}类型{fish_type}"
            delta = 15 * i + cur
            instance_object.entityId = entity_id_start + delta
            instance_object.enabled = 1
            instance_object.dropPackId = drop_pack_id_start + i * 10000 + fish_type - 1
            instance_object.itemType = 10
            instance_object.itemID = fish_card_tpid_start + cur
            drop_turn = pack_info_cfg["dropTurn_list"][fish_type - 1]
            item_count = pack_info_cfg['itemCount_list'][fish_type - 1]
            if drop_turn == 0:
                instance_object.itemCount = 1
            else:
                instance_object.itemCount = item_count // drop_turn

            instance_object.itemCountMax = instance_object.itemCount
            instance_object.params = ["0", "0", "0"]
            instance_object.dropType = 1
            instance_object.dropValue = 1
            print(instance_object)
            if mode == 0:
                excel_tool.change_object(key=key, value=instance_object.entityId, instance_object=instance_object, table_data_detail=drop_entity_detail)
            else:
                excel_tool.add_object(key=key, value=instance_object.entityId, instance_object=instance_object, table_data_detail=drop_entity_detail)
            cur += 1
        i += 1


def fishcard(excel_tool: ExcelToolsForActivities, fish_card_tpid_start, fishery_index, fishery_id, item_main_tpid_start):
    fishcard_detail = excel_tool.get_table_data_detail(book_name="FISHCARD.xlsm")
    key = "tpId"
    template_fish_card_tpid_start = 1010001
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=fish_card_tpid_start, table_data_detail=fishcard_detail)
    if table_data_object_list:
        mode = 0
        template_fish_card_tpid_start = fish_card_tpid_start
    else:
        mode = 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fishcard_detail) + 1

    fish_card_fishery = fishery_id
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fish_card_fishery)
    cur = 0
    while cur < 15:
        instance_object: FISHCARD
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_fish_card_tpid_start + cur, table_data_detail=fishcard_detail, cls=FISHCARD)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = replace_number_between_keywords(content=instance_object.name, replacement=str(fishery_index), pre="新主线", next="-")
        instance_object.tpId = fish_card_tpid_start + cur
        fish_id = int(fish_id_list[cur])
        instance_object.rank = excel_tool.get_fish_type(fish_id=fish_id)
        instance_object.fishCardFishery = fishery_id
        instance_object.fishCardFish = fish_id
        instance_object.fishCardupId = 40 + instance_object.rank
        subspecies_id = int(fish_id_list[15 + cur])
        instance_object.subspeciesId[0] = subspecies_id
        instance_object.fishClassType = excel_tool.get_fish_class(fish_id=subspecies_id) + 4
        instance_object.revealPackId = item_main_tpid_start + 2
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fishcard_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fishcard_detail)
        cur += 1

def fishcard_pack_info(excel_tool: ExcelToolsForActivities, fishery_index,fishery_id, item_main_tpid_start, pack_info_cfg_list, fishcard_pack_info_tpid_start=None):
    fishcard_pack_info_detail = excel_tool.get_table_data_detail(book_name="FISHCARD_PACK_INFO.xlsm")
    key = "tpId"
    template_fishcard_pack_info_tpid_start = 362
    if fishcard_pack_info_tpid_start is None:
        mode = 1
        fishcard_pack_info_tpid_start = excel_tool.get_max_value(key=key, table_object_detail=fishcard_pack_info_detail) + 1
    else:
        mode = 0
        template_fishcard_pack_info_tpid_start = fishcard_pack_info_tpid_start
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fishcard_pack_info_detail) + 1

    cur = 0
    while cur < len(pack_info_cfg_list):
        pack_info_cfg = pack_info_cfg_list[cur]
        instance_object: FISHCARD_PACK_INFO
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_fishcard_pack_info_tpid_start + cur, table_data_detail=fishcard_pack_info_detail, cls=FISHCARD_PACK_INFO)
        if mode == 1:
            instance_object.id = id_start + cur

        pattern = r'(.*新主线)\d+.*'
        match = re.match(pattern, instance_object.name)
        instance_object.name = f"{match.group(1)}{fishery_index}"
        instance_object.tpId = fishcard_pack_info_tpid_start + cur
        instance_object.packItemId = item_main_tpid_start + cur
        instance_object.smallNum = pack_info_cfg["itemCount_list"][0]
        instance_object.midiumNum = pack_info_cfg["itemCount_list"][1]
        instance_object.largeNum = pack_info_cfg["itemCount_list"][2]
        instance_object.hiddenNum = pack_info_cfg["itemCount_list"][3]
        instance_object.bossNum = pack_info_cfg["itemCount_list"][4]
        instance_object.fisheryId = fishery_id
        if pack_info_cfg["fish_type"] > 3:
            instance_object.fisheryId = None
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fishcard_pack_info_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fishcard_pack_info_detail)
        cur += 1

def fishcard_reward_group(excel_tool: ExcelToolsForActivities, fishery_index, fishery_id, item_main_tpid_start,fishcard_reward_group_tpid_start=None):
    fishcard_reward_group_detail = excel_tool.get_table_data_detail(book_name="FISHCARD_REWARD_GROUP.xlsm")
    template_fishcard_reward_group_tpid_start = 211
    key = "TPID"
    if fishcard_reward_group_tpid_start is None:
        mode = 1
        fishcard_reward_group_tpid_start = excel_tool.get_max_value(key=key, table_object_detail=fishcard_reward_group_detail) + 1
    else:
        mode = 0
        template_fishcard_reward_group_tpid_start = fishcard_reward_group_tpid_start
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fishcard_reward_group_detail) + 1
    cur = 0
    while cur < 10:
        instance_object: FISHCARD_REWARD_GROUP
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_fishcard_reward_group_tpid_start + cur, table_data_detail=fishcard_reward_group_detail, cls=FISHCARD_REWARD_GROUP)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = f"{instance_object.name.split('-')[0]}-新主线-{excel_tool.get_fishery_name(fishery_id=fishery_id)}-渔场{fishery_index}"
        instance_object.TPID = fishcard_reward_group_tpid_start + cur
        instance_object.rewardGroupId = 10001 + cur
        instance_object.fisheriesId = fishery_id
        instance_object.fishcardItemId = item_main_tpid_start + cur
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.TPID, instance_object=instance_object,  table_data_detail=fishcard_reward_group_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.TPID, instance_object=instance_object,  table_data_detail=fishcard_reward_group_detail)
        cur += 1

def payment_gift_group(excel_tool: ExcelToolsForActivities, fishery_id, giftId_start, payment_gift_group_tp_id_start):
    # payment_gift
    payment_gift_detail = excel_tool.get_table_data_detail(book_name="PAYMENT_GIFT.xlsm")
    fish_bag_detail = baseDataRead.convert_to_json(path=excel_tool.root_dir + "/activities/customTables/", prefix="FISH_BAG")
    template_giftId_start = 2310023
    key = "giftId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=giftId_start, table_data_detail=payment_gift_detail)
    if table_data_object_list:
        mode = 0
        template_giftId_start = giftId_start
    else:
        mode = 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=payment_gift_detail) + 1
    cur = 0
    while cur < 4:
        instance_object: PAYMENT_GIFT
        json_object, instance_object = excel_tool.get_object(key=key, value=template_giftId_start + 100 * cur, table_data_detail=payment_gift_detail, cls=PAYMENT_GIFT)
        if mode == 1:
            instance_object.id = id_start + cur
        name_split = instance_object.name.split("-")
        instance_object.name = f"{name_split[0]}-{excel_tool.get_fishery_name(fishery_id=fishery_id)}-{name_split[2]}"
        instance_object.giftId = giftId_start + 100 * cur
        items_list = instance_object.itemGroups[0].items
        # 鱼卡包转换渔场
        for items in items_list:
            fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=items.tpId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
            if not fish_bag:
                continue
            items.tpId = fish_bag
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.giftId, instance_object=instance_object,  table_data_detail=payment_gift_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.giftId, instance_object=instance_object,  table_data_detail=payment_gift_detail)
        cur += 1

    # payment_gift_group
    payment_gift_group_detail = excel_tool.get_table_data_detail(book_name="PAYMENT_GIFT_GROUP.xlsm")
    template_tp_id_start = 100023
    key = "tp_id"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=payment_gift_group_tp_id_start, table_data_detail=payment_gift_group_detail)
    if json_object_list:
        mode = 0
        template_tp_id_start = payment_gift_group_tp_id_start
    else:
        mode = 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=payment_gift_group_detail) + 1
    cur = 0
    while cur < 4:
        instance_object: PAYMENT_GIFT_GROUP
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tp_id_start + 100000 * cur, table_data_detail=payment_gift_group_detail, cls=PAYMENT_GIFT_GROUP)
        if mode == 1:
            instance_object.id = id_start + cur
        name_split = instance_object.name.split("-")
        instance_object.name = f"{name_split[0]}-{excel_tool.get_fishery_name(fishery_id=fishery_id)}-{name_split[2]}"
        instance_object.tp_id = payment_gift_group_tp_id_start + 100000 * cur
        instance_object.giftId = giftId_start + 100 * cur
        instance_object.extra_arg = fishery_id
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tp_id, instance_object=instance_object,  table_data_detail=payment_gift_group_detail)
        else:
            excel_tool.add_object(key=key, value=instance_object.tp_id, instance_object=instance_object,  table_data_detail=payment_gift_group_detail)
        cur += 1






def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    drop_id_start = None            # 为None则新增
    drop_pack_id_start = None             # 为None则新增
    entity_id_start = None                # 为None则新增
    fishcard_pack_info_tpid_start = None  # 为None则新增
    fishcard_reward_group_tpid_start = 231         # 为None则新增

    icon_name = "S01C03"
    fishery_id = 500303

    pack_info_cfg_list = [
        {"name": "10","itemCount_list": [3, 3, 2, 2, 0, 10], "dropTurn_list": [1, 1 ,2 ,2, 0], "fish_type": 0},
        {"name": "20","itemCount_list":[6, 5, 5, 3, 1, 20], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "50","itemCount_list":[15, 13, 12, 7, 3, 50], "dropTurn_list": [1, 1 ,2 ,1, 1], "fish_type": 0},
        {"name": "100","itemCount_list":[30, 26, 24, 14, 6, 100], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "200","itemCount_list":[60, 52, 48, 28, 12, 200], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "1000", "itemCount_list":[300, 260, 240, 140, 60, 1000], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "隐藏","itemCount_list":[0, 0, 0, 20, 0, 20], "dropTurn_list": [0, 0 ,0 ,1, 0], "fish_type": 4},
        {"name": "隐藏100","itemCount_list":[0, 0, 0, 100, 0, 100], "dropTurn_list": [0, 0 ,0 ,1, 0], "fish_type": 4},
        {"name": "boss","itemCount_list":[0, 0, 0, 0, 20, 20], "dropTurn_list": [0, 0 ,0 ,0, 1], "fish_type": 5},
        {"name": "boss100","itemCount_list":[0, 0, 0, 0, 100, 100],"dropTurn_list": [0, 0 ,0 ,0, 1], "fish_type": 5},
    ]
    fishery_index = fishery_id - 500300
    giftId_start = 2310022 + fishery_index
    payment_gift_group_tp_id_start = 100022 + fishery_index
    # item_main_tpid_start = 211264 + (fishery_index-1) * 10
    # fish_card_tpid_start = 1010001 + (fishery_index-1) * 15
    # drop_id_start = drop_main(excel_tool=excel_tool, drop_id_start=drop_id_start, fishery_index=fishery_index)
    # item_main_tpid_start = item_main(excel_tool=excel_tool, tpid_start=item_main_tpid_start, fishery_index=fishery_index, icon_name=icon_name,  drop_id_start=drop_id_start)
    # item_main_language(excel_tool=excel_tool, tpid_start=item_main_tpid_start,fishery_index=fishery_index, fishery_id=fishery_id, pack_info_cfg_list=pack_info_cfg_list)
    # drop_pack_id_start = drop_pack(excel_tool=excel_tool, drop_id_start=drop_id_start,drop_pack_id_start=drop_pack_id_start, fishery_index=fishery_index, pack_info_cfg_list=pack_info_cfg_list)
    # drop_entity(excel_tool=excel_tool,drop_pack_id_start=drop_pack_id_start, entity_id_start=entity_id_start, fishery_index=fishery_index, fishery_id=fishery_id, fish_card_tpid_start=fish_card_tpid_start, pack_info_cfg_list=pack_info_cfg_list)
    # fishcard(excel_tool=excel_tool, fish_card_tpid_start=fish_card_tpid_start, fishery_index=fishery_index,fishery_id=fishery_id, item_main_tpid_start=item_main_tpid_start)
    # fishcard_pack_info(excel_tool=excel_tool, fishery_index=fishery_index, fishery_id=fishery_id, fishcard_pack_info_tpid_start=fishcard_pack_info_tpid_start, item_main_tpid_start=item_main_tpid_start,  pack_info_cfg_list=pack_info_cfg_list)
    # fishcard_reward_group(excel_tool=excel_tool, fishery_index=fishery_index, fishery_id=fishery_id, fishcard_reward_group_tpid_start=fishcard_reward_group_tpid_start, item_main_tpid_start=item_main_tpid_start)
    payment_gift_group(excel_tool=excel_tool, fishery_id=fishery_id, giftId_start=giftId_start, payment_gift_group_tp_id_start=payment_gift_group_tp_id_start)

if __name__ == '__main__':
    main()
