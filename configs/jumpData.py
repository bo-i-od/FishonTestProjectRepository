from configs.elementsData import ElementsData


class JumpData:
    element_data_home = ElementsData.HomePanel.HomePanel
    panel_list = [ElementsData.Panels, ElementsData.Home3DPanel.Home3DPanel]
    pop_window_set = {
        "AnniversaryEventMainPanel",
        "AquariumCommonFishChangePanel",
        "AquariumNewActivityInnerPopupPanel",
        "AquariumNewActivityPopupPanel",
        "AvatarSkinPopPanel",
        "AvatarSkinPopPanel_subType_2",
        "BaitAndRodShowPanel",
        "BattleTreasureMapPanel",
        "BattleTreasureMapDescriptionPanel",
        "ChallengeMainStageAFKPanel",
        "ChampointshipResultPopup",
        "ClubRedEnvelopePanel",
        "DailyTipsPanel",
        "DivisionChangePanel",
        "EventSignSevenDayPanel",
        "EnergyGiftPackPanel",
        "FacePopNewYear1Panel",
        "FacePopNewYear2Panel",
        "FishAlbumPreviewPanel",
        "FishBagPanel",
        "FisheryGiftPackPanel",
        "FisheryUnlockPanel",
        "FlashCardReceivePanel",
        "GachaPackPopupPanel",
        "GearEnhanceSuccesPanel",
        "KatanaPackPopupPanel",
        "LeaderBoardPopResultPanel",
        "LocationPanel",
        "LoginAnnouncementPanel",
        "PartySalePanel",
        "PlayerLevelupPanel",
        "PVENewbieGiftPackPanel",
        "PVPBoosterGiftPackPanel",
        "PVPRoomInvitePanel",
        "QuestBossTipsPanel",
        "RankFishSettleResultPanel",
        "Recharge1And1Panel",
        "RechargeBlack5Panel",
        "RechargeEndlessThanksPanel",
        "RechargeEndlessNewYearPanel",
        "RodSkinGiftPack027Panel",
        "RodSkinGiftPack030Panel",
        "RogueSelectSkillPanel",
        "StoreSuitPopupPanel",
        "StoreChristmasPopupPanel",
        "MainlineFlashCardReceivePanel",
        "MessageBoxPanel",
        "MidAutumnPackPopupPanel",
        "MonthCardPopPanel",

    }

    panel_dict = {
        "AchievementCategoryPanel": {"element_data": ElementsData.AchievementCategoryPanel.AchievementCategoryPanel, "close_path": [ElementsData.AchievementCategoryPanel.btn_close]},
        "AchievementGroupPanel": {"element_data": ElementsData.AchievementGroupPanel.AchievementGroupPanel, "close_path": [ElementsData.AchievementGroupPanel.btn_close]},
        "AchievementPanel": {"element_data": ElementsData.AchievementPanel.AchievementPanel, "open_path": [ElementsData.HomePanel.btn_achievement], "close_path": [ElementsData.AchievementPanel.btn_close]},
        "AchievementPopupPanel": {"element_data": ElementsData.AchievementPopupPanel.AchievementPopupPanel},
        "AchievementWantedPanel": {"element_data": ElementsData.AchievementWantedPanel.AchievementWantedPanel, "close_path": [ElementsData.AchievementWantedPanel.btn_close]},
        "AlbumFishDetailPanel": {"element_data": ElementsData.AlbumFishDetailPanel.AlbumFishDetailPanel, "close_path": [ElementsData.AlbumFishDetailPanel.btn_close_share_chat, ElementsData.AlbumFishDetailPanel.btn_close]},
        "AnniversaryEventMainPanel": {"element_data": ElementsData.AnniversaryEventMainPanel.AnniversaryEventMainPanel, "close_path": [ElementsData.AnniversaryEventMainPanel.btn_close]},
        "AquariumFishNewPanel": {"element_data": ElementsData.AquariumFishNewPanel.AquariumFishNewPanel, "open_path": [ElementsData.HomePanel.btn_aquarium, ElementsData.AquariumMainPanel.btn_fish]},
        "AquariumMainPanel": {"element_data": ElementsData.AquariumMainPanel.AquariumMainPanel, "open_path": [ElementsData.HomePanel.btn_aquarium], "close_path": [ElementsData.AquariumMainPanel.btn_close]},
        "AquariumNewSkinPanel": {"element_data": ElementsData.AquariumNewSkinPanel.AquariumNewSkinPanel, "close_path": [ElementsData.AquariumNewSkinPanel.btn_close]},
        "AquariumShopPanel": {"element_data": ElementsData.AquariumShopPanel.AquariumShopPanel, "close_path": [ElementsData.AquariumShopPanel.btn_close]},
        # "AquariumCommonFishChangePanel":{"element_data": ElementsData.AquariumCommonFishChangePanel.AquariumCommonFishChangePanel, "close_path":  [ElementsData.AquariumCommonFishChangePanel.btn_close]},
        # "AquariumFishPanel":{"element_data": ElementsData.AquariumFishPanel.AquariumFishPanel, "close_path": [ElementsData.AquariumFishPanel.btn_close]},
        "AquariumNewActivityInnerPopupPanel": {"element_data": ElementsData.AquariumNewActivityInnerPopupPanel.AquariumNewActivityInnerPopupPanel, "close_path": [ElementsData.AquariumNewActivityInnerPopupPanel.btn_close]},
        "AquariumNewActivityPopupPanel": {"element_data": ElementsData.AquariumNewActivityPopupPanel.AquariumNewActivityPopupPanel, "close_path": [ElementsData.AquariumNewActivityPopupPanel.btn_close]},
        "AvatarMainPanel": {"element_data": ElementsData.AvatarMainPanel.AvatarMainPanel, "close_path": [ElementsData.AvatarMainPanel.btn_close]},
        "AvatarSelectPanel": {"element_data": ElementsData.AvatarSelectPanel.AvatarSelectPanel},
        "AvatarTipsView": {"element_data": ElementsData.AvatarTipsView.AvatarTipsView, "close_path": [ElementsData.AvatarTipsView.tap_to_continue]},
        "AvatarSkinPopPanel": {"element_data": ElementsData.AvatarSkinPopPanel.AvatarSkinPopPanel, "close_path": [ElementsData.AvatarSkinPopPanel.btn_close]},
        "AvatarSkinPopPanel_subType_2": {"element_data": ElementsData.AvatarSkinPopPanel_subType_2.AvatarSkinPopPanel_subType_2, "close_path": [ElementsData.AvatarSkinPopPanel_subType_2.btn_close]},
        "ActivityCenterPanel": {"element_data": ElementsData.ActivityCenterPanel.ActivityCenterPanel, "open_path": [ElementsData.HomePanel.btn_center_new], "close_path": [ElementsData.ActivityCenterPanel.btn_close]},
        "BaitAndRodAlbumPanel": {"element_data": ElementsData.BaitAndRodAlbumPanel.BaitAndRodAlbumPanel, "open_path": [ElementsData.HomePanel.btn_gears], "close_path": [ElementsData.BaitAndRodAlbumPanel.btn_close]},
        "BaitAndRodShowPanel": {"element_data": ElementsData.BaitAndRodShowPanel.BaitAndRodShowPanel, "close_path": [ElementsData.BaitAndRodShowPanel.tap_to_continue]},
        "BattleExplainPanel": {"element_data": ElementsData.BattleExplainPanel.BattleExplainPanel, "close_path": [ElementsData.BattleExplainPanel.close]},
        "BattleFailedPanel": {"element_data": ElementsData.BattleFailedPanel.BattleFailedPanel, "close_path": [ElementsData.BattleFailedPanel.btn_again]},
        "BattlePassBuyLevelPanel": {"element_data": ElementsData.BattlePassBuyLevelPanel.BattlePassBuyLevelPanel, "close_path": [ElementsData.BattlePassBuyLevelPanel.btn_close]},
        "BattlePassBuyLicensePanel": {"element_data": ElementsData.BattlePassBuyLicensePanel.BattlePassBuyLicensePanel, "close_path": [ElementsData.BattlePassBuyLicensePanel.btn_close]},
        "BattlePassIntroPanel": {"element_data": ElementsData.BattlePassIntroPanel.BattlePassIntroPanel, "close_path": [ElementsData.BattlePassIntroPanel.panel1to2Btn, ElementsData.BattlePassIntroPanel.panel2to3Btn, ElementsData.BattlePassIntroPanel.btn_go]},
        "BattlePassPanel": {"element_data": ElementsData.BattlePassPanel.BattlePassPanel, "open_path": [ElementsData.HomePanel.btn_bp], "close_path": [ElementsData.BattlePassPanel.btn_close]},
        "BattlePassPopPanel": {"element_data": ElementsData.BattlePassPopPanel.BattlePassPopPanel, "close_path": [ElementsData.BattlePassPopPanel.btn_close]},
        "BattlePassRewardPanel": {"element_data": ElementsData.BattlePassRewardPanel.BattlePassRewardPanel, "close_path": [ElementsData.BattlePassRewardPanel.btn_close]},
        "BattlePreparePanel": {"element_data": ElementsData.BattlePreparePanel.BattlePreparePanel, "close_path": [ElementsData.BattlePreparePanel.panel_gears_switch.btn_cancel, ElementsData.BattlePreparePanel.btn_close]},
        "BattleTreasureMapPanel": {"element_data": ElementsData.BattleTreasureMapPanel.BattleTreasureMapPanel, "close_path": [ElementsData.BattleTreasureMapPanel.btn_close]},
        "BattleTreasureMapDescriptionPanel": {"element_data": ElementsData.BattleTreasureMapDescriptionPanel.BattleTreasureMapDescriptionPanel, "close_path": [ElementsData.BattleTreasureMapDescriptionPanel.btn_close]},
        "BugMultiplePanel": {"element_data": ElementsData.BugMultiplePanel.BugMultiplePanel, "close_path": [ElementsData.BugMultiplePanel.btn_cancel]},
        "BuyEnergyPanel": {"element_data": ElementsData.BuyEnergyPanel.BuyEnergyPanel, "open_path": [ElementsData.HomePanel.btn_add_100500], "close_path": [ElementsData.BuyEnergyPanel.btn_close]},
        "CareerPanel": {"element_data": ElementsData.CareerPanel.CareerPanel, "open_path": [ElementsData.HomePanel.btn_career], "close_path": [ElementsData.CareerPanel.btn_close]},
        "ChatPanel": {"element_data": ElementsData.ChatPanel.ChatPanel, "close_path": [ElementsData.ChatPanel.btn_close]},
        "ChallengeMainStageAFKPanel": {"element_data": ElementsData.ChallengeMainStageAFKPanel.ChallengeMainStageAFKPanel,"close_path": [ElementsData.ChallengeMainStageAFKPanel.btn_close]},
        "ChampointshipResultPopup": {"element_data": ElementsData.ChampointshipResultPopup.ChampointshipResultPopup, "close_path": [ElementsData.ChampointshipResultPopup.btn_close]},
        "CommonWebViewPanel": {"element_data": ElementsData.CommonWebViewPanel.CommonWebViewPanel, "close_path": [ElementsData.CommonWebViewPanel.btn_close]},
        "ClubApplyPanel": {"element_data": ElementsData.ClubApplyPanel.ClubApplyPanel, "close_path": [ElementsData.ClubApplyPanel.btn_close]},
        "ClubRedEnvelopePanel": {"element_data": ElementsData.ClubRedEnvelopePanel.ClubRedEnvelopePanel, "close_path": [ElementsData.ClubRedEnvelopePanel.btn_close]},
        "DailyTipsPanel": {"element_data": ElementsData.DailyTipsPanel.DailyTipsPanel, "close_path": [ElementsData.DailyTipsPanel.btn_close]},
        "DivisionChangePanel": {"element_data": ElementsData.DivisionChangePanel.DivisionChangePanel, "close_path": [ElementsData.DivisionChangePanel.tap_to_close]},
        "DivisionLeaderboardPanel": {"element_data": ElementsData.DivisionLeaderboardPanel.DivisionLeaderboardPanel, "open_path": [ElementsData.Home3DPanel.btn_pve, ElementsData.TournamentsPanel.btn_leaderboard], "close_path": [ElementsData.DivisionLeaderboardPanel.btn_close]},
        "DivisionListPanel": {"element_data": ElementsData.DivisionListPanel.DivisionListPanel, "close_path": [ElementsData.DivisionListPanel.btn_close]},
        "DLCDownloadPanel": {"element_data": ElementsData.DLCDownloadPanel.DLCDownloadPanel, "open_path": [ElementsData.HomePanel.btn_download], "close_path": [ElementsData.DLCDownloadPanel.btn_close, ElementsData.DLCDownloadPanel_oversea.btn_close]},
        "EnergyGiftPackPanel": {"element_data": ElementsData.EnergyGiftPackPanel.EnergyGiftPackPanel},
        "EventSignSevenDayPanel": {"element_data": ElementsData.EventSignSevenDayPanel.EventSignSevenDayPanel, "close_path": [ElementsData.EventSignSevenDayPanel.btn_receive]},
        "EventsGiftCenterPanel": {"element_data": ElementsData.EventsGiftCenterPanel.EventsGiftCenterPanel, "close_path": [ElementsData.EventsGiftCenterPanel.btn_close]},
        "FacePopNewYear1Panel": {"element_data": ElementsData.FacePopNewYear1Panel.FacePopNewYear1Panel, "close_path": [ElementsData.FacePopNewYear1Panel.btn_close]},
        "FacePopNewYear2Panel":{"element_data": ElementsData.FacePopNewYear2Panel.FacePopNewYear2Panel, "close_path": [ElementsData.FacePopNewYear2Panel.btn_close]},
        "FishAlbum3DPanel": {"element_data": ElementsData.FishAlbum3DPanel.FishAlbum3DPanel, "open_path": [ElementsData.HomePanel.btn_fishalbum], "close_path": [ElementsData.FishAlbum3DPanel.btn_close], },
        "FishBagPanel": {"element_data": ElementsData.FishBagPanel.FishBagPanel, "close_path": [ElementsData.FishBagPanel.btn_close, ElementsData.FishBagPanel.btn_next]},
        "FishAlbumPreviewPanel": {"element_data": ElementsData.FishAlbumPreviewPanel.FishAlbumPreviewPanel, "close_path": [ElementsData.FishAlbumPreviewPanel.btn_close]},
        "FishCardGiftPackCustomizePanel": {"element_data": ElementsData.FishCardGiftPackCustomizePanel.FishCardGiftPackCustomizePanel, "close_path": [ElementsData.FishCardGiftPackCustomizePanel.btn_close]},
        "FishCardPanel": {"element_data": ElementsData.FishCardPanel.FishCardPanel, "open_path": [ElementsData.HomePanel.btn_fishcard], "close_path": [ElementsData.FishCardPanel.btn_close]},
        "FlashCardReceivePanel": {"element_data": ElementsData.FlashCardReceivePanel.FlashCardReceivePanel, "close_path": [ElementsData.FlashCardReceivePanel.btn_close]},
        "FisheryUnlockPanel": {"element_data": ElementsData.FisheryUnlockPanel.FisheryUnlockPanel, "close_path": [ElementsData.FisheryUnlockPanel.btn_close]},
        "FishCardUpgradePanel": {"element_data": ElementsData.FishCardUpgradePanel.FishCardUpgradePanel, "close_path": [ElementsData.FishCardUpgradePanel.btn_close]},
        "FisheryGiftPackPanel": {"element_data": ElementsData.FisheryGiftPackPanel.FisheryGiftPackPanel, "open_path": [ElementsData.HomePanel.btn_event_location]},
        "FriendPanel": {"element_data": ElementsData.FriendPanel.FriendPanel, "open_path": [ElementsData.HomePanel.btn_friend], "close_path": [ElementsData.FriendPanel.btn_close]},
        "GachaPackPopupPanel": {"element_data": ElementsData.GachaPackPopupPanel.GachaPackPopupPanel,  "close_path": [ElementsData.GachaPackPopupPanel.btn_close]},
        "GearPanel": {"element_data": ElementsData.GearPanel.GearPanel, "open_path": [ElementsData.HomePanel.btn_gears], "close_path": [ElementsData.GearPanel.btn_close]},
        "GearLevelupPanel": {"element_data": ElementsData.GearLevelupPanel.GearLevelupPanel, "close_path": [ElementsData.GearLevelupPanel.btn_close]},
        "GearEnhancePanel": {"element_data": ElementsData.GearEnhancePanel.GearEnhancePanel, "close_path": [ElementsData.GearEnhancePanel.btn_close]},
        "GearEnhanceSuccesPanel": {"element_data": ElementsData.GearEnhanceSuccesPanel.GearEnhanceSuccesPanel, "close_path": [ElementsData.GearEnhanceSuccesPanel.btn_close]},
        "HomePanelNew": {"element_data": ElementsData.HomePanelNew.HomePanelNew, "open_path": [ElementsData.Home3DPanel.btn_mainstage],},
        "HomePanel": {"element_data": ElementsData.HomePanel.HomePanel},
        "IAAPanel": {"element_data": ElementsData.IAAPanel.IAAPanel, "close_path": [ElementsData.IAAPanel.btn_close]},
        "KatanaPackPopupPanel": {"element_data": ElementsData.KatanaPackPopupPanel.KatanaPackPopupPanel, "close_path": [ElementsData.KatanaPackPopupPanel.btn_close]},
        "LeaderBoardPopResultPanel": {"element_data": ElementsData.LeaderBoardPopResultPanel.LeaderBoardPopResultPanel, "close_path": [ElementsData.LeaderBoardPopResultPanel.btn_claim]},
        "LocationPanel": {"element_data": ElementsData.LocationPanel.LocationPanel, "close_path": [ElementsData.LocationPanel.btn_cancel]},
        "LoginPanel": {"element_data": ElementsData.LoginPanel.LoginPanel, "close_path": [ElementsData.LoginPanel.btn_login_cn, ElementsData.LoginPanel.btn_login]},
        "LoginAnnouncementPanel": {"element_data": ElementsData.LoginAnnouncementPanel.LoginAnnouncementPanel, "close_path": [ElementsData.LoginAnnouncementPanel.btn_close]},
        "MailPanel": {"element_data": ElementsData.MailPanel.MailPanel, "open_path": [ElementsData.HomePanel.btn_mail], "close_path": [ElementsData.MailPanel.btn_close]},
        "MainlineFlashCardReceivePanel":{"element_data": ElementsData.MainlineFlashCardReceivePanel.MainlineFlashCardReceivePanel, "close_path": [ElementsData.MainlineFlashCardReceivePanel.btn_close]},
        "MessageBoxPanel": {"element_data": ElementsData.MessageBoxPanel.MessageBoxPanel, "close_path": [ElementsData.MessageBoxPanel.toggle, ElementsData.MessageBoxPanel.btn_confirm]},
        "MidAutumnPackPopupPanel": {"element_data": ElementsData.MidAutumnPackPopupPanel.MidAutumnPackPopupPanel, "close_path": [ElementsData.MidAutumnPackPopupPanel.btn_close]},
        "MonthCardPopPanel": {"element_data": ElementsData.MonthCardPopPanel.MonthCardPopPanel, "close_path": [ElementsData.MonthCardPopPanel.btn_close]},
        "NewbieTaskPanel": {"element_data": ElementsData.NewbieTaskPanel.NewbieTaskPanel, "open_path": [ElementsData.HomePanel.btn_rookie3days]},
        "PartySalePanel": {"element_data": ElementsData.PartySalePanel.PartySalePanel, "close_path": [ElementsData.PartySalePanel.btn_close]},
        "PlayerInfoPanel": {"element_data": ElementsData.PlayerInfoPanel.PlayerInfoPanel, "open_path": [ElementsData.HomePanel.player_info], "close_path": [ElementsData.PlayerInfoPanel.btn_close_additional, ElementsData.PlayerInfoPanel.btn_confirm, ElementsData.PlayerInfoPanel.Panel_PlayerCard_new.btn_close, ElementsData.PlayerInfoPanel.btn_close]},
        "PlayerLevelupPanel": {"element_data": ElementsData.PlayerLevelupPanel.PlayerLevelupPanel, "close_path": [ElementsData.PlayerLevelupPanel.tap_to_continue]},
        "PVPBoosterGiftPackPanel": {"element_data": ElementsData.PVPBoosterGiftPackPanel.PVPBoosterGiftPackPanel, "close_path": [ElementsData.PVPBoosterGiftPackPanel.btn_close]},
        "PVENewbieGiftPackPanel": {"element_data": ElementsData.PVENewbieGiftPackPanel.PVENewbieGiftPackPanel, "close_path": [ElementsData.PVENewbieGiftPackPanel.btn_close]},
        "ProgressRewardsPanel": {"element_data": ElementsData.ProgressRewardsPanel.ProgressRewardsPanel, "open_path": [ElementsData.HomePanel.btn_globa_progress], "close_path": [ElementsData.ProgressRewardsPanel.btn_close]},
        "PVPHallPanel": {"element_data": ElementsData.PVPHallPanel.PVPHallPanel, "open_path": [ElementsData.Home3DPanel.btn_pvp, ElementsData.NewbieGuidePanel.NBG_friend_duel_1_1, ElementsData.PVPResultPanel.tap_to_close], "close_path": [ElementsData.PVPHallPanel.btn_close]},
        "PVPResultPanel": {"element_data": ElementsData.PVPResultPanel.PVPResultPanel, "close_path": [ElementsData.PVPResultPanel.tap_to_close]},
        "PVPRoomInvitePanel": {"element_data": ElementsData.PVPRoomInvitePanel.PVPRoomInvitePanel, "close_path": [ElementsData.PVPRoomInvitePanel.btn_close]},
        "PVPRuleTipsPanel": {"element_data": ElementsData.PVPRuleTipsPanel.PVPRuleTipsPanel, "close_path": [ElementsData.PVPRuleTipsPanel.btn_close]},
        "QuestBossTipsPanel":{"element_data": ElementsData.QuestBossTipsPanel.QuestBossTipsPanel, "close_path": [ElementsData.QuestBossTipsPanel.QuestBossTipsPanel]},
        "QuestionnairePanel": {"element_data": ElementsData.QuestionnairePanel.QuestionnairePanel, "open_path": [ElementsData.HomePanel.btn_questionnaire], "close_path": [ElementsData.QuestionnairePanel.btn_close]},
        "RankPanel": {"element_data": ElementsData.RankPanel.RankPanel, "open_path": [ElementsData.HomePanel.btn_fishranking], "close_path": [ElementsData.RankPanel.btn_close]},
        "RankFishLeaderboardPanel": {"element_data": ElementsData.RankFishLeaderboardPanel.RankFishLeaderboardPanel, "close_path": [ElementsData.RankFishLeaderboardPanel.btn_close]},
        "RankFishSettleResultPanel": {"element_data": ElementsData.RankFishSettleResultPanel.RankFishSettleResultPanel, "close_path": [ElementsData.RankFishSettleResultPanel.btn_close]},
        "ResultPanel": {"element_data": ElementsData.ResultPanel.ResultPanel, "close_path": [ElementsData.ResultPanel.btn_claim_pve, ElementsData.ResultPanel.btn_claim_token_fish, ElementsData.ResultPanel.btn_claim_pvp]},
        "RewardsPanel": {"element_data": ElementsData.RewardsPanel.RewardsPanel, "close_path": [ElementsData.RewardsPanel.tap_to_claim]},
        "RodMoreToOnePanel": {"element_data": ElementsData.RodMoreToOnePanel.RodMoreToOnePanel, "close_path": [ElementsData.RodMoreToOnePanel.btn_close]},
        "RodSkinGiftPack027Panel": {"element_data": ElementsData.RodSkinGiftPack027Panel.RodSkinGiftPack027Panel, "close_path": [ElementsData.RodSkinGiftPack027Panel.btn_close]},
        "RodSkinGiftPack030Panel": {"element_data": ElementsData.RodSkinGiftPack030Panel.RodSkinGiftPack030Panel, "close_path": [ElementsData.RodSkinGiftPack030Panel.btn_close]},
        "RogueSelectSkillPanel":{"element_data": ElementsData.RogueSelectSkillPanel.RogueSelectSkillPanel, "close_path": [ElementsData.RogueSelectSkillPanel.skill_list, ElementsData.RogueSelectSkillPanel.btn_orange]},
        "Recharge1And1Panel": {"element_data": ElementsData.Recharge1And1Panel.Recharge1And1Panel, "open_path": [ElementsData.HomePanel.btn_1add1]},
        "RechargeBlack5Panel": {"element_data": ElementsData.RechargeBlack5Panel.RechargeBlack5Panel, "open_path": [ElementsData.HomePanel.btn_black5], "close_path": [ElementsData.EventsGiftCenterPanel.btn_close]},
        "RechargeEndlessThanksPanel": {"element_data": ElementsData.RechargeEndlessThanksPanel.RechargeEndlessThanksPanel, "open_path": [ElementsData.HomePanel.btn_events_endless_thanksgiving], "close_path": [ElementsData.RechargeEndlessThanksPanel.btn_close, ElementsData.EventsGiftCenterPanel.btn_close]},
        "RechargeEndlessNewYearPanel": {"element_data": ElementsData.RechargeEndlessNewYearPanel.RechargeEndlessNewYearPanel, "open_path": [ElementsData.HomePanel.btn_events_endless_newyear], "close_path": [ElementsData.RechargeEndlessNewYearPanel.btn_close, ElementsData.EventsGiftCenterPanel.btn_close]},
        "RoulettePanel": {"element_data": ElementsData.RoulettePanel.RoulettePanel, "open_path": [ElementsData.Home3DPanel.btn_pvp, ElementsData.PVPHallPanel.btn_turntable], "close_path": [ElementsData.RoulettePanel.btn_close]},
        "StoreSuitPopupPanel": {"element_data": ElementsData.StoreSuitPopupPanel.StoreSuitPopupPanel, "close_path": [ElementsData.StoreSuitPopupPanel.btn_close]},
        "StoreChristmasPopupPanel": {"element_data": ElementsData.StoreChristmasPopupPanel.StoreChristmasPopupPanel, "close_path": [ElementsData.StoreChristmasPopupPanel.btn_close]},
        "StorePanel": {"element_data": ElementsData.StorePanel.StorePanel, "open_path": [ElementsData.HomePanel.btn_store], "close_path": [ElementsData.StorePanel.btn_close]},
        "TaskFishingCareerPanel": {"element_data": ElementsData.TaskFishingCareerPanel.TaskFishingCareerPanel, "close_path": [ElementsData.TaskFishingCareerPanel.btn_close]},
        "TournamentsInfoPanel": {"element_data": ElementsData.TournamentsInfoPanel.TournamentsInfoPanel, "close_path": [ElementsData.TournamentsInfoPanel.btn_close]},
        "TreasureChestGearsShardsPanel": {"element_data": ElementsData.TreasureChestGearsShardsPanel.TreasureChestGearsShardsPanel, "close_path": [ElementsData.TreasureChestGearsShardsPanel.btn_close]},
        "TaskPanel": {"element_data": ElementsData.TaskPanel.TaskPanel, "open_path": [ElementsData.HomePanel.btn_bp, ElementsData.BattlePassRewardPanel.btn_close, ElementsData.BattlePassIntroPanel.next1to2, ElementsData.BattlePassIntroPanel.next2to3, ElementsData.BattlePassIntroPanel.btn_go, ElementsData.BattlePassPanel.btn_task], "close_path":  [ElementsData.TaskPanel.btn_close]},
        "TournamentsPanel": {"element_data": ElementsData.TournamentsPanel.TournamentsPanel, "open_path": [ElementsData.Home3DPanel.btn_pve], "close_path": [ElementsData.TournamentsPanel.btn_close]},
        "TreasureChestPanel": {"element_data": ElementsData.TreasureChestPanel.TreasureChestPanel, "open_path": [ElementsData.Home3DPanel.btn_chest], "close_path": [ElementsData.TreasureChestPanel.btn_close]},
        "TreasureChestRewardsPanel": {"element_data": ElementsData.TreasureChestRewardsPanel.TreasureChestRewardsPanel, "close_path": [ElementsData.TreasureChestRewardsPanel.btn_close]},
    }












