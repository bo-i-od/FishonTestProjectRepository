from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoginPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Login.LoginPanel):
            return True
        return False
    def click_btn_login(self):
        self.click_element(element_data=ElementsData.Login.btn_login)

    def set_login_name(self, login_name):
        self.set_text(element_data=ElementsData.Login.InputField_UserName, text=login_name)

    def get_login_name(self):
        login_name = self.get_text(element_data=ElementsData.Login.InputField_UserName)
        return login_name

