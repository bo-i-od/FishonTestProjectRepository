from common.basePage import BasePage
from configs.elementsData import ElementsData


class BaitAndRodShowPanel(BasePage):
    def click_tap_to_continue(self):
        self.click_element(element_data=ElementsData.BaitAndRodShowPanel.tap_to_continue, ignore_set={"BaitAndRodShowPanel"})

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BaitAndRodShowPanel.BaitAndRodShowPanel)

    def wait_for_panel_appear(self):
        self.wait_for_appear(element_data=ElementsData.BaitAndRodShowPanel.BaitAndRodShowPanel, ignore_set={"BaitAndRodShowPanel"})

    def open_and_close_talent(self):
        position = self.click_element(element_data=ElementsData.BaitAndRodShowPanel.talent)
        if not self.exist(element_data=ElementsData.BaitAndRodShowPanel.tips_talent):
            # print("没有成功打开天赋细节")
            return False
        self.click_position(position)

    def open_and_close_5d(self):
        position = self.click_element(element_data=ElementsData.BaitAndRodShowPanel.five_dimension)
        if not self.exist(element_data=ElementsData.BaitAndRodShowPanel.tips_five_dimension):
            # print("没有成功打开5d细节")
            return False
        self.click_position(position)

    def get_gear_name(self):
        gear_name = self.get_text(element_data=ElementsData.BaitAndRodShowPanel.name)
        return gear_name

    def click_skill(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.BaitAndRodShowPanel.skill_list, index=index, ignore_set={"BaitAndRodShowPanel"})

    operation_pool = [
        {"element_data": ElementsData.BaitAndRodShowPanel.tap_to_continue, "func": click_tap_to_continue, "weight": 1},
        {"element_data":ElementsData.BaitAndRodShowPanel.skill_list, "func": click_skill, "weight": 2},
        ]

if __name__ == '__main__':
    bp = BasePage()
    BaitAndRodShowPanel.click_skill(bp)
    bp.connect_close()