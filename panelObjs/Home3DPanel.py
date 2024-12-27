from common.basePage import BasePage
from configs.elementsData import ElementsData


class Home3DPanel(BasePage):
    def click_panel_entrance_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.Home3DPanel.panel_entrance_btns, index=index)

    def click_btn_avatar(self):
        self.click_element(element_data=ElementsData.Home3DPanel.btn_avatar)

    def click_btn_chest(self):
        self.click_element(element_data=ElementsData.Home3DPanel.btn_chest)

    operation_pool = [
        {"element_data": ElementsData.Home3DPanel.panel_entrance_btns, "func": click_panel_entrance_btn, "weight": 1},
        {"element_data": ElementsData.Home3DPanel.btn_avatar, "func": click_btn_avatar, "weight": 1},
        {"element_data": ElementsData.Home3DPanel.btn_chest, "func": click_btn_chest, "weight": 1},
        ]
