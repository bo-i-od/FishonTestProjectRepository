from common.basePage import BasePage
from configs.elementsData import ElementsData


class MainStageFishSpotPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.MainStageFishSpotPanel.MainStageFishSpotPanel)

    def click_btn_go(self):
        self.click_element(element_data=ElementsData.MainStageFishSpotPanel.btn_go)

if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21583")
    MainStageFishSpotPanel.click_btn_go(bp)
    bp.connect_close()
