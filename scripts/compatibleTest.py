import random

from common.basePage import BasePage
from netMsg import fishingMsg
from panelObjs.AlbumFishDetailPanel import AlbumFishDetailPanel
from panelObjs.AvatarSelectPanel import AvatarSelectPanel
from panelObjs.BattleFailedPanel import BattleFailedPanel
from panelObjs.BattlePanel import BattlePanel
from panelObjs.BattlePassBuyLevelPanel import BattlePassBuyLevelPanel
from panelObjs.BattlePassBuyLicensePanel import BattlePassBuyLicensePanel
from panelObjs.BattlePassIntroPanel import BattlePassIntroPanel
from panelObjs.BattlePassPopPanel import BattlePassPopPanel
from panelObjs.BattlePassRewardPanel import BattlePassRewardPanel
from panelObjs.BattlePreparePanel import BattlePreparePanel
from panelObjs.BuyEnergyPanel import BuyEnergyPanel
from panelObjs.DivisionLeaderboardPanel import DivisionLeaderboardPanel
from panelObjs.DivisionListPanel import DivisionListPanel
from panelObjs.DLCDownloadPanel import DLCDownloadPanel
from panelObjs.FishAlbumPreviewPanel import FishAlbumPreviewPanel
from panelObjs.FishCardMultipleLevelUpPanel import FishCardMultipleLevelUpPanel
from panelObjs.FishCardMultipleLevelUpSuccessPanel import FishCardMultipleLevelUpSuccessPanel
from panelObjs.HomePanel import HomePanel
from panelObjs.LeaderBoardPanel import LeaderBoardPanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.LoadingPanel import LoadingPanel
from panelObjs.MailPanel import MailPanel
from panelObjs.MessageBoxPanel import MessageBoxPanel
from panelObjs.NewbieTaskPanel import NewbieTaskPanel
from panelObjs.PartySalePanel import PartySalePanel
from panelObjs.PlayerEditNamePanel import PlayerEditNamePanel
from panelObjs.PlayerInfoPanel import PlayerInfoPanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from panelObjs.ProgressRewardsPanel import ProgressRewardsPanel
from panelObjs.PVPBattleHUDPanel import PVPBattleHUDPanel
from panelObjs.PVPHallPanel import PVPHallPanel
from panelObjs.PVPMatchPanel import PVPMatchPanel
from panelObjs.PVPResultPanel import PVPResultPanel
from panelObjs.PVPRuleTipsPanel import PVPRuleTipsPanel
from panelObjs.QuestionnairePanel import QuestionnairePanel
from panelObjs.RodMoreToOnePanel import RodMoreToOnePanel
from panelObjs.RoulettePanel import RoulettePanel
from panelObjs.SharePanel import SharePanel
from panelObjs.TaskPanel import TaskPanel
from panelObjs.TournamentsInfoPanel import TournamentsInfoPanel
from panelObjs.TournamentsPanel import TournamentsPanel
from panelObjs.TreasureChestGearsShardsPanel import TreasureChestGearsShardsPanel
from panelObjs.TreasureChestPanel import TreasureChestPanel
from panelObjs.TreasureChestRewardsPanel import TreasureChestRewardsPanel
from scripts import guideTest, playerInfoTest
from panelObjs.PlayerSettingPanel import PlayerSettingPanel
from panelObjs.FishAlbum3DPanel import FishAlbum3DPanel
from panelObjs.StorePanel import StorePanel
from panelObjs.BaitAndRodShowPanel import BaitAndRodShowPanel
from panelObjs.RewardsPanel import RewardsPanel
from panelObjs.FishBagPanel import FishBagPanel
from panelObjs.GearPanel import GearPanel
from panelObjs.GearLevelupPanel import GearLevelupPanel
from panelObjs.GearEnhanceSuccesPanel import GearEnhanceSuccesPanel
from panelObjs.GearEnhancePanel import GearEnhancePanel
from panelObjs.FishCardPanel import FishCardPanel
from panelObjs.FishCardUpgradePanel import FishCardUpgradePanel
from panelObjs.FishCardGiftPackCustomizePanel import FishCardGiftPackCustomizePanel
from panelObjs.AchievementPanel import AchievementPanel
from panelObjs.AchievementGroupPanel import AchievementGroupPanel
from panelObjs.AchievementWantedPanel import AchievementWantedPanel
from panelObjs.AchievementCategoryPanel import AchievementCategoryPanel
from panelObjs.BattlePassPanel import BattlePassPanel
from scripts import duelTest
from common import gameInit
import time


