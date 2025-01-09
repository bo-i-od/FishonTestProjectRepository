from common.basePage import BasePage
from configs.elementsData import ElementsData


class AquariumShopBuyPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumShopBuyPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumShopBuyPanel.AquariumShopBuyPanel)

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumShopBuyPanel.btn_list, index=index)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumShopBuyPanel.top_res_btns, index=index)

    operation_pool = [
        {"element_data": ElementsData.AquariumShopBuyPanel.btn_list, "func": click_btn, "weight": 1},
        {"element_data": ElementsData.AquariumShopBuyPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumShopBuyPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # AquariumShopBuyPanel.click_btn(bp)
    AquariumShopBuyPanel.click_btn_close(bp)
    # AquariumShopBuyPanel.click_top_res_btn(bp)
    # AquariumShopBuyPanel.is_panel_active(bp)
    bp.connect_close()