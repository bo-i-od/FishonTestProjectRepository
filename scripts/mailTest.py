import random
from items.resource import *
from panelObjs.rewardsPanel import RewardsPanel
from panelObjs.itemTipsPanel import ItemTipsPanel
from tools.viewport import Viewport
from common.basePage import BasePage
from panelObjs.homePanel import HomePanel
from panelObjs.mailPanel import MailPanel
from panelObjs.fishCardPackTipsPanel import FishCardPackTipsPanel
from panelObjs.baitAndRodShowPanel import BaitAndRodShowPanel



def switch_tab_test(bp:BasePage):
    tab_position_list = MailPanel.get_tab_position_list(bp)
    MailPanel.switch_tab(bp, tab_position_list, 0)
    MailPanel.switch_tab(bp, tab_position_list, 1)
    print("switch_tab_test切换标签测试通过")

def select_mail_test(bp:BasePage):
    if MailPanel.is_mail_empty(bp):
        print("信箱为空，跳过测试")
        return
    mail_viewport = MailPanel.get_mail_viewport(bp)
    mail_id_list = mail_viewport.item_id_list
    r = random.randint(0, len(mail_id_list) - 1)
    mail_viewport.move_until_appear(mail_id_list[r])
    mail_position_list = MailPanel.get_mail_position_list(bp)
    bp.click_position(mail_position_list[r])
    mail_is_on_list = MailPanel.get_mail_is_on_list(bp)
    toggle_is_on_index = get_toggle_is_on_index(mail_is_on_list)
    compare(r, toggle_is_on_index)
    print("select_mail_test选择信件测试通过")

def click_icon_test(bp: BasePage):
    reward_icon_list = MailPanel.get_reward_icon_list(bp)
    if not reward_icon_list:
        print("没有可以点击的图标，跳过测试")
        return
    reward_position_list = MailPanel.get_reward_position_list(bp)
    r = random.randint(0, len(reward_icon_list) - 1)
    bp.click_position(reward_position_list[r])
    if ItemTipsPanel.is_panel_active(bp):
        item_icon = ItemTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon_list[r])
        bp.click_position([0.5, 0.1])
    elif FishCardPackTipsPanel.is_panel_active(bp):
        item_icon = FishCardPackTipsPanel.get_item_icon(bp)
        compare(item_icon, reward_icon_list[r])
        bp.click_position([0.5, 0.1])
    elif BaitAndRodShowPanel.is_panel_active(bp):
        BaitAndRodShowPanel.click_tap_to_continue(bp)
    print("click_icon_test点击图标测试通过")


def click_btn_claim_test(bp:BasePage):
    if not MailPanel.is_claimable(bp):
        print("没有可领取奖励跳过测试")
        return
    reward_icon_expect_list = MailPanel.get_reward_icon_list(bp)
    MailPanel.click_btn_claim(bp)
    reward_icon_list = RewardsPanel.get_reward_icon_list(bp, is_divide=False)
    print(reward_icon_expect_list, reward_icon_list)
    compare_list(reward_icon_expect_list, reward_icon_list)
    RewardsPanel.click_tap_to_continue(bp)
    if not MailPanel.is_claimed(bp):
        raise FindNoElementError
    print("奖励领取测试通过")

def MailPanel_test(bp:BasePage):
    HomePanel.go_to_MailPanel(bp)
    switch_tab_test(bp)
    select_mail_test(bp)
    click_icon_test(bp)
    click_btn_claim_test(bp)
    MailPanel.click_btn_close(bp)



if __name__ == '__main__':
    bp = BasePage()
    MailPanel_test(bp)