def account_init(bp: BasePage):
    count_dict = {"100000": 1234567890, "100100": 123456, "100300": 58000, "100500": 1234, "100700": 1234, "101000": 123456, "200300": 123456, "200600": 12, "207001": 123, "207002": 123, "207003": 123, "207004": 123, "207005": 123, "201001":12345, "209001": 12345}
    for c in count_dict:
        bp.set_item_count(target_count=count_dict[c], item_tpid=c)
        bp.sleep(0.2)

    cmd_list = ["allrod 1234", "fishcardall 999", "unlockfish", "progressSetPoint 123456"]
    for cmd in cmd_list:
        bp.cmd(cmd)
        bp.sleep(0.2)


def achievement(bp: BasePage):
    bp.go_to_panel("AchievementPanel")

    # 点击tips
    bp.sleep(1)
    AchievementPanel.click_btn_i(bp)
    bp.sleep(0.5)
    AchievementPanel.click_btn_i(bp)

    # 解锁
    position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(position_list[1])
    bp.sleep(0.5)
    bp.click_position([0.5, 0.1])
    bp.sleep(0.5)

    # 点击minitask
    AchievementPanel.click_task_mini(bp)
    bp.sleep(1)

    # 领取奖励
    AchievementGroupPanel.click_btn_collect(bp)
    bp.sleep(0.5)

    # 查看奖励预览
    AchievementGroupPanel.click_box(bp)
    bp.sleep(0.5)
    bp.click_position([0.5, 0.1])
    bp.sleep(0.5)

    AchievementGroupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 解锁悬赏
    AchievementPanel.switch_tab(bp, 1)
    cur = 1
    while cur < 6:
        bp.cmd(f"mode 400301 39000{cur}")
        bp.sleep(1)
        fishingMsg.fish(bp, [{"spot_id": f"40030103", "times": 1}])
        cur += 1
    bp.sleep(1)

    # 解锁
    position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(position_list[0])
    bp.sleep(1)

    # 进入
    bp.click_position(position_list[0])
    bp.sleep(1)

    reward_position_list = AchievementWantedPanel.get_reward_position_list(bp)
    bp.click_position(reward_position_list[len(reward_position_list) - 1])
    bp.sleep(0.5)
    bp.click_position([0.5, 0.1])
    bp.sleep(0.5)

    # 解锁
    wanted_position_list = AchievementWantedPanel.get_wanted_position_list(bp)
    bp.click_position(wanted_position_list[0])
    bp.sleep(1)

    # 进入
    bp.click_position(wanted_position_list[0])
    bp.sleep(1)

    # 退出
    AlbumFishDetailPanel.click_btn_share(bp)
    bp.sleep(1)

    SharePanel.click_btn_close(bp)
    bp.sleep(1)

    AlbumFishDetailPanel.click_btn_close(bp)
    bp.sleep(1)

    bp.sleep(1)
    AchievementWantedPanel.click_btn_close(bp)

    # 解锁鱼种
    AchievementPanel.switch_tab(bp, 2)
    bp.sleep(1)

    # 解锁
    position_list = AchievementPanel.get_achievement_position_list(bp)
    bp.click_position(position_list[0])
    bp.sleep(1)

    # 进入
    bp.click_position(position_list[0])
    bp.sleep(1)

    reward_position_list = AchievementCategoryPanel.get_reward_position_list(bp)
    bp.click_position(reward_position_list[len(reward_position_list) - 1])
    bp.sleep(0.5)
    bp.click_position([0.5, 0.1])
    bp.sleep(0.5)

    AchievementCategoryPanel.click_btn_close(bp)

    bp.go_home()


