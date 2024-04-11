import random

from common import resource
from tools.commonTools import *
from common.basePage import BasePage
from panelObjs.newbieTaskPanel import NewbieTaskPanel
from panelObjs.partySalePanel import PartySalePanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from panelObjs.rewardsPanel import RewardsPanel

def party_sale_test(bp: BasePage):
    # 点击道具图标
    item_icon_list = PartySalePanel.get_item_icon_list(bp)
    item_quantity_list = PartySalePanel.get_item_quantity_list(bp)
    skip_len = 1

    # 之后需要补充装备的数量测试
    # gear_icon = item_icon_list[0]
    # gear_quantity = item_quantity_list[0]
    item_icon_list = item_icon_list[-(len(item_icon_list) - skip_len):]
    item_quantity_list = item_quantity_list[-(len(item_quantity_list) - skip_len):]
    item_dict = resource.make_item_dict(item_icon_list=item_icon_list, item_quantity_list=item_quantity_list)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)

    # 点击购买
    PartySalePanel.click_btn_buy(bp)
    RewardsPanel.wait_for_panel_appear(bp)

    reward_dict = RewardsPanel.get_reward_dict(bp)
    print("item_dict", item_dict)
    print("reward_dict",reward_dict)
    # compare_dict(item_dict, reward_dict)
    cur = 0
    while cur < len(stock_expect_list):
        stock_expect_list[cur] += item_quantity_list[cur]
        cur += 1

    stock_list = bp.get_item_count_list(item_icon_name_list=item_icon_list)
    print(stock_expect_list, stock_list)
    # compare_list(stock_expect_list, stock_list)

    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)



if __name__ == '__main__':
    bp = BasePage()
    party_sale_test(bp)