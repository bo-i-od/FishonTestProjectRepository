from common.basePage import BasePage

from panelObjs.buyEnergyPanel import BuyEnergyPanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.champoinshipTournamentsPanel import ChampoinshipTournamentsPanel





def circulate_fish(bp: BasePage):
    print(f'初始经验：{bp.get_item_count(item_tpid="100200")}')
    cur = 1
    # bp.cmd(f"mode 400301 301013")
    while True:
        # index = str(cur).zfill(2)
        # bp.cmd(f"mode 400308 3080" + index)
        BattlePreparePanel.click_btn_cast(bp)
        while BuyEnergyPanel.is_panel_active(bp):
            BuyEnergyPanel.buy_energy(bp)
            bp.sleep(0.5)
            BuyEnergyPanel.click_tap_to_close(bp)
            bp.sleep(0.5)
            BattlePreparePanel.click_btn_cast(bp)

        BattlePanel.reel_quick(bp)
        ResultPanel.wait_for_result(bp)
        exp = ResultPanel.get_exp(bp)
        print(f"本次获取经验：{exp}")
        exp_all = bp.get_item_count(item_tpid="100200")
        print(f'第{cur}次抛竿，当前经验：{exp_all}')
        if exp_all > 29299:
            break
        ResultPanel.automatic_settlement(bp)
        cur += 1
        # print(f"第{cur}次钓鱼,鱼的概率为{fish/float(cur)}")



if __name__ == '__main__':
    bp = BasePage()
    # bp.cmd("add 1 100200 10000000")

    bp.cmd("autofish")
    circulate_fish(bp)




