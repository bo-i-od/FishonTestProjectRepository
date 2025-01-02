from common.basePage import BasePage
from configs.elementsData import ElementsData


class BattleFailedPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattleFailedPanel.BattleFailedPanel)
    def click_upgrade(self):
        self.click_until_disappear(element_data=ElementsData.BattleFailedPanel.btn_upgrade, ignore_set={"BattleFailedPanel"})

    def click_cast_again(self):
        self.click_until_disappear(element_data=ElementsData.BattleFailedPanel.btn_again, ignore_set={"BattleFailedPanel"})

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BattleFailedPanel.btns, index=index)

    operation_pool = [
        {"element_data": ElementsData.BattleFailedPanel.btns, "func": click_btn, "weight": 1},
    ]

if __name__ == '__main__':
    bp = BasePage()
    BattleFailedPanel.click_btn(bp)
    bp.connect_close()