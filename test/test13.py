import random
import re

from common.basePage import BasePage
from configs.elementsData import ElementsData
from netMsg import csMsgAll
from panelObjs.RoguePrepare import RoguePrepare
from panelObjs.RogueSelectSkillPanel import RogueSelectSkillPanel
from panelObjs.RogueMainStagePanel import RogueMainStagePanel
from panelObjs.RogueResultPanel import RogueResultPanel
from test import test11
from test.test11 import PersonalityNB


def level_up(difficulty):
    cur = 0
    while cur < difficulty:
        RogueMainStagePanel.click_btn_challenge(bp)
        bp.sleep(1)
        bp.cmd("towerPass 1 1 3 10000")
        bp.wait_for_appear(element_data=ElementsData.RogueResultPanel.RogueResultPanel)
        RogueResultPanel.click_btn_orange(bp)
        bp.sleep(1)
        RogueMainStagePanel.panel_tips_up.click_btn_close(bp)
        bp.sleep(1)
        cur += 1





def main(bp:BasePage):
    RogueMainStagePanel.click_btn_challenge(bp)
    bp.sleep(3)
    while not bp.exist(element_data=ElementsData.RogueResultPanel.RogueResultPanel):
        angry_target = RoguePrepare.get_target_num(bp)
        test11.fish_once(bp=bp, personality=PersonalityNB())
        bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.centerAnchor,interval=0.5,timeout=10)
        while bp.exist(element_data=ElementsData.RogueSelectSkillPanel.centerAnchor):
            # bp.sleep(3)
            RogueSelectSkillPanel.choose_skill(bp)
        bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.challenge,interval=0.5,timeout=10)
        while bp.exist(element_data=ElementsData.RogueSelectSkillPanel.challenge):
            angry_now = RogueSelectSkillPanel.get_now_num(bp)
            RogueSelectSkillPanel.choose_challenge(bp,angry_target=angry_target, angry_now=angry_now)


if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    gear_lv = 30
    kind = 3
    # test11.change_gear(bp=bp,kind=kind)
    difficulty = 0
    # 升爬塔难度
    # level_up(difficulty=difficulty)
    # main(bp=bp)
    RogueResultPanel.result(bp,gear_lv=gear_lv,kind=kind)
    bp.connect_close()