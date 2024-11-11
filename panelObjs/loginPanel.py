from common.basePage import BasePage
from configs.elementsData import ElementsData


class LoginPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Login.LoginPanel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.Login.LoginPanel, ignore_set={"LoginPanel"})

    def is_btn_login_active(self):
        object_id_list = self.get_object_id_list(element_data_list=[ElementsData.Login.btn_login,ElementsData.Login.btn_login_cn])
        if object_id_list[0] or object_id_list[1]:
            return True
        return False

    def wait_for_btn_login(self):
        self.wait_for_appear(element_data_list=[ElementsData.Login.btn_login, ElementsData.Login.btn_login_cn], timeout=20)

    def click_btn_login(self):
        btn_login_element = ElementsData.Login.btn_login
        if self.exist(element_data=ElementsData.Login.btn_login_cn):
            btn_login_element = ElementsData.Login.btn_login_cn
        self.click_until_disappear(element_data=btn_login_element, interval=2, ignore_set={"LoginPanel"})

    def is_InputField_UserName_active(self):
        return self.exist(element_data=ElementsData.Login.InputField_UserName)

    def set_login_name(self, login_name):
        self.set_text(element_data=ElementsData.Login.InputField_UserName, text=login_name)

    def get_login_name(self):
        login_name = self.get_text(element_data=ElementsData.Login.InputField_UserName)
        return login_name

    def set_server(self, index):
        self.set_dropdown_value(element_data=ElementsData.Login.Dropdown, index=index)

if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21503", is_mobile_device=False)
    bp.click_element(element_data=ElementsData.Login.btn_login)

    bp.connect_close()
