from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearSkillTipsPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.GearSkillTips.GearSkillTipsPanel):
            return True
        return False

    def get_skill_icon(self):
        skill_icon = self.get_icon(element_data=ElementsData.GearSkillTips.skill_icon)
        return skill_icon