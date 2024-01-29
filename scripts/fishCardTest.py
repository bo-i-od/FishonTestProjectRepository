import random

from common.basePage import BasePage
from panelObjs.fishCardPanel import FishCardPanel
from panelObjs.fishCardUpgradePanel import FishCardUpgradePanel
from panelObjs.homePanel import HomePanel
from panelObjs.fishCardGiftPackPanel import FishCardGiftPackPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from common import resource
from tools.commonTools import *
def FishCardUpgradePanel_test(bp: BasePage):
    # 比较卡面和右侧面板数值
    card_information_now = FishCardUpgradePanel.get_card_information(bp)
    level_up_information_now = FishCardUpgradePanel.get_level_up_information(bp)
    compare(card_information_now["level"], level_up_information_now["level_now"])
    compare(level_up_information_now["level_now"] + 1, level_up_information_now["level_next"])
    compare(card_information_now["progress_numerator"], level_up_information_now["progress_numerator"])
    compare(card_information_now["progress_denominator"], level_up_information_now["progress_denominator"])
    compare(card_information_now["talent"], level_up_information_now["talent_val_now_list"][0])
    # 计算费用
    cost = level_up_information_now["cost_value_list"][0]
    stock_expect = FishCardUpgradePanel.get_stock(bp)
    # 点击升级
    FishCardUpgradePanel.click_btn_level_up(bp)
    # 比较费用与预期是否一致
    stock_expect -= cost
    stock = FishCardUpgradePanel.get_stock(bp)
    compare(stock_expect, stock)
    # 升满了就返回
    if level_up_information_now["level_next"] == 20:
        return
    # 比较卡牌和面板数值
    card_information_next = FishCardUpgradePanel.get_card_information(bp)
    level_up_information_next = FishCardUpgradePanel.get_level_up_information(bp)
    compare(card_information_next["level"], level_up_information_next["level_now"])
    compare(level_up_information_next["level_now"] + 1, level_up_information_next["level_next"])
    compare(card_information_next["progress_numerator"], level_up_information_next["progress_numerator"])
    compare(card_information_next["progress_denominator"], level_up_information_next["progress_denominator"])
    compare(card_information_next["talent"], level_up_information_next["talent_val_now_list"][0])
    # 比较升级前后数值
    progress_expect = card_information_now["progress_numerator"] - card_information_now["progress_denominator"]
    compare(progress_expect, card_information_next["progress_numerator"])
    cur = 0
    while cur < len(level_up_information_now["talent_val_now_list"]):
        talent_val_expect = level_up_information_now["talent_val_now_list"][cur] + level_up_information_now["talent_val_next_list"][cur]
        compare(talent_val_expect, level_up_information_next["talent_val_now_list"][cur])
        cur += 1
    print("level_up_test升级测试通过")
    # return card_information_next

def check_information_test(bp: BasePage):
    card_information = FishCardPanel.get_card_information(bp)
    main_name, main_size = FishCardPanel.get_main_name_and_size(bp)
    compare(main_name, card_information["fish_name"])
    size_expect = FishCardPanel.bg_to_tier(card_information["title_bg"])
    compare(size_expect, main_size)
    return card_information

def level_up_test(bp: BasePage):
    FishCardPanel.select_arrow_card(bp)
    check_information_test(bp)
    FishCardPanel.click_btn_upgrade(bp)
    while FishCardUpgradePanel.is_btn_level_up_abled(bp):
        FishCardUpgradePanel.level_up_check(bp)
        FishCardUpgradePanel_test(bp)
        # card_information_now = FishCardUpgradePanel.get_card_information(bp)
        # compare(card_information, card_information_now)
    FishCardUpgradePanel.click_btn_close(bp)
    if FishCardGiftPackPanel.is_panel_active(bp):
        FishCardGiftPackPanel.click_btn_close(bp)


def select_card_test(bp: BasePage):
    fisheries_list = FishCardPanel.get_fisheries_list(bp)
    r = random.randint(0, len(fisheries_list) - 1)
    FishCardPanel.switch_tab(bp, r)
    card_information = check_information_test(bp)
    compare(fisheries_list[r], card_information["fisheries_name"])
    card_id_list = FishCardPanel.get_card_id_list(bp)
    r = random.randint(0, len(card_id_list) - 1)
    FishCardPanel.select_card(bp, r)
    print("select_card_test选择卡片测试通过")

def FishCardGiftPackPanel_test(bp: BasePage):
    FishCardPanel.click_btn_events(bp)
    bp.sleep(0.5)
    icon_list = FishCardGiftPackPanel.get_item_icon_list(bp)
    quantity_list = FishCardGiftPackPanel.get_item_quantity_list(bp)
    click_pack_icon_test(bp, icon_list)
    resource.str_to_int_list(quantity_list)
    item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    cur = 0
    while cur < len(item_count_expect_list):
        item_count_expect_list[cur] += quantity_list[cur]
        cur += 1
    FishCardGiftPackPanel.click_btn_buy(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_dict, reward_dict)
    item_count_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    print(item_count_expect_list, item_count_list)
    compare_list(item_count_expect_list, item_count_list)
    RewardsPanel.click_tap_to_claim(bp)
    print("buy_pack_test购买礼包测试通过")

def click_pack_icon_test(bp: BasePage, icon_list):
    position_list = FishCardGiftPackPanel.get_item_position_list(bp)
    r = random.randint(0, len(position_list) - 1)
    bp.click_position(position_list[r])
    item_icon = ""
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
    compare(item_icon, icon_list[r])
    bp.click_position([0.5, 0.1])
    print("click_pack_icon_test点击图标测试通过")

def FishCardPanel_test(bp: BasePage):
    # HomePanel.go_to_FishCardPanel(bp)
    bp.set_item_count(target_count=1234567890, item_tpid="100000")
    r = random.randint(0, 166)
    num_str = str(r).zfill(3)
    bp.cmd(f"add 10 1000{num_str} 500000")
    bp.cmd(f"add 10 1000008 500000")
    bp.go_to_panel("FishCardPanel")
    select_card_test(bp)
    level_up_test(bp)
    FishCardGiftPackPanel_test(bp)
    FishCardPanel.click_btn_close(bp)

if __name__ == "__main__":
    bp = BasePage()
    # FishCardPanel.click_btn_upgrade(bp)
    FishCardPanel_test(bp)




