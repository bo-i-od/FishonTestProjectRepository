from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.resource import *
class BattlePassPopPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassPopPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassPopPanel.BattlePassPopPanel)

    def click_get_premium(self):
        self.click_element(element_data=ElementsData.BattlePassPopPanel.btn_confirm)


    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassPopPanel.Viewport, element_item_list=ElementsData.BattlePassPopPanel.icon_list)
        icon_list, position_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_list)
        return icon_list, position_list



if __name__ == '__main__':
    bp = BasePage()
    BattlePassPopPanel.get_clickable_icon_and_position_list(bp)



