import random

from common.basePage import BasePage
from common.slider import Slider
from configs.elementsData import ElementsData


class BugMultiplePanel(BasePage):
    def click_btn_cancel(self):
        self.click_element(element_data=ElementsData.BugMultiplePanel.btn_cancel)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BugMultiplePanel.BugMultiplePanel)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.BugMultiplePanel.btn_confirm)

    def click_btn_add(self):
        self.click_element(element_data=ElementsData.BugMultiplePanel.btn_add)

    def click_btn_sub(self):
        self.click_element(element_data=ElementsData.BugMultiplePanel.btn_sub)

    def click_btn_max(self):
        self.click_element(element_data=ElementsData.BugMultiplePanel.btn_max)

    def click_btn_min(self):
        self.click_element(element_data=ElementsData.BugMultiplePanel.btn_min)

    def get_drink_icon(self):
        return self.get_icon(element_data=ElementsData.BugMultiplePanel.icon)

    def get_drink_quantity(self):
        drink_quantity = self.get_text(element_data=ElementsData.BugMultiplePanel.quantity)
        return int(drink_quantity)

    def get_drink_value(self):
        drink_value = self.get_text(element_data=ElementsData.BugMultiplePanel.value).split('/')
        drink_cur = drink_value[0]
        drink_max = drink_value[1]
        return int(drink_cur), int(drink_max)

    def click_drink_icon(self):
        return self.click_element(element_data=ElementsData.BugMultiplePanel.icon)

    def get_slider(self):
        return Slider(self, element_slider=ElementsData.BugMultiplePanel.slider)

    def swipe_slider(self, value_start=None, value_end=None):
        if not value_start:
            value_start = random.random()
        if not value_end:
            value_end = random.random()
        slider = BugMultiplePanel.get_slider(self)
        point_start, point_end = slider.get_slide_point_start_and_end(slide_range=[value_start, value_end])
        if value_start > value_end:
            t = value_start - value_end
        else:
            t = value_end - value_start
        self.swipe(point_start=point_start, point_end=point_end, t=t)


    operation_pool = [
        {"element_data": ElementsData.BugMultiplePanel.btn_cancel, "func": click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.BugMultiplePanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.BugMultiplePanel.btn_add, "func": click_btn_add, "weight": 1},
        {"element_data": ElementsData.BugMultiplePanel.btn_sub, "func": click_btn_sub, "weight": 1},
        {"element_data": ElementsData.BugMultiplePanel.btn_max, "func": click_btn_max, "weight": 1},
        {"element_data": ElementsData.BugMultiplePanel.btn_min, "func": click_btn_min, "weight": 1},
        ]

if __name__ == '__main__':
    bp = BasePage()
    BugMultiplePanel.swipe_slider(bp)
    bp.connect_close()






