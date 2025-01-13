from common.basePage import BasePage
from configs.elementsData import ElementsData

class BattleResultSharePanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.BattleResultSharePanel.btn_close, ignore_set={"BattleResultSharePanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattleResultSharePanel.BattleResultSharePanel)

    def click_btn_share(self):
        self.click_element(element_data=ElementsData.BattleResultSharePanel.btn_share)

    operation_pool = [
        {"element_data": ElementsData.BattleResultSharePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.BattleResultSharePanel.btn_share, "func": click_btn_share, "weight": 1},

        ]
if __name__ == "__main__":
    bp = BasePage()
    # BattleResultSharePanel.click_btn_close(bp)
    BattleResultSharePanel.click_btn_share(bp)
    # BattleResultSharePanel.is_panel_active(bp)
    bp.connect_close()