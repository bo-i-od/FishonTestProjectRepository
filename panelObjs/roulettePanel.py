from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class RoulettePanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.Roulette.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Roulette.RoulettePanel)

    def click_btn_spin(self):
        self.click_element(element_data=ElementsData.Roulette.btn_spin)

    def press_btn_spin(self, t):
        self.press(element_data=ElementsData.Roulette.btn_spin, duration=t)

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.Roulette.reward_icon_list)
        return reward_icon_list

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.Roulette.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    def get_ticket(self):
        ticket = self.get_text(element_data=ElementsData.Roulette.ticket_count)
        ticket = ticket.split('</color>')
        ticket_count = str_to_int(ticket[0].split('>')[1])
        ticket_cost = str_to_int(ticket[1].split('>')[1])
        return ticket_count, ticket_cost

    def get_turntable_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.Roulette.turntable_icon_list)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.Roulette.btn_i)

    def click_btn_announcement(self):
        self.click_element(element_data=ElementsData.Roulette.btn_announcement)


if __name__ == '__main__':
    bp = BasePage()
    RoulettePanel.click_btn_spin(bp)