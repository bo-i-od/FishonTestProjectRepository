import os
import sys

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
from activities.fishery.temp.main_id import load_main_id, save_main_id
from tools import commonTools, baseDataRead
from tools.excelRead import ExcelToolsForActivities
from tools.decl2py import *

"""
    这个是没有开过双周活动的单周配置模板
"""

def activity_double_week(excel_tool: ExcelToolsForActivities,fishery_id, chapterID, icon_name, paymentGiftId_start, activityFisheryNameId, returnTimerId,open_time,internal_or_global,notShowBeforeReturn, wildCardId=None):
    # paymentGiftId_cfg = {
    #     500021: {"paymentGiftId_start": 2510096, "paymentGiftId_count": 10},
    #     500023: {"paymentGiftId_start": 2510085, "paymentGiftId_count": 10},
    #     500024: {"paymentGiftId_start": 2510117, "paymentGiftId_count": 10},
    #     500026: {"paymentGiftId_start": 2510075, "paymentGiftId_count": 10},
    #     500028: {"paymentGiftId_start": 2510039, "paymentGiftId_count": 10},
    #     500029: {"paymentGiftId_start": 2510064, "paymentGiftId_count": 10},
    #        }
    key = "tpId"
    tpId = 10000000 + fishery_id
    activity_double_week_detail = excel_tool.get_table_data_detail(book_name="ACTIVITY_DOUBLE_WEEK.xlsm")
    template_tpId = 10400310
    # mode = 1 新增, mode = 2 替换
    if excel_tool.get_table_data_object_list_by_key_value(key=key, value=tpId, table_data_detail=activity_double_week_detail):
        template_tpId = tpId
        mode = 2
    else:
        mode = 1

    instance_object: ACTIVITY_DOUBLE_WEEK
    json_object, instance_object = excel_tool.get_object(key="tpId", value=template_tpId, table_data_detail=activity_double_week_detail, cls=ACTIVITY_DOUBLE_WEEK)
    fisheries_language_detail = excel_tool.get_table_data_detail(book_name="FISHERIES_LANGUAGE.xlsm")
    if mode == 1:
        instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=activity_double_week_detail) + 1
    if notShowBeforeReturn:
        TimerId, chapterTimerId = timer_main(excel_tool=excel_tool, open_time=open_time, fishery_id=fishery_id)
        instance_object.chapterTimerId = chapterTimerId
        instance_object.TimerId = TimerId
        instance_object.doubleRewardTimerId = TimerId
        instance_object.activityFisheryNameId = activityFisheryNameId
        wildCardId = item_main_wild_card(excel_tool=excel_tool, fishery_id=fishery_id, icon_name=icon_name, wildCardId=wildCardId)
        instance_object.wildCardId = wildCardId
        item_main_language_wild_card(excel_tool=excel_tool, fishery_id=fishery_id, internal_or_global=internal_or_global, wildCardId=wildCardId)
    else:
        timer_main(excel_tool=excel_tool, open_time=open_time, fishery_id=fishery_id, chapterTimerId=instance_object.chapterTimerId)
    if chapterID is None:
        chapterID = excel_tool.get_max_value(key="chapterID", table_object_detail=activity_double_week_detail) + 1
    instance_object.chapterID = chapterID
    instance_object.name = excel_tool.get_table_data_object_by_key_value(key="tpId", value=fishery_id, table_data_detail=fisheries_language_detail)["t_name"]
    instance_object.tpId = tpId
    instance_object.fishSceneTpId = fishery_id
    instance_object.fishSpot = [fishery_id * 100 + 1, fishery_id * 100 + 2, fishery_id * 100 + 3, fishery_id * 100 + 4]
    if notShowBeforeReturn:
        instance_object.fishSpotB = [fishery_id * 100 + 1, fishery_id * 100 + 2, fishery_id * 100 + 3, fishery_id * 100 + 4]
    else:
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

    payment_gift_id_list = []
    cur = 0
    while cur < 10:
        payment_gift_id_list.append(paymentGiftId_start + cur)
        cur += 1
    # rod_id = excel_tool.get_rod(fishery_id=fishery_id, rarity=4)[0]
    # if rod_id not in paymentGiftId_cfg:
    #     raise FileNotFoundError("没有适合该渔场的礼包配置")
    # paymentGiftId_start = paymentGiftId_cfg[rod_id]["paymentGiftId_start"]
    # paymentGiftId_count = paymentGiftId_cfg[rod_id]["paymentGiftId_count"]
    # print(f"paymentGiftId_start:{paymentGiftId_start}")
    # payment_gift_id_list = []
    # cur = 0
    # while cur < paymentGiftId_count:
    #     payment_gift_id_list.append(paymentGiftId_start + cur)
    #     cur += 1
    # while cur < 10:
    #     payment_gift_id_list.append(0)
    #     cur += 1
    instance_object.paymentGiftId = payment_gift_id_list


    instance_object.wildCardOpen = 1
    instance_object.returnId = 1
    instance_object.returnTimerId = returnTimerId
    instance_object.flashCardOrder = instance_object.chapterID
    instance_object.notShowBeforeReturn = notShowBeforeReturn
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=activity_double_week_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=activity_double_week_detail, instance_object=instance_object)
    return instance_object.chapterID, instance_object.wildCardId

