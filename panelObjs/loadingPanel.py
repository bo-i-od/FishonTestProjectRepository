from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoadingPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Loading.LoadingPanel):
            return True
        return False

    def wait_until_panel_disappear(self):
        while LoadingPanel.is_panel_active(self):
            pass