from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoadingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LoadingPanel.LoadingPanel)

    def wait_for_panel_appear(self):
        while True:
            if LoadingPanel.is_panel_active(self):
                break
            self.sleep(1)

    def wait_until_panel_disappear(self, is_wait_for_appear=True):
        if is_wait_for_appear:
            LoadingPanel.wait_for_panel_appear(self)
        while LoadingPanel.is_panel_active(self):
            self.sleep(0.1)