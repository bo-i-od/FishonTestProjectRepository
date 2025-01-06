import random
import string
from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import generate_random_string


class ClubModifyPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ClubModifyPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ClubModifyPanel.ClubModifyPanel)

    def click_btn_disband(self):
        self.click_element(element_data=ElementsData.ClubModifyPanel.btn_disband)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.ClubModifyPanel.btn_confirm)

    def input_club_name(self, text=None):
        if text is None:
            letters = string.ascii_letters
            text = random.choice(letters) + generate_random_string(random.randint(0, 7))
        self.set_text(element_data=ElementsData.ClubModifyPanel.Input_clubname, text=text)
        self.click_element(element_data=ElementsData.ClubModifyPanel.Input_clubname)
        self.sleep(0.1)
        self.click_position([0.5, 0.5])


    def input_club_introduction(self, text=None):
        if text is None:
            text = generate_random_string(random.randint(0, 40))
        self.set_text(element_data=ElementsData.ClubModifyPanel.Input_clubintroduction, text=text)
        self.click_element(element_data=ElementsData.ClubModifyPanel.Input_clubintroduction)
        self.sleep(0.1)
        self.click_position([0.5, 0.5])

    def click_tag(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubModifyPanel.tag_list, index=index)

    def click_btn_limit(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubModifyPanel.btns_limit, index=index)

    def switch_tab_flag(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubModifyPanel.tabs_flag, index=index)

    def click_block(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubModifyPanel.block_list, index=index)

    def click_flag(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubModifyPanel.flag_list, index=index, element_viewport=ElementsData.ClubModifyPanel.viewport_flag, viewport_direction="column")

    operation_pool = [
        {"element_data": ElementsData.ClubModifyPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.btn_disband, "func": click_btn_disband, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.Input_clubname, "func": input_club_name, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.Input_clubintroduction, "func": input_club_introduction, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.tag_list, "func": click_tag, "weight": 2},
        {"element_data": ElementsData.ClubModifyPanel.btns_limit, "func": click_btn_limit, "weight": 2},
        {"element_data": ElementsData.ClubModifyPanel.tabs_flag, "func": switch_tab_flag, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.block_list, "func": click_block, "weight": 1},
        {"element_data": ElementsData.ClubModifyPanel.flag_list, "func": click_flag, "weight": 1},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)
    # ClubModifyPanel.click_btn_close(bp)
    # ClubModifyPanel.click_btn_disband(bp)
    # ClubModifyPanel.click_btn_confirm(bp)
    # ClubModifyPanel.input_club_name(bp)
    # ClubModifyPanel.input_club_introduction(bp)
    # ClubModifyPanel.click_tag(bp)
    # ClubModifyPanel.click_btn_limit(bp)
    # ClubModifyPanel.switch_tab_flag(bp)
    # ClubModifyPanel.click_block(bp)
    # ClubModifyPanel.click_flag(bp)
    bp.connect_close()