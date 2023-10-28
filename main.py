# coding=utf-8
from poco.drivers.unity3d import UnityPoco
from common.basePage import BasePage
from tools.rpcMethod import *
from panelObjs.homePanel import HomePanel
from panelObjs.treasureChestPanel import TreasureChestPanel
from panelObjs.gearPanel import GearPanel
from panelObjs.playerSettingPanel import PlayerSettingPanel
from panelObjs.tournamentsPanel import TournamentsPanel
from panelObjs.battlePanel import BattlePanel
from panelObjs.battlePreparePanel import BattlePreparePanel
from panelObjs.resultPanel import ResultPanel
from panelObjs.taskPanel import TaskPanel
from panelObjs.battlePassIntroPanel import BattlePassIntroPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
from panelObjs.recharge1And1Panel import Recharge1And1Panel
from panelObjs.rechargeEndlessPanel import RechargeEndlessPanel
from configs.elementsData import ElementsData
import re
import base64
from airtest.core.api import connect_device
from scripts import battleTest, guideTest, resultTest, rechargeEndlessTest, recharge1And1Test, treasureChestTest

def test_all():
    bp = BasePage()
    # 起名部分的新手引导
    if PlayerEditNamePanel.is_panel_active(bp):
        print("在起名界面")
        guideTest.playerEditNamePanelTest(bp)
    # 新手引导
    guideTest.newbieGuidePanelTest(bp)
    # 1+1 礼包图标点击测试
    if Recharge1And1Panel.is_panel_active(bp):
        recharge1And1Test.click_icon_test(bp)
        Recharge1And1Panel.close_Recharge1And1Panel(bp)
    # 1+1 礼包购买测试
    recharge1And1Test.buy_test(bp)
    Recharge1And1Panel.close_Recharge1And1Panel(bp)
    # 无尽充值购买测试
    rechargeEndlessTest.buy_many_test(bp)
    # 开鱼箱测试
    treasureChestTest.box_quantity_init(bp)
    treasureChestTest.change_box_test(bp)
    # 点击鱼箱点鱼箱测试
    treasureChestTest.get_box_point_box_test(bp)
    # 宝箱商人购买测试
    treasureChestTest.TreasureChestMerchant_test(bp)
    treasureChestTest.jump_test(bp)


if __name__ == '__main__':
    test_all()





