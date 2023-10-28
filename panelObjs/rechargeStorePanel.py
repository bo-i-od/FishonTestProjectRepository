from common.basePage import BasePage
from configs.elementsData import ElementsData


class RechargeStorePanel(BasePage):
    def close_RechargeStorePanel(self):
        self.click_until_disappear(element_data=ElementsData.RechargeStore.btn_close)
