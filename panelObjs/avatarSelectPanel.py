from common.basePage import BasePage
from configs.elementsData import ElementsData


class AvatarSelectPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarSelect.AvatarSelectPanel)

    def wait_for_panel_appear(self):
        while not AvatarSelectPanel.is_panel_active(self):
            self.sleep(1)

    def click_btn_start(self, is_ray_input=False):
        if is_ray_input:
            self.ray_input(target_name="btn_start", element_data=ElementsData.AvatarSelect.btn_start, kind="click")
            return
        self.click_element(element_data=ElementsData.AvatarSelect.btn_start)

    def get_gender_icon_position_list(self):
        return self.get_position_list(element_data=ElementsData.AvatarSelect.gender_icon_list)

    def click_first_icon(self, is_ray_input=False):
        if is_ray_input:
            self.ray_input(target_name="1", kind="click", element_data=ElementsData.AvatarSelect.gender_icon_list)
            return
        position_list = self.get_position_list(element_data=ElementsData.AvatarSelect.gender_icon_list)
        self.click_position(position_list[0])
