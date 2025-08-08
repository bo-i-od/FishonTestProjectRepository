from common.basePage import BasePage
from configs.elementsData import ElementsData


class ChampionshipNavigationPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ChampionshipNavigationPanel.ChampionshipNavigationPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ChampionshipNavigationPanel.btn_close)

    def get_logo_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.ChampionshipNavigationPanel.logo_list)
        return icon_list
