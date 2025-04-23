from airtest.core.api import connect_device

from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll
from scripts.createUsers import login, logout

from tools import fastCommand

def gear_init(bp: BasePage):
    # 跳过引导
    bp.cmd_list(["levelupto 21", "guideskip"])
    bp.sleep(1)
    gameInit.guide_skip(bp)
    bp.sleep(1)
    bp.set_item_count(item_tpid="102700", target_count=1000000)
    bp.set_item_count(item_tpid="102800", target_count=10000000000)
    bp.set_item_count(item_tpid="102900", target_count=100000000)
    bp.set_item_count(item_tpid="103000", target_count=10000000000)
    bp.set_item_count(item_tpid="103100", target_count=10000000000)
    bp.sleep(1)
    fastCommand.level_up_to_new_plot(bp, level=99)
    bp.sleep(1)
    bp.cmd_list(["equip all"])
    bp.sleep(1)
    # bp.lua_console('PanelMgr:OpenPanel("HomePanelNew")')
    fastCommand.quest_done(bp)
    # bp.cmd("setQuest 80000031")

def gear_level(bp:BasePage, lv):
    cur = 0
    while cur < lv - 1:
        lua_code = csMsgAll.get_CSEquipPartLevelUpMsg(addition_part="cmd.type = 1", dlcId=1)
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        lua_code = csMsgAll.get_CSEquipPartLevelUpMsg(addition_part="cmd.type = 2", dlcId=1)
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        lua_code = csMsgAll.get_CSEquipPartLevelUpMsg(addition_part="cmd.type = 3", dlcId=1)
        bp.lua_console(lua_code)
        bp.sleep(0.1)
        cur += 1

def gear_star(bp, star_line_lure, star_rod):
    # 鱼线鱼饵升星

    table_data_object_list = bp.excelTools.get_table_data_object_list(book_name="ADV_GEAR_FISHING_GEAR_SHARDS.xlsm")
    for table_data_object in table_data_object_list:
        if "enabled" not in table_data_object:
            continue
        tpId = table_data_object["tpId"]
        bp.cmd(f"add 18 {tpId} 3000")
        star_max = 6
        if "qualityType" in table_data_object:
            star_max = table_data_object["qualityType"]
        if str(tpId)[3] == "1":
            star = star_rod
            tpId += 100000
        else:
            star = star_line_lure
            tpId -= 100000
        cur = 0
        while cur < star and cur < star_max:
            lua_code = csMsgAll.get_CSEquipPartStarLevelUpMsg(id=tpId)
            bp.lua_console(lua_code)
            cur += 1


def fish_card_level(bp: BasePage, lv):
    table_data_object_list = bp.excelTools.get_table_data_object_list_by_key_value(key="uptpId", value=11, book_name="FISHCARD_UP.xlsm")
    fish_card_count = 1
    for table_data_object in table_data_object_list:
        if "fishcardUpCard" not in table_data_object:
            continue
        if table_data_object["level"] > lv:
            break
        fish_card_count += table_data_object["fishcardUpCard"]



    bp.cmd_list(["add 1 100000 10000000000", f"fishcardall {fish_card_count}"])

    table_data_object_list = bp.excelTools.get_table_data_object_list("FISHCARD.xlsm")
    fish_card_list = []
    fishery_last = None
    for table_data_object in table_data_object_list:
        if table_data_object["fishCardFishery"] == fishery_last:
            fish_card_list.append(table_data_object["tpId"])
            fishery_last = table_data_object["fishCardFishery"]
            continue
        fishery_last = table_data_object["fishCardFishery"]
        if fish_card_list:
            lua_code = csMsgAll.get_CSFishCardOneKeyLevelUpMsg(fishCardTpIds=fish_card_list)
            bp.lua_console(lua_code)
            bp.sleep(0.1)
        fish_card_list.clear()
        fish_card_list.append(table_data_object["tpId"])
    if fish_card_list:
        lua_code = csMsgAll.get_CSFishCardOneKeyLevelUpMsg(fishCardTpIds=fish_card_list)
        bp.lua_console(lua_code)



