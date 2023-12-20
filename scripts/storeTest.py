import random
from common.basePage import BasePage
from panelObjs.storePanel import StorePanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from tools.commonTools import *


def gift_pack_test(bp:BasePage):
    StorePanel.change_tab(bp, 0)
    gift_pack_click_icon_test(bp)
    gift_pack_buy_test(bp)


def gift_pack_click_icon_test(bp:BasePage):
    gift_pack_icon_list, gift_pack_position_list = StorePanel.get_gift_pack_icon_and_position_list(bp)
    r = random.randint(0, len(gift_pack_position_list) - 1)
    bp.click_position(gift_pack_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, gift_pack_icon_list[r])
    bp.click_position([0.5, 0.1])


def gift_pack_buy_test(bp:BasePage):
    gift_pack_dict_list = StorePanel.get_gift_pack_dict_list(bp)
    r = random.randint(0, len(gift_pack_dict_list) - 1)
    btn_position_list = StorePanel.get_btn_position_list(bp)
    gift_pack_dict = gift_pack_dict_list[r]
    gift_pack_icon_list = list(gift_pack_dict)
    item_count_expect_list = bp.get_item_count_list(gift_pack_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += gift_pack_dict[gift_pack_icon_list[cur]]
        cur += 1
    bp.click_position(btn_position_list[r])
    # 加支付逻辑
    bp.sleep(1)
    # 加支付逻辑
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(reward_dict, gift_pack_dict)
    item_count_list = bp.get_item_count_list(gift_pack_icon_list)
    compare_list(item_count_expect_list, item_count_list)
    RewardsPanel.click_tap_to_claim(bp)


def cash_test(bp:BasePage):
    StorePanel.change_tab(bp, 3)
    cash_click_icon_test(bp)
    cash_buy_test(bp)


def cash_click_icon_test(bp:BasePage):
    if ItemTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])
    cash_icon_list = StorePanel.get_cash_icon_list(bp)
    cash_position_list = StorePanel.get_cash_position_list(bp)
    r = random.randint(0, len(cash_position_list) - 1)
    bp.click_position(cash_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, cash_icon_list[r])
    bp.click_position([0.5, 0.1])


def cash_buy_test(bp:BasePage):
    cash_icon_list = StorePanel.get_cash_icon_list(bp)
    cash_quantity_list = StorePanel.get_cash_quantity_list(bp)
    cash_first_time_list = StorePanel.get_cash_first_time_list(bp)
    r = random.randint(0, len(cash_icon_list) - 1)
    btn_position_list = StorePanel.get_btn_position_list(bp)
    item_count_expect = bp.get_item_count(item_icon_name=cash_icon_list[r])
    cur = 0
    while cur < len(cash_quantity_list):
        if cash_first_time_list[cur]:
            cash_quantity_list[cur] *= 2
        cur += 1
    bp.click_position(btn_position_list[r])
    # 加支付逻辑
    bp.sleep(1)
    # 加支付逻辑
    item_count_expect += cash_quantity_list[r]
    reward_quantity_list = RewardsPanel.get_reward_quantity_list(bp)
    print(cash_quantity_list[r], reward_quantity_list[0])
    compare(cash_quantity_list[r], reward_quantity_list[0])
    item_count = bp.get_item_count(item_icon_name=cash_icon_list[r])
    compare(item_count_expect, item_count)
    RewardsPanel.click_tap_to_claim(bp)


def gear_click_icon_test(bp:BasePage):
    gear_position_list = StorePanel.get_gear_position_list(bp)
    gear_name_list = StorePanel.get_gear_name_list(bp)
    r = random.randint(0, len(gear_position_list) - 1)
    bp.click_position(gear_position_list[r])
    gear_name = BaitAndRodShowPanel.get_gear_name(bp)
    compare(gear_name_list[r], gear_name)
    BaitAndRodShowPanel.click_tap_to_continue(bp)


def gear_buy_test(bp:BasePage):
    gear_icon_list = StorePanel.get_gear_icon_list(bp)
    gear_id_list = StorePanel.get_item_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=gear_id_list)
    price_list = StorePanel.get_price_list(bp, item_id_list=gear_id_list)
    r = random.randint(0, len(btn_position_list) - 1)
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    bp.click_position(btn_position_list[r])
    if not is_clickable:
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
        return
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    cash_expect -= price_list[r]
    cash = StorePanel.get_cash(bp)
    compare(cash_expect, cash)
    reward_item_icon_list, reward_gear_icon_list = RewardsPanel.get_reward_icon_list(bp, is_divide=True)
    compare(reward_gear_icon_list[0], gear_icon_list[r])
    RewardsPanel.click_tap_to_claim(bp)


