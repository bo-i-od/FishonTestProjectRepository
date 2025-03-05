import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from netMsg import csMsgAll
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

def challenge():
    RogueMainStagePanel.click_btn_challenge(bp)
    bp.sleep(1)

def choose_skill():
    skill_list = bp.get_icon_list(element_data=ElementsData.RogueSelectSkillPanel.skill_attribute_list)
    skill_attribute_list = [int(s.split("_")[-1]) for s in skill_list]

    # 选择最强的技能组成新列表
    best_attribute = min(skill_attribute_list)
    best_attribute_list = [i for i, x in enumerate(skill_attribute_list) if x == best_attribute]
    # 随机选择一个下标输出
    index = random.choice(best_attribute_list)
    skill_position_list = bp.get_position_list(element_data=ElementsData.RogueSelectSkillPanel.skill_list)
    bp.click_position(skill_position_list[index])
    # print(f"选择第{index + 1}个技能")
    bp.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_orange)


def choose_challenge():
    challenge_list = bp.get_text_list(element_data=ElementsData.RogueSelectSkillPanel.challenge_list)
    challenge_list = [int(s) for s in challenge_list]
    # 选择怒气值最高/低的事件
    max_challenge = max(challenge_list)
    min_challenge = min(challenge_list)
    index = challenge_list.index(max_challenge)

    challenge_position_list = bp.get_position_list(element_data=ElementsData.RogueSelectSkillPanel.challenge_position_list)
    bp.click_position(challenge_position_list[index])
    # print(f"已选择第{index+1}个事件")
    bp.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_orange)

def main():

    challenge()
    while not bp.exist(element_data=ElementsData.RogueResultPanel.RogueResultPanel):
        test11.fish_once(bp=bp,personality=PersonalityNB())
        bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.centerAnchor,interval=0.5,timeout=10)
        while bp.exist(element_data=ElementsData.RogueSelectSkillPanel.centerAnchor):
            choose_skill()
        bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.challenge,interval=0.5,timeout=10)
        while bp.exist(element_data=ElementsData.RogueSelectSkillPanel.challenge):
            choose_challenge()


if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    kind = 1
    test11.change_gear(kind=kind)
    difficulty = 0
    # 升爬塔难度
    level_up(difficulty=difficulty)
    main()
    bp.connect_close()