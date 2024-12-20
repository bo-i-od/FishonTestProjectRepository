from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class RechargeEndlessPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.EventsGiftCenter.EventsGiftCenterPanel)

    def get_item_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.RechargeEndless.item_model_list)

    def get_item_info_list(self):
        item_id_list = RechargeEndlessPanel.get_item_id_list(self)
        icon_main_list = self.get_icon_list(object_id_list=item_id_list, offspring_path=">group>icon")
        quantity_main_list = self.get_text_list(object_id_list=item_id_list, offspring_path=">group>icon>quantity>value")
        icon_sub_list = self.get_icon_list(object_id_list=item_id_list, offspring_path=">group>item_list>item_model_mini(Clone)>icon")
        quantity_sub_list = self.get_text_list(object_id_list=item_id_list, offspring_path=">group>item_list>item_model_mini(Clone)>quantity>value")

        item_info_list = []

        cur = 0
        while cur < len(item_id_list):
            quantity_list = quantity_main_list[cur] + quantity_sub_list[cur]
            str_to_int_list(quantity_list)
            item_dict = make_item_dict(item_icon_list=icon_main_list[cur] + icon_sub_list[cur], item_quantity_list=quantity_list)
            item_info_list.append(item_dict)
            cur += 1
        return item_info_list

    def get_item_icon_position_list(self):
        item_id_list = RechargeEndlessPanel.get_item_id_list(self)
        icon_main_position_list = self.get_position_list(object_id_list=item_id_list, offspring_path=">group>icon")
        icon_sub_position_list = self.get_position_list(object_id_list=item_id_list, offspring_path=">group>item_list>item_model_mini(Clone)>icon")
        item_icon_position_list = []

        cur = 0
        while cur < len(item_id_list):
            item_icon_position_list.append(icon_main_position_list[cur] + icon_sub_position_list[cur])
            cur += 1
        return item_icon_position_list


    def get_item_cost_list(self):
        item_id_list = RechargeEndlessPanel.get_item_id_list(self)
        cost_list = []
        for item_id in item_id_list:
            value_list = self.get_text_list(object_id=item_id, offspring_path="item_buy>btn>value")
            if not value_list:
                cost_list.append(0)
                continue
            cost_list.append(str_to_int(value_list[0]))
        return cost_list

    def get_btn_buy_position_list(self):
        return self.get_position_list(element_data=ElementsData.RechargeEndless.btn_buy_list)

    def get_btn_status(self):
        btn_buy_position_list = RechargeEndlessPanel.get_btn_buy_position_list(self)
        unlocked_index = 0
        locked_list = []
        cur = 0
        while cur < len(btn_buy_position_list) - 1:
            locked_list.append(cur)
            if btn_buy_position_list[unlocked_index][0] > btn_buy_position_list[cur + 1][0]:
                unlocked_index = cur + 1
            cur += 1
        locked_list.append(cur)
        locked_list.remove(unlocked_index)

        return unlocked_index, locked_list




if __name__ == '__main__':
    bp = BasePage()
    a = RechargeEndlessPanel.get_item_info_list(bp)
    b = RechargeEndlessPanel.get_item_cost_list(bp)
    print(a)
    print(b)