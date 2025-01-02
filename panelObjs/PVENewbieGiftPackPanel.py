from common.basePage import BasePage
from configs.elementsData import ElementsData


class PVENewbieGiftPackPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PVENewbieGiftPackPanel. PVENewbieGiftPackPanel)

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.PVENewbieGiftPackPanel.btn_buy)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PVENewbieGiftPackPanel.btn_close)

    def click_item_icon(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PVENewbieGiftPackPanel.item_icon_list, index=index)

    operation_pool = [
        {"element_data": ElementsData.PVENewbieGiftPackPanel.btn_buy, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.PVENewbieGiftPackPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PVENewbieGiftPackPanel.item_icon_list, "func": click_item_icon, "weight": 1},
        ]

if __name__ == '__main__':
    bp = BasePage()