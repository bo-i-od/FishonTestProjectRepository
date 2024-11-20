import random

from common import gameInit
from common.basePage import BasePage
from panelObjs.bugMultiplePanel import BugMultiplePanel
from panelObjs.buyEnergyPanel import BuyEnergyPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from tools.commonTools import *

def energy_drink_single_test(bp: BasePage):
    # 设定体力
    energy = random.randint(0, 200)
    bp.set_item_count(target_count=energy, item_tpid="100500")
    # 设定绿钞
    bp.set_item_count(target_count=0, item_tpid="100100")

    # 关闭打开刷新
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(1)

    # 得到可以恢复的体力值
    drink_recovery_value = BuyEnergyPanel.get_drink_recovery_value(bp)

    # 应该处于不可点击状态
    # btn_cash_status = BuyEnergyPanel.get_btn_cash_status(bp)
    # compare(btn_cash_status, 0)
    BuyEnergyPanel.click_btn_cash(bp)
    bp.sleep(1)
    energy_expect = energy
    energy = BuyEnergyPanel.get_energy_value(bp)
    compare(energy_expect, energy)


    # 设定饮料数
    drink_count = 1
    bp.set_item_count(target_count=drink_count, item_tpid="200600")

    # 关闭打开刷新
    BuyEnergyPanel.click_tap_to_close(bp)
    bp.sleep(1)
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(1)


    # 喝饮料
    while BuyEnergyPanel.get_btn_drink_status(bp) != 0:
        energy_expect = drink_recovery_value + energy
        BuyEnergyPanel.click_btn_drink(bp)
        bp.sleep(1)
        energy = BuyEnergyPanel.get_energy_value(bp)
        compare(energy_expect, energy)
        drink_count_expect = drink_count - 1
        drink_count = BuyEnergyPanel.get_drink_count(bp)
        compare(drink_count_expect, drink_count)

        # 等待动画播放完
        bp.sleep(1)

    # 饮料喝完的情况
    energy_expect = energy
    BuyEnergyPanel.click_btn_drink(bp)
    bp.sleep(1)
    energy = BuyEnergyPanel.get_energy_value(bp)
    compare(energy_expect, energy)


def energy_drink_multiple_test(bp: BasePage):
    # 设定饮料数
    drink_count = 1500
    bp.set_item_count(target_count=drink_count, item_tpid="200600")

    # 关闭打开刷新
    BuyEnergyPanel.click_tap_to_close(bp)
    bp.sleep(1)
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(1)
    BuyEnergyPanel.click_btn_drink(bp)
    bp.sleep(1)
    BugMultiplePanel.click_btn_cancel(bp)
    bp.sleep(1)
    BuyEnergyPanel.click_btn_drink(bp)
    bp.sleep(1)

    # 最大
    BugMultiplePanel.click_btn_max(bp)
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, value_max)

    # 点击-号
    BugMultiplePanel.click_btn_sub(bp)
    # 检查数值
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, value_max - 1)

    # 最小
    BugMultiplePanel.click_btn_min(bp)
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, 1)

    # 点击+号
    BugMultiplePanel.click_btn_add(bp)
    # 检查数值
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, 2)

    # 最小
    slider = BugMultiplePanel.get_slider(bp)

    # 滑到最大
    bp.swipe(point_start=[slider.slider_range[1] - slider.slider_size[0] * 0.2, slider.slider_position[1]], point_end=[slider.slider_range[1] + slider.slider_size[0] * 0.2, slider.slider_position[1]])
    bp.sleep(1)
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, value_max)


    bp.swipe(point_start=[slider.slider_range[0] + slider.slider_size[0] * 0.2, slider.slider_position[1]], point_end=[slider.slider_range[0] - slider.slider_size[0] * 0.2, slider.slider_position[1]])
    bp.sleep(1)
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, 1)

    # 最大
    BugMultiplePanel.click_btn_max(bp)
    value_cur, value_max = BugMultiplePanel.get_drink_value(bp)
    compare(value_cur, value_max)


    # 测试数值
    drink_icon = BugMultiplePanel.get_drink_icon(bp)
    drink_quantity_expect = BugMultiplePanel.get_drink_quantity(bp)

    # 测图标浮窗
    BugMultiplePanel.click_drink_icon(bp)
    bp.sleep(1)
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(drink_icon, item_icon)
    item_quantitiy = ItemTipsPanel.get_item_quantitiy(bp)
    compare(item_quantitiy, drink_quantity_expect)

    # 测饮料使用
    drink_quantity_expect -= value_cur
    energy_expect = bp.get_item_count(item_tpid="100500") + value_cur * 10
    BugMultiplePanel.click_btn_confirm(bp)
    bp.sleep(1)

    drink_quantity = bp.get_item_count(item_icon_name=drink_icon)
    energy = bp.get_item_count(item_tpid="100500")
    compare(drink_quantity_expect, drink_quantity)
    compare(energy_expect, energy)








