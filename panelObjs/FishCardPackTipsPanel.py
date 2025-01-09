from common.basePage import BasePage
from configs.elementsData import ElementsData
from common import resource


class FishCardPackTipsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardPackTipsPanel.FishCardPackTipsPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardPackTipsPanel.btn_close)

    def get_item_icon(self):
        item_icon = self.get_icon(element_data=ElementsData.FishCardPackTipsPanel.item_icon)
        item_icon = resource.check_icon(item_icon)
        return item_icon

    def get_fish_card_name(self):
        fish_card_name = self.get_text(element_data=ElementsData.FishCardPackTipsPanel.fish_card_name)
        return fish_card_name

    operation_pool = [
        {"element_data": ElementsData.FishCardPackTipsPanel.btn_close, "func": click_btn_close, "weight": 10},

    ]


if __name__ == "__main__":
    bp = BasePage()
    FishCardPackTipsPanel.click_btn_close(bp)
    bp.connect_close()