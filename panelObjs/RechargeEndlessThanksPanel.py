from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *


class RechargeEndlessThanksPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RechargeEndlessThanksPanel.RechargeEndlessThanksPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RechargeEndlessThanksPanel.btn_close,
                           ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessThanksPanel"})

    def get_item_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.RechargeEndlessThanksPanel.item_model_list)

    def get_item_info_list(self):
        item_id_list = RechargeEndlessThanksPanel.get_item_id_list(self)
        icon_main_list = self.get_icon_list(object_id_list=item_id_list, offspring_path=">group>icon")
        quantity_main_list = self.get_text_list(object_id_list=item_id_list,
                                                offspring_path=">group>icon>quantity>value")
        icon_sub_list = self.get_icon_list(object_id_list=item_id_list, offspring_path=">group>item_list>>icon")
        quantity_sub_list = self.get_text_list(object_id_list=item_id_list,
                                               offspring_path=">group>item_list>>quantity>value")

        item_info_list = []

        cur = 0
        while cur < len(item_id_list):
            quantity_list = quantity_main_list[cur] + quantity_sub_list[cur]
            str_to_int_list(quantity_list)
            item_dict = make_item_dict(item_icon_list=icon_main_list[cur] + icon_sub_list[cur],
                                       item_quantity_list=quantity_list)
            item_info_list.append(item_dict)
            cur += 1
        return item_info_list

    def get_item_icon_position_list(self):
        item_id_list = RechargeEndlessThanksPanel.get_item_id_list(self)
        icon_main_position_list = self.get_position_list(object_id_list=item_id_list, offspring_path=">group>icon")
        icon_sub_position_list = self.get_position_list(object_id_list=item_id_list,
                                                        offspring_path=">group>item_list>>icon")
        item_icon_position_list = []

        cur = 0
        while cur < len(item_id_list):
            item_icon_position_list.append(icon_main_position_list[cur] + icon_sub_position_list[cur])
            cur += 1
        return item_icon_position_list

    def get_item_cost_list(self):
        item_id_list = RechargeEndlessThanksPanel.get_item_id_list(self)
        cost_list = []
        for item_id in item_id_list:
            value_list = self.get_text_list(object_id=item_id, offspring_path="item_buy>btn>value")
            if not value_list:
                cost_list.append(0)
                continue
            cost_list.append(str_to_int(value_list[0]))
        return cost_list

    def get_btn_buy_position_list(self):
        return self.get_position_list(element_data=ElementsData.RechargeEndlessThanksPanel.btn_buy_list)

    def get_btn_status(self):
        btn_buy_position_list = RechargeEndlessThanksPanel.get_btn_buy_position_list(self)
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

    def click_icon_main(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RechargeEndlessThanksPanel.icon_main_list,
                                            index=index,
                                            ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessThanksPanel"})

    def click_icon_sub(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RechargeEndlessThanksPanel.icon_sub_list,
                                            index=index,
                                            ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessThanksPanel"})

    def click_btn_buy(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RechargeEndlessThanksPanel.btn_buy_list,
                                            index=index,
                                            ignore_set={"CommonRewardsTipsPanel", "RechargeEndlessThanksPanel"})

    operation_pool = [
        {"element_data": ElementsData.RechargeEndlessThanksPanel.icon_main_list, "func": click_icon_main, "weight": 1},
        {"element_data": ElementsData.RechargeEndlessThanksPanel.icon_sub_list, "func": click_icon_sub, "weight": 1},
        {"element_data": ElementsData.RechargeEndlessThanksPanel.btn_buy_list, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.RechargeEndlessThanksPanel.btn_close, "func": click_btn_close, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    RechargeEndlessThanksPanel.click_icon_main(bp)
    RechargeEndlessThanksPanel.click_icon_sub(bp)
    bp.connect_close()