def energy_cash_test(bp: BasePage):
    # 设定绿钞
    bp.set_item_count(target_count=10000, item_tpid="100100")
    # 关闭打开刷新
    BuyEnergyPanel.click_tap_to_close(bp)
    bp.sleep(1)
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(1)

    energy = BuyEnergyPanel.get_energy_value(bp)
    # cash买
    while BuyEnergyPanel.get_btn_cash_status(bp) != 2:
        cash_cost = BuyEnergyPanel.get_cash_cost(bp)
        cash_count_expect = BuyEnergyPanel.get_cash_value(bp) - cash_cost
        cash_recovery_value = BuyEnergyPanel.get_cash_recovery_value(bp)
        energy_expect = cash_recovery_value + energy
        BuyEnergyPanel.click_btn_cash(bp)
        bp.sleep(1)
        energy = BuyEnergyPanel.get_energy_value(bp)
        compare(energy_expect, energy)
        cash_count = BuyEnergyPanel.get_cash_value(bp)
        compare(cash_count_expect, cash_count)
        # 等待动画播放完
        bp.sleep(1)

def energy_cash_usd_test(bp:BasePage):
    if not bp.is_pay:
        return
    energy = BuyEnergyPanel.get_energy_value(bp)
    # cash_usd买
    cur = 1
    while BuyEnergyPanel.get_btn_cash_usd_status(bp) != 2:
        cash_usd_recovery_value = BuyEnergyPanel.get_cash_usd_recovery_value(bp)
        energy_expect = cash_usd_recovery_value + energy
        BuyEnergyPanel.click_btn_cash_usd(bp)
        bp.sleep(2)
        while RewardsPanel.is_panel_active(bp):
            RewardsPanel.click_tap_to_claim(bp)
            bp.sleep(1)
        energy = BuyEnergyPanel.get_energy_value(bp)
        compare(energy_expect, energy)
        # 等待动画播放完
        bp.sleep(1)
        cur += 1
        if cur > 5:
            continue
        # 分别测0，小，中，大，超R
        layer = f"{cur}000"
        bp.debug_log(f"当前分层为{layer}")
        cmd = f"setPlayerLayer " + layer
        bp.cmd(command=cmd)
        BuyEnergyPanel.click_tap_to_close(bp)
        # 关闭打开刷新
        bp.go_to_panel("BuyEnergyPanel")
        bp.sleep(1)

def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["guideskip", "add 1 101900 100000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # 喝饮料测试
    energy_drink_single_test(bp)

    # 钻石购买测试
    energy_cash_test(bp)

    # 充值测试
    energy_cash_usd_test(bp)

    # 关闭页面
    BuyEnergyPanel.click_tap_to_close(bp)


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533", is_mobile_device=False)
    energy_drink_multiple_test(bp)
    bp.connect_close()





