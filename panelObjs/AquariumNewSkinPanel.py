from common.basePage import BasePage
from configs.elementsData import ElementsData


class AquariumNewSkinPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumNewSkinPanel.AquariumNewSkinPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumNewSkinPanel.btn_close)

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumNewSkinPanel.btns, element_viewport=ElementsData.AquariumNewSkinPanel.viewport, index=index)

    operation_pool = [
        {"element_data": ElementsData.AquariumNewSkinPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumNewSkinPanel.btns, "func": click_btn, "weight": 2},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)

    # AquariumNewSkinPanel.click_btn_close(bp)

    AquariumNewSkinPanel.click_btn(bp)

    bp.connect_close()