import re

from common.basePage import BasePage
from configs.elementsData import ElementsData

class HomePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Home.HomePanel)

    def get_head_img(self):
        head_img = self.get_icon(element_data=ElementsData.Home.head_img)
        return head_img

    def get_flag(self):
        flag = self.get_icon(element_data=ElementsData.Home.flag)
        return flag

    def get_player_name(self):
        player_name = self.get_text(element_data=ElementsData.Home.player_name)
        return player_name

    def get_rating(self):
        rating = self.get_text(element_data=ElementsData.Home.rating)
        return rating

    def is_btn_questionnaire_exist(self):
        return self.exist(element_data=ElementsData.Home.btn_questionnaire)

    def get_level(self):
        player_lv = self.get_text(element_data=ElementsData.Home.player_lv)
        return player_lv

    def get_player_info(self):
        lv = int(self.get_text(element_data=ElementsData.Home.player_lv))
        rating = int(self.get_text(element_data=ElementsData.Home.rating))
        player_info = {
            "player_name": self.get_text(element_data=ElementsData.Home.player_name),
            "head_img": self.get_icon(element_data=ElementsData.Home.head_img),
            "lv": lv,
            "rating": rating,
            "head_frame": self.get_icon(element_data=ElementsData.Home.head_frame),
        }
        return player_info


    class Minitask(BasePage):
        def click_btn_recommend(self):
            self.click_element(element_data=ElementsData.Home.Minitask.btn_recommend)

        def click_btn_go(self):
            self.click_element(element_data=ElementsData.Home.Minitask.btn_go)

        def get_progress(self):
            progress = self.get_text(element_data=ElementsData.Home.Minitask.progress)
            res = progress.split("/")
            numerator = int(res[0])
            denominator = int(res[1])
            return numerator, denominator

        def click_btn_claim(self):
            self.click_element(element_data=ElementsData.Home.Minitask.btn_claim)

        def get_text_task(self):
            return self.get_text(element_data=ElementsData.Home.Minitask.text_task)







if __name__ == '__main__':
    bp = BasePage()
    print(HomePanel.get_exp_val(bp))



