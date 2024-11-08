from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class TournamentsPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Tournaments.TournamentsPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Tournaments.btn_close)


    def get_fishery_tpid_list(self):
        table_data_detail = self.excelTools.get_table_data_detail(book_name="FISHERIES.xlsm")
        bg_list = self.get_icon_list(element_data=ElementsData.Tournaments.bg_list)
        cur = 0
        while cur < len(bg_list):
            bg_list[cur] = "icon_fisheries_" + bg_list[cur].split('_')[2]
            cur += 1

        res_list = []
        cur = 0
        while cur < len(bg_list):
            table_data_object_list = self.excelTools.get_table_data_object_list_by_key_value(key="displayicon", value=bg_list[cur], table_data_detail=table_data_detail)
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
        size = self.get_size(element_data=ElementsData.Tournaments.panel_sidebar_bg)
        edge_left = 0.75 * size[0]
        # 多人房进入按钮和单人房加一起
        model_id_list = self.get_object_id_list(element_data=ElementsData.Tournaments.model_list)
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
        entrance_viewport = Viewport(self, element_viewport=ElementsData.Tournaments.entrance_viewport, item_id_list= item_id_list)
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
    def go_to_fishery_by_index(self, index):
        entrance_viewport = TournamentsPanel.get_entrance_viewport(self)
        while self.exist(object_id=entrance_viewport.item_id_list[index]):
            entrance_viewport.move_until_appear(entrance_viewport.item_id_list[index])
            entrance_position = self.get_position(object_id=entrance_viewport.item_id_list[index])
            self.click_position(entrance_position)
            self.sleep(0.2)

    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.Tournaments.btn_leaderboard)

    def get_tournaments_info_position_list(self):
        return self.get_position_list(element_data=ElementsData.Tournaments.tournaments_info_list)

    def get_tournaments_info_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.Tournaments.tournaments_info_list)

    def get_tournaments_info_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.Tournaments.tournaments_info_list)

    def get_tournaments_index_list(self):
        tournaments_index_list = []
        parent_id_list = self.get_parent_id_list(element_data=ElementsData.Tournaments.bg_list)
        cur = 0
        while cur < len(parent_id_list):
            position_list = self.get_position_list(object_id=parent_id_list[cur], offspring_path="tournaments_info>logo")
            if not position_list:
                cur += 1
                continue
            tournaments_index_list.append(cur)
            cur += 1
        return tournaments_index_list


if __name__ == "__main__":
    bp = BasePage(serial_number="127.0.0.1:21503", is_mobile_device=True)
    # TournamentsPanel.get_fishery_list(bp)
    # a = TournamentsPanel.get_fishery_tpid_list(bp)
    parent_id_list = TournamentsPanel.get_tournaments_index_list(bp)
    print(parent_id_list)
    # print(a)
    bp.connect_close()



