from configs.elementsData import ElementsData

class JumpData:
    pop_window_set = {
        "AquariumCommonFishChangePanel",
        "AvatarSkinPopPanel",
        "AvatarSkinPopPanel_subType_2",
        "BaitAndRodShowPanel",
        "ChampointshipResultPopup",
        "DailyTipsPanel",
        "DivisionChangePanel",
        "EventSignSevenDayPanel",
        "FishAlbumPreviewPanel",
        "FishBagPanel",
        "FisheryGiftPackPanel",
        "FisheryUnlockPanel",
        "FlashCardReceivePanel",
        "LeaderBoardPopResultPanel",
        "LoginAnnouncementPanel",
        "PartySalePanel",
        # "NBG_prepare_2_album_01(Clone)",
        "PlayerLevelupPanel",
        "PVENewbieGiftPackPanel",
        "PVPBoosterGiftPackPanel",
        "RankFishSettleResultPanel",
        "Recharge1And1Panel",
        "RodSkinGiftPack027Panel",
        "RodSkinGiftPack030Panel",
        "BattleTreasureMapPanel",
        "MessageBoxPanel",
        "MidAutumnPackPopupPanel",
        "MonthCardPopPanel",
    }

    panel_close_dict = {
        "AchievementGroupPanel": [ElementsData.AchievementGroup.btn_close],
        "AchievementWantedPanel": [ElementsData.AchievementWanted.btn_close],
        "AchievementCategoryPanel": [ElementsData.AchievementCategory.btn_close],
        "AchievementPanel": [ElementsData.Achievement.btn_close],
        "ActivityCenterPanel": [ElementsData.ActivityCenter.btn_close],
        "AquariumPanel": [ElementsData.Aquarium.btn_close],
        "AquariumCommonFishChangePanel": [ElementsData.AquariumCommonFishChange.btn_close],
        "AquariumFishPanel":[ElementsData.AquariumFish.btn_close],
        "AvatarMainPanel":[ElementsData.AvatarMain.btn_close],
        "AvatarSkinPopPanel":[ElementsData.AvatarSkinPop.btn_close],
        "AvatarSkinPopPanel_subType_2":[ElementsData.AvatarSkinPop2.btn_close],
        "BaitAndRodAlbumPanel": [ElementsData.BaitAndRodAlbum.btn_close],
        "BaitAndRodShowPanel": [ElementsData.BaitAndRodShow.tap_to_continue],
        "BattleExplainPanel": [ElementsData.BattleExplain.close],
        "BattleFailedPanel": [ElementsData.BattleFailed.btn_again],
        "BattlePassBuyLevelPanel": [ElementsData.BattlePassBuyLevel.btn_close],
        "BattlePassBuyLicensePanel": [ElementsData.BattlePassBuyLicense.btn_close],
        "BattlePassIntroPanel": [ElementsData.BattlePassIntro.panel1to2Btn, ElementsData.BattlePassIntro.panel2to3Btn,ElementsData.BattlePassIntro.btn_go],
        "BattlePassPanel": [ElementsData.BattlePass.btn_close],
        "BattlePassPopPanel": [ElementsData.BattlePassPop.btn_close],
        "BattlePassRewardPanel": [ElementsData.BattlePassReward.btn_close],
        "BattlePreparePanel": [ElementsData.BattlePrepare.btn_close],
        "BattleTreasureMapPanel":[ElementsData.BattleTreasureMap.btn_close],
        "BuyEnergyPanel": [ElementsData.BuyEnergy.btn_close],
        "CareerPanel": [ElementsData.Career.btn_close],
        "ChampointshipResultPopup": [ElementsData.ChampointshipResult.btn_close],
        "CommonWebViewPanel":[ElementsData.CommonWebView.btn_close],
        "DailyTipsPanel": [ElementsData.DailyTips.btn_close],
        "DivisionChangePanel": [ElementsData.DivisionChange.tap_to_close],
        "DivisionLeaderboardPanel":[ElementsData.DivisionLeaderboard.btn_close],
        "DivisionListPanel":[ElementsData.DivisionList.btn_close],
        "DLCDownloadPanel": [ElementsData.DLCDownload.btn_close],
        "EventSignSevenDayPanel":[ElementsData.EventSignSevenDay.btn_receive, ElementsData.Rewards.tap_to_claim],
        "EventsGiftCenterPanel": [ElementsData.EventsGiftCenter.btn_close],
        "FishAlbum3DPanel":[ElementsData.FishAlbum3D.btn_close],
        "FishAlbumPreviewPanel": [ElementsData.FishAlbumPreview.btn_close],
        "FishBagPanel": [ElementsData.FishBag.btn_close, ElementsData.FishBag.btn_next],
        # "FishBagPanel": [ElementsData.FishBag.btn_next],
        "FishCardGiftPackCustomizePanel": [ElementsData.FishCardGiftPackCustomize.btn_close],
        "FishCardPanel": [ElementsData.FishCard.btn_close],
        "FlashCardReceivePanel": [ElementsData.FlashCardReceive.btn_close],
        "FisheryGiftPackPanel": [ElementsData.EventsGiftCenter.btn_close],
        "FisheryUnlockPanel": [ElementsData.FisheryUnlock.btn_close],
        "FishCardUpgradePanel": [ElementsData.FishCardUpgrade.btn_close],
        "FriendPanel": [ElementsData.Friend.btn_close],
        "GearPanel": [ElementsData.Gear.btn_close],
        "GearLevelupPanel":[ElementsData.GearLevelup.btn_close],
        "GearEnhancePanel":[ElementsData.GearEnhance.btn_close],
        "GearEnhanceSuccesPanel":[ElementsData.GearEnhanceSucces.btn_close],
        "IAAPanel": [ElementsData.IAA.btn_close],
        "LeaderBoardPopResultPanel": [ElementsData.LeaderBoardPopResult.btn_claim],
        "LoginPanel": [ElementsData.Login.btn_login_cn, ElementsData.Login.btn_login],
        "LoginAnnouncementPanel":[ElementsData.LoginAnnouncement.btn_close],
        "MailPanel": [ElementsData.Mail.btn_close],
        "MessageBoxPanel": [ElementsData.MessageBox.toggle, ElementsData.MessageBox.btn_confirm],
        "MidAutumnPackPopupPanel":[ElementsData.MidAutumnPackPopup.btn_close],
        "MonthCardPopPanel": [ElementsData.MonthCardPop.btn_close],
        # "NBG_prepare_2_album_01(Clone)": [ElementsData.NewbieGuide.NBG_prepare_2_album_01, ElementsData.NewbieGuide.NBG_prepare_2_album_02, ElementsData.NewbieGuide.NBG_prepare_2_album_03, ElementsData.NewbieGuide.NBG_album_01, ElementsData.NewbieGuide.NBG_album_02, ElementsData.NewbieGuide.NBG_album_03, ElementsData.NewbieGuide.NBG_prepare_weak_01],
        "PartySalePanel":[ElementsData.PartySale.btn_close],
        "PlayerInfoPanel": [ElementsData.PlayerInfo.btn_close_additional, ElementsData.PlayerInfo.btn_confirm, ElementsData.PlayerInfo.btn_close],
        "PlayerSettingPanel": [ElementsData.PlayerSetting.btn_close_additional, ElementsData.PlayerSetting.btn_close],
        "PlayerLevelupPanel": [ElementsData.PlayerLevelup.tap_to_continue],
        "PVPBoosterGiftPackPanel": [ElementsData.PVPBoosterGiftPack.btn_close],
        "ProgressRewardsPanel":[ElementsData.ProgressRewards.btn_close],
        "PVENewbieGiftPackPanel":[ElementsData.PVENewbieGiftPack.btn_close],
        "PVPHallPanel": [ElementsData.NewbieGuide.NBG_friend_duel_1_1, ElementsData.PVPHall.btn_close],
        "PVPResultPanel": [ElementsData.PVPResult.tap_to_close],
        "PVPRuleTipsPanel": [ElementsData.PVPRuleTips.btn_close],
        "QuestionnairePanel": [ElementsData.Questionnaire.btn_close],
        "RankPanel": [ElementsData.Rank.btn_close],
        "RankFishLeaderboardPanel": [ElementsData.RankFishLeaderboard.btn_close],
        "RankFishSettleResultPanel": [ElementsData.RankFishSettleResult.btn_close],
        "Recharge1And1Panel": [ElementsData.Recharge1And1.btn_close],
        "RechargeBlack5Panel": [ElementsData.RechargeBlack5.btn_close],
        "RechargeEndlessPanel": [ElementsData.RechargeEndless.btn_close],
        "ResultPanel": [ElementsData.Result.btn_claim],
        "RewardsPanel": [ElementsData.Rewards.tap_to_claim],
        "RodMoreToOnePanel": [ElementsData.RodMoreToOne.btn_close],
        "RodSkinGiftPack027Panel": [ElementsData.RodSkinGiftPack027.btn_close],
        "RodSkinGiftPack030Panel":[ElementsData.RodSkinGiftPack030.btn_close],
        "RoulettePanel": [ElementsData.Roulette.btn_close],
        "StorePanel": [ElementsData.Store.btn_close],
        "TaskFishingCareerPanel": [ElementsData.TaskFishingCareer.btn_close],
        "TaskPanel": [ElementsData.Task.btn_close],
        "TournamentsPanel": [ElementsData.Tournaments.btn_close],
        "TreasureChestGearsShardsPanel": [ElementsData.TreasureChestGearsShards.btn_close],
        "TreasureChestPanel": [ElementsData.TreasureChest.btn_close],
        "TreasureChestRewardsPanel": [ElementsData.TreasureChestRewards.btn_close]
    }

    panel_dict = {
        "AchievementPanel": {"element_data": ElementsData.Achievement.AchievementPanel, "open_path": [ElementsData.Home.btn_achievement], },
        "AquariumPanel": {"element_data": ElementsData.Aquarium.AquariumPanel, "open_path": [ElementsData.Home.btn_aquarium]},
        "ActivityCenterPanel": {"element_data": ElementsData.ActivityCenter.ActivityCenterPanel, "open_path": [ElementsData.Home.btn_center_new]},
        "BattlePassPanel": {"element_data": ElementsData.BattlePass.BattlePassPanel, "open_path": [ElementsData.Home.btn_bp]},
        "BaitAndRodAlbumPanel": {"element_data": ElementsData.BaitAndRodAlbum.BaitAndRodAlbumPanel, "open_path": [ElementsData.Home.btn_gears]},
        "BuyEnergyPanel": {"element_data": ElementsData.BuyEnergy.BuyEnergyPanel, "open_path": [ElementsData.Home.btn_add_100500]},
        "CareerPanel": {"element_data": ElementsData.Career.CareerPanel, "open_path": [ElementsData.Home.btn_career]},
        "DivisionLeaderboardPanel": {"element_data": ElementsData.DivisionLeaderboard.DivisionLeaderboardPanel, "open_path": [ElementsData.Home.btn_pve, ElementsData.Tournaments.btn_leaderboard]},
        "DLCDownloadPanel": {"element_data": ElementsData.DLCDownload.DLCDownloadPanel, "open_path": [ElementsData.Home.btn_download]},
        "DLCDownloadPanel_oversea": {"element_data": ElementsData.DLCDownload_oversea.DLCDownloadPanel, "open_path": [ElementsData.Home.btn_download]},
        "FishAlbum3DPanel": {"element_data": ElementsData.FishAlbum3D.FishAlbum3DPanel, "open_path": [ElementsData.Home.btn_fishalbum]},
        "FishCardPanel": {"element_data": ElementsData.FishCard.FishCardPanel, "open_path": [ElementsData.Home.btn_fishcard]},
        "FisheryGiftPackPanel": {"element_data": ElementsData.FisheryGiftPack.FisheryGiftPackPanel, "open_path": [ElementsData.Home.btn_event_location]},
        "FriendPanel": {"element_data": ElementsData.Friend.FriendPanel, "open_path": [ElementsData.Home.btn_friend]},
        "GearPanel": {"element_data": ElementsData.Gear.GearPanel, "open_path": [ElementsData.Home.btn_gears]},
        "MailPanel": {"element_data": ElementsData.Mail.MailPanel, "open_path": [ElementsData.Home.btn_mail]},
        "NewbieTaskPanel": {"element_data": ElementsData.NewbieTask.NewbieTaskPanel, "open_path": [ElementsData.Home.btn_rookie3days]},
        "PlayerSettingPanel": {"element_data": ElementsData.PlayerSetting.PlayerSettingPanel, "open_path": [ElementsData.Home.player_info, ElementsData.PlayerInfo.btn_setting]},
        "PlayerInfoPanel": {"element_data": ElementsData.PlayerInfo.PlayerInfoPanel, "open_path": [ElementsData.Home.player_info]},
        "ProgressRewardsPanel": {"element_data": ElementsData.ProgressRewards.ProgressRewardsPanel, "open_path": [ElementsData.Home.btn_globa_progress]},
        "PVPHallPanel": {"element_data": ElementsData.PVPHall.PVPHallPanel, "open_path": [ElementsData.Home.btn_pvp, ElementsData.NewbieGuide.NBG_friend_duel_1_1]},
        "QuestionnairePanel": {"element_data": ElementsData.Questionnaire.QuestionnairePanel, "open_path": [ElementsData.Home.btn_questionnaire]},
        "RankPanel": {"element_data": ElementsData.Rank.RankPanel, "open_path": [ElementsData.Home.btn_fishranking]},
        "Recharge1And1Panel": {"element_data": ElementsData.Recharge1And1.Recharge1And1Panel, "open_path": [ElementsData.Home.btn_1add1]},
        "RechargeBlack5Panel": {"element_data": ElementsData.RechargeBlack5.RechargeBlack5Panel, "open_path": [ElementsData.Home.btn_black5]},
        "RechargeEndlessPanel": {"element_data": ElementsData.RechargeEndless.RechargeEndlessPanel, "open_path": [ElementsData.Home.btn_endless]},
        "RoulettePanel": {"element_data": ElementsData.Roulette.RoulettePanel, "open_path": [ElementsData.Home.btn_pvp, ElementsData.PVPHall.btn_turntable]},
        "StorePanel": {"element_data": ElementsData.Store.StorePanel, "open_path": [ElementsData.Home.btn_store]},
        "TaskPanel": {"element_data": ElementsData.Task.TaskPanel, "open_path": [ElementsData.Home.btn_bp,ElementsData.BattlePassReward.btn_close, ElementsData.BattlePassIntro.next1to2,  ElementsData.BattlePassIntro.next2to3, ElementsData.BattlePassIntro.btn_go, ElementsData.BattlePass.btn_task]},
        "TournamentsPanel": {"element_data": ElementsData.Tournaments.TournamentsPanel, "open_path": [ElementsData.Home.btn_pve]},
        "TreasureChestPanel": {"element_data": ElementsData.TreasureChest.TreasureChestPanel, "open_path": [ElementsData.Home.btn_chest]},
    }
