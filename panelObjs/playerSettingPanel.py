from common.basePage import BasePage
from configs.elementsData import ElementsData
from tools.commonTools import *

class PlayerSettingPanel(BasePage):
    def click_tab_player(self):
        self.click_element(element_data=ElementsData.PlayerSetting.tab_player)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_player) is False:
            raise FindNoElementError

    def click_tab_setting(self):
        self.click_element(element_data=ElementsData.PlayerSetting.tab_setting)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_setting) is False:
            raise FindNoElementError

    def click_tab_language(self):
        self.click_element(element_data=ElementsData.PlayerSetting.tab_language)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_language) is False:
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
        if self.exist(element_data=ElementsData.PlayerSetting.panel_name) is False:
            raise FindNoElementError

    def click_head(self):
        self.click_element(element_data=ElementsData.PlayerSetting.head)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_name) is False:
            raise FindNoElementError

    def click_flag(self):
        self.click_element(element_data=ElementsData.PlayerSetting.flag)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_banner) is False:
            raise FindNoElementError

    def click_edit_info(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_edit_info)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_avatar) is False:
            raise FindNoElementError

    def click_edit_badge(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_edit_badge)
        if self.exist(element_data=ElementsData.PlayerSetting.panel_badge) is False:
            raise FindNoElementError

    def close_edit_profile(self):
        self.click_element(element_data=ElementsData.PlayerSetting.btn_close_profile)
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Popups_Edit):
            raise FindElementError

    def click_badge_i(self):
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules):
            self.click_element(element_data=ElementsData.PlayerSetting.btn_i_badge)
            if self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules):
                raise FindElementError
            return
        self.click_element(element_data=ElementsData.PlayerSetting.btn_i_badge)
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules) is False:
            raise FindNoElementError
        self.click_element(element_data=ElementsData.PlayerSetting.btn_i_badge)
        if self.exist(element_data=ElementsData.PlayerSetting.Panel_Tip_Rules):
            raise FindElementError

    def get_slider_music(self):
        return self.get_slider_value(element_data=ElementsData.PlayerSetting.options_music)

    def set_slider_music(self, target):
        if target > 0.99:
            target = 0.99
        w = self.get_size(element_data=ElementsData.PlayerSetting.options_music_bg)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerSetting.options_music_bg)
        x_start = x_center - 0.5 * w
        x_target = x_start + target * w
        self.click_position([x_target, y_center])
        slider_music = PlayerSettingPanel.get_slider_music(self)
        delta = abs(target - slider_music)
        if delta > 0.05:
            raise DifferError

    def get_slider_sound(self):
        return self.get_slider_value(element_data=ElementsData.PlayerSetting.options_sound)

    def set_slider_sound(self, target):
        if target > 0.99:
            target = 0.99
        w = self.get_size(element_data=ElementsData.PlayerSetting.options_sound_bg)[0]
        x_center, y_center = self.get_position(element_data=ElementsData.PlayerSetting.options_sound_bg)
        x_start = x_center - 0.5 * w
        x_target = x_start + target * w
        self.click_position([x_target, y_center])
        slider_sound = PlayerSettingPanel.get_slider_sound(self)
        delta = abs(target - slider_sound)
        if delta > 0.05:
            raise DifferError

    def language_test(self):
        language_check_dict = {"English": "SETTINGS", "русский": "НАСТРОЙКА", "Deutsch": "EINSTELLUNG",
                               "Português": "CONFIGURAÇÃO", "Bahasa Indonesia": "PENGATURAN"}
        self.click_element(element_data=ElementsData.PlayerSetting.tab_language)
        self.sleep(1)
        language_title_text_list = self.get_text_list(element_data=ElementsData.PlayerSetting.language_title_list)
        language_title_position_list = self.get_position_list(element_data=ElementsData.PlayerSetting.language_title_list)
        language_title_parent_id_list = self.get_parent_id_list(element_data=ElementsData.PlayerSetting.language_title_list)
        cur = 0
        while cur < len(language_title_text_list):
            self.click_position(language_title_position_list[cur])
            # 比较当前点击标签与选中标签是否一致
            select_parent_id = self.get_parent_id(element_data=ElementsData.PlayerSetting.select)
            compare(language_title_parent_id_list[cur], select_parent_id)
            # 保存
            self.click_element(element_data=ElementsData.PlayerSetting.btn_save_language)
            # 比较语言是否改为对应语言
            text_tab_setting_expect = language_check_dict[language_title_text_list[cur]]
            text_tab_setting = self.get_text(element_data=ElementsData.PlayerSetting.tab_setting)
            compare(text_tab_setting, text_tab_setting_expect)
            print(f"更改{language_title_text_list[cur]}语言成功")
            # 看保存按钮是否切换为SAVED
            if self.exist(element_data=ElementsData.PlayerSetting.btn_saved_language) is False:
                raise FindNoElementError
            cur += 1
        print("切换语言测试通过")


if __name__ == '__main__':
    bp = BasePage()
    a = PlayerSettingPanel.language_test(bp)
    print(a)





