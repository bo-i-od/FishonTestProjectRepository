from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.battleFailedPanel import BattleFailedPanel
from panelObjs.flashCardReceivePanel import FlashCardReceivePanel
from panelObjs.rewardsPanel import RewardsPanel


class ResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Result.ResultPanel)

    def get_exp(self):
        exp_str = self.get_text(element_data=ElementsData.Result.exp)
        return exp_str

    def wait_for_result(self):
        while True:
            self.clear_popup()
            if RewardsPanel.is_panel_active(self):
                RewardsPanel.click_tap_to_claim(self)
            # if FlashCardReceivePanel.is_panel_active(self):
            #     self.sleep(6)
            #     img = self.get_full_screen_shot()
            #     self.save_img(img)
            #     self.clear_popup()
            #     self.cur += 1
            position_list = self.get_position_list(element_data_list=[ElementsData.Result.btn_claim, ElementsData.Result.btn_claim_token_fish, ElementsData.BattleFailed.btn_again])
            if position_list[0]:
                return ElementsData.Result.btn_claim
            if position_list[1]:
                return ElementsData.Result.btn_claim_token_fish
            if position_list[2]:
                return ElementsData.BattleFailed.btn_again
            self.sleep(1)

    def automatic_settlement(self, element_btn):
        # f_flag = True
        while True:
            if not self.exist(element_data=element_btn):
                break
            # if f_flag:
            #     img = self.get_full_screen_shot()
            #     self.save_img(img)
            #     f_flag = False

            self.clear_popup_once()
            self.sleep(1)
            self.click_element_safe(element_data=element_btn)



    def click_btn_claim(self):
        self.click_until_disappear(element_data=ElementsData.Result.btn_claim, ignore_set={"ResultPanel"})

    def click_btn_claim_token_fish(self):
        self.click_until_disappear(element_data=ElementsData.Result.btn_claim_token_fish, ignore_set={"ResultPanel"})


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



if __name__ == '__main__':
    bp = BasePage()
    ResultPanel.wait_for_result(bp)
    print(bp.cur)
    bp.connect_close()