# coding=utf-8
from common.basePage import BasePage
from tools.rpcMethod import *
import random

# def test_all():
#     bp = BasePage()
#     # 起名部分的新手引导
#     if PlayerEditNamePanel.is_panel_active(bp):
#         print("在起名界面")
#         guideTest.playerEditNamePanelTest(bp)
#     # 新手引导
#     guideTest.newbieGuidePanelTest(bp)
#     # # 1+1 礼包图标点击测试
#     # if Recharge1And1Panel.is_panel_active(bp):
#     #     recharge1And1Test.click_icon_test(bp)
#     #     Recharge1And1Panel.close_Recharge1And1Panel(bp)
#     # # 1+1 礼包购买测试
#     # recharge1And1Test.buy_test(bp)
#     # Recharge1And1Panel.close_Recharge1And1Panel(bp)
#     # 无尽充值购买测试
#     rechargeEndlessTest.buy_many_test(bp)
#     # 开鱼箱测试
#     treasureChestTest.change_box_test(bp)
#     # 点击鱼箱点鱼箱测试
#     treasureChestTest.get_box_point_box_test(bp)
#     # 点击预览和图标测试
#     treasureChestTest.click_tips_test(bp)
#     # 宝箱商人购买测试
#     treasureChestTest.TreasureChestMerchant_test(bp)



if __name__ == '__main__':
    bp = BasePage()
    cur = 29
    max = 38
    while cur <= max:
        r = random.randint(0,25)
        # bp.set_item_count(target_count=r, item_tpid=f"2000{cur}")
        # print(f"2000{cur}:{r}")
        # bp.sleep(0.1)
        print(bp.get_item_count(item_tpid=f"2000{cur}"))
        bp.sleep(0.1)
        cur += 1