def battle_pass_main_2024(excel_tool: ExcelToolsForActivities, fishery_id, returnTimerId, newNDaysImgName, activityFisheryNameId, groupId_battle_pass=None, bounsRate=None):
    battle_pass_main_2024_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS_MAIN_2024.xlsm")
    template_groupId = 21
    instance_object: BATTLE_PASS_MAIN_2024
    key = "tpId"
    if groupId_battle_pass is None:
        mode = 1
        _, instance_object = excel_tool.get_object(key="groupId", value=template_groupId, table_data_detail=battle_pass_main_2024_detail, cls=BATTLE_PASS_MAIN_2024)
        instance_object.tpId = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=battle_pass_main_2024_detail, start=1030036)
        groupId_battle_pass = excel_tool.get_max_value(key="groupId", table_object_detail=battle_pass_main_2024_detail) + 1
        instance_object.id = excel_tool.get_min_value_more_than_start(key="id", table_object_detail=battle_pass_main_2024_detail, start=132952)
    else:
        mode = 2
        _, instance_object = excel_tool.get_object(key="groupId", value=groupId_battle_pass, table_data_detail=battle_pass_main_2024_detail, cls=BATTLE_PASS_MAIN_2024)

    instance_object.name = f"{fishery_id}双周BP"
    instance_object.groupId = groupId_battle_pass
    instance_object.firstOpenTimerId = returnTimerId
    instance_object.activityBPName = f"Assets/InBundle/UI/Texture/activity_ndays/{newNDaysImgName}.png"
    instance_object.activityBPId = activityFisheryNameId
    instance_object.fisheriesId = fishery_id
    if bounsRate:
        instance_object.bounsRate = bounsRate
        instance_object.bounsRateAdvance = bounsRate
        instance_object.bounsRatePromote = bounsRate
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=battle_pass_main_2024_detail, instance_object=instance_object)

    return  instance_object.groupId

def battle_pass(excel_tool: ExcelToolsForActivities, groupId_battle_pass):
    battle_pass_detail = excel_tool.get_table_data_detail(book_name="BATTLE_PASS.xlsm")
    template_groupId = 21
    id_start = excel_tool.get_max_value(key="id", table_object_detail=battle_pass_detail) + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_battle_pass, table_data_detail=battle_pass_detail)
    key = "tpId"
    if table_data_object_list:
        mode = 2
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
        if mode == 2:
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
        # mode = 2 替换， mode = 1 新增
        if excel_tool.get_table_data_object_list_by_key_value(key=key, value=fish_id, table_data_detail=collection_base_detail):
            mode = 2
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
        if mode == 2:
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
        mode = 2
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
        if mode == 2:
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
        mode = 2
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
        if mode == 2:
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
#         mode = 2
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
        mode = 2
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
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=collection_reward_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=collection_reward_detail, instance_object=instance_object)
        cur += 1

def event_endless_sale(excel_tool: ExcelToolsForActivities, fishery_id, groupId):
    groupId_sale = groupId + 1
    event_endless_sale_detail = excel_tool.get_table_data_detail(book_name="EVENT_ENDLESS_SALE.xlsm")
    fishing_rod_detail = excel_tool.get_table_data_detail(book_name="FISHING_ROD.xlsm")
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    fisheries_detail = excel_tool.get_table_data_detail(book_name="FISHERIES.xlsm")
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_sale, table_data_detail=event_endless_sale_detail)
    template_autoId_start = 20020651
    key = "autoId"
    if table_data_object_list:
        mode = 2
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
        if mode == 2:
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
        mode = 2
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
        if mode == 2:
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
        mode = 2
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
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.autoId, table_data_detail=event_n_day_tasks_milestone_detail, instance_object=instance_object)
        cur += 1

