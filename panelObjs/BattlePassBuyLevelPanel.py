import random
from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *
from common.viewport import Viewport
from common.slider import Slider


class BattlePassBuyLevelPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevelPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassBuyLevelPanel.BattlePassBuyLevelPanel)

    def click_btn_add(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevelPanel.btn_add)

    def click_btn_sub(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevelPanel.btn_sub)

    def get_buy_level_and_new_level(self):
        pattern = r'\d+<'
        text = self.get_text(element_data=ElementsData.BattlePassBuyLevelPanel.level_cal)
        matches = re.findall(pattern, text)
        buy_level = int(matches[0].replace("<", ""))
        new_level = int(matches[1].replace("<", ""))
        return buy_level, new_level

    def get_cost(self):
        btn_buy_text = self.get_text(element_data=ElementsData.BattlePassBuyLevelPanel.btn_buy)
        cost = int(btn_buy_text)
        return cost

    def get_cash(self):
        cash = get_resource(self, "100100", element_data=ElementsData.BattlePassBuyLevelPanel.text_100100)
        return cash

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevelPanel.btn_buy)

    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassBuyLevelPanel.Viewport,
                            element_item_list=ElementsData.BattlePassBuyLevelPanel.reward_icon_free_list)
        icon_free_list, position_free_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_free_list)
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassBuyLevelPanel.Viewport,
                            element_item_list=ElementsData.BattlePassBuyLevelPanel.reward_icon_premium_list)
        icon_premium_list, position_premium_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_premium_list)
        return icon_free_list, position_free_list,icon_premium_list, position_premium_list

    def get_gear_position(self):
        position_list = self.get_position_list(element_data=ElementsData.BattlePassBuyLevelPanel.reward_gear_list)
        if position_list:
            return position_list[0]
        return None

    def get_slider(self):
        return Slider(self, element_slider=ElementsData.BattlePassBuyLevelPanel.slider)

    def go_to_RechargeStorePanel(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevelPanel.btn_add_100100)

    def click_top_res_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BattlePassBuyLevelPanel.top_res_btns, index=index)

    def swipe_slider_base(self, value_start=None, value_end=None):
        if not value_start:
            value_start = random.random()
        if not value_end:
            value_end = random.random()
        slider = BattlePassBuyLevelPanel.get_slider(self)
        point_start, point_end = slider.get_slide_point_start_and_end(slide_range=[value_start, value_end])
        if value_start > value_end:
            t = value_start - value_end
        else:
            t = value_end - value_start
        self.swipe(point_start=point_start, point_end=point_end, t=t)

    operation_pool = [
        {"element_data": ElementsData.BattlePassBuyLevelPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.BattlePassBuyLevelPanel.btn_add, "func": click_btn_add, "weight": 1},
        {"element_data": ElementsData.BattlePassBuyLevelPanel.btn_sub, "func": click_btn_sub, "weight": 1},
        {"element_data": ElementsData.BattlePassBuyLevelPanel.btn_buy, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.BattlePassBuyLevelPanel.top_res_btns, "func": click_top_res_btn, "weight": 1},
        {"element_data": ElementsData.BattlePassBuyLevelPanel.slider, "func": swipe_slider_base, "weight": 1},
    ]

if __name__ == '__main__':
    bp = BasePage()
    BattlePassBuyLevelPanel.swipe_slider_base(bp)
    bp.connect_close()

