from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class RoulettePanel(BasePage):
    def click_btn_close(self):
        self.click_until_disappear(element_data=ElementsData.RoulettePanel.btn_close, ignore_set={"RoulettePanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.RoulettePanel.RoulettePanel)

    def click_btn_spin(self):
        self.click_element(element_data=ElementsData.RoulettePanel.btn_spin)

    def press_btn_spin(self, t):
        self.press(element_data=ElementsData.RoulettePanel.btn_spin, duration=t)

    def get_reward_icon_list(self):
        reward_icon_list = self.get_icon_list(element_data=ElementsData.RoulettePanel.reward_icon_list)
        return reward_icon_list

    def get_reward_quantity_list(self):
        reward_quantity_list = self.get_text_list(element_data=ElementsData.RoulettePanel.reward_quantity_list)
        str_to_int_list(reward_quantity_list)
        return reward_quantity_list

    def get_ticket(self):
        ticket = self.get_text(element_data=ElementsData.RoulettePanel.ticket_count)
        ticket = ticket.split('</color>')
        ticket_count = str_to_int(ticket[0].split('>')[1])
        ticket_cost = str_to_int(ticket[1].split('>')[1])
        return ticket_count, ticket_cost

    def get_turntable_icon_list(self):
        return self.get_icon_list(element_data=ElementsData.RoulettePanel.turntable_icon_list)

    def click_btn_i(self):
        self.click_element(element_data=ElementsData.RoulettePanel.btn_i)

    def click_btn_announcement(self):
        self.click_element(element_data=ElementsData.RoulettePanel.btn_announcement)

    def click_btn_close_tips(self):
        self.click_element(element_data=ElementsData.RoulettePanel.btn_close_tips)


    operation_pool = [
        {"element_data": ElementsData.RoulettePanel.btn_announcement, "func": click_btn_announcement, "weight": 1},
        {"element_data": ElementsData.RoulettePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.RoulettePanel.btn_close_tips, "func": click_btn_close_tips, "weight": 1},
        {"element_data": ElementsData.RoulettePanel.btn_i, "func": click_btn_i, "weight": 1},
        {"element_data": ElementsData.RoulettePanel.btn_spin, "func": click_btn_spin, "weight": 1},

        {"element_data": ElementsData.RoulettePanel.btn_spin, "func": press_btn_spin, "weight": 1},
    ]


if __name__ == "__main__":
    bp = BasePage()
    RoulettePanel.click_btn_announcement(bp)
    RoulettePanel.click_btn_close(bp)
    RoulettePanel.click_btn_close_tips(bp)
    RoulettePanel.click_btn_i(bp)
    RoulettePanel.click_btn_spin(bp)
    RoulettePanel.press_btn_spin(bp)
    bp.connect_close()