def item_main_wild_card(excel_tool: ExcelToolsForActivities, fishery_id, icon_name, wildCardId):
    # 万能卡
    template_itemTpId = 240153
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    if wildCardId is None:
        mode = 1
        json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
        wildCardId = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=item_main_detail, start=template_itemTpId)
        instance_object.itemTpId = wildCardId
        instance_object.id = instance_object.itemTpId
    else:
        mode = 2
        instance_object: ITEM_MAIN
        json_object, instance_object = excel_tool.get_object(key=key, value=wildCardId, table_data_detail=item_main_detail, cls=ITEM_MAIN)

    instance_object.name = f"{fishery_id}万能卡"
    instance_object.iconName = f"flashcard_com_{icon_name}"
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    return wildCardId
def item_main_language_wild_card(excel_tool: ExcelToolsForActivities, fishery_id, internal_or_global, wildCardId):
    # 万能卡
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"
    instance_object: ITEM_MAIN_LANGUAGE
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=wildCardId, table_data_detail=item_main_language_detail)
    if json_object_list:
        mode = 2
        instance_object = json_to_instance(json_object=json_object_list[0], cls=ITEM_MAIN_LANGUAGE)
    else:
        mode = 1
        instance_object = ITEM_MAIN_LANGUAGE()
        instance_object.itemTpId = wildCardId
        instance_object.id = instance_object.itemTpId
    instance_object.tpId = wildCardId
    instance_object.id = instance_object.tpId
    instance_object.name = f"{fishery_id}万能卡"
    t_name = excel_tool.get_table_data_object_by_key_value(key="tpId",value=fishery_id,  book_name="FISHERIES_LANGUAGE.xlsm")["t_name"]

    if internal_or_global == "internal":
        instance_object.t_name = f"{t_name}-万能卡"
        instance_object.t_description = f"可兑换<{t_name}>闪卡册的任意一张闪卡"
    else:
        instance_object.t_name = f"{t_name} - Mystery Card"
        instance_object.t_description = f"Exchangeable for any Chrome Card from the {t_name} Chrome Card Album. "
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)

def item_main(excel_tool: ExcelToolsForActivities, fishery_id,tokenID=None):
    # 活动代币
    template_itemTpId = 291008
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    key = "itemTpId"
    if tokenID is None:
        mode = 1
        tokenID = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=item_main_detail, start=template_itemTpId)
    else:
        mode = 2
        template_itemTpId = tokenID

    instance_object: ITEM_MAIN
    json_object, instance_object = excel_tool.get_object(key=key, value=template_itemTpId, table_data_detail=item_main_detail, cls=ITEM_MAIN)
    instance_object.name = f"{fishery_id}双周返场活动代币"
    instance_object.itemTpId = tokenID
    instance_object.id = tokenID
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.itemTpId, table_data_detail=item_main_detail, instance_object=instance_object)

    return tokenID

def item_main_language(excel_tool: ExcelToolsForActivities,fishery_id, tokenID, activityFisheryName, internal_or_global):
    item_main_language_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN_LANGUAGE.xlsm")
    key = "tpId"
    # 活动代币
    template_tpId = 291008
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=tokenID, table_data_detail=item_main_language_detail)
    if table_data_object_list:
        mode = 2
        template_tpId = table_data_object_list[0][key]
    else:
        mode = 1
    instance_object: ITEM_MAIN_LANGUAGE
    json_object, instance_object = excel_tool.get_object(key=key, value=template_tpId, table_data_detail=item_main_language_detail, cls=ITEM_MAIN_LANGUAGE)
    # if mode == 1:
    #     instance_object.id = excel_tool.get_max_value(key="id", table_object_detail=item_main_language_detail) + 1
    instance_object.name = f"{fishery_id}双周返场活动代币"
    instance_object.tpId = tokenID
    instance_object.id = instance_object.tpId
    if internal_or_global == "internal":
        instance_object.t_description = f"在{activityFisheryName}中收集活动积分，赢取额外奖励。"
    else:
        instance_object.t_description = f"Collect Event Points to win extra rewards in {activityFisheryName}"
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=item_main_language_detail, instance_object=instance_object)

