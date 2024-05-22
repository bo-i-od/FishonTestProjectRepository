from common.basePage import BasePage
from common.resource import make_item_dict
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel
from common import resource
from tools.commonTools import *


class CareerPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Career.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Career.CareerPanel)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.Career.btn_i)

    def is_tips_active(self):
        return self.exist(element_data=ElementsData.Career.tips)

    def click_btn_enhance(self):
        self.click_element(element_data=ElementsData.Career.btn_enhance)

    def get_cost_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.Career.cost_icon_list)

    def get_cost_quantity_list(self):
        cost_quantity_list = self.get_text_list(element_data=ElementsData.Career.cost_quantity_list)
        str_to_int_list(cost_quantity_list)
        return cost_quantity_list

    def get_rating_total(self):
        rating_total = self.get_text(element_data=ElementsData.Career.rating_total)
        return int(rating_total)

    def get_rating(self):
        rating = self.get_text(element_data=ElementsData.Career.rating)
        return int(rating)

    def get_item_icon(self):
        return self.get_icon(element_data=ElementsData.Career.item_icon)

    def get_item_lv(self):
        if self.get_object_id_list(element_data=ElementsData.Career.item_lock):
            return 0
        return int(self.get_text(element_data=ElementsData.Career.item_lv))

    def get_unlock_condition(self):
        tips_lock = self.get_text(element_data=ElementsData.Career.tips_lock)
        lv = re.search(r'\d+', tips_lock).group()
        return int(lv)

    def click_btn_add_100000(self):
        self.click_element(element_data=ElementsData.Career.btn_add_100000)

    def get_group_id_list(self):
        group_id_list = self.get_object_id_list(element_data=ElementsData.Career.group_list)
        return group_id_list

    def get_cost_dict(self):
        cost_icon_list = self.get_icon_list(element_data=ElementsData.Career.cost_icon_list)
        cost_quantity_list = self.get_text_list(element_data=ElementsData.Career.cost_quantity_list)
        cost_dict = make_item_dict(item_icon_list=cost_icon_list, item_quantity_list=cost_quantity_list)
        return cost_dict


if __name__ == '__main__':
    bp = BasePage()
    a = CareerPanel.get_group_id_list(bp)
    print(a)

