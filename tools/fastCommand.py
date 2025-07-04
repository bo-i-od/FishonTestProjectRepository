import re
import time

from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll, fishingMsg
from panelObjs import BattlePanel
from panelObjs.ChallengeMainStagePanel import ChallengeMainStagePanel
from panelObjs.MainStageSettlePanel import MainStageSettlePanel
from panelObjs.RogueMainStagePanel import RogueMainStagePanel
from panelObjs.RogueResultPanel import RogueResultPanel
from scripts import battleTest, duelTest, gearTest, fishCardTest, flashCardTest, createUsers
from tools import commonTools



def quest_done(bp: BasePage):
    table_data_detail = bp.excelTools.get_table_data_detail(book_name="NEW_PLOT_QUEST.xlsm")
    table_data_object_list, _, _ = table_data_detail
    table_data_object = table_data_object_list[0]
    quest_id = table_data_object["tpId"]


    # # 发送消息
    # lua_code = csMsgAll.get_CSQuestCancelNewMsg(questTpId=quest_id)
    # bp.lua_console(lua_code)
    # bp.sleep(0.1)
    while True:

        # bp.cmd(f"questFinish {quest_id}")

        if "nextQuestId" not in table_data_object:
            break
        # if table_data_object["nextQuestId"] == 80000047:
        #     break
        bp.cmd(f"questFinish {quest_id}")
        bp.sleep(0.1)

        # 发送消息
        lua_code = csMsgAll.get_CSGetQuestRewardsMsg(questTpId=quest_id)
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        quest_id = table_data_object["nextQuestId"]
        table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=quest_id, table_data_detail=table_data_detail)


def talent_all(bp: BasePage):
    bp.cmd("talentall")


def full_gear(bp: BasePage):
    # 旧装备升级
    bp.cmd("allrod 500")
    bp.sleep(1)
    bp.set_item_count(target_count=10000000000, item_tpid="100000")
    bp.set_item_count(target_count=10000000, item_tpid="200300")
    gearTest.full_star(bp)
    gearTest.full_level(bp)

    # 新装备


def unlock_fish_album(bp: BasePage, fishery_id):
    fish_id_list = bp.get_fish_id_list(fishery_id=fishery_id)
    for fish_id in fish_id_list:
        fish_quick(bp, fish_id=fish_id)
        bp.sleep(0.1)


def achievement_done(bp):
    bp.cmd("missiondone 10")


def wanted_done(bp: BasePage, fishery_id):
    fishery_id = int(fishery_id)
    table_data_object_list = bp.excelTools.get_table_data_object_list_by_key_value(key="fishery", value=fishery_id,book_name="ACHIEVEMENT_WANTED.xlsm")
    fish_id_set = set()
    for table_data_object in table_data_object_list:
        if "fishery" not in table_data_object:
            continue
        if table_data_object["fishery"] != fishery_id:
            continue
        if "isOpen" not in table_data_object:
            continue

        fish_id_list = table_data_object["target"]
        fish_id_set.update(fish_id_list)
    for fish_id in fish_id_set:
        fish_quick(bp, fish_id=fish_id, is_map=True)
        bp.sleep(0.1)


def category_done(bp: BasePage, category_id):
    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="TPID", value=category_id, book_name="ACHIEVEMENT_CATEGORY.xlsm")
    fish_list = table_data_object["fishList"]
    for fish in fish_list:
        if "fish" not in fish:
            continue
        fish_id = fish["fish"]
        fish_quick(bp, fish_id=fish_id)


def fish_quick(bp: BasePage, fish_id, is_map=False, times=1):
    if times > 1:
        times -= 1
        fish_quick(bp=bp, fish_id=fish_id, is_map=is_map, times=times)
    if fish_id in [0, "0"]:
        return
    fishery_id = bp.fish_id_to_fishery_id(fish_id=fish_id)
    spot_id_list, is_in_double_week, is_new_plot = bp.get_spot_id_list(fishery_id=fishery_id)
    spot_id = spot_id_list[0]
    map_id = 399001
    is_limited = False
    scene_type = 1
    if is_new_plot:
        map_id = 399002
        is_limited = True
        scene_type = 4
    bp.custom_cmd(f"setSceneType {scene_type}")
    if not is_map:
        bp.cmd(f"mode {fishery_id} {fish_id}")
        bp.sleep(0.1)
        fishingMsg.fish(bp, [{"spot_id": f"{spot_id}", "times": 1,  "is_activity_spot": is_in_double_week}])
        return

    spot_id_list = list(set(spot_id_list) & set(bp.fish_id_to_spot_id(fish_id=fish_id)))
    is_bone = False
    bone_id = 0

    bp.cmd(f"mode {fishery_id} {map_id}")
    bp.sleep(0.1)
    fishingMsg.fish(bp, [{"spot_id": f"{spot_id}", "times": 1, "is_activity_spot": is_in_double_week}])
    bp.sleep(0.1)

    for spot_id_temp in spot_id_list:
        drop_item_id_list = bp.get_drop_item_id_list(spot_id=spot_id_temp)
        for drop_item_id in drop_item_id_list:
            fish_id_temp = bp.fish_bone_id_to_fish_id(fish_bone_id=drop_item_id)
            is_target = fish_id_temp == str(fish_id)
            is_gold = str(drop_item_id)[0:2] == "37" or str(drop_item_id)[0:3] == "385"

            if is_target and is_gold:
                is_bone = True
                bone_id = drop_item_id
                spot_id = spot_id_temp
                break
        if is_bone:
            break

    if is_bone:
        bp.cmd(f"mode {fishery_id} {bone_id}")
        bp.sleep(0.1)
        fishingMsg.fish(bp, [{"spot_id": f"{spot_id}", "times": 1, "is_activity_spot": is_in_double_week, "is_limited": is_limited}])
        bp.sleep(0.1)

    bp.cmd(f"mode {fishery_id} {fish_id}")
    bp.sleep(0.1)
    fishingMsg.fish(bp, [{"spot_id": f"{spot_id}", "times": 1, "is_activity_spot": is_in_double_week, "is_limited": is_limited}])


