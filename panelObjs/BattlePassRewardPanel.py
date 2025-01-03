from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.basePage import BasePage
from common.error import *
class BattlePassRewardPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassRewardPanel.BattlePassRewardPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassRewardPanel.btn_close)

    def click_btn_unlock(self):
        self.click_element(element_data=ElementsData.BattlePassRewardPanel.btn_unLock)

    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassRewardPanel.Viewport_free, element_item_list=ElementsData.BattlePassRewardPanel.reward_icon_free_list, viewport_direction="row")
        icon_free_list, position_free_list = viewport.get_clickable_icon_and_position_list()
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassRewardPanel.Viewport_premium, element_item_list=ElementsData.BattlePassRewardPanel.reward_icon_premium_list, viewport_direction="row")
        icon_premium_list, position_premium_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_free_list)
        # check_icon_list(icon_premium_list)
        return icon_free_list, position_free_list, icon_premium_list, position_premium_list

    def click_item_free(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BattlePassRewardPanel.item_list_free, element_viewport=ElementsData.BattlePassRewardPanel.Viewport_free, viewport_direction="row", index=index)

    def click_item_premium(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BattlePassRewardPanel.item_list_premium, element_viewport=ElementsData.BattlePassRewardPanel.Viewport_premium, viewport_direction="row", index=index)


    operation_pool = [
        {"element_data": ElementsData.BattlePassRewardPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.BattlePassRewardPanel.btn_unLock, "func": click_btn_unlock, "weight": 1},
        {"element_data": ElementsData.BattlePassRewardPanel.item_list_free, "func": click_item_free, "weight": 1},
        {"element_data": ElementsData.BattlePassRewardPanel.item_list_premium, "func": click_item_premium, "weight": 1},

        ]

if __name__ == '__main__':
    bp = BasePage()
    BattlePassRewardPanel.click_item_free(bp)
    bp.connect_close()