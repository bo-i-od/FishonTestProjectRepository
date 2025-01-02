from common.basePage import BasePage
from configs.elementsData import ElementsData

class LoginAnnouncementPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.LoginAnnouncementPanel.LoginAnnouncementPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.LoginAnnouncementPanel.btn_close)
