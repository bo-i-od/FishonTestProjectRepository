from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class RankPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Rank.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Rank.RankPanel)

    def get_fisheries_position_list(self):
        return self.get_position_list(element_data=ElementsData.Rank.fisheries_list)

    def get_fisheries_viewport(self):
        edge_up = 0.05
        edge_down = 0.05
        fisheries_viewport = Viewport(self, element_viewport=ElementsData.Rank.fisheries_viewport, element_item_list=ElementsData.Rank.fisheries_list, viewport_edge=[edge_up, edge_down])
        return fisheries_viewport

    def get_tab_area_position_list(self):
        tab_area_position_list = self.get_position_list(element_data=ElementsData.Rank.tab_area_list)
        return tab_area_position_list

    def get_tab_time_position_list(self):
        tab_time_position_list = self.get_position_list(element_data=ElementsData.Rank.tab_time_list)
        return tab_time_position_list

    def is_time_active(self):
        return self.exist(element_data=ElementsData.Rank.time)

    def get_photo_viewport(self):
        edge = [0.05, 0.05]
        photo_viewport = Viewport(self, element_viewport=ElementsData.Rank.photo_viewport, element_item_list=ElementsData.Rank.photo_list, viewport_edge=edge)
        return photo_viewport

    def get_photo_position_list(self):
        return self.get_position_list(element_data=ElementsData.Rank.photo_list)

    def get_photo_status(self):
        photo_id_list = self.get_object_id_list(element_data=ElementsData.Rank.photo_list)
        cur = 0
        data_list = []
        no_data_list = []
        while cur < len(photo_id_list):
            no_player = self.get_offspring_id_list(object_id=photo_id_list[cur], offspring_path="tips")
            if no_player:
                no_data_list.append(cur)
                cur += 1
                continue
            data_list.append(cur)
            cur += 1
        return data_list, no_data_list

    def get_photo_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.Rank.photo_list)

    def get_rank_data(self, index):
        photo_id_list = RankPanel.get_photo_id_list(self)
        rank_data = {
            "player_name": self.get_text(object_id=photo_id_list[index], offspring_path="player_info>player_name"),
            "division": self.get_icon(object_id=photo_id_list[index], offspring_path="player_info>division"),
            "lv": self.get_text(object_id=photo_id_list[index], offspring_path="player_info>lv"),
            "rating": self.get_text(object_id=photo_id_list[index], offspring_path="player_info>rating>num"),
            "head_img": self.get_icon(object_id=photo_id_list[index], offspring_path="player_info>head>head_mask>head_img"),
            "rank": self.get_icon(object_id=photo_id_list[index], offspring_path="rank"),
            "fish": self.get_icon_list(object_id=photo_id_list[index], offspring_path="fish"),
            "fish_black": self.get_icon_list(object_id=photo_id_list[index], offspring_path="fish_black"),
            "fish_name": self.get_text(object_id=photo_id_list[index], offspring_path="fish_name"),
            "points": self.get_text(object_id=photo_id_list[index], offspring_path="points")}
        return rank_data

if __name__ == '__main__':
    bp = BasePage()
    print(RankPanel.get_photo_status(bp))
