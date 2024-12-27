from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoadingFisheryPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LoadingFisheryPanel.LoadingFisheryPanel)

    def wait_until_panel_disappear(self):
        while LoadingFisheryPanel.is_panel_active(self):
            self.sleep(0.1)
