from common.basePage import BasePage
from configs.elementsData import ElementsData



class CommonWebViewPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.CommonWebViewPanel.btn_close)

    def wait_for_btn_close_appear(self):
        self.wait_for_appear(element_data=ElementsData.CommonWebViewPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.CommonWebViewPanel.CommonWebViewPanel)

    operation_pool = [
        {"element_data": ElementsData.CommonWebViewPanel.btn_close, "func": click_btn_close, "weight": 1},
        ]

if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)

    bp.connect_close()