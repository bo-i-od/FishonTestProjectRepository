from common.basePage import BasePage
from configs.elementsData import ElementsData


class ChampionshipNewPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ChampionshipNewPanel.ChampionshipNewPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ChampionshipNewPanel.btn_close)

    def is_completed(self):
        return self.exist(element_data=ElementsData.ChampionshipNewPanel.text_completed)