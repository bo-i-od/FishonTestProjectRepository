from common.basePage import BasePage
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
from panelObjs.EventsGiftCenterPanel import EventsGiftCenterPanel
from panelObjs.LeaderBoardPanel import LeaderBoardPanel
from panelObjs.LoadingFisheryPanel import LoadingFisheryPanel
from panelObjs.MailPanel import MailPanel
from panelObjs.NewbieTaskPanel import NewbieTaskPanel
from panelObjs.PartySalePanel import PartySalePanel
from panelObjs.PlayerLevelupPanel import PlayerLevelupPanel
from panelObjs.ProgressRewardsPanel import ProgressRewardsPanel
from panelObjs.PVPHallPanel import PVPHallPanel
from panelObjs.PVPResultPanel import PVPResultPanel
from panelObjs.QuestionnairePanel import QuestionnairePanel
from panelObjs.RodMoreToOnePanel import RodMoreToOnePanel
from panelObjs.RoulettePanel import RoulettePanel
from panelObjs.TaskPanel import TaskPanel
from panelObjs.TournamentsInfoPanel import TournamentsInfoPanel
from panelObjs.TournamentsPanel import TournamentsPanel
from panelObjs.TreasureChestGearsShardsPanel import TreasureChestGearsShardsPanel
from panelObjs.TreasureChestPanel import TreasureChestPanel
from panelObjs.TreasureChestRewardsPanel import TreasureChestRewardsPanel
from scripts import guideTest
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
    count_list = [1234567890, 123456, 58000, 1234, 1234, 123456, 123456, 12, 123, 123, 123, 123, 123, 12345, 123456]
    tpid_list = ["100000", "100100", "100300", "100500", "100700", "101000", "200300", "200600", "207001", "207002", "207003", "207004", "207005", "201001", "209001"]
    cur = 0
    while cur < len(count_list):
        bp.set_item_count(target_count=count_list[cur], item_tpid=tpid_list[cur])
        bp.sleep(0.2)
        cur += 1

    cmd_list = ["allrod 1234", "fishcardall 999", "unlockfish", "progressSetPoint 123456", "aquarium"]
    for cmd in cmd_list:
        bp.cmd(cmd)
        bp.sleep(0.2)
    cur = 1
    while cur < 13:
        index = str(cur).zfill(2)
        bp.cmd(f"fishscenefish 4003{index}")
        bp.sleep(0.2)
        cur += 1
    bp.sleep(0.2)
    bp.cmd("missiondone 2")
    bp.sleep(0.2)
    bp.cmd("missiondone 3")
    bp.sleep(0.2)
    bp.cmd("missiondone 4")


def achievement(bp: BasePage):
    bp.go_to_panel("AchievementPanel")

    # 点击tips
    bp.sleep(1)
    AchievementPanel.click_btn_i(bp)
    bp.sleep(1)
    AchievementPanel.click_btn_i(bp)

    # 解锁
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    unlockable_list = list(unlockable_set)
    cur = 0
    while cur < len(unlockable_list):
        viewport.move_until_appear(viewport.item_id_list[unlockable_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlockable_list[cur]])
        cur += 1
        if cur < len(unlockable_list):
            continue
        bp.sleep(1)
        bp.click_position(position_list[unlockable_list[cur - 1]])
        bp.sleep(1)



    # 领取奖励
    cur = 0
    while cur < 10:
        AchievementGroupPanel.click_btn_collect(bp)
        bp.sleep(1)
        cur += 1

    AchievementGroupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 解锁悬赏
    AchievementPanel.switch_tab(bp, 1)
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    unlockable_list = list(unlockable_set)
    cur = 0
    while cur < len(unlockable_list):
        viewport.move_until_appear(viewport.item_id_list[unlockable_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlockable_list[cur]])
        cur += 1
        if cur < len(unlockable_list):
            continue
        bp.sleep(1)
        bp.click_position(position_list[unlockable_list[cur - 1]])
        bp.sleep(1)

    bp.sleep(1)
    AchievementWantedPanel.click_btn_close(bp)

    # 解锁鱼种
    AchievementPanel.switch_tab(bp, 2)
    locked_set, unlockable_set, unlocked_set = AchievementPanel.get_achievement_status_set(bp)
    viewport = AchievementPanel.get_viewport(bp)
    unlockable_list = list(unlockable_set)
    cur = 0
    while cur < len(unlockable_list):
        viewport.move_until_appear(viewport.item_id_list[unlockable_list[cur]])
        position_list = AchievementPanel.get_achievement_position_list(bp)
        bp.click_position(position_list[unlockable_list[cur]])
        cur += 1
        if cur < len(unlockable_list):
            continue
        bp.sleep(1)
        bp.click_position(position_list[unlockable_list[cur - 1]])
        bp.sleep(1)

    bp.sleep(1)
    AchievementCategoryPanel.click_btn_close(bp)
    bp.sleep(1)

    bp.go_home()


