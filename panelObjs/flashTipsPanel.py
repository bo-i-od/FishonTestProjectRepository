from common.basePage import BasePage
from configs.elementsData import ElementsData


class FlashTipsPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.FlashTips.FlashTipsPanel):
            return True
        return False