import re

from common.basePage import BasePage
from configs.elementsData import ElementsData


class TreasureChestRewardsPanel(BasePage):
    def skip_anime(self):
        self.wait_for_appear(element_data=ElementsData.TreasureChestRewards.TreasureChestRewardsPanel, is_click=True, ignore_set={"TreasureChestRewardsPanel"})
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.TreasureChestRewards.btn_close)

    def get_box_fragment_position(self):
        position_list = self.get_position_list(element_data=ElementsData.TreasureChestRewards.box_fragment)
        if position_list:
            return position_list[0]
        return []

    def click_open_x(self):
        self.click_element(element_data=ElementsData.TreasureChestRewards.btn_open)

    def get_open_x_n(self):
        self.wait_for_appear(element_data=ElementsData.TreasureChestRewards.TreasureChestRewardsPanel, is_click=True, ignore_set={"TreasureChestRewardsPanel"})
        open_x_n = self.get_text_list(element_data=ElementsData.TreasureChestRewards.btn_open)
        while not open_x_n:
            self.clear_popup_once()
            open_x_n = self.get_text_list(element_data=ElementsData.TreasureChestRewards.btn_open)
        pattern = r"\d+"
        match = re.search(pattern, open_x_n[0])
        n = match.group()
        return int(n)

if __name__ == '__main__':
    bp = BasePage()
    TreasureChestRewardsPanel.click_open_x(bp)