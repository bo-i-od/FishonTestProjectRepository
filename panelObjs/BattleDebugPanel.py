from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattleDebugPanel(BasePage):
    def get_hold_status(self):
        text_list = self.get_text_list(element_data=ElementsData.BattleDebugPanel.hold_status)
        if not text_list:
            return
        return text_list[0]