def aquarium(bp: BasePage):
    bp.go_to_panel("AquariumPanel")
    AquariumPanel.guide(bp)
    bp.go_home()

def battle_pass(bp: BasePage):
    bp.go_to_panel("BattlePassPanel")
    bp.sleep(1)

    # 通行证介绍
    if BattlePassIntroPanel.is_panel_active(bp):
        BattlePassIntroPanel.close_battlePassIntroPanel(bp, is_test=False)
    # 通行证升级奖励
    elif BattlePassRewardPanel.is_panel_active(bp):
        BattlePassRewardPanel.click_btn_close(bp)
    bp.sleep(1)

    # 通行证倒数弹窗
    if BattlePassPopPanel.is_panel_active(bp):
        BattlePassPopPanel.click_btn_close(bp)
        bp.sleep(1)

    # 购买等级
    BattlePassPanel.click_btn_buy(bp)
    bp.sleep(1)
    BattlePassBuyLevelPanel.click_btn_buy(bp)
    bp.sleep(1)
    BattlePassRewardPanel.click_btn_close(bp)
    bp.sleep(1)

    # 购买通行证
    BattlePassPanel.click_btn_premium(bp)
    bp.sleep(1)
    BattlePassBuyLicensePanel.click_btn_close(bp)
    bp.sleep(1)

    # 银行
    BattlePassPanel.click_btn_i_gold_bank(bp)
    bp.sleep(1)
    bp.click_position_base([0.9, 0.1])

    # 任务界面
    BattlePassPanel.click_btn_task(bp)
    bp.sleep(1)
    TaskPanel.switch_tab(bp, 1)
    bp.sleep(1)
    TaskPanel.switch_tab(bp, 2)
    bp.sleep(1)
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
    cur = 0
    while cur < 5:
        # 选箱子
        TreasureChestPanel.select_box(bp, cur)
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
            TreasureChestGearsShardsPanel.click_btn_close(bp)
            bp.sleep(1)
        cur += 1

    # 点击宝箱点
    cur = 0
    while cur < 5:
        TreasureChestPanel.click_progressbar_box(bp)
        bp.sleep(1)
        cur += 1

    # 点击奖励预览
    TreasureChestPanel.click_btn_magnifier(bp)
    bp.sleep(1)
    TreasureChestPanel.click_btn_magnifier(bp)
    bp.sleep(1)

    bp.go_home()


def division(bp: BasePage):
    bp.go_to_panel("DivisionLeaderboardPanel")
    bp.sleep(1)

    # 所有段位
    DivisionLeaderboardPanel.panel_myleague.click_btn_alldivisions(bp)
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
    BuyEnergyPanel.click_btn_cash(bp)
    bp.sleep(1)
    BuyEnergyPanel.click_btn_cash(bp)
    bp.sleep(1)
    BuyEnergyPanel.click_btn_drink(bp)
    bp.sleep(1)
    bp.go_home()


def fish_album(bp: BasePage):
    bp.go_to_panel("FishAlbum3DPanel")
    FishAlbum3DPanel.guide(bp)


def fish_card(bp: BasePage):
    FishCardPanel.guide(bp)

    # 鱼卡升级
    FishCardPanel.select_card(bp, 0)
    bp.sleep(1)
    FishCardUpgradePanel.click_btn_next(bp)
    bp.sleep(1)
    FishCardUpgradePanel.click_btn_previous(bp)
    bp.sleep(1)
    cur = 0
    while cur < 10:
        FishCardUpgradePanel.click_btn_level_up(bp)
        FishCardUpgradePanel.click_fishcard(bp)
        cur += 1
    FishCardUpgradePanel.click_btn_close(bp)
    bp.sleep(1)
    EventsGiftCenterPanel.click_btn_close(bp)
    bp.sleep(1)

    # 挨个点击渔场
    cur = 11
    while cur >= 0:
        FishCardPanel.switch_tab(bp, cur)
        bp.sleep(1)
        FishCardPanel.switch_sub_tab(bp, cur % 2)
        bp.sleep(1)
        cur -= 1

    # 规则说明
    FishCardPanel.click_btn_i(bp)
    bp.sleep(1)
    FishCardPanel.click_btn_i(bp)

    bp.go_home()


