from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishBagPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishBag.FishBagPanel)

    def click_tap_to_continue(self):
        while FishBagPanel.is_panel_active(self):
            self.click_element_safe(element_data=ElementsData.FishBag.btn_close)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.FishBag.FishBagPanel, ignore_set={"FishBagPanel"})



