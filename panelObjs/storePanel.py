from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common import resource
from common.viewport import Viewport


class StorePanel(BasePage):
    @staticmethod
    def get_StorePanel_element_data():
        return ElementsData.Store.StorePanel

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Store.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Store.StorePanel)

    def click_btn_refresh(self):
        position_list = self.get_position_list(element_data=ElementsData.Store.Box.btn_refresh_text)
        if position_list:
            position = position_list[0]
            self.click_position(position)
            return
        position = self.get_position(element_data=ElementsData.Store.Box.btn_refresh_value)
        self.click_position(position)


    def change_tab(self, index):
        edge = [0.01, 0.01]
        viewport_tab = Viewport(self, element_viewport=ElementsData.Store.viewport_tab, element_item_list=ElementsData.Store.tab_list, viewport_edge=edge)
        viewport_tab.move_until_appear(viewport_tab.item_id_list[index])
        self.sleep(0.5)
        position_list = self.get_position_list(element_data=ElementsData.Store.tab_list)
        self.click_position(position_list[index])

    # 看还有几次刷新次数
    def get_times_refresh(self):
        times_refresh_str = self.get_text(element_data=ElementsData.Store.Box.times_refresh)
        times_refresh_split_str = times_refresh_str.split("/")
        # 分子
        times_refresh_numerator = int(times_refresh_split_str[0])
        # 分母
        times_refresh_denominator = int(times_refresh_split_str[1])
        return times_refresh_numerator, times_refresh_denominator

    def click_btn_add_100100(self):
        self.click_element(element_data=ElementsData.Store.btn_add_100100)


    # 获得图标、数量和折扣列表
    def get_box_details(self):
        icon_list = self.get_icon_list(element_data=ElementsData.Store.Box.box_list)
        quantity_list = self.get_text_list(element_data=ElementsData.Store.Box.quantity_list)
        item_id_list = self.get_object_id_list(element_data=ElementsData.Store.Box.item_list)
        off_list = []
        cur = 0
        while cur < len(item_id_list):
            # off_list[cur] = int(off_list[cur].split('%')[0]) / float(100)
            off = self.get_text_list(object_id=item_id_list[cur], offspring_path="value_bg>number")
            if off:
                off_list.append(1 - (int(off[0]) / float(10)))
                cur += 1
                continue
            off_list.append(0)
            cur += 1
        off_list[0] = 1
        str_to_int_list(quantity_list)
        return icon_list, quantity_list, off_list

    # 获得折扣和价格的列表 没有就补零填充
    def get_price_list(self, item_id_list=None):
        price_list = []
        for item_id in item_id_list:
            btn_disabled_id = self.get_offspring_id_list("btn_disabled", object_id=item_id)
            if btn_disabled_id:
                # -1 代表已经购买
                price_list.append("-1")
                continue
            text_sellout_id = self.get_offspring_id_list("sellout>text", object_id=item_id)
            if text_sellout_id:
                # -1 代表已经购买
                price_list.append("-1")
                continue
            text_sellout_id = self.get_offspring_id_list("soldout>bg>text", object_id=item_id)
            if text_sellout_id:
                # -1 代表已经购买
                price_list.append("-1")
                continue
            text_sellout_id = self.get_offspring_id_list("sellout>bg>text", object_id=item_id)
            if text_sellout_id:
                # -1 代表已经购买
                price_list.append("-1")
                continue
            btn_buy_id = self.get_offspring_id("btn_buy>text", object_id=item_id)
            price = self.get_text(object_id=btn_buy_id)
            free_list = ["FREE", "免费"]
            if price in free_list:
                price = '0'

            price_list.append(price)
            # if btn_buy_id != 0:
            #     btn_buy_text_id = self.get_child_id("text",object_id=btn_buy_id)
            #     print(btn_buy_text_id)
            #     btn_buy_text = self.get_text(object_id=btn_buy_text_id)
            #     print(btn_buy_text)
            #     price_list.append(btn_buy_text)
            # else:
            #     price_list.append("-1")
        str_to_int_list(price_list)
        return price_list
        # price_list = self.get_text_list(element_data=ElementsData.TreasureChestMerchant.items_buy)
        #
        # if price_list[0] == 'free':
        #     price_list[0] = '0'
        # str_to_int_list(price_list)
        # return price_list

    def get_btn_icon_list(self, item_id_list):
        btn_icon_list = []
        for item_id in item_id_list:
            btn_disabled_id = self.get_offspring_id_list("btn_disabled>text", object_id=item_id)
            if btn_disabled_id:
                # -1 代表已经购买
                btn_icon_list.append("")
                continue
            text_sellout_id = self.get_offspring_id_list("sellout>text", object_id=item_id)
            if text_sellout_id:
                btn_icon_list.append("")
                continue
            text_sellout_id = self.get_offspring_id_list("soldout>bg>text", object_id=item_id)
            if text_sellout_id:
                btn_icon_list.append("")
                continue
            text_sellout_id = self.get_offspring_id_list("sellout>bg>text", object_id=item_id)
            if text_sellout_id:
                btn_icon_list.append("")
                continue
            btn_icon_id = self.get_offspring_id("btn_buy>icon", object_id=item_id)
            btn_icon_list.append(self.get_icon(object_id=btn_icon_id))
        return btn_icon_list
    # 没有状态变化的按钮就直接返回位置列表
    # 因为按钮状态有三个所以将按钮位置保存到列表
    # 点击按钮时直接点列表对应索引的位置
    def get_btn_position_list(self, item_id_list):
        btn_position_list = []
        for item_id in item_id_list:
            btn_disabled_id = self.get_offspring_id_list("btn_disabled>text", object_id=item_id)
            if btn_disabled_id:
                # -1 代表已经购买
                btn_position_list.append(self.get_position(object_id=btn_disabled_id[0]))
                continue
            text_sellout_id = self.get_offspring_id_list("sellout>text", object_id=item_id)
            if text_sellout_id:
                btn_position_list.append(self.get_position(object_id=text_sellout_id[0]))
                continue
            text_sellout_id = self.get_offspring_id_list("soldout>bg>text", object_id=item_id)
            if text_sellout_id:
                btn_position_list.append(self.get_position(object_id=text_sellout_id[0]))
                continue
            text_sellout_id = self.get_offspring_id_list("sellout>bg>text", object_id=item_id)
            if text_sellout_id:
                btn_position_list.append(self.get_position(object_id=text_sellout_id[0]))
                continue
            btn_buy_id = self.get_offspring_id_list("btn_buy>text", object_id=item_id)
            if btn_buy_id:
                btn_position_list.append(self.get_position(object_id=btn_buy_id[0]))
            btn_get_id = self.get_offspring_id_list("btn_get>text", object_id=item_id)
            if btn_get_id:
                btn_position_list.append(self.get_position(object_id=btn_get_id[0]))
        return btn_position_list


    def get_box_id_list(self):
        item_id_list = self.get_object_id_list(element_data=ElementsData.Store.Box.item_list)
        return item_id_list

    def get_item_id_list(self):
        item_id_list = self.get_object_id_list(element_data=ElementsData.Store.Resource.item_list)
        return item_id_list

    def get_cash_id_list(self):
        cash_id_list = self.get_object_id_list(element_data=ElementsData.Store.Cash.cash_list)
        return cash_id_list

    def get_gift_pack_id_list(self):
        gift_pack_id_list = self.get_object_id_list(element_data=ElementsData.Store.GiftPack.gift_pack_list)
        return gift_pack_id_list


    # 算出期望的价格列表
    def get_expect_price_list(self, icon_list, quantity_list, off_list):
        worksheet = self.excelTools.get_worksheet("ITEM_MAIN.xlsm", "模板数据")
        priceDiamond_list = self.excelTools.same_row_different_column_convert_list(worksheet, "iconName", "priceDiamond", icon_list)
        # print(priceDiamond_list)
        # str_to_int_list(priceDiamond_list)
        expect_price_list = []
        cur = 0
        while cur < len(icon_list):
            expect_price = int(priceDiamond_list[cur] * quantity_list[cur] * (1 - off_list[cur]))
            expect_price_list.append(expect_price)
            cur += 1
        return expect_price_list

    # 获取刷新按钮上的价格  FREE和SOLD OUT分别记为0和-1
    def get_refresh_cost(self):
        price_str_list = self.get_text_list(element_data=ElementsData.Store.Box.btn_refresh_text)
        if not price_str_list:
            price_str = self.get_text(element_data=ElementsData.Store.Box.btn_refresh_value)
        else:
            price_str = price_str_list[0]
        free_list = ["FREE", "免费"]
        if price_str in free_list:
            return 0
        sold_out_list = ["SOLD OUT", "售罄"]
        if price_str in sold_out_list:
            return -1
        return int(price_str)

    # 获得绿钞数量

    # 看该按钮是否可以点击
    def is_clickable(self, cost, icon):
        if cost < 0:
            self.debug_log("已经购买无法购买")
            return False
        item_tpid = self.get_tpid(item_icon_name=icon)
        element_data = None
        if item_tpid == "100000":
            element_data = ElementsData.Store.text_100000
        elif item_tpid == "100100":
            element_data = ElementsData.Store.text_100100

        count = resource.get_resource(self, item_tpid=item_tpid, element_data=element_data)
        if cost > count:
            self.debug_log("资源不足")
            return False
        return True


    def get_cash(self):
        cash = resource.get_resource(self, "100100", element_data=ElementsData.Store.text_100100)
        return cash

    # 宝箱商店的箱子转换为箱子的索引号
    # def TreasureChestMerchant_icon_to_TreasureChest_icon_index(self, TreasureChestMerchant_icon, box_icon_TreasureChest_list):
    #     cur = 0
    #     while cur < len(box_icon_TreasureChest_list):
    #         if box_icon_TreasureChest_list[cur] == TreasureChestMerchant_icon:
    #             break
    #         cur += 1
    #     return cur


    def get_gift_pack_dict_list(self):
        gift_pack_dict_list = []
        gift_pack_id_list = self.get_object_id_list(element_data=ElementsData.Store.GiftPack.gift_pack_list)
        for gift_pack_id in gift_pack_id_list:
            icon_id_list = self.get_offspring_id_list(offspring_path="group>item_list>>icon", object_id=gift_pack_id)
            quantity_id_list = self.get_offspring_id_list(offspring_path="group>item_list>>quantity>value", object_id=gift_pack_id)
            icon_list = self.get_icon_list(object_id_list=icon_id_list)
            resource.check_icon_list(icon_list)
            quantity_list = self.get_text_list(object_id_list=quantity_id_list)
            str_to_int_list(quantity_list)
            item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
            gift_pack_dict_list.append(item_dict)
        return gift_pack_dict_list

    def get_gift_pack_position_list(self):
        gift_pack_position_list = self.get_position_list(element_data=ElementsData.Store.GiftPack.icon_list)
        return gift_pack_position_list

    def get_gift_pack_icon_list(self):
        gift_pack_icon_list = self.get_icon_list(element_data=ElementsData.Store.GiftPack.icon_list)
        return gift_pack_icon_list

    def get_gear_position_list(self):
        gear_position_list = self.get_position_list(element_data=ElementsData.Store.Resource.gear_card_list)
        return gear_position_list

    def get_gear_name_list(self):
        gear_name_list = self.get_text_list(element_data=ElementsData.Store.Resource.gear_name_list)
        cur = 0
        while cur < len(gear_name_list):
            gear_name_list[cur] = gear_name_list[cur].split('>')[1].split('<')[0]
            cur += 1
        return gear_name_list

    def get_gear_icon_list(self):
        gear_card_id_list = self.get_object_id_list(element_data=ElementsData.Store.Resource.gear_card_list)
        gear_icon_id_list = []
        for gear_card_id in gear_card_id_list:
            icon_id_list = self.get_offspring_id_list(object_id=gear_card_id, offspring_path="rod_mask>icon")
            if icon_id_list:
                gear_icon_id_list.append(icon_id_list[0])
            icon_id_list = self.get_offspring_id_list(object_id=gear_card_id, offspring_path="bait_mask>icon")
            if icon_id_list:
                gear_icon_id_list.append(icon_id_list[0])
        gear_icon_list = self.get_icon_list(object_id_list=gear_icon_id_list)
        return gear_icon_list

    def click_btn_info(self):
        self.click_element(element_data=ElementsData.Store.Resource.btn_info)

    def get_fish_card_icon_list(self):
        fish_card_icon_list = self.get_icon_list(element_data=ElementsData.Store.Resource.fish_card_icon_list)
        return fish_card_icon_list

    def get_fish_card_name_list(self):
        fish_card_name_list = self.get_text_list(element_data=ElementsData.Store.Resource.fish_card_name_list)
        return fish_card_name_list

    def get_fish_card_main_name(self):
        fish_card_main_name = self.get_text(element_data=ElementsData.Store.Resource.fish_card_main_name)
        return fish_card_main_name

    def get_fish_card_position_list(self):
        fish_card_position_list = self.get_position_list(element_data=ElementsData.Store.Resource.fish_card_icon_list)
        return fish_card_position_list
    def get_fish_card_quantity_list(self):
        fish_card_quantity_list = self.get_text_list(element_data=ElementsData.Store.Resource.fish_card_quantity_list)
        return fish_card_quantity_list

    def get_booster_dict_list(self):
        booster_dict_list = []
        booster_id_list = self.get_object_id_list(element_data=ElementsData.Store.Resource.item_list)
        for booster_id in booster_id_list:
            icon_id_list = self.get_offspring_id_list(offspring_path="group>icon_list>>icon", object_id=booster_id)
            quantity_id_list = self.get_offspring_id_list(offspring_path="group>icon_list>>quantity>value", object_id=booster_id)
            icon_list = self.get_icon_list(object_id_list=icon_id_list)
            resource.check_icon_list(icon_list)
            quantity_list = self.get_text_list(object_id_list=quantity_id_list)
            str_to_int_list(quantity_list)
            item_dict = resource.make_item_dict(item_icon_list=icon_list, item_quantity_list=quantity_list)
            booster_dict_list.append(item_dict)
        return booster_dict_list

    def get_booster_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.Store.Resource.booster_icon_list)
        return icon_list

    def get_booster_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.Store.Resource.booster_icon_list)
        return position_list

    def get_materials_icon_list(self):
        materials_icon_list = self.get_icon_list(element_data=ElementsData.Store.Resource.materials_icon_list)
        return materials_icon_list

    def get_materials_position_list(self):
        materials_position_list = self.get_position_list(element_data=ElementsData.Store.Resource.materials_icon_list)
        return materials_position_list

    def click_btn_min(self):
        self.click_element(element_data=ElementsData.Store.Resource.btn_min)

    def click_btn_max(self):
        self.click_element(element_data=ElementsData.Store.Resource.btn_max)

    def click_btn_add(self):
        self.click_element(element_data=ElementsData.Store.Resource.btn_add)

    def click_btn_sub(self):
        self.click_element(element_data=ElementsData.Store.Resource.btn_sub)

    def click_btn_purchase(self):
        self.click_element(element_data=ElementsData.Store.Resource.btn_purchase)

    def get_slider_size(self):
        return self.get_size(element_data=ElementsData.Store.Resource.slider)

    def get_slider_position(self):
        return self.get_position(element_data=ElementsData.Store.Resource.slider)

    def get_item_icon(self):
        item_icon = self.get_icon(element_data=ElementsData.Store.Resource.item_icon)
        return item_icon

    def get_item_quantity(self):
        item_quantity = self.get_text(element_data=ElementsData.Store.Resource.item_quantity)
        item_quantity = str_to_int(item_quantity)
        return item_quantity

    def get_cost_icon(self):
        item_icon = self.get_icon(element_data=ElementsData.Store.Resource.cost_icon)
        return item_icon

    def get_cost_quantity(self):
        item_quantity = self.get_text(element_data=ElementsData.Store.Resource.cost_quantity)
        item_quantity = str_to_int(item_quantity)
        return item_quantity

    def get_cash_position_list(self):
        cash_position_list = self.get_position_list(element_data=ElementsData.Store.Cash.cash_icon_list)
        return cash_position_list

    def get_cash_icon_list(self):
        cash_icon_list = self.get_icon_list(element_data=ElementsData.Store.Cash.cash_icon_list)
        return cash_icon_list

    def get_cash_quantity_list(self):
        cash_quantity_list = self.get_text_list(element_data=ElementsData.Store.Cash.cash_quantity_list)
        str_to_int_list(cash_quantity_list)
        return cash_quantity_list

    def get_cash_first_time_list(self):
        cash_id_list = self.get_object_id_list(element_data=ElementsData.Store.Cash.cash_list)
        cash_first_time_list = []
        for cash_id in cash_id_list:
            first_bg = self.get_offspring_id_list(object_id=cash_id, offspring_path="first_bg")
            cash_first_time_list.append(first_bg)
        return cash_first_time_list

    def change_resource_tab(self, index):
        resource_tab_position_list = self.get_position_list(element_data=ElementsData.Store.Resource.resource_tab_list)
        self.click_position(resource_tab_position_list[index])

    def get_month_model_1_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.Store.MonthCard.month_model_1)

    def get_month_card_1_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.Store.MonthCard.month_card_1_icon_list)
        return icon_list

    def get_month_card_1_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.Store.MonthCard.month_card_1_icon_list)
        return position_list

    def get_month_card_1_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.Store.MonthCard.month_card_1_quantity_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_month_card_1_quantity_total(self):
        quantity = self.get_text(element_data=ElementsData.Store.MonthCard.month_card_1_quantity_total)
        quantity = str_to_int(quantity)
        return quantity

    def get_month_model_2_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.Store.MonthCard.month_model_2_list)

    def get_month_card_2_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.Store.MonthCard.month_card_2_icon_list)
        return icon_list

    def get_month_card_2_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.Store.MonthCard.month_card_2_icon_list)
        return position_list

    def get_month_card_2_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.Store.MonthCard.month_card_2_quantity_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_month_card_2_quantity_total_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.Store.MonthCard.month_card_2_quantity_total_list)
        str_to_int_list(quantity_list)
        return quantity_list

    def get_month_card_2_collected_list(self):
        item_model_id_list = self.get_object_id_list(element_data=ElementsData.Store.MonthCard.month_card_2_item_model_list)
        collected_list = []
        cur = 0
        while cur < len(item_model_id_list):
            collected = self.get_offspring_id_list(object_id=item_model_id_list[cur], offspring_path="collected")
            if not collected:
                cur += 1
                continue
            collected_list.append(cur)
            cur += 1
        return collected_list






if __name__ == '__main__':
    bp = BasePage()
    StorePanel.change_tab(bp, 0)
    # cur = 301
    # while cur <= 400:
    #     name = f"player0"
    #     login(bp, name, cur)
    #     fish(bp)
    #     logout(bp, cur)
    #     cur += 1
