from common.basePage import BasePage
from configs.elementsData import ElementsData


class ClubPanel(BasePage):
    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ClubPanel.btn_close)

    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ClubPanel.ClubPanel)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.tab_list, index=index)

    class panel_clubhome(BasePage):
        def click_btn_chat(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.btn_chat)

        def click_task_mini(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.task_mini)

        def click_toggle(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.toggle)

        def click_btn_goweek(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.btn_goweek)

        def click_btn_copy(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.btn_copy)

        def click_red_envelope(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubhome.red_envelope_list, element_viewport=ElementsData.ClubPanel.panel_clubhome.viewport, viewport_direction="column", index=index)

        def click_btn(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubhome.btn_list, element_viewport=ElementsData.ClubPanel.panel_clubhome.viewport, viewport_direction="column", index=index)

        def click_btn_flashcard(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.btn_flashcard)

        def click_btn_dragonboat(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.btn_dragonboat)

        def click_btn_edit(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubhome.btn_edit)

    class panel_clubmember(BasePage):
        def click_btn_leave(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubmember.btn_leave)

        def click_btn_list(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubmember.btn_list)

        def click_btn_playercard(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubmember.btn_playercard_list, element_viewport=ElementsData.ClubPanel.panel_clubmember.viewport,viewport_direction="column", index=index)

        def click_btn_edit(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubmember.btn_edit_list, element_viewport=ElementsData.ClubPanel.panel_clubmember.viewport,viewport_direction="column",  index=index)

        def click_btn_close_edit(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubmember.btn_close_edit)

        def click_btn(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubmember.btns, index=index)

    class panel_clubweek(BasePage):
        def click_reward(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubweek.reward_list, index=index)

        def click_top(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_clubweek.top_list, index=index)

        def click_btn_i(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubweek.btn_i)

        def click_btn_close_tips(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_clubweek.btn_close_tips)

    class Panel_Flashcard(BasePage):
        def click_btn_close(self):
            self.click_element(element_data=ElementsData.ClubPanel.Panel_Flashcard.btn_close)

        def click_btn_save(self):
            self.click_element(element_data=ElementsData.ClubPanel.Panel_Flashcard.btn_save)

        def click_btn_cancel(self):
            self.click_element(element_data=ElementsData.ClubPanel.Panel_Flashcard.btn_cancel)

        def switch_tab(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.Panel_Flashcard.tab_list, element_viewport=ElementsData.ClubPanel.Panel_Flashcard.viewport_tab, viewport_direction="column", index=index)

        def click_flashcard(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.Panel_Flashcard.flashcard_list, element_viewport=ElementsData.ClubPanel.Panel_Flashcard.viewport_flashcard, viewport_direction="column",index=index)

    class panel_popups_confirm(BasePage):
        def click_btn_close(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_popups_confirm.btn_close)

        def click_btn_exchange(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_popups_confirm.btn_exchange)

    class panel_popup_applylist(BasePage):
        def click_btn_close(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_popup_applylist.btn_close)

        def click_btn_leave(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_popup_applylist.btn_leave)

        def click_btn_list(self):
            self.click_element(element_data=ElementsData.ClubPanel.panel_popup_applylist.btn_list)

        def click_btn_cancel(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_popup_applylist.btn_cancel_list, element_viewport=ElementsData.ClubPanel.panel_popup_applylist.viewport, viewport_direction="column", index=index)

        def click_btn_confirm(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.ClubPanel.panel_popup_applylist.btn_confirm_list, element_viewport=ElementsData.ClubPanel.panel_popup_applylist.viewport, viewport_direction="column", index=index)


    operation_pool = [
        {"element_data": ElementsData.ClubPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubPanel.tab_list, "func": switch_tab, "weight": 2},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_chat, "func": panel_clubhome.click_btn_chat, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.task_mini, "func": panel_clubhome.click_task_mini, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.toggle, "func": panel_clubhome.click_toggle, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_goweek, "func": panel_clubhome.click_btn_goweek, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_copy, "func": panel_clubhome.click_btn_copy, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.red_envelope_list, "func": panel_clubhome.click_red_envelope, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_list, "func": panel_clubhome.click_btn, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_flashcard, "func": panel_clubhome.click_btn_flashcard, "weight": 2},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_dragonboat, "func": panel_clubhome.click_btn_dragonboat, "weight": 2},
        {"element_data": ElementsData.ClubPanel.panel_clubhome.btn_edit, "func": panel_clubhome.click_btn_edit, "weight": 2},
        {"element_data": ElementsData.ClubPanel.panel_clubmember.btn_close_edit, "func": panel_clubmember.click_btn_close_edit, "weight": 10},
        {"element_data": ElementsData.ClubPanel.panel_clubmember.btn_leave, "func": panel_clubmember.click_btn_leave, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubmember.btn_list, "func": panel_clubmember.click_btn_list, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubmember.btn_playercard_list, "func": panel_clubmember.click_btn_playercard, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubmember.btn_edit_list, "func": panel_clubmember.click_btn_edit, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubmember.btns, "func": panel_clubmember.click_btn, "weight": 10},
        {"element_data": ElementsData.ClubPanel.panel_clubweek.reward_list, "func": panel_clubweek.click_reward, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubweek.top_list, "func": panel_clubweek.click_top, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubweek.btn_i, "func": panel_clubweek.click_btn_i, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_clubweek.btn_close_tips, "func": panel_clubweek.click_btn_close_tips, "weight": 1},
        {"element_data": ElementsData.ClubPanel.Panel_Flashcard.btn_close, "func": Panel_Flashcard.click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubPanel.Panel_Flashcard.btn_save, "func": Panel_Flashcard.click_btn_save, "weight": 1},
        {"element_data": ElementsData.ClubPanel.Panel_Flashcard.btn_cancel, "func": Panel_Flashcard.click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.ClubPanel.Panel_Flashcard.tab_list, "func": Panel_Flashcard.switch_tab, "weight": 1},
        {"element_data": ElementsData.ClubPanel.Panel_Flashcard.flashcard_list, "func": Panel_Flashcard.click_flashcard, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popups_confirm.btn_close, "func": panel_popups_confirm.click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popups_confirm.btn_exchange, "func": panel_popups_confirm.click_btn_exchange, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popup_applylist.btn_close, "func": panel_popup_applylist.click_btn_close, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popup_applylist.btn_leave, "func": panel_popup_applylist.click_btn_leave, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popup_applylist.btn_list, "func": panel_popup_applylist.click_btn_list, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popup_applylist.btn_cancel_list, "func": panel_popup_applylist.click_btn_cancel, "weight": 1},
        {"element_data": ElementsData.ClubPanel.panel_popup_applylist.btn_confirm_list, "func": panel_popup_applylist.click_btn_confirm, "weight": 1},

        ]


if __name__ == "__main__":
    bp = BasePage("127.0.0.1:21573", is_mobile_device=False)

    # 测试
    # ClubPanel.click_btn_close(bp)
    # ClubPanel.switch_tab(bp)
    # ClubPanel.Panel_Flashcard.click_btn_close(bp)
    # ClubPanel.Panel_Flashcard.click_btn_save(bp)
    # ClubPanel.Panel_Flashcard.click_flashcard(bp)
    # ClubPanel.Panel_Flashcard.switch_tab(bp)
    # ClubPanel.panel_clubhome.click_btn(bp)
    # ClubPanel.panel_clubhome.click_btn_chat(bp)
    # ClubPanel.panel_clubhome.click_btn_copy(bp)
    # ClubPanel.panel_clubhome.click_btn_dragonboat(bp)
    # ClubPanel.panel_clubhome.click_btn_edit(bp)
    # ClubPanel.panel_clubhome.click_btn_flashcard(bp)
    # ClubPanel.panel_clubhome.click_btn_goweek(bp)
    # ClubPanel.panel_clubhome.click_red_envelope(bp)
    # ClubPanel.panel_clubhome.click_task_mini(bp)
    # ClubPanel.panel_clubhome.click_toggle(bp)
    # ClubPanel.panel_clubmember.click_btn(bp)
    # ClubPanel.panel_clubmember.click_btn_edit(bp)
    # ClubPanel.panel_clubmember.click_btn_close_edit(bp)
    # ClubPanel.panel_clubmember.click_btn_leave(bp)
    # ClubPanel.panel_clubmember.click_btn_list(bp)
    # ClubPanel.panel_clubmember.click_btn_playercard(bp)
    ClubPanel.panel_clubweek.click_btn_close_tips(bp)
    # ClubPanel.panel_clubweek.click_reward(bp)
    # ClubPanel.panel_clubweek.click_top(bp)
    # ClubPanel.panel_popup_applylist.click_btn_cancel(bp)
    # ClubPanel.panel_popup_applylist.click_btn_close(bp)
    # ClubPanel.panel_popup_applylist.click_btn_confirm(bp)
    # ClubPanel.panel_popup_applylist.click_btn_leave(bp)
    # ClubPanel.panel_popup_applylist.click_btn_list(bp)
    # ClubPanel.panel_popups_confirm.click_btn_close(bp)
    # ClubPanel.panel_popups_confirm.click_btn_exchange(bp)

    bp.connect_close()


