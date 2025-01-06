from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class GearEnhanceSuccesPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.GearEnhanceSuccesPanel.btn_close, ignore_set={"GearEnhanceSuccesPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.GearEnhanceSuccesPanel.GearEnhanceSuccesPanel)

    def wait_for_panel_appear(self):
        while not GearEnhanceSuccesPanel.is_panel_active(self):
            self.sleep(0.1)

    operation_pool = [
        {"element_data": ElementsData.GearEnhanceSuccesPanel.btn_close, "func": click_btn_close, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    GearEnhanceSuccesPanel.click_btn_close(bp)
    bp.connect_close()