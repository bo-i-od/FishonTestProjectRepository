from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import compare


class RankFishLeaderboardPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.RankFishLeaderboard.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RankFishLeaderboard.RankFishLeaderboardPanel)

    def get_rank_data(self):
        photo_id = self.get_object_id(element_data=ElementsData.RankFishLeaderboard.photo)
        rank_data = {"player_name": self.get_text(object_id=photo_id, offspring_path="player_info>player_name"),
                     "division": self.get_icon(object_id=photo_id, offspring_path="player_info>division"),
                     "lv": self.get_text(object_id=photo_id, offspring_path="player_info>lv"),
                     "rating": self.get_text(object_id=photo_id, offspring_path="player_info>rating>num"),
                     "head_img": self.get_icon(object_id=photo_id, offspring_path="player_info>head>head_mask>head_img"),
                     "rank": self.get_icon(object_id=photo_id, offspring_path="rank"),
                     "fish": self.get_icon_list(object_id=photo_id, offspring_path="fish"),
                     "fish_black": self.get_icon_list(object_id=photo_id, offspring_path="fish_black"),
                     "fish_name": self.get_text(object_id=photo_id, offspring_path="fish_name"),
                     "points": self.get_text(object_id=photo_id, offspring_path="points")}
        ranking_id_list = self.get_object_id_list(element_data=ElementsData.RankFishLeaderboard.rank_list)
        ranking_id = ranking_id_list[0]
        player_name = self.get_text(object_id=ranking_id, offspring_path="player_name")
        division = self.get_icon(object_id=ranking_id, offspring_path="division")
        lv = self.get_text(object_id=ranking_id, offspring_path="lv")
        rating = self.get_text(object_id=ranking_id, offspring_path="rating>num")
        head_img = self.get_icon(object_id=ranking_id, offspring_path="head>head_mask>head_img")
        rank = self.get_icon(object_id=ranking_id, offspring_path="rank")
        points = self.get_text(object_id=ranking_id, offspring_path="score>value_2").split(">")[1].split("<")[0]
        compare(rank_data["player_name"], player_name)
        compare(rank_data["division"], division)
        compare(rank_data["lv"], lv)
        compare(rank_data["rating"], rating)
        compare(rank_data["head_img"], head_img)
        compare(rank_data["rank"], rank)
        compare(rank_data["points"], points)
        return rank_data

    def get_rank_data_oversea(self):
        photo_id = self.get_object_id(element_data=ElementsData.RankFishLeaderboard.photo)
        rank_data = {"player_name": self.get_text(object_id=photo_id, offspring_path="player_info>player_name_model>player_name"),
                     "division": self.get_icon(object_id=photo_id, offspring_path="player_info>player_name_model>division"),
                     "lv": self.get_text(object_id=photo_id, offspring_path="player_info>lv"),
                     "rating": self.get_text(object_id=photo_id, offspring_path="player_info>rating>num"),
                     "head_img": self.get_icon(object_id=photo_id, offspring_path="player_info>head>head_mask>head_img"),
                     "rank": self.get_icon(object_id=photo_id, offspring_path="rank"),
                     "fish": self.get_icon_list(object_id=photo_id, offspring_path="fish"),
                     "fish_black": self.get_icon_list(object_id=photo_id, offspring_path="fish_black"),
                     "fish_name": self.get_text(object_id=photo_id, offspring_path="fish_name"),
                     "points": self.get_text(object_id=photo_id, offspring_path="points")}
        ranking_id_list = self.get_object_id_list(element_data=ElementsData.RankFishLeaderboard.rank_list)
        ranking_id = ranking_id_list[0]
        player_name = self.get_text(object_id=ranking_id, offspring_path="player_name_model>player_name")
        division = self.get_icon(object_id=ranking_id, offspring_path="player_name_model>division")
        lv = self.get_text(object_id=ranking_id, offspring_path="lv")
        rating = self.get_text(object_id=ranking_id, offspring_path="rating>num")
        head_img = self.get_icon(object_id=ranking_id, offspring_path="head>head_mask>head_img")
        rank = self.get_icon(object_id=ranking_id, offspring_path="rank")
        points = self.get_text(object_id=ranking_id, offspring_path="score>value_2").split(">")[1].split("<")[0]
        compare(rank_data["player_name"], player_name)
        compare(rank_data["division"], division)
        compare(rank_data["lv"], lv)
        compare(rank_data["rating"], rating)
        compare(rank_data["head_img"], head_img)
        compare(rank_data["rank"], rank)
        compare(rank_data["points"], points)
        return rank_data


    def click_btn_like(self):
        self.click_element(element_data=ElementsData.RankFishLeaderboard.btn_like)

    def get_like_value(self):
        like_value = self.get_text(element_data=ElementsData.RankFishLeaderboard.like_value)
        return int(like_value)

    def is_btn_like_normal(self):
        btn_normal = self.get_object_id_list(element_data=ElementsData.RankFishLeaderboard.btn_like, offspring_path="btn_normal")
        if btn_normal:
            return True
        return False


if __name__ == '__main__':
    bp = BasePage()
    a = RankFishLeaderboardPanel.get_rank_data(bp)
    print(a)
