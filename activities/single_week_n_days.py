from activities.decl.ACTIVITY_DOUBLE_WEEK import ACTIVITY_DOUBLE_WEEK
from activities.decl.BATTLE_PASS import BATTLE_PASS
from activities.decl.BATTLE_PASS_MAIN_2024 import BATTLE_PASS_MAIN_2024
from activities.decl.COLLECTION_BASE import COLLECTION_BASE, Energy_Drop_Rare
from activities.decl.COLLECTION_ENERGY_COST_DEBUFF import COLLECTION_ENERGY_COST_DEBUFF
from activities.decl.COLLECTION_EXCHANGE_STORE import COLLECTION_EXCHANGE_STORE
from activities.decl.COLLECTION_REWARD import COLLECTION_REWARD, CollectionReward
from activities.decl.EVENT_ENDLESS_SALE import EVENT_ENDLESS_SALE
from activities.decl.EVENT_N_DAY_TASKS_LEADERBOARD import EVENT_N_DAY_TASKS_LEADERBOARD
from activities.decl.EVENT_N_DAY_TASKS_MILESTONE import EVENT_N_DAY_TASKS_MILESTONE
from activities.decl.ITEM_MAIN import ITEM_MAIN
from activities.decl.ITEM_MAIN_LANGUAGE import ITEM_MAIN_LANGUAGE
from activities.decl.MISSION_CONDITION import MISSION_CONDITION
from activities.decl.MISSION_GROUP import MISSION_GROUP
from activities.decl.MISSION_MAIN import MISSION_MAIN
from activities.decl.PANEL_STATIC_LANGUAGE import PANEL_STATIC_LANGUAGE
from activities.decl.REPEATABLE_CHALLENGE import REPEATABLE_CHALLENGE
from activities.decl.REPEATABLE_CHALLENGE_LANGUAGE import REPEATABLE_CHALLENGE_LANGUAGE
from activities.decl.THREE_FISH_MAIN import THREE_FISH_MAIN, ThreeFishOffset
from activities.decl.THREE_FISH_RANK_REWARD import THREE_FISH_RANK_REWARD
from activities.decl.TIMER_MAIN import TIMER_MAIN
from configs.pathConfig import EXCEL_PATH
from tools import commonTools, baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
这个是没有开过双周活动的单周配置模板
"""

def activity_double_week(excel_tool: ExcelToolsForActivities,fishery_id, chapterID, TimerId, icon_name, paymentGiftId_start, activityFisheryNameId, chapterTimerId, returnTimerId, notShowBeforeReturn, wildCardId=None):
    paymentGiftId_cfg = {
        500021: {"paymentGiftId_start": 2510096, "paymentGiftId_count": 9},
        500023: {"paymentGiftId_start": 2510085, "paymentGiftId_count": 10},
        500024: {"paymentGiftId_start": 2510117, "paymentGiftId_count": 10},
        500026: {"paymentGiftId_start": 2510075, "paymentGiftId_count": 10},
        500028: {"paymentGiftId_start": 2510039, "paymentGiftId_count": 10},
        500029: {"paymentGiftId_start": 2510064, "paymentGiftId_count": 10},
           }
    key = "tpId"
    tpId = 10000000 + fishery_id
    activity_double_week_detail = excel_tool.get_table_data_detail(book_name="ACTIVITY_DOUBLE_WEEK.xlsm")
    json_object_list = activity_double_week_detail[0]
    template_tpId = 10400310
    # mode = 0 替换， mode = 1 新增
    if excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId, table_data_detail=activity_double_week_detail):
        template_tpId = tpId
        mode = 0
    else:
        mode = 1

    instance_object: ACTIVITY_DOUBLE_WEEK
    json_object, instance_object = excel_tool.get_object(key="tpId", value=template_tpId, table_data_detail=activity_double_week_detail, cls=ACTIVITY_DOUBLE_WEEK)
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=activity_double_week_detail) + 1
    instance_object.chapterID = chapterID
    instance_object.name = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_language_detail)["t_name"]
    instance_object.tpId = tpId
    instance_object.fishSceneTpId = fishery_id
    instance_object.fishSpot = [fishery_id * 100 + 1, fishery_id * 100 + 2, fishery_id * 100 + 3, fishery_id * 100 + 4]
    instance_object.fishSpotB = [fishery_id * 100 + 11, fishery_id * 100 + 12, fishery_id * 100 + 13, fishery_id * 100 + 14]

    # 渔场鱼数
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)
    fish_type_detail = excel_tool.get_fishery_fish_type_detail(fishery_id=fishery_id)
    instance_object.fishIdNew = [int(fish_id_list[-3]), int(fish_id_list[-2]), int(fish_id_list[-1])]
    instance_object.chapterPrizeIconName = f"division_flashcard_{icon_name}"
    instance_object.chapterProgressNum = f"{fish_type_detail['total']},{fish_type_detail['monster']},{fish_type_detail['elite'] + fish_type_detail['rare']},{fish_type_detail['total_common']}"
    instance_object.chapterPrizeEnterIconName = f"division_flashcard_{icon_name}"
    instance_object.chapterPrizeResultIcon = f"flashcard_result_bannerbg_{icon_name}"
    instance_object.chapterPrizeResultTopIcon = f"flashcard_result_alltop_{icon_name}"
    instance_object.flashCardBooksMaterial = f"FlashCardBooks_out_mat_{icon_name}"
    rod_id = excel_tool.get_rod(fishery_id=fishery_id, rarity=4)[0]
    if rod_id not in paymentGiftId_cfg:
        raise FileNotFoundError("没有适合该渔场的礼包配置")
    paymentGiftId_start = paymentGiftId_cfg[rod_id]["paymentGiftId_start"]
    paymentGiftId_count = paymentGiftId_cfg[rod_id]["paymentGiftId_count"]
    print(f"paymentGiftId_start:{paymentGiftId_start}")
    payment_gift_id_list = []
    cur = 0
    while cur < paymentGiftId_count:
        payment_gift_id_list.append(paymentGiftId_start + cur)
        cur += 1
    while cur < 10:
        payment_gift_id_list.append(0)
        cur += 1
    instance_object.paymentGiftId = payment_gift_id_list
    instance_object.activityFisheryNameId = activityFisheryNameId
    if wildCardId:
        instance_object.wildCardOpen = 1
        instance_object.wildCardId = wildCardId
    instance_object.chapterTimerId = chapterTimerId
    if TimerId:
        instance_object.TimerId = TimerId
        instance_object.doubleRewardTimerId = TimerId
    instance_object.returnId = 1
    instance_object.returnTimerId = returnTimerId
    instance_object.notShowBeforeReturn = notShowBeforeReturn
    instance_object.flashCardOrder = instance_object.chapterID
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=activity_double_week_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=activity_double_week_detail, instance_object=instance_object)

def battle_pass_main_2024(excel_tool: ExcelToolsForActivities, fishery_id, groupId_battle_pass, returnTimerId, newNDaysImgName, activityFisheryNameId):
    battle_pass_main_2024_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS_MAIN_2024.xlsm")
    template_groupId = 21

    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_battle_pass, table_data_detail=battle_pass_main_2024_detail)
    key = "tpId"
    instance_object: BATTLE_PASS_MAIN_2024
    if table_data_object_list:
        mode = 0
        instance_object = json_to_instance(json_object=table_data_object_list[0], cls=BATTLE_PASS_MAIN_2024)
    else:
        mode = 1
        _, instance_object = excel_tool.get_object(key="groupId", value=template_groupId, table_data_detail=battle_pass_main_2024_detail, cls=BATTLE_PASS_MAIN_2024)
        instance_object.tpId = excel_tool.get_max_value(key=key, table_object_detail=battle_pass_main_2024_detail) + 1
    instance_object.name = f"{fishery_id}双周BP"
    instance_object.groupId = groupId_battle_pass
    instance_object.firstOpenTimerId = returnTimerId
    instance_object.activityBPName = f"Assets/InBundle/UI/Texture/activity_ndays/{newNDaysImgName}.png"
    instance_object.activityBPId = activityFisheryNameId
    instance_object.fisheriesId = fishery_id
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)

def battle_pass(excel_tool: ExcelToolsForActivities, groupId_battle_pass):
    battle_pass_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS.xlsm")
    template_groupId = 21
    id_start = excel_tool.get_max_value(key="id", table_object_detail=battle_pass_detail) + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_battle_pass, table_data_detail=battle_pass_detail)
    key = "tpId"
    if table_data_object_list:
        mode = 0
        tpId_start = table_data_object_list[0]["tpId"]
    else:
        mode = 1
        table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=battle_pass_detail)
        tpId_start = excel_tool.get_max_value(key=key, table_object_detail=battle_pass_detail) + 1
    cur = 0
    while cur < len(table_data_object_list):
        json_object = table_data_object_list[cur]
        instance_object: BATTLE_PASS
        instance_object = json_to_instance(json_object=json_object, cls=BATTLE_PASS)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.tpId = tpId_start + cur
        instance_object.groupId = groupId_battle_pass

        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_detail, instance_object=instance_object)

        cur += 1



def collection_base(excel_tool: ExcelToolsForActivities, fishery_id, collectionChapterId):
    cfg_list = [
        {"dropRate_list": [1, 5, 30], "ownedDebuff": 30, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [1, 3, 16], "ownedDebuff": 30, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [2, 4, 7], "ownedDebuff": 30, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [3, 3, 7], "ownedDebuff": 30, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [3, 3, 5], "ownedDebuff": 30, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [9, 9, 12], "ownedDebuff": 30, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [11, 11, 15],"ownedDebuff": 40, "totalEnergyCostGroup": [0, 0, 0]},
        {"dropRate_list": [40, 40, 30],"ownedDebuff": 20, "totalEnergyCostGroup": [0, 0, 0]},
    ]

    collection_base_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_BASE.xlsm")
    fish_detail = excel_tool.get_table_data_detail(book_name="FISH.xlsm")
    key = "fishId"
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)
    fishery_fish_type_detail = excel_tool.get_fishery_fish_type_detail(fishery_id=fishery_id)
    fish_count = fishery_fish_type_detail["total"]

    template_fish_id = 310001
    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_base_detail) + 1
    collectionId_start = excel_tool.get_max_value(key="collectionId", table_object_detail=collection_base_detail) + 1
    cur = 0
    while cur < fish_count:
        fish_id = fish_id_list[cur]
        # mode = 0 替换， mode = 1 新增
        if excel_tool.get_table_data_object_list_by_key_value(key=key, value=fish_id, table_data_detail=collection_base_detail):
            mode = 0
            template_fish_id = fish_id_list[cur]
        else:
            mode = 1

        instance_object: COLLECTION_BASE
        json_object, instance_object = excel_tool.get_object(key=key, value=template_fish_id, table_data_detail=collection_base_detail, cls=COLLECTION_BASE)
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.collectionId = collectionId_start + cur
        instance_object.name = f"{cur + 1}"
        instance_object.fishId = fish_id
        instance_object.fishSceneTpId = fishery_id
        fish_class = excel_tool.get_fish_class(fish_id=fish_id, fish_detail=fish_detail)
        if fish_class > 3:
            instance_object.collectionLevel = 3
        elif fish_class > 1:
            instance_object.collectionLevel = 2
        else:
            instance_object.collectionLevel = 1
        instance_object.collectionChapterId = collectionChapterId

        if fish_class == 1:
            fish_type = excel_tool.get_fish_type(fish_id=fish_id)
            fish_kind = fish_type - 1
        else:
            fish_kind = fish_class + 3

        energy_drop_rare_0 = Energy_Drop_Rare()
        energy_drop_rare_0.baseCost = 1
        energy_drop_rare_0.dropRate = cfg_list[fish_kind]["dropRate_list"][0]
        energy_drop_rare_1 = Energy_Drop_Rare()
        energy_drop_rare_1.baseCost = 3
        energy_drop_rare_1.dropRate = cfg_list[fish_kind]["dropRate_list"][1]
        energy_drop_rare_2 = Energy_Drop_Rare()
        energy_drop_rare_2.baseCost = 10
        energy_drop_rare_2.dropRate = cfg_list[fish_kind]["dropRate_list"][2]
        instance_object.energyDropRate = [energy_drop_rare_0, energy_drop_rare_1, energy_drop_rare_2]
        instance_object.ownedDebuff = cfg_list[fish_kind]["ownedDebuff"]

        name = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fish_id, table_data_detail=fish_detail)["displayicon"].split("/")[1]
        instance_object.resourceName = f"icon_flashcard_{name}"
        instance_object.orderId = cur + 1
        # if fish_count != 15:
        #     raise IndexError("totalEnergyCostGroup需要确认下配置")
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.fishId, table_data_detail=collection_base_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.fishId, table_data_detail=collection_base_detail, instance_object=instance_object)
        cur += 1

def collection_energy_cost_debuff(excel_tool: ExcelToolsForActivities, fishery_id):
    collection_energy_cost_debuff_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_ENERGY_COST_DEBUFF.xlsm")

    template_tpId_start = 129
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

def collection_exchange_store(excel_tool: ExcelToolsForActivities, fishery_id, collectionChapterId, wildCardId):
    """
    itemTpId万能卡id
    """
    collection_exchange_store_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_EXCHANGE_STORE.xlsm")
    template_tpId_start = 76
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="collectionChapterId", value=collectionChapterId, table_data_detail=collection_exchange_store_detail)
    key = "tpId"
    if table_data_object_list:
        mode = 0
        template_tpId_start = table_data_object_list[0]["tpId"]
        tpId_start = template_tpId_start
    else:
        mode = 1
        tpId_start = excel_tool.get_max_value(key=key, table_object_detail=collection_exchange_store_detail) + 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_exchange_store_detail) + 1

    cur = 0
    while cur < 5:
        instance_object: COLLECTION_ENERGY_COST_DEBUFF
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail=collection_exchange_store_detail, cls=COLLECTION_EXCHANGE_STORE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.tpId = tpId_start + cur
        instance_object.collectionChapterId = collectionChapterId

        if cur > 3:
            instance_object.itemId = wildCardId
        elif cur % 2 == 0:
            instance_object.itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.itemId, fishery_id=fishery_id)
        else:
            instance_object.itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.itemId, fishery_id=5)


        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_exchange_store_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_exchange_store_detail, instance_object=instance_object)

        cur += 1
# 稍后写
# def collection_protect(excel_tool: ExcelToolsForActivities, fishery_id):
#     collection_protect_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_PROTECT.xlsm")
#     table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="fishSceneTpId", value=fishery_id, table_data_detail=collection_protect_detail)
#     template_tpId_start =
#     if table_data_object_list:
#         mode = 0
#         template_tpId_start = table_data_object_list[0]["tpId"]
#         tpId_start = template_tpId_start
#     else:
#         mode = 1
#         tpId_start = get_max_tpId() + 1

def collection_reward(excel_tool: ExcelToolsForActivities, fishery_id, collectionChapterId, big_reward):
    collection_reward_detail = excel_tool.get_table_data_detail(book_name="COLLECTION_REWARD.xlsm")
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="collectionChapterId", value=collectionChapterId, table_data_detail=collection_reward_detail)
    template_tpId_start = 65
    key = "tpId"
    if table_data_object_list:
        mode = 0
        template_tpId_start = table_data_object_list[0]["tpId"]
        tpId_start = template_tpId_start
    else:
        mode = 1
        tpId_start = excel_tool.get_max_value(key=key, table_object_detail=collection_reward_detail) + 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=collection_reward_detail) + 1
    cur = 0
    while cur < 4:
        instance_object: COLLECTION_REWARD
        json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId_start + cur, table_data_detail=collection_reward_detail, cls=COLLECTION_REWARD)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.tpId = tpId_start + cur
        instance_object.collectionChapterId = collectionChapterId
        if cur == 0:
            instance_object.eventRewards[0].itemId = big_reward["tpId"]
            instance_object.eventRewards[0].itemType = big_reward["itemType"]
            instance_object.eventRewards[0].itemCount = big_reward["count"]
            instance_object.normalRewards[0] = instance_object.eventRewards[0]
            instance_object.eventRewards[1].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.eventRewards[1].itemId, fishery_id=fishery_id)
            instance_object.eventRewards[2].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.eventRewards[2].itemId, fishery_id=fishery_id)
            instance_object.normalRewards[1].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.normalRewards[1].itemId, fishery_id=fishery_id)
            instance_object.normalRewards[2].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.normalRewards[2].itemId, fishery_id=fishery_id)
        else:
            instance_object.eventRewards[0].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.eventRewards[0].itemId, fishery_id=fishery_id)
            instance_object.normalRewards[0].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.normalRewards[0].itemId, fishery_id=fishery_id)
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_reward_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_reward_detail, instance_object=instance_object)
        cur += 1

def event_endless_sale(excel_tool: ExcelToolsForActivities, fishery_id, groupId):
    groupId_sale = groupId + 1
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    fishing_rod_detail = excel_tool.get_table_data_detail(book_name="FISHING_ROD.xlsm")
    fish_bag_detail = baseDataRead.convert_to_json(path=excel_tool.root_dir + "/activities/customTables/", prefix="FISH_BAG")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_sale, table_data_detail=event_endless_sale_detail)
    template_autoId_start = 20020651
    key = "autoId"
    if table_data_object_list:
        mode = 0
        autoId_start = table_data_object_list[0]["autoId"]
        template_autoId_start = autoId_start
    else:
        mode = 1
        autoId_start = excel_tool.get_max_value(key=key, table_object_detail=event_endless_sale_detail) + 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=event_endless_sale_detail) + 1

    cur = 0
    while cur < 9:
        instance_object: EVENT_ENDLESS_SALE
        json_object, instance_object = excel_tool.get_object(key=key, value=template_autoId_start + cur, table_data_detail=event_endless_sale_detail, cls=EVENT_ENDLESS_SALE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.autoId = autoId_start + cur
        instance_object.groupId = groupId_sale
        rod_id = excel_tool.get_rod(fishery_id=fishery_id, rarity=4, fishing_rod_detail=fishing_rod_detail, fisheries_detail=fisheries_detail)[0]
        rod_icon = excel_tool.get_rod_icon(rod_id=rod_id, fishing_rod_detail=fishing_rod_detail)
        instance_object.imgRodGiftpack = rod_icon
        for item in instance_object.normalItem:
            if item.ioIdType == 5:
                item.tpId = rod_id
                continue
            fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=item.tpId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
            if fish_bag:
                item.tpId = fish_bag

        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_endless_sale_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_endless_sale_detail, instance_object=instance_object)
        cur += 1

def event_n_day_tasks_leaderboard(excel_tool: ExcelToolsForActivities, fishery_id, groupId):
    event_n_day_tasks_leaderboard_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_LEADERBOARD.xlsm")
    template_autoId_start = 302
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=event_n_day_tasks_leaderboard_detail)
    key = "autoId"
    if table_data_object_list:
        mode = 0
        template_autoId_start = table_data_object_list[0]["autoId"]
        autoId_start = template_autoId_start
    else:
        mode = 1
        autoId_start = excel_tool.get_max_value(key=key, table_object_detail=event_n_day_tasks_leaderboard_detail) + 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=event_n_day_tasks_leaderboard_detail) + 1
    cur = 0
    while cur < 9:
        instance_object: EVENT_N_DAY_TASKS_LEADERBOARD
        json_object, instance_object = excel_tool.get_object(key=key, value=template_autoId_start + cur, table_data_detail=event_n_day_tasks_leaderboard_detail, cls=EVENT_N_DAY_TASKS_LEADERBOARD)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.autoId = autoId_start + cur
        instance_object.groupId = groupId

        instance_object.leaderboardAwards[0].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.leaderboardAwards[0].itemId, fishery_id=fishery_id)
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_leaderboard_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_leaderboard_detail, instance_object=instance_object)
        cur += 1

def event_n_day_tasks_milestone(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID):
    event_n_day_tasks_milestone_detail = excel_tool.get_table_data_detail(book_name="EVENT_N_DAY_TASKS_MILESTONE.xlsm")
    template_autoId_start = 1577
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=event_n_day_tasks_milestone_detail)
    key = "autoId"
    if table_data_object_list:
        mode = 0
        template_autoId_start = table_data_object_list[0]["autoId"]
        autoId_start = template_autoId_start
    else:
        mode = 1
        autoId_start = excel_tool.get_max_value(key=key, table_object_detail=event_n_day_tasks_milestone_detail) + 1

    id_start = excel_tool.get_max_value(key="id", table_object_detail=event_n_day_tasks_milestone_detail) + 1
    cur = 0
    while cur < 25:
        instance_object: EVENT_N_DAY_TASKS_MILESTONE
        json_object, instance_object = excel_tool.get_object(key=key, value=template_autoId_start + cur, table_data_detail=event_n_day_tasks_milestone_detail, cls=EVENT_N_DAY_TASKS_MILESTONE)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.autoId = autoId_start + cur
        instance_object.tokenID = tokenID
        instance_object.groupId = groupId
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.milestoneRewards[0].itemId, fishery_id=fishery_id)
        if fish_bag:
            instance_object.milestoneRewards[0].itemId = fish_bag
        if cur == 24:
            instance_object.milestoneRewards[0].itemId = excel_tool.get_rod(fishery_id=fishery_id, rarity=4)[0]
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        cur += 1

def item_main(excel_tool: ExcelToolsForActivities, fishery_id, wildCardId, icon_name,tokenID):
    # 万能卡
    template_itemTpId = 240153
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=wildCardId, table_data_detail=item_main_detail)
    if table_data_object_list:
        mode = 0
        template_itemTpId = table_data_object_list[0]["itemTpId"]
    else:
        mode = 1
    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    instance_object.name = f"{fishery_id}万能卡"
    instance_object.itemTpId = wildCardId
    instance_object.iconName = f"flashcard_com_{icon_name}"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)


    # 活动代币
    template_itemTpId = 291008
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_detail)
    if table_data_object_list:
        mode = 0
        template_itemTpId = table_data_object_list[0]["itemTpId"]
    else:
        mode = 1
    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_detail) + 1
    instance_object.name = f"{fishery_id}双周返场活动代币"
    instance_object.itemTpId = tokenID
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)

def item_main_language(excel_tool: ExcelToolsForActivities,fishery_id, wildCardId, tokenID, activityFisheryName, internal_or_global):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"

    # 万能卡
    template_tpId = 240153
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
    instance_object.name = f"{fishery_id}万能卡"
    t_name = excel_tool.get_table_data_object_by_key_value(key="tpId",value=fishery_id,  book_name="FISHERIES_LANGUAGE.xlsm")["t_name"]

    if internal_or_global == "internal":
        instance_object.t_name = f"{t_name}-万能卡"
        instance_object.t_description = f"可兑换<{t_name}>闪卡册的任意一张闪卡"
    else:
        instance_object.t_name = f"{t_name} - Mystery Card"
        instance_object.t_description = f"Exchangeable for any Chrome Card from the {t_name} Chrome Card Album. "
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)

    # 活动代币
    template_tpId = 291008
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 0
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    instance_object.name = f"{fishery_id}双周返场活动代币"
    instance_object.tpId = tokenID
    if internal_or_global == "internal":
        instance_object.t_description = f"在{activityFisheryName}中收集活动积分，赢取额外奖励。"
    else:
        instance_object.t_description = f"Collect Event Points to win extra rewards in {activityFisheryName}"
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)

def mission_group(excel_tool: ExcelToolsForActivities, groupId, TimerId, fishery_id, activityName, imgNameInner,  newNDaysImgName, missionType, groupId_three_fish=None):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    key = "groupId"

    # ndays
    template_groupId = 5100011
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId, table_data_detail=mission_group_detail)
    if table_data_object_list:
        mode = 0
        template_groupId = table_data_object_list[0][key]
    else:
        mode = 1
    id_start = excel_tool.get_max_value(key="id", table_object_detail=mission_group_detail) + 1
    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    if mode == 1:
        instance_object.id = id_start
    instance_object.name = f"{fishery_id}的返场活动"
    instance_object.groupId = groupId
    instance_object.openArg = TimerId
    instance_object.closeArg = TimerId
    instance_object.extArgs[2] = f"{groupId + 1}"
    instance_object.extArgs[5] = f"{fishery_id}"
    instance_object.extArgs[6] = instance_object.extArgs[5]
    instance_object.extArgs[7] = "0"
    if groupId_three_fish:
        instance_object.extArgs[7] = f"{groupId_three_fish}"
    server_chara_level = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fishery_id, book_name="FISHERIES.xlsm")["needPlayerLv"]
    instance_object.serverCharaLevel = server_chara_level
    instance_object.activityName = activityName
    instance_object.imgNameInner = imgNameInner
    instance_object.iconName = "prepare_activity_RookieTasks_2"
    if missionType is None:
        missionType = excel_tool.get_max_value(key="missionType", table_object_detail=mission_group_detail)
    instance_object.missionType = missionType
    instance_object.newNDaysImgName = newNDaysImgName
    instance_object.activityName2 = None
    if server_chara_level < 40:
        instance_object.rankHouseRulesId = 1001
    else:
        instance_object.rankHouseRulesId = 1002
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

    # ndays促销
    template_groupId += 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId + 1, table_data_detail=mission_group_detail)
    if table_data_object_list:
        mode = 0
        template_groupId = table_data_object_list[0][key]
    else:
        mode = 1
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    if mode == 1:
        instance_object.id = id_start + 1
    instance_object.name = f"{fishery_id}的促销"
    instance_object.openArg = TimerId
    instance_object.closeArg = TimerId
    instance_object.groupId = groupId + 1
    rod_id = excel_tool.get_rod(fishery_id=fishery_id, rarity=4)[0]
    rod_icon = excel_tool.get_table_data_object_by_key_value(key="tpId", value=rod_id, book_name="FISHING_ROD.xlsm")["displayicon"]
    instance_object.imgRodGiftpack = rod_icon
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

    # # 三鱼排行榜
    if groupId_three_fish is None:
        return
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId_three_fish, table_data_detail=mission_group_detail)
    if table_data_object_list:
        mode = 0
        instance_object = json_to_instance(json_object=table_data_object_list[0], cls=MISSION_GROUP)
    else:
        mode = 1
        instance_object = MISSION_GROUP()
        instance_object.id = id_start + 2
    instance_object.name = "三鱼排行榜活动"
    instance_object.groupId = groupId_three_fish
    instance_object.enabled = 1
    instance_object.key = "THREE_FISH"
    instance_object.keyDesc = "三鱼排行榜活动"
    instance_object.openType = 2
    instance_object.openArg = TimerId
    instance_object.closeType = 2
    instance_object.closeArg = TimerId
    instance_object.extArgs = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",]
    instance_object.serverCharaLevel = server_chara_level
    if server_chara_level < 40:
        instance_object.rankHouseRulesId = 1001
    else:
        instance_object.rankHouseRulesId = 1002
    instance_object.missionType = 0

    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

def mission_main(excel_tool: ExcelToolsForActivities,fishery_id, groupId, missionType, tokenID):
    mission_cfg_list = [
        {"template_missionID": 6011236, "template_missionConditionIDs": {6011250:["fishery_id", "fisheries_language"], } },
        {"template_missionID": 6011237, "template_missionConditionIDs": {6011251: ["fishery_id", "fisheries_language"],} },
        {"template_missionID": 6011238, "template_missionConditionIDs": {6011252: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011239, "template_missionConditionIDs": {6011253: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011240, "template_missionConditionIDs": {6011254: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011241, "template_missionConditionIDs": {6011255: ["fishery_id", "fisheries_language", "fish_language1"]}, },
        {"template_missionID": 6011242, "template_missionConditionIDs": {6011256: ["fishery_id", "fisheries_language", "fish_language1"]}, },
        {"template_missionID": 6011243, "template_missionConditionIDs": {6011257: ["fishery_id", "fisheries_language", "fish_language1"]}, },
        {"template_missionID": 6011244, "template_missionConditionIDs": {6011258: ["fishery_id", "fisheries_language", "fish_language1"]}, },
        {"template_missionID": 6011245, "template_missionConditionIDs": {6011259: ["fishery_id", "fisheries_language", "fish_language1"]}, },
        {"template_missionID": 6011246, "template_missionConditionIDs": {6011260: ["fishery_id", "fisheries_language", "fish_language2"]}, },
        {"template_missionID": 6011247, "template_missionConditionIDs": {6011261: ["fishery_id", "fisheries_language", "fish_language2"]}, },
        {"template_missionID": 6011248, "template_missionConditionIDs": {6011262: ["fishery_id", "fisheries_language", "fish_language2"]}, },
        {"template_missionID": 6011249, "template_missionConditionIDs": {6011263: ["fishery_id", "fisheries_language", "fish_language2"]}, },
        {"template_missionID": 6011250, "template_missionConditionIDs": {6011264: ["fishery_id", "fisheries_language", "fish_language2"]}, },
        {"template_missionID": 6011251, "template_missionConditionIDs": {6011265: ["fishery_id", "fisheries_language"], 6011292:["fishery_id"] }},
        {"template_missionID": 6011252, "template_missionConditionIDs": {6011266: ["fishery_id", "fisheries_language"], 6011293:["fishery_id"] }},
        {"template_missionID": 6011253, "template_missionConditionIDs": {6011267: ["fishery_id", "fisheries_language"], 6011294:["fishery_id"] }},
        {"template_missionID": 6011254, "template_missionConditionIDs": {6011268: ["fishery_id", "fisheries_language"], 6011295:["fishery_id"] }},
        {"template_missionID": 6011255, "template_missionConditionIDs": {6011269: ["fishery_id", "fisheries_language"], 6011296:["fishery_id"]}},
        {"template_missionID": 6011256, "template_missionConditionIDs": {6011270: ["fishery_id", "fisheries_language"], 6011297:["fishery_id"] }},
        {"template_missionID": 6011257, "template_missionConditionIDs": {6011271: ["fishery_id", "fisheries_language"], 6011298:["fishery_id"]}},
        {"template_missionID": 6011258, "template_missionConditionIDs": {6011272: ["rod_detail"]}, "mission_language": "lv"},
        {"template_missionID": 6011259, "template_missionConditionIDs": {6011273: ["rod_detail"]}, "mission_language": "lv"},
        {"template_missionID": 6011260, "template_missionConditionIDs": {6011274: ["rod_detail"]}, "mission_language": "lv"},
        {"template_missionID": 6011261, "template_missionConditionIDs": {6011275: ["rod_detail"]}, "mission_language": "star"},
        {"template_missionID": 6011262, "template_missionConditionIDs": {6011276: ["rod_detail"]}, "mission_language": "star"},
        {"template_missionID": 6011263, "template_missionConditionIDs": {6011277: ["rod_detail"]}, "mission_language": "star" },
        {"template_missionID": 6011264, "template_missionConditionIDs": {6011278: []}, },
        {"template_missionID": 6011265, "template_missionConditionIDs": {6011279: []}, },
        {"template_missionID": 6011266, "template_missionConditionIDs": {6011280: []}, },
        {"template_missionID": 6011267, "template_missionConditionIDs": {6011281: []}, },
        {"template_missionID": 6011268, "template_missionConditionIDs": {6011282: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011269, "template_missionConditionIDs": {6011283: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011270, "template_missionConditionIDs": {6011284: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011271, "template_missionConditionIDs": {6011285: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011272, "template_missionConditionIDs": {6011286: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011273, "template_missionConditionIDs": {6011287: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011274, "template_missionConditionIDs": {6011288: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011275, "template_missionConditionIDs": {6011289: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011276, "template_missionConditionIDs": {6011290: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011277, "template_missionConditionIDs": {6011291: ["fishery_id", "fisheries_language"]}, },
        {"template_missionID": 6011846, "template_missionConditionIDs": {6011946: ["fishery_id", "fisheries_language"]} },
        {"template_missionID": 6011847, "template_missionConditionIDs": {6011947: ["fishery_id", "fisheries_language"]}},
        {"template_missionID": 6011848, "template_missionConditionIDs": {6011948: ["fishery_id", "fisheries_language"]} },
        {"template_missionID": 6011849, "template_missionConditionIDs": {6011949: ["fishery_id", "fisheries_language"]}}
    ]
    def get_mission_language_id(fishery_living, mode):
        if mode == "star":
            if fishery_living == 1:
                return 6011108
            else:
                return 6011113
        # lv
        if fishery_living == 1:
            return 6011107
        else:
            return 6011112
    mission_main_detail = excel_tool.get_table_data_detail(book_name="MISSION_MAIN.xlsm")
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    fish_bag_detail = baseDataRead.convert_to_json(path=excel_tool.root_dir + "/activities/customTables/", prefix="FISH_BAG")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=mission_main_detail) + 1
    missionConditionID_start = excel_tool.get_max_value(key="missionConditionID", table_object_detail=mission_condition_detail) + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=mission_main_detail)
    if table_data_object_list:
        mode = 0
    else:
        mode = 1
    missionID_start = excel_tool.get_max_value(key="missionID", table_object_detail=mission_main_detail) + 1
    missionConditionID_set = set()
    key = "missionID"
    cur = 0
    while cur < len(mission_cfg_list):
        mission_cfg = mission_cfg_list[cur]
        instance_object: MISSION_MAIN

        if mode == 1:
            json_object, instance_object = excel_tool.get_object(key=key, value=mission_cfg["template_missionID"], table_data_detail=mission_main_detail, cls=MISSION_MAIN)
            instance_object.id = id_start + cur
            instance_object.missionID = missionID_start + cur
            missionConditionID = missionConditionID_start + cur
            while missionConditionID in missionConditionID_set:
                missionConditionID += 1
            instance_object.missionConditionIDs[0] = missionConditionID
            missionConditionID_set.add(instance_object.missionConditionIDs[0])
            if len(mission_cfg["template_missionConditionIDs"]) > 1:
                instance_object.missionConditionIDs[1] = instance_object.missionConditionIDs[0] + 27
                missionConditionID_set.add(instance_object.missionConditionIDs[1])
        else:
            instance_object = json_to_instance(json_object=table_data_object_list[cur], cls=MISSION_MAIN)
            missionConditionID_set.add(instance_object.missionConditionIDs[0])
            if len(mission_cfg["template_missionConditionIDs"]) > 1:
                missionConditionID_set.add(instance_object.missionConditionIDs[1])
        # missionConditionID_set有该值就加一直到无重复
        if "mission_language" in mission_cfg:
            fishery_rank, fishery_living, _ = excel_tool.get_fishery_detail(fishery_id=fishery_id, fisheries_detail=fisheries_detail)
            mission_language_id = get_mission_language_id(fishery_living, mission_cfg["mission_language"])
            instance_object.mission_language = mission_language_id

        instance_object.enabled = 1
        instance_object.groupId = groupId
        instance_object.missionType = missionType
        if instance_object.missionRedirection == 8:
            instance_object.redirectionParams[0] = fishery_id

        instance_object.awards[0].itemId = tokenID

        # 卡包转换
        fish_bag = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.awards[1].itemId, fishery_id=fishery_id, table_object_detail=fish_bag_detail)
        if fish_bag:
            instance_object.awards[1].itemId = fish_bag
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.missionID, table_data_detail=mission_main_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionID, table_data_detail=mission_main_detail, instance_object=instance_object)
        cur += 1

    # 接着整mission_condition表
    missionConditionID_list = sorted(missionConditionID_set)
    mission_condition(excel_tool=excel_tool, fishery_id=fishery_id, mission_cfg_list=mission_cfg_list,  missionConditionID_list=missionConditionID_list)

def mission_condition(excel_tool: ExcelToolsForActivities,fishery_id, mission_cfg_list, missionConditionID_list):
    mission_condition_detail = excel_tool.get_table_data_detail(book_name="MISSION_CONDITION.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    mission_condition_cfg_dict = {}
    cur = 0
    while cur < len(mission_cfg_list):
        template_missionConditionIDs = mission_cfg_list[cur]["template_missionConditionIDs"]
        mission_condition_cfg_dict.update(template_missionConditionIDs)
        cur += 1
    template_missionConditionID_list = sorted(mission_condition_cfg_dict)
    template_missionConditionID_list_copy = template_missionConditionID_list
    id_start = excel_tool.get_max_value(key="id", table_object_detail=mission_condition_detail) + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="missionConditionID", value=missionConditionID_list[0], table_data_detail=mission_condition_detail)
    if table_data_object_list:
        mode = 0
        template_missionConditionID_list = missionConditionID_list
    else:
        mode = 1

    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)
    key = "missionConditionID"

    cur = 0
    while cur < len(template_missionConditionID_list):
        missionConditionID = missionConditionID_list[cur]
        template_missionConditionID = template_missionConditionID_list[cur]
        mission_condition_cfg = mission_condition_cfg_dict[template_missionConditionID_list_copy[cur]]
        instance_object: MISSION_CONDITION
        json_object, instance_object = excel_tool.get_object(key=key, value=template_missionConditionID, table_data_detail=mission_condition_detail, cls=MISSION_CONDITION)
        if mode == 1:
            instance_object.id = id_start + cur
        instance_object.missionConditionID = missionConditionID
        if "rod_detail" in mission_condition_cfg:
            fishery_rank, fishery_living, _ = excel_tool.get_fishery_detail(fishery_id=fishery_id, fisheries_detail=fisheries_detail)
            instance_object.triggerKeyM = fishery_rank
            instance_object.triggerKeyS = fishery_living
            instance_object.numDisplay[0] = f"{fishery_rank}"
        if "fishery_id" in mission_condition_cfg:
            instance_object.triggerKeyM = fishery_id
        if "fisheries_language" in mission_condition_cfg:
            instance_object.numDisplay[0] = f"fisheries_language|t_name|{fishery_id}"
        if "fish_language1" in mission_condition_cfg:
            instance_object.numDisplay[1] = f"fish_language|t_fishName|{fish_id_list[-2]}"
            instance_object.triggerKeyS = fish_id_list[-2]
        if "fish_language2" in mission_condition_cfg:
            instance_object.numDisplay[1] = f"fish_language|t_fishName|{fish_id_list[-1]}"
            instance_object.triggerKeyS = fish_id_list[-1]


        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        cur += 1

def panel_static_language(excel_tool: ExcelToolsForActivities, t_panellanguage):
    # 标题语言
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    key = "templateID"
    instance_object = PANEL_STATIC_LANGUAGE()
    instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=panel_static_language_detail) + 1
    instance_object.name = t_panellanguage
    instance_object.templateID = excel_tool.get_max_value(key=key, table_object_detail=panel_static_language_detail) + 1
    instance_object.t_panellanguage = t_panellanguage
    print(instance_object)
    excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)


def repeatable_challenge(excel_tool: ExcelToolsForActivities, fishery_id, groupId, tokenID):
    repeatable_challenge_detail = excel_tool.get_table_data_detail(book_name="REPEATABLE_CHALLENGE.xlsm")
    repeatable_challenge_language_detail = excel_tool.get_table_data_detail(book_name="REPEATABLE_CHALLENGE_LANGUAGE.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=repeatable_challenge_detail) + 1
    id_start_language = excel_tool.get_max_value(key="id", table_object_detail=repeatable_challenge_language_detail) + 1
    key = "autoId"
    autoId_start = excel_tool.get_max_value(key=key, table_object_detail=repeatable_challenge_detail) + 1
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=repeatable_challenge_detail)
    template_groupId = 5042001
    template_autoId = 101
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId, table_data_detail=repeatable_challenge_detail)

    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)

    cur = 0
    while cur < 6:
        instance_object: REPEATABLE_CHALLENGE
        instance_object = json_to_instance(json_object=json_object_list[cur], cls=REPEATABLE_CHALLENGE)
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.autoId = autoId_start + cur
        instance_object.groupId = groupId
        instance_object.redirectionParams[0] = fishery_id
        instance_object.triggerKeyM = fishery_id
        instance_object.triggerKeyS = fish_id_list[-(6 - cur)]
        instance_object.rewards[0].itemId = tokenID

        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value= instance_object.autoId, table_data_detail=repeatable_challenge_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value= instance_object.autoId, table_data_detail=repeatable_challenge_detail, instance_object=instance_object)

        # 多语言
        instance_object_language: REPEATABLE_CHALLENGE_LANGUAGE
        json_object, instance_object_language = excel_tool.get_object(key="autoId", value=instance_object.autoId, table_data_detail=repeatable_challenge_language_detail, cls=REPEATABLE_CHALLENGE_LANGUAGE)
        if instance_object_language:
            mode_language = 0
        else:
            _, instance_object_language = excel_tool.get_object(key="autoId", value=template_autoId, table_data_detail=repeatable_challenge_language_detail, cls=REPEATABLE_CHALLENGE_LANGUAGE)
            instance_object_language.id = id_start_language + cur
            mode_language = 1
        instance_object_language.autoId = instance_object.autoId
        fishery_name = excel_tool.get_fishery_name(fishery_id=fishery_id)
        fish_name = excel_tool.get_fish_name(fish_id=instance_object.triggerKeyS)
        instance_object_language.name = instance_object.name
        instance_object_language.t_missiontype = f"{fishery_name}的怪物"
        instance_object_language.t_missionname = fishery_name
        instance_object_language.t_missiondes = f"{fishery_name}最受青睐的{fish_name}"

        print(instance_object_language)
        if mode_language == 0:
            excel_tool.change_object(key=key, value= instance_object_language.autoId, table_data_detail=repeatable_challenge_language_detail, instance_object=instance_object_language)
        else:
            excel_tool.add_object(key=key, value= instance_object_language.autoId, table_data_detail=repeatable_challenge_language_detail, instance_object=instance_object_language)
        cur += 1


def three_fish_main(excel_tool: ExcelToolsForActivities, fishery_id, groupId_three_fish, fishOffset_list, activityRankTitle, displayBanner):
    three_fish_main_detail = excel_tool.get_table_data_detail(book_name="THREE_FISH_MAIN.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=three_fish_main_detail) + 1
    key = "groupId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId_three_fish, table_data_detail=three_fish_main_detail)
    template_groupId_three_fish = 5200010
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=template_groupId_three_fish, table_data_detail=three_fish_main_detail)
    instance_object: THREE_FISH_MAIN
    instance_object = json_to_instance(json_object=json_object_list[0], cls=THREE_FISH_MAIN)
    if mode == 1:
        instance_object.id = id_start
    instance_object.groupId = groupId_three_fish
    instance_object.fishSceneTpId = fishery_id
    instance_object.activityRankTitle = activityRankTitle
    instance_object.activityRankDescTitle = instance_object.activityRankTitle
    instance_object.displayBanner = displayBanner
    instance_object.fishIdNew = []
    instance_object.fishOffset = []
    fish_id_list = excel_tool.get_fish_id_list(fishery_id=fishery_id)
    cur = 0
    while cur < len(fishOffset_list):
        fish_offset = ThreeFishOffset()
        if "offsetX" in fishOffset_list[cur]:
            fish_offset.offsetX = fishOffset_list[cur]["offsetX"]
        if "offsetY" in fishOffset_list[cur]:
            fish_offset.offsetY = fishOffset_list[cur]["offsetY"]
        if "scale" in fishOffset_list[cur]:
            fish_offset.scale = fishOffset_list[cur]["scale"]
        if "cardScale" in fishOffset_list[cur]:
            fish_offset.cardScale = fishOffset_list[cur]["cardScale"]
        if "cardOffsetX" in fishOffset_list[cur]:
            fish_offset.cardOffsetX = fishOffset_list[cur]["cardOffsetX"]
        if "cardOffsetY" in fishOffset_list[cur]:
            fish_offset.cardOffsetY = fishOffset_list[cur]["cardOffsetY"]
        instance_object.fishOffset.append(fish_offset)
        instance_object.fishIdNew.append(fish_id_list[-(4 - cur)])
        cur += 1
    print(instance_object)
    if mode == 0:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=three_fish_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=three_fish_main_detail, instance_object=instance_object)

def three_fish_rank_reward(excel_tool: ExcelToolsForActivities, fishery_id, groupId_three_fish):
    three_fish_rank_reward_detail = excel_tool.get_table_data_detail(book_name="THREE_FISH_RANK_REWARD.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=three_fish_rank_reward_detail) + 1
    tpId_start = excel_tool.get_max_value(key="tpId", table_object_detail=three_fish_rank_reward_detail) + 1
    key = "tpId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_three_fish, table_data_detail=three_fish_rank_reward_detail)
    template_groupId_three_fish = 5200010
    if json_object_list:
        mode = 0
    else:
        mode = 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=template_groupId_three_fish, table_data_detail=three_fish_rank_reward_detail)
    instance_id_list = json_list_to_instance_list(json_object_list=json_object_list, cls=THREE_FISH_RANK_REWARD)
    cur = 0
    while cur < len(instance_id_list):
        instance_object: THREE_FISH_RANK_REWARD
        instance_object = instance_id_list[cur]
        if mode == 1:
            instance_object.id = id_start + cur
            instance_object.tpId = tpId_start + cur
        instance_object.groupId = groupId_three_fish
        instance_object.threeFishRankReward[0].itemId = excel_tool.change_fish_bag_fishery(fish_bag_id=instance_object.threeFishRankReward[0].itemId, fishery_id=fishery_id)
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=three_fish_rank_reward_detail , instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=three_fish_rank_reward_detail , instance_object=instance_object)
        cur += 1

def timer_main(excel_tool: ExcelToolsForActivities, fishery_id, open_time,  returnTimerId, TimerId, chapterTimerId):
    key = "timerID"
    def doubleweek_back():
        # 双周返场
        timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
        id_start = excel_tool.get_max_value(key="id", table_object_detail=timer_main_detail) + 1

        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=returnTimerId, table_data_detail=timer_main_detail)
        if json_object_list:
            mode = 0
            instance_object = json_to_instance(json_object=json_object_list[0], cls=TIMER_MAIN)
        else:
            mode = 1
            instance_object = TIMER_MAIN()
            instance_object.id = id_start
        instance_object.name = f"{fishery_id}双周返场活动"
        instance_object.timerID = returnTimerId
        instance_object.timerName = instance_object.name
        instance_object.cycleType = 1
        instance_object.openTime = open_time
        instance_object.endTime = commonTools.get_time(time=open_time, days=7, seconds=-1)
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)

    # 假双周
    def doubleweek():
        timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
        id_start = excel_tool.get_max_value(key="id", table_object_detail=timer_main_detail) + 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=TimerId, table_data_detail=timer_main_detail)
        if json_object_list:
            mode = 0
            instance_object = json_to_instance(json_object=json_object_list[0], cls=TIMER_MAIN)
        else:
            mode = 1
            instance_object = TIMER_MAIN()
            instance_object.id = id_start
        instance_object.name = f"{fishery_id}双周活动"
        instance_object.timerID = TimerId
        instance_object.timerName = instance_object.name
        instance_object.cycleType = 1
        instance_object.openTime = commonTools.get_time(time=open_time, days=-207)
        instance_object.endTime = commonTools.get_time(time=open_time, days=-200, seconds=-1)
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)

    # 假闪卡
    def flash_card():
        timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
        id_start = excel_tool.get_max_value(key="id", table_object_detail=timer_main_detail) + 1
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=chapterTimerId, table_data_detail=timer_main_detail)
        if json_object_list:
            mode = 0
            instance_object = json_to_instance(json_object=json_object_list[0], cls=TIMER_MAIN)
        else:
            mode = 1
            instance_object = TIMER_MAIN()
            instance_object.id = id_start
        instance_object.name = f"{fishery_id}双周闪卡"
        instance_object.timerID = chapterTimerId
        instance_object.timerName = instance_object.name
        instance_object.cycleType = 1
        instance_object.openTime = open_time
        instance_object.endTime = "2034-12-26 23:59:59"
        print(instance_object)
        if mode == 0:
            excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)

    doubleweek_back()
    if TimerId:
        doubleweek()
    flash_card()



def main():
    cfg = {
        "internal_or_global": "internal",    # 国内还是海外 (item_main_language)
        "fishery_id": 400319,                # 渔场id
        "open_time": "2025-05-02 00:00:00",  # 活动开始时间 (timer_main)
        "missionType": 72,                   # 任务类型 (mission_group, mission_main)
        "collectionChapterId": 9,           # 闪卡章节 (activity_double_week)
        "TimerId": None,                   # 双周时间id (activity_double_week, timer_main)
        "chapterTimerId": 102051,            # 闪卡开启时间 (activity_double_week, timer_main)
        "returnTimerId": 151209,             # 返场时间id (activity_double_week, battle_pass_main_2024, mission_group, timer_main) ×
        "groupId": 5100048,                  # 返场活动的groupId (event_endless_sale, event_n_day_tasks_leaderboard, event_n_day_tasks_milestone, mission_group, repeatable_challenge)
        "groupId_battle_pass": 31,           # battle_pass表里的groupId (battle_pass_main_2024, battle_pass)
        "groupId_three_fish": None,       # 三鱼榜的groupId (mission_group, three_fish_main, three_fish_rank_reward)
        "icon_name": "B09",                  # 图标的特殊后缀 (activity_double_week, item_main)
        "paymentGiftId_start": 2510085,      # paymentGiftId开始 (activity_double_week)
        "activityFisheryNameId": 19960006,   # 活动名的id (activity_double_week, battle_pass_main_2024, panel_static_language, mission_group, three_fish_main, mission_main)
        "activityFisheryNameId_return": 1998226,
        "wildCardId": 240130,                # 万能卡id (activity_double_week, collection_exchange_store, item_main, item_main_language)
        "tokenID": 260074,                   # ndays积分币 可填None(event_n_day_tasks_milestone, item_main, item_main_language, mission_main, repeatable_challenge) ×
        "notShowBeforeReturn": 0,            # 返场前隐藏 (activity_double_week)
        "activityFisheryName_return": "漫溯乌苏里",   # 活动名 (item_main_language, panel_static_language)
        "imgNameInner": "ActivityTasks_banner_bg_40",                 # 活动内的背景 (mission_group)
        "newNDaysImgName": "ActivityTasks_ndays_logo_wslj",          # (battle_pass_main_2024, mission_group)
        "big_reward": {"tpId": 1104011, "itemType": 11, "count": 1},  # 闪卡集齐大奖 (collection_reward)
        "displayBanner": "activitycarnival_njld/ActivityCarnival_njld_leaderboard_tittle",        # 三鱼排行榜banner (three_fish_main)
        "fishOffset_list": [
            {"offsetX": 122, "offsetY": 3, "scale": 1, "cardOffsetX": 8, "cardOffsetY": 47, "cardScale": 0.55},
            {"offsetX": 116, "offsetY": -2, "scale": 1, "cardOffsetX": -2, "cardOffsetY": 50, "cardScale": 0.54},
            {"offsetX": 122, "offsetY": None, "scale": 1, "cardOffsetX": None, "cardOffsetY": 43, "cardScale": 0.55},
        ],                                                            # 排行榜上鱼的位置偏移和缩放 (three_fish_main)
    }

    excel_tool = ExcelToolsForActivities(EXCEL_PATH)

    activity_double_week(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], chapterID=cfg["collectionChapterId"], TimerId=cfg["TimerId"], icon_name=cfg["icon_name"], paymentGiftId_start=cfg["paymentGiftId_start"], activityFisheryNameId=cfg["activityFisheryNameId"], wildCardId=cfg["wildCardId"], chapterTimerId=cfg["chapterTimerId"], returnTimerId=cfg["returnTimerId"], notShowBeforeReturn=cfg["notShowBeforeReturn"])
    battle_pass_main_2024(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId_battle_pass=cfg["groupId_battle_pass"], returnTimerId=cfg["returnTimerId"], newNDaysImgName=cfg["newNDaysImgName"], activityFisheryNameId=cfg["activityFisheryNameId_return"])
    battle_pass(excel_tool=excel_tool, groupId_battle_pass=cfg["groupId_battle_pass"])
    collection_base(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], collectionChapterId=cfg["collectionChapterId"])
    collection_energy_cost_debuff(excel_tool=excel_tool, fishery_id=cfg["fishery_id"])
    collection_exchange_store(excel_tool=excel_tool,  fishery_id=cfg["fishery_id"], collectionChapterId=cfg["collectionChapterId"], wildCardId=cfg["wildCardId"])
    collection_reward(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], collectionChapterId=cfg["collectionChapterId"], big_reward=cfg["big_reward"])
    event_endless_sale(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId=cfg["groupId"])
    event_n_day_tasks_leaderboard(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId=cfg["groupId"])
    event_n_day_tasks_milestone(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId=cfg["groupId"], tokenID=cfg["tokenID"])
    item_main(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], wildCardId=cfg["wildCardId"], icon_name=cfg["icon_name"], tokenID=cfg["tokenID"])
    item_main_language(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], wildCardId=cfg["wildCardId"], tokenID=cfg["tokenID"], activityFisheryName=cfg["activityFisheryName_return"], internal_or_global=cfg["internal_or_global"])
    mission_group(excel_tool=excel_tool, groupId=cfg["groupId"], TimerId=cfg["returnTimerId"], groupId_three_fish=cfg["groupId_three_fish"], fishery_id=cfg["fishery_id"], activityName=cfg["activityFisheryNameId_return"], imgNameInner=cfg["imgNameInner"], missionType=cfg["missionType"], newNDaysImgName=cfg["newNDaysImgName"])
    mission_main(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId=cfg["groupId"], missionType=cfg["missionType"], tokenID=cfg["tokenID"])
    panel_static_language(excel_tool=excel_tool, t_panellanguage=cfg["activityFisheryName_return"])
    repeatable_challenge(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId=cfg["groupId"], tokenID=cfg["tokenID"])
    timer_main(excel_tool=excel_tool, open_time=cfg["open_time"], fishery_id=cfg["fishery_id"], returnTimerId=cfg["returnTimerId"], TimerId=cfg["TimerId"], chapterTimerId=cfg["chapterTimerId"])
    if cfg["groupId_three_fish"]:
        three_fish_main(excel_tool=excel_tool, fishery_id=cfg["fishery_id"], groupId_three_fish=cfg["groupId_three_fish"], fishOffset_list=cfg["fishOffset_list"], activityRankTitle=cfg["activityFisheryNameId_return"], displayBanner=cfg["displayBanner"])
        three_fish_rank_reward(excel_tool=excel_tool, fishery_id=cfg["fishery_id"],groupId_three_fish=cfg["groupId_three_fish"])

if __name__ == '__main__':
    main()
