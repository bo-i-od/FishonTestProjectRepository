from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.roulettePanel import RoulettePanel
from configs.elementsData import ElementsData
from tools.commonTools import *
from items import resource

def spin_test(bp: BasePage):
    ticket_expect_count, ticket_cost = RoulettePanel.get_ticket(bp)
    if ticket_expect_count < ticket_cost:
        return False
    ticket_expect_count -= ticket_cost
    bp.sleep(0.5)
    RoulettePanel.click_btn_spin(bp)
    bp.sleep(1)
    ticket_count, ticket_cost = RoulettePanel.get_ticket(bp)
    compare(ticket_expect_count, ticket_count)
    return True

def RoulettePanel_test(bp: BasePage):
    HomePanel.go_to_RoulettePanel(bp)
    if not spin_test(bp):
        RoulettePanel.click_btn_close(bp)
        return
    bp.sleep(5)
    reward_icon_list = RoulettePanel.get_reward_icon_list(bp)
    reward_quantity_list = RoulettePanel.get_reward_quantity_list(bp)
    item_expect_dict = resource.make_item_dict(reward_icon_list, reward_quantity_list)
    stock_quantity_expect_list = bp.get_item_count_list(reward_icon_list)
    print(stock_quantity_expect_list)
    cur = 0
    while cur < len(reward_icon_list):
        stock_quantity_expect_list[cur] += item_expect_dict[reward_icon_list[cur]]
        cur += 1
    RoulettePanel.click_btn_close(bp)
    reward_dict = RewardsPanel.get_reward_dict(bp)
    print(item_expect_dict, reward_dict)
    compare_dict(item_expect_dict, reward_dict)
    stock_quantity_list = bp.get_item_count_list(reward_icon_list)
    print(stock_quantity_expect_list, stock_quantity_list)
    compare(stock_quantity_expect_list, stock_quantity_list)



if __name__ == '__main__':
    bp = BasePage()
    RoulettePanel_test(bp)
