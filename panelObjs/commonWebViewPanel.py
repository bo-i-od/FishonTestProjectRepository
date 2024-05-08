from common.basePage import BasePage
from configs.elementsData import ElementsData



class CommonWebViewPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.CommonWebView.btn_close)
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.CommonWebView.CommonWebViewPanel)