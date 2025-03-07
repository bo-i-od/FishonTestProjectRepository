import random
import re

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
    bp.sleep(3)

def choose_skill():
    bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.skill_attribute_list, interval=0.5, timeout=10)
    skill_list = bp.get_icon_list(element_data=ElementsData.RogueSelectSkillPanel.skill_attribute_list)
    skill_attribute_list = [int(s.split("_")[-1]) for s in skill_list]
    # print(skill_list)
    # print(skill_attribute_list)
    # 选择最强的技能组成新列表
    best_attribute = min(skill_attribute_list)
    best_attribute_list = [i for i, x in enumerate(skill_attribute_list) if x == best_attribute]
    # 随机选择一个下标输出
    index = random.choice(best_attribute_list)
    skill_position_list = bp.get_position_list(element_data=ElementsData.RogueSelectSkillPanel.skill_list)
    bp.click_position(skill_position_list[index])
    # print(f"选择第{index + 1}个技能")
    bp.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_orange)


def choose_challenge(angry_target, angry_now):
    challenge_list = bp.get_text_list(element_data=ElementsData.RogueSelectSkillPanel.challenge_list)
    challenge_list = [int(s) for s in challenge_list]
    choose_num = 0
    # 选择怒气值最高/低的事件
    max_challenge = max(challenge_list)
    if (angry_target - angry_now) > max_challenge:
        choose_num = max_challenge
    else:
        choose_num = angry_target - angry_now
    index = challenge_list.index(choose_num)

    challenge_position_list = bp.get_position_list(element_data=ElementsData.RogueSelectSkillPanel.challenge_position_list)
    bp.click_position(challenge_position_list[index])
    # print(f"已选择第{index+1}个事件")
    bp.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_orange)

def get_target_num():
    task = bp.get_text(element_data=ElementsData.BattlePreparePanel.rogue_prepare.task03)
    target = re.search(r'总怒火值(?:大于|等于|超过|小于)(\d+\.?\d*)', task)
    if target:
        num = int(target.group(1))
        print(f"目标难度为：{num}")
        return num
    else:
        print("未找到数字")

def get_now_num():
    bp.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_blue)
    num = bp.get_text(element_data=ElementsData.RogueShowSkillsPanel.raise_all)
    num =int(num)
    bp.click_element(element_data=ElementsData.RogueShowSkillsPanel.btn_close)
    return num

def result(gear_lv,kind):
    res = f"{gear_lv}级_"
    if kind == 1:
       res += "力_"
    elif kind == 2:
        res += "敏_"
    elif kind ==3:
        res += "智_"
    if bp.exist(element_data=ElementsData.RogueResultPanel.panel_succeed):
        value = bp.get_text(element_data=ElementsData.RogueResultPanel.succeed_item2_value)
        res += f"难度{value}成功_"
        if bp.exist(element_data=ElementsData.RogueResultPanel.tips):
            res += "无损"
        else:
            res += "非无损"
    elif bp.exist(element_data=ElementsData.RogueResultPanel.panel_lost):
        value = bp.get_text(element_data=ElementsData.RogueResultPanel.lost_item2_value)
        res += f"难度{value}失败"
    print(res)



def main():

    challenge()
    while not bp.exist(element_data=ElementsData.RogueResultPanel.RogueResultPanel):
        angry_target = get_target_num()
        test11.fish_once(bp=bp,personality=PersonalityNB())
        bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.centerAnchor,interval=0.5,timeout=10)
        while bp.exist(element_data=ElementsData.RogueSelectSkillPanel.centerAnchor):
            # bp.sleep(3)
            choose_skill()
        bp.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.challenge,interval=0.5,timeout=10)
        while bp.exist(element_data=ElementsData.RogueSelectSkillPanel.challenge):
            angry_now = get_now_num()
            choose_challenge(angry_target=angry_target, angry_now=angry_now)


if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    gear_lv = 90
    kind = 2
    # test11.change_gear(bp=bp,kind=kind)
    difficulty = 0
    # 升爬塔难度
    # level_up(difficulty=difficulty)
    # main()
    result(gear_lv=gear_lv,kind=kind)
    bp.connect_close()