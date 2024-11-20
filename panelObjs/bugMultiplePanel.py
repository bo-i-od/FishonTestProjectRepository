from common.basePage import BasePage
from common.slider import Slider
from configs.elementsData import ElementsData


class BugMultiplePanel(BasePage):
    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.BugMultiple.btn_cancel)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BugMultiple.BugMultiplePanel)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.BugMultiple.btn_confirm)

    def click_btn_add(self):
        self.click_element(element_data=ElementsData.BugMultiple.btn_add)

    def click_btn_sub(self):
        self.click_element(element_data=ElementsData.BugMultiple.btn_sub)

    def click_btn_max(self):
        self.click_element(element_data=ElementsData.BugMultiple.btn_max)

    def click_btn_min(self):
        self.click_element(element_data=ElementsData.BugMultiple.btn_min)

    def get_drink_icon(self):
        return self.get_icon(element_data=ElementsData.BugMultiple.icon)

    def get_drink_quantity(self):
        drink_quantity = self.get_text(element_data=ElementsData.BugMultiple.quantity)
        return int(drink_quantity)

    def get_drink_value(self):
        drink_value = self.get_text(element_data=ElementsData.BugMultiple.value).split('/')
        drink_cur = drink_value[0]
        drink_max = drink_value[1]
        return int(drink_cur), int(drink_max)

    def click_drink_icon(self):
        return self.click_element(element_data=ElementsData.BugMultiple.icon)

    def get_slider(self):
        return Slider(self, element_slider=ElementsData.BugMultiple.slider)








