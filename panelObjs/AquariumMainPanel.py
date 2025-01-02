from common.basePage import BasePage
from configs.elementsData import ElementsData


class AquariumMainPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumMainPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumMainPanel.AquariumMainPanel)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumMainPanel.top_res_btns, index=index)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.AquariumMainPanel.btn_i)

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumMainPanel.btns, index=index)

    def click_btn_change(self):
        self.click_element(element_data=ElementsData.AquariumMainPanel.btn_change)

    def click_btn_collect(self):
        self.click_element(element_data=ElementsData.AquariumMainPanel.btn_collect)

    def click_btn_close_level_up(self):
        self.click_element(element_data=ElementsData.AquariumMainPanel.btn_close_level_up)



    operation_pool = [
        {"element_data": ElementsData.AquariumMainPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumMainPanel.btns, "func": click_btn, "weight": 4},
        {"element_data": ElementsData.AquariumMainPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.AquariumMainPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
        {"element_data": ElementsData.AquariumMainPanel.top_res_btns, "func": click_btn_change, "weight": 2},
        {"element_data": ElementsData.AquariumMainPanel.btn_collect, "func": click_btn_collect, "weight": 2},
        {"element_data": ElementsData.AquariumMainPanel.btn_close_level_up, "func": click_btn_close_level_up, "weight": 1},

        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)

    # AquariumMainPanel.click_btn(bp)

    # AquariumMainPanel.click_btn_i(bp)
    #
    # AquariumMainPanel.click_top_res_btn(bp)
    #
    # AquariumMainPanel.click_btn_change(bp)
    #
    # AquariumMainPanel.click_btn_close(bp)

    # AquariumMainPanel.click_btn_collect(bp)

    AquariumMainPanel.click_btn_close_level_up(bp)

    bp.connect_close()