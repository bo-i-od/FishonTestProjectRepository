from common.basePage import BasePage
from configs.elementsData import ElementsData


class ItemTipsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ItemTips.ItemTipsPanel)

    def get_item_icon(self):
        return self.get_icon(element_data=ElementsData.ItemTips.icon)

    def get_item_title(self):
        return self.get_text(element_data=ElementsData.ItemTips.title)

    def get_item_quantitiy(self):
        return int(self.get_text(element_data=ElementsData.ItemTips.quantity))
