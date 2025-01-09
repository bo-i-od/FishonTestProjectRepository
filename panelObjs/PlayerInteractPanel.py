from common.basePage import BasePage
from configs.elementsData import ElementsData
class PlayerInteractPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerInteractPanel.PlayerInteractPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_close)

    def click_btn_aquarium(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_aquarium)

    def click_btn_changecamera(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_changecamera)

    def click_player_rod_btn_i(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.player_rod_btn_i)

    def click_tab1(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.panel_tab1)

    def click_tab2(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.panel_tab2)

    def click_tab3(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.panel_tab3)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInteractPanel.tab_list)


    def click_btn_close_tips_player_rod(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_close_tips_player_rod)

    def click_rating_btn_i(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.rating_btn_i)

    def click_btn_close_tips_rating(self):
        self.click_element(element_data=ElementsData.PlayerInteractPanel.btn_close_tips_rating)

    def click_rod(self, index=-1):
        size_list = self.get_size_list(element_data=ElementsData.PlayerInteractPanel.rod_list)

        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInteractPanel.rod_list, element_viewport=ElementsData.PlayerInteractPanel.viewport_rod, viewport_direction="row", viewport_edge=[0.01, -size_list[0][0]], index=index)

    def click_badge(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInteractPanel.badge_list, element_viewport=ElementsData.PlayerInteractPanel.viewport_badge, viewport_direction="row", viewport_edge=[0.01, 0.01], index=index)


    operation_pool = [
        {"element_data": ElementsData.PlayerInteractPanel.badge_list, "func": click_badge, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.btn_aquarium, "func": click_btn_aquarium, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.btn_changecamera, "func": click_btn_changecamera, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.btn_close_tips_player_rod, "func": click_btn_close_tips_player_rod, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.btn_close_tips_rating, "func": click_btn_close_tips_rating, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.player_rod_btn_i, "func": click_player_rod_btn_i, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.rating_btn_i, "func": click_rating_btn_i, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.rod_list, "func": click_rod, "weight": 1},
        {"element_data": ElementsData.PlayerInteractPanel.tab_list, "func": switch_tab, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # PlayerInteractPanel.click_badge(bp)
    # PlayerInteractPanel.click_btn_aquarium(bp)
    # PlayerInteractPanel.click_btn_changecamera(bp)
    #
    # PlayerInteractPanel.click_btn_close_tips_player_rod(bp)
    # PlayerInteractPanel.click_btn_close_tips_rating(bp)
    # PlayerInteractPanel.click_player_rod_btn_i(bp)
    # PlayerInteractPanel.click_rating_btn_i(bp)
    # PlayerInteractPanel.click_rod(bp, 11)
    # PlayerInteractPanel.switch_tab(bp)
    # PlayerInteractPanel.click_btn_close(bp)
    bp.connect_close()


