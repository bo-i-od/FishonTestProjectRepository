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
        exp_progress = self.get_slider_value(ElementsData.Home.exp)[0]
        print(exp_progress)
        # 得到当前等级经验上限
        exp_limit = HomePanel.get_exp_limit_val(self,lv)
        # 经验 = 经验上限 * 进度条占总进度的百分比
        exp = int(exp_progress * exp_limit + 0.5)  # 求出的数是float需要四舍五入一下
        return exp, lv

    def get_exp_limit_val(self, lv):
        return self.excelTools.get_exp_limit(lv)

    # 跳转界面
    def go_to(self, element):
        self.try_click_element(element_data=element)

    def go_to_BattlePassPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_bp)

    def go_to_TaskPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_task)

    def go_to_FishCardPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_album)

    def go_to_RoulettePanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_roulette)

    def go_to_PlayerSettingPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.player_info)

    def go_to_AchievementPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_achievement)

    def go_to_MailPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_mail)

    def go_to_RechargeBlack5Panel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_black5)

    def go_to_PVPHallPanel(self):
        HomePanel.go_to(self, element=ElementsData.Home.btn_pvp)


if __name__ == '__main__':
    bp = BasePage()



