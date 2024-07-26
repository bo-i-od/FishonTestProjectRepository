from common.basePage import BasePage
from configs.elementsData import ElementsData


class AvatarSelectPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarSelect.AvatarSelectPanel)

    def click_btn_start(self):
        self.click_element(element_data=ElementsData.AvatarSelect.btn_start)

    def get_gender_icon_position_list(self):
        return self.get_position_list(element_data=ElementsData.AvatarSelect.gender_icon_list)