def mission_group(excel_tool: ExcelToolsForActivities, TimerId, is_open_three_fish, fishery_id, activityName, imgNameInner,  newNDaysImgName, missionType=None, groupId=None, groupId_three_fish=None):
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    key = "groupId"

    # ndays
    template_groupId = 5100011
    if groupId is None:
        mode = 1
        groupId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=mission_group_detail, start=template_groupId, long=2)
    else:
        mode = 2
        template_groupId = groupId

    instance_object: MISSION_GROUP
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)
    instance_object.name = f"{fishery_id}的返场活动"
    if mode == 1:
        instance_object.groupId = groupId
        instance_object.id = instance_object.groupId
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
        json_object_list = mission_group_detail[0]
        max_value = 0
        for json_object in json_object_list:
            if "missionType" not in json_object:
                continue
            if max_value > json_object["missionType"][0]:
                continue
            max_value = json_object[key]
        missionType = max_value + 1
    instance_object.missionType = missionType
    instance_object.newNDaysImgName = newNDaysImgName
    instance_object.activityName2 = None
    if server_chara_level < 40:
        instance_object.rankHouseRulesId = 1001
    else:
        instance_object.rankHouseRulesId = 1002
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

    # ndays促销
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    template_groupId += 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key=key, value=groupId + 1, table_data_detail=mission_group_detail)
    if table_data_object_list:
        mode = 2
        template_groupId = table_data_object_list[0][key]
    else:
        mode = 1
    json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId, table_data_detail=mission_group_detail, cls=MISSION_GROUP)

    instance_object.groupId = groupId + 1
    instance_object.id = instance_object.groupId
    instance_object.name = f"{fishery_id}的促销"
    instance_object.openArg = TimerId
    instance_object.closeArg = TimerId
    rod_id = excel_tool.get_rod(fishery_id=fishery_id, rarity=4)[0]
    rod_icon = excel_tool.get_table_data_object_by_key_value(key="tpId", value=rod_id, book_name="FISHING_ROD.xlsm")["displayicon"]
    instance_object.imgRodGiftpack = rod_icon
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

    # # 三鱼排行榜
    if not is_open_three_fish:
        return missionType, groupId, groupId_three_fish
    mission_group_detail = excel_tool.get_table_data_detail(book_name="MISSION_GROUP.xlsm")
    if groupId_three_fish is None:
        mode = 1
        instance_object = MISSION_GROUP()
        groupId_three_fish = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=mission_group_detail, start=template_groupId)
        instance_object.groupId = groupId_three_fish
        instance_object.id = instance_object.groupId
    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=groupId_three_fish, table_data_detail=mission_group_detail, cls=MISSION_GROUP)

    instance_object.name = "三鱼排行榜活动"
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
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=mission_group_detail, instance_object=instance_object)

    return missionType, groupId, groupId_three_fish

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
    fish_bag_detail = excel_tool.get_table_data_detail(book_name="FISH_BAG.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=mission_main_detail) + 1
    missionConditionID_start = excel_tool.get_max_value(key="missionConditionID", table_object_detail=mission_condition_detail) + 1
    table_data_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId, table_data_detail=mission_main_detail)
    if table_data_object_list:
        mode = 2
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
            fishery_detail = excel_tool.get_fishery_detail(fishery_id=fishery_id, fisheries_detail=fisheries_detail)
            fishery_living = fishery_detail["fisheriesLiving"]
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
        if mode == 2:
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
        mode = 2
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
            fishery_detail = excel_tool.get_fishery_detail(fishery_id=fishery_id, fisheries_detail=fisheries_detail)
            fishery_rank = fishery_detail["fisheriesRank"]
            fishery_living = fishery_detail["fisheriesLiving"]
            is_new_fishery = 0
            if "fisheriesType" in fishery_detail:
                is_new_fishery = 1
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
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.missionConditionID, table_data_detail=mission_condition_detail, instance_object=instance_object)
        cur += 1

