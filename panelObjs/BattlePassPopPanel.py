from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport
from common.resource import *
class BattlePassPopPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BattlePassPopPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BattlePassPopPanel.BattlePassPopPanel)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.BattlePassPopPanel.btn_confirm)


    def get_clickable_icon_and_position_list(self):
        viewport = Viewport(self, element_viewport=ElementsData.BattlePassPopPanel.Viewport, element_item_list=ElementsData.BattlePassPopPanel.icon_list)
        icon_list, position_list = viewport.get_clickable_icon_and_position_list()
        # check_icon_list(icon_list)
        return icon_list, position_list

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BattlePassPopPanel.icon_list, element_viewport=ElementsData.BattlePassPopPanel.Viewport, viewport_direction="row")



    operation_pool = [
        {"element_data": ElementsData.BattlePassPopPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.BattlePassPopPanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.BattlePassPopPanel.icon_list, "func": click_item, "weight": 1},
        ]

if __name__ == '__main__':
    bp = BasePage()



