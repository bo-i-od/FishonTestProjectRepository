import datetime
import random

from common import gameInit
from common.resource import *
from panelObjs.playerInfoPanel import PlayerInfoPanel
from panelObjs.playerSettingPanel import PlayerSettingPanel
from common.basePage import BasePage
from panelObjs.messageBoxPanel import MessageBoxPanel
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.homePanel import HomePanel

def gift_code_test(bp: BasePage):
    if not PlayerSettingPanel.is_btn_giftcode_active(bp):
        bp.debug_log("跳过激活码测试")
        return
    PlayerInfoPanel.click_btn_giftcode(bp)
    bp.sleep(1)
    # 输入不存在的礼包码
    giftcode = "1234"
    PlayerInfoPanel.set_giftcode(bp, giftcode)
    giftcode_input = PlayerSettingPanel.get_giftcode(bp)
    compare(giftcode, giftcode_input)
    PlayerInfoPanel.click_btn_confirm(bp)
    bp.sleep(1)
    bp.cmd("activationcodeclear")
    # 输入存在的礼包码
    giftcode = "fishon888"
    PlayerInfoPanel.set_giftcode(bp, giftcode)
    giftcode_input = PlayerInfoPanel.get_giftcode(bp)
    compare(giftcode, giftcode_input)
    PlayerInfoPanel.click_btn_confirm(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_btn_close_additional(bp)

def settings_test(bp: BasePage):
    PlayerInfoPanel.click_tab_avatar(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_name(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_setting(bp)
    bp.sleep(1)
    PlayerInfoPanel.set_slider_music(bp, random.random())
    PlayerInfoPanel.set_slider_sound(bp, random.random())
    PlayerInfoPanel.set_options_graphics(bp, random.randint(0, 2))
    PlayerInfoPanel.set_options_frame(bp, random.randint(0, 1))
    PlayerInfoPanel.set_options_joystick(bp, random.randint(0, 1))
    PlayerInfoPanel.set_options_vibration(bp, random.randint(0, 1))
    PlayerInfoPanel.set_options_gyro(bp, random.randint(0, 1))
    PlayerInfoPanel.set_options_invite(bp, random.randint(0, 1))

def name_test(bp: BasePage):
    PlayerInfoPanel.click_tab_name(bp)
    bp.sleep(1)
    bp.set_item_count(target_count=300, item_tpid="100100")
    # 将名字改为当前时间
    now = datetime.datetime.now()
    name = 't' + now.strftime("%y%m%d%H%M%S")
    PlayerInfoPanel.set_player_name(bp, name)

    # 保存
    PlayerInfoPanel.click_btn_save(bp)
    bp.sleep(1)

    # 二次确认
    MessageBoxPanel.click_btn_confirm(bp)
    bp.sleep(1)
    if not PlayerInfoPanel.is_btn_save_pay_abled(bp):
        bp.debug_log("erro_"+"if not PlayerInfoPanel.is_btn_save_pay_abled(bp)")

    # # 返回上级 对比是否改名成功
    # PlayerInfoPanel.click_btn_close_additional(bp)
    # bp.sleep(1)
    # playerInfo = PlayerInfoPanel.get_player_info(bp)
    # compare(name, playerInfo["player_name"])
    #
    # # 再次进入界面
    # PlayerInfoPanel.click_btn_setting(bp)
    # bp.sleep(1)
    # PlayerInfoPanel.click_tab_name(bp)
    # bp.sleep(1)
    #
    # # 测试付费改名
    # value_cost = PlayerInfoPanel.get_value_cost(bp)
    # cash_expect = bp.get_item_count(item_tpid="100100") - value_cost
    # name = name + "0"
    # PlayerInfoPanel.set_player_name(bp, name)
    # # 保存
    # PlayerInfoPanel.click_btn_save_pay(bp)
    # bp.sleep(1)
    # cash = bp.get_item_count(item_tpid="100100")
    # compare(cash_expect, cash)
    # if PlayerInfoPanel.is_btn_save_pay_abled(bp):
    #     bp.debug_log("erro_" + "PlayerInfoPanel.is_btn_save_pay_abled(bp)")


    # # 返回上级 对比名称
    # PlayerInfoPanel.click_btn_close_additional(bp)
    # bp.sleep(1)
    # playerInfo = PlayerInfoPanel.get_player_info(bp)
    # compare(name, playerInfo["player_name"])

    PlayerInfoPanel.click_btn_close_additional(bp)

def avatar_test(bp: BasePage):
    PlayerInfoPanel.click_tab_avatar(bp)
    bp.sleep(1)
    # 排除当前选中的头像
    avatar_id_list = PlayerInfoPanel.get_avatar_id_list(bp)
    selected_avatar_index = PlayerInfoPanel.get_selected_icon_index(bp, avatar_id_list)
    excluded_nums = [selected_avatar_index]  # 要跳过的数
    start_num = 0
    end_num = len(avatar_id_list) - 1

    # 随机选择头像进行点击
    random_num = random.choice([num for num in range(start_num, end_num + 1) if num not in excluded_nums])
    PlayerInfoPanel.select_avatar(bp, avatar_id_list=avatar_id_list, index=random_num)
    selected_avatar_index = PlayerInfoPanel.get_selected_icon_index(bp, avatar_id_list)
    compare(selected_avatar_index, random_num)
    avatar = PlayerInfoPanel.get_avatar(bp, avatar_id=avatar_id_list[selected_avatar_index])
    PlayerInfoPanel.click_btn_save(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_btn_close_additional(bp)
    player_info = PlayerInfoPanel.get_player_info(bp)
    compare(avatar, player_info["head_img"])

def main(bp:BasePage):
    # 登录到大厅
    cmd_list = ["guideskip"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    bp.go_to_panel("PlayerInfoPanel")
    bp.sleep(1)

    # 点击复制姓名
    PlayerInfoPanel.click_btn_copy(bp)
    bp.sleep(1)

    # 点击战力详情
    PlayerInfoPanel.click_btn_i_rating(bp)
    bp.sleep(1)
    bp.click_position([0.1, 0.5])

    # 点击鱼竿详情
    PlayerInfoPanel.click_btn_i_rod(bp)
    bp.sleep(1)
    bp.click_position([0.1, 0.5])

    # 点击礼包码
    gift_code_test(bp)

    # 点击我的记录和我的勋章切换
    PlayerInfoPanel.click_btn_tag(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_btn_tag(bp)
    bp.sleep(1)

    # 点击设置
    PlayerInfoPanel.click_btn_setting(bp)
    bp.sleep(1)
    settings_test(bp)
    PlayerInfoPanel.click_btn_close_additional(bp)

    # 改名测试
    PlayerInfoPanel.click_btn_edit_player_info(bp)
    bp.sleep(1)
    name_test(bp)

    # 换头像测试
    PlayerInfoPanel.click_btn_edit_player_info(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_avatar(bp)
    bp.sleep(1)
    avatar_test(bp)

    #
    playerInfo = PlayerInfoPanel.get_player_info(bp)
    bp.go_home()
    playerInfo_home = HomePanel.get_player_info(bp)
    compare(playerInfo, playerInfo_home)




if __name__ == '__main__':
    bp = BasePage("192.168.111.81:20012")
    main(bp)
    bp.connect_close()