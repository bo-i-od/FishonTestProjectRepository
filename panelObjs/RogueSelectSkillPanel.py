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



if __name__ == "__main__":
    bp = BasePage()
    RogueSelectSkillPanel.select_skill(bp)
    RogueSelectSkillPanel.click_btn_orange(bp)
    bp.connect_close()