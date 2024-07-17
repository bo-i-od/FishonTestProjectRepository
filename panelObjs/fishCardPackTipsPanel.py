from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource


class FishCardPackTipsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardPackTips.FishCardPackTipsPanel)

    def get_item_icon(self):
        item_icon = self.get_icon(element_data=ElementsData.FishCardPackTips.item_icon)
        item_icon = resource.check_icon(item_icon)
        return item_icon

    def get_fish_card_name(self):
        fish_card_name = self.get_text(element_data=ElementsData.FishCardPackTips.fish_card_name)
        return fish_card_name
