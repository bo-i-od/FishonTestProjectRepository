from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoadingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Loading.LoadingPanel)

    def wait_until_panel_disappear(self, is_wait_for_appear=True):
        if is_wait_for_appear:
            self.wait_for_appear(element_data=ElementsData.Loading.LoadingPanel, ignore_set={"LoadingPanel"})
        while LoadingPanel.is_panel_active(self):
            self.sleep(0.1)