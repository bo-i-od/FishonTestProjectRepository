from common.basePage import BasePage

from panelObjs.buyEnergyPanel import BuyEnergyPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.champoinshipTournamentsPanel import ChampoinshipTournamentsPanel


def fish_once(bp: BasePage, fishscene_id="", fish_id=""):
    if fish_id != "":
        bp.cmd(f"mode {fishscene_id} {fishscene_id}")
    bp.cmd("autofish")
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook(bp)
    ResultPanel.wait_for_result(bp)
    ResultPanel.automatic_settlement(bp)
    bp.cmd(f"mode 0 0")


def circulate_fish(bp: BasePage):
    cur = 8
    # bp.cmd(f"mode 400301 301013")
    while True:
        index = str(cur).zfill(2)
        print(index)
        bp.cmd(f"mode 400301 3010{index}")
        BattlePreparePanel.click_btn_cast(bp)
        while BuyEnergyPanel.is_panel_active(bp):
            BuyEnergyPanel.buy_energy(bp)
            bp.sleep(0.5)
            BuyEnergyPanel.click_tap_to_close(bp)
            bp.sleep(0.5)
            BattlePreparePanel.click_btn_cast(bp)
        BattlePanel.hook(bp)
        BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        ResultPanel.automatic_settlement(bp)
        cur += 1
        # print(f"第{cur}次钓鱼,鱼的概率为{fish/float(cur)}")



if __name__ == '__main__':
    bp = BasePage()
    # bp.cmd("add 1 100200 10000000")

    bp.cmd("autofish")
    #
    circulate_fish(bp)
    # a = bp.get_item_count(item_tpid="100500")
    # print(a)




