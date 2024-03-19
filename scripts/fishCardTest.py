import random

from common.basePage import BasePage
from panelObjs.achievementPopupPanel import AchievementPopupPanel
from panelObjs.commonItemGetPanel import CommonItemGetPanel
from panelObjs.fishCardPanel import FishCardPanel
from panelObjs.fishCardUpgradePanel import FishCardUpgradePanel
from panelObjs.homePanel import HomePanel
from panelObjs.flashTipsPanel import FlashTipsPanel
from panelObjs.fishCardGiftPackPanel import FishCardGiftPackPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.storePanel import StorePanel
from common import resource, gameInit
from tools.commonTools import *
def FishCardUpgradePanel_test(bp: BasePage):
    # 比较卡面和右侧面板数值
    card_information_now = FishCardUpgradePanel.get_card_information(bp)
    level_up_information_now = FishCardUpgradePanel.get_level_up_information(bp)
    compare(card_information_now["level"], level_up_information_now["level_now"])
    compare(level_up_information_now["level_now"] + 1, level_up_information_now["level_next"])
    # compare(card_information_now["progress_numerator"], level_up_information_now["progress_numerator"])
    # compare(card_information_now["progress_denominator"], level_up_information_now["progress_denominator"])
    # compare(card_information_now["talent"], level_up_information_now["talent_val_now_list"][0])
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
    if level_up_information_now["level_next"] == 50:
        return
    # 比较卡牌和面板数值
    card_information_next = FishCardUpgradePanel.get_card_information(bp)
    level_up_information_next = FishCardUpgradePanel.get_level_up_information(bp)
    compare(card_information_next["level"], level_up_information_next["level_now"])
    compare(level_up_information_next["level_now"] + 1, level_up_information_next["level_next"])
    # compare(card_information_next["talent"], level_up_information_next["talent_val_now_list"][0])
    # 比较升级前后数值
    progress_expect = level_up_information_now["progress_numerator"] - level_up_information_now["progress_denominator"]
    compare(progress_expect, level_up_information_next["progress_numerator"])
    cur = 0
    while cur < len(level_up_information_now["talent_val_now_list"]):
        talent_val_expect = level_up_information_now["talent_val_next_list"][cur]
        compare(talent_val_expect, level_up_information_next["talent_val_now_list"][cur])
        cur += 1
    print("level_up_test升级测试通过")
    # return card_information_next

# def check_information_test(bp: BasePage):
#     card_information = FishCardPanel.get_card_information(bp)
#     main_name, main_size = FishCardPanel.get_main_name_and_size(bp)
#     compare(main_name, card_information["fish_name"])
#     size_expect = FishCardPanel.bg_to_tier(card_information["title_bg"])
#     compare(size_expect, main_size)
#     return card_information

def level_up_test(bp: BasePage):
    # check_information_test(bp)
    # FishCardPanel.click_btn_upgrade(bp)
    # 跳转商店
    FishCardUpgradePanel.click_btn_add_100000(bp)
    bp.sleep(1)
    StorePanel.click_btn_close(bp)
    bp.sleep(1)
    # 升到不能再升
    while FishCardUpgradePanel.is_btn_level_up_abled(bp):
        # FishCardUpgradePanel.level_up_check(bp)
        FishCardUpgradePanel_test(bp)
        bp.sleep(0.5)
        # card_information_now = FishCardUpgradePanel.get_card_information(bp)
        # compare(card_information, card_information_now)
    FishCardUpgradePanel.click_btn_close(bp)
    if FishCardGiftPackPanel.is_panel_active(bp):
        FishCardGiftPackPanel.click_btn_close(bp)


