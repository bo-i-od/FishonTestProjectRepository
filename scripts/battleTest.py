from common.basePage import BasePage

from panelObjs.buyEnergyPanel import BuyEnergyPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.champoinshipTournamentsPanel import ChampoinshipTournamentsPanel
from threading import Thread

def fish_once(bp: BasePage, fishscene_id="", fish_id=""):
    if fish_id != "":
        bp.cmd(f"mode {fishscene_id} {fish_id}")
    bp.cmd("autofish")
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp)
    bp.cmd(f"mode 0 0")


def circulate_fish(bp: BasePage):
    cur = 0

    while True:
        index = str(cur).zfill(2)
        bp.cmd(f"mode 400301 3010{index}")
        BattlePreparePanel.click_btn_cast(bp)
        # while BuyEnergyPanel.is_panel_active(bp):
        #     BuyEnergyPanel.buy_energy(bp)
        #     bp.sleep(0.5)
        #     BuyEnergyPanel.click_tap_to_close(bp)
        #     bp.sleep(0.5)
        #     BattlePreparePanel.click_btn_cast(bp)
        BattlePanel.hook(bp)
        bp.sleep(1)
        if BattlePanel.is_reel_active(bp):
            bp.custom_cmd("autofish")
            qteThread = Thread(target=BattlePanel.qte, args=[bp])
            qteThread.start()
        # BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        ResultPanel.automatic_settlement(bp)
        cur += 1
        print(f"第{cur}次钓鱼")



if __name__ == '__main__':
    bp = BasePage()
    # bp.cmd("add 1 100200 10000000")
    # bp.set_item_count(target_count=100,item_tpid="100100")
    # bp.cmd("autofish")
    #
    circulate_fish(bp)
    # a = bp.get_item_count(item_tpid="100500")
    # print(a)




