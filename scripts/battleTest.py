from common.basePage import BasePage
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from threading import Thread

def fish_once(bp: BasePage, fishery_id="", fish_id="",is_quick = True):
    print(fish_id)
    if fish_id != "":
        bp.cmd(f"mode {fishery_id} {fish_id}")
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    bp.sleep(1)
    if BattlePanel.is_reel_active(bp):
        bp.custom_cmd("autofish")
        qteThread = Thread(target=BattlePanel.qte, args=[bp])
        qteThread.start()
    if is_quick:
        BattlePanel.reel_quick(bp)
    element_btn = ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp, element_btn=element_btn)
    bp.cmd("mode 0 0")


def circulate_fish(bp: BasePage):
    cur = 6
    fishery = "302"
    while cur < 30000:
        index = str(cur).zfill(2)
        # bp.cmd(f"mode 400{fishery} {fishery}0{index}")
        BattlePreparePanel.click_btn_cast(bp)
        BattlePanel.hook(bp)
        bp.sleep(1)
        if BattlePanel.is_reel_active(bp):
            bp.custom_cmd("autofish")
            qteThread = Thread(target=BattlePanel.qte, args=[bp])
            qteThread.start()
        # BattlePanel.reel_quick(bp)
        element_btn = ResultPanel.wait_for_result(bp)
        ResultPanel.automatic_settlement(bp, element_btn=element_btn)
        cur += 1
        print(f"第{cur}次钓鱼")

def monster_all(bp: BasePage, fishery_id):
    cur = 2
    while cur < 7:
        bais = str(int(fishery_id[-2:]) - 1).zfill(2)
        fish_once(bp, fishery_id=fishery_id, fish_id=f"390{bais}{cur}")
        cur += 1




if __name__ == '__main__':
    bp = BasePage()
    bp.cmd("mode 400301 390005")
    circulate_fish(bp)
    # bp.cmd("add 1 100200 10000000")
    # bp.set_item_count(target_count=100,item_tpid="100100")GG
    # bp.cmd("autofish")
    #
    # monster_all(bp, "400303")
    # a = bp.get_item_count(item_tpid="100500")
    # print(a)




