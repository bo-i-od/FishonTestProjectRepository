from common.basePage import BasePage
from configs.elementsData import ElementsData


class GearSkillTipsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.GearSkillTipsPanel.GearSkillTipsPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearSkillTipsPanel.btn_close)

    def get_skill_icon(self):
        skill_icon = self.get_icon(element_data=ElementsData.GearSkillTipsPanel.skill_icon)
        return skill_icon


    operation_pool = [
        {"element_data": ElementsData.GearSkillTipsPanel.btn_close, "func": click_btn_close, "weight": 10},

    ]
if __name__ == "__main__":
    bp = BasePage()
    GearSkillTipsPanel.click_btn_close(bp)
    bp.connect_close()