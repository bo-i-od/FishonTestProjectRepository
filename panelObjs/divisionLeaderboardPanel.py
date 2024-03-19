from configs.elementsData import ElementsData
from common.basePage import BasePage
from tools.commonTools import *

class DivisionLeaderboardPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.DivisionLeaderboard.btn_close)
        if DivisionLeaderboardPanel.is_panel_active(self):
            raise FindElementError

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.DivisionLeaderboard.DivisionLeaderboardPanel):
            return True
        return False

    def switch_tab(self, index):
        position_list = self.get_position_list(element_data=ElementsData.DivisionLeaderboard.tab_list)
        self.click_position(position_list[index])

    def click_btn_alldivisions(self):
        self.click_element(element_data=ElementsData.DivisionLeaderboard.btn_alldivisions)

if __name__ == '__main__':
    bp = BasePage()
    DivisionLeaderboardPanel.switch_tab(bp, 0)