from common.basePage import BasePage
from configs.elementsData import ElementsData


class RodMoreToOnePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RodMoreToOnePanel.RodMoreToOnePanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RodMoreToOnePanel.btn_close)

    def click_confirm(self):
        self.click_element(element_data=ElementsData.RodMoreToOnePanel.btn_confirm)

    def get_rod_icon_and_position_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.RodMoreToOnePanel.icon_list)
        position_list = self.get_position_list(element_data=ElementsData.RodMoreToOnePanel.icon_list)
        return icon_list, position_list

    def get_btn_preview_position_list(self):
        btn_preview_position_list = self.get_position_list(element_data=ElementsData.RodMoreToOnePanel.tipsBtn_list)
        return btn_preview_position_list

    def click_rod(self, index=-1):
        self.click_object_of_plural_objects(element_viewport=ElementsData.RodMoreToOnePanel.icon_list, index=index)

    def click_tipsBtn(self, index=-1):
        self.click_object_of_plural_objects(element_viewport=ElementsData.RodMoreToOnePanel.tipsBtn_list, index=index)


    operation_pool = [
        {"element_data": ElementsData.RodMoreToOnePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.RodMoreToOnePanel.btn_confirm, "func": click_confirm, "weight": 1},
        {"element_data": ElementsData.RodMoreToOnePanel.icon_list, "func": click_rod, "weight": 1},
        {"element_data": ElementsData.RodMoreToOnePanel.tipsBtn_list, "func": click_tipsBtn, "weight": 1},

    ]


if __name__ == "__main__":
    bp = BasePage()
    RodMoreToOnePanel.click_btn_close(bp)
    RodMoreToOnePanel.click_confirm(bp)
    RodMoreToOnePanel.click_rod(bp)
    RodMoreToOnePanel.click_tipsBtn(bp)
    bp.connect_close()