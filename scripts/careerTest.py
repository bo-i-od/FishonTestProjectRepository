from common import gameInit
from common.basePage import BasePage
from panelObjs.careerPanel import CareerPanel
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.storePanel import StorePanel


def enhance_test(bp: BasePage):
    res = True
    cost_dict = CareerPanel.get_cost_dict(bp)
    cost_icon_list = list(cost_dict)
    item_count_list = bp.get_item_count_list(item_icon_name_list=cost_icon_list)
    stock_expect_list = item_count_list.copy()
    # 计算期望数量
    cur = 0
    while cur < len(cost_icon_list):
        if cost_dict[cost_icon_list[cur]] > item_count_list[cur]:
            res = False
            break
        cur += 1
        # 计算期望库存
        stock_expect_list[cur] -= cost_dict[cost_icon_list[cur]]
        cur += 1

    #
    rating = CareerPanel.get_rating(bp)
    rating_total = CareerPanel.get_rating_total(bp)
    lv = CareerPanel.get_item_lv(bp)

    # 点击突破
    CareerPanel.click_btn_enhance(bp)
    bp.sleep(0.5)
    if not res:
        stock_expect_list = item_count_list.copy()
        MessageBoxPanel.click_btn_confirm(bp)
        bp.sleep(0.5)



def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["guideskip", "levelupto 10"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # 点击？
    CareerPanel.click_btn_i(bp)
    bp.sleep(0.5)
    if not CareerPanel.is_tips_active(bp):
        bp.debug_log("erro_", "if not CareerPanel.is_tips_active(bp)")
    bp.click_position([0.5, 0.1])
    bp.sleep(0.5)

    # 点击金币+
    CareerPanel.click_btn_add_100000(bp)
    bp.sleep(0.5)
    StorePanel.click_btn_close(bp)
    bp.sleep(0.5)

    # 点击突破


if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20066")