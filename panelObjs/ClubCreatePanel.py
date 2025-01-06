import random
import string
from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import generate_random_string


class ClubCreatePanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ClubCreatePanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ClubCreatePanel.ClubCreatePanel)

    def click_btn_create(self):
        self.click_element(element_data=ElementsData.ClubCreatePanel.btn_cast)

    def input_club_name(self, text=None):
        if text is None:
            letters = string.ascii_letters
            text = random.choice(letters) + generate_random_string(random.randint(0, 7))
        self.set_text(element_data=ElementsData.ClubCreatePanel.Input_clubname, text=text)
        self.click_element(element_data=ElementsData.ClubCreatePanel.Input_clubname)
        self.sleep(0.1)
        self.click_position([0.5, 0.5])


    def input_club_introduction(self, text=None):
        if text is None:
            text = generate_random_string(random.randint(0, 40))
        self.set_text(element_data=ElementsData.ClubCreatePanel.Input_clubintroduction, text=text)
        self.click_element(element_data=ElementsData.ClubCreatePanel.Input_clubintroduction)
        self.sleep(0.1)
        self.click_position([0.5, 0.5])

    def click_tag(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubCreatePanel.tag_list, index=index)

    def click_btn_limit(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubCreatePanel.btns_limit, index=index)

    def switch_tab_flag(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubCreatePanel.tabs_flag, index=index)

    def click_block(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubCreatePanel.block_list, index=index)

    def click_flag(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubCreatePanel.flag_list, index=index, element_viewport=ElementsData.ClubCreatePanel.viewport_flag, viewport_direction="column")

    operation_pool = [
        {"element_data": ElementsData.ClubCreatePanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubCreatePanel.btn_cast, "func": click_btn_create, "weight": 1},
        {"element_data": ElementsData.ClubCreatePanel.Input_clubname, "func": input_club_name, "weight": 1},
        {"element_data": ElementsData.ClubCreatePanel.Input_clubintroduction, "func": input_club_introduction, "weight": 1},
        {"element_data": ElementsData.ClubCreatePanel.tag_list, "func": click_tag, "weight": 2},
        {"element_data": ElementsData.ClubCreatePanel.btns_limit, "func": click_btn_limit, "weight": 2},
        {"element_data": ElementsData.ClubCreatePanel.tabs_flag, "func": switch_tab_flag, "weight": 1},
        {"element_data": ElementsData.ClubCreatePanel.block_list, "func": click_block, "weight": 1},
        {"element_data": ElementsData.ClubCreatePanel.flag_list, "func": click_flag, "weight": 1},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    # ClubCreatePanel.click_btn_close(bp)
    # ClubCreatePanel.click_btn_create(bp)
    ClubCreatePanel.input_club_name(bp)
    ClubCreatePanel.input_club_introduction(bp)
    # ClubCreatePanel.click_tag(bp)
    # ClubCreatePanel.click_btn_limit(bp)
    # ClubCreatePanel.switch_tab_flag(bp)
    # ClubCreatePanel.click_block(bp)
    # ClubCreatePanel.click_flag(bp, 0)
    bp.connect_close()