def level_up_to_new_plot(bp: BasePage, level, tp_id="102600"):
    item_count = bp.get_item_count(item_tpid=tp_id)
    table_data_object_list = bp.excelTools.get_table_data_object_list(book_name="NEW_PLOT_LEVEL_UP.xlsm")
    exp = 0
    for table_data_object in table_data_object_list:
        if table_data_object["level"] > level:
            break
        if "exp" not in table_data_object:
            continue
        exp += table_data_object["exp"]
    if item_count >= exp:
        return
    bp.cmd(f"add 1 {tp_id} {exp - item_count}")


def tower_level_up(bp: BasePage, tag, lv):
    cur = 0
    while cur < lv:
        RogueMainStagePanel.click_btn_challenge(bp)
        bp.sleep(1)
        bp.cmd(f"towerPass 1 {tag} 3 10000")
        bp.sleep(4)
        RogueResultPanel.click_btn_orange(bp)
        bp.sleep(1)
        RogueMainStagePanel.panel_tips_up.click_btn_close(bp)
        bp.sleep(1)
        cur += 1

def challenge(bp: BasePage, times=100):
    cur = 0
    while cur < times:
        ChallengeMainStagePanel.click_btn_orange(bp)
        battleTest.fish_once(bp, is_quick=False)
        MainStageSettlePanel.click_btn_blue(bp)
        bp.sleep(1)
        cur += 1


def dialog_show(bp: BasePage, start_quest_id:int):
    table_data_detail = bp.excelTools.get_table_data_detail(book_name="NEW_PLOT_QUEST.xlsm")
    table_data_object_list, _, _ = table_data_detail
    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=start_quest_id, table_data_detail=table_data_detail)
    quest_id = start_quest_id
    title = "Complete"
    count = 0

    while True:

        if count != 0 and "endStoryId" in table_data_object:
            target_log = bp.receive_until_get_msg(msg_name="", key_sc=title, timeout=50)
            # print(bp.log_list)
        count+=1
        # print(bp.log_list)
        # if interact_mode:
        #     if not continue_dialog(): break

        if "showStoryId" in table_data_object:
            story_id = table_data_object["showStoryId"]
            bp.cmd(f"dialog {story_id}")
            bp.log_list.clear()
            print(story_id)

            bp.sleep(0.1)
            target_log = bp.receive_until_get_msg(msg_name="", key_sc=title, timeout=50)
            # print(bp.log_list)

        # if interact_mode:
        #     if not continue_dialog(): break

        if "endStoryId" in table_data_object:
            story_id = table_data_object["endStoryId"]
            bp.cmd(f"dialog {story_id}")
            bp.log_list.clear()
            print(story_id)
            bp.sleep(0.2)

        if "nextQuestId" not in table_data_object:
            break

        quest_id = table_data_object["nextQuestId"]
        table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=quest_id,
                                                                             table_data_detail=table_data_detail)
def quest_start_to_end(bp: BasePage, start_quest_id: int, end_quest_id: int):
    table_data_detail = bp.excelTools.get_table_data_detail(book_name="NEW_PLOT_QUEST.xlsm")
    table_data_object_list, _, _ = table_data_detail
    table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=start_quest_id, table_data_detail=table_data_detail)

    quest_id = start_quest_id

    while True:
        if "nextQuestId" not in table_data_object:
            break
        if table_data_object["nextQuestId"] == end_quest_id:
            break
        bp.cmd(f"questFinish {quest_id}")
        bp.sleep(1)

        # 发送消息
        lua_code = csMsgAll.get_CSGetQuestRewardsMsg(questTpId=quest_id)
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        quest_id = table_data_object["nextQuestId"]
        table_data_object = bp.excelTools.get_table_data_object_by_key_value(key="tpId", value=quest_id, table_data_detail=table_data_detail)

#使用该函数前，需要使用 setQuest {quest_id} 命令, 设置当前任务为最后一个任务
def clue_start_to_end(bp: BasePage, start_clue_id: int, end_clue_id: int):
    table_data_detail = bp.excelTools.get_table_data_detail(book_name="NEW_PLOT_CLUE_STATE")
    table_data_object_list, _, _ = table_data_detail

    # 按clueStateId排序，防止无序
    table_data_object_list = sorted(table_data_object_list, key=lambda x: x['clueStateId'])

    # 遍历所有clueStateId介于start和end之间（含端点）的项
    for clue_obj in table_data_object_list:
        clue_id = clue_obj['clueStateId']
        if start_clue_id <= clue_id <= end_clue_id:
            bp.cmd(f"cubeGet 500304 {clue_id}")
            bp.sleep(1)
            print(f"当前clue_id: {clue_id}")

if __name__ == '__main__':
    base_page = BasePage(serial_number="127.0.0.1:21593", is_mobile_device=False)
    # base_page.cmd_list(["mode 500301 360107"])
    #
    base_page.is_time_scale = False
    base_page.time_scale_default = 5
    base_page.set_time_scale(base_page.time_scale_default)
    # base_page.set_is_quick_qte(True)
    # base_page.set_object_active(active=False, element_data={"locator": "UICanvas>Default>EventPanel_N_DAYS_10>Panel>panel_right>tab>Scroll View>Viewport>content>day_1(Clone)>lock"})
    # base_page.cmd("mode 500301 360101")
    # gameInit.set_joystick(base_page)
    # BattlePanel.hold_btn_reel(base_page)
    # base_page.cmd("clone 1000002002")
    #
    #
    #
    # base_page.cmd_list(["levelupto 101","add 1 100500 10000000", "guideskip"])
    # base_page.sleep(1)
    # # # # # 跳过引导
    # gameInit.guide_skip(base_page)
    # base_page.set_item_count(target_count=10000, item_tpid="100500")
    # base_page.set_item_count(target_count=0, item_tpid="101500")
    # # # # # # #
    # # # # # # # #
    #
    # # # # # #
    # # # # # # # 新主线升到指定等级
    # level_up_to_new_plot(base_page, 99)
    # # # # # # # # # #
    # # # # # # # # # # 完成新主线剧情任务
    # quest_done(base_page)
    # # # # #
    # # # # 天赋满级
    # # talent_all(base_page)
    # # # #
    # # # # # 装备满级满星
    # # full_gear(base_page)
    # # # # #
    # # # # # # 鱼卡满级
    # fishCardTest.fish_card_one_key_level_up(base_page)

    # 指定渔场渔册满
    # unlock_fish_album(base_page, fishery_id=400302)

    # 完成全部成就gg
    # achievement_done(base_page)

    # 照片墙 奇珍黄金鱼没有鱼骨 该方法完成不了a
    # wanted_done(base_page, fishery_id=400303)

    # 鱼种
    # category_done(base_page, category_id=10004)

    # # 钓一次鱼 运行界面：备战界面
    # base_page.cmd("mode 500301 360113")
    # battleTest.fish_once(base_page, is_quick=True, fish_id=360115)

    # 循环钓鱼 运行界面：备战界面
    # 填渔场id会将该渔场鱼钓一遍
    # base_page.cmd("mode 500301 360115")

    # battleTest.circulate_fish(base_page, is_quick=False, fishery_id="500301")


    # 钓者挑战打times关
    challenge(base_page, times=10)

    # 体感抛竿
    # battleTest.vibration_cast(base_page)

    # 设定指定对决杯数
    # duelTest.set_duelcup(base_page, 3990)

    # 对决一次 运行界面：对决大厅界面
    # rank0-7代表黑铁到传奇
    # duelTest.duel_once(base_page, rank=1)

    # 该渔场闪卡获得一张
    # flashCardTest.get_flash_card(base_page, fishery_id="400319")

    # 任意界面接口钓鱼 1021
    # fish_quick(base_page, fish_id=350114, is_map=False, times=1)

    # 设定道具数量
    # base_page.set_item_count(item_tpid="102100", target_count=10)

    # 读取道具数量
    # print(base_page.get_item_count(item_tpid="103100"))

    # 发送gm命令
    # base_page.cmd("levelupto 51")

    # 获取鱼体型
    # print(base_page.get_fish_type(fish_tpid="390005"))

    # 爬塔难度升若干级，在RogueMainStagePanel界面运行
    # tag 1强壮 2敏捷 3多变
    # tower_level_up(base_page, tag=1, lv=1)

    # base_page.lua_console('PanelMgr:OpenPanel("HomePanelNew")')

    # createUsers.logout(base_page)

    base_page.connect_close()