# 重启式创号
if __name__ == "__main__":
    bp = BasePage(serial_number="127.0.0.1:21593", is_mobile_device=False)

    # # fish_card_level(bp, 10)
    prefix = "n"
    # # prefix = "lv_2_"
    # index_list = [1, 15]
    # index_list = [1, 15, 30, 45, 60, 69, 78, 84, 90, 105, 120, 150, 170, 185, 195, 205, 215, 225, 235, 245, 255, 300]
    # index_list = [240, 255, 270, 285, 300]
    index_list = [
                  # {"lv": 30, "star": 0, "star_rod":0},
                  # {"lv": 60, "star": 0, "star_rod": 0},
                  # {"lv": 90, "star": 0, "star_rod": 0},
                  # {"lv": 120, "star": 0, "star_rod": 0},
                  # {"lv": 150, "star": 0, "star_rod": 0},
                  # {"lv": 215, "star": 0, "star_rod": 0},
                  # {"lv": 30, "star": 3, "star_rod": 0},
                  # {"lv": 60, "star": 3, "star_rod": 0},
                  # {"lv": 90, "star": 3, "star_rod": 0},
                  # {"lv": 120, "star": 3, "star_rod": 0},
                  # {"lv": 150, "star": 3, "star_rod": 0},
                  # {"lv": 215, "star": 3, "star_rod": 0},
                  # {"lv": 30, "star": 2, "star_rod": 2},
                  # {"lv": 60, "star": 2, "star_rod": 2},
                  # {"lv": 90, "star": 2, "star_rod": 2},
                  # {"lv": 120, "star": 2, "star_rod": 2},
                  # {"lv": 150, "star": 2, "star_rod": 2},
                  # {"lv": 215, "star": 2, "star_rod": 2},
                  # {"lv": 30, "star": 4, "star_rod": 4},
                  # {"lv": 60, "star": 4, "star_rod": 4},
                  # {"lv": 90, "star": 4, "star_rod": 4},
                  # {"lv": 120, "star": 4, "star_rod": 4},
                  # {"lv": 150, "star": 4, "star_rod": 4},
                  # {"lv": 215, "star": 4, "star_rod": 4},
                  {"lv": 30, "star": 0, "star_rod": 1},
                  {"lv": 60, "star": 0, "star_rod": 1},
                  {"lv": 90, "star": 0, "star_rod": 1},
                  {"lv": 120, "star": 0, "star_rod": 1},
                  {"lv": 150, "star": 0, "star_rod": 1},
                  {"lv": 215, "star": 0, "star_rod": 1},
                  # {"lv": 30, "star": 5, "star_rod": 2},
                  # {"lv": 60, "star": 5, "star_rod": 2},
                  # {"lv": 90, "star": 5, "star_rod": 2},
                  # {"lv": 120, "star": 5, "star_rod": 2},
                  # {"lv": 150, "star": 5, "star_rod": 2},
                  # {"lv": 215, "star": 5, "star_rod": 2},
                  # {"lv": 30, "star": 4, "star_rod": 2},
                  # {"lv": 60, "star": 4, "star_rod": 2},
                  # {"lv": 90, "star": 4, "star_rod": 2},
                  # {"lv": 120, "star": 4, "star_rod": 2},
                  # {"lv": 150, "star": 4, "star_rod": 2},
                {"lv": 30, "star": 0, "star_rod": 3},
                {"lv": 60, "star": 0, "star_rod": 3},
                {"lv": 90, "star": 0, "star_rod": 3},
                {"lv": 120, "star": 0, "star_rod": 3},
                {"lv": 150, "star": 0, "star_rod": 3},
                {"lv": 215, "star": 0, "star_rod": 3},
        {"lv": 30, "star": 0, "star_rod": 4},
        {"lv": 60, "star": 0, "star_rod": 4},
        {"lv": 90, "star": 0, "star_rod": 4},
        {"lv": 120, "star": 0, "star_rod": 4},
        {"lv": 150, "star": 0, "star_rod": 4},
        {"lv": 215, "star": 0, "star_rod": 4},
        # {"lv": 30, "star": 0, "star_rod": 0},
        # {"lv": 90, "star": 1, "star_rod": 2},
        # {"lv": 90, "star": 3, "star_rod": 2},
        # {"lv": 90, "star": 4, "star_rod": 2},
        # # {"lv": 1, "star": 2, "star_rod": 2},
        # # {"lv": 1, "star": 3, "star_rod": 3},
        # # {"lv": 1, "star": 4, "star_rod": 4},
        # # {"lv": 1, "star": 5, "star_rod": 4},
                ]
    # gear_init(bp)
    # gear_level(bp, lv=129)
    # gear_star(bp, star_line_lure=0, star_rod=2)

    i = 0
    while i < len(index_list):
        name = f"{prefix}_{index_list[i]['lv']}_{index_list[i]['star_rod']}_{index_list[i]['star']}"
        login(bp, name)
        bp.sleep(2)
        bp.clear_popup()
        gear_init(bp)
        gear_level(bp, lv=index_list[i]["lv"])
        gear_star(bp, star_line_lure=index_list[i]["star"], star_rod=index_list[i]["star_rod"])
        logout(bp)
        i += 1


    # bp.lua_console('PanelMgr:OpenPanel("BattleDebugPanel")')
    # bp.sleep(0.5)
    # bp.lua_console('PanelMgr:ClosePanel("BattleDebugPanel")')
    bp.connect_close()