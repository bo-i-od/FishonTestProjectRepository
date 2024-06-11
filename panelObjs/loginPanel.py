from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoginPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Login.LoginPanel):
            return True
        return False

    def is_btn_login_active(self):
        if self.exist(element_data=ElementsData.Login.btn_login) or self.exist(element_data=ElementsData.Login.btn_login_cn) :
            return True
        return False

    def wait_for_btn_login(self):
        while not LoginPanel.is_btn_login_active(self):
            self.sleep(0.5)

    def click_btn_login(self):
        self.click_until_disappear(element_data=ElementsData.Login.btn_login, interval=2)

    def click_btn_login_cn(self):
        self.click_until_disappear(element_data=ElementsData.Login.btn_login_cn)

    def set_login_name(self, login_name):
        self.set_text(element_data=ElementsData.Login.InputField_UserName, text=login_name)

    def get_login_name(self):
        login_name = self.get_text(element_data=ElementsData.Login.InputField_UserName)
        return login_name

    def set_server(self, index):
        self.set_dropdown_value(element_data=ElementsData.Login.Dropdown, index=index)

