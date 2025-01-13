from common.basePage import BasePage
from configs.elementsData import ElementsData


class RankFishCardDetailPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RankFishCardDetailPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RankFishCardDetailPanel.RankFishCardDetailPanel)

    def click_card(self):
        self.click_element(element_data=ElementsData.RankFishCardDetailPanel.card)


    operation_pool = [
        {"element_data": ElementsData.RankFishCardDetailPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.RankFishCardDetailPanel.card, "func": click_card, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    RankFishCardDetailPanel.click_btn_close(bp)
    # RankFishCardDetailPanel.click_card(bp)
    bp.connect_close()