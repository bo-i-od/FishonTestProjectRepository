from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *


class CommonPurchaseBoxVIew(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.CommonPurchaseBox.btn_close)
        if CommonPurchaseBoxVIew.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.CommonPurchaseBox.CommonPurchaseBoxVIew):
            return True
        return False

    def click_btn_min(self):
        self.click_element(element_data=ElementsData.CommonPurchaseBox.btn_min)

    def click_btn_max(self):
        self.click_element(element_data=ElementsData.CommonPurchaseBox.btn_max)

    def click_btn_add(self):
        self.click_element(element_data=ElementsData.CommonPurchaseBox.btn_add)

    def click_btn_sub(self):
        self.click_element(element_data=ElementsData.CommonPurchaseBox.btn_sub)

    def click_btn_purchase(self):
        self.click_element(element_data=ElementsData.CommonPurchaseBox.btn_purchase)

    def get_item_icon(self):
        item_icon = self.get_icon(element_data=ElementsData.CommonPurchaseBox.item_icon)
        return item_icon

    def get_item_quantity(self):
        item_quantity = self.get_text(element_data=ElementsData.CommonPurchaseBox.item_quantity)
        item_quantity = str_to_int(item_quantity)
        return item_quantity

    def get_cost_icon(self):
        item_icon = self.get_icon(element_data=ElementsData.CommonPurchaseBox.cost_icon)
        return item_icon

    def get_cost_quantity(self):
        item_quantity = self.get_text(element_data=ElementsData.CommonPurchaseBox.cost_quantity)
        item_quantity = str_to_int(item_quantity)
        return item_quantity

    def get_slider(self):
        slider = self.get_slider_value(element_data=ElementsData.CommonPurchaseBox.slider)
        return slider