def panel_static_language(excel_tool: ExcelToolsForActivities, t_panellanguage, activityFisheryNameId_return=None):
    panel_static_language_detail = excel_tool.get_table_data_detail(book_name="PANEL_STATIC_LANGUAGE.xlsm")
    key = "templateID"
    if activityFisheryNameId_return is None:
        mode = 1
        instance_object = PANEL_STATIC_LANGUAGE()
        instance_object.templateID = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=panel_static_language_detail, start=1998237)
        instance_object.id = instance_object.templateID
    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=activityFisheryNameId_return, table_data_detail=panel_static_language_detail, cls=PANEL_STATIC_LANGUAGE)
    # 标题语言

    instance_object.name = t_panellanguage
    instance_object.t_panellanguage = t_panellanguage
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.templateID, table_data_detail=panel_static_language_detail, instance_object=instance_object)
    return activityFisheryNameId_return


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
        mode = 2
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
        if mode == 2:
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


def three_fish_main(excel_tool: ExcelToolsForActivities, fishery_id, fishOffset_list, activityRankTitle, displayBanner, groupId_three_fish=None):
    three_fish_main_detail = excel_tool.get_table_data_detail(book_name="THREE_FISH_MAIN.xlsm")
    key = "groupId"
    id_start = excel_tool.get_max_value(key="id", table_object_detail=three_fish_main_detail) + 1
    template_groupId_three_fish = 5200010
    instance_object: THREE_FISH_MAIN
    if groupId_three_fish is None:
        mode = 1
        json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId_three_fish, table_data_detail=three_fish_main_detail, cls=THREE_FISH_MAIN)
        instance_object.id = id_start
        instance_object.groupId = excel_tool.get_min_value_more_than_start(key=key, table_object_detail=three_fish_main_detail, start=template_groupId_three_fish)
    else:
        mode = 2
        template_groupId_three_fish = groupId_three_fish
        json_object, instance_object = excel_tool.get_object(key=key, value=template_groupId_three_fish, table_data_detail=three_fish_main_detail, cls=THREE_FISH_MAIN)

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
        instance_object.fishIdNew.append(fish_id_list[-(3 - cur)])
        cur += 1
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.groupId, table_data_detail=three_fish_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.groupId, table_data_detail=three_fish_main_detail, instance_object=instance_object)
    return groupId_three_fish
def three_fish_rank_reward(excel_tool: ExcelToolsForActivities, fishery_id, groupId_three_fish):
    three_fish_rank_reward_detail = excel_tool.get_table_data_detail(book_name="THREE_FISH_RANK_REWARD.xlsm")
    id_start = excel_tool.get_max_value(key="id", table_object_detail=three_fish_rank_reward_detail) + 1
    tpId_start = excel_tool.get_max_value(key="tpId", table_object_detail=three_fish_rank_reward_detail) + 1
    key = "tpId"
    json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="groupId", value=groupId_three_fish, table_data_detail=three_fish_rank_reward_detail)
    template_groupId_three_fish = 5200010
    if json_object_list:
        mode = 2
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
        if mode == 2:
            excel_tool.change_object(key=key, value=instance_object.tpId, table_data_detail=three_fish_rank_reward_detail , instance_object=instance_object)
        else:
            excel_tool.add_object(key=key, value=instance_object.tpId, table_data_detail=three_fish_rank_reward_detail , instance_object=instance_object)
        cur += 1

def timer_main_return(excel_tool: ExcelToolsForActivities, fishery_id, open_time,  returnTimerId=None):
    key = "timerID"
    # 双周返场
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    if returnTimerId is None:
        mode = 1
        instance_object = TIMER_MAIN()
        returnTimerId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=timer_main_detail, start=150001)
    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=returnTimerId, table_data_detail=timer_main_detail, cls=TIMER_MAIN)

    instance_object.name = f"{fishery_id}双周返场活动"
    instance_object.timerID = returnTimerId
    instance_object.id = instance_object.timerID
    instance_object.timerName = instance_object.name
    instance_object.cycleType = 1
    instance_object.openTime = open_time
    instance_object.endTime = commonTools.get_time(time=open_time, days=7, seconds=-1)
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    return returnTimerId