def aquarium(bp: BasePage):
    # 进入水族箱
    bp.go_to_panel("AquariumPanel")
    bp.sleep(3)

    # # 跳转商城
    # AquariumPanel.click_btn_add_100100(bp)
    # bp.sleep(1)
    # StorePanel.click_btn_close(bp)
    # bp.sleep(1)

    # 点宝箱看奖励预览
    AquariumPanel.click_rewards(bp)
    bp.sleep(1)
    bp.click_position([0.5, 0.1])

    # 点击建造
    AquariumPanel.click_btn_build(bp)
    bp.sleep(1)

    # 点击建筑
    build_lv_position_list = AquariumBuildMainPanel.get_build_lv_position_list(bp)
    while build_lv_position_list:
        bp.click_position(build_lv_position_list[0])
        bp.sleep(1)
        build_lv_position_list = AquariumBuildMainPanel.get_build_lv_position_list(bp)



    # 切换到更换皮肤
    AquariumBuildPanel.switch_tab(bp, 1)
    bp.sleep(1)

    # # 跳转商城返回
    # AquariumBuildPanel.click_btn_add_100100(bp)
    # bp.sleep(1)
    # StorePanel.click_btn_close(bp)
    # bp.sleep(1)

    # 返回水族箱主界面
    AquariumBuildPanel.click_btn_close(bp)
    bp.sleep(1)
    AquariumBuildMainPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点击放鱼
    AquariumPanel.click_btn_fish(bp)
    bp.sleep(1)

    # # 跳转商城返回
    # AquariumFishPanel.click_btn_add_100100(bp)
    # bp.sleep(1)
    # StorePanel.click_btn_close(bp)
    # bp.sleep(1)

    # 切换到观赏鱼
    AquariumFishPanel.switch_tab(bp, 1)
    bp.sleep(1)

    # 返回
    AquariumFishPanel.click_btn_close(bp)

    # 返回大厅
    bp.go_home()

