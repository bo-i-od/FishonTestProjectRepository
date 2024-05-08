import re

from common.basePage import BasePage
from configs.elementsData import ElementsData

class HomePanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.Home.HomePanel):
            return True
        return False

    # 获取玩家经验值
    def get_exp_val(self):
        # 得到等级
        lv_str = self.get_text(element_data=ElementsData.Home.player_lv)
        lv = int(lv_str)
        # 得到slider
        exp_progress = self.get_slider_value(element_data=ElementsData.Home.exp)
        print(exp_progress)
        # 得到当前等级经验上限
        exp_limit = HomePanel.get_exp_limit_val(self,lv)[0]
        print(exp_limit)
        # 经验 = 经验上限 * 进度条占总进度的百分比
        exp = int(exp_progress * exp_limit + 0.5)  # 求出的数是float需要四舍五入一下
        return exp, lv

    def get_exp_limit_val(self, lv):
        return self.excelTools.get_exp_limit(lv)

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
        if self.exist(element_data=ElementsData.Home.btn_questionnaire):
            return True
        return False

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



