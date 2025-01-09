from common.basePage import BasePage
from configs.elementsData import ElementsData


class AquariumNewActivityInnerPopupPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumNewActivityInnerPopupPanel.btn_close, ignore_set={"AquariumNewActivityInnerPopupPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumNewActivityInnerPopupPanel.AquariumNewActivityInnerPopupPanel)

    operation_pool = [
        {"element_data": ElementsData.AquariumNewActivityInnerPopupPanel.btn_close, "func": click_btn_close, "weight": 1},
    ]

if __name__ == '__main__':
    bp = BasePage()
    AquariumNewActivityInnerPopupPanel.click_btn_close(bp)
    bp.connect_close()