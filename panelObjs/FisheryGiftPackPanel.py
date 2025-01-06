from common.basePage import BasePage
from configs.elementsData import ElementsData

class FisheryGiftPackPanel(BasePage):
    # def click_btn_close(self):
    #     self.click_element(element_data=ElementsData.FisheryGiftPackPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FisheryGiftPackPanel.FisheryGiftPackPanel)

    def get_item_quantity_list(self):
        quantity_list = self.get_text_list(element_data=ElementsData.FisheryGiftPackPanel.quantity_list)
        return quantity_list

    def get_item_icon_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.FisheryGiftPackPanel.icon_list)
        return icon_list

    def get_item_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.FisheryGiftPackPanel.icon_list)
        return position_list

    def click_item(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.FisheryGiftPackPanel.icon_list, index=index, ignore_set={"FisheryGiftPackPanel"})

    def click_btn_buy(self):
        self.click_element(element_data=ElementsData.FisheryGiftPackPanel.btn_buy, ignore_set={"FisheryGiftPackPanel"})

    operation_pool = [
        {"element_data": ElementsData.FisheryGiftPackPanel.btn_buy, "func": click_btn_buy, "weight": 1},
        {"element_data": ElementsData.FisheryGiftPackPanel.icon_list, "func": click_item, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # FisheryGiftPackPanel.click_btn_close(bp)
    FisheryGiftPackPanel.click_item(bp)
    # FisheryGiftPackPanel.click_btn_buy(bp)
    bp.connect_close()