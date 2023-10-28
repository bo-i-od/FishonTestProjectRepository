from common.basePage import BasePage
from configs.elementsData import ElementsData
import json


class ChampoinshipTournamentsPanel(BasePage):
    def get_points_list(self):
        return self.get_text_list(element_data=ElementsData.ChampoinshipTournaments.current_tournament.points_list)

    def get_rank_list(self):
        return self.get_text_list(element_data=ElementsData.ChampoinshipTournaments.current_tournament.rank_list)

    def get_name_list(self):
        return self.get_text_list(element_data=ElementsData.ChampoinshipTournaments.current_tournament.player_name_list)

    def get_data_myself(self):
        points_myself = self.get_text(
            element_data=ElementsData.ChampoinshipTournaments.current_tournament.points_myself)
        flag_myself = self.get_icon(element_data=ElementsData.ChampoinshipTournaments.current_tournament.flag_myself)
        head_myself = self.get_icon(element_data=ElementsData.ChampoinshipTournaments.current_tournament.head_myself)
        rank_myself = self.get_text(element_data=ElementsData.ChampoinshipTournaments.current_tournament.rank_myself)
        player_name_myself = self.get_text(
            element_data=ElementsData.ChampoinshipTournaments.current_tournament.player_name_myself)
        return rank_myself, head_myself, flag_myself, player_name_myself, points_myself

    def get_rank_data(self):
        if self.exist(element_data=ElementsData.ChampoinshipTournaments.btn_fold) is False:
            self.click_a_until_b_appear(element_data_a=ElementsData.ChampoinshipTournaments.btn_unfold,
                                        element_data_b=ElementsData.ChampoinshipTournaments.btn_fold)
        self.click_a_until_b_appear(element_data_a=ElementsData.ChampoinshipTournaments.current_tournament.tab_rank,
                                    element_data_b=ElementsData.ChampoinshipTournaments.current_tournament.points_list)
        points_list = ChampoinshipTournamentsPanel.get_points_list(self)
        rank_list = ChampoinshipTournamentsPanel.get_rank_list(self)
        name_list = ChampoinshipTournamentsPanel.get_name_list(self)
        return rank_list, name_list, points_list

    def save_rank_data(self, rank_list, name_list, points_list, times):
        cur = 0
        while cur < len(points_list):
            res = {}
            res["rank"] = rank_list[cur]
            res["name"] = name_list[cur]
            res["points"] = points_list[cur]
            res_json = json.dumps(res)
            with open(f'C:/Users/TU/Desktop/soroya20-30/{times}.txt', 'a', encoding='utf-8') as f:
                f.write(res_json)
                f.write('\n')
                f.close()
            cur += 1


if __name__ == '__main__':
    pass
