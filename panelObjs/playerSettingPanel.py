from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *
from common.viewport import Viewport

class PlayerSettingPanel(BasePage):
    def is_panel_active(self):
        if self.exist(element_data=ElementsData.PlayerSetting.PlayerSettingPanel):
            return True
        return False

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_close)

    def click_tab_player(self):
        self.click_element(element_data=ElementsData.PlayerSetting.tab_player)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_player):
            raise FindNoElementError

    def click_tab_settings(self):
        self.click_element(element_data=ElementsData.PlayerSetting.tab_setting)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_setting):
            raise FindNoElementError

    def click_tab_language(self):
        self.click_element(element_data=ElementsData.PlayerSetting.tab_language)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_language):
            raise FindNoElementError

    def get_exp_val(self):
        # 得到等级
        lv_str = self.get_text(element_data=ElementsData.PlayerSetting.player_lv)
        lv = int(lv_str)
        # 得到进度条占总进度的百分比
        exp_progress = self.get_slider_value(element_data=ElementsData.PlayerSetting.exp)
        # 得到当前等级经验上限
        exp_limit, exp_limit_all = self.excelTools.get_exp_limit(lv)
        print(exp_limit)
        # 经验 = 经验上限 * 进度条占总进度的百分比 + 以前等级的经验总量
        exp = int(exp_progress * exp_limit + 0.5) + exp_limit_all  # 求出的数是float需要四舍五入一下
        # 通过指令读取当前经验总量
        exp_db = self.get_item_count(item_tpid="100200")
        compare(exp, exp_db)
        print(f"当前经验总量为{exp}")
        return exp

    def get_player_data(self):
        name = self.get_text(element_data=ElementsData.PlayerSetting.player_name)
        head = self.get_icon(element_data=ElementsData.PlayerSetting.head)
        flag = self.get_icon(element_data=ElementsData.PlayerSetting.flag)
        lv_str = self.get_text(element_data=ElementsData.PlayerSetting.player_lv)
        lv = int(lv_str)
        return name, head, flag, lv

    def click_name(self):
        self.click_element(element_data=ElementsData.PlayerSetting.player_name)
        self.sleep(0.5)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_name):
            raise FindNoElementError

    def click_head(self):
        self.click_element(element_data=ElementsData.PlayerSetting.head)
        self.sleep(0.5)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_avatar):
            raise FindNoElementError

    def click_flag(self):
        self.click_element(element_data=ElementsData.PlayerSetting.flag)
        self.sleep(0.5)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_banner):
            raise FindNoElementError

    def click_edit_info(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_edit_info)
        self.sleep(0.5)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_avatar):
            raise FindNoElementError

    def click_edit_badge(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_edit_badge)
        self.sleep(0.5)
        if not self.exist(element_data=ElementsData.PlayerSetting.panel_badge):
            raise FindNoElementError

    def close_edit_profile(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_close_additional)
        self.sleep(0.5)
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Popups_Edit):
            raise FindElementError

    def click_btn_giftcode(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_giftcode)

    def set_giftcode(self, text):
        self.set_text(element_data=ElementsData.PlayerSetting.giftcode_input, text=text)

    def get_giftcode(self):
        giftcode_input = self.get_text(element_data=ElementsData.PlayerSetting.giftcode_input)
        return giftcode_input

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_confirm)

    def click_btn_close_giftcode(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_close_additional)
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Giftcode):
            raise FindElementError

    def click_badge_i(self):
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules):
            self.click_element(element_data=ElementsData.PlayerSetting.btn_i_badge)
            if self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules):
                raise FindElementError
            return
        self.click_element(element_data=ElementsData.PlayerSetting.btn_i_badge)
        if not self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules):
            raise FindNoElementError

    def get_slider_music(self):
        return self.get_slider_value(element_data=ElementsData.PlayerSetting.options_music)

    def set_slider_music(self, target_val):
        if target_val > 0.99:
            target_val = 0.99
        w = self.get_size(element_data=ElementsData.PlayerSetting.options_music_bg)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerSetting.options_music_bg)
        x_start = x_center - 0.5 * w
        x_target = x_start + target_val * w
        self.click_position([x_target, y_center])
        slider_music = PlayerSettingPanel.get_slider_music(self)
        delta = abs(target_val - slider_music)
        if delta > 0.05:
            raise DifferError

    def get_slider_sound(self):
        return self.get_slider_value(element_data=ElementsData.PlayerSetting.options_sound)

    def set_slider_sound(self, target):
        if target > 0.95:
            target = 0.95
        if target < 0.05:
            target = 0.05
        w = self.get_size(element_data=ElementsData.PlayerSetting.options_sound_bg)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerSetting.options_sound_bg)
        x_start = x_center - 0.5 * w
        x_target = x_start + target * w
        self.click_position([x_target, y_center])
        slider_sound = PlayerSettingPanel.get_slider_sound(self)
        delta = abs(target - slider_sound)
        if delta > 0.1:
            raise DifferError

    def get_options_graphics_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSetting.options_graphics_list)
        return position_list

    def set_options_graphics(self, index):
        position_list = PlayerSettingPanel.get_options_graphics_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSetting.options_graphics_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_frame_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSetting.options_frame_list)
        return position_list

    def set_options_frame(self, index):
        position_list = PlayerSettingPanel.get_options_frame_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSetting.options_frame_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_joystick_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSetting.options_joystick_list)
        return position_list

    def set_options_joystick(self, index):
        position_list = PlayerSettingPanel.get_options_joystick_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSetting.options_joystick_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    def get_options_vibration_position_list(self):
        position_list = self.get_position_list(element_data=ElementsData.PlayerSetting.options_vibration_list)
        return position_list

    def set_options_vibration(self, index):
        position_list = PlayerSettingPanel.get_options_vibration_position_list(self)
        self.click_position(position_list[index])
        tab_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSetting.options_vibration_list)
        toggle_is_on_list = self.get_toggle_is_on_list(object_id_list=tab_id_list)
        toggle_is_on_index = get_toggle_is_on_index(toggle_is_on_list)
        compare(index, toggle_is_on_index)

    @staticmethod
    def get_language_check_dict():
        language_check_dict = {"English": "SETTINGS", "русский": "НАСТРОЙКА", "Deutsch": "EINSTELLUNG",
                               "Português": "CONFIGURAÇÃO", "Bahasa Indonesia": "PENGATURAN", "简体中文": "设置"}
        return language_check_dict

    def get_text_tab_setting(self):
        return self.get_text(element_data=ElementsData.PlayerSetting.tab_setting)

    def get_select_parent_id(self):
        return self.get_parent_id(element_data=ElementsData.PlayerSetting.select)

    def get_language_title_parent_id_list(self):
        return self.get_parent_id_list(element_data=ElementsData.PlayerSetting.language_title_list)

    def get_language_title_text_list(self):
        language_title_list = self.get_text_list(element_data=ElementsData.PlayerSetting.language_title_list)
        return language_title_list

    def click_btn_save_language(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_save_language)

    def is_btn_saved_language_active(self):
        if self.exist(element_data=ElementsData.PlayerSetting.btn_saved_language):
            return True
        return False

    def get_language_title_position_list(self):
        return self.get_position_list(element_data=ElementsData.PlayerSetting.language_title_list)

    def click_btn_logout(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_logout)

    def get_avatar_id_list(self):
        return self.get_object_id_list(element_data=ElementsData.PlayerSetting.avatar_list)

    def get_avatar_viewport(self, avatar_id_list):
        avatar_viewport = Viewport(self, element_viewport=ElementsData.PlayerSetting.viewport_avatar, item_id_list=avatar_id_list)
        return avatar_viewport

    def select_avatar(self, avatar_id_list, index):
        self.click_element(object_id=avatar_id_list[index])
        select_id_list = self.get_offspring_id_list(object_id=avatar_id_list[index], offspring_path="select")
        if not select_id_list:
            raise FindNoElementError

    def get_avatar(self, avatar_id):
        head_img_id = self.get_offspring_id(object_id=avatar_id, offspring_path="head>head_mask>head_img")
        return self.get_icon(object_id=head_img_id)



if __name__ == '__main__':
    bp = BasePage()
    options_graphics_position_list = PlayerSettingPanel.get_options_graphics_position_list(bp)
    a = PlayerSettingPanel.set_options_graphics(bp, options_graphics_position_list,0)
    print(a)