def gear(bp: BasePage):
    bp.go_to_panel("GearPanel")
    bp.sleep(1)
    rodlist_viewport = GearPanel.get_rodlist_viewport(bp)
    rod_count = len(rodlist_viewport.item_id_list)
    rodlist_viewport.move_until_appear(rodlist_viewport.item_id_list[rod_count - 1])

    # 升级面板
    GearPanel.click_btn_upgrade(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_next(bp)
    bp.sleep(1)
    GearLevelupPanel.click_btn_previous(bp)
    bp.sleep(1)
    cur = 0
    while cur < 10:
        GearLevelupPanel.click_btn_upgrade(bp)

        bp.sleep(1)
        cur += 1
    GearLevelupPanel.click_btn_close(bp)
    bp.sleep(1)

    # 升星面板
    GearPanel.click_btn_enhance(bp)
    bp.sleep(1)
    GearEnhancePanel.click_btn_next(bp)
    bp.sleep(1)
    GearEnhancePanel.click_btn_previous(bp)
    bp.sleep(1)
    cur = 0
    while cur < 4:
        GearEnhancePanel.click_btn_enhance(bp)
        bp.sleep(5)
        GearEnhanceSuccesPanel.click_btn_close(bp)
        cur += 1
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
    MailPanel.switch_tab(bp, index=0)
    bp.sleep(1)
    MailPanel.switch_tab(bp, index=1)
    bp.sleep(1)
    MailPanel.click_btn_close(bp)

def newbie_task(bp: BasePage):
    bp.go_to_panel("NewbieTaskPanel")
    bp.sleep(1)

    # 介绍
    NewbieTaskPanel.click_btn_i(bp)
    bp.sleep(1)
    NewbieTaskPanel.click_tap_to_close(bp)
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
# # 切换页签
#     NewbieTaskPanel.switch_tab(bp, 1)
#     bp.sleep(1)
#     NewbieTaskPanel.switch_tab(bp, 2)
#     bp.sleep(1)
#     NewbieTaskPanel.switch_tab(bp, 3)
#     bp.sleep(1)

    # 购买礼包
    NewbieTaskPanel.click_btn_sale(bp)
    bp.sleep(1)
    PartySalePanel.click_btn_close(bp)

    # 回大厅
    bp.go_home()

def playerEditName(bp: BasePage):
    guideTest.player_edit_name_test(bp)


def player_setting(bp: BasePage):
    bp.go_to_panel("PlayerSettingPanel")
    bp.sleep(1)
    # setting面板
    PlayerSettingPanel.click_tab_settings(bp)
    PlayerSettingPanel.set_slider_music(bp, 0.5)
    PlayerSettingPanel.set_slider_sound(bp, 0.5)
    PlayerSettingPanel.set_options_graphics(bp, 2)
    PlayerSettingPanel.set_options_frame(bp, 1)
    PlayerSettingPanel.set_options_joystick(bp, 1)
    PlayerSettingPanel.set_options_vibration(bp, 0)

    # player面板点击
    PlayerSettingPanel.click_tab_player(bp)
    bp.sleep(1)
    PlayerSettingPanel.click_edit_info(bp)
    # PlayerSettingPanel.click_tab_banner(bp)
    PlayerSettingPanel.click_tab_name(bp)
    PlayerSettingPanel.click_tab_badge(bp)
    PlayerSettingPanel.close_edit_profile(bp)

    # # language面板
    # PlayerSettingPanel.click_tab_language(bp)
    # bp.sleep(1)
    # language_title_position_list = PlayerSettingPanel.get_language_title_position_list(bp)
    # bp.click_position(language_title_position_list[0])
    # bp.sleep(1)
    # PlayerSettingPanel.click_btn_save_language(bp)

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
    BattlePreparePanel.panel_pve_prepare.click_btn_tournaments(bp)
    bp.sleep(1)
    TournamentsInfoPanel.switch_tab(bp, 1)
    bp.sleep(1)
    TournamentsInfoPanel.switch_tab(bp, 2)
    bp.sleep(1)
    TournamentsInfoPanel.click_btn_close(bp)
    bp.sleep(1)

    # 点全局进度条
    BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.click_progress_info(bp)
    bp.sleep(1)
    # 如果可领奖先领
    if RewardsPanel.is_panel_active(bp):
        RewardsPanel.click_tap_to_claim(bp)
        bp.sleep(1)
        BattlePreparePanel.panel_pve_prepare.panel_tournaments_mini.click_progress_info(bp)
        bp.sleep(1)
    ProgressRewardsPanel.click_btn_close(bp)
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
    TournamentsPanel.go_to_fishery_by_id(bp, fishery_id=fishery)
    LoadingFisheryPanel.wait_until_panel_disappear(bp)

    # 进行刺鱼引导
    bp.cmd("mode 400301 301013")
    BattlePreparePanel.click_btn_cast(bp)
    BattlePanel.hook_guide(bp)

    # 超范围测试
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

    # 解锁
    wanted_position_list = AchievementWantedPanel.get_wanted_position_list(bp)
    cur = 0
    while cur < len(wanted_position_list):
        bp.click_position(wanted_position_list[cur])
        bp.sleep(1)
        cur += 1

    # 领取奖励 对比奖励数量
    AchievementWantedPanel.click_btn_rewards(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)

    # 回大厅
    bp.go_home()



def pvp(bp: BasePage):
    duelTest.set_duelcup_random(bp, 7)
    bp.sleep(1)
    bp.go_to_panel("PVPHallPanel")
    bp.sleep(1)

    # # 规则介绍
    # PVPHallPanel.click_btn_i(bp)
    # bp.sleep(1)
    # PVPRuleTipsPanel.click_btn_close(bp)
    # bp.sleep(1)

    # 战斗
    PVPHallPanel.click_btn_play(bp, 7)
    duelTest.pvp_fish(bp)
    bp.sleep(2)
    PVPResultPanel.click_btn_open(bp)
    bp.sleep(1)
    PVPResultPanel.click_tap_to_click(bp)

    bp.go_home()



def roulette(bp: BasePage):
    bp.go_to_panel("RoulettePanel")
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
    bp.sleep(20)

    RoulettePanel.click_btn_spin(bp)
    bp.sleep(1)

    RoulettePanel.click_btn_close(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)

    bp.go_home()

def questionnaire(bp: BasePage):
    bp.go_to_panel("QuestionnairePanel")
    bp.sleep(1)
    QuestionnairePanel.click_btn_close(bp)


def store(bp: BasePage):
    bp.go_to_panel("StorePanel")
    bp.sleep(1)

    # 购买鱼竿
    StorePanel.change_tab(bp, 1)
    bp.sleep(1)
    StorePanel.click_btn_purchase(bp)
    BaitAndRodShowPanel.wait_for_panel_appear(bp)
    BaitAndRodShowPanel.click_tap_to_continue(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)
    gear_position_list = StorePanel.get_gear_position_list(bp)
    cur = 1
    while cur < len(gear_position_list):
        bp.click_position(gear_position_list[cur])
        bp.sleep(1)
        cur += 1

    # 购买鱼卡
    StorePanel.change_resource_tab(bp, 1)
    bp.sleep(1)
    StorePanel.click_btn_purchase(bp)
    bp.sleep(1)
    if RewardsPanel.is_panel_active(bp):
        RewardsPanel.wait_for_panel_appear(bp)
        bp.sleep(1)
        RewardsPanel.click_tap_to_claim(bp)
    FishBagPanel.wait_for_panel_appear(bp)
    bp.clear_popup()
    bp.sleep(1)
    if RewardsPanel.is_panel_active(bp):
        RewardsPanel.wait_for_panel_appear(bp)
        bp.sleep(1)
        RewardsPanel.click_tap_to_claim(bp)
    StorePanel.click_btn_info(bp)
    bp.sleep(1)
    StorePanel.click_btn_info(bp)

    bp.sleep(1)
    fish_card_position_list = StorePanel.get_fish_card_position_list(bp)
    cur = 1
    while cur < len(fish_card_position_list):
        bp.click_position(fish_card_position_list[cur])
        bp.sleep(1)
        cur += 1


    # 购买材料
    StorePanel.change_resource_tab(bp, 2)
    bp.sleep(1)
    StorePanel.click_btn_purchase(bp)
    RewardsPanel.wait_for_panel_appear(bp)
    bp.sleep(1)
    RewardsPanel.click_tap_to_claim(bp)
    bp.sleep(1)
    materials_position_list = StorePanel.get_materials_position_list(bp)
    cur = 1
    while cur < len(materials_position_list):
        bp.click_position(materials_position_list[cur])
        bp.sleep(1)
        cur += 1
    StorePanel.click_btn_info(bp)
    bp.sleep(1)
    bp.click_position_base([0.5, 0.1])

    # 鱼箱
    StorePanel.change_tab(bp, 2)
    bp.sleep(1)
    cur = 0
    while cur < 8:
        StorePanel.click_btn_refresh(bp)
        bp.sleep(1)
        cur += 1

    # 现金
    StorePanel.change_tab(bp, 3)
    bp.sleep(1)

    # 关闭商城
    bp.go_home()



def main(bp: BasePage):
    login(bp)
    playerEditName(bp)
    guide(bp)
    bp.cmd_list(["levelupto 99", "missiondone 10"])

    player_setting(bp)
    PlayerLevelupPanel.wait_for_panel_appear(bp)
    bp.clear_popup()
    account_init(bp)
    fish_album(bp)
    aquarium(bp)
    store(bp)
    gear(bp)
    fish_card(bp)
    achievement(bp)
    battle_pass(bp)
    mail(bp)
    questionnaire(bp)
    download(bp)
    energy(bp)
    newbie_task(bp)
    chest(bp)
    division(bp)
    roulette(bp)
    pve(bp)
    pvp(bp)


if __name__ == '__main__':
    bp = BasePage("127.0.0.1:21503", is_mobile_device=True)
    account_init(bp)
    # main(bp)
