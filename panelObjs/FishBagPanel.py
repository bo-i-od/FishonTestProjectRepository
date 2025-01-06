from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishBagPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishBagPanel.FishBagPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishBagPanel.btn_close, ignore_set={"FishBagPanel"})

    def click_btn_next(self):
        self.click_element(element_data=ElementsData.FishBagPanel.btn_next, ignore_set={"FishBagPanel"})

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.FishBagPanel.FishBagPanel, ignore_set={"FishBagPanel"})

    operation_pool = [
        {"element_data": ElementsData.FishBagPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FishBagPanel.btn_next, "func": click_btn_next, "weight": 1},

        ]



