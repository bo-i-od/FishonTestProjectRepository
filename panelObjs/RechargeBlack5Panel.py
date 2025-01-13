from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class RechargeBlack5Panel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RechargeBlack5Panel.btn_close, ignore_set={"EventsGiftCenterPanel", "RechargeBlack5Panel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RechargeBlack5Panel.RechargeBlack5Panel)

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.RechargeBlack5Panel.btn_buy, ignore_set={"EventsGiftCenterPanel", "RechargeBlack5Panel"})

    def click_btn_collect(self):
        self.click_element(element_data=ElementsData.RechargeBlack5Panel.btn_collect, ignore_set={"EventsGiftCenterPanel", "RechargeBlack5Panel"})
    def is_btn_collect_clickable(self):
        if self.get_offspring_id_list("btn_disabled", element_data=ElementsData.RechargeBlack5Panel.btn_collect):
            return False
        return True

    def get_day_icon_list(self, day):
        element_data = ElementsData.RechargeBlack5Panel.day1_icon_list
        if day == 1:
            element_data = ElementsData.RechargeBlack5Panel.day1_icon_list
        elif day == 2:
            element_data = ElementsData.RechargeBlack5Panel.day2_icon_list
        elif day == 3:
            element_data = ElementsData.RechargeBlack5Panel.day3_icon_list
        icon_list = self.get_icon_list(element_data=element_data)
        return icon_list

    def get_day_quantity_list(self, day):
        element_data = ElementsData.RechargeBlack5Panel.day1_icon_list
        if day == 1:
            element_data = ElementsData.RechargeBlack5Panel.day1_quantity_list
        elif day == 2:
            element_data = ElementsData.RechargeBlack5Panel.day2_quantity_list
        elif day == 3:
            element_data = ElementsData.RechargeBlack5Panel.day3_quantity_list
        quantity_list = self.get_text_list(element_data=element_data)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.RechargeBlack5Panel.icon_list)
        return icon_list

    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.RechargeBlack5Panel.icon_list)
        return position_list

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RechargeBlack5Panel.item_list, index=index, ignore_set={"EventsGiftCenterPanel", "RechargeBlack5Panel"})


    operation_pool = [
        {"element_data": ElementsData.RechargeBlack5Panel.btn_buy, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.RechargeBlack5Panel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.RechargeBlack5Panel.btn_collect, "func": click_btn_collect, "weight": 1},
        {"element_data": ElementsData.RechargeBlack5Panel.item_list, "func": click_item, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # RechargeBlack5Panel.click_btn_buy(bp)
    # RechargeBlack5Panel.click_btn_close(bp)
    # RechargeBlack5Panel.click_btn_collect(bp)
    RechargeBlack5Panel.click_item(bp)
    bp.connect_close()