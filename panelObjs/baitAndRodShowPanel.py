from common.basePage import BasePage
from configs.elementsData import ElementsData


class BaitAndRodShowPanel(BasePage):
    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.BaitAndRodShow.tap_to_continue, ignore_set={"BaitAndRodShowPanel"})

    def is_panel_active(self):
        if self.exist(element_data=ElementsData.BaitAndRodShow.BaitAndRodShowPanel):
            return True
        return False

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.BaitAndRodShow.BaitAndRodShowPanel)

    def open_and_close_talent(self):
        position = self.click_element(element_data=ElementsData.BaitAndRodShow.talent)
        if not self.exist(element_data=ElementsData.BaitAndRodShow.tips_talent):
            # print("没有成功打开天赋细节")
            return False
        self.click_position(position)

    def open_and_close_5d(self):
        position = self.click_element(element_data=ElementsData.BaitAndRodShow.five_dimension)
        if not self.exist(element_data=ElementsData.BaitAndRodShow.tips_five_dimension):
            # print("没有成功打开5d细节")
            return False
        self.click_position(position)

    def get_gear_name(self):
        gear_name = self.get_text(element_data=ElementsData.BaitAndRodShow.name)
        return gear_name


