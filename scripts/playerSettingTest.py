import random
from common.resource import *
from panelObjs.playerSettingPanel import PlayerSettingPanel
from common.basePage import BasePage
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.rewardsPanel import RewardsPanel

def player_test(bp: BasePage):
    PlayerSettingPanel.click_tab_player(bp)

    PlayerSettingPanel.click_head(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_flag(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_name(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_edit_badge(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_badge_i(bp)
    bp.click_position([0.5, 0.1])

    PlayerSettingPanel.click_edit_info(bp)

def avatar_test(bp: BasePage):
    pass

def banner_test(bp: BasePage):
    pass

def name_test(bp: BasePage):
    pass

def badge_test(bp: BasePage):
    pass


def settings_test(bp: BasePage):
    # 切换到settings
    PlayerSettingPanel.click_tab_settings(bp)

    PlayerSettingPanel.set_slider_music(bp, random.random())
    PlayerSettingPanel.set_slider_sound(bp, random.random())
    PlayerSettingPanel.set_options_graphics(bp, random.randint(0, 2))
    PlayerSettingPanel.set_options_frame(bp, random.randint(0, 1))
    PlayerSettingPanel.set_options_joystick(bp, random.randint(0, 1))
    PlayerSettingPanel.set_options_vibration(bp, random.randint(0, 1))

def language_test(bp: BasePage):
    # 得到不同语言对应的settings文本
    language_check_dict = PlayerSettingPanel.get_language_check_dict()

    # 切换到language
    PlayerSettingPanel.click_tab_language(bp)
    bp.sleep(0.5)

    # 得到语言选项信息
    language_title_text_list = PlayerSettingPanel.get_language_title_text_list(bp)
    language_title_position_list = PlayerSettingPanel.get_language_title_position_list(bp)
    language_title_parent_id_list = PlayerSettingPanel.get_language_title_parent_id_list(bp)

    # 从后往前点击并对照
    cur = len(language_title_text_list) - 1
    while cur >= 0:
        bp.click_position(language_title_position_list[cur])
        # 比较当前点击标签与选中标签是否一致
        select_parent_id = PlayerSettingPanel.get_select_parent_id(bp)
        compare(language_title_parent_id_list[cur], select_parent_id)
        # 保存
        PlayerSettingPanel.click_btn_save_language(bp)
        # 比较语言是否改为对应语言
        text_tab_setting_expect = language_check_dict[language_title_text_list[cur]]
        text_tab_setting = PlayerSettingPanel.get_text_tab_setting(bp)
        compare(text_tab_setting, text_tab_setting_expect)
        # 看保存按钮是否切换为SAVED
        if not PlayerSettingPanel.is_btn_saved_language_active(bp):
            raise FindNoElementError
        cur -= 1
    print("切换语言测试通过")

def gift_code_test(bp: BasePage):
    PlayerSettingPanel.click_btn_giftcode(bp)
    bp.sleep(0.2)
    # 输入不存在的礼包码
    giftcode = "1234"
    PlayerSettingPanel.set_giftcode(bp, giftcode)
    giftcode_input = PlayerSettingPanel.get_giftcode(bp)
    compare(giftcode, giftcode_input)
    PlayerSettingPanel.click_btn_confirm(bp)
    bp.sleep(0.2)
    bp.cmd("activationcodeclear")
    # 输入存在的礼包码
    giftcode = "fishon888"
    PlayerSettingPanel.set_giftcode(bp, giftcode)
    giftcode_input = PlayerSettingPanel.get_giftcode(bp)
    compare(giftcode, giftcode_input)
    PlayerSettingPanel.click_btn_confirm(bp)
    bp.sleep(0.2)
    RewardsPanel.click_tap_to_claim(bp)
    PlayerSettingPanel.click_btn_close_giftcode(bp)



if __name__ == '__main__':
    bp = BasePage()
    gift_code_test(bp)