from common.basePage import BasePage
from configs.elementsData import ElementsData


class AvatarSelectPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarSelectPanel.AvatarSelectPanel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.AvatarSelectPanel.AvatarSelectPanel, timeout=5)

    def click_btn_start(self, is_ray_input=False):
        if is_ray_input:
            self.ray_input(element_data=ElementsData.AvatarSelectPanel.btn_start, kind="click")
            return
        self.click_element(element_data=ElementsData.AvatarSelectPanel.btn_start)

    def get_gender_icon_position_list(self):
        return self.get_position_list(element_data=ElementsData.AvatarSelectPanel.gender_icon_list)

    def click_gender_icon(self, is_ray_input=False, index=-1):
        if is_ray_input:
            self.ray_input(kind="click", element_data=ElementsData.AvatarSelectPanel.gender_icon_list)
            return
        self.click_object_of_plural_objects(element_data=ElementsData.AvatarSelectPanel.gender_icon_list, index=index)


    operation_pool = [
        {"element_data": ElementsData.AvatarSelectPanel.gender_icon_list, "func": click_gender_icon, "weight": 2},
        {"element_data": ElementsData.AvatarSelectPanel.btn_start, "func": click_btn_start, "weight": 1},
        ]

if __name__ == '__main__':
    bp = BasePage()
    AvatarSelectPanel.click_btn_start(bp, is_ray_input=True)
    bp.connect_close()