import random
from common.basePage import BasePage
from panelObjs.FisheryGiftPackPanel import FisheryGiftPackPanel
from panelObjs.FishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from panelObjs.BaitAndRodShowPanel import BaitAndRodShowPanel
from tools.commonTools import *
from common import resource


def click_icon_test(bp: BasePage):
    icon_list = FisheryGiftPackPanel.get_item_icon_list(bp)
    position_list = FisheryGiftPackPanel.get_item_position_list(bp)
    r = random.randint(0, 1)
    bp.click_position(position_list[r])
    bp.sleep(0.2)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    r = random.randint(2, len(position_list) - 1)
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, icon_list[r])
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        compare(item_icon, icon_list[r])
    bp.click_position([0.5, 0.9])
    print("click_icon_test点击图标测试通过")

def buy_test(bp: BasePage):
    icon_list = FisheryGiftPackPanel.get_item_icon_list(bp)
    quantity_list = FisheryGiftPackPanel.get_item_quantity_list(bp)
    reward_expect_dict = resource.make_item_dict(icon_list, quantity_list)
    item_count_expect_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    cur = 0
    while cur < len(icon_list):
        item_count_expect_list[cur] += quantity_list[cur]
        cur += 1
    FisheryGiftPackPanel.click_btn_buy(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    item_count_list = bp.get_item_count_list(item_icon_name_list=icon_list)

    compare_dict(reward_expect_dict, reward_dict)

    compare_list(item_count_expect_list, item_count_list)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

if __name__ == "__main__":
    bp = BasePage()
    bp.go_to_panel("FisheryGiftPackPanel")
    click_icon_test(bp)
    buy_test(bp)

