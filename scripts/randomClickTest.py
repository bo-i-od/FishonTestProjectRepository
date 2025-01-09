import random


from common.basePage import BasePage
from common.error import InvalidOperationError
from configs.jumpData import JumpData
from panelObjs import *
from tools.commonTools import merge_list


class RegistryPanel:
    _panels = {}

    @classmethod
    def register_panel(cls, name, panel):
        cls._panels[name] = panel

    @classmethod
    def get_panel(cls, name):
        return cls._panels.get(name)

def registry_panels():
    panels = RegistryPanel()
    panels.register_panel(name="AchievementCategoryPanel", panel=AchievementCategoryPanel)
    panels.register_panel(name="AchievementGroupPanel", panel=AchievementGroupPanel)
    panels.register_panel(name="AchievementPanel", panel=AchievementPanel)
    panels.register_panel(name="AchievementPopupPanel", panel=AchievementPopupPanel)
    panels.register_panel(name="AchievementWantedPanel", panel=AchievementWantedPanel)
    panels.register_panel(name="AlbumFishDetailPanel", panel=AlbumFishDetailPanel)
    panels.register_panel(name="AquariumFishGuardSideBarPanel", panel=AquariumFishGuardSideBarPanel)
    panels.register_panel(name="AquariumFishNewPanel", panel=AquariumFishNewPanel)
    panels.register_panel(name="AquariumMainPanel", panel=AquariumMainPanel)
    panels.register_panel(name="AquariumNewSkinPanel", panel=AquariumNewSkinPanel)
    panels.register_panel(name="AquariumShopPanel", panel=AquariumShopPanel)
    panels.register_panel(name="AvatarMainPanel", panel=AvatarMainPanel)
    panels.register_panel(name="AvatarSelectPanel", panel=AvatarSelectPanel)
    panels.register_panel(name="AvatarTipsView", panel=AvatarTipsView)
    panels.register_panel(name="BaitAndRodShowPanel", panel=BaitAndRodShowPanel)
    panels.register_panel(name="BattleExplainPanel", panel=BattleExplainPanel)
    panels.register_panel(name="BattleFailedPanel", panel=BattleFailedPanel)
    panels.register_panel(name="BattlePanel", panel=BattlePanel)
    panels.register_panel(name="BattlePassBuyLevelPanel", panel=BattlePassBuyLevelPanel)
    panels.register_panel(name="BattlePassBuyLicensePanel", panel=BattlePassBuyLicensePanel)
    panels.register_panel(name="BattlePassIntroPanel", panel=BattlePassIntroPanel)
    panels.register_panel(name="BattlePassPanel", panel=BattlePassPanel)
    panels.register_panel(name="BattlePassPopPanel", panel=BattlePassPopPanel)
    panels.register_panel(name="BattlePassRewardPanel", panel=BattlePassRewardPanel)
    panels.register_panel(name="BattlePreparePanel", panel=BattlePreparePanel)
    panels.register_panel(name="BugMultiplePanel", panel=BugMultiplePanel)
    panels.register_panel(name="BuyEnergyPanel", panel=BuyEnergyPanel)
    panels.register_panel(name="CareerPanel", panel=CareerPanel)
    panels.register_panel(name="ChatPanel", panel=ChatPanel)
    panels.register_panel(name="ClubApplyPanel", panel=ClubApplyPanel)
    panels.register_panel(name="ClubCreatePanel", panel=ClubCreatePanel)
    panels.register_panel(name="ClubPanel", panel=ClubPanel)
    panels.register_panel(name="CommonItemGetPanel", panel=CommonItemGetPanel)
    panels.register_panel(name="CommonWebViewPanel", panel=CommonWebViewPanel)
    panels.register_panel(name="DailyTipsPanel", panel=DailyTipsPanel)
    panels.register_panel(name="DivisionLeaderboardPanel", panel=DivisionLeaderboardPanel)
    panels.register_panel(name="DivisionListPanel", panel=DivisionListPanel)
    panels.register_panel(name="DLCDownloadPanel", panel=DLCDownloadPanel)
    panels.register_panel(name="EntryUpdateLoading", panel=EntryUpdateLoading)
    panels.register_panel(name="EventsGiftCenterPanel", panel=EventsGiftCenterPanel)
    panels.register_panel(name="FishAlbum3DPanel", panel=FishAlbum3DPanel)
    panels.register_panel(name="FishAlbumPreviewPanel", panel=FishAlbumPreviewPanel)
    panels.register_panel(name="FishBagPanel", panel=FishBagPanel)
    panels.register_panel(name="FishCardGiftPackCustomizePanel", panel=FishCardGiftPackCustomizePanel)
    panels.register_panel(name="FishCardMultipleLevelUpPanel", panel=FishCardMultipleLevelUpPanel)
    panels.register_panel(name="FishCardMultipleLevelUpSuccessPanel", panel=FishCardMultipleLevelUpSuccessPanel)
    panels.register_panel(name="FishCardPackTipsPanel", panel=FishCardPackTipsPanel)
    panels.register_panel(name="FishCardPanel", panel=FishCardPanel)
    panels.register_panel(name="FishCardUpgradePanel", panel=FishCardUpgradePanel)
    panels.register_panel(name="FisheryGiftPackPanel", panel=FisheryGiftPackPanel)
    panels.register_panel(name="FishingTipsPanel", panel=FishingTipsPanel)
    panels.register_panel(name="FlashCardBoxesPanel", panel=FlashCardBoxesPanel)
    panels.register_panel(name="FlashCardReceivePanel", panel=FlashCardReceivePanel)
    panels.register_panel(name="FlashTipsPanel", panel=FlashTipsPanel)
    panels.register_panel(name="FriendPanel", panel=FriendPanel)
    panels.register_panel(name="GearEnhancePanel", panel=GearEnhancePanel)
    panels.register_panel(name="GearEnhanceSuccesPanel", panel=GearEnhanceSuccesPanel)
    panels.register_panel(name="GearLevelupPanel", panel=GearLevelupPanel)
    panels.register_panel(name="GearNewPanel", panel=GearNewPanel)
    panels.register_panel(name="GearPanel", panel=GearPanel)
    panels.register_panel(name="GearSkillTipsPanel", panel=GearSkillTipsPanel)
    panels.register_panel(name="Home3DPanel", panel=Home3DPanel)
    panels.register_panel(name="HomePanel", panel=HomePanel)
    panels.register_panel(name="ItemTipsPanel", panel=ItemTipsPanel)
    panels.register_panel(name="LeaderBoardPanel", panel=LeaderBoardPanel)
    panels.register_panel(name="LeaderBoardPopResultPanel", panel=LeaderBoardPopResultPanel)
    panels.register_panel(name="LoadingFisheryPanel", panel=LoadingFisheryPanel)
    panels.register_panel(name="LoadingPanel", panel=LoadingPanel)
    panels.register_panel(name="LoginAnnouncementPanel", panel=LoginAnnouncementPanel)
    panels.register_panel(name="LoginPanel", panel=LoginPanel)
    panels.register_panel(name="MailPanel", panel=MailPanel)
    panels.register_panel(name="MessageBoxPanel", panel=MessageBoxPanel)
    panels.register_panel(name="NewbieGuidePanel", panel=NewbieGuidePanel)
    panels.register_panel(name="NewbieTaskPanel", panel=NewbieTaskPanel)
    panels.register_panel(name="PartySalePanel", panel=PartySalePanel)
    panels.register_panel(name="PlayerEditNamePanel", panel=PlayerEditNamePanel)
    panels.register_panel(name="PlayerInfoPanel", panel=PlayerInfoPanel)
    panels.register_panel(name="PlayerInteractPanel", panel=PlayerInteractPanel)
    panels.register_panel(name="PlayerLevelupPanel", panel=PlayerLevelupPanel)
    panels.register_panel(name="ProgressRewardsPanel", panel=ProgressRewardsPanel)
    panels.register_panel(name="PVEMultiRoomFriendPanel", panel=PVEMultiRoomFriendPanel)
    panels.register_panel(name="PVENewbieGiftPackPanel", panel=PVENewbieGiftPackPanel)
    panels.register_panel(name="PVERuleTipsPanel", panel=PVERuleTipsPanel)
    panels.register_panel(name="PVPBattleHUDPanel", panel=PVPBattleHUDPanel)
    panels.register_panel(name="PVPHallPanel", panel=PVPHallPanel)
    panels.register_panel(name="PVPMatchPanel", panel=PVPMatchPanel)
    panels.register_panel(name="PVPResultPanel", panel=PVPResultPanel)
    panels.register_panel(name="PVPRoomInvitePanel", panel=PVPRoomInvitePanel)
    panels.register_panel(name="PVPRoomPanel", panel=PVPRoomPanel)
    panels.register_panel(name="PVPRuleTipsPanel", panel=PVPRuleTipsPanel)
    panels.register_panel(name="QuestionnairePanel", panel=QuestionnairePanel)
    panels.register_panel(name="RankFishLeaderboardPanel", panel=RankFishLeaderboardPanel)
    panels.register_panel(name="RankPanel", panel=RankPanel)
    panels.register_panel(name="Recharge1And1Panel", panel=Recharge1And1Panel)
    panels.register_panel(name="RechargeBlack5Panel", panel=RechargeBlack5Panel)
    panels.register_panel(name="RechargeEndlessPanel", panel=RechargeEndlessPanel)
    panels.register_panel(name="ResultPanel", panel=ResultPanel)
    panels.register_panel(name="RewardsPanel", panel=RewardsPanel)
    panels.register_panel(name="RewardsPreviewPanel", panel=RewardsPreviewPanel)
    panels.register_panel(name="RodMoreToOnePanel", panel=RodMoreToOnePanel)
    panels.register_panel(name="RoulettePanel", panel=RoulettePanel)
    panels.register_panel(name="SharePanel", panel=SharePanel)
    panels.register_panel(name="StorePanel", panel=StorePanel)
    panels.register_panel(name="TaskPanel", panel=TaskPanel)
    panels.register_panel(name="TournamentsInfoPanel", panel=TournamentsInfoPanel)
    panels.register_panel(name="TournamentsPanel", panel=TournamentsPanel)
    panels.register_panel(name="TreasureChestGearsShardsPanel", panel=TreasureChestGearsShardsPanel)
    panels.register_panel(name="TreasureChestPanel", panel=TreasureChestPanel)
    panels.register_panel(name="TreasureChestRewardsPanel", panel=TreasureChestRewardsPanel)
    panels.register_panel(name="WaitHintPanel", panel=WaitHintPanel)
    return panels


