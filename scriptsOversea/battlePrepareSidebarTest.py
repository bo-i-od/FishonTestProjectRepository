from common import gameInit
from common.basePage import BasePage
from panelObjs import FishAlbum3DPanel, FlashCardBoxesPanel, FishCardPanel
from panelObjs.AchievementWantedPanel import AchievementWantedPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.CareerPanel import CareerPanel
from panelObjs.ClubApplyPanel import ClubApplyPanel
from panelObjs.FriendPanel import FriendPanel
from panelObjs.HomePanel import HomePanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.FlashCardBoxesPanel import FlashCardBoxesPanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.PlayerInfoPanel import PlayerInfoPanel
from panelObjs.PlayerInteractPanel import PlayerInteractPanel
from panelObjs.RankPanel import RankPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.StorePanel import StorePanel
from panelObjs.TournamentsPanel import TournamentsPanel
from scripts import battleTest
from tools.commonTools import *





def main(bp: BasePage):
    # 登录到大厅
    cmd_list = ["guideskip", "levelupto 20"]
    gameInit.login_to_hall(bp, cmd_list=cmd_list)

    bp.clear_popup()

    # 去渔场
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)
    TournamentsPanel.go_to_fishery_by_index(bp, 1)

    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 点击打开备战收纳界面
    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)


    #  点击查看玩家名片
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_player(bp)
    bp.sleep(1)
    PlayerInteractPanel.is_panel_active(bp)
    PlayerInteractPanel.click_btn_close(bp)

    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看鱼册
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_fishalbum(bp)
    bp.sleep(1)
    FishAlbum3DPanel.is_panel_active(bp)
    FishAlbum3DPanel.click_btn_close(bp)

    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看闪卡
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_flashcard(bp)
    bp.sleep(1)
    FlashCardBoxesPanel.is_panel_active(bp)
    FlashCardBoxesPanel.click_btn_close(bp)

    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看鱼卡
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_fishcard(bp)
    bp.sleep(1)
    FishCardPanel.is_panel_active(bp)
    FishCardPanel.click_btn_close(bp)

    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看照片墙
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_achievement(bp)
    bp.sleep(1)
    AchievementWantedPanel.is_panel_active(bp)
    AchievementWantedPanel.click_btn_close(bp)

    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看商城
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_store(bp)
    bp.sleep(1)
    StorePanel.is_panel_active(bp)
    StorePanel.click_btn_close(bp)
    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看钓者生涯
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_career(bp)
    bp.sleep(1)
    CareerPanel.is_panel_active(bp)
    CareerPanel.click_btn_close(bp)
    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看好友
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_friend(bp)
    bp.sleep(1)
    FriendPanel.is_panel_active(bp)
    FriendPanel.click_btn_close(bp)
    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看俱乐部
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_club(bp)
    bp.sleep(1)
    ClubApplyPanel.is_panel_active(bp)
    ClubApplyPanel.click_btn_close(bp)
    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看鱼竿
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_gears(bp)
    bp.sleep(1)

    BattlePreparePanel.panel_gears_new.click_btn_cancel(bp)
    BattlePreparePanel.panel_pve_prepare.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看鱼护
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_aquarium(bp)
    bp.sleep(1)
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_close(bp)







    # 点击查看邮件
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_fishcard(bp)

    # 点击查看公告
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_fishcard(bp)


    # 点击查看avatar
    BattlePreparePanel.panel_pve_prepare.panel_main_sidebar.click_btn_fishcard(bp)


if __name__ == '__main__':

    bp = BasePage("127.0.0.1:21503", is_mobile_device=False)
    main(bp)
    bp.connect_close()