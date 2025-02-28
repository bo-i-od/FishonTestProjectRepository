import random

from common import gameInit
from panelObjs.EventsGiftCenterPanel import EventsGiftCenterPanel
from panelObjs.FishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from tools.commonTools import *
from common.basePage import BasePage
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from panelObjs.RechargeEndlessNewYearPanel import RechargeEndlessNewYearPanel
from panelObjs.RechargeEndlessThanksPanel import RechargeEndlessThanksPanel
from configs.elementsData import ElementsData


def click_icon_test(bp: BasePage,item_icon_list, item_icon_position_list):
    # 随机选中一个图标
    cur = 0
    while cur < len(item_icon_list):
        bp.click_position(item_icon_position_list[cur], ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessThanksPanel", "RechargeEndlessNewYearPanel"})
        bp.sleep(0.5)
        if ItemTipsPanel.is_panel_active(bp):
            item_icon = ItemTipsPanel.get_item_icon(bp)
        else:
            item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        # 对比物品图标和浮窗物品图标
        compare(item_icon, item_icon_list[cur])
        bp.click_position([0.5, 0.1], ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessThanksPanel", "RechargeEndlessNewYearPanel"})
        bp.sleep(0.5)
        cur += 1


def buy_test(bp: BasePage):
    panel = None
    if RechargeEndlessNewYearPanel.is_panel_active(bp):
        panel = RechargeEndlessNewYearPanel
    elif RechargeEndlessThanksPanel.is_panel_active(bp):
        panel = RechargeEndlessThanksPanel
    # 获取当前点卷
    money_expect = bp.get_item_count(item_tpid="101900")

    # 获取商品信息
    unlocked_index, locked_index_list = panel.get_btn_status(bp)
    item_info_list = panel.get_item_info_list(bp)

    item_info_buy = item_info_list[unlocked_index]
    item_icon_list = list(item_info_buy)
    item_icon_position_list = panel.get_item_icon_position_list(bp)[unlocked_index]
    click_icon_test(bp, item_icon_list, item_icon_position_list)
    btn_buy_position_list = panel.get_btn_buy_position_list(bp)

    cost_list = panel.get_item_cost_list(bp)
    money_expect = money_expect - cost_list[unlocked_index]


    # 点一个锁定的
    if locked_index_list:
        r = random.randint(0, len(locked_index_list) - 1)
        btn_buy_locked_index = locked_index_list[r]
        bp.click_position(btn_buy_position_list[btn_buy_locked_index], ignore_set={panel.__name__})
        bp.sleep(1)

    # 点非锁定的
    bp.click_position(btn_buy_position_list[unlocked_index], ignore_set={panel.__name__})
    RewardsPanel.wait_for_panel_appear(bp, ignore_set={panel.__name__, "RewardsPanel"})

    # 对照数量
    money = bp.get_item_count(item_tpid="101900")
    compare(money_expect, money)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_info_buy, reward_dict)

    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp, ignore_set={panel.__name__, "RewardsPanel"})
    bp.sleep(1)
    bp.clear_popup(ignore_set={panel.__name__})


def main(bp: BasePage):
    panel = None
    if RechargeEndlessNewYearPanel.is_panel_active(bp):
        panel = RechargeEndlessNewYearPanel
    elif RechargeEndlessThanksPanel.is_panel_active(bp):
        panel = RechargeEndlessThanksPanel
    # cmd_list = ["guideskip", f"add 1 101900 1000000", f"levelupto 16"]
    # bp.cmd("add 1 101900 1000000")
    # gameInit.login_to_hall(bp, cmd_list=cmd_list)
    #
    # # # 关闭升级弹窗
    # PlayerLevelupPanel.wait_for_panel_appear(bp)
    # bp.clear_popup()
    # bp.go_to_panel("RechargeEndlessPanel")

    # 若干次购买
    while panel.get_item_id_list(bp):
        buy_test(bp)

    # 返回大厅，但由于购买过多卡包，所以只用返回看到开卡包面板
    # bp.go_home(target_panel="FishBagPanel")

if __name__ == '__main__':
    bp = BasePage(serial_number="127.0.0.1:21523", is_mobile_device=False)
    main(bp)
    bp.connect_close()


