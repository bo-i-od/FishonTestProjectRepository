from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattleExplainPanel(BasePage):
    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.BattleExplain.BattleExplainPanel)
