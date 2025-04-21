from activities.decl.DROP_ENTITY import DROP_ENTITY
from activities.decl.DROP_MAIN import DROP_MAIN
from activities.decl.DROP_PACK import DROP_PACK
from activities.decl.FISHCARD import FISHCARD
from activities.decl.FISHCARD_PACK_INFO import FISHCARD_PACK_INFO
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from common.error import DifferError
from configs.pathConfig import EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities

import re


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


def item_main(excel_tool: ExcelToolsForActivities, tpid_start, fishery_index, icon_name,  drop_id_start):
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1

    prefix = item_main_detail[2]
    template_tpid_list = [211264, 211265, 211266, 211267, 211268, 211269, 211270, 211271, 211272, 211273]
    key = "itemTpId"
    cur = 0
    while cur < len(template_tpid_list):
        template_tpid = template_tpid_list[cur]
        instance_object: ITEM_MAIN
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_tpid, table_data_detail=item_main_detail, cls=ITEM_MAIN)
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
        # excel_tool.add_object(key=key, value=instance_object.itemTpId, instance_object=instance_object, table_data_detail=item_main_detail)
        excel_tool.change_object(key=key, value=instance_object.itemTpId, instance_object=instance_object, table_data_detail=item_main_detail)
        cur += 1

def item_main_language(excel_tool: ExcelToolsForActivities, tpid_start, fishery_index, pack_info_cfg_list):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    id_start=133255
    prefix = item_main_language_detail[2]
    template_tpid_list = [211264, 211265, 211266, 211267, 211268, 211269, 211270, 211271, 211272, 211273]
    key = "tpId"
    cur = 0
    while cur < len(template_tpid_list):
        template_tpid = template_tpid_list[cur]
        instance_object: ITEM_MAIN_LANGUAGE
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_tpid, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
        instance_object.id = id_start + cur
        instance_object.tpId = tpid_start + cur
        table_data_object = excel_tool.get_table_data_object_by_key_value(key="tpId", value=500300 + fishery_index, table_data_detail=fisheries_language_detail)
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
        excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=item_main_language_detail)
        cur += 1

def drop_main(excel_tool: ExcelToolsForActivities, drop_id_start, fishery_index):
    drop_main_detail = excel_tool.get_table_data_detail(book_name="DROP_MAIN.xlsm")
    prefix = drop_main_detail[2]
    id_start = excel_tool.get_max_value(key="id", table_object_detail=drop_main_detail) + 1
    template_drop_id_start = 1010123
    key = "dropId"
    cur = 0
    while cur < 10:
        template_drop_id = template_drop_id_start + cur * 100
        instance_object: DROP_MAIN
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_drop_id, table_data_detail=drop_main_detail, cls=DROP_MAIN)
        instance_object.id = id_start + cur
        instance_object.name = f"{instance_object.name.split('-')[0]}-鱼场新主线{fishery_index}"
        instance_object.dropId = drop_id_start + cur * 100
        print(instance_object)
        # excel_tool.change_object(key=key, value=instance_object.dropId, instance_object=instance_object, table_data_detail=drop_main_detail)
        excel_tool.add_object(key=key, value=instance_object.dropId, instance_object=instance_object, table_data_detail=drop_main_detail)
        cur += 1


def drop_pack(excel_tool: ExcelToolsForActivities, drop_id_start, drop_pack_id_start, fishery_index, pack_info_cfg_list):
    drop_pack_detail = excel_tool.get_table_data_detail(book_name="DROP_PACK.xlsm")
    prefix = drop_pack_detail[2]
    # 从最大+1开始新增
    form_id_max = 0
    for json_object in drop_pack_detail[0]:
        if "formId"not in json_object:
            continue
        if form_id_max >= json_object["formId"]:
            continue
        form_id_max = json_object["formId"]
    id_start = excel_tool.get_max_value(key="id", table_object_detail=drop_pack_detail) + 1
    formId_start = form_id_max + 1
    id_start = 133711
    formId_start = 10460
    template_drop_pack_id_start = 412301
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
            instance_object.id = id_start + delta
            # 使用正则表达式定位并替换"鱼场"和"鱼卡"之间的数字
            # 执行替换
            instance_object.name = replace_number_between_keywords(content=instance_object.name, replacement=str(fishery_index), pre="场", next="鱼卡")
            instance_object.formId = formId_start + delta
            instance_object.dropPackId = drop_pack_id_start + delta_drop_pack_id
            instance_object.dropId = drop_id
            drop_turn = drop_turn_list[i]
            instance_object.dropTurnMin = drop_turn
            instance_object.dropTurnMax = instance_object.dropTurnMin
            if drop_turn == 0:
                instance_object.dropTurnMin = None
                instance_object.dropTurnMax = None
            print(instance_object)
            excel_tool.change_object(key=key, value=instance_object.dropPackId, instance_object=instance_object, table_data_detail=drop_pack_detail)
            i += 1
        j += 1

