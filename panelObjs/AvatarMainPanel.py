from common.basePage import BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData


class AvatarMainPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarMainPanel.AvatarMainPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.btn_close)

    def click_tab_avatar(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_avatar)

    def click_tab_rod(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_rod)

    def click_tab_bag(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_bag)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.tab_list, index=index)


    class panel_Avatar(BasePage):
        def switch_avatar_tab(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Avatar.tab_list, element_viewport=ElementsData.AvatarMainPanel.panel_Avatar.viewport_tab, viewport_direction="column",index=index)

        def click_btn_confirm(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.btn_confirm)

        def click_btn_changesex(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.btn_changesex)

        def click_btn_changecamera(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.btn_changecamera)

        def click_btn_hide(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.btn_hide)

        def click_toggle_own(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.toggle_own)

        def click_item(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Avatar.item_list, element_viewport=ElementsData.AvatarMainPanel.panel_Avatar.viewport, index=index)

        def switch_tab(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Avatar.tab_list, element_viewport=ElementsData.AvatarMainPanel.panel_Avatar.viewport_tab, index=index)

        def click_tags(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.tags)

        def click_btn_close_tags(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Avatar.btn_close_tags)

    class panel_Rod(BasePage):
        def switch_tab_rod(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Rod.tab_rod_list, element_viewport=ElementsData.AvatarMainPanel.panel_Rod.viewport_tab_rod, index=index)

        def switch_rod(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Rod.item_list, element_viewport=ElementsData.AvatarMainPanel.panel_Rod.viewport, index=index)

        def click_btn_bobox(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.btn_bobox)

        def click_btn_hide(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.btn_hide)

        def click_btn_changecamera(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.btn_changecamera)

        def switch_bobox(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Rod.bobox_on_list, index=index)

        def switch_tab_top(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.AvatarMainPanel.panel_Rod.tabs_top, index=index)

        def click_btn_form(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.btn_form)

        def click_tags(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.tags)

        def click_btn_close_tags(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.btn_close_tags)
        def click_btn_fast(self):
            self.click_element(element_data=ElementsData.AvatarMainPanel.panel_Rod.btn_fast)


    operation_pool = [
        {"element_data": ElementsData.AvatarMainPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.tab_list, "func": switch_tab, "weight": 2},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.btn_hide, "func": panel_Avatar.click_btn_hide, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.btn_changecamera, "func": panel_Avatar.click_btn_changecamera, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.btn_changesex, "func": panel_Avatar.click_btn_changesex, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.btn_confirm, "func": panel_Avatar.click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.toggle_own, "func": panel_Avatar.click_toggle_own, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.item_list, "func": panel_Avatar.click_item, "weight": 3},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.tab_list, "func": panel_Avatar.switch_avatar_tab, "weight": 2},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.tags, "func": panel_Avatar.click_tags, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Avatar.btn_close_tags, "func": panel_Avatar.click_btn_close_tags, "weight": 10},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.tab_rod_list, "func": panel_Rod.switch_tab_rod, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.item_list, "func": panel_Rod.switch_rod, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.btn_bobox, "func": panel_Rod.click_btn_bobox, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.bobox_on_list, "func": panel_Rod.switch_bobox, "weight": 2},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.btn_hide, "func": panel_Rod.click_btn_hide, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.btn_changecamera, "func": panel_Rod.click_btn_changecamera, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.tabs_top, "func": panel_Rod.switch_tab_top, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.btn_form, "func": panel_Rod.click_btn_form, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.tags, "func": panel_Rod.click_tags, "weight": 1},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.btn_close_tags, "func": panel_Rod.click_btn_close_tags, "weight": 10},
        {"element_data": ElementsData.AvatarMainPanel.panel_Rod.btn_fast, "func": panel_Rod.click_btn_fast, "weight": 1},
        ]

if __name__ == '__main__':
    bp = BasePage()
    # AvatarMainPanel.click_btn_close(bp)
    # AvatarMainPanel.switch_tab(bp)
    # AvatarMainPanel.panel_Avatar.click_btn_hide(bp)
    # AvatarMainPanel.panel_Avatar.click_btn_changecamera(bp)
    # AvatarMainPanel.panel_Avatar.click_btn_changesex(bp)
    # AvatarMainPanel.panel_Avatar.click_btn_confirm(bp)
    # AvatarMainPanel.panel_Avatar.click_toggle_own(bp)
    # AvatarMainPanel.panel_Avatar.click_item(bp, 7)
    # AvatarMainPanel.panel_Avatar.switch_avatar_tab(bp, 0)
    # AvatarMainPanel.panel_Rod.switch_tab_rod(bp)
    # AvatarMainPanel.panel_Rod.switch_rod(bp, 7)
    # AvatarMainPanel.panel_Rod.click_btn_bobox(bp)
    # AvatarMainPanel.panel_Rod.switch_bobox(bp)
    # AvatarMainPanel.panel_Rod.click_btn_hide(bp)
    # AvatarMainPanel.panel_Rod.click_btn_changecamera(bp)
    # AvatarMainPanel.panel_Rod.switch_tab_top(bp)
    # AvatarMainPanel.panel_Rod.click_btn_form(bp)
    # AvatarMainPanel.panel_Rod.click_tags(bp)
    # AvatarMainPanel.panel_Rod.click_btn_fast(bp)
    # AvatarMainPanel.panel_Avatar.click_btn_close_tags(bp)
    AvatarMainPanel.panel_Rod.click_btn_close_tags(bp)


    bp.connect_close()