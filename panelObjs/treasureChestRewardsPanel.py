from common.basePage import BasePage
from configs.elementsData import ElementsData


class TreasureChestRewardsPanel(BasePage):
    def click_btn_close(self):
        self.wait_for_appear(element_data=ElementsData.TreasureChestRewards.TreasureChestRewardsPanel, is_click=True)
        self.click_element(element_data=ElementsData.TreasureChestRewards.btn_close)

    def click_open_x(self):
        self.click_element(element_data=ElementsData.TreasureChestRewards.btn_open)

    def get_open_x_n(self):
        self.wait_for_appear(element_data=ElementsData.TreasureChestRewards.TreasureChestRewardsPanel, is_click=True)
        open_x_n = self.get_text_list(element_data=ElementsData.TreasureChestRewards.btn_open)
        while not open_x_n:
            self.clear_popup_once()
            open_x_n = self.get_text_list(element_data=ElementsData.TreasureChestRewards.btn_open)
        n = open_x_n[0].split('x')[1]
        return int(n)

if __name__ == '__main__':
    bp = BasePage()
    TreasureChestRewardsPanel.click_open_x(bp)