def timer_main(excel_tool: ExcelToolsForActivities, fishery_id, open_time, chapterTimerId=None):
    key = "timerID"
    print(chapterTimerId)
    # 假闪卡
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    if chapterTimerId is None:
        mode = 1
        instance_object = TIMER_MAIN()
        chapterTimerId= excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=timer_main_detail, start=1150091)
        instance_object.id = chapterTimerId
    else:
        mode = 2
        json_object, instance_object = excel_tool.get_object(key=key, value=chapterTimerId, table_data_detail=timer_main_detail, cls=TIMER_MAIN)
    instance_object.timerID = chapterTimerId
    instance_object.name = f"{fishery_id}双周闪卡"
    instance_object.timerName = instance_object.name
    instance_object.cycleType = 1
    instance_object.openTime = open_time
    instance_object.endTime = "2034-12-26 23:59:59"
    print(instance_object)
    if mode == 2:
        excel_tool.change_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    else:
        excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)

    if mode == 2:
        return None, chapterTimerId
    # 假双周
    timer_main_detail = excel_tool.get_table_data_detail(book_name="TIMER_MAIN.xlsm")
    instance_object = TIMER_MAIN()
    TimerId = excel_tool.get_min_value_more_than_start(key_list=[key, "id"], table_object_detail=timer_main_detail, start=1150091)
    instance_object.timerID = TimerId
    instance_object.id = instance_object.timerID

    instance_object.name = f"{fishery_id}双周活动"
    instance_object.timerName = instance_object.name
    instance_object.cycleType = 1
    instance_object.openTime = commonTools.get_time(time=open_time, days=-207)
    instance_object.endTime = commonTools.get_time(time=open_time, days=-200, seconds=-1)
    print(instance_object)

    excel_tool.add_object(key=key, value=instance_object.timerID, table_data_detail=timer_main_detail, instance_object=instance_object)
    return TimerId, chapterTimerId


