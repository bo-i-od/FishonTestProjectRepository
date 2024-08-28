from common.basePage import BasePage
from configs.elementsData import ElementsData


class EventsGiftCenterPanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.EventsGiftCenter.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.EventsGiftCenter.EventsGiftCenterPanel)