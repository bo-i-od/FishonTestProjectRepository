from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *

class DivisionListPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DivisionListPanel.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DivisionListPanel.DivisionListPanel):
            return True
        return False

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.DivisionListPanel.item_list, element_viewport=ElementsData.DivisionListPanel.viewport, viewport_direction="row", index=index, viewport_edge=[0, 0.2])

    operation_pool = [
        {"element_data": ElementsData.DivisionListPanel.btn_close, "func": click_btn_close, "weight": 10},
        {"element_data": ElementsData.DivisionListPanel.item_list, "func": click_item, "weight": 10},
        ]


if __name__ == '__main__':
    bp = BasePage()
    DivisionListPanel.click_item(bp, 5)
    bp.connect_close()