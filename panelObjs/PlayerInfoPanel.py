import random
import re

import tools
from common.basePage import BasePage
from common.slider import Slider
from common.viewport import Viewport
from configs.elementsData import ElementsData
from tools.commonTools import get_toggle_is_on_index, compare, merge_list


class PlayerInfoPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerInfoPanel.PlayerInfoPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_close)

    def click_btn_changecamera(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_changecamera)

    def click_btn_changerod(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_changerod)

    def switch_tab(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.tab_list, index=index)

    def click_btn_setting(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_setting)

    def click_btn_giftcode(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_giftcode)

    def click_btn_aquarium(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_aquarium)

    def set_giftcode(self, text=None):
        if text is None:
            text = tools.commonTools.generate_random_string(random.randint(0, 15))
        self.set_text(element_data=ElementsData.PlayerInfoPanel.giftcode_input, text=text)

    def get_giftcode(self):
        giftcode_input = self.get_text(element_data=ElementsData.PlayerInfoPanel.giftcode_input)
        return giftcode_input


    def click_btn_close_additional(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_close_additional)

    def click_btn_edit_player_info(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_edit_player_info)

    def click_btn_copy(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_copy)

    def click_btn_i_rating(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_i_rating)

    def click_btn_close_tips_rating(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_close_tips_rating)

    def click_btn_i_rod(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_i_rod)

    def click_btn_close_tips_rod(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_close_tips_rod)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_confirm)

    def click_btn_edit_achievement(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_edit_achievement)


    def get_player_info(self):
        lv_str = self.get_text(element_data=ElementsData.PlayerInfoPanel.lv)
        lv = int(lv_str)
        rating = int(self.get_text(element_data=ElementsData.PlayerInfoPanel.rating))
        player_info = {
        "player_name": self.get_text(element_data=ElementsData.PlayerInfoPanel.player_name),
        "head_img": self.get_icon(element_data=ElementsData.PlayerInfoPanel.head_img),
        "head_frame": self.get_icon(element_data=ElementsData.PlayerInfoPanel.head_frame),
        "lv": lv,
        "rating": rating,
        }
        return player_info


    def get_value_cost(self):
        value_cost = int(self.get_text(element_data=ElementsData.PlayerInfoPanel.value_cost))
        return value_cost

    def get_badge_show_id_list(self):
        badge_show_id_list = self.get_object_id_list(element_data=ElementsData.PlayerInfoPanel.badge_show_list)
        return badge_show_id_list

    def get_badge_select_id_list(self):
        badge_select_id_list = self.get_object_id_list(element_data=ElementsData.PlayerInfoPanel.badge_select_list)
        return badge_select_id_list

    def get_badge_show_viewport(self, badge_show_id_list):
        size_list = self.get_size_list(object_id=badge_show_id_list[0])
        badge_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfoPanel.viewport_badge_show,
                                  item_id_list=badge_show_id_list, viewport_direction="row", viewport_edge=[size_list[0][0] * 0.4, size_list[0][0] * 0.1])
        return badge_viewport

    def get_badge_select_viewport(self, badge_select_id_list):
        # size_list = self.get_size_list(object_id_list=badge_select_id_list)
        badge_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfoPanel.viewport_badge_select,
                                  item_id_list=badge_select_id_list, viewport_direction="row", viewport_edge=[0.01, 0.01])
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

    def click_badge_show(self, index=-1):
        size_list = self.get_size_list(element_data=ElementsData.PlayerInfoPanel.badge_show_list)
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.badge_show_list, element_viewport=ElementsData.PlayerInfoPanel.viewport_badge_show, viewport_direction="row", viewport_edge=[size_list[0][0] * 0.4, size_list[0][0] * 0.1], index=index)

    def get_selected_badge_show_index(self):
        toggle_is_on_list = self.get_toggle_is_on_list(element_data=ElementsData.PlayerInfoPanel.badge_show_list)
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
        icon_list = merge_list(icon_list)
        return icon_list

    def select_badge_select(self, badge_select_id_list, index):
        badge_select_viewport = PlayerInfoPanel.get_badge_select_viewport(self, badge_select_id_list)
        badge_select_viewport.move_until_appear(target_id=badge_select_id_list[index])
        self.click_element(object_id=badge_select_id_list[index], focus=[0, 0.5])

    def click_badge_select(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.badge_select_list, element_viewport=ElementsData.PlayerInfoPanel.viewport_badge_select, viewport_direction="row", viewport_edge=[0.01, 0.01], index=index)

    def click_rod(self, index=-1):
        size_list = self.get_size_list(element_data=ElementsData.PlayerInfoPanel.rod_list)

        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.rod_list, element_viewport=ElementsData.PlayerInfoPanel.viewport_rod, viewport_direction="row", viewport_edge=[0.01, -size_list[0][0]], index=index)

    def switch_tab_setting(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.tab_list_setting, index=index)

    def get_slider_music(self):
        return self.get_slider_value(element_data=ElementsData.PlayerInfoPanel.options_music)

    def set_slider_music(self, target_val=None):
        if target_val is None:
            target = random.random()
        if target_val > 0.99:
            target_val = 0.99
        w = self.get_size(element_data=ElementsData.PlayerInfoPanel.options_music)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerInfoPanel.options_music)
        x_start = x_center - 0.5 * w
        x_target = x_start + target_val * w
        self.click_position([x_target, y_center])
        self.sleep(1)
        slider_music = PlayerInfoPanel.get_slider_music(self)
        delta = abs(target_val - slider_music)
        # if delta > 0.1:
        #     raise DifferError


    def swipe_slider_music(self, value_start=None, value_end=None):
        slider = Slider(self, element_slider=ElementsData.PlayerInfoPanel.options_music)
        self.swipe_slider_base(slider=slider, value_start=value_start, value_end=value_end)

    def swipe_slider_sound(self, value_start=None, value_end=None):
        slider = Slider(self, element_slider=ElementsData.PlayerInfoPanel.options_sound)
        self.swipe_slider_base(slider=slider, value_start=value_start, value_end=value_end)

    def get_slider_sound(self):
        return self.get_slider_value(element_data=ElementsData.PlayerInfoPanel.options_sound)

    def set_slider_sound(self, target=None):
        if target is None:
            target = random.random()
        if target > 0.95:
            target = 0.95
        if target < 0.05:
            target = 0.05
        w = self.get_size(element_data=ElementsData.PlayerInfoPanel.options_sound)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerInfoPanel.options_sound)
        x_start = x_center - 0.5 * w
        x_target = x_start + target * w
        self.click_position([x_target, y_center])
        self.sleep(1)
        slider_sound = PlayerInfoPanel.get_slider_sound(self)
        delta = abs(target - slider_sound)
        # if delta > 0.1:
        #     raise DifferError


    def click_options(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.options_list, index=index)

    def get_options_graphics_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.options_graphics_list)
        return position_list

    def set_options_graphics(self, index):
        position_list = PlayerInfoPanel.get_options_graphics_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfoPanel.options_graphics_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_frame_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.options_frame_list)
        return position_list

    def set_options_frame(self, index):
        position_list = PlayerInfoPanel.get_options_frame_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfoPanel.options_frame_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_joystick_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.options_joystick_list)
        return position_list

    def set_options_joystick(self, index):
        position_list = PlayerInfoPanel.get_options_joystick_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfoPanel.options_joystick_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_vibration_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.options_vibration_list)
        return position_list

    def set_options_vibration(self, index):
        position_list = PlayerInfoPanel.get_options_vibration_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfoPanel.options_vibration_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_gyro_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.options_gyro_list)
        return position_list

    def set_options_gyro(self, index):
        position_list = PlayerInfoPanel.get_options_gyro_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfoPanel.options_gyro_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_invite_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.options_invite_list)
        return position_list

    def set_options_invite(self, index):
        position_list = PlayerInfoPanel.get_options_invite_position_list(self)
        if not position_list:
            return
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerInfoPanel.options_invite_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def click_btn_copy_id(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerInfoPanel.btn_copy_id)
        if not position_list:
            return
        self.click_position(position_list[0])

    def get_id(self):
        self.get_text(element_data=ElementsData.PlayerInfoPanel.options_id)

    def click_tab_name(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.tab_name)

    def click_tab_avatar(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.tab_avatar)

    def click_tab_head_frame(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.tab_head_frame)

    def click_tab_setting(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.tab_setting)

    def set_player_name(self, name=None):
        if name is None:
            name = tools.commonTools.generate_random_string(random.randint(0, 30))
        self.set_text(element_data=ElementsData.PlayerInfoPanel.Input_PlayerName, text=name)

    def click_btn_save_head_frame(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_save_head_frame)

    def click_btn_save_head(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_save_head)

    def click_btn_save_profile(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_save_profile)

    def click_btn_save_pay(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_save_profile)

    def is_btn_save_pay_abled(self):
        return self.exist(element_data=ElementsData.PlayerInfoPanel.btn_save_pay, offspring_path="btn_disabled")

    def get_avatar_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerInfoPanel.avatar_list)

    def get_head_frame_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerInfoPanel.head_frame_list)

    def get_avatar_viewport(self, avatar_id_list):
        size_list = self.get_size_list(object_id=avatar_id_list[0])
        h = 0
        if size_list:
            h = size_list[0][1]
        avatar_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfoPanel.viewport_avatar, item_id_list=avatar_id_list, viewport_direction="column", viewport_edge=[0, 0.5 * h])
        return avatar_viewport

    def get_head_framer_viewport(self, head_frame_id_list):
        size_list = self.get_size_list(object_id=head_frame_id_list[0])
        h = 0
        if size_list:
            h = size_list[0][1]
        head_frame_viewport = Viewport(self, element_viewport=ElementsData.PlayerInfoPanel.viewport_head_frame, item_id_list=head_frame_id_list, viewport_direction="column", viewport_edge=[0, 0.5 * h])
        return head_frame_viewport

    def select_avatar(self, avatar_id_list, index):
        avatar_viewport = PlayerInfoPanel.get_avatar_viewport(self, avatar_id_list)
        avatar_viewport.move_until_appear(target_id=avatar_id_list[index])
        self.click_element(object_id=avatar_id_list[index], focus=[0, 0.5])
        selected_avatar_index = PlayerInfoPanel.get_selected_icon_index(self, avatar_id_list)
        compare(index, selected_avatar_index)

    def click_avatar(self, index=-1):
        h = self.get_size_list(element_data=ElementsData.PlayerInfoPanel.avatar_list)[0][0]
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.avatar_list, element_viewport=ElementsData.PlayerInfoPanel.viewport_avatar, viewport_direction="column", viewport_edge=[0, 0.5 * h], index=index)

    def select_head_frame(self, head_frame_id_list, index):
        head_framer_viewport = PlayerInfoPanel.get_head_framer_viewport(self, head_frame_id_list)
        head_framer_viewport.move_until_appear(target_id=head_frame_id_list[index])
        self.click_element(object_id=head_frame_id_list[index], focus=[0, 0.5])

    def click_head_frame(self, index=-1):
        h = self.get_size_list(element_data=ElementsData.PlayerInfoPanel.head_frame_list)[0][0]
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.head_frame_list, element_viewport=ElementsData.PlayerInfoPanel.viewport_head_frame, viewport_direction="column", viewport_edge=[0, 0.5 * h], index=index)

    def get_selected_icon_index(self, icon_id_list):
        select_id_list = self.get_offspring_id_list(object_id_list=icon_id_list, offspring_path="select")
        select_id_list = merge_list(select_id_list)
        icon_id = self.get_parent_id(object_id=select_id_list[0])
        index = icon_id_list.index(icon_id)
        return index

    def get_locked_icon_index_list(self, icon_id_list):
        locked_id_list = self.get_offspring_id_list(object_id_list=icon_id_list, offspring_path="locked")
        locked_id_list = merge_list(locked_id_list)
        parent_id_list = self.get_parent_id_list(object_id_list=locked_id_list)

        index_list = []
        for parent_id in parent_id_list:
            index = icon_id_list.index(parent_id[0])
            index_list.append(index)
        return index_list

    def get_avatar(self, avatar_id):
        head_img_id = self.get_offspring_id(object_id=avatar_id, offspring_path="head>head_mask>head_img")
        return self.get_icon(object_id=head_img_id)

    def get_head_frame(self, head_frame_id):
        return self.get_icon(object_id=head_frame_id)

    def click_btn_appicp(self):
        self.click_element(element_data=ElementsData.PlayerInfoPanel.btn_appicp)

    def click_btn(self, index=-1):
        self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.btns, index=index)

    class Panel_PlayerCard_new(BasePage):
        def click_btn_close(self):
            self.click_element(element_data=ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_close)

        def click_btn_changecamera(self):
            self.click_element(element_data=ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_changecamera)

        def click_btn_confirm(self):
            self.click_element(element_data=ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_confirm)

        def switch_tab(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.tab_list, index=index)

        def click_item(self, index=-1):
            self.click_object_of_plural_objects(element_data=ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.item_list, element_viewport=ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.viewport, viewport_direction="column", index=index)


    operation_pool = [
        {"element_data": ElementsData.PlayerInfoPanel.avatar_list, "func": click_avatar, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.badge_select_list, "func": click_badge_select, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.badge_show_list, "func": click_badge_show, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btns, "func": click_btn, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_appicp, "func": click_btn_appicp, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_aquarium, "func": click_btn_aquarium, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_changecamera, "func": click_btn_changecamera, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_changerod, "func": click_btn_changerod, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_close, "func": click_btn_close, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_close_additional, "func": click_btn_close_additional, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_confirm, "func": click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_copy, "func": click_btn_copy, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_copy_id, "func": click_btn_copy_id, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_edit_achievement, "func": click_btn_edit_achievement, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_edit_player_info, "func": click_btn_edit_player_info, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_giftcode, "func": click_btn_giftcode, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_i_rating, "func": click_btn_i_rating, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_i_rod, "func": click_btn_i_rod, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_close_tips_rating, "func": click_btn_close_tips_rating, "weight": 10},
        {"element_data": ElementsData.PlayerInfoPanel.btn_close_tips_rod, "func": click_btn_close_tips_rod, "weight": 10},

        {"element_data": ElementsData.PlayerInfoPanel.btn_save_profile, "func": click_btn_save_profile, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_save_head_frame, "func": click_btn_save_head_frame, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.btn_setting, "func": click_btn_setting, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.head_frame_list, "func": click_head_frame, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.options_list, "func": click_options, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.rod_list, "func": click_rod, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.giftcode_input, "func": set_giftcode, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.Input_PlayerName, "func": set_player_name, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.options_music, "func": swipe_slider_music, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.options_sound, "func": swipe_slider_sound, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.tab_list, "func": switch_tab, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.tab_list_setting, "func": switch_tab_setting, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_changecamera, "func": Panel_PlayerCard_new.click_btn_changecamera, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_close, "func": Panel_PlayerCard_new.click_btn_close, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_confirm, "func": Panel_PlayerCard_new.click_btn_confirm, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.item_list, "func": Panel_PlayerCard_new.click_item, "weight": 1},
        {"element_data": ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.tab_list, "func": Panel_PlayerCard_new.switch_tab, "weight": 1},
    ]
if __name__ == "__main__":
    bp = BasePage()
    # PlayerInfoPanel.click_avatar(bp, 0)
    # PlayerInfoPanel.click_badge_select(bp)
    # PlayerInfoPanel.click_badge_show(bp)
    # PlayerInfoPanel.click_btn(bp)
    # PlayerInfoPanel.click_btn_appicp(bp)
    # PlayerInfoPanel.click_btn_aquarium(bp)
    # PlayerInfoPanel.click_btn_changecamera(bp)
    # PlayerInfoPanel.click_btn_changerod(bp)
    # PlayerInfoPanel.click_btn_close(bp)
    # PlayerInfoPanel.click_btn_close_additional(bp)
    # PlayerInfoPanel.click_btn_confirm(bp)
    # PlayerInfoPanel.click_btn_copy(bp)
    # PlayerInfoPanel.click_btn_copy_id(bp)
    # PlayerInfoPanel.click_btn_edit_achievement(bp)
    # PlayerInfoPanel.click_btn_edit_player_info(bp)
    # PlayerInfoPanel.click_btn_giftcode(bp)
    # PlayerInfoPanel.click_btn_i_rating(bp)
    # PlayerInfoPanel.click_btn_i_rod(bp)
    # PlayerInfoPanel.click_btn_save_profile(bp)
    # PlayerInfoPanel.click_btn_save_head_frame(bp)
    # PlayerInfoPanel.click_btn_setting(bp)
    # PlayerInfoPanel.click_head_frame(bp)
    # PlayerInfoPanel.click_options(bp)
    # PlayerInfoPanel.click_rod(bp)
    # PlayerInfoPanel.set_giftcode(bp)
    # PlayerInfoPanel.set_player_name(bp)
    # PlayerInfoPanel.swipe_slider_music(bp)
    # PlayerInfoPanel.swipe_slider_sound(bp)
    # PlayerInfoPanel.switch_tab(bp)
    # PlayerInfoPanel.switch_tab_setting(bp)
    # PlayerInfoPanel.Panel_PlayerCard_new.click_btn_changecamera(bp)
    # PlayerInfoPanel.Panel_PlayerCard_new.click_btn_close(bp)
    # PlayerInfoPanel.Panel_PlayerCard_new.click_btn_confirm(bp)
    PlayerInfoPanel.Panel_PlayerCard_new.click_item(bp)
    # PlayerInfoPanel.Panel_PlayerCard_new.switch_tab(bp)
    bp.connect_close()
