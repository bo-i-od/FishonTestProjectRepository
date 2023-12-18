from common.basePage import BasePage
from configs.elementsData import ElementsData


class LeaderBoardPopResultPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.LeaderBoardPopResult.LeaderBoardPopResultPanel):
            return True
        return False
    def click_btn_claim(self):
        self.click_element(element_data=ElementsData.LeaderBoardPopResult.btn_claim)