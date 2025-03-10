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


def level_up(fish_kind,difficulty):
    cur = 0
    while cur < difficulty:
        RogueMainStagePanel.click_btn_challenge(bp)
        bp.sleep(1)
        bp.cmd(f"towerPass 1 {fish_kind} 3 10000")
        bp.wait_for_appear(element_data=ElementsData.RogueResultPanel.RogueResultPanel)
        RogueResultPanel.click_btn_orange(bp)
        bp.sleep(1)
        RogueMainStagePanel.panel_tips_up.click_btn_close(bp)
        bp.sleep(1)
        cur += 1


def settle(bp: BasePage, flag, angry_target):
    t = 0
    while t < 3:
        object_id_list = bp.get_object_id_list(element_data_list=[ElementsData.RogueResultPanel.RogueResultPanel,
                                                                  ElementsData.RogueSelectSkillPanel.centerAnchor,
                                                                  ElementsData.RogueSelectSkillPanel.challenge])
        if object_id_list[0]:
            flag = False
            print(flag)
            return flag
        if object_id_list[1]:
            bp.sleep(2)
            RogueSelectSkillPanel.choose_skill(bp)
            continue
        if object_id_list[2]:
            bp.sleep(2)
            angry_now = RogueSelectSkillPanel.get_now_num(bp)
            RogueSelectSkillPanel.choose_challenge(bp, angry_target=angry_target, angry_now=angry_now)
            continue
        bp.sleep(1)
        t += 1
    flag = True
    return flag

def main(bp:BasePage):
    bp.custom_cmd("setQTECD 0.8")
    bp.custom_cmd("setQuickQTE 1")
    RogueMainStagePanel.click_btn_challenge(bp)
    bp.sleep(3)
    flag = True
    while flag is True:
        angry_target = RoguePrepare.get_target_num(bp)
        test11.fish_once(bp=bp, personality=PersonalityNB())
        bp.set_time_scale(time_scale=time_scale)
        flag = settle(bp, flag, angry_target)
        print(flag)



if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    bp.is_time_scale = True

    time_scale = 4
    gear_lv = 255
    # 1力 2敏 3智
    fish_kind = 2
    bp.set_time_scale(time_scale=time_scale)
    # 套装0-9
    # 0.初始 1.强力收线/强力爆气 2.强力回拉/强力刺鱼 3.技巧拔竿/技巧压制 4.超负荷气 5.长线绝杀 6.不动如山 7.乘胜追击 8.背水一战 9.一刺入魂
    gear_kind = 6
    test11.change_gear(bp=bp,kind=gear_kind)
    difficulty =3
    # 升爬塔难度
    # bp.cmd(f"towerReset 1 {fish_kind} 3")
    level_up(fish_kind=fish_kind,difficulty=difficulty)
    main(bp=bp)
    bp.sleep(2)
    RogueResultPanel.result(bp,gear_lv=gear_lv,kind=fish_kind)
    bp.connect_close()