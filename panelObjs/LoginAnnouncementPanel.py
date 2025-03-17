from common.basePage import BasePage
from configs.elementsData import ElementsData

class LoginAnnouncementPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LoginAnnouncementPanel.LoginAnnouncementPanel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.MailPanel.MailPanel, interval=1, timeout=3, ignore_set={"LoginAnnouncementPanel"})

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.LoginAnnouncementPanel.btn_close, ignore_set={"LoginAnnouncementPanel"})

    operation_pool = [
        {"element_data": ElementsData.LoginAnnouncementPanel.btn_close, "func": click_btn_close, "weight": 1},
    ]

if __name__ == "__main__":
    bp = BasePage()
    LoginAnnouncementPanel.click_btn_close(bp)
    bp.connect_close()