def main(excel_tool: ExcelToolsForActivities):
    """
        读写方式：新增/修改

    """
    # mode=1 新增   mode=2 修改
    mode = 2

    file_name = os.path.basename(__file__).split('.')[0]

    # 配置修改区起始
    internal_or_global = "internal"    # 国内还是海外 (item_main_language)
    fishery_id = 400309                # 渔场id
    open_time = "2025-05-16 00:00:00"  # 活动开始时间 (timer_main)
    icon_name = "B12"                  # 图标的特殊后缀 (activity_double_week, item_main)
    paymentGiftId_start= 2510117       # paymentGiftId开始 (activity_double_week)
    notShowBeforeReturn = 0            # 0 返场活动前显示闪卡  1 返场活动前隐藏闪卡
    is_open_three_fish = False         # 是否开三鱼榜
    activityFisheryName_return= "探礁南澳岛"  # 活动名 (item_main_language, panel_static_language)
    imgNameInner= "ActivityTasks_banner_bg_50"                 # 活动内的背景 (mission_group)
    newNDaysImgName= "ActivityTasks_ndays_logo_nad"          # (battle_pass_main_2024, mission_group)
    big_reward= {"tpId": 1500025, "itemType": 15, "count": 1}  # 闪卡全卡集齐大奖 (collection_reward)
    bounsRate= 3000      # 返比(battle_pass_main_2024)
    displayBanner= "activitycarnival_njld/ActivityCarnival_njld_leaderboard_tittle"        # 三鱼排行榜banner (three_fish_main)
    # 排行榜上鱼的位置偏移和缩放 (three_fish_main)
    fishOffset_list= [
        {"offsetX": 122, "offsetY": 3, "scale": 1, "cardOffsetX": 8, "cardOffsetY": 47, "cardScale": 0.55},
        {"offsetX": 116, "offsetY": -2, "scale": 1, "cardOffsetX": -2, "cardOffsetY": 50, "cardScale": 0.54},
        {"offsetX": 122, "offsetY": None, "scale": 1, "cardOffsetX": None, "cardOffsetY": 43, "cardScale": 0.55},
    ]

    # 该区域参数为None则新增
    if mode == 1:
        groupId= None                  # 返场活动的groupId (event_endless_sale, event_n_day_tasks_leaderboard, event_n_day_tasks_milestone, mission_group, repeatable_challenge)
        missionType = None                  # 任务类型 (mission_group, mission_main)
        returnTimerId= None             # 返场时间id (activity_double_week, battle_pass_main_2024, mission_group, timer_main)
        groupId_three_fish= None          # 三鱼榜的groupId (mission_group, three_fish_main, three_fish_rank_reward)
        groupId_battle_pass= None          # battle_pass表里的groupId (battle_pass_main_2024, battle_pass)
        activityFisheryNameId_return= None  # panel_static_language里的templateID 返场活动名templateID
        tokenID= None                   # ndays积分币(event_n_day_tasks_milestone, item_main, item_main_language, mission_main, repeatable_challenge)
        collectionChapterId= None            # 闪卡章节 (activity_double_week)
        wildCardId = None                    # 闪卡万能卡
    else:
        id_dict = load_main_id(file_name=file_name)
        groupId = id_dict["groupId"]
        missionType = id_dict["missionType"]
        returnTimerId = id_dict["returnTimerId"]
        groupId_three_fish = id_dict["groupId_three_fish"]
        groupId_battle_pass = id_dict["groupId_battle_pass"]
        activityFisheryNameId_return = id_dict["activityFisheryNameId_return"]
        tokenID = id_dict["tokenID"]
        collectionChapterId = id_dict["collectionChapterId"]
        wildCardId = id_dict["wildCardId"]

    # 配置修改区结束
    returnTimerId = timer_main_return(excel_tool=excel_tool, open_time=open_time, fishery_id=fishery_id, returnTimerId=returnTimerId)
    activityFisheryNameId_return = panel_static_language(excel_tool=excel_tool, t_panellanguage=activityFisheryName_return, activityFisheryNameId_return=activityFisheryNameId_return)
    missionType, groupId, groupId_three_fish = mission_group(excel_tool=excel_tool, TimerId=returnTimerId, is_open_three_fish=is_open_three_fish, fishery_id=fishery_id, activityName=activityFisheryNameId_return, imgNameInner=imgNameInner, newNDaysImgName=newNDaysImgName, missionType=missionType, groupId=groupId, groupId_three_fish=groupId_three_fish)
    tokenID = item_main(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID)
    item_main_language(excel_tool=excel_tool, fishery_id=fishery_id, tokenID=tokenID, activityFisheryName=activityFisheryName_return, internal_or_global=internal_or_global)
    collectionChapterId, wildCardId = activity_double_week(excel_tool=excel_tool, fishery_id=fishery_id, chapterID=collectionChapterId, icon_name=icon_name, paymentGiftId_start=paymentGiftId_start, activityFisheryNameId=activityFisheryNameId_return, wildCardId=wildCardId, returnTimerId=returnTimerId, open_time=open_time, notShowBeforeReturn=notShowBeforeReturn,internal_or_global=internal_or_global)
    groupId_battle_pass = battle_pass_main_2024(excel_tool=excel_tool, fishery_id=fishery_id, groupId_battle_pass=groupId_battle_pass, returnTimerId=returnTimerId, newNDaysImgName=newNDaysImgName, activityFisheryNameId=activityFisheryNameId_return, bounsRate=bounsRate)
    battle_pass(excel_tool=excel_tool, groupId_battle_pass=groupId_battle_pass)
    collection_base(excel_tool=excel_tool, fishery_id=fishery_id, collectionChapterId=collectionChapterId)
    collection_energy_cost_debuff(excel_tool=excel_tool, fishery_id=fishery_id)
    collection_exchange_store(excel_tool=excel_tool,  fishery_id=fishery_id, collectionChapterId=collectionChapterId, wildCardId=wildCardId)
    collection_reward(excel_tool=excel_tool, fishery_id=fishery_id, collectionChapterId=collectionChapterId, big_reward=big_reward)
    event_endless_sale(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId)
    event_n_day_tasks_leaderboard(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId)
    event_n_day_tasks_milestone(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)
    repeatable_challenge(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, tokenID=tokenID)
    if is_open_three_fish:
        groupId_three_fish = three_fish_main(excel_tool=excel_tool, fishery_id=fishery_id, groupId_three_fish=groupId_three_fish, fishOffset_list=fishOffset_list, activityRankTitle=activityFisheryNameId_return, displayBanner=displayBanner)
        three_fish_rank_reward(excel_tool=excel_tool, fishery_id=fishery_id,groupId_three_fish=groupId_three_fish)
    mission_main(excel_tool=excel_tool, fishery_id=fishery_id, groupId=groupId, missionType=missionType, tokenID=tokenID)

    save_main_id(file_name=file_name, id_dict={"groupId": groupId, "missionType": missionType, "returnTimerId":returnTimerId, "groupId_three_fish":groupId_three_fish, "groupId_battle_pass":groupId_battle_pass, "activityFisheryNameId_return": activityFisheryNameId_return, "tokenID": tokenID, "collectionChapterId": collectionChapterId, "wildCardId": wildCardId})
    print("涉及到的表：", list(excel_tool.data_txt_changed))


if __name__ == '__main__':
    excel_tool = ExcelToolsForActivities(EXCEL_PATH)
    main(excel_tool)
