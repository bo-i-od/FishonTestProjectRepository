from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class TournamentsPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Tournaments.TournamentsPanel):
            return True
        return False
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Tournaments.btn_close)


    def get_fishery_tpid_list(self):
        table_data = self.excelTools.get_table_data("FISHERIES.xlsm")
        bg_list = self.get_icon_list(element_data=ElementsData.Tournaments.bg_list)
        cur = 0
        while cur < len(bg_list):
            bg_list[cur] = "icon_fisheries_" + bg_list[cur].split('_')[2]
            cur += 1

        tpId_list = table_data["tpId"]
        res_list = []
        displayicon_list = table_data["displayicon"]

        cur = 0
        while cur < len(bg_list):
            if bg_list[cur] not in displayicon_list:
                res_list.append("")
                cur += 1
                continue
            index = displayicon_list.index(bg_list[cur])
            tpId = tpId_list[index]
            res_list.append(str(tpId))
            cur += 1
            continue
        return res_list

    def get_entrance_viewport(self):
        size = self.get_size(element_data=ElementsData.Tournaments.panel_sidebar_bg)
        edge_left = 0.75 * size[0]
        entrance_viewport = Viewport(self, element_viewport=ElementsData.Tournaments.entrance_viewport, element_item_list=ElementsData.Tournaments.btn_enter_list)
        entrance_viewport.viewport_range = [entrance_viewport.viewport_range[0], 1]
        entrance_viewport.viewport_edge = [edge_left, 0.05]
        entrance_viewport.viewport_range_shift()
        return entrance_viewport

    def get_fisheries_table_data(self):
        table_data = self.excelTools.get_table_data("FISHERIES.xlsm")
        return table_data

    def get_fish_list(self, fishery_id):
        table_data = TournamentsPanel.get_fisheries_table_data(self)
        tpId_list = table_data["tpId"]
        index = tpId_list.index(int(fishery_id))
        fish_list = table_data["fish"]
        res_list = []
        cur = 0
        while cur < len(fish_list):
            fish_id = fish_list[cur][index]
            if fish_id in [0, "0", ""]:
                cur += 1
                continue
            res_list.append(str(fish_id))
            cur += 1
        return res_list


    # 跳转指定tpid渔场
    def go_to_fishery_by_tpid(self, fishery_tpid):
        fishery_tpid_list = TournamentsPanel.get_fishery_tpid_list(self)
        index = fishery_tpid_list.index(fishery_tpid)
        TournamentsPanel.go_to_fishery_by_index(self, index)

    # 跳转指定索引渔场
    def go_to_fishery_by_index(self, index):
        entrance_viewport = TournamentsPanel.get_entrance_viewport(self)
        entrance_viewport.move_until_appear(entrance_viewport.item_id_list[index])
        entrance_position = self.get_position(object_id=entrance_viewport.item_id_list[index])
        while self.exist(object_id=entrance_viewport.item_id_list[index]):
            self.click_position(entrance_position)
            self.sleep(0.2)

    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.Tournaments.btn_leaderboard)

    def get_tournaments_info_position_list(self):
        return self.get_position_list(element_data=ElementsData.Tournaments.tournaments_info_list)

    def get_tournaments_info_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.Tournaments.tournaments_info_list)


if __name__ == "__main__":
    bp = BasePage("192.168.111.77:20086")
    # TournamentsPanel.get_fishery_list(bp)
    a = TournamentsPanel.go_to_fishery_by_tpid(bp, "400301")

    print(a)