def fish_card_test(bp:BasePage):
    fish_card_click_icon_test(bp)
    fish_card_buy_test(bp)


def fish_card_buy_test(bp:BasePage):
    fish_card_id_list = StorePanel.get_item_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=fish_card_id_list)
    price_list = StorePanel.get_price_list(bp, item_id_list=fish_card_id_list)
    r = random.randint(0, len(btn_position_list) - 1)
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    bp.click_position(btn_position_list[r])
    if not is_clickable:
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
        return
    bp.clear_popup_until_appear(StorePanel.get_StorePanel_element_data())
    cash_expect -= price_list[r]
    cash = StorePanel.get_cash(bp)
    compare(cash_expect, cash)


def fish_card_click_icon_test(bp:BasePage):
    if FishCardPackTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])
    fish_card_position_list = StorePanel.get_fish_card_position_list(bp)
    fish_card_name_list = StorePanel.get_fish_card_name_list(bp)
    r = random.randint(0, len(fish_card_position_list) - 1)
    bp.click_position(fish_card_position_list[r])
    fish_card_name = FishCardPackTipsPanel.get_fish_card_name(bp)
    compare(fish_card_name_list[r], fish_card_name)
    bp.click_position([0.5, 0.1])


def booster_click_icon_test(bp:BasePage):
    if ItemTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])
    booster_icon_list = StorePanel.get_booster_icon_list(bp)
    booster_position_list = StorePanel.get_booster_position_list(bp)
    r = random.randint(0, len(booster_position_list) - 1)
    bp.click_position(booster_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(item_icon, booster_icon_list[r])
    bp.click_position([0.5, 0.1])


def booster1_buy_test(bp:BasePage):
    booster_id_list = StorePanel.get_item_id_list(bp)
    price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
    booster_dict_list = StorePanel.get_booster_dict_list(bp)
    # 买每日免费booster礼包
    r = 0
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=booster_id_list)
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    if price_list[r] != -1:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
        price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
        compare(price_list[r], -1)
    # 买每日lager booster礼包
    r = 1
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    if price_list[r] != -1 and is_clickable:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
        price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
        compare(price_list[r], -1)
    else:
        bp.click_position(btn_position_list[r])
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
    # 随机选一个
    r = random.randint(2, 5)
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    if is_clickable:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
    else:
        bp.click_position(btn_position_list[r])
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)


def booster2_buy_test(bp:BasePage):
    booster_id_list = StorePanel.get_item_id_list(bp)
    price_list = StorePanel.get_price_list(bp, item_id_list=booster_id_list)
    booster_dict_list = StorePanel.get_booster_dict_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=booster_id_list)
    # 随机选一个
    r = random.randint(0, 5)
    booster_dict = booster_dict_list[r]
    booster_icon_list = list(booster_dict)
    item_count_expect_list = bp.get_item_count_list(booster_icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += booster_dict[booster_icon_list[cur]]
        cur += 1
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    if is_clickable:
        cash_expect -= price_list[r]
        bp.click_position(btn_position_list[r])
        reward_dict = RewardsPanel.get_reward_dict(bp)
        compare_dict(reward_dict, booster_dict)
        RewardsPanel.click_tap_to_claim(bp)
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)
    else:
        bp.click_position(btn_position_list[r])
        cash = StorePanel.get_cash(bp)
        compare(cash_expect, cash)


def materials_click_icon_test(bp:BasePage):
    if ItemTipsPanel.is_panel_active(bp):
        bp.click_position([0.5, 0.1])
    materials_position_list = StorePanel.get_materials_position_list(bp)
    materials_icon_list = StorePanel.get_materials_icon_list(bp)
    r = random.randint(0, len(materials_position_list) - 1)
    bp.click_position(materials_position_list[r])
    materials_icon = ItemTipsPanel.get_item_icon(bp)
    compare(materials_icon_list[r], materials_icon)
    bp.click_position([0.5, 0.1])


def materials_buy_test(bp:BasePage):
    materials_id_list = StorePanel.get_item_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, item_id_list=materials_id_list)
    price_list = StorePanel.get_price_list(bp, item_id_list=materials_id_list)
    r = random.randint(0, len(btn_position_list) - 1)
    cash_expect = StorePanel.get_cash(bp)
    is_clickable = StorePanel.is_clickable(bp, price_list[r])
    bp.click_position(btn_position_list[r])
    if not is_clickable:
        return

    cash_expect -= price_list[r]
    cash = StorePanel.get_cash(bp)
    compare(cash_expect, cash)

if __name__ == '__main__':
    bp = BasePage()
    cash_test(bp)