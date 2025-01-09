from common.basePage import BasePage
from configs.elementsData import ElementsData

class FisheryUnlockPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FisheryUnlockPanel.btn_close, ignore_set={"FisheryUnlockPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FisheryUnlockPanel.FisheryUnlockPanel)

    def click_btn_go(self):
        self.click_element(element_data=ElementsData.FisheryUnlockPanel.btn_go, ignore_set={"FisheryUnlockPanel"})

    operation_pool = [
        {"element_data": ElementsData.FisheryUnlockPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FisheryUnlockPanel.btn_go, "func": click_btn_go, "weight": 1},
        # {"element_data": ElementsData.FisheryUnlockPanel., "func": is_panel_active, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # FisheryUnlockPanel.click_btn_close(bp)
    FisheryUnlockPanel.click_btn_go(bp)
    # FisheryUnlockPanel.is_panel_active(bp)
    bp.connect_close()