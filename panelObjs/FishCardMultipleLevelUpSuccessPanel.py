from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishCardMultipleLevelUpSuccessPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardMultipleLevelUpSuccessPanel.FishCardMultipleLevelUpSuccessPanel)

    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.FishCardMultipleLevelUpSuccessPanel.btn_close)

    operation_pool = [
        {"element_data": ElementsData.FishCardMultipleLevelUpSuccessPanel.btn_close, "func": click_btn_close, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    FishCardMultipleLevelUpSuccessPanel.click_btn_close(bp)
    FishCardMultipleLevelUpSuccessPanel.is_panel_active(bp)
    bp.connect_close()