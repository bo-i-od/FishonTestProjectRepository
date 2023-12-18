from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *
class RechargeEndlessPanel(BasePage):
    def close_RechargeEndlessPanel(self):
        self.click_element(element_data=ElementsData.RechargeEndless.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.RechargeEndless.RechargeEndlessPanel):
            return True
        return False

    # 点击并返回价格文本
    def click_btn_buy(self, index):
        btn_buy_position_list = self.get_position_list(element_data=ElementsData.RechargeEndless.btn_buy_list)
        btn_buy_text_list = self.get_text_list(element_data=ElementsData.RechargeEndless.btn_buy_list)
        self.click_position(btn_buy_position_list[index])
        return btn_buy_text_list[index]

    def get_item_icon_and_quantity_list(self):
        item_icon_list = self.get_icon_list(element_data=ElementsData.RechargeEndless.icon_list)
        # check_icon_list(item_icon_list)
        item_quantity_list = self.get_text_list(element_data=ElementsData.RechargeEndless.quantity_list)
        str_to_int_list(item_quantity_list)
        return item_icon_list, item_quantity_list

    def get_select_icon_and_quantity_list(self, index):
        group_id_list = self.get_object_id_list(element_data=ElementsData.RechargeEndless.group_list)
        group_id = group_id_list[index]
        icon_id_list = self.get_offspring_id_list("item_list>>icon", object_id=group_id)
        quantity_id_list = self.get_offspring_id_list("item_list>>quantity>value", object_id=group_id)
        select_icon_list = self.get_icon_list(object_id_list=icon_id_list)
        select_quantity_list = self.get_text_list(object_id_list=quantity_id_list)
        str_to_int_list(select_quantity_list)
        item_icon_and_quantity_list = RechargeEndlessPanel.get_item_icon_and_quantity_list(self)
        select_icon_list.append(item_icon_and_quantity_list[0][index])
        select_quantity_list.append(item_icon_and_quantity_list[1][index])
        return select_icon_list, select_quantity_list

    def get_clickable_icon_and_position_list(self, index):
        group_id_list = self.get_object_id_list(element_data=ElementsData.RechargeEndless.group_list)
        clickable_icon_list = []
        clickable_position_list = []
        index_max = index + 4
        cur = index
        while cur < index_max:
            group_id = group_id_list[cur]
            icon_id_list = self.get_offspring_id_list("item_list>>icon", object_id=group_id)
            icon_list = self.get_icon_list(object_id_list=icon_id_list)
            position_list = self.get_position_list(object_id_list=icon_id_list)
            clickable_icon_list += icon_list
            clickable_position_list += position_list
            cur += 1
        return clickable_icon_list, clickable_position_list



if __name__ == '__main__':
    bp = RechargeEndlessPanel()
    a = bp.get_select_icon_and_quantity_list(1)
    print(a)