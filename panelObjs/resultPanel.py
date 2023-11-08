from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel

class ResultPanel(BasePage):

    def get_exp(self):
        exp_str = self.get_text(element_data=ElementsData.Result.pve_result.exp)
        exp_str = exp_str[1:]
        exp = int(exp_str)
        return exp

    def wait_for_result(self):
        while (self.exist(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again) or self.exist(element_data=ElementsData.Result.pve_result.btn_claim) or self.exist(element_data=ElementsData.Result.pve_result.btn_throw)) is False:
            self.sleep(1)

    def automatic_settlement(self, is_return=True):
        if is_return is False:
            if self.exist(element_data=ElementsData.Result.pve_result.btn_claim):
                self.click_element(element_data=ElementsData.Result.pve_result.btn_claim)
                return 1
            ResultPanel.duel_sundries(self, is_return=False)
            self.sleep(1)
            self.try_click_element(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again)
            return 0
        if self.exist(element_data=ElementsData.Result.pve_result.btn_claim):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_claim)
            return "", {}
        chest_icon, item_dict = ResultPanel.duel_sundries(self)
        self.sleep(1)
        self.try_click_element(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again)
        return chest_icon, item_dict




    def duel_sundries(self, is_return=True):
        if is_return is False:
            if self.exist(element_data=ElementsData.Result.pve_result.btn_open_by_key):
                self.click_element(element_data=ElementsData.Result.pve_result.btn_open_by_key)
            elif self.exist(element_data=ElementsData.Result.pve_result.btn_open_by_cash):
                self.click_element(element_data=ElementsData.Result.pve_result.btn_open_by_cash)
            elif self.exist(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again):
                self.click_element(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again)
            else:
                self.click_element(element_data=ElementsData.Result.pve_result.btn_throw)
            RewardsPanel.wait_for_RewardsPanel(self)
            self.sleep(0.5)
            RewardsPanel.click_tap_to_continue(self)
            return
        chest_icon = ResultPanel.get_chest_icon(self)
        if self.exist(element_data=ElementsData.Result.pve_result.btn_open_by_key):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_open_by_key)
        elif self.exist(element_data=ElementsData.Result.pve_result.btn_open_by_cash):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_open_by_cash)
        elif self.exist(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again)
        else:
            self.click_element(element_data=ElementsData.Result.pve_result.btn_throw)
            return "", {}
        RewardsPanel.wait_for_RewardsPanel(self)
        self.sleep(0.5)
        item_dict = {}
        if chest_icon != "":
            item_dict = RewardsPanel.get_reward_dict(self)
        RewardsPanel.click_tap_to_continue(self)
        return chest_icon, item_dict

    def get_chest_icon(self):
        icon = self.get_icon(element_data=ElementsData.Result.pve_result.icon_sundries)
        if icon != "ChestNormal" and icon != "ChestGold" and icon != "ChestSilver":
            return ""
        print("钓到了箱子")
        return icon


    def goto_HomePanel(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.Result.pve_result.btn_gohome, element_data_b=ElementsData.Home.HomePanel)
