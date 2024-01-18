import random
from common.basePage import BasePage
from panelObjs.buyEnergyPanel import BuyEnergyPanel
from tools.commonTools import *


def energy_test(bp: BasePage):
    # 设定体力
    energy = random.randint(0, 200)
    bp.set_item_count(target_count=energy, item_tpid="100500")

    # 设定绿钞
    bp.set_item_count(target_count=0, item_tpid="100100")

    # 关闭打开刷新
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(0.5)

    # 得到可以恢复的体力值
    drink_recovery_value = BuyEnergyPanel.get_drink_recovery_value(bp)
    cash_recovery_value = BuyEnergyPanel.get_cash_recovery_value(bp)

    # 应该处于不可点击状态
    btn_cash_status = BuyEnergyPanel.get_btn_cash_status(bp)
    compare(btn_cash_status, 0)
    BuyEnergyPanel.click_btn_cash(bp)
    bp.sleep(0.5)
    energy_expect = energy
    energy = BuyEnergyPanel.get_energy_value(bp)
    compare(energy_expect, energy)


    # 设定饮料数
    drink_count = 2
    bp.set_item_count(target_count=drink_count, item_tpid="200600")

    # 设定绿钞
    bp.set_item_count(target_count=10000, item_tpid="100100")

    # 关闭打开刷新
    BuyEnergyPanel.click_tap_to_close(bp)
    bp.sleep(0.5)
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(0.5)


    # 喝饮料
    while BuyEnergyPanel.get_btn_drink_status(bp) != 0:
        energy_expect = drink_recovery_value + energy
        BuyEnergyPanel.click_btn_drink(bp)
        bp.sleep(0.5)
        energy = BuyEnergyPanel.get_energy_value(bp)
        compare(energy_expect, energy)
        drink_count_expect = drink_count - 1
        drink_count = BuyEnergyPanel.get_drink_count(bp)
        compare(drink_count_expect, drink_count)

        # 等待动画播放完
        bp.sleep(2)

    # 饮料喝完的情况
    energy_expect = energy
    BuyEnergyPanel.click_btn_drink(bp)
    bp.sleep(0.5)
    energy = BuyEnergyPanel.get_energy_value(bp)
    compare(energy_expect, energy)

    # cash买
    while BuyEnergyPanel.get_btn_cash_status(bp) != 2:
        cash_cost = BuyEnergyPanel.get_cash_cost(bp)
        cash_count_expect = BuyEnergyPanel.get_cash_value(bp) - cash_cost
        cash_usd_recovery_value = BuyEnergyPanel.get_cash_usd_recovery_value(bp)
        energy_expect = cash_recovery_value + energy
        BuyEnergyPanel.click_btn_cash(bp)
        bp.sleep(0.5)
        energy = BuyEnergyPanel.get_energy_value(bp)
        compare(energy_expect, energy)
        cash_count = BuyEnergyPanel.get_cash_value(bp)
        compare(cash_count_expect, cash_count)
        # 等待动画播放完
        bp.sleep(2)

    # cash_usd买
    while BuyEnergyPanel.get_btn_cash_usd_status(bp) != 2:
        energy_expect = cash_usd_recovery_value + energy
        BuyEnergyPanel.click_btn_cash_usd(bp)
        bp.sleep(0.5)
        energy = BuyEnergyPanel.get_energy_value(bp)
        compare(energy_expect, energy)
        # 等待动画播放完
        bp.sleep(2.5)

    # 关闭页面
    BuyEnergyPanel.click_tap_to_close(bp)


if __name__ == '__main__':
    bp = BasePage()
    energy_test(bp)





