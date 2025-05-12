from activities.decl.COLLECTION_BASE import COLLECTION_BASE
from activities.decl.COLLECTION_CHAPTER import COLLECTION_CHAPTER
from activities.decl.COLLECTION_ENERGY_COST_DEBUFF import COLLECTION_ENERGY_COST_DEBUFF
from activities.decl.COLLECTION_EXCHANGE_STORE import COLLECTION_EXCHANGE_STORE
from activities.decl.COLLECTION_PROTECT import COLLECTION_PROTECT
from activities.decl.COLLECTION_REWARD import COLLECTION_REWARD
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.decl.TIMER_MAIN import TIMER_MAIN
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    新主线闪卡配置模板
"""

def collection_base(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index, collectionChapterId):
    cfg = {
        1:{"collectionLevel":1, "energyDropRate": 9, "totalEnergyCostByDiffCardNum": [0, 31250, 62500, 93750, 125000, 135000]},
        2: {"collectionLevel":1,"energyDropRate": 10, "totalEnergyCostByDiffCardNum": [1500, 16125, 30750, 45375, 60000, 70000]},
        3: {"collectionLevel":1,"energyDropRate": 6, "totalEnergyCostByDiffCardNum": [3000, 23500, 44000, 64500, 85000, 95000]},
        4: {"collectionLevel":1,"energyDropRate": 13, "totalEnergyCostByDiffCardNum": [5000, 26250,47500,68750,90000,100000]},
        5: {"collectionLevel":1,"energyDropRate": 8, "totalEnergyCostByDiffCardNum": [11000, 35750,60500,85250,110000,120000 ]},
        6: {"collectionLevel":2,"energyDropRate": 20, "totalEnergyCostByDiffCardNum": [8000, 27781,47562,67343,87125,97125]},
        7: {"collectionLevel":2,"energyDropRate": 40, "totalEnergyCostByDiffCardNum": [14000, 35500,57000,78500,100000,110000]},
        8: {"collectionLevel":3,"energyDropRate": 70, "totalEnergyCostByDiffCardNum": [20000, 40000, 60000, 80000, 100000, 110000]},
    }
    collection_base_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_BASE.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    template_collectionId_start = 1310001
    collectionId_start = 1310001 + fishery_index * 100
    key = "collectionId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=collectionId_start, table_data_detail=collection_base_detail)
    if json_object_list:
        mode = 0
        template_collectionId_start = collectionId_start
    else:
        mode = 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_base_detail) + 1
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id, fisheries_detail=fisheries_detail)

    # 将鱼按照fish_class进行排序
    cur = 15
    while cur < len(fish_id_list) - 1:
        i = cur
        while i < len(fish_id_list) - 1:
            if excel_tool.get_fish_class(fish_id=fish_id_list[i], fish_detail=fish_detail) > excel_tool.get_fish_class(fish_id=fish_id_list[i + 1], fish_detail=fish_detail):
                fish_id_list[i] = fish_id_list[i] ^ fish_id_list[i + 1]
                fish_id_list[i + 1] = fish_id_list[i] ^ fish_id_list[i + 1]
                fish_id_list[i] = fish_id_list[i] ^ fish_id_list[i + 1]
            i += 1
        cur += 1
    cur = 0
    while cur < 30:
        fish_id = fish_id_list[cur]
        instance_object: COLLECTION_BASE
        json_object, instance_object = excel_tool.get_object(key=key, value=template_collectionId_start + cur, table_data_detail=collection_base_detail, cls=COLLECTION_BASE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.name = cur + 1
        instance_object.collectionId = collectionId_start + cur
        instance_object.fishId = fish_id_list[cur]
        instance_object.fishSceneTpId = fishery_id
        instance_object.orderId = cur + 1
        instance_object.resourceName = "icon_flashcard_" + excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_id, table_data_detail=fish_detail)["assetName"].split("/")[-1]
        fish_class = excel_tool.get_fish_class(fish_id=fish_id, fish_detail=fish_detail)
        fish_type = excel_tool.get_fish_type(fish_id=fish_id, fish_detail=fish_detail)
        if fish_class == 1:
            fish_kind = fish_type
        else:
            fish_kind = fish_class + 4
        instance_object.collectionLevel = cfg[fish_kind]["collectionLevel"]
        instance_object.energyDropRate[2].dropRate = cfg[fish_kind]["energyDropRate"]
        instance_object.totalEnergyCostByDiffCardNum = cfg[fish_kind]["totalEnergyCostByDiffCardNum"]
        instance_object.collectionSeasonId = 2
        instance_object.collectionChapterId = collectionChapterId
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.collectionId, table_data_detail=collection_base_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.collectionId, table_data_detail=collection_base_detail, instance_object=instance_object)
        cur += 1

def timer_main(excel_tool: ExcelToolsForActivities,fishery_index, time_start, timerID=None):
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    instance_object: TIMER_MAIN
    key = "timerID"
    if timerID is None:
        mode = 1
        instance_object = TIMER_MAIN()
        instance_object.timerID = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=timer_main_detail, start=151100)
        instance_object.id = instance_object.timerID
    else:
        mode = 0
        json_object, instance_object = excel_tool.get_object(key=key, value=timerID, table_data_detail=timer_main_detail, cls=TIMER_MAIN)
    instance_object.name = f"闪卡新主线-渔场{fishery_index}"
    instance_object.timerName = instance_object.name
    instance_object.cycleType = 1
    instance_object.openTime = time_start
    instance_object.endTime = "2035-12-28 23:59:59"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    return instance_object.timerID



def collection_chapter(excel_tool: ExcelToolsForActivities, fishery_id, fishery_index, chapterTimerId, chapterNamePanelId, icon_name, wildCardId, notOpenText=None):
    collection_chapter_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_CHAPTER.xlsm")
    key = "tpId"
    template_tpId = 1
    tpId = fishery_index
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId, table_data_detail=collection_chapter_detail)
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_tpId, table_data_detail=collection_chapter_detail)
    instance_object: COLLECTION_CHAPTER
    instance_object = json_to_instance(json_object=json_object_list[0], cls=COLLECTION_CHAPTER)
    instance_object.id = tpId
    instance_object.name = str(tpId)
    instance_object.tpId = tpId
    instance_object.chapterID = 100 + fishery_index
    instance_object.fishSceneTpId = fishery_id
    instance_object.chapterTimerId = chapterTimerId
    instance_object.chapterNamePanelId = chapterNamePanelId
    # instance_object.chapterPrizeIconName=f"division_flashcard_{icon_name}"
    instance_object.chapterPrizeIconName="division_flashcard_B13"
    instance_object.chapterPrizeResultIcon= f"flashcard_result_bannerbg_M_{icon_name}"
    instance_object.chapterPrizeResultTopIcon = f"flashcard_result_alltop_{icon_name}"
    instance_object.flashCardBooksMaterial = f"FlashCardBooks_M_{icon_name}"
    instance_object.wildCardId = wildCardId
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_chapter_detail,  instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_chapter_detail,  instance_object=instance_object)

def item_main(excel_tool: ExcelToolsForActivities, fishery_index, wildCardId, icon_name):
    # 万能卡
    template_itemTpId = 240150
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=wildCardId, table_data_detail=item_main_detail)
    if table_data_object_list:
        mode = 0
        template_itemTpId = table_data_object_list[0]["itemTpId"]
    else:
        mode = 1
        wildCardId = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=item_main_detail, start=240150)
    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    if mode == 1:
        instance_object.id = wildCardId
    instance_object.name = f"新主线万能卡{fishery_index}"
    instance_object.itemTpId = wildCardId
    instance_object.iconName = f"flashcard_com_{icon_name}"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)


def item_main_language(excel_tool: ExcelToolsForActivities,fishery_id, fishery_index, wildCardId):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"

    # 万能卡
    template_tpId = 240150
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=wildCardId, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 0
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    instance_object.tpId = wildCardId
    instance_object.name = f"新主线万能卡{fishery_index}"
    t_name = excel_tool.get_table_data_object_by_key_value(key="tpId",value=fishery_id,  book_name="FISHERIES_LANGUAGE.xlsm")["t_name"]

    instance_object.t_name = f"{t_name}-万能卡"
    instance_object.t_description = f"可兑换<{t_name}>闪卡册的任意一张闪卡"

    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)


def collection_energy_cost_debuff(excel_tool: ExcelToolsForActivities, fishery_id):
    collection_energy_cost_debuff_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_ENERGY_COST_DEBUFF.xlsm")

    template_tpId_start = 97
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fishSceneTpId", value=fishery_id, table_data_detail=collection_energy_cost_debuff_detail)
    key = "tpId"
    if table_data_object_list:
        mode = 0
        template_tpId_start = table_data_object_list[0]["tpId"]
        tpId_start = template_tpId_start
    else:
        mode = 1
        tpId_start = excel_tool.get_max_value(key=key, table_object_detail=collection_energy_cost_debuff_detail) + 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_energy_cost_debuff_detail) + 1
    cur = 0
    while cur < 8:
        instance_object: COLLECTION_ENERGY_COST_DEBUFF
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail= collection_energy_cost_debuff_detail, cls=COLLECTION_ENERGY_COST_DEBUFF)
        if mode == 1:
            instance_object.id = id_start + cur

        instance_object.tpId = tpId_start + cur
        instance_object.name = instance_object.tpId
        instance_object.fishSceneTpId = fishery_id
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_energy_cost_debuff_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_energy_cost_debuff_detail, instance_object=instance_object)
        cur += 1

def collection_protect(excel_tool: ExcelToolsForActivities, fishery_id):
    collection_protect_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_PROTECT.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    template_fishSceneTpId = 500301
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fishSceneTpId", value=fishery_id, table_data_detail=collection_protect_detail)
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fishSceneTpId", value=template_fishSceneTpId, table_data_detail=collection_protect_detail)
    key = "tpId"
    tpId_start = excel_tool.get_max_value(key=key, table_object_detail=collection_protect_detail) + 1
    id_start = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=collection_protect_detail, start=json_object_list[0]["id"], long=18)
    id_start = 137
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)
    monster_id_list = []
    for fish_id in fish_id_list:
        fish_class = excel_tool.get_fish_class(fish_id=fish_id, fish_detail=fish_detail)
        if fish_class != 4:
            continue
        monster_id_list.append(fish_id)
    cur = 0
    while cur < len(json_object_list):
        instance_object: COLLECTION_PROTECT
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=COLLECTION_PROTECT)
        if mode == 1:

            instance_object.tpId = tpId_start + cur
        instance_object.id = id_start + cur
        instance_object.fishSceneTpId = fishery_id
        instance_object.protectFishIdGroup[0] = monster_id_list[cur // 3]
        instance_object.protectFlashCardIdGroup[0] = excel_tool.get_flash_card_id(fish_id=instance_object.protectFishIdGroup[0])
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_protect_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_protect_detail, instance_object=instance_object)
        cur += 1


def collection_exchange_store(excel_tool: ExcelToolsForActivities, fishery_id, collectionChapterId, wildCardId):
    """
    itemTpId万能卡id
    """
    collection_exchange_store_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_EXCHANGE_STORE.xlsm")
    template_collectionChapterId = 101
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="collectionChapterId", value=collectionChapterId, table_data_detail=collection_exchange_store_detail)
    key = "tpId"
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="collectionChapterId", value=template_collectionChapterId, table_data_detail=collection_exchange_store_detail)
    tpId_start = excel_tool.get_max_value(key=key, table_object_detail=collection_exchange_store_detail) + 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_exchange_store_detail) + 1
    cur = 0
    while cur < len(json_object_list):
        instance_object: COLLECTION_EXCHANGE_STORE
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=COLLECTION_EXCHANGE_STORE)
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.tpId = tpId_start + cur
        instance_object.collectionChapterId = collectionChapterId

        if cur < 2:
            instance_object.itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.itemId, fishery_id=fishery_id)
        else:
            instance_object.itemId = wildCardId
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_exchange_store_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_exchange_store_detail, instance_object=instance_object)

        cur += 1


def collection_reward(excel_tool: ExcelToolsForActivities, fishery_id, collectionChapterId):
    collection_reward_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_REWARD.xlsm")
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="collectionChapterId", value=collectionChapterId, table_data_detail=collection_reward_detail)
    template_collectionChapterId = 102
    key = "tpId"
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="collectionChapterId", value=template_collectionChapterId, table_data_detail=collection_reward_detail)
    tpId_start = excel_tool.get_max_value(key=key, table_object_detail=collection_reward_detail) + 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_reward_detail) + 1
    cur = 0
    while cur < len(json_object_list):
        instance_object: COLLECTION_REWARD
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=COLLECTION_REWARD)
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.tpId = tpId_start + cur
        instance_object.collectionChapterId = collectionChapterId
        for normalRewards in instance_object.normalRewards:
            fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=normalRewards.itemId, fishery_id=fishery_id)
            if not fish_bag:
                continue
            normalRewards.itemId = fish_bag
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_reward_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_reward_detail, instance_object=instance_object)
        cur += 1

def panel_static_language(excel_tool: ExcelToolsForActivities, fishery_id, chapterNamePanelId, notOpenText=None):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    key = "templateID"
    instance_object: PANEL_STATIC_LANGUAGE

    # chapterNamePanelId
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=chapterNamePanelId, table_data_detail=panel_static_language_detail)
    if json_object_list:
        mode = 0
        instance_object = json_to_instance(json_object=json_object_list[0], cls=PANEL_STATIC_LANGUAGE)
    else:
        mode = 1
        instance_object = PANEL_STATIC_LANGUAGE()
    instance_object.id = chapterNamePanelId
    instance_object.name = "新主线闪卡"
    instance_object.templateID = chapterNamePanelId
    instance_object.t_panellanguage = f"{excel_tool.get_fishery_name(fishery_id=fishery_id)}"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)

    # notOpenText
    if notOpenText is None:
        mode = 1
        instance_object = PANEL_STATIC_LANGUAGE()
        notOpenText = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=panel_static_language_detail, start=19960945)
        instance_object.templateID = notOpenText
        instance_object.id = instance_object.templateID
    else:
        mode = 0
        json_object, instance_object = excel_tool.get_object(key=key, value=notOpenText, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)
    instance_object.name = "闪卡相关-渔场开启条件"
    instance_object.t_panellanguage = f"完成{excel_tool.get_fishery_name(fishery_id=fishery_id-1)}游钓任务后解锁{excel_tool.get_fishery_name(fishery_id=fishery_id)}渔场"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)

    return notOpenText





def main():
    """
        读写方式：新增/修改
    """
    # 配置修改区起始
    fishery_id = 500303
    icon_name = "S01C03"
    time_start = "2025-05-30 00:00:00"

    # 该区域参数为None则新增
    notOpenText = None  # panel_static_language中templateID 完成xxx游钓任务后解锁yyy渔场
    chapterTimerId = None  # timer_main中timerID 闪卡开启和结束时间
    wildCardId = None  # item_main中itemTpId 万能卡id

    # 根据偏移算中间值，当渔场id不按顺序新增时可能有问题
    fishery_index = fishery_id - 500300
    collectionChapterId = 100 + fishery_index
    chapterNamePanelId = 19960300 + fishery_index

    # 配置修改区结束
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    item_main(excel_tool=excel_tool, fishery_index=fishery_index, wildCardId=wildCardId, icon_name=icon_name)
    notOpenText = panel_static_language(excel_tool=excel_tool, fishery_id=fishery_id, chapterNamePanelId=chapterNamePanelId, notOpenText=notOpenText)
    item_main_language(excel_tool=excel_tool, fishery_id=fishery_id,fishery_index=fishery_index, wildCardId=wildCardId)
    collection_energy_cost_debuff(excel_tool=excel_tool, fishery_id=fishery_id)
    collection_exchange_store(excel_tool=excel_tool, fishery_id=fishery_id, collectionChapterId=collectionChapterId, wildCardId=wildCardId)
    collection_reward(excel_tool=excel_tool, fishery_id=fishery_id, collectionChapterId=collectionChapterId)
    collection_base(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index, collectionChapterId=collectionChapterId)
    chapterTimerId = timer_main(excel_tool=excel_tool,fishery_index=fishery_index, time_start=time_start, timerID=chapterTimerId)
    collection_chapter(excel_tool=excel_tool, fishery_id=fishery_id, fishery_index=fishery_index, chapterTimerId=chapterTimerId, chapterNamePanelId=chapterNamePanelId, icon_name=icon_name, wildCardId=wildCardId, notOpenText=notOpenText)
    collection_protect(excel_tool=excel_tool,  fishery_id=fishery_id)

    print("涉及到的表：", list(excel_tool.data_txt_changed))


if __name__ == '__main__':
    main()