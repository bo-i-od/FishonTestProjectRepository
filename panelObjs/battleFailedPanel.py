from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattleFailedPanel(BasePage):
    def click_upgrade(self):
        self.click_until_disappear(element_data=ElementsData.BattleFailedPanel.btn_upgrade, ignore_set={"BattleFailedPanel"})

    def click_cast_again(self):
        self.click_until_disappear(element_data=ElementsData.BattleFailedPanel.btn_again, ignore_set={"BattleFailedPanel"})

