import random

from common.basePage import BasePage
from configs.elementsData import ElementsData


class RogueSelectSkillPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RogueSelectSkillPanel.RogueSelectSkillPanel)

    def click_btn_orange(self):
        self.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_orange, ignore_set={"RogueSelectSkillPanel"})

    def click_btn_blue(self):
        self.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_blue, ignore_set={"RogueSelectSkillPanel"})

    def select_skill(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RogueSelectSkillPanel.skill_list, index=index, ignore_set={"RogueSelectSkillPanel"})

    def choose_skill(self):
        self.wait_for_appear(element_data=ElementsData.RogueSelectSkillPanel.skill_attribute_list, interval=0.5,timeout=10)
        skill_list = self.get_icon_list(element_data=ElementsData.RogueSelectSkillPanel.skill_attribute_list)
        skill_attribute_list = [int(s.split("_")[-1]) for s in skill_list]
        # print(skill_list)
        # print(skill_attribute_list)
        # 选择最强的技能组成新列表
        best_attribute = min(skill_attribute_list)
        best_attribute_list = [i for i, x in enumerate(skill_attribute_list) if x == best_attribute]
        # 随机选择一个下标输出
        index = random.choice(best_attribute_list)
        skill_position_list = self.get_position_list(element_data=ElementsData.RogueSelectSkillPanel.skill_list)
        self.click_position(skill_position_list[index])
        # print(f"选择第{index + 1}个技能")
        self.click_element(element_data=ElementsData.RogueSelectSkillPanel.btn_orange)

    def choose_challenge(self,angry_target, angry_now):
        challenge_list = self.get_text_list(element_data=ElementsData.RogueSelectSkillPanel.challenge_list)
        challenge_list = [int(s) for s in challenge_list]
        choose_num = 0
        # 选择怒气值最高/低的事件
        max_challenge = max(challenge_list)
        if (angry_target - angry_now) > max_challenge:
            choose_num = max_challenge
        else:
            choose_num = angry_target - angry_now
        index = challenge_list.index(choose_num)

        challenge_position_list = self.get_position_list(element_data=ElementsData.RogueSelectSkillPanel.challenge_position_list)
        self.click_position(position=challenge_position_list[index])

        # print(f"已选择第{index+1}个事件")
        self.ray_input(kind='click',element_data=ElementsData.RogueSelectSkillPanel.btn_orange)

    def get_now_num(self):
        self.ray_input(kind='click',element_data=ElementsData.RogueSelectSkillPanel.btn_blue)
        num = self.get_text(element_data=ElementsData.RogueShowSkillsPanel.raise_all)
        num = int(num)
        self.click_element(element_data=ElementsData.RogueShowSkillsPanel.btn_close)
        return num



if __name__ == "__main__":
    bp = BasePage()
    RogueSelectSkillPanel.select_skill(bp)
    RogueSelectSkillPanel.click_btn_orange(bp)
    bp.connect_close()


