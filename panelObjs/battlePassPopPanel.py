from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from tools.viewport import Viewport
from items.resource import *
class BattlePassPopPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassPop.btn_close)
        if BattlePassPopPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BattlePassPop.BattlePassPopPanel):
            return True
        return False

    def click_get_premium(self):
        self.click_element(element_data=ElementsData.BattlePassPop.btn_confirm)


    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassPop.Viewport, element_item_list=ElementsData.BattlePassPop.icon_list)
        icon_list, position_list = viewport.get_clickable_icon_and_position_list()
        check_icon_list(icon_list)
        return icon_list, position_list



if __name__ == '__main__':
    bp = BasePage()
    BattlePassPopPanel.get_clickable_icon_and_position_list(bp)



