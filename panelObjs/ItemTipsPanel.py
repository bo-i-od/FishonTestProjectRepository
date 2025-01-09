from common.basePage import BasePage
from configs.elementsData import ElementsData


class ItemTipsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ItemTipsPanel.ItemTipsPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ItemTipsPanel.btn_close)

    def get_item_icon(self):
        return self.get_icon(element_data=ElementsData.ItemTipsPanel.icon)

    def get_item_title(self):
        return self.get_text(element_data=ElementsData.ItemTipsPanel.title)

    def get_item_quantitiy(self):
        return int(self.get_text(element_data=ElementsData.ItemTipsPanel.quantity))

    operation_pool = [
        {"element_data": ElementsData.ItemTipsPanel.btn_close, "func": click_btn_close, "weight": 10},

    ]
if __name__ == "__main__":
    bp = BasePage()
    ItemTipsPanel.click_btn_close(bp)
    bp.connect_close()