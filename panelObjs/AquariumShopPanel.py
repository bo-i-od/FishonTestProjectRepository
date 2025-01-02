import random

from common.basePage import BasePage
from common.slider import Slider
from configs.elementsData import ElementsData


class AquariumShopPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AquariumShopPanel.AquariumShopPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_close)

    def click_btn_buy(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumShopPanel.btn_buy_list, element_viewport=ElementsData.AquariumShopPanel.viewport, index=index)

    def click_btn_magnifier(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_magnifier)

    def click_item_icon(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AquariumShopPanel.item_icon_list, element_viewport=ElementsData.AquariumShopPanel.viewport, index=index)

    def click_item_icon_purchase(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.item_icon_purchase)

    def click_btn_close_purchase(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_close_purchase)

    def click_btn_sub(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_sub)

    def click_btn_add(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_add)

    def click_btn_max(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_max)

    def click_btn_min(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_min)

    def click_btn_exchange(self):
        self.click_element(element_data=ElementsData.AquariumShopPanel.btn_exchange)

    def swipe_slider(self, value_start=None, value_end=None):
        if not value_start:
            value_start = random.random()
        if not value_end:
            value_end = random.random()
        slider = Slider(self, element_slider=ElementsData.AquariumShopPanel.slider)
        point_start, point_end = slider.get_slide_point_start_and_end(slide_range=[value_start, value_end])
        if value_start > value_end:
            t = value_start - value_end
        else:
            t = value_end- value_start
        self.swipe(point_start=point_start, point_end=point_end, t=t)

    operation_pool = [
        {"element_data": ElementsData.AquariumShopPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_buy_list, "func": click_btn_buy, "weight": 4},
        {"element_data": ElementsData.AquariumShopPanel.btn_magnifier, "func": click_btn_magnifier, "weight": 2},
        {"element_data": ElementsData.AquariumShopPanel.item_icon_list, "func": click_item_icon, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.item_icon_purchase, "func": click_item_icon_purchase, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_close_purchase, "func": click_btn_close_purchase, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_sub, "func": click_btn_sub, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_add, "func": click_btn_add, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_max, "func": click_btn_max, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_min, "func": click_btn_min, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.slider, "func": swipe_slider, "weight": 1},
        {"element_data": ElementsData.AquariumShopPanel.btn_exchange, "func": click_btn_exchange, "weight": 2},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    # AquariumShopPanel.click_btn_close(bp)

    # AquariumShopPanel.click_btn_buy(bp)
    #
    # AquariumShopPanel.click_btn_magnifier(bp)

    # AquariumShopPanel.click_item_icon_purchase(bp)

    # AquariumShopPanel.click_btn_sub(bp)
    #
    # AquariumShopPanel.click_btn_add(bp)
    #
    # AquariumShopPanel.click_btn_max(bp)
    #
    # AquariumShopPanel.click_btn_min(bp)
    #
    # AquariumShopPanel.click_btn_exchange(bp)

    # AquariumShopPanel.swipe_slider(bp)

    bp.connect_close()