def drop_entity(excel_tool: ExcelToolsForActivities, drop_pack_id_start, entity_id_start, fishery_index, fish_card_tpid_start, pack_info_cfg_list):

    drop_entity_detail = excel_tool.get_table_data_detail(book_name="DROP_ENTITY.xlsm")
    prefix = drop_entity_detail[2]
    id_start = excel_tool.get_max_value(key="id", table_object_detail=drop_entity_detail) + 1
    id_start = 133906
    template_entity_id_start = 200901

    fish_card_fishery = 500300 + fishery_index
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fish_card_fishery)

    key = "entityId"
    json_object_origin, _ = excel_tool.get_object(key=key, value=template_entity_id_start, table_data_detail=drop_entity_detail)
    i = 0
    for pack_info_cfg in pack_info_cfg_list:
        cur = 0
        while cur < 15:
            instance_object = DROP_ENTITY()
            instance_object.id = id_start + 15 * i + cur
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
            # excel_tool.add_object(key=key, value=instance_object.entityId, instance_object=instance_object, table_data_detail=drop_entity_detail)
            excel_tool.change_object(key=key, value=instance_object.entityId, instance_object=instance_object, table_data_detail=drop_entity_detail)
            cur += 1
        i += 1


def fishcard(excel_tool: ExcelToolsForActivities, fish_card_tpid_start, fishery_index, item_main_tpid_start):
    fishcard_detail = excel_tool.get_table_data_detail(book_name="FISHCARD.xlsm")
    prefix = fishcard_detail[2]
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fishcard_detail) + 1
    template_fish_card_tpid_start = 1010001
    key = "tpId"
    fish_card_fishery = 500300 + fishery_index
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fish_card_fishery)
    cur = 0
    while cur < 15:
        instance_object: FISHCARD
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_fish_card_tpid_start + cur, table_data_detail=fishcard_detail, cls=FISHCARD)
        instance_object.id = id_start + cur
        instance_object.name = replace_number_between_keywords(content=instance_object.name, replacement=str(fishery_index), pre="新主线", next="-")
        instance_object.tpId = fish_card_tpid_start + cur
        fish_id = int(fish_id_list[cur])
        instance_object.rank = excel_tool.get_fish_type(fish_id=fish_id)
        instance_object.fishCardFishery = 500300 + fishery_index
        instance_object.fishCardFish = fish_id
        instance_object.fishCardupId = 40 + instance_object.rank
        subspecies_id = int(fish_id_list[15 + cur])
        instance_object.subspeciesId = subspecies_id
        instance_object.fishClassType = excel_tool.get_fish_type(fish_id=fish_id) + 4
        instance_object.revealPackId = item_main_tpid_start + 2
        print(instance_object)
        excel_tool.add_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fishcard_detail)
        # excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object, table_data_detail=fishcard_detail)
        cur += 1

def fishcard_pack_info(excel_tool: ExcelToolsForActivities, fishery_index, fishcard_pack_info_tpid_start, item_main_tpid_start, pack_info_cfg_list):
    fishcard_pack_info_detail = excel_tool.get_table_data_detail(book_name="FISHCARD_PACK_INFO.xlsm")
    prefix = fishcard_pack_info_detail[2]
    id_start = excel_tool.get_max_value(key="id", table_object_detail=fishcard_pack_info_detail) + 1
    id_start =131391
    template_fishcard_pack_info_tpid_start = 362
    key = "tpId"
    cur = 0
    while cur < len(pack_info_cfg_list):
        pack_info_cfg = pack_info_cfg_list[cur]
        instance_object: FISHCARD_PACK_INFO
        json_object_origin, instance_object = excel_tool.get_object(key=key, value=template_fishcard_pack_info_tpid_start + cur, table_data_detail=fishcard_pack_info_detail, cls=FISHCARD_PACK_INFO)
        instance_object.id = id_start + cur

        pattern = r'(.*新主线)\d+.*'
        match = re.match(pattern, instance_object.name)
        instance_object.name = f"{match.group(1)}{fishery_index}"

        instance_object.tpId = fishcard_pack_info_tpid_start + cur
        instance_object.packItemId = item_main_tpid_start + cur
        instance_object.smallNum = pack_info_cfg[0]
        instance_object.midiumNum = pack_info_cfg[1]
        instance_object.largeNum = pack_info_cfg[2]
        instance_object.hiddenNum = pack_info_cfg[3]
        instance_object.bossNum = pack_info_cfg[4]
        instance_object.fisheryId = 500300 + fishery_index
        if pack_info_cfg["fish_type"] > 3:
            instance_object.fisheryId = None
        print(instance_object)
        excel_tool.change_object(key=key, value=instance_object.tpId, instance_object=instance_object,  table_data_detail=fishcard_pack_info_detail)
        cur += 1

