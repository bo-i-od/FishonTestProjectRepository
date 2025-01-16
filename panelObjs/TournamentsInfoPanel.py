from common.basePage import BasePage
from configs.elementsData import ElementsData

class TournamentsInfoPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.TournamentsInfoPanel.TournamentsInfoPanel)

    def wait_for_panel_appear(self):
        while not TournamentsInfoPanel.is_panel_active(self):
            self.sleep(1)

    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.TournamentsInfoPanel.btn_close)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.TournamentsInfoPanel.tab_list, index=index)

    def is_checked(self):
        return self.exist(element_data=ElementsData.TournamentsInfoPanel.check)

    def get_progress(self):
        progress_cur_text, progress_max_text = self.get_text_list(element_data_list=[ElementsData.TournamentsInfoPanel.progress_cur, ElementsData.TournamentsInfoPanel.progress_max])
        progress_cur = int(progress_cur_text[0])
        progress_max = int(progress_max_text[0])
        return progress_cur, progress_max

    class panel_ranking(BasePage):
        def click_btn_playercard(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.TournamentsInfoPanel.panel_ranking.btn_playercard_list,
                                                element_viewport=ElementsData.TournamentsInfoPanel.panel_ranking.viewport,
                                                viewport_edge=[-0.05, 0],
                                                viewport_direction="column", index=index)

        def click_btn_playercard_myself(self):
            self.click_element(element_data=ElementsData.TournamentsInfoPanel.panel_ranking.btn_playercard_myself)

    class panel_rewards(BasePage):
        def click_btn_playercard(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.TournamentsInfoPanel.panel_rewards.btn_playercard_list,
                                                viewport_edge=[-0.05, 0],
                                                element_viewport=ElementsData.TournamentsInfoPanel.panel_rewards.viewport,
                                                viewport_direction="column", index=index)

        def click_btn_playercard_myself(self):
            self.click_element(element_data=ElementsData.TournamentsInfoPanel.panel_rewards.btn_playercard_myself)

        def click_item(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.TournamentsInfoPanel.panel_rewards.item_list,
                                                viewport_edge=[-0.05, 0],
                                                element_viewport=ElementsData.TournamentsInfoPanel.panel_rewards.viewport,
                                                viewport_direction="column", index=index)

        def click_item_myself(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.TournamentsInfoPanel.panel_rewards.item_list_myself, index=index)

    class panel_rules(BasePage):
        def click_item_main(self):
            self.click_element(element_data=ElementsData.TournamentsInfoPanel.panel_rules.item_main)

        def click_item(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.TournamentsInfoPanel.panel_rules.item_list, element_viewport=ElementsData.TournamentsInfoPanel.panel_rules.viewport, viewport_direction="row", index=index)

        def click_btn_claim(self):
            self.click_element(element_data=ElementsData.TournamentsInfoPanel.panel_rules.btn_claim)

        def click_btn_i(self):
            self.click_element(element_data=ElementsData.TournamentsInfoPanel.panel_rules.btn_i)

        def click_btn_close_tips(self):
            self.click_element(element_data=ElementsData.TournamentsInfoPanel.panel_rules.btn_close_tips)


    operation_pool = [
        {"element_data": ElementsData.TournamentsInfoPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.tab_list, "func": switch_tab, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_ranking.btn_playercard_list, "func": panel_ranking.click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_ranking.btn_playercard_myself, "func": panel_ranking.click_btn_playercard_myself, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rewards.btn_playercard_list, "func": panel_rewards.click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rewards.btn_playercard_myself, "func": panel_rewards.click_btn_playercard_myself, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rewards.item_list, "func": panel_rewards.click_item, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rewards.item_list_myself, "func": panel_rewards.click_item_myself, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rules.btn_claim, "func": panel_rules.click_btn_claim, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rules.btn_close_tips, "func": panel_rules.click_btn_close_tips, "weight": 10},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rules.btn_i, "func": panel_rules.click_btn_i, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rules.item_list, "func": panel_rules.click_item, "weight": 1},
        {"element_data": ElementsData.TournamentsInfoPanel.panel_rules.item_main, "func": panel_rules.click_item_main, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # TournamentsInfoPanel.click_btn_close(bp)
    # TournamentsInfoPanel.switch_tab(bp)
    # TournamentsInfoPanel.panel_ranking.click_btn_playercard(bp, 0)
    # TournamentsInfoPanel.panel_ranking.click_btn_playercard_myself(bp)
    # TournamentsInfoPanel.panel_rewards.click_btn_playercard(bp, 29)
    # TournamentsInfoPanel.panel_rewards.click_btn_playercard_myself(bp)
    # TournamentsInfoPanel.panel_rewards.click_item(bp, 0)
    # TournamentsInfoPanel.panel_rewards.click_item_myself(bp)
    TournamentsInfoPanel.panel_rules.click_btn_claim(bp)
    # TournamentsInfoPanel.panel_rules.click_btn_close_tips(bp)
    # TournamentsInfoPanel.panel_rules.click_btn_i(bp)
    # TournamentsInfoPanel.panel_rules.click_item(bp, 0)
    # TournamentsInfoPanel.panel_rules.click_item_main(bp)
    bp.connect_close()