def randomClick(bp:BasePage):
    # 获取当前存在面板
    name_list = bp.get_name_list(element_data_list=JumpData.panel_list)
    name_list = merge_list(name_list)
    print(name_list)

    # 将注册过的面板中的操作池加在一起
    operation_pool = []
    for name in name_list:
        panel = panels.get_panel(name)
        if not panel:
            continue
        operation_pool += panel.operation_pool
    print(operation_pool)

    # 查看哪些操作当前可执行
    element_data_list = []
    for operation in operation_pool:
        element_data_list.append(operation["element_data"])
    object_id_list = bp.get_object_id_list(element_data_list=element_data_list)
    weight_list = []
    weight_total = 0

    # 将不可执行操作权重置零
    cur = 0
    while cur < len(object_id_list):
        if not object_id_list[cur]:
            weight_list.append(0)
            cur += 1
            continue
        weight = operation_pool[cur]["weight"]
        weight_list.append(weight)
        weight_total += weight
        cur += 1

    # 按权重随机出一个操作尝试执行
    operation_random = random.choices(operation_pool, weights=weight_list, k=1)[0]
    try:
        operation_random['func'](bp)
    except InvalidOperationError:
        pass


if __name__ == '__main__':
    bp = BasePage()
    panels = registry_panels()
    randomClick(bp)
