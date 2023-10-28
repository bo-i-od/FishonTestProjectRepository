from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from panelObjs.treasureChestPanel import TreasureChestPanel

class TreasureChestMerchantPanel(BasePage):
    def click_btn_refresh(self):
        if self.exist(element_data=ElementsData.TreasureChestMerchant.btn_refresh_text):
            position = self.get_position(element_data=ElementsData.TreasureChestMerchant.btn_refresh_text)
        else:
            position = self.get_position(element_data=ElementsData.TreasureChestMerchant.btn_refresh_value)

        times_refresh_numerator, times_refresh_denominator = TreasureChestMerchantPanel.get_times_refresh(self)
        times_refresh_expect = times_refresh_numerator
        cash = TreasureChestMerchantPanel.get_resource(self)
        refresh_cost = TreasureChestMerchantPanel.get_refresh_cost(self)
        cash_expect = cash - refresh_cost
        if refresh_cost < 0 or cash_expect < 0:
            price_list_expect = TreasureChestMerchantPanel.get_price_list(self)
            cash_expect = cash
            # 不管按钮是否可点击都点击
            self.click_position(position)
            cash = TreasureChestMerchantPanel.get_resource(self)
            price_list = TreasureChestMerchantPanel.get_price_list(self)
            times_refresh_numerator, times_refresh_denominator = TreasureChestMerchantPanel.get_times_refresh(self)
            print("无法刷新")
            compare(cash, cash_expect)
            compare(price_list, price_list_expect)
            compare(times_refresh_numerator, times_refresh_expect)
            return
        price_list_pre = TreasureChestMerchantPanel.get_price_list(self)
        self.click_position(position)
        price_list = TreasureChestMerchantPanel.get_price_list(self)
        cash = TreasureChestMerchantPanel.get_resource(self)
        times_refresh_expect -= 1
        times_refresh_numerator, times_refresh_denominator = TreasureChestMerchantPanel.get_times_refresh(self)
        compare(cash, cash_expect)
        compare(times_refresh_numerator, times_refresh_expect)
        if price_list_pre == price_list:
            print("未刷新成功")
            raise SameError


    # 看还有几次刷新次数
    def get_times_refresh(self):
        times_refresh_str = self.get_text(element_data=ElementsData.TreasureChestMerchant.times_refresh)
        times_refresh_split_str = times_refresh_str.split("/")
        # 分子
        times_refresh_numerator = int(times_refresh_split_str[0])
        # 分母
        times_refresh_denominator = int(times_refresh_split_str[1])
        return times_refresh_numerator, times_refresh_denominator

    def goto_RechargeStorePanel(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.TreasureChestMerchant.btn_add_100100, element_data_b=ElementsData.RechargeStore.RechargeStorePanel)
        return ElementsData.TreasureChestMerchant.TreasureChestMerchantPanel

    def close_TreasureChestMerchantPanel(self):
        self.click_until_disappear(element_data=ElementsData.TreasureChestMerchant.btn_close)

    # 获得图标、数量和折扣列表
    def get_box_icon_and_quantity_and_box_off_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.TreasureChestMerchant.box_list)
        quantity_list = self.get_text_list(element_data=ElementsData.TreasureChestMerchant.quantity_list)
        off_list = self.get_text_list(element_data=ElementsData.TreasureChestMerchant.off_list)
        cur = 0
        while cur < len(off_list):
            off_list[cur] = int(off_list[cur].split('%')[0]) / float(100)
            cur += 1
        cur = 0
        while cur < len(icon_list):
            off_list.append(float(0))
            cur += 1
        str_to_int_list(quantity_list)
        return icon_list, quantity_list, off_list

    # 获得折扣和价格的列表 没有就补零填充
    def get_price_list(self):
        item_id_list = self.get_object_id_list(element_data=ElementsData.TreasureChestMerchant.item_list)
        price_list = []
        for item_id in item_id_list:
            btn_disabled_id = self.get_child_id_list("btn_disabled", object_id=item_id)
            if btn_disabled_id:
                # -1代表已经购买
                price_list.append("-1")
                continue
            free_id = self.get_child_id_list("free", object_id=item_id)
            if free_id:
                price_list.append("0")
                continue
            pay_id = self.get_child_id("pay", object_id=item_id)
            btn_buy_id = self.get_child_id("btn_buy", object_id=pay_id)
            text_id = self.get_child_id("text", object_id=btn_buy_id)
            price_list.append(self.get_text(object_id=text_id))
            # if btn_buy_id != 0:
            #     btn_buy_text_id = self.get_child_id("text",object_id=btn_buy_id)
            #     print(btn_buy_text_id)
            #     btn_buy_text = self.get_text(object_id=btn_buy_text_id)
            #     print(btn_buy_text)
            #     price_list.append(btn_buy_text)
            # else:
            #     price_list.append("-1")
        str_to_int_list(price_list)
        print(f"价格列表为：{price_list}")
        return price_list
        # price_list = self.get_text_list(element_data=ElementsData.TreasureChestMerchant.items_buy)
        #
        # if price_list[0] == 'free':
        #     price_list[0] = '0'
        # str_to_int_list(price_list)
        # return price_list

    # 因为按钮状态有三个所以将按钮位置保存到列表
    # 点击按钮时直接点列表对应索引的位置
    def get_btn_position_list(self):
        item_id_list = self.get_object_id_list(element_data=ElementsData.TreasureChestMerchant.item_list)
        btn_position_list = []
        for item_id in item_id_list:
            btn_disabled_id = self.get_child_id_list("btn_disabled", object_id=item_id)
            if btn_disabled_id:
                # -1代表已经购买
                btn_position_list.append(self.get_position(object_id=btn_disabled_id[0]))
                continue
            free_id = self.get_child_id_list("free", object_id=item_id)
            if free_id:
                btn_buy_id = self.get_child_id("btn_buy", object_id=free_id[0])
                btn_position_list.append(self.get_position(object_id=btn_buy_id))
                continue
            pay_id = self.get_child_id("pay", object_id=item_id)
            btn_buy_id = self.get_child_id("btn_buy", object_id=pay_id)
            btn_position_list.append(self.get_position(object_id=btn_buy_id))
            # if btn_buy_id != 0:
            #     btn_buy_text_id = self.get_child_id("text",object_id=btn_buy_id)
            #     print(btn_buy_text_id)
            #     btn_buy_text = self.get_text(object_id=btn_buy_text_id)
            #     print(btn_buy_text)
            #     price_list.append(btn_buy_text)
            # else:
            #     price_list.append("-1")
        print(btn_position_list)
        return btn_position_list

    # 算出期望的价格列表
    def get_expect_price_list(self, icon_list, quantity_list, off_list):
        worksheet = self.excelTools.get_worksheet("ITEM_MAIN.xlsm", "模板数据")
        priceDiamond_list = self.excelTools.same_row_different_column_convert_list(worksheet, "iconName", "priceDiamond", icon_list)
        str_to_int_list(priceDiamond_list)
        expect_price_list = []
        cur = 0
        while cur < len(icon_list):
            expect_price = int(priceDiamond_list[cur] * quantity_list[cur] * (1 - off_list[cur]))
            expect_price_list.append(expect_price)
            cur += 1
        return expect_price_list

    # 获取刷新按钮上的价格  FREE和SOLD OUT分别记为0和-1
    def get_refresh_cost(self):
        price_str_list = self.get_text_list(element_data=ElementsData.TreasureChestMerchant.btn_refresh_text)
        if not price_str_list:
            price_str = self.get_text(element_data=ElementsData.TreasureChestMerchant.btn_refresh_value)
        else:
            price_str = price_str_list[0]
        if price_str == 'FREE':
            return 0
        if price_str == 'SOLD OUT':
            return -1
        return int(price_str)

    # 获得绿钞数量
    def get_resource(self):
        cash_db = self.get_item_count(item_tpid="100100")
        print(cash_db)
        cash_show = self.get_text(element_data=ElementsData.TreasureChestMerchant.text_100100)
        print(cash_show)
        compare(cash_db, int(cash_show))
        print(f"显示绿钞与数据库绿钞一致，数量为{cash_db}")
        return cash_db

    # 看该按钮是否可以点击
    def is_clickable(self, price):
        if price < 0:
            print("已经购买无法购买")
            return False
        cash = TreasureChestMerchantPanel.get_resource(self)
        if price > cash:
            print("绿钞不足")
            return False
        print("绿钞充足")
        return True

    # 记录买之前的状态算出点击后的期望状态再进行点击
    # 点击完后对比期望状态和实际状态
    def click_btn_buy(self, index: int):
        btn_position_list = TreasureChestMerchantPanel.get_btn_position_list(self)
        price_list = TreasureChestMerchantPanel.get_price_list(self)
        cash_expect = TreasureChestMerchantPanel.get_resource(self)
        box_icon_TreasureChest_list, quantity_TreasureChest_list = TreasureChestPanel.get_box_icon_and_quantity_list(self)
        print("点击购买")
        quantity_TreasureChest_list_expect = quantity_TreasureChest_list
        if TreasureChestMerchantPanel.is_clickable(self,price_list[index]):
            print("可以点击")
            box_icon_TreasureChestMerchant_list, quantity_TreasureChestMerchant_list, box_off_list =TreasureChestMerchantPanel.get_box_icon_and_quantity_and_box_off_list(self)
            TreasureChest_icon_index = TreasureChestMerchantPanel.TreasureChestMerchant_icon_to_TreasureChest_icon_index(self,box_icon_TreasureChestMerchant_list[index],box_icon_TreasureChest_list)
            quantity_TreasureChest_list_expect[TreasureChest_icon_index] += quantity_TreasureChestMerchant_list[index]
            cash_expect -= price_list[index]
        self.click_position(btn_position_list[index])
        box_icon_TreasureChest_list, quantity_TreasureChest_list = TreasureChestPanel.get_box_icon_and_quantity_list(self)
        print("点击后的期望箱子数量列表为",quantity_TreasureChest_list_expect)
        print("点击后的实际箱子数量列表为", quantity_TreasureChest_list)
        compare(quantity_TreasureChest_list, quantity_TreasureChest_list_expect)
        cash = TreasureChestMerchantPanel.get_resource(self)
        print(f"点击后的期望绿钞数为{cash_expect}，实际绿钞数为{cash}")
        compare(cash, cash_expect)

    # 宝箱商店的箱子转换为箱子的索引号
    def TreasureChestMerchant_icon_to_TreasureChest_icon_index(self, TreasureChestMerchant_icon, box_icon_TreasureChest_list):
        cur = 0
        while cur < len(box_icon_TreasureChest_list):
            if box_icon_TreasureChest_list[cur] == TreasureChestMerchant_icon:
                break
            cur += 1
        return cur




if __name__ == '__main__':
    bp = TreasureChestMerchantPanel()
    # icon_list, quantity_list, off_list = bp.get_box_icon_and_quantity_and_box_off_list()
    bp.click_btn_buy(0)
    bp.click_btn_buy(5)
    bp.click_btn_buy(0)
    bp.click_btn_buy(3)
    bp.click_btn_refresh()
    bp.click_btn_buy(2)
    bp.click_btn_buy(0)
    bp.click_btn_buy(1)
    bp.click_btn_buy(0)
    # price = bp.get_refresh_price()
    # print(price)
    # # print()
    # print(bp.get_expect_price_list(icon_list, quantity_list, off_list))

