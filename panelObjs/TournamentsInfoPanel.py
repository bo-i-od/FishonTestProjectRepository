from common.basePage import BasePage
from configs.elementsData import ElementsData

class TournamentsInfoPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.TournamentsInfoPanel.TournamentsInfoPanel)

    def wait_for_panel_appear(self):
        while not TournamentsInfoPanel.is_panel_active(self):
            self.sleep(1)

    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.TournamentsInfoPanel.btn_close)

    def switch_tab(self, index):
        tab_position_list = self.get_position_list(element_data=ElementsData.TournamentsInfoPanel.tab_list)
        self.click_position(tab_position_list[index])

    def is_checked(self):
        return self.exist(element_data=ElementsData.TournamentsInfoPanel.check)

    def get_progress(self):
        progress_cur_text, progress_max_text = self.get_text_list(element_data_list=[ElementsData.TournamentsInfoPanel.progress_cur, ElementsData.TournamentsInfoPanel.progress_max])
        progress_cur = int(progress_cur_text[0])
        progress_max = int(progress_max_text[0])
        return progress_cur, progress_max
