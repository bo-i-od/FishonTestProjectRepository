from common.basePage import BasePage
from configs.elementsData import ElementsData
from common.viewport import Viewport

class TournamentsInfoPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.TournamentsInfo.TournamentsInfoPanel)
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.TournamentsInfo.btn_close)

    def switch_tab(self, index):
        tab_position_list = self.get_position_list(element_data=ElementsData.TournamentsInfo.tab_list)
        self.click_position(tab_position_list[index])