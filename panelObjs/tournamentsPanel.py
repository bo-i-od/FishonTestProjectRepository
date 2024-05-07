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


    def go_to_first_location(self):
        position_list = self.get_position_list(element_data=ElementsData.Tournaments.btn_enter_list)
        self.click_position(position_list[0])
        # entrance_list = self.get_element(ElementsData.Tournaments.entrance_list)
        # entrance_list[random.randint(0, 2)].click()

    def get_fishery_tpid_list(self):
        bg_list = self.get_icon_list(element_data=ElementsData.Tournaments.bg_list)
        cur = 0
        while cur < len(bg_list):
            bg_list[cur] = "icon_fisheries_" + bg_list[cur].split('_')[2]
            cur += 1
        worksheet = self.excelTools.get_worksheet("FISHERIES.xlsm", "模板数据")
        tpid_list = self.excelTools.same_row_different_column_convert_list(worksheet, "displayicon", "tpId", bg_list)
        cur = 0
        while cur < len(tpid_list):
            tpid_list[cur] = str(tpid_list[cur])
            cur += 1
        return tpid_list

    def get_entrance_viewport(self):
        size = self.get_size(element_data=ElementsData.Tournaments.panel_sidebar_bg)
        edge_left = 0.75 * size[0]
        entrance_viewport = Viewport(self, element_viewport=ElementsData.Tournaments.entrance_viewport, element_item_list=ElementsData.Tournaments.btn_enter_list, )
        entrance_viewport.viewport_range = [entrance_viewport.viewport_range[0], 1]
        entrance_viewport.viewport_edge = [edge_left, 0.05]
        entrance_viewport.viewport_range_shift()
        return entrance_viewport

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
        self.click_position(entrance_position)

    def click_btn_leaderboard(self):
        self.click_element(element_data=ElementsData.Tournaments.btn_leaderboard)


if __name__ == "__main__":
    bp = BasePage("b6h65hd64p5pxcyh")
    # TournamentsPanel.get_fishery_list(bp)
    entrance_viewport = TournamentsPanel.get_entrance_viewport(bp)
    entrance_viewport.move_until_appear(entrance_viewport.item_id_list[3])



