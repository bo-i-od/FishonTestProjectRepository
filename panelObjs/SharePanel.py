from common.basePage import BasePage
from configs.elementsData import ElementsData

class SharePanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.SharePanel.btn_close, ignore_set={"SharePanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.SharePanel.SharePanel)

    def click_btn_share(self):
        self.click_element(element_data=ElementsData.SharePanel.btn_share)

    operation_pool = [
        {"element_data": ElementsData.SharePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.SharePanel.btn_share, "func": click_btn_share, "weight": 1},

        ]

if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)