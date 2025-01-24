import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class TournamentsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.TournamentsPanel.TournamentsPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.TournamentsPanel.btn_close)


    def get_fishery_tpid_list(self):
        table_data_detail = self.excelTools.get_table_data_detail(book_name="FISHERIES.xlsm")
        table_data_detail_activity = self.excelTools.get_table_data_detail(book_name="FISHERIES_ACTIVITY.xlsm")
        bg_list = self.get_icon_list(element_data=ElementsData.TournamentsPanel.bg_list)

        cur = 0
        while cur < len(bg_list):
            bg_list[cur] = "bg_fisheries_blur_" + bg_list[cur].split('_')[2]
            cur += 1

        res_list = []
        cur = 0
        while cur < len(bg_list):
            table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key="displayBlurBG", value=bg_list[cur], table_data_detail=table_data_detail) + self.excelTools.get_table_data_object_list_by_key_value(key="displayBlurBG", value=bg_list[cur], table_data_detail=table_data_detail_activity)

            if not table_data_object_list:
                res_list.append("")
                cur += 1
                continue
            table_data_object = table_data_object_list[0]
            tpId = table_data_object["tpId"]
            # index = displayicon_list.index(bg_list[cur])
            # tpId = tpId_list[index]
            res_list.append(str(tpId))
            cur += 1
            continue
        return res_list

    def get_entrance_viewport(self):
        size = self.get_size(element_data=ElementsData.TournamentsPanel.panel_sidebar_bg)
        edge_left = 0.75 * size[0]
        # 多人房进入按钮和单人房加一起
        model_id_list = self.get_object_id_list(element_data=ElementsData.TournamentsPanel.model_list)
        item_id_list = []
        for model_id in model_id_list:
            btn_enter_id_list = self.get_offspring_id_list(object_id=model_id, offspring_path="btn_enter>text")
            if btn_enter_id_list:
                item_id_list.append(btn_enter_id_list[0])
                continue
            btn_players_id_list = self.get_offspring_id_list(object_id=model_id, offspring_path="btn_players>btn_players>text")
            if btn_players_id_list:
                item_id_list.append(btn_players_id_list [0])
                continue
        entrance_viewport = Viewport(self, element_viewport=ElementsData.TournamentsPanel.entrance_viewport, item_id_list= item_id_list)
        entrance_viewport.viewport_range = [entrance_viewport.viewport_range[0], 1]
        entrance_viewport.viewport_edge = [edge_left, 0.05]
        entrance_viewport.viewport_range_shift()
        return entrance_viewport

    # 跳转指定tpid渔场
    def go_to_fishery_by_tpid(self, fishery_tpid):
        fishery_tpid_list = TournamentsPanel.get_fishery_tpid_list(self)
        index = fishery_tpid_list.index(str(fishery_tpid))
        TournamentsPanel.go_to_fishery_by_index(self, index)

    # 跳转指定索引渔场
    def go_to_fishery_by_index(self, index=-1):
        entrance_viewport = TournamentsPanel.get_entrance_viewport(self)

        if index < 0:
            index = random.randint(0, len(entrance_viewport.item_id_list) - 1)
        while self.exist(object_id=entrance_viewport.item_id_list[index]):
            entrance_viewport.move_until_appear(entrance_viewport.item_id_list[index])
            entrance_position = self.get_position(object_id=entrance_viewport.item_id_list[index])
            self.click_position(entrance_position)
            self.sleep(0.2)

    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.TournamentsPanel.btn_leaderboard)

    def get_tournaments_info_position_list(self):
        return self.get_position_list(element_data=ElementsData.TournamentsPanel.tournaments_info_list)

    def get_tournaments_info_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.TournamentsPanel.tournaments_info_list)

    def get_tournaments_info_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.TournamentsPanel.tournaments_info_list)

    def get_tournaments_index_list(self):
        tournaments_index_list = []
        parent_id_list = self.get_parent_id_list(element_data=ElementsData.TournamentsPanel.bg_list)
        cur = 0
        while cur < len(parent_id_list):
            position_list = self.get_position_list(object_id=parent_id_list[cur], offspring_path="tournaments_info>logo")
            if not position_list:
                cur += 1
                continue
            tournaments_index_list.append(cur)
            cur += 1
        return tournaments_index_list

    def click_btn_setting(self):
        self.click_element(element_data=ElementsData.TournamentsPanel.btn_setting)

    def click_btn_magnifier(self):
        self.click_element(element_data=ElementsData.TournamentsPanel.btn_magnifier)

    def click_btn_turntable(self):
        self.click_element(element_data=ElementsData.TournamentsPanel.btn_turntable)

    def click_btn_flashcard_banner(self):
        self.click_element(element_data=ElementsData.TournamentsPanel.btn_flashcard_banner)

    def click_btn_players_tab(self, index=-1):
        viewport = TournamentsPanel.get_entrance_viewport(self)
        viewport.viewport_range[0] = viewport.viewport_range[0] + 0.15
        viewport.item_id_list = self.get_object_id_list(element_data=ElementsData.TournamentsPanel.btn_players_tab_list)
        self.click_object_of_plural_objects(element_data=ElementsData.TournamentsPanel.btn_players_tab_list, viewport=viewport, index=index)

    def click_flashcard_buff(self, index=-1):
        viewport = TournamentsPanel.get_entrance_viewport(self)
        viewport.item_id_list = self.get_object_id_list(element_data=ElementsData.TournamentsPanel.flashcard_buff_list)
        self.click_object_of_plural_objects(element_data=ElementsData.TournamentsPanel.flashcard_buff_list, viewport=viewport, index=index)


    class panel_popups_setting(BasePage):
        def click_btn_close(self):
            self.click_element(element_data=ElementsData.TournamentsPanel.panel_popups_setting.btn_close)

        def click_btn_i(self):
            self.click_element(element_data=ElementsData.TournamentsPanel.panel_popups_setting.btn_i)

        def click_btn_close_tips(self):
            self.click_element(element_data=ElementsData.TournamentsPanel.panel_popups_setting.btn_close_tips)

        def click_btn_switch(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.TournamentsPanel.panel_popups_setting.btn_switch_list, index=index)

    operation_pool = [
        {"element_data": ElementsData.TournamentsPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.btn_flashcard_banner, "func": click_btn_flashcard_banner, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.btn_leaderboard, "func": click_btn_leaderboard, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.btn_magnifier, "func": click_btn_magnifier, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.btn_players_tab_list, "func": click_btn_players_tab, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.btn_setting, "func": click_btn_setting, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.btn_turntable, "func": click_btn_turntable, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.flashcard_buff_list, "func": click_flashcard_buff, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.TournamentsPanel, "func": go_to_fishery_by_index, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.panel_popups_setting.btn_close, "func": panel_popups_setting.click_btn_close, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.panel_popups_setting.btn_close_tips, "func": panel_popups_setting.click_btn_close_tips, "weight": 10},
        {"element_data": ElementsData.TournamentsPanel.panel_popups_setting.btn_i, "func": panel_popups_setting.click_btn_i, "weight": 1},
        {"element_data": ElementsData.TournamentsPanel.panel_popups_setting.btn_switch_list, "func": panel_popups_setting.click_btn_switch, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # TournamentsPanel.click_btn_close(bp)
    # TournamentsPanel.click_btn_flashcard_banner(bp)
    # TournamentsPanel.click_btn_leaderboard(bp)
    # TournamentsPanel.click_btn_magnifier(bp)
    # TournamentsPanel.click_btn_players_tab(bp, 1)
    # TournamentsPanel.click_btn_setting(bp)
    # TournamentsPanel.click_btn_turntable(bp)
    # TournamentsPanel.click_flashcard_buff(bp)
    # TournamentsPanel.go_to_fishery_by_index(bp)
    # TournamentsPanel.panel_popups_setting.click_btn_close(bp)
    # TournamentsPanel.panel_popups_setting.click_btn_close_tips(bp)
    # TournamentsPanel.panel_popups_setting.click_btn_i(bp)
    # TournamentsPanel.panel_popups_setting.click_btn_switch(bp, 0)
    bp.connect_close()



