from common.basePage import BasePage
from configs.elementsData import ElementsData

class PVPMatchPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVPMatchPanel.PVPMatchPanel)

    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.PVPMatchPanel.btn_cancel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.PVPMatchPanel.PVPMatchPanel, ignore_set={"PVPMatchPanel"})


    operation_pool = [
        {"element_data": ElementsData.PVPMatchPanel.btn_cancel, "func": click_btn_cancel, "weight": 1},
    ]


if __name__ == '__main__':
    bp = BasePage("R5CT22NJ44H")
    PVPMatchPanel.click_btn_cancel(bp)