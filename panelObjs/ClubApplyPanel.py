from common.basePage import BasePage
from configs.elementsData import ElementsData


class ClubApplyPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ClubApplyPanel.ClubApplyPanel)


    def click_btn_apply(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_apply)

    def click_btn_report(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_report)

    def click_btn_copy(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_copy)

    def click_btn_create(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_create)

    def click_btn_fast(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_fast)

    def click_btn_refresh(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_refresh)

    def click_btn_search(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_search)

    def click_toggle(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.toggle)

    def click_club(self):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubApplyPanel.club_list, element_viewport=ElementsData.ClubApplyPanel.viewport, viewport_direction="column")

    def get_club_id(self):
        text_list = self.get_text_list(element_data=ElementsData.ClubApplyPanel.club_id)
        if not text_list:
            return ""
        return text_list[0]

    def input_id(self, text=None):
        if text is None:
            text = ClubApplyPanel.get_club_id(self)
        print(text)
        self.set_text(element_data=ElementsData.ClubApplyPanel.Input_clubid, text=text)

    def click_btn_delete(self):
        self.click_element(element_data=ElementsData.ClubApplyPanel.btn_delete)
        
    operation_pool = [
        {"element_data": ElementsData.ClubApplyPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_apply, "func": click_btn_apply, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_search, "func": click_btn_search, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_refresh, "func": click_btn_refresh, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_copy, "func": click_btn_copy, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_create, "func": click_btn_create, "weight": 2},
        {"element_data": ElementsData.ClubApplyPanel.toggle, "func": click_toggle, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_fast, "func": click_btn_fast, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.btn_report, "func": click_btn_report, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.Input_clubid, "func": input_id, "weight": 1},
        {"element_data": ElementsData.ClubApplyPanel.club_list, "func": click_club, "weight": 2},
        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)

    # ClubApplyPanel.click_btn_close(bp)

    # ClubApplyPanel.click_btn_apply(bp)

    # ClubApplyPanel.click_btn_search(bp)
    #
    # ClubApplyPanel.click_btn_refresh(bp)
    #
    # ClubApplyPanel.click_btn_copy(bp)
    # ClubApplyPanel.click_btn_create(bp)

    # ClubApplyPanel.click_toggle(bp)

    # ClubApplyPanel.click_btn_fast(bp)
    # ClubApplyPanel.click_btn_report(bp)
    # ClubApplyPanel.input_id(bp)

    # ClubApplyPanel.click_club(bp)

    bp.connect_close()