def select_card_test(bp: BasePage):
    # 选择未解锁的卡片
    FishCardPanel.switch_tab(bp, 0)
    FishCardPanel.switch_sub_tab(bp, 0)
    bp.sleep(1)
    unlock_list, unlevelable_list, levelable_list = FishCardPanel.get_card_status(bp)
    if unlock_list:
        r = random.randint(0, len(unlock_list) - 1)
        FishCardPanel.select_card(bp, unlock_list[r])
        bp.sleep(1)
    card_monster_count = len(unlock_list) + len(unlevelable_list) + len(levelable_list)
    FishCardPanel.switch_sub_tab(bp, 1)
    bp.sleep(1)
    unlock_list, unlevelable_list, levelable_list = FishCardPanel.get_card_status(bp)
    card_normal_count = len(unlock_list) + len(unlevelable_list) + len(levelable_list)
    if card_monster_count >= card_normal_count:
        raise CompareError


    # 选择不可升级的卡片
    FishCardPanel.switch_tab(bp, 1)
    bp.sleep(1)
    unlock_list, unlevelable_list, levelable_list = FishCardPanel.get_card_status(bp)
    if unlevelable_list:
        r = random.randint(0, len(unlevelable_list) - 1)
        FishCardPanel.select_card(bp, unlevelable_list[r])
        bp.sleep(1)
        FishCardUpgradePanel.click_btn_level_up(bp)
        bp.sleep(1)
        CommonItemGetPanel.click_btn_close(bp)
        bp.sleep(1)
        FishCardUpgradePanel.click_btn_close(bp)

    # 选择未解锁渔场
    unlock_tab_list, lock_tab_list = FishCardPanel.get_tab_status(bp)
    if lock_tab_list:
        r = random.randint(0, len(lock_tab_list) - 1)
        FishCardPanel.switch_tab(bp, lock_tab_list[r])
        bp.sleep(1)
        card_status = FishCardPanel.get_card_status(bp)
        compare((unlock_list, unlevelable_list, levelable_list), card_status)

    # 选择可升级的卡片
    FishCardPanel.switch_tab(bp, 2)
    bp.sleep(1)
    unlock_list, unlevelable_list, levelable_list = FishCardPanel.get_card_status(bp)
    if levelable_list:
        r = random.randint(0, len(levelable_list) - 1)
        FishCardPanel.select_card(bp, levelable_list[r])

    # 左右切换卡片
    card_information_0 = FishCardUpgradePanel.get_card_information(bp)
    FishCardUpgradePanel.click_btn_previous(bp)
    bp.sleep(1)
    card_information_1 = FishCardUpgradePanel.get_card_information(bp)
    if card_information_0 == card_information_1:
        raise SameError
    FishCardUpgradePanel.click_btn_next(bp)
    bp.sleep(1)
    card_information_2 = FishCardUpgradePanel.get_card_information(bp)
    compare(card_information_0, card_information_2)
    print("select_card_test选择卡片测试通过")

def a_test(bp: BasePage):
    card_information_0 = FishCardUpgradePanel.get_card_information(bp)
    FishCardUpgradePanel.click_btn_previous(bp)
    bp.sleep(1)
    card_information_1 = FishCardUpgradePanel.get_card_information(bp)
    if card_information_0 == card_information_1:
        raise SameError
    FishCardUpgradePanel.click_btn_next(bp)
    bp.sleep(1)
    card_information_2 = FishCardUpgradePanel.get_card_information(bp)
    compare(card_information_0, card_information_2)

def FishCardGiftPackPanel_test(bp: BasePage):
    # 鱼卡的图标保存在一对多的情况，因此不做后端数据的验证
    FishCardPanel.click_btn_events(bp)
    bp.sleep(1)
    icon_list = FishCardGiftPackPanel.get_item_icon_list(bp)
    quantity_list = FishCardGiftPackPanel.get_item_quantity_list(bp)
    click_pack_icon_test(bp, icon_list)
    resource.str_to_int_list(quantity_list)
    item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
    # item_count_expect_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    # cur = 0
    # while cur < len(item_count_expect_list):
    #     item_count_expect_list[cur] += quantity_list[cur]
    #     cur += 1
    FishCardGiftPackPanel.click_btn_buy(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_dict, reward_dict)
    # item_count_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    # compare_list(item_count_expect_list, item_count_list)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
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
    bp.click_position_base([0.9, 0.1])
    print("click_pack_icon_test点击图标测试通过")

def click_tips_test(bp: BasePage):
    FishCardPanel.click_btn_i(bp)
    if not FishCardPanel.is_tips_cardbonus_active(bp):
        raise FindNoElementError
    FishCardPanel.click_btn_i(bp)
    if FishCardPanel.is_tips_cardbonus_active(bp):
        raise FindElementError

def main(bp: BasePage):
    # 进入大厅
    r1 = random.randint(8, 22)
    r2 = random.randint(23, 37)
    cmd_list = ["guideskip", "add 1 100000 1234567890", "add 1 100200 123456", f"add 10 1000{str(r1).zfill(3)} 1", f"add 10 1000{str(r2).zfill(3)} 500000"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # 进入鱼卡系统
    bp.go_to_panel("FishCardPanel")

    # 等待成就跳转消失
    AchievementPopupPanel.wait_for_panel_disappear(bp)

    select_card_test(bp)
    level_up_test(bp)
    FishCardGiftPackPanel_test(bp)
    FishCardPanel.click_btn_close(bp)


if __name__ == "__main__":
    bp = BasePage()
    main(bp)




