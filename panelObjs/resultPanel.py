from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.rewardsPanel import RewardsPanel

class ResultPanel(BasePage):

    def get_exp(self):
        exp_str = self.get_text(element_data=ElementsData.Result.exp)
        return exp_str

    def wait_for_result(self):
        btn_claim = self.exist(element_data=ElementsData.Result.btn_claim)
        btn_claim_token_fish = self.exist(element_data=ElementsData.Result.btn_claim_token_fish)
        while not (btn_claim or btn_claim_token_fish):
            btn_claim = self.exist(element_data=ElementsData.Result.btn_claim)
            btn_claim_token_fish = self.exist(element_data=ElementsData.Result.btn_claim_token_fish)

    def automatic_settlement(self):
        if self.exist(element_data=ElementsData.Result.btn_claim):
            ResultPanel.click_btn_claim(self)
            return
        if self.exist(element_data=ElementsData.Result.btn_claim_token_fish):
            ResultPanel.click_btn_claim_token_fish(self)
            return



    def click_btn_claim(self):
        self.click_until_disappear(element_data=ElementsData.Result.btn_claim)

    def click_btn_claim_token_fish(self):
        self.click_until_disappear(element_data=ElementsData.Result.btn_claim_token_fish)


    def duel_sundries(self):
        if self.exist(element_data=ElementsData.Result.pve_result.btn_open_by_key):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_open_by_key)
        elif self.exist(element_data=ElementsData.Result.pve_result.btn_open_by_cash):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_open_by_cash)
        elif self.exist(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again):
            self.click_element(element_data=ElementsData.Result.pve_result.btn_open_and_cast_again)
        else:
            self.click_element(element_data=ElementsData.Result.pve_result.btn_throw)
        RewardsPanel.wait_for_panel_appear(self)
        self.sleep(0.5)
        RewardsPanel.click_tap_to_claim(self)
        return



    def goto_HomePanel(self):
        self.click_a_until_b_appear(element_data_a=ElementsData.Result.pve_result.btn_gohome, element_data_b=ElementsData.Home.HomePanel)

if __name__ == '__main__':
    bp = BasePage()
    ResultPanel.click_btn_claim(bp)