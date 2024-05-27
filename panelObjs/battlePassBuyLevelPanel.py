from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.resource import *
from common.viewport import Viewport
from common.slider import Slider
class BattlePassBuyLevelPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevel.btn_close)

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePassBuyLevel.BattlePassBuyLevelPanel):
            return True
        return False

    def click_add_level(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevel.btn_add)

    def click_sub_level(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevel.btn_sub)

    def get_buy_level_and_new_level(self):
        pattern = r'\d+<'
        text = self.get_text(element_data=ElementsData.BattlePassBuyLevel.level_cal)
        matches = re.findall(pattern, text)
        buy_level = int(matches[0].replace("<", ""))
        new_level = int(matches[1].replace("<", ""))
        return buy_level, new_level


    def get_cost(self):
        btn_buy_text = self.get_text(element_data=ElementsData.BattlePassBuyLevel.btn_buy_text)
        cost = int(btn_buy_text)
        return cost

    def get_cash(self):
        cash = get_resource(self, "100100", element_data=ElementsData.BattlePassBuyLevel.text_100100)
        return cash
    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevel.btn_buy_text)

    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassBuyLevel.Viewport,
                            element_item_list=ElementsData.BattlePassBuyLevel.reward_icon_free_list)
        icon_free_list, position_free_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_free_list)
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassBuyLevel.Viewport,
                            element_item_list=ElementsData.BattlePassBuyLevel.reward_icon_premium_list)
        icon_premium_list, position_premium_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_premium_list)
        return icon_free_list, position_free_list,icon_premium_list, position_premium_list

    def get_gear_position(self):
        position_list = self.get_position_list(element_data=ElementsData.BattlePassBuyLevel.reward_gear_list)
        if position_list:
            return position_list[0]
        return None

    def get_slider(self):
        return Slider(self, element_slider=ElementsData.BattlePassBuyLevel.slider)

    def go_to_RechargeStorePanel(self):
        self.click_element(element_data=ElementsData.BattlePassBuyLevel.btn_add_100100)

if __name__ == "__main__":
    bp = BattlePassBuyLevelPanel()
