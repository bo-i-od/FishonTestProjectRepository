import random

from common import gameInit
from common.resource import *
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.ItemTipsPanel import ItemTipsPanel
from common.basePage import BasePage
from panelObjs.MailPanel import MailPanel
from panelObjs.FishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.BaitAndRodShowPanel import BaitAndRodShowPanel



def switch_tab_test(bp:BasePage):
    # 切换tab
    MailPanel.switch_tab(bp, 0)
    bp.sleep(1)
    MailPanel.switch_tab(bp,  1)
    bp.sleep(1)

def select_mail_test(bp:BasePage):
    # 信箱为空
    if MailPanel.is_mail_empty(bp):
        return

    # 随机选择一封邮件点击
    mail_viewport = MailPanel.get_mail_viewport(bp)
    mail_id_list = mail_viewport.item_id_list
    r = random.randint(0, len(mail_id_list) - 1)

    mail_viewport.move_until_appear(mail_id_list[r])
    mail_position_list = MailPanel.get_mail_position_list(bp)
    bp.click_position(mail_position_list[r])

    # 检查是否选中
    mail_is_on_list = MailPanel.get_mail_is_on_list(bp)
    toggle_is_on_index = get_toggle_is_on_index(mail_is_on_list)
    compare(r, toggle_is_on_index)


def click_icon_test(bp: BasePage):
    reward_icon_list = MailPanel.get_reward_icon_list(bp)

    # 没有奖励图标直接跳过后续测试
    if not reward_icon_list:
        return

    # 随机点击一个图标
    reward_icon_id_list = MailPanel.get_reward_icon_id_list(bp)
    mail_detail_viewport = MailPanel.get_mail_detail_viewport(bp, reward_icon_id_list)
    mail_detail_viewport.move_until_appear(target_id=reward_icon_id_list[0])
    bp.sleep(1)
    reward_position_list = MailPanel.get_reward_position_list(bp)
    r = random.randint(0, len(reward_icon_list) - 1)
    bp.click_position(reward_position_list[r])

    # 道具/鱼卡/鱼竿会有不同响应
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon_list[r])
        bp.click_position_base([0.5, 0.9])
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon_list[r])
        bp.click_position_base([0.5, 0.9])
    elif BaitAndRodShowPanel.is_panel_active(bp):
        BaitAndRodShowPanel.click_tap_to_continue(bp)



def click_btn_claim_test(bp:BasePage):
    # 没有可领取的奖励直接跳过
    if not MailPanel.is_claimable(bp):
        return

    # 随机点击一个奖励领取
    btn_claim_id_list = MailPanel.get_btn_claim_id_list(bp)
    mail_detail_viewport = MailPanel.get_mail_detail_viewport(bp, btn_claim_id_list)
    mail_detail_viewport.move_until_appear(target_id=btn_claim_id_list[0])
    reward_icon_expect_list = MailPanel.get_reward_icon_list(bp)
    MailPanel.click_btn_claim(bp)
    bp.sleep(0.5)
    reward_icon_list = RewardsPanel.get_reward_icon_list(bp, is_divide=False)
    compare_list(reward_icon_expect_list, reward_icon_list)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    if not MailPanel.is_claimed(bp):
        bp.debug_log("error:" , "if not MailPanel.is_claimed(bp)")


def main(bp:BasePage):
    # 查询邮件的解锁等级
    unlock_lv = bp.get_unlock_lv("邮件")

    # 进入大厅
    cmd_list = ["guideskip", f"levelupto {unlock_lv}"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    # 关闭升级弹窗
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()


    bp.go_to_panel("MailPanel")
    bp.sleep(1)
    switch_tab_test(bp)
    select_mail_test(bp)
    click_icon_test(bp)
    click_btn_claim_test(bp)
    MailPanel.click_btn_close(bp)





if __name__ == '__main__':
    bp = BasePage("192.168.111.77:20052")
    main(bp)
    bp.connect_close()