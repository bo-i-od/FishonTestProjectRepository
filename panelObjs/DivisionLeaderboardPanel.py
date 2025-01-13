from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *

class DivisionLeaderboardPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.btn_close)


    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DivisionLeaderboardPanel.DivisionLeaderboardPanel):
            return True
        return False

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.tab_list, index=index)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.btn_i)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.btn_close_tips)


    class panel_myleague(BasePage):
        def click_btn_alldivisions(self):
            self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.panel_myleague.btn_alldivisions)

        def click_crown(self):
            self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.panel_myleague.crown)

        def click_btn_playercard(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_myleague.btn_playercard_list, element_viewport=ElementsData.DivisionLeaderboardPanel.panel_myleague.viewport, viewport_direction="column", viewport_edge=[0, 0.05], index=index)

        def click_btn_playercard_self(self):
            self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.panel_myleague.btn_playercard_myself)

        def click_item(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_myleague.item_list, element_viewport=ElementsData.DivisionLeaderboardPanel.panel_myleague.viewport, viewport_direction="column", viewport_edge=[0, 0.05], index=index)

        def click_item_self(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_myleague.item_myself, index=index)

    class panel_arena(BasePage):
        def switch_tab(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_arena.tab_list, index=index)

        def click_btn_playercard(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_arena.btn_playercard_list, element_viewport=ElementsData.DivisionLeaderboardPanel.panel_arena.viewport, viewport_direction="column", viewport_edge=[0, 0.05],index=index)

        def click_btn_playercard_self(self):
            self.click_element(element_data=ElementsData.DivisionLeaderboardPanel.panel_arena.btn_playercard_myself)

        def click_item(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_arena.item_list, element_viewport=ElementsData.DivisionLeaderboardPanel.panel_arena.viewport, viewport_direction="column", viewport_edge=[0, 0.05], index=index)

        def click_item_self(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.DivisionLeaderboardPanel.panel_arena.item_myself, index=index)

    operation_pool = [
        {"element_data": ElementsData.DivisionLeaderboardPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.btn_close_tips, "func": click_btn_close_tips, "weight": 10},
        {"element_data": ElementsData.DivisionLeaderboardPanel.tab_list, "func": switch_tab, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_myleague.btn_alldivisions, "func": panel_myleague.click_btn_alldivisions, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_myleague.crown, "func": panel_myleague.click_crown, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_myleague.btn_playercard_list, "func": panel_myleague.click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_myleague.btn_playercard_myself, "func": panel_myleague.click_btn_playercard_self, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_myleague.item_list, "func": panel_myleague.click_item, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_myleague.item_myself, "func": panel_myleague.click_item_self, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_arena.tab_list, "func": panel_arena.switch_tab, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_arena.btn_playercard_list, "func": panel_arena.click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_arena.btn_playercard_myself, "func": panel_arena.click_btn_playercard_self, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_arena.item_list, "func": panel_arena.click_item, "weight": 1},
        {"element_data": ElementsData.DivisionLeaderboardPanel.panel_arena.item_myself, "func": panel_arena.click_item_self, "weight": 1},
        ]


if __name__ == '__main__':
    bp = BasePage()
    # DivisionLeaderboardPanel.click_btn_close(bp)
    # DivisionLeaderboardPanel.switch_tab(bp)
    # DivisionLeaderboardPanel.panel_arena.click_btn_playercard(bp)
    # DivisionLeaderboardPanel.panel_arena.click_btn_playercard_self(bp)
    # DivisionLeaderboardPanel.panel_arena.click_item(bp)
    # DivisionLeaderboardPanel.panel_arena.click_item_self(bp)
    # DivisionLeaderboardPanel.panel_arena.switch_tab(bp)
    # DivisionLeaderboardPanel.panel_myleague.click_btn_alldivisions(bp)
    # DivisionLeaderboardPanel.panel_myleague.click_btn_playercard(bp, 7)
    # DivisionLeaderboardPanel.panel_myleague.click_btn_playercard_self(bp)
    # DivisionLeaderboardPanel.panel_myleague.click_crown(bp)
    # DivisionLeaderboardPanel.panel_myleague.click_item(bp)
    # DivisionLeaderboardPanel.panel_myleague.click_item_self(bp)
    DivisionLeaderboardPanel.click_btn_i(bp)
    DivisionLeaderboardPanel.click_btn_close_tips(bp)


    bp.connect_close()