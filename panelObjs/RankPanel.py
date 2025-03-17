from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class RankPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RankPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RankPanel.RankPanel)

    def get_fisheries_position_list(self):
        return self.get_position_list(element_data=ElementsData.RankPanel.fisheries_list)

    def get_fisheries_viewport(self):
        fisheries_viewport = Viewport(self, element_viewport=ElementsData.RankPanel.fisheries_viewport, element_item_list=ElementsData.RankPanel.fisheries_list, viewport_range=[0.1, 0.95])
        return fisheries_viewport

    def get_tab_area_position_list(self):
        tab_area_position_list = self.get_position_list(element_data=ElementsData.RankPanel.tab_area_list)
        return tab_area_position_list

    def get_tab_time_position_list(self):
        tab_time_position_list = self.get_position_list(element_data=ElementsData.RankPanel.tab_time_list)
        return tab_time_position_list

    def is_time_active(self):
        return self.exist(element_data=ElementsData.RankPanel.time)

    def get_photo_viewport(self):
        edge = [0.05, 0.05]
        photo_viewport = Viewport(self, element_viewport=ElementsData.RankPanel.photo_viewport, element_item_list=ElementsData.RankPanel.photo_list, viewport_edge=edge)
        return photo_viewport

    def get_photo_position_list(self):
        return self.get_position_list(element_data=ElementsData.RankPanel.photo_list)

    def get_photo_status(self):
        photo_id_list = self.get_object_id_list(element_data=ElementsData.RankPanel.photo_list)
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
        return self.get_object_id_list(element_data=ElementsData.RankPanel.photo_list)

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

    def switch_fishery(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RankPanel.fisheries_list, element_viewport=ElementsData.RankPanel.fisheries_viewport, viewport_range=[0.1, 0.95], index=index)

    def switch_tab_area(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RankPanel.tab_area_list, index=index)

    def switch_tab_time(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RankPanel.tab_time_list, index=index)

    def click_btn_playercard(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RankPanel.btn_playercard_list, element_viewport=ElementsData.RankPanel.photo_viewport, viewport_direction="column", index=index)

    def click_photo(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.RankPanel.photo_list, element_viewport=ElementsData.RankPanel.photo_viewport, viewport_direction="column", index=index)


    operation_pool = [
        {"element_data": ElementsData.RankPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.RankPanel.btn_playercard_list, "func": click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.RankPanel.photo_list, "func": click_photo, "weight": 1},
        {"element_data": ElementsData.RankPanel.fisheries_list, "func": switch_fishery, "weight": 1},
        {"element_data": ElementsData.RankPanel.tab_area_list, "func": switch_tab_area, "weight": 1},
        {"element_data": ElementsData.RankPanel.tab_time_list, "func": switch_tab_time, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    # RankPanel.click_btn_close(bp)
    # RankPanel.click_btn_playercard(bp)
    # RankPanel.click_photo(bp)
    RankPanel.switch_fishery(bp, index=0)
    # RankPanel.switch_tab_area(bp)
    # RankPanel.switch_tab_time(bp)
    bp.connect_close()