from common.basePage import BasePage
from configs.elementsData import ElementsData


class BaitAndRodShowPanel(BasePage):
    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.BaitAndRodShow.closeArea)

    def open_and_close_talent(self):
        position = self.click_element(element_data=ElementsData.BaitAndRodShow.talent)
        if self.exist(element_data=ElementsData.BaitAndRodShow.tips_talent) is False:
            print("没有成功打开天赋细节")
            return False
        self.click_position(position)

    def open_and_close_5d(self):
        position = self.click_element(element_data=ElementsData.BaitAndRodShow.five_dimension)
        if self.exist(element_data=ElementsData.BaitAndRodShow.tips_five_dimension) is False:
            print("没有成功打开5d细节")
            return False
        self.click_position(position)

