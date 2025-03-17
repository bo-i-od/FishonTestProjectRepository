import re

from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll, fishingMsg
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


if __name__ == '__main__':
    base_page = BasePage(serial_number="127.0.0.1:21593", is_mobile_device=False)
    # base_page.sleep(3)
    # base_page.go_to_panel("AchievementPanel")
    base_page.is_time_scale = True
    base_page.custom_cmd("setQuickQTE 1")
    base_page.tension_default = 0.65
    base_page.custom_cmd("setTension 0.65")
    base_page.is_quick_qte = True
    #
    # # # 跳过引导
    # gameInit.guide_skip(base_page)
    #
    # #
    # base_page.cmd_list(["levelupto 21"])
    # # #
    # # # # # # 新主线升到指定等级
    # level_up_to_new_plot(base_page, 60)
    # # #
    # # # 完成新主线剧情任务
    # quest_done(base_page)

    # 天赋满级
    # talent_all(base_page)

    # 装备满级满星
    # full_gear(base_page)

    # 鱼卡满级
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
    battleTest.fish_once(base_page, is_quick=False, fish_id="360113")

    # 循环钓鱼 运行界面：备战界面
    # 填渔场id会将该渔场鱼钓一遍
    # battleTest.circulate_fish(base_page, is_quick=False, fishery_id="400304", start=13)

    # 体感抛竿
    # battleTest.vibration_cast(base_page)

    # 设定指定对决杯数
    # duelTest.set_duelcup(base_page, 3990)

    # 对决一次 运行界面：对决大厅界面
    # rank0-7代表黑铁到传奇
    # duelTest.duel_once(base_page, rank=0)

    # 该渔场闪卡获得一张
    # flashCardTest.get_flash_card(base_page, fishery_id="500301")

    # 任意界面接口钓鱼 1021
    # fish_quick(base_page, fish_id=360101, is_map=False, times=1)

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
