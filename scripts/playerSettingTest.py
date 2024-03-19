import random
import time

from common import gameInit
from common.resource import *
from panelObjs.playerSettingPanel import PlayerSettingPanel
from common.basePage import BasePage
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.homePanel import HomePanel
import datetime



def player_test(bp: BasePage):
    PlayerSettingPanel.click_head(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_flag(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_name(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_edit_badge(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    PlayerSettingPanel.click_badge_i(bp)
    bp.click_position_base([0.5, 0.9])



def avatar_test(bp: BasePage):
    PlayerSettingPanel.click_tab_avatar(bp)
    bp.sleep(1)
    # 排除当前选中的头像
    avatar_id_list = PlayerSettingPanel.get_avatar_id_list(bp)
    selected_avatar_index = PlayerSettingPanel.get_selected_icon_index(bp, avatar_id_list)
    excluded_nums = [selected_avatar_index]  # 要跳过的数
    start_num = 0
    end_num = len(avatar_id_list) - 1

    # 随机选择头像进行点击
    random_num = random.choice([num for num in range(start_num, end_num + 1) if num not in excluded_nums])
    PlayerSettingPanel.select_avatar(bp, avatar_id_list=avatar_id_list, index=random_num)
    selected_avatar_index = PlayerSettingPanel.get_selected_icon_index(bp, avatar_id_list)
    compare(selected_avatar_index, random_num)
    avatar = PlayerSettingPanel.get_avatar(bp, avatar_id=avatar_id_list[selected_avatar_index])
    PlayerSettingPanel.click_btn_save(bp)
    bp.sleep(1)
    bp.go_home()
    head_img = HomePanel.get_head_img(bp)
    compare(avatar, head_img)




def banner_test(bp: BasePage):
    PlayerSettingPanel.click_tab_banner(bp)
    bp.sleep(1)
    # 排除当前选中的头像
    banner_id_list = PlayerSettingPanel.get_banner_id_list(bp)
    selected_banner_index = PlayerSettingPanel.get_selected_icon_index(bp, banner_id_list)
    excluded_nums = [selected_banner_index]  # 要跳过的数
    start_num = 0
    end_num = len(banner_id_list) - 1

    # 随机选择头像进行点击
    random_num = random.choice([num for num in range(start_num, end_num + 1) if num not in excluded_nums])
    PlayerSettingPanel.select_banner(bp, banner_id_list=banner_id_list, index=random_num)
    selected_banner_index = PlayerSettingPanel.get_selected_icon_index(bp, banner_id_list)
    compare(selected_banner_index, random_num)
    banner = PlayerSettingPanel.get_banner(bp, banner_id=banner_id_list[selected_banner_index])
    PlayerSettingPanel.click_btn_save(bp)
    bp.sleep(1)
    bp.go_home()
    flag = HomePanel.get_flag(bp)
    compare(banner, flag)

def name_test(bp: BasePage):
    PlayerSettingPanel.click_tab_name(bp)
    bp.sleep(1)
    # 将名字改为当前时间
    now = datetime.datetime.now()
    formatted_time = now.strftime("%y%m%d%H%M%S")
    PlayerSettingPanel.set_player_name(bp, formatted_time)

    # 保存
    PlayerSettingPanel.click_btn_save(bp)
    bp.sleep(1)

    # 回主界面对比名称是否改成功
    bp.go_home()
    name = HomePanel.get_player_name(bp)
    compare(name, formatted_time)

def badge_test(bp: BasePage):
    # 先切到其它页签
    PlayerSettingPanel.click_tab_avatar(bp)

    # 210001到210018 随机选3个
    badge_tpid_list = random.sample(range(210001, 210019), 3)
    badge_tpid_list = list(map(str, badge_tpid_list))
    bp.set_item_count_list(target_count_list=[1, 1, 1], item_tpid_list=badge_tpid_list)

    # 点击徽章页签
    PlayerSettingPanel.click_tab_badge(bp)
    bp.sleep(1)

    # 确认装备的成就有equipped
    badge_slot_id_list = PlayerSettingPanel.get_badge_slot_id_list(bp)
    badge_slot_list = PlayerSettingPanel.get_badge_slot_list(bp, badge_slot_id_list)
    badge_id_list = PlayerSettingPanel.get_badge_id_list(bp)
    badge_list = PlayerSettingPanel.get_badge_list(bp, badge_id_list)
    badge_status = PlayerSettingPanel.get_badge_status(bp, badge_id_list)

    badge_equipped_list = []
    cur = 0
    while cur < len(badge_status[2]):
        badge_equipped_list.append(badge_list[badge_status[2][cur]])
        cur += 1
    print(badge_slot_list)
    while '' in badge_slot_list:
        badge_slot_list.remove('')
    compare_list(badge_slot_list, badge_equipped_list)

    # 给孔位随机选成就徽章
    cur = 0
    while cur < len(badge_slot_id_list):
        PlayerSettingPanel.select_badge_slot(bp, badge_slot_id_list=badge_slot_id_list, index=cur)
        r = random.randint(0, len(badge_status[1]) - 1)
        PlayerSettingPanel.select_badge(bp, badge_id_list=badge_id_list, index=badge_status[1][r])
        if badge_list[badge_status[1][r]] != badge_slot_list[cur]:
            PlayerSettingPanel.click_btn_save(bp)
        badge_status = PlayerSettingPanel.get_badge_status(bp, badge_id_list)
        if badge_status[1][r] in badge_status[2]:
            badge_slot_list = PlayerSettingPanel.get_badge_slot_list(bp, badge_slot_id_list)
            cur += 1
            continue
        raise FindNoElementError

    # 再次确认装备的成就有equipped
    badge_slot_list = PlayerSettingPanel.get_badge_slot_list(bp, badge_slot_id_list)
    badge_list = PlayerSettingPanel.get_badge_list(bp, badge_id_list)
    badge_status = PlayerSettingPanel.get_badge_status(bp, badge_id_list)
    badge_equipped_list = []
    cur = 0
    while cur < len(badge_status[2]):
        badge_equipped_list.append(badge_list[badge_status[2][cur]])
        cur += 1
    while '' in badge_slot_list:
        badge_slot_list.remove('')
    compare_list(badge_slot_list, badge_equipped_list)

    # 关闭面板
    PlayerSettingPanel.close_edit_profile(bp)

    # 跟设置界面的徽章对比
    badge_player_list = PlayerSettingPanel.get_badge_player_list(bp)
    compare_list(badge_player_list, badge_slot_list)




def settings_test(bp: BasePage):
    PlayerSettingPanel.set_slider_music(bp, random.random())
    PlayerSettingPanel.set_slider_sound(bp, random.random())
    PlayerSettingPanel.set_options_graphics(bp, random.randint(0, 2))
    PlayerSettingPanel.set_options_frame(bp, random.randint(0, 1))
    PlayerSettingPanel.set_options_joystick(bp, random.randint(0, 1))
    PlayerSettingPanel.set_options_vibration(bp, random.randint(0, 1))

def language_test(bp: BasePage):
    # 得到不同语言对应的settings文本
    language_check_dict = PlayerSettingPanel.get_language_check_dict()

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
    if not PlayerSettingPanel.is_btn_giftcode_active(bp):
        bp.debug_log("跳过激活码测试")
        return
    PlayerSettingPanel.click_btn_giftcode(bp)
    bp.sleep(1)
    # 输入不存在的礼包码
    giftcode = "1234"
    PlayerSettingPanel.set_giftcode(bp, giftcode)
    giftcode_input = PlayerSettingPanel.get_giftcode(bp)
    compare(giftcode, giftcode_input)
    PlayerSettingPanel.click_btn_confirm(bp)
    bp.sleep(1)
    bp.cmd("activationcodeclear")
    # 输入存在的礼包码
    giftcode = "fishon888"
    PlayerSettingPanel.set_giftcode(bp, giftcode)
    giftcode_input = PlayerSettingPanel.get_giftcode(bp)
    compare(giftcode, giftcode_input)
    PlayerSettingPanel.click_btn_confirm(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)
    PlayerSettingPanel.click_btn_close_giftcode(bp)


def main(bp: BasePage):
    # 进入大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    HomePanel.go_to_panel(bp,"PlayerSettingPanel")
    PlayerSettingPanel.click_tab_player(bp)
    bp.sleep(1)
    player_test(bp)

    PlayerSettingPanel.open_edit_profile(bp)
    avatar_test(bp)

    PlayerSettingPanel.open_edit_profile(bp)
    banner_test(bp)

    PlayerSettingPanel.open_edit_profile(bp)
    name_test(bp)

    PlayerSettingPanel.open_edit_profile(bp)
    badge_test(bp)

    # 切换到settings
    PlayerSettingPanel.click_tab_settings(bp)
    bp.sleep(1)
    settings_test(bp)

    PlayerSettingPanel.click_tab_language(bp)
    bp.sleep(1)
    language_test(bp)

    gift_code_test(bp)

    bp.go_home()


if __name__ == '__main__':
    bp = BasePage()
    # badge_test(bp)
    main(bp)
