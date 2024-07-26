import re

from common.basePage import BasePage
from common.viewport import Viewport
from configs.elementsData import ElementsData
from tools.commonTools import get_toggle_is_on_index, compare


class PlayerInfoPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerInfo.PlayerInfoPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_close)

    def click_btn_setting(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_setting)

    def click_btn_logout(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_logout)

    def click_btn_giftcode(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_giftcode)

    def set_giftcode(self, text):
        self.set_text(element_data=ElementsData.PlayerInfo.giftcode_input, text=text)

    def get_giftcode(self):
        giftcode_input = self.get_text(element_data=ElementsData.PlayerInfo.giftcode_input)
        return giftcode_input


    def click_btn_close_additional(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_close_additional)

    def click_btn_edit_player_info(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_edit_player_info)

    def click_btn_copy(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_copy)

    def click_btn_i_rating(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_i_rating)

    def click_btn_i_rod(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_i_rod)

    def click_btn_tag(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_tag)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_confirm)

    def click_btn_edit_achievement(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_edit_achievement)

    def get_player_info(self):
        lv_str = self.get_text(element_data=ElementsData.PlayerInfo.lv)
        lv = int(re.search(r'(\d+)级', lv_str).group(1))
        rating = int(self.get_text(element_data=ElementsData.PlayerInfo.rating))
        player_info = {
        "player_name": self.get_text(element_data=ElementsData.PlayerInfo.player_name),
        "head_img": self.get_icon(element_data=ElementsData.PlayerInfo.head_img),
        "lv": lv,
        "rating": rating,
        }
        return player_info

    def get_value_cost(self):
        value_cost = int(self.get_text(element_data=ElementsData.PlayerInfo.value_cost))
        return value_cost

    def get_badge_show_id_list(self):
        badge_show_id_list = self.get_object_id_list(element_data=ElementsData.PlayerInfo.badge_show_list)
        return badge_show_id_list

    def get_badge_select_id_list(self):
        badge_select_id_list = self.get_object_id_list(element_data=ElementsData.PlayerInfo.badge_select_list)
        return badge_select_id_list

    def get_badge_show_viewport(self, badge_show_id_list):
        size_list = self.get_size_list(object_id_list=badge_show_id_list)
        badge_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfo.viewport_badge_show,
                                  item_id_list=badge_show_id_list, viewport_direction="row",viewport_edge=[size_list[0][0] * 0.4, size_list[0][0] * 0.1])
        return badge_viewport

    def get_badge_select_viewport(self, badge_select_id_list):
        # size_list = self.get_size_list(object_id_list=badge_select_id_list)
        badge_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfo.viewport_badge_select,
                                  item_id_list=badge_select_id_list, viewport_direction="row",viewport_edge=[0.01, 0.01])
        return badge_viewport

    def get_badge_show_list(self, badge_show_id_list):
        badge_show_list = []
        cur = 0
        while cur < len(badge_show_id_list):
            badge_img_list = self.get_icon_list(object_id=badge_show_id_list[cur], offspring_path="badge_img")
            if badge_img_list:
                badge_show_list.append(badge_img_list[0])
                cur += 1
                continue
            badge_show_list.append("")
            cur += 1

        return badge_show_list

    def select_badge_show(self, badge_show_id_list, index):
        self.click_element(object_id=badge_show_id_list[index])

    def get_selected_badge_show_index(self):
        toggle_is_on_list = self.get_toggle_is_on_list(element_data=ElementsData.PlayerInfo.badge_show_list)
        index = get_toggle_is_on_index(toggle_is_on_list=toggle_is_on_list)
        return index

    def get_badge_status(self, badge_select_id_list):
        locked_list = []
        unlocked_list = []
        equipped_list = []
        cur = 0
        while cur < len(badge_select_id_list):
            lock_id_list = self.get_offspring_id_list(object_id=badge_select_id_list[cur], offspring_path="badge_lock")
            if lock_id_list:
                locked_list.append(cur)
                cur += 1
                continue
            badge_equipped_id_list = self.get_offspring_id_list(object_id=badge_select_id_list[cur],
                                                              offspring_path="badge_equipped")
            if badge_equipped_id_list:
                equipped_list.append(cur)
            unlocked_list.append(cur)
            cur += 1
        return locked_list, unlocked_list, equipped_list

    def get_badge_select_list(self, badge_select_id_list):
        icon_list = self.get_icon_list(object_id_list=badge_select_id_list, offspring_path="icon")
        return icon_list

    def select_badge(self, badge_select_id_list, index):
        badge_select_viewport = PlayerInfoPanel.get_badge_select_viewport(self, badge_select_id_list)
        badge_select_viewport.move_until_appear(target_id=badge_select_id_list[index])
        self.click_element(object_id=badge_select_id_list[index], focus=[0, 0.5])

    def get_slider_music(self):
        return self.get_slider_value(element_data=ElementsData.PlayerInfo.options_music)

    def set_slider_music(self, target_val):
        if target_val > 0.99:
            target_val = 0.99
        w = self.get_size(element_data=ElementsData.PlayerInfo.options_music)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerInfo.options_music)
        x_start = x_center - 0.5 * w
        x_target = x_start + target_val * w
        self.click_position([x_target, y_center])
        self.sleep(1)
        slider_music = PlayerInfoPanel.get_slider_music(self)
        delta = abs(target_val - slider_music)
        # if delta > 0.1:
        #     raise DifferError
        print(delta)

    def get_slider_sound(self):
        return self.get_slider_value(element_data=ElementsData.PlayerInfo.options_sound)

    def set_slider_sound(self, target):
        if target > 0.95:
            target = 0.95
        if target < 0.05:
            target = 0.05
        w = self.get_size(element_data=ElementsData.PlayerInfo.options_sound)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerInfo.options_sound)
        x_start = x_center - 0.5 * w
        x_target = x_start + target * w
        self.click_position([x_target, y_center])
        self.sleep(1)
        slider_sound = PlayerInfoPanel.get_slider_sound(self)
        delta = abs(target - slider_sound)
        # if delta > 0.1:
        #     raise DifferError
        print(delta)

    def get_options_graphics_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfo.options_graphics_list)
        return position_list

    def set_options_graphics(self, index):
        position_list = PlayerInfoPanel.get_options_graphics_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfo.options_graphics_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_frame_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfo.options_frame_list)
        return position_list

    def set_options_frame(self, index):
        position_list = PlayerInfoPanel.get_options_frame_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfo.options_frame_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_joystick_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfo.options_joystick_list)
        return position_list

    def set_options_joystick(self, index):
        position_list = PlayerInfoPanel.get_options_joystick_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfo.options_joystick_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_vibration_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfo.options_vibration_list)
        return position_list

    def set_options_vibration(self, index):
        position_list = PlayerInfoPanel.get_options_vibration_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfo.options_vibration_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_gyro_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfo.options_gyro_list)
        return position_list

    def set_options_gyro(self, index):
        position_list = PlayerInfoPanel.get_options_gyro_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfo.options_gyro_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_invite_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfo.options_invite_list)
        return position_list

    def set_options_invite(self, index):
        position_list = PlayerInfoPanel.get_options_invite_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfo.options_invite_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def click_tab_name(self):
        self.click_element(element_data=ElementsData.PlayerInfo.tab_name)

    def click_tab_avatar(self):
        self.click_element(element_data=ElementsData.PlayerInfo.tab_avatar)

    def click_tab_setting(self):
        self.click_element(element_data=ElementsData.PlayerInfo.tab_setting)

    def set_player_name(self, name):
        self.set_text(element_data=ElementsData.PlayerInfo.Input_PlayerName, text=name)

    def click_btn_save(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_save_profile)

    def click_btn_save_pay(self):
        self.click_element(element_data=ElementsData.PlayerInfo.btn_save_pay)

    def is_btn_save_pay_abled(self):
        return self.exist(element_data=ElementsData.PlayerInfo.btn_save_pay, offspring_path="btn_disabled")

    def get_avatar_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerInfo.avatar_list)

    def get_avatar_viewport(self, avatar_id_list):
        size_list = self.get_size_list(object_id_list=avatar_id_list)
        h = 0
        if size_list:
            h = size_list[0][1]
        avatar_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfo.viewport_avatar, item_id_list=avatar_id_list,viewport_direction="column", viewport_edge=[0, 0.5 * h])
        return avatar_viewport

    def select_avatar(self, avatar_id_list, index):
        avatar_viewport = PlayerInfoPanel.get_avatar_viewport(self, avatar_id_list)
        avatar_viewport.move_until_appear(target_id=avatar_id_list[index])
        self.click_element(object_id=avatar_id_list[index], focus=[0, 0.5])
        selected_avatar_index = PlayerInfoPanel.get_selected_icon_index(self, avatar_id_list)
        compare(index, selected_avatar_index)

    def get_selected_icon_index(self, icon_id_list):
        select_id_list = self.get_offspring_id_list(object_id_list=icon_id_list, offspring_path="select")
        icon_id = self.get_parent_id(object_id=select_id_list[0])
        index = icon_id_list.index(icon_id)
        return index

    def get_avatar(self, avatar_id):
        head_img_id = self.get_offspring_id(object_id=avatar_id, offspring_path="head>head_mask>head_img")
        return self.get_icon(object_id=head_img_id)



if __name__ == '__main__':
    bp = BasePage("ABSHUT1818002287")
    badge_show_id_list = PlayerInfoPanel.get_badge_show_id_list(bp)
    a = PlayerInfoPanel.get_badge_show_viewport(bp, badge_show_id_list=badge_show_id_list)
    a.move_until_appear(target_id=a.item_id_list[0])
    # print(a)
