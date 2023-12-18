import random

from common.basePage import BasePage
from configs.elementsData import ElementsData

class TournamentsPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.Tournaments.btn_close)

    def random_tournament(self):
        position_list = self.get_position_list(element_data=ElementsData.Tournaments.entrance_list)
        self.click_position(position_list[0])
        # entrance_list = self.get_element(ElementsData.Tournaments.entrance_list)
        # entrance_list[random.randint(0, 2)].click()
