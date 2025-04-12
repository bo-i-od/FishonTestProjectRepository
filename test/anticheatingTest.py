# 新主线一个普通渔场所有鱼、关卡若干关、爬塔一个难度、旧主线一个普通渔场所有鱼
from panelObjs.ChallengeMainStagePanel import ChallengeMainStagePanel
from panelObjs.MainStageSettlePanel import MainStageSettlePanel
from panelObjs.HomePanelNew import HomePanelNew
from panelObjs.RogueMainStagePanel import RogueMainStagePanel
from panelObjs.RoguePrepare import RoguePrepare
from panelObjs.RogueResultPanel import RogueResultPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from scripts import battleTest
from common.basePage import BasePage

from test import test12,test11
from test.test13 import settle


def new_spot_fish(bp: BasePage, spot_id):

    bp.go_to_spot(spot_id=spot_id)
    fishery_id = bp.spot_id_to_fishery_id(spot_id=spot_id)
    # battleTest.circulate_fish(base_page, fishery_id=fishery_id, is_quick=True)
    battleTest.fish_once(base_page,fishery_id=fishery_id,fish_id=360115,is_quick=True)
    bp.sleep(2)
    BattlePreparePanel.panel_MainStage_daily_prepare.click_btn_gohome(bp)
    bp.sleep(2)

def angler_challenge(bp: BasePage,start,end):
    HomePanelNew.click_btn_menu(bp)
    bp.sleep(2)
    HomePanelNew.click_btn_entrance1(bp)
    cur = start
    while cur <= end:
        index = str(cur)
        if cur < 10:
            index = "0" + index
        bp.cmd(f"setChallenge 1 10000{index}")
        ChallengeMainStagePanel.click_btn_orange(bp)
        battleTest.fish_once(base_page, is_quick=False)
        MainStageSettlePanel.click_btn_blue(bp)
        cur += 1
    ChallengeMainStagePanel.click_btn_close(bp)
    bp.sleep(1)

def rogue(bp:BasePage):
    HomePanelNew.click_btn_menu(bp)
    bp.sleep(1)
    HomePanelNew.click_btn_entrance2(bp)
    bp.custom_cmd("setQTECD 0.8")
    bp.custom_cmd("setQuickQTE 1")
    RogueMainStagePanel.click_btn_challenge(bp)
    bp.sleep(3)
    flag = True
    # flag = True
    while flag is True:
    #     angry_target = RoguePrepare.get_target_num(bp)

        battleTest.fish_once(base_page, is_quick=False)
        bp.sleep(3)
        flag = not RogueResultPanel.is_panel_active(bp)
        # flag = not RogueResultPanel.is_panel_active(bp)
    RogueResultPanel.click_btn_orange(bp)
    bp.sleep(2)
    # RogueMainStagePanel.click_btn_close(bp)
    # bp.sleep(2)
    # HomePanelNew.click_btn_close(bp)

def old_spot_fish(bp:BasePage,fishery_id):
    bp.go_to_fishery(fishery_id=fishery_id)
    battleTest.circulate_fish(base_page, fishery_id=fishery_id, is_quick=True)



if __name__ == '__main__':
    base_page = BasePage(serial_number="127.0.0.1:21533", is_mobile_device=False)
    # 新主线渔场某一钓点钓所有鱼，spot_id是钓点id，在new_plot_fish_spot表里查询
    new_spot_fish(bp=base_page,spot_id='10101')
    # 钓者挑战的关卡范围
    start = 1
    end = 2
    # 钓者挑战
    angler_challenge(bp=base_page,start=start,end=end)
    # 爬塔一个难度
    rogue(bp=base_page)
    # 某一老渔场 钓所有鱼
    old_spot_fish(bp=base_page,fishery_id='400301')
