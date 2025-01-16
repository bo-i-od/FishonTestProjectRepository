from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.BattleFailedPanel import BattleFailedPanel
from panelObjs.FlashCardReceivePanel import FlashCardReceivePanel
from panelObjs.RewardsPanel import RewardsPanel


class ResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ResultPanel.ResultPanel)

    def get_exp(self):
        exp_str = self.get_text(element_data=ElementsData.ResultPanel.exp)
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
            position_list = self.get_position_list(element_data_list=[ElementsData.ResultPanel.btn_claim_pve, ElementsData.ResultPanel.btn_claim_token_fish, ElementsData.BattleFailedPanel.btn_again])
            if position_list[0]:
                return ElementsData.ResultPanel.btn_claim_pve
            if position_list[1]:
                return ElementsData.ResultPanel.btn_claim_token_fish
            if position_list[2]:
                return ElementsData.BattleFailedPanel.btn_again
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

            self.clear_popup()
            self.sleep(1)
            if self.is_ray_input:
                self.ray_input(kind="click", element_data=element_btn)
                continue
            self.click_element_safe(element_data=element_btn)



    def click_btn_claim_pve(self):
        self.click_until_disappear(element_data=ElementsData.ResultPanel.btn_claim_pve, ignore_set={"ResultPanel"})

    def click_btn_claim_pvp(self):
        self.click_until_disappear(element_data=ElementsData.ResultPanel.btn_claim_pvp, ignore_set={"ResultPanel"})

    def click_btn_claim_token_fish(self):
        self.click_until_disappear(element_data=ElementsData.ResultPanel.btn_claim_token_fish, ignore_set={"ResultPanel"})

    def click_btn_share(self):
        self.click_element(element_data=ElementsData.ResultPanel.btn_share)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.ResultPanel.btn_i)



    operation_pool = [
        {"element_data": ElementsData.ResultPanel.btn_claim_pve, "func": click_btn_claim_pve, "weight": 1},
        {"element_data": ElementsData.ResultPanel.btn_claim_pvp, "func": click_btn_claim_pvp, "weight": 1},
        {"element_data": ElementsData.ResultPanel.btn_claim_token_fish, "func": click_btn_claim_token_fish, "weight": 1},
        {"element_data": ElementsData.ResultPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.ResultPanel.btn_share, "func": click_btn_share, "weight": 1},

    ]
if __name__ == "__main__":
    bp = BasePage()
    # ResultPanel.click_btn_claim(bp)
    # ResultPanel.click_btn_claim_token_fish(bp)
    # ResultPanel.click_btn_i(bp)
    ResultPanel.click_btn_share(bp)
    bp.connect_close()