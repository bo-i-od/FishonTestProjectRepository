from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport
from panelObjs.homePanel import HomePanel

class PlayerSettingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.PlayerSettingPanel.PlayerSettingPanel)

    def is_btn_giftcode_active(self):
        return self.exist(element_data=ElementsData.PlayerSettingPanel.btn_giftcode)

    def is_Panel_Popups_Edit_active(self):
        return self.exist(element_data=ElementsData.PlayerSettingPanel.Panel_Popups_Edit)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_close)

    def click_tab_player(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_player)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_player):
            raise FindNoElementError

    def click_tab_settings(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_setting)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_setting):
            raise FindNoElementError

    def click_tab_language(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_language)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_language):
            raise FindNoElementError


    def get_exp_val(self):
        # 得到等级
        lv_str = self.get_text(element_data=ElementsData.PlayerSettingPanel.player_lv)
        lv = int(lv_str)
        # 得到进度条占总进度的百分比
        exp_progress = self.get_slider_value(element_data=ElementsData.PlayerSettingPanel.exp)
        # 得到当前等级经验上限
        exp_limit, exp_limit_all = self.excelTools.get_exp_limit(lv)
        # 经验 = 经验上限 * 进度条占总进度的百分比 + 以前等级的经验总量
        exp = int(exp_progress * exp_limit + 0.5) + exp_limit_all  # 求出的数是float需要四舍五入一下
        # 通过指令读取当前经验总量
        exp_db = self.get_item_count(item_tpid="100200")
        compare(exp, exp_db)
        return exp

    def get_player_data(self):
        name = self.get_text(element_data=ElementsData.PlayerSettingPanel.player_name)
        head = self.get_icon(element_data=ElementsData.PlayerSettingPanel.head)
        flag = self.get_icon(element_data=ElementsData.PlayerSettingPanel.flag)
        lv_str = self.get_text(element_data=ElementsData.PlayerSettingPanel.player_lv)
        lv = int(lv_str)
        return name, head, flag, lv

    def click_name(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.player_name)
        self.sleep(1)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_name):
            raise FindNoElementError

    def click_head(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.head)
        self.sleep(1)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_avatar):
            raise FindNoElementError

    def click_flag(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.flag)
        self.sleep(1)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_banner):
            raise FindNoElementError

    def click_edit_info(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_edit_info)
        self.sleep(1)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_avatar):
            raise FindNoElementError

    def click_edit_badge(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_edit_badge)
        self.sleep(1)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.panel_badge):
            raise FindNoElementError

    def close_edit_profile(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_close_additional)
        self.sleep(1)
        if self.exist(element_data=ElementsData.PlayerSettingPanel.Panel_Popups_Edit):
            raise FindElementError

    def click_btn_giftcode(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_giftcode)

    def set_giftcode(self, text):
        self.set_text(element_data=ElementsData.PlayerSettingPanel.giftcode_input, text=text)

    def get_giftcode(self):
        giftcode_input = self.get_text(element_data=ElementsData.PlayerSettingPanel.giftcode_input)
        return giftcode_input

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_confirm)

    def click_btn_close_giftcode(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_close_additional)

    def click_badge_i(self):
        if self.exist(element_data=ElementsData.PlayerSettingPanel.Panel_Tip_Rules):
            self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_i_badge)
            if self.exist(element_data=ElementsData.PlayerSettingPanel.Panel_Tip_Rules):
                raise FindElementError
            return
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_i_badge)
        if not self.exist(element_data=ElementsData.PlayerSettingPanel.Panel_Tip_Rules):
            raise FindNoElementError

    def get_slider_music(self):
        return self.get_slider_value(element_data=ElementsData.PlayerSettingPanel.options_music)

    def set_slider_music(self, target_val):
        if target_val > 0.99:
            target_val = 0.99
        w = self.get_size(element_data=ElementsData.PlayerSettingPanel.options_music_bg)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerSettingPanel.options_music_bg)
        x_start = x_center - 0.5 * w
        x_target = x_start + target_val * w
        self.click_position([x_target, y_center])
        self.sleep(1)
        slider_music = PlayerSettingPanel.get_slider_music(self)
        delta = abs(target_val - slider_music)
        # if delta > 0.1:
        #     raise DifferError
        print(delta)

    def get_slider_sound(self):
        return self.get_slider_value(element_data=ElementsData.PlayerSettingPanel.options_sound)

    def set_slider_sound(self, target):
        if target > 0.95:
            target = 0.95
        if target < 0.05:
            target = 0.05
        w = self.get_size(element_data=ElementsData.PlayerSettingPanel.options_sound_bg)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerSettingPanel.options_sound_bg)
        x_start = x_center - 0.5 * w
        x_target = x_start + target * w
        self.click_position([x_target, y_center])
        self.sleep(1)
        slider_sound = PlayerSettingPanel.get_slider_sound(self)
        delta = abs(target - slider_sound)
        # if delta > 0.1:
        #     raise DifferError
        print(delta)

    def get_options_graphics_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSettingPanel.options_graphics_list)
        return position_list

    def set_options_graphics(self, index):
        position_list = PlayerSettingPanel.get_options_graphics_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSettingPanel.options_graphics_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_frame_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSettingPanel.options_frame_list)
        return position_list

    def set_options_frame(self, index):
        position_list = PlayerSettingPanel.get_options_frame_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSettingPanel.options_frame_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_joystick_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSettingPanel.options_joystick_list)
        return position_list

    def set_options_joystick(self, index):
        position_list = PlayerSettingPanel.get_options_joystick_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSettingPanel.options_joystick_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_vibration_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSettingPanel.options_vibration_list)
        return position_list

    def set_options_vibration(self, index):
        position_list = PlayerSettingPanel.get_options_vibration_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSettingPanel.options_vibration_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_list = merge_list(toggle_is_on_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    @staticmethod
    def get_language_check_dict():
        language_check_dict = {"English": "SETTINGS", "русский": "НАСТРОЙКА", "Deutsch": "EINSTELLUNG",
                               "Português": "CONFIGURAÇÃO", "Bahasa Indonesia": "PENGATURAN", "简体中文": "设置"}
        return language_check_dict

    def get_text_tab_setting(self):
        return self.get_text(element_data=ElementsData.PlayerSettingPanel.tab_setting)

    def get_select_parent_id(self):
        return self.get_parent_id(element_data=ElementsData.PlayerSettingPanel.select)

    def get_language_title_parent_id_list(self):
        return self.get_parent_id_list(element_data=ElementsData.PlayerSettingPanel.language_title_list)

    def get_language_title_text_list(self):
        language_title_list = self.get_text_list(element_data=ElementsData.PlayerSettingPanel.language_title_list)
        return language_title_list

    def click_btn_save_language(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_save_language)

    def is_btn_saved_language_active(self):
        return self.exist(element_data=ElementsData.PlayerSettingPanel.btn_saved_language)

    def get_language_title_position_list(self):
        return self.get_position_list(element_data=ElementsData.PlayerSettingPanel.language_title_list)

    def click_btn_logout(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_logout)

    # edit profile

    def open_edit_profile(self):
        HomePanel.go_to_panel(self, "PlayerSettingPanel")
        if PlayerSettingPanel.is_Panel_Popups_Edit_active(self):
            return
        PlayerSettingPanel.click_tab_player(self)
        self.sleep(1)
        PlayerSettingPanel.click_edit_info(self)

    def click_tab_avatar(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_avatar)

    def click_tab_banner(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_banner)

    def click_tab_name(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_name)

    def click_tab_badge(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.tab_badge)




    def get_avatar_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerSettingPanel.avatar_list)

    def get_avatar_viewport(self, avatar_id_list):
        size_list = self.get_size_list(object_id=avatar_id_list[0])
        h = 0
        if size_list:
            h = size_list[0][1]
        avatar_viewport = Viewport(self, element_viewport=ElementsData.PlayerSettingPanel.viewport_avatar, item_id_list=avatar_id_list, viewport_direction="column", viewport_edge=[0, 0.5 * h])
        return avatar_viewport

    def select_avatar(self, avatar_id_list, index):
        avatar_viewport = PlayerSettingPanel.get_avatar_viewport(self, avatar_id_list)
        avatar_viewport.move_until_appear(target_id=avatar_id_list[index])
        self.click_element(object_id=avatar_id_list[index], focus=[0, 0.5])
        selected_avatar_index = PlayerSettingPanel.get_selected_icon_index(self, avatar_id_list)
        compare(index, selected_avatar_index)

    def get_selected_icon_index(self, icon_id_list):
        select_id_list = self.get_offspring_id_list(object_id_list=icon_id_list, offspring_path="select")
        select_id_list = merge_list(select_id_list)
        icon_id = self.get_parent_id(object_id=select_id_list[0])
        index = icon_id_list.index(icon_id)
        return index

    def get_avatar(self, avatar_id):
        head_img_id = self.get_offspring_id(object_id=avatar_id, offspring_path="head>head_mask>head_img")
        return self.get_icon(object_id=head_img_id)

    def get_banner_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerSettingPanel.banner_list)

    def get_banner_viewport(self, banner_id_list):
        size_list = self.get_size_list(object_id=banner_id_list[0])
        h = 0
        if size_list:
            h = size_list[0][1]
        banner_viewport = Viewport(self, element_viewport=ElementsData.PlayerSettingPanel.viewport_banner, item_id_list=banner_id_list, viewport_direction="column", viewport_edge=[0, 0.5 * h])
        return banner_viewport

    def select_banner(self, banner_id_list, index):
        banner_viewport = PlayerSettingPanel.get_banner_viewport(self, banner_id_list)
        banner_viewport.move_until_appear(target_id=banner_id_list[index])
        self.click_element(object_id=banner_id_list[index], focus=[0, 0.5])
        selected_banner_index = PlayerSettingPanel.get_selected_icon_index(self, banner_id_list)
        compare(index, selected_banner_index)



    def get_banner(self, banner_id):
        head_img_id = self.get_offspring_id(object_id=banner_id, offspring_path="icon")
        return self.get_icon(object_id=head_img_id)

    def click_btn_save(self):
        self.click_element(element_data=ElementsData.PlayerSettingPanel.btn_save_profile)

    def is_btn_saved_active(self):
        btn_saved_profile_id_list = self.get_object_id_list(element_data=ElementsData.PlayerSettingPanel.btn_saved_profile)
        if btn_saved_profile_id_list:
            return True
        return False

    def get_badge_slot_id_list(self):
        badge_slot_id_list =  self.get_object_id_list(element_data=ElementsData.PlayerSettingPanel.badge_slot_list)
        return badge_slot_id_list

    def get_badge_id_list(self):
        badge_id_list = self.get_object_id_list(element_data=ElementsData.PlayerSettingPanel.badge_list)
        return badge_id_list

    def get_badge_viewport(self, badge_id_list):
        size_list = self.get_size_list(object_id=badge_id_list[0])
        h = 0
        if size_list:
            h = size_list[0][1]
        badge_viewport = Viewport(self, element_viewport=ElementsData.PlayerSettingPanel.viewport_badge, item_id_list=badge_id_list, viewport_direction="column", viewport_edge=[-0.5 * h, 0.5 * h])
        return badge_viewport

    def get_badge_slot_list(self, badge_slot_id_list):
        badge_slot_list = []
        cur = 0
        while cur < len(badge_slot_id_list):
            badge_img_list = self.get_icon_list(object_id=badge_slot_id_list[cur], offspring_path="badge_img")
            if badge_img_list:
                badge_slot_list.append(badge_img_list[0])
                cur += 1
                continue
            badge_slot_list.append("")
            cur += 1


        return badge_slot_list

    def select_badge_slot(self, badge_slot_id_list, index):
        self.click_element(object_id=badge_slot_id_list[index])

    def get_selected_badge_slot_index(self):
        toggle_is_on_list = self.get_toggle_is_on_list(element_data=ElementsData.PlayerSettingPanel.badge_slot_list)
        index = get_toggle_is_on_index(toggle_is_on_list=toggle_is_on_list)
        return index

    def get_badge_status(self, badge_id_list):
        locked_list = []
        unlocked_list = []
        equipped_list = []
        cur = 0
        while cur < len(badge_id_list):
            lock_id_list = self.get_offspring_id_list(object_id=badge_id_list[cur], offspring_path="lock")
            if lock_id_list:
                locked_list.append(cur)
                cur += 1
                continue
            tip_equipped_id_list = self.get_offspring_id_list(object_id=badge_id_list[cur], offspring_path="tip_equipped")
            if tip_equipped_id_list:
                equipped_list.append(cur)
            unlocked_list.append(cur)
            cur += 1
        return locked_list, unlocked_list, equipped_list

    def get_badge_list(self, badge_id_list):
        icon_list = self.get_icon_list(object_id_list=badge_id_list, offspring_path="icon")
        return icon_list

    def select_badge(self, badge_id_list, index):
        badge_viewport = PlayerSettingPanel.get_badge_viewport(self, badge_id_list)
        badge_viewport.move_until_appear(target_id=badge_id_list[index])
        self.click_element(object_id=badge_id_list[index], focus=[0, 0.5])

    def get_badge_player_list(self):
        icon_list = self.get_icon_list(element_data=ElementsData.PlayerSettingPanel.badge_player_list)
        icon_list = merge_list(icon_list)
        return icon_list

    def set_player_name(self, name):
        self.set_text(element_data=ElementsData.PlayerSettingPanel.Input_PlayerName, text=name)

    def get_points(self):
        points = self.get_text_list(element_data=ElementsData.PlayerSettingPanel.points)
        if not points:
            return "0"
        return points[0]

    def get_weight(self):
        weight = self.get_text_list(element_data=ElementsData.PlayerSettingPanel.weight)
        if not weight:
            return "0"
        return weight[0]


if __name__ == '__main__':
    bp = BasePage()
    a = bp.excelTools.get_exp_limit(10)
    print(a)
    # options_graphics_position_list = PlayerSettingPanel.get_options_graphics_position_list(bp)
    # a = PlayerSettingPanel.set_options_graphics(bp, options_graphics_position_list,0)