def fishcard_reward_group(excel_tool: ExcelToolsForActivities, fishery_index, item_main_tpid_start):
    fishcard_reward_group_detail = excel_tool.get_table_data_detail(book_name="FISHCARD_REWARD_GROUP.xlsm")
    prefix = fishcard_reward_group_detail[2]



def main():
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    item_main_tpid_start = 211274
    drop_id_start = 1010124
    drop_pack_id_start = 412401
    entity_id_start = 201051
    fish_card_tpid_start = 1010016
    fishcard_pack_info_tpid_start = 372
    icon_name = "S01C02"
    fishery_index = 2

    pack_info_cfg_list = [
        {"name": "10","itemCount_list": [4, 2, 3, 1, 0, 10], "dropTurn_list": [2, 2 ,1 ,1, 0], "fish_type": 0},
        {"name": "20","itemCount_list":[6, 5, 6, 2, 1, 20], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "50","itemCount_list":[15, 13, 14, 5, 3, 50], "dropTurn_list": [1, 1 ,2 ,1, 1], "fish_type": 0},
        {"name": "100","itemCount_list":[30, 26, 28, 10, 6, 100], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "200","itemCount_list":[60, 52, 56, 20, 12, 200], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "1000", "itemCount_list":[300, 260, 280, 100, 60, 1000], "dropTurn_list": [2, 1 ,1 ,1, 1], "fish_type": 0},
        {"name": "隐藏","itemCount_list":[0, 0, 0, 20, 0, 20], "dropTurn_list": [0, 0 ,0 ,1, 0], "fish_type": 4},
        {"name": "隐藏100","itemCount_list":[0, 0, 0, 100, 0, 100], "dropTurn_list": [0, 0 ,0 ,1, 0], "fish_type": 4},
        {"name": "boss","itemCount_list":[0, 0, 0, 0, 20, 20], "dropTurn_list": [0, 0 ,0 ,0, 1], "fish_type": 5},
        {"name": "boss100","itemCount_list":[0, 0, 0, 0, 100, 100],"dropTurn_list": [0, 0 ,0 ,0, 1], "fish_type": 5},
    ]

    # item_main(excel_tool=excel_tool, tpid_start=item_main_tpid_start, fishery_index=fishery_index,icon_name=icon_name,  drop_id_start= drop_id_start)
    item_main_language(excel_tool=excel_tool, tpid_start=item_main_tpid_start, fishery_index=fishery_index, pack_info_cfg_list=pack_info_cfg_list)
    # drop_main(excel_tool=excel_tool, drop_id_start=drop_id_start, fishery_index=fishery_index)
    # drop_pack(excel_tool=excel_tool, drop_id_start=drop_id_start,drop_pack_id_start=drop_pack_id_start, fishery_index=fishery_index, pack_info_cfg_list=pack_info_cfg_list)
    # drop_entity(excel_tool=excel_tool,drop_pack_id_start=drop_pack_id_start, entity_id_start=entity_id_start, fishery_index=fishery_index, fish_card_tpid_start=fish_card_tpid_start, pack_info_cfg_list=pack_info_cfg_list)
    # fishcard(excel_tool=excel_tool, fish_card_tpid_start=fish_card_tpid_start, fishery_index=fishery_index, item_main_tpid_start=item_main_tpid_start)
    # fishcard_pack_info(excel_tool=excel_tool,fishery_index=fishery_index, fishcard_pack_info_tpid_start=fishcard_pack_info_tpid_start, item_main_tpid_start=item_main_tpid_start,  pack_info_cfg_list=pack_info_cfg_list)



if __name__ == '__main__':
    main()