def battle_pass(bp: BasePage):
    bp.go_to_panel("BattlePassPanel")
    bp.sleep(1)

    # 通行证介绍
    if BattlePassIntroPanel.is_panel_active(bp):
        BattlePassIntroPanel.close_battlePassIntroPanel(bp, is_test=False)
    # 通行证升级奖励
    elif BattlePassRewardPanel.is_panel_active(bp):
        BattlePassRewardPanel.click_tap_to_continue(bp)
    bp.sleep(1)

    # 通行证倒数弹窗
    if BattlePassPopPanel.is_panel_active(bp):
        BattlePassPopPanel.click_btn_close(bp)
        bp.sleep(1)

    # # 进入装备预览
    # BattlePassPanel.click_btn_detail(bp)
    # bp.sleep(1)
    # BaitAndRodShowPanel.click_tap_to_continue(bp)
    # bp.sleep(1)

    # 购买等级
    BattlePassPanel.click_btn_buy_levels(bp)
    bp.sleep(1)
    slider = BattlePassBuyLevelPanel.get_slider(bp)
    bp.swipe(point_start=[slider.slider_range[1] - slider.slider_size[0] * 0.2, slider.slider_position[1]], point_end=[slider.slider_range[1] + slider.slider_size[0] * 0.2, slider.slider_position[1]])
    BattlePassBuyLevelPanel.click_add_level(bp)
    bp.sleep(0.5)
    BattlePassBuyLevelPanel.click_btn_buy(bp)
    bp.sleep(1)
    BattlePassRewardPanel.click_tap_to_continue(bp)
    bp.sleep(1)

    # 购买通行证
    BattlePassPanel.click_btn_get_premium(bp)
    bp.sleep(1)
    BattlePassBuyLicensePanel.click_btn_close(bp)
    bp.sleep(1)

    # 银行
    BattlePassPanel.click_btn_i_gold_band(bp)
    bp.sleep(1)
    bp.click_position_base([0.9, 0.1])

    # 任务界面
    BattlePassPanel.click_btn_task(bp)
    bp.sleep(1)
    box_position_list = TaskPanel.get_box_position_list(bp)
    bp.click_position(box_position_list[len(box_position_list) - 1])
    TaskPanel.switch_tab(bp, 1)
    bp.sleep(1)
    TaskPanel.switch_tab(bp, 2)
    bp.sleep(1)

    bp.sleep(0.5)
    bp.click_position([0.5, 0.2])
    bp.sleep(0.5)
    TaskPanel.click_btn_close(bp)
    bp.sleep(1)

    # 领取全部
    BattlePassPanel.click_btn_collect_all(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    # 关闭界面
    BattlePassPanel.click_btn_close(bp)

    # 等待三选一 礼包
    while not RodMoreToOnePanel.is_panel_active(bp):
        bp.sleep(1)
    RodMoreToOnePanel.click_confirm(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

def chest(bp: BasePage):
    bp.go_to_panel("TreasureChestPanel")
    bp.sleep(1)

    # 选箱子
    TreasureChestPanel.select_box(bp, 4)
    bp.sleep(1)
    #  开箱子
    TreasureChestPanel.click_open_x(bp)
    bp.sleep(1)
    # 跳动画
    TreasureChestRewardsPanel.skip_anime(bp)
    bp.sleep(1)

    TreasureChestRewardsPanel.click_btn_close(bp)
    bp.sleep(1)
    if TreasureChestGearsShardsPanel.is_panel_active(bp):
        TreasureChestGearsShardsPanel.click_tap_to_continue(bp)
        bp.sleep(1)

    TreasureChestPanel.click_progressbar_box(bp)
    bp.sleep(1)

    # 点击奖励预览
    TreasureChestPanel.click_btn_magnifier(bp)
    bp.sleep(1)
    TreasureChestPanel.click_btn_magnifier(bp)
    bp.sleep(1)

    bp.go_home()


def division(bp: BasePage):
    bp.go_to_panel("PVPHallPanel")
    bp.sleep(1)
    PVPHallPanel.click_btn_leaderboard(bp)
    bp.sleep(1)

    # 所有段位
    DivisionLeaderboardPanel.click_btn_alldivisions(bp)
    bp.sleep(1)
    DivisionListPanel.click_btn_close(bp)
    bp.sleep(1)

    # 切到传奇排行榜
    DivisionLeaderboardPanel.switch_tab(bp, 1)
    bp.sleep(1)

    bp.go_home()


def download(bp: BasePage):
    bp.go_to_panel("DLCDownloadPanel")
    bp.sleep(1)
    DLCDownloadPanel.click_btn_close(bp)


def energy(bp: BasePage):
    bp.go_to_panel("BuyEnergyPanel")
    bp.sleep(1)
    BuyEnergyPanel.click_btn_drink(bp)
    bp.sleep(1)
    bp.go_home()


def fish_album(bp: BasePage):
    bp.go_to_panel("FishAlbum3DPanel")
    # 点击分享按钮
    FishAlbum3DPanel.click_btn_share(bp)
    bp.sleep(1)

    # 等待分享图
    bp.sleep(2)
    SharePanel.click_btn_close(bp)
    bp.sleep(1)

    # 点击更换渔场按钮
    FishAlbum3DPanel.click_btn_switch(bp)
    bp.sleep(1)

    bp.go_home()
    bp.go_to_panel("FishAlbum3DPanel")

    # 点i
    FishAlbum3DPanel.click_btn_i(bp)
    bp.sleep(0.5)
    FishAlbum3DPanel.click_btn_i(bp)
    bp.sleep(0.5)

    # 点星
    star_position_list = FishAlbum3DPanel.get_star_position_list(bp)
    bp.click_position(star_position_list[0])
    bp.sleep(0.5)
    bp.click_position(star_position_list[0])
    bp.sleep(0.5)

    # 点渔场预览
    FishAlbum3DPanel.click_btn_preview(bp)
    bp.sleep(2)
    FishAlbumPreviewPanel.click_btn_close(bp)
    bp.sleep(1)

    # 回到大厅
    bp.go_home()


def fish_card(bp: BasePage):
    bp.go_to_panel("FishCardPanel")
    # 切换tab
    FishCardPanel.switch_sub_tab(bp, 1)
    bp.sleep(1)


    # 鱼卡升级
    FishCardPanel.select_card(bp, 0)
    bp.sleep(1)
    FishCardUpgradePanel.click_btn_next(bp)
    bp.sleep(1)
    FishCardUpgradePanel.click_btn_previous(bp)
    bp.sleep(1)

    FishCardUpgradePanel.click_btn_level_up(bp)
    bp.sleep(1)

    FishCardUpgradePanel.click_btn_close(bp)
    bp.sleep(1)
    FishCardGiftPackCustomizePanel.click_btn_close(bp)
    bp.sleep(1)

    # 鱼卡一键升级
    FishCardPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    FishCardMultipleLevelUpPanel.click_btn_draw(bp)
    bp.sleep(1)
    FishCardMultipleLevelUpSuccessPanel.click_btn_close(bp)
    bp.sleep(1)

    # 规则说明
    FishCardPanel.click_btn_i(bp)
    bp.sleep(1)
    FishCardPanel.click_btn_i(bp)

    bp.go_home()


def gear(bp: BasePage):
    bp.go_to_panel("GearPanel")
    bp.sleep(1)

    # 升级面板
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_next(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_previous(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 升星面板
    GearPanel.click_btn_enhance(bp)
    bp.sleep(1)
    GearEnhancePanel.click_btn_next(bp)
    bp.sleep(1)
    GearEnhancePanel.click_btn_previous(bp)
    bp.sleep(1)

    GearEnhancePanel.click_btn_enhance(bp)
    bp.sleep(7)
    if GearEnhanceSuccesPanel.is_panel_active(bp):
        GearEnhanceSuccesPanel.click_btn_close(bp)
        bp.sleep(1)
    GearEnhancePanel.click_skill_icon(bp)
    bp.sleep(1)
    GearEnhancePanel.click_btn_close(bp)
    bp.sleep(1)

    # 筛选
    GearPanel.click_btn_filter(bp)
    available_location_position_list = GearPanel.get_available_location_position_list(bp)
    bp.click_position(available_location_position_list[1])
    rarity_position_list = GearPanel.get_rarity_position_list(bp)
    bp.click_position(rarity_position_list[1])
    GearPanel.click_btn_apply(bp)
    bp.sleep(1)

    # 点技能
    skill_position_list = GearPanel.get_skill_position_list(bp)
    r = random.randint(0, len(skill_position_list) - 1)
    bp.click_position(skill_position_list[r])

    bp.go_home()


def guide(bp: BasePage):
    guideTest.guide_rookie_test(bp)


def login(bp: BasePage):
    t = str(time.time()).split('.')
    username = t[0] + t[1]
    gameInit.login(bp, username)



def mail(bp: BasePage):
    bp.go_to_panel("MailPanel")
    bp.sleep(1)
    tab_position_list = MailPanel.get_tab_position_list(bp)
    MailPanel.switch_tab(bp, position_list=tab_position_list, index=0)
    bp.sleep(1)
    MailPanel.switch_tab(bp, position_list=tab_position_list, index=1)
    bp.sleep(1)
    MailPanel.click_btn_close(bp)

def newbie_task(bp: BasePage):
    bp.go_to_panel("NewbieTaskPanel")
    bp.sleep(1)

    # 排行榜
    NewbieTaskPanel.click_btn_leaderboard(bp)
    bp.sleep(1)
    LeaderBoardPanel.click_btn_i(bp)
    bp.sleep(1)
    LeaderBoardPanel.click_tap_to_close(bp)
    bp.sleep(1)
    LeaderBoardPanel.click_btn_close(bp)
    bp.sleep(1)

#
# 切换页签
    cur = 0
    while cur < 5:
        NewbieTaskPanel.switch_tab(bp, cur)
        bp.sleep(1)
        cur += 1

    # 购买礼包
    NewbieTaskPanel.click_btn_sale(bp)
    bp.sleep(1)

    # 回大厅
    bp.go_home()


def playerEditName(bp: BasePage):
    if not PlayerEditNamePanel.is_panel_active(bp):
        return
    # 点击确认按钮
    PlayerEditNamePanel.click_confirm(bp)
    bp.sleep(1)
    # 随机选择性别
    r = random.randint(0, 1)
    gender_icon_position_list = AvatarSelectPanel.get_gender_icon_position_list(bp)
    bp.click_position(gender_icon_position_list[r])
    bp.sleep(0.5)
    AvatarSelectPanel.click_btn_start(bp)
    bp.sleep(1)


def player_setting(bp: BasePage):
    bp.go_to_panel("PlayerInfoPanel")
    bp.sleep(1)

    PlayerInfoPanel.switch_tab(bp, 1)
    bp.sleep(1)

    # 点击鱼竿详情
    PlayerInfoPanel.click_btn_i_rod(bp)
    bp.sleep(1)
    bp.click_position([0.1, 0.5])
    bp.sleep(1)

    # 点击勋章再退出
    PlayerInfoPanel.click_btn_edit_achievement(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_btn_confirm(bp)
    bp.sleep(1)

    # 切换到数据
    PlayerInfoPanel.switch_tab(bp, 2)
    bp.sleep(1)

    # 点击设置
    PlayerInfoPanel.click_btn_setting(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_avatar(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_head_frame(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_name(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_tab_setting(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_btn_close_additional(bp)
    bp.sleep(1)

    # 切换信息
    PlayerInfoPanel.switch_tab(bp, 0)
    bp.sleep(1)

    PlayerInfoPanel.click_btn_changecamera(bp)
    bp.sleep(1)
    PlayerInfoPanel.click_btn_changecamera(bp)
    bp.sleep(1)

    # 点击战力详情
    PlayerInfoPanel.click_btn_i_rating(bp)
    bp.sleep(1)
    bp.click_position([0.1, 0.5])

    # 点击复制姓名
    PlayerInfoPanel.click_btn_copy(bp)
    bp.sleep(1)

    # 兑换码点击
    if PlayerSettingPanel.is_btn_giftcode_active(bp):
        PlayerSettingPanel.click_btn_giftcode(bp)
        bp.sleep(1)
        PlayerSettingPanel.click_btn_close_giftcode(bp)

    bp.go_home()

def pve(bp: BasePage):
    # 进入选择渔场界面
    bp.go_to_panel("TournamentsPanel")
    bp.sleep(1)

    TournamentsPanel.go_to_fishery_by_index(bp, index=0)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 点锦标赛
    BattlePreparePanel.click_btn_tournaments(bp)
    bp.sleep(1)
    TournamentsInfoPanel.switch_tab(bp, 0)
    bp.sleep(1)
    TournamentsInfoPanel.switch_tab(bp, 1)
    bp.sleep(1)
    TournamentsInfoPanel.switch_tab(bp, 2)
    bp.sleep(1)
    TournamentsInfoPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点全局进度条
    BattlePreparePanel.click_progress_info(bp)
    bp.sleep(1)
    # 如果可领奖先领
    if RewardsPanel.is_panel_active(bp):
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(1)
        BattlePreparePanel.click_progress_info(bp)
        bp.sleep(1)
    ProgressRewardsPanel.click_btn_close(bp)
    bp.sleep(1)

    # 鱼册
    BattlePreparePanel.click_btn_collection(bp)
    bp.sleep(1)
    FishAlbum3DPanel.click_btn_close(bp)
    bp.sleep(1)

    # 体力面板
    BattlePreparePanel.click_btn_add_100500(bp)
    bp.sleep(1)
    BuyEnergyPanel.click_tap_to_close(bp)
    bp.sleep(1)

    # 多倍钓点按钮
    BattlePreparePanel.click_btn_location(bp)
    bp.sleep(1)
    bp.click_position([0.5, 0.1])
    bp.sleep(1)

    # 选择装备
    BattlePreparePanel.click_gears(bp)
    bp.sleep(1)
    BattlePreparePanel.click_btn_apply(bp)
    bp.sleep(1)


    # 回选择界面
    BattlePreparePanel.click_btn_close(bp)
    bp.sleep(1)

    # 读表格数据
    table_data_object_list = bp.excelTools.get_table_data_detail(book_name="ACHIEVEMENT_WANTED.xlsm")[0]
    # 选第一个有悬赏鱼的钓场完成
    r = 0
    table_data_object = table_data_object_list[r]
    fishery = str(table_data_object["fishery"])
    TournamentsPanel.go_to_fishery_by_tpid(bp, fishery_tpid=fishery)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)


    # 超范围测试
    BattlePreparePanel.click_btn_cast(bp)
    BattleFailedPanel.click_cast_again(bp)
    bp.sleep(1)

    # 钓悬赏鱼
    AchievementWantedPanel.do_wanted(bp, table_data_object=table_data_object)


    bp.go_home()

    # 去悬赏界面
    bp.go_to_panel("AchievementPanel")
    bp.sleep(1)
    AchievementPanel.switch_tab(bp, 1)
    bp.sleep(1)

    # 选择对应的渔场
    target_icon = table_data_object["icon"]
    achievement_icon_list = AchievementPanel.get_achievement_icon_list(bp)
    achievement_position_list = AchievementPanel.get_achievement_position_list(bp)
    index = achievement_icon_list.index(target_icon)
    bp.click_position(achievement_position_list[index])
    bp.sleep(1)

    # 解锁
    wanted_position_list = AchievementWantedPanel.get_wanted_position_list(bp)
    cur = 0
    while cur < len(wanted_position_list):
        bp.click_position(wanted_position_list[cur])
        bp.sleep(1)
        cur += 1

    # 领取奖励
    AchievementWantedPanel.click_btn_rewards(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 回大厅
    bp.go_home()



def pvp(bp: BasePage):
    bp.go_to_panel("PVPHallPanel")
    bp.sleep(1)

    # # 规则介绍
    # PVPHallPanel.click_btn_i(bp)
    # bp.sleep(1)
    # PVPRuleTipsPanel.click_btn_close(bp)
    # bp.sleep(1)

    # 战斗
    PVPHallPanel.click_btn_play(bp, 0)

    # 取消对决
    PVPMatchPanel.wait_for_panel_appear(bp)
    PVPMatchPanel.click_btn_cancel(bp)
    PVPHallPanel.wait_for_panel_appear(bp)
    PVPHallPanel.click_btn_play(bp, 3)

    # 表情和投降
    PVPBattleHUDPanel.wait_for_panel_appear(bp)
    PVPBattleHUDPanel.click_btn_chat(bp)
    bp.sleep(1)
    PVPBattleHUDPanel.click_btn_surrender(bp)
    bp.sleep(1)
    MessageBoxPanel.click_btn_confirm(bp)

    # 打开战绩
    bp.sleep(3)
    PVPResultPanel.click_btn_open(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)
    bp.sleep(1)

    PVPHallPanel.click_btn_play(bp, 7)
    duelTest.pvp_fish(bp)
    bp.sleep(2)
    PVPResultPanel.click_btn_open(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)

    bp.go_home()



def roulette(bp: BasePage):
    bp.go_to_panel("PVPHallPanel")
    bp.sleep(1)
    PVPHallPanel.click_btn_turntable(bp)
    bp.sleep(1)

    # 点击玩法说明
    RoulettePanel.click_btn_i(bp)
    bp.sleep(1)
    RoulettePanel.click_btn_i(bp)

    # 点击旋转
    RoulettePanel.click_btn_spin(bp)
    bp.sleep(3)

    # 按压旋转
    RoulettePanel.press_btn_spin(bp, 1)
    bp.sleep(10)

    RoulettePanel.click_btn_spin(bp)
    bp.sleep(1)

    RoulettePanel.click_btn_close(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    bp.go_home()

def questionnaire(bp: BasePage):
    if not HomePanel.is_btn_questionnaire_exist(bp):
        return
    bp.go_to_panel("QuestionnairePanel")
    bp.sleep(1)
    QuestionnairePanel.click_btn_close(bp)


def store(bp: BasePage):
    bp.go_to_panel("StorePanel")
    bp.sleep(1)

    StorePanel.change_tab(bp, 1)
    bp.sleep(1)

    # 买月卡
    StorePanel.change_tab(bp, 2)
    bp.sleep(1)
    month_model_1_id_list = StorePanel.get_month_model_1_id_list(bp)
    btn_position_list = StorePanel.get_btn_position_list(bp, month_model_1_id_list)
    bp.click_position(btn_position_list[0])
    RewardsPanel.wait_for_panel_appear(bp)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    StorePanel.change_tab(bp, 3)
    bp.sleep(1)

    # 购买鱼竿
    StorePanel.change_tab(bp, 4)
    bp.sleep(1)
    StorePanel.click_btn_info(bp)
    BaitAndRodShowPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    bp.sleep(1)
    # gear_position_list = StorePanel.get_gear_position_list(bp)
    # cur = 1
    # while cur < len(gear_position_list):
    #     bp.click_position(gear_position_list[cur])
    #     bp.sleep(1)
    #     cur += 1

    # 鱼卡
    StorePanel.change_resource_tab(bp, 1)
    bp.sleep(1)
    StorePanel.click_btn_info(bp)
    bp.sleep(1)
    bp.click_position([0.5, 0.1])
    bp.sleep(1)
    # fish_card_position_list = StorePanel.get_fish_card_position_list(bp)
    # cur = 1
    # while cur < len(fish_card_position_list):
    #     bp.click_position(fish_card_position_list[cur])
    #     bp.sleep(1)
    #     cur += 1


    # 购买材料
    StorePanel.change_resource_tab(bp, 2)
    bp.sleep(1)
    # StorePanel.click_btn_purchase(bp)
    # RewardsPanel.wait_for_panel_appear(bp)
    # bp.sleep(1)
    # RewardsPanel.click_tap_to_claim(bp)
    # bp.sleep(1)
    # materials_position_list = StorePanel.get_materials_position_list(bp)
    # cur = 1
    # while cur < len(materials_position_list):
    #     bp.click_position(materials_position_list[cur])
    #     bp.sleep(1)
    #     cur += 1
    StorePanel.click_btn_info(bp)
    bp.sleep(1)
    bp.click_position_base([0.5, 0.1])

    # 鱼箱
    StorePanel.change_tab(bp, 5)
    bp.sleep(1)

    # 现金
    StorePanel.change_tab(bp, 6)
    bp.sleep(1)

    # 关闭商城
    bp.go_home()


def main(bp: BasePage):
    # login(bp)
    # playerEditName(bp)
    # guide(bp)
    # bp.cmd("guideskip")
    # bp.cmd("missiondone 10")
    # achievement(bp)
    # bp.cmd("levelupto 61")
    # player_setting(bp)
    # account_init(bp)
    # fish_album(bp)
    # aquarium(bp)
    # store(bp)
    # gear(bp)
    # fish_card(bp)
    # battle_pass(bp)
    # mail(bp)
    # duelTest.random_duelcup(bp, 7)
    # questionnaire(bp)
    # download(bp)
    # energy(bp)
    # newbie_task(bp)
    chest(bp)
    division(bp)
    roulette(bp)
    pve(bp)
    pvp(bp)


if __name__ == '__main__':
    bp = BasePage("192.168.111.32:20063")
    main(bp)


