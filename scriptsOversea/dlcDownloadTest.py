import random

from common import gameInit
from common.basePage import BasePage
from panelObjs.DLCDownloadPanel import DLCDownloadPanel_oversea
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from tools.commonTools import *

def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)
    # 进入界面
    bp.go_to_panel("DLCDownloadPanel_oversea")
    bp.sleep(1)

    # 随机点击图标
    reward_icon_list = DLCDownloadPanel_oversea.get_reward_icon_list(bp)
    reward_icon_position_list = DLCDownloadPanel_oversea.get_reward_icon_position_list(bp)
    r = random.randint(0, len(reward_icon_position_list) - 1)
    bp.click_position(reward_icon_position_list[r])
    item_icon = ItemTipsPanel.get_item_icon(bp)
    compare(reward_icon_list[r], item_icon)
    bp.click_position([0.5, 0.1])

    # 点击领取
    item_dict_list = DLCDownloadPanel_oversea.get_item_dict_list(bp)
    btn_claim_position_list = DLCDownloadPanel_oversea.get_btn_claim_position_list(bp)
    cur = 0
    while cur < len(item_dict_list):
        if not btn_claim_position_list[cur]:
            cur += 1
            continue
        claim_once_test(bp, item_dict_list, btn_claim_position_list, cur)
        cur += 1

    # 关闭界面
    DLCDownloadPanel_oversea.click_btn_close(bp)

def claim_once_test(bp: BasePage, item_dict_list, btn_claim_position_list, index):
    # 计算期望
    item_dict = item_dict_list[index]
    icon_list = list(item_dict)
    stock_expect_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    cur = 0
    while cur < len(icon_list):
        stock_expect_list[cur] += item_dict[icon_list[cur]]
        cur += 1

    # 点击领取
    btn_claim_position = btn_claim_position_list[index]
    bp.click_position(btn_claim_position)
    bp.sleep(1)

    # 对比奖励
    reward_dict = RewardsPanel.get_reward_dict(bp)
    compare_dict(item_dict_list[index], reward_dict)

    # 对比库存
    stock_list = bp.get_item_count_list(item_icon_name_list=icon_list)
    compare_list(stock_expect_list, stock_list)

    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    btn_claim_position_list = DLCDownloadPanel_oversea.get_btn_claim_position_list(bp)
    if btn_claim_position_list[index]:
        raise FindElementError



if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21533", is_mobile_device=False)
    main(bp)
    bp.connect_close()