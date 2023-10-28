from common.basePage import BasePage
from configs.elementsData import ElementsData


class TreasureChestRewardsPanel(BasePage):
    def close_TreasureChestRewardsPanel(self):
        self.wait_for_appear(element_data=ElementsData.TreasureChestRewards.TreasureChestRewardsPanel)
        self.try_click_element(element_data=ElementsData.TreasureChestRewards.btn_close)

    def click_open_x(self):
        self.click_element(element_data=ElementsData.TreasureChestRewards.btn_open_x)