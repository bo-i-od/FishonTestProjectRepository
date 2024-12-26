from common.basePage import BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData


class AvatarMainPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.AvatarMainPanel.AvatarMainPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.btn_close)

    def click_btn_changesex(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.btn_changesex)

    def click_btn_changecamera(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.btn_changecamera)

    def click_tab_avatar(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_avatar)

    def click_tab_rod(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_rod)

    def click_tab_bag(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_bag)

    def switch_avatar_tab(self, index):
        position_list = self.get_position_list(element_data=ElementsData.AvatarMainPanel.avatar_tab_list)
        self.click_position(position_list[index])

    def click_btn_confirm(self):
        position_list = self.get_position_list(element_data_list=[ElementsData.AvatarMainPanel.btn_confirm_avatar, ElementsData.AvatarMainPanel.tip_avatar])
        if position_list[0]:
            self.click_position(position_list[0][0])
            return
        self.click_position(position_list[1][0])

    def click_toggle_own(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.toggle_own)

    def switch_tab_rod(self, index):
        viewport = Viewport(self, element_viewport=ElementsData.AvatarMainPanel.viewport_tab_rod, element_item_list=ElementsData.AvatarMainPanel.tab_rod_list)
        viewport.move_until_appear(target_id=viewport.item_id_list[index])
        self.click_element(object_id=viewport.item_id_list[index])

    def switch_rod(self, index):
        viewport = Viewport(self, element_viewport=ElementsData.AvatarMainPanel.viewport_rod,
                            element_item_list=ElementsData.AvatarMainPanel.rod_list)
        viewport.move_until_appear(target_id=viewport.item_id_list[index])
        self.click_element(object_id=viewport.item_id_list[index])

    def click_btn_bobox(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.btn_bobox)

    def switch_bobox(self, index):
        position_list = self.get_position_list(element_data=ElementsData.AvatarMainPanel.bobox_on_list)
        print(position_list)
        self.click_position(position_list[index])

    def click_tab_skin(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_skin)

    def click_tab_attach(self):
        self.click_element(element_data=ElementsData.AvatarMainPanel.tab_attach)


if __name__ == '__main__':
    bp = BasePage()
    AvatarMainPanel.click_tab_skin(bp)

    bp.connect_close()