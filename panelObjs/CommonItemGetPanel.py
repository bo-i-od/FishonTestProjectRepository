from common.basePage import BasePage
from configs.elementsData import ElementsData



class CommonItemGetPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.CommonItemGetPanel.btn_close)
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.CommonItemGetPanel.CommonItemGetPanel)

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.CommonItemGetPanel.btn_list, element_viewport=ElementsData.CommonItemGetPanel.viewport, viewport_direction="column", index=index)

    operation_pool = [
        {"element_data": ElementsData.CommonItemGetPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.CommonItemGetPanel.btn_list, "func": click_btn, "weight": 1},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    CommonItemGetPanel.click_btn(bp)
    bp.connect_close()