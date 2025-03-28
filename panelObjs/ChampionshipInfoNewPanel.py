from common.basePage import BasePage
from configs.elementsData import ElementsData


class ChampionshipInfoNewPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ChampionshipInfoNewPanel.ChampionshipInfoNewPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ChampionshipInfoNewPanel.btn_close)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ChampionshipInfoNewPanel.tab_list, index=index)

    def is_checked(self):
        return self.exist(element_data=ElementsData.ChampionshipInfoNewPanel.check)

    def get_progress(self):
        progress_cur_text, progress_max_text = self.get_text_list(element_data_list=[ElementsData.ChampionshipInfoNewPanel.progress_cur, ElementsData.ChampionshipInfoNewPanel.progress_max])
        progress_cur = int(progress_cur_text[0])
        progress_max = int(progress_max_text[0])
        return progress_cur, progress_max


