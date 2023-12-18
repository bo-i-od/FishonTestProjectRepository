from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.basePage import BasePage
from common.error import *
class BattlePassRewardPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePassReward.BattlePassRewardPanel):
            return True
        return False

    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.BattlePassReward.btn_close)
        if BattlePassRewardPanel.is_panel_active(self):
            raise FindElementError

    def click_get_premium(self):
        self.click_element(element_data=ElementsData.BattlePassReward.btn_unLock)
        if not self.exist(element_data=ElementsData.BattlePassBuyLicense.BattlePassBuyLicensePanel):
            raise FindNoElementError

    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassReward.Viewport_free, element_item_list=ElementsData.BattlePassReward.reward_icon_free_list)
        icon_free_list, position_free_list = viewport.get_clickable_icon_and_position_list()
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassReward.Viewport_premium, element_item_list=ElementsData.BattlePassReward.reward_icon_premium_list)
        icon_premium_list, position_premium_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_free_list)
        # check_icon_list(icon_premium_list)
        return icon_free_list, position_free_list, icon_premium_list, position_premium_list


if __name__ == '__main__':
    bp = BasePage()
    a = BattlePassRewardPanel.get_clickable_icon_and_position_list(bp)
    print(a)
