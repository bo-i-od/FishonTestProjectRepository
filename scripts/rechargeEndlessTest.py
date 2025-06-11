import random

from common import gameInit
from panelObjs.EventsGiftCenterPanel import EventsGiftCenterPanel
from panelObjs.FishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from tools.commonTools import *
from common.basePage import BasePage
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from panelObjs.RechargeEndlessThanksPanel import RechargeEndlessThanksPanel
from panelObjs.RechargeEndlessAddOnPanel import RechargeEndlessAddOnPanel
from panelObjs.FishCardSelectPanel import FishCardSelectPanel
from configs.elementsData import ElementsData


def click_icon_test(bp: BasePage,item_icon_list, item_icon_position_list):
    # 随机选中一个图标
    cur = 0
    while cur < len(item_icon_list):
        print(f"打印目当前icon：{item_icon_list[cur]}")
        bp.click_position(item_icon_position_list[cur], ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessAddOnPanel","EventsGiftCenterPanel"})
        bp.sleep(2)
        if ItemTipsPanel.is_panel_active(bp):
            item_icon = ItemTipsPanel.get_item_icon(bp)
            print(f"打印tips中的icon：{item_icon}")
        else:
            print(f"ItemTipsPanel is not active")
            #FishCardSelectPanel.wait_for_panel_appear(bp,ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessAddOnPanel","EventsGiftCenterPanel"})
            #item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        # 对比物品图标和浮窗物品图标
        compare(item_icon, item_icon_list[cur])
        bp.click_position([0.5, 0.8], ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessAddOnPanel","EventsGiftCenterPanel"})
        bp.sleep(0.5)
        cur += 1


def buy_test(bp: BasePage):
    panel = None
    if RechargeEndlessAddOnPanel.is_panel_active(bp):
        panel = RechargeEndlessAddOnPanel
    # 获取当前点卷
    money_expect = bp.get_item_count(item_tpid="101900")

    # 获取商品信息
    unlocked_index, locked_index_list = panel.get_btn_status(bp)
    print(f"已解锁商品索引：{unlocked_index}")
    print(f"锁定商品索引列表：{locked_index_list}")

    item_info_list = panel.get_item_info_list(bp)
    print('全部商品信息(item_info_list):', item_info_list)

    item_info_buy = item_info_list[unlocked_index]
    print('已解锁商品信息(item_info_buy):', item_info_buy)

    item_icon_list = list(item_info_buy)
    print('已解锁商品icon list(item_icon_list):', item_icon_list)

    item_icon_position_list = panel.get_item_icon_position_list(bp)[unlocked_index]
    print('已解锁商品icon位置(item_icon_position_list):', item_icon_position_list)

    click_icon_test(bp, item_icon_list, item_icon_position_list)

    btn_buy_position_list = panel.get_btn_buy_position_list(bp)
    print('全部购买按钮位置(btn_buy_position_list):', btn_buy_position_list)

    cost_list = panel.get_item_cost_list(bp)
    print('全部商品价格(cost_list):', cost_list)
    print('已解锁商品价格:', cost_list[unlocked_index])

    money_expect = money_expect - cost_list[unlocked_index]
    print('扣除后预期余额(money_expect):', money_expect)


    # 点非锁定的
    buy_pos=btn_buy_position_list[unlocked_index]
    print(buy_pos)
    if buy_pos and isinstance(buy_pos,(tuple,list)) and any(buy_pos):
        bp.click_position(btn_buy_position_list[unlocked_index], ignore_set={"CommonRewardsTipsPanel","EventsGiftCenterPanel","RechargeEndlessAddOnPanel"})
        RewardsPanel.wait_for_panel_appear(bp, ignore_set={"EventsGiftCenterPanel", "RechargeEndlessAddOnPanel",
                                                           "RewardsPanel"})
    else:
        print(f"未找到可用的购买按钮，跳过点击。位置{buy_pos}")

    # 点一个锁定的
    if locked_index_list:
        r = random.randint(0, len(locked_index_list) - 1)
        btn_buy_locked_index = locked_index_list[r]
        bp.click_position(btn_buy_position_list[btn_buy_locked_index],  ignore_set={"EventsGiftCenterPanel","RechargeEndlessAddOnPanel"})
        bp.sleep(1)



    # 对照数量
    money = bp.get_item_count(item_tpid="101900")
    compare(money_expect, money)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_info_buy, reward_dict)


    #if RewardsPanel.wait_for_panel_appear(bp):
     #   RewardsPanel.click_tap_to_claim(bp, ignore_set={panel.__name__, "RewardsPanel"})
    #bp.sleep(1)
    #bp.clear_popup(ignore_set={panel.__name__})




def main(bp: BasePage):
    panel = None
    if RechargeEndlessAddOnPanel.is_panel_active(bp):
        panel = RechargeEndlessAddOnPanel
    # cmd_list = [ f"add 1 101900 1000000", f"levelupto 16"]
    # bp.cmd("add 1 101900 1000000")
    # gameInit.login_to_hall(bp, cmd_list=cmd_list)
    #
    # # # 关闭升级弹窗
    # PlayerLevelupPanel.wait_for_panel_appear(bp)
    # bp.clear_popup()
    # bp.go_to_panel("RechargeEndlessPanel")

    # 若干次购买
    while panel.get_item_id_list(bp):
        item_list=panel.get_item_id_list(bp)
        print("元素",item_list)
        buy_test(bp)

    bp.clear_popup(ignore_set={panel.__name__})

    while FishCardSelectPanel.is_panel_active(bp):
        FishCardSelectPanel.click_btn_fishery(bp)
        FishCardSelectPanel.click_btn_confirm(bp)


    # 返回大厅，但由于购买过多卡包，所以只用返回看到开卡包面板
    bp.go_home(target_panel="FishBagPanel")

if __name__ == '__main__':
    bp = BasePage(serial_number="127.0.0.1:21523", is_mobile_device=False)
    main(bp)
    bp.connect_close()


