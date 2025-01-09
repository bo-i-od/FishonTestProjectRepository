from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource
from tools.commonTools import *


class PartySalePanel(BasePage):
    # 面板是否存在
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PartySalePanel.PartySalePanel)

    # 点击关闭按钮
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PartySalePanel.btn_close, ignore_set={"PartySalePanel"})

    # 点击购买
    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.PartySalePanel.btn_buy, ignore_set={"PartySalePanel"})

    def get_cost_icon(self):
        return self.get_icon(element_data=ElementsData.PartySalePanel.cost_icon)

    def get_cost_quantity(self):
        cost_quantity = self.get_text(element_data=ElementsData.PartySalePanel.cost_quantity)
        cost_quantity = str_to_int(cost_quantity)
        return cost_quantity

    # 获取图标
    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.PartySalePanel.item_icon_list)
        return icon_list

    # 获取图标位置
    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PartySalePanel.item_icon_list)
        return position_list

    # 获取图标
    def get_item_quantity_list(self):
        quantity_list =self.get_text_list(element_data=ElementsData.PartySalePanel.item_quantity_list)
        resource.str_to_int_list(quantity_list)
        return quantity_list

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PartySalePanel.item_icon_list, index=index, ignore_set={"PartySalePanel"})


    operation_pool = [
        {"element_data": ElementsData.PartySalePanel.btn_buy, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.PartySalePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PartySalePanel.item_icon_list, "func": click_item, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # PartySalePanel.click_btn_buy(bp)
    # PartySalePanel.click_btn_close(bp)
    PartySalePanel.click_item(bp)
    # PartySalePanel.get_cost_icon(bp)
    # PartySalePanel.get_cost_quantity(bp)
    # PartySalePanel.get_item_icon_list(bp)
    # PartySalePanel.get_item_position_list(bp)
    # PartySalePanel.get_item_quantity_list(bp)
    # PartySalePanel.is_panel_active(bp)
    bp.connect_close()