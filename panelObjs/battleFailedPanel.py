from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattleFailedPanel(BasePage):
    def click_leave(self):
        self.click_until_disappear(element_data=ElementsData.BattleFailed.btn_cancel)

    def click_cast_again(self):
        self.click_until_disappear(element_data=ElementsData.BattleFailed.btn_again)
