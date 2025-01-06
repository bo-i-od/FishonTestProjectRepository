from common.basePage import BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData

class FishCardMultipleLevelUpPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishCardMultipleLevelUpPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishCardMultipleLevelUpPanel.FishCardMultipleLevelUpPanel)

    def click_btn_draw(self):
        self.click_element(element_data=ElementsData.FishCardMultipleLevelUpPanel.btn_draw)

    def click_toggle_choice_all(self):
        self.click_element(element_data=ElementsData.FishCardMultipleLevelUpPanel.choice_all)

    def get_viewport(self):
        size_list = self.get_size_list(element_data=ElementsData.FishCardMultipleLevelUpPanel.choice_list)
        edge = [0.5 * size_list[0][0], 0.5 * size_list[0][0]]
        viewport = Viewport(self, element_item_list=ElementsData.FishCardMultipleLevelUpPanel.card_list, element_viewport=ElementsData.FishCardMultipleLevelUpPanel.viewport, viewport_direction="row", viewport_edge=edge)
        return viewport

    def click_toggle_choice(self, index=-1):
        viewport = FishCardMultipleLevelUpPanel.get_viewport(self)
        self.click_object_of_plural_objects(element_data=ElementsData.FishCardMultipleLevelUpPanel.choice_list, viewport=viewport, index=index)

    def click_card(self, index=-1):
        viewport = FishCardMultipleLevelUpPanel.get_viewport(self)
        self.click_object_of_plural_objects(element_data=ElementsData.FishCardMultipleLevelUpPanel.card_list, viewport=viewport, index=index)

    operation_pool = [
        {"element_data": ElementsData.FishCardMultipleLevelUpPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.FishCardMultipleLevelUpPanel.btn_draw, "func": click_btn_draw, "weight": 1},
        {"element_data": ElementsData.FishCardMultipleLevelUpPanel.card_list, "func": click_card, "weight": 1},
        {"element_data": ElementsData.FishCardMultipleLevelUpPanel.choice_list, "func": click_toggle_choice, "weight": 1},
        {"element_data": ElementsData.FishCardMultipleLevelUpPanel.choice_all, "func": click_toggle_choice_all, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # FishCardMultipleLevelUpPanel.click_btn_close(bp)
    # FishCardMultipleLevelUpPanel.click_btn_draw(bp)
    # FishCardMultipleLevelUpPanel.click_card(bp)
    FishCardMultipleLevelUpPanel.click_toggle_choice(bp, 0)
    # FishCardMultipleLevelUpPanel.click_toggle_choice_all(bp)
    bp.connect_close()