from common import gameInit
from common.basePage import BasePage

from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from threading import Thread
from panelObjs.tournamentsPanel import TournamentsPanel



def fish_once(bp: BasePage, fishery_id="", fish_id="", is_quick=False):
    bp.set_time_scale()
    if fish_id != "":
        c = f"mode {fishery_id} {fish_id}"
        print(c)
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
    element_btn = ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp, element_btn=element_btn)

    if fish_id != "":
        bp.cmd("mode 0 0")



def circulate_fish(bp: BasePage, fishery_id=None, is_quick=False, times=500, start=0):
    fish_list = []
    cur = start
    if fishery_id is not None:
        fish_list = TournamentsPanel.get_fish_list(bp, fishery_id)
        times = len(fish_list)
    while cur < times:
        fish_id = ""
        # 指定鱼
        if fish_list:
            fish_id = fish_list[cur]
            if fish_id == "0" or fish_id == 0:
                cur += 1
                continue
        # bp.sleep(1)
        bp.clear_popup()
        # if cur == 1:
        #     select_rod(bp, 3)
        # if cur == 5:
        #     select_rod(bp, 3)
        # if cur == 9:
        #     select_rod(bp, 2)
        fish_once(bp, fishery_id=fishery_id, fish_id=fish_id, is_quick=is_quick)
        # print(f"第{cur}次钓鱼")
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
    table_data = bp.excelTools.get_table_data("FISHERIES.xlsm")
    tpid_fishery_list = table_data["tpId"]
    cur = 0
    while cur < len(tpid_fishery_list):
        fishery_id = str(tpid_fishery_list[cur])
        if table_data["enabled"][cur] != 1:
            cur += 1
            continue
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
    # 连接设备号为127.0.0.1:21533的设备
    bp = BasePage("127.0.0.1:21513")
    bp.set_send_log_flag(False)
    gameInit.set_joystick(bp)
    bp.is_time_scale = False
    bp.custom_cmd("setTension 0.9")
    circulate_fish(bp, is_quick=False,times=120)
    # fish_once(bp)
    # # 按渔场id从小到大，再按鱼从小到大钓一遍
    # fish_all(bp,  is_quick=True)
    # fish_all(bp, is_quick=True)
    # l = ["390011","390013", "390014", "390017", "390018"]
    # cur = 1
    # while cur < 6:
    #     fish_once(bp, is_quick=False, fishery_id="400301", fish_id=f"39000{cur}")
    #     cur += 1
    #
    # 断开连接
    bp.connect_close()








