import re
from common.basePage import BasePage
from netMsg import csMsgAll, fishingMsg
from scripts import battleTest, duelTest, gearTest, fishCardTest, flashCardTest


def guide_skip(bp: BasePage):
    text = bp.lua_console_with_response(lua_code_return="_G.PassiveNewbieGuideEnum")
    pattern = '"([^"]*)"'
    result = re.findall(pattern, text)
    lua_code_list = []
    for r in result:
        lua_code = csMsgAll.get_CSNewGuideStoreMsg(key=r)
        lua_code_list.append(lua_code)
    bp.lua_console_list(command_list=lua_code_list)


def talent_all(bp: BasePage):
    bp.cmd("talentall")


def full_gear(bp: BasePage):
    bp.cmd("allrod 500")
    bp.sleep(1)
    bp.set_item_count(target_count=10000000000, item_tpid="100000")
    bp.set_item_count(target_count=10000000, item_tpid="200300")
    gearTest.full_star(bp)
    gearTest.full_level(bp)


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


def fish_quick(bp: BasePage, fish_id, is_map=False):
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




if __name__ == '__main__':
    base_page = BasePage()

    # # 跳过引导
    # guide_skip(base_page)

    # 天赋满级
    # talent_all(base_page)

    # 装备满级满星
    # full_gear(base_page)

    # 鱼卡满级
    # fishCardTest.fish_card_one_key_level_up(base_page)

    # 指定渔场渔册满
    # unlock_fish_album(base_page, fishery_id=400302)

    # 完成全部成就
    # achievement_done(base_page)

    # 照片墙 奇珍黄金鱼没有鱼骨 该方法完成不了
    # wanted_done(base_page, fishery_id=400302)

    # 鱼种
    # category_done(base_page, category_id=10004)

    # # 钓一次鱼 运行界面：备战界面
    # battleTest.fish_once(base_page, is_quick=False)

    # 循环钓鱼 运行界面：备战界面
    # 填渔场id会将该渔场鱼钓一遍
    # battleTest.circulate_fish(base_page, is_quick=True, times=100)

    # 体感抛竿
    # battleTest.vibration_cast(base_page)

    # 设定指定对决杯数
    # duelTest.set_duelcup(base_page, 3000)

    # 对决一次 运行界面：对决大厅界面
    # rank0-7代表黑铁到传奇
    # duelTest.duel_once(base_page, rank=1)

    # 该渔场闪卡获得一张
    # flashCardTest.get_flash_card(base_page, fishery_id="400302")

    # 任意界面接口钓鱼
    # fish_quick(base_page, fish_id=350115, is_map=False)

    base_page.connect_close()
