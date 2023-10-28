from common.basePage import BasePage
from configs.elementsData import ElementsData


class FishBagPanel(BasePage):
    def tap_to_continue(self):
        self.click_element(element_data=ElementsData.FishBag.tap_to_continue)



