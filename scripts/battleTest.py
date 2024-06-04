import random

import common.gameInit
from common import gameInit
from common.basePage import BasePage
from netMsg import csMsgAll
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from threading import Thread
from panelObjs.tournamentsPanel import TournamentsPanel


def fish_once(bp: BasePage, fishery_id="", fish_id="", is_quick=True):
    bp.set_time_scale()
    # bp.sleep(6)
    if fish_id != "":
        c = f"mode {fishery_id} {fish_id}"
        bp.cmd(c)
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    bp.set_time_scale()
    if BattlePanel.is_reel_active(bp):
        bp.custom_cmd("autofish")
        qteThread = Thread(target=BattlePanel.qte, args=[bp])
        qteThread.start()
    if is_quick:
        BattlePanel.reel_quick(bp)
    bp.set_time_scale()
    # bp.sleep(6)
    element_btn = ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp, element_btn=element_btn)
    if fish_id != "":
        bp.cmd("mode 0 0")



def circulate_fish(bp: BasePage, fishery_id=None, is_quick=False, times=500):
    fish_list = []
    cur = 0
    if fishery_id is not None:
        fish_list = TournamentsPanel.get_fish_list(bp, fishery_id)
        times = len(fish_list)
    while cur < times:
        fish_id = ""
        # 指定鱼
        if fish_list:
            fish_id = fish_list[cur]
        bp.sleep(2)
        bp.clear_popup()
        # if cur == 1:
        #     select_rod(bp, 3)
        # if cur == 5:
        #     select_rod(bp, 3)
        # if cur == 9:
        #     select_rod(bp, 2)
        fish_once(bp, fishery_id=fishery_id, fish_id=fish_id, is_quick=is_quick)
        print(f"第{cur}次钓鱼")
        cur += 1


def select_rod(bp: BasePage, index):
    BattlePreparePanel.click_gears(bp)
    bp.sleep(1)
    rod_position_list = BattlePreparePanel.get_rod_position_list(bp)
    bp.click_position(rod_position_list[index - 1])
    bp.sleep(1)
    BattlePreparePanel.click_btn_apply(bp)
    bp.sleep(1)

def select_location(bp: BasePage, index):
    BattlePreparePanel.click_btn_location(bp)
    bp.sleep(1)
    # BattlePreparePanel




def fish_all(bp: BasePage, is_quick=False):
    cur = 1
    while cur < 13:
        index = str(cur).zfill(2)
        fishery_id = f"4003{index}"
        TournamentsPanel.go_to_fishery_by_tpid(bp, fishery_id)
        circulate_fish(bp, fishery_id=fishery_id, is_quick=is_quick)
        BattlePreparePanel.click_btn_close(bp)
        bp.sleep(1)
        cur += 1

def tournament(bp: BasePage):
    bp.go_home()
    bp.go_to_panel("TournamentsPanel")
    TournamentsPanel.go_to_fishery_by_index(bp, 0)
    circulate_fish(bp, is_quick=False, times=10)
    bp.go_home()
    bp.go_to_panel("TournamentsPanel")
    TournamentsPanel.go_to_fishery_by_index(bp, 1)
    circulate_fish(bp, is_quick=False, times=18)



if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21523")
    bp.cmd_list(["add 1 100000 113245464"])
    # fish_once(bp)
    #
    # cur = 1
    # while cur < 9:
    #     lua_code = csMsgAll.get_CSBaitAndRodLevelUpToMsg(tpId=(500010 + cur), targetLevel=30, ioIdType=5)
    #     bp.lua_console(lua_code)
    #     bp.sleep(0.5)
    #     cur += 1




    # gameInit.set_joystick(bp)
    # bp.cmd("levelupto 50")
    circulate_fish(bp, is_quick=False, fishery_id="400301")

    # fish_all(bp, is_quick=False)
    # monster_all(bp, is_quick=True, fishery_id="400317")
    # while True:
    #     tournament(bp)
    # bp.set_item_count(target_count=72000,item_tpid="209013")
    # cur = 0
    # while cur < 10:
    #     circulate_fish(bp, is_quick=True, fishery_id="400302")
    # bp.cmd("mode 400301 390001")

    # worksheet = bp.excelTools.get_worksheet(book_name="玩家信息采样.xlsx", sheet_name="Sheet1")
    # column_data = []
    # # 第六行开始
    # cur = 3
    # column_index = 3
    # while worksheet.cell(cur, 2).value is not None:
    #     index = column_index - 1
    #     column_data.append(worksheet.cell(cur, column_index).value)
    #     cur += 1
    # print(column_data)
    # bp.cmd("mode 400301 390005")
    # createUsers.main(bp)
    # bp.cmd("add 1 100200 10000000")
    # bp.set_item_count(target_count=100,item_tpid="100100")GG
    # bp.cmd("autofish")
    #
    # monster_all(bp, "400303")
    # a = bp.get_item_count(item_tpid="100500")
    # print(a)




