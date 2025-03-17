from common import gameInit
from common.basePage import BasePage
from panelObjs.FishCardPanel import FishCardPanel
from panelObjs.FishAlbum3DPanel import FishAlbum3DPanel
from panelObjs.FlashCardBoxesPanel import FlashCardBoxesPanel
from panelObjs.AchievementWantedPanel import AchievementWantedPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.CareerPanel import CareerPanel
from panelObjs.ClubApplyPanel import ClubApplyPanel
from panelObjs.FriendPanel import FriendPanel
from panelObjs.HomePanel import HomePanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.PlayerInfoPanel import PlayerInfoPanel
from panelObjs.PlayerInteractPanel import PlayerInteractPanel
from panelObjs.RankPanel import RankPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.StorePanel import StorePanel
from panelObjs.MailPanel import MailPanel
from panelObjs.TournamentsPanel import TournamentsPanel
from panelObjs.AquariumFishGuardSideBarPanel import AquariumFishGuardSideBarPanel
from panelObjs.LoginAnnouncementPanel import LoginAnnouncementPanel
from panelObjs.AvatarMainPanel import AvatarMainPanel
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
    TournamentsPanel.go_to_fishery_by_index(bp, 0)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 点击打开备战收纳界面
    #  点击查看玩家名片
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_player(bp)
    PlayerInteractPanel.wait_for_panel_appear(bp)
    PlayerInteractPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看鱼册
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_fishalbum(bp)
    FishAlbum3DPanel.wait_for_panel_appear(bp)
    FishAlbum3DPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看闪卡
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_flashcard(bp)
    FlashCardBoxesPanel.wait_for_panel_appear(bp)
    FlashCardBoxesPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看鱼卡
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_fishcard(bp)
    FishCardPanel.wait_for_panel_appear(bp)
    FishCardPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看照片墙
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_achievement(bp)
    AchievementWantedPanel.wait_for_panel_appear(bp)
    AchievementWantedPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看商城
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_store(bp)
    StorePanel.wait_for_panel_appear(bp)
    StorePanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看钓者生涯
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_career(bp)
    CareerPanel.wait_for_panel_appear(bp)
    CareerPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看好友
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_friend(bp)
    FriendPanel.wait_for_panel_appear(bp)
    FriendPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看俱乐部
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_club(bp)
    ClubApplyPanel.wait_for_panel_appear(bp)
    ClubApplyPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看鱼竿
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_gears(bp)
    bp.sleep(1)
    BattlePreparePanel.panel_gears_new.click_btn_cancel(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)

    # 点击查看鱼护
    BattlePreparePanel.SideBar.click_btn_aquarium(bp)
    AquariumFishGuardSideBarPanel.wait_for_panel_appear(bp)
    AquariumFishGuardSideBarPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看邮件
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_mail(bp)
    MailPanel.wait_for_panel_appear(bp)
    MailPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看公告
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_announcement(bp)
    LoginAnnouncementPanel.wait_for_panel_appear(bp)
    LoginAnnouncementPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 点击查看avatar
    BattlePreparePanel.SideBar.click_btn_menu(bp)
    bp.sleep(1)
    BattlePreparePanel.SideBar.click_btn_avatar(bp)
    AvatarMainPanel.wait_for_panel_appear(bp)
    AvatarMainPanel.click_btn_close(bp)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    bp.go_home()




if __name__ == '__main__':

    bp = BasePage("127.0.0.1:21503", is_mobile_device=False)
    main(bp)
    bp.connect_close()