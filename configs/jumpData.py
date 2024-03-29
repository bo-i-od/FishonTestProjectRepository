from configs.elementsData import ElementsData

class JumpData:
    pop_window_set = {
        "AquariumCommonFishChangePanel",
        "BaitAndRodShowPanel",
        "ChampointshipResult",
        "DailyTipsPanel",
        "DivisionChangePanel",
        "FishBagPanel",
        "FisheryGiftPackPanel",
        "LeaderBoardPopResultPanel",
        "PlayerLevelupPanel",
        "PVPBoosterGiftPackPanel",
        "Recharge1And1Panel",
        "MessageBoxPanel"
    }

    panel_close_dict = {
        "AchievementGroupPanel": [ElementsData.AchievementGroup.btn_close],
        "AchievementPanel": [ElementsData.Achievement.btn_close],
        "AquariumPanel": [ElementsData.Aquarium.btn_close],
        "AquariumCommonFishChangePanel": [ElementsData.AquariumCommonFishChange.btn_close],
        "BaitAndRodAlbumPanel": [ElementsData.BaitAndRodAlbum.btn_close],
        "BaitAndRodShowPanel": [ElementsData.BaitAndRodShow.closeArea],
        "BattleExplainPanel": [ElementsData.BattleExplain.close],
        "BattleFailedPanel": [ElementsData.BattleFailed.btn_again],
        "BattlePassBuyLevelPanel": [ElementsData.BattlePassBuyLevel.btn_close],
        "BattlePassBuyLicensePanel": [ElementsData.BattlePassBuyLicense.btn_close],
        "BattlePassIntroPanel": [ElementsData.BattlePassIntro.panel1to2Btn, ElementsData.BattlePassIntro.panel2to3Btn,
                                 ElementsData.BattlePassIntro.btn_go],
        "BattlePassPanel": [ElementsData.BattlePass.btn_close],
        "BattlePassPopPanel": [ElementsData.BattlePassPop.btn_close],
        "BattlePassRewardPanel": [ElementsData.BattlePassReward.btn_close],
        "BattlePreparePanel": [ElementsData.BattlePrepare.btn_close],
        "BuyEnergyPanel": [ElementsData.BuyEnergy.btn_close],
        "ChampointshipResult": [ElementsData.ChampointshipResult.btn_collect],
        "DailyTipsPanel": [ElementsData.DailyTips.btn_close],
        "DivisionChangePanel": [ElementsData.DivisionChange.tap_to_close],
        "FishBagPanel": [ElementsData.FishBag.tap_to_continue],
        "FishCardGiftPackPanel": [ElementsData.FishCardGiftPack.btn_close],
        "FishCardPanel": [ElementsData.FishCard.btn_close],
        "FisheryGiftPackPanel": [ElementsData.FisheryGiftPack.btn_close],
        "FishCardUpgradePanel": [ElementsData.FishCardUpgrade.btn_close],
        "GearPanel": [ElementsData.Gear.btn_close],
        "IAAPanel": [ElementsData.IAA.btn_close],
        "LeaderBoardPopResultPanel": [ElementsData.LeaderBoardPopResult.btn_claim],
        "MailPanel": [ElementsData.Mail.btn_close],
        "MessageBoxPanel": [ElementsData.MessageBox.btn_confirm],
        "PlayerSettingPanel": [ElementsData.PlayerSetting.btn_close_additional, ElementsData.PlayerSetting.btn_close],
        "PlayerLevelupPanel": [ElementsData.PlayerLevelup.tap_to_continue],
        "PVPBoosterGiftPackPanel": [ElementsData.PVPBoosterGiftPack.btn_close],
        "ProgressRewardsPanel":[ElementsData.ProgressRewards.btn_close],
        "PVPHallPanel": [ElementsData.PVPHall.btn_close],
        "PVPResultPanel": [ElementsData.PVPResult.tap_to_close],
        "PVPRuleTipsPanel": [ElementsData.PVPRuleTipsPanel.btn_close],
        "Recharge1And1Panel": [ElementsData.Recharge1And1.btn_close],
        "RechargeBlack5Panel": [ElementsData.RechargeBlack5.btn_close],
        "RechargeEndlessPanel": [ElementsData.RechargeEndless.btn_close],
        "ResultPanel": [ElementsData.Result.btn_claim],
        "RewardsPanel": [ElementsData.Rewards.tap_to_claim],
        "RodMoreToOnePanel": [ElementsData.RodMoreToOne.btn_close],
        "RoulettePanel": [ElementsData.Roulette.btn_close],
        "StorePanel": [ElementsData.Store.btn_close],
        "TaskFishingCareerPanel": [ElementsData.TaskFishingCareer.btn_close],
        "TaskPanel": [ElementsData.Task.btn_close],
        "TournamentsPanel": [ElementsData.Tournaments.btn_close],
        "TreasureChestGearsShardsPanel": [ElementsData.TreasureChestGearsShards.btn_close],
        "TreasureChestPanel": [ElementsData.TreasureChest.btn_close],
        "TreasureChestRewardsPanel": [ElementsData.TreasureChestRewards.btn_close]
    }

    panel_open_dict = {
        "AchievementPanel": [ElementsData.Home.btn_achievement],
        "BattlePassPanel": [ElementsData.Home.btn_bp],
        "BaitAndRodAlbumPanel": [ElementsData.Home.btn_gears],
        "BuyEnergyPanel": [ElementsData.Home.btn_add_100500],
        "FishCardPanel": [ElementsData.Home.btn_fishcard],
        "FisheryGiftPackPanel": [ElementsData.Home.btn_event_location],
        "MailPanel": [ElementsData.Home.btn_mail],
        "PlayerSettingPanel": [ElementsData.Home.player_info],
        "ProgressRewardsPanel": [ElementsData.Home.btn_globa_progress],
        "PVPHallPanel": [ElementsData.Home.btn_pvp],
        "Recharge1And1Panel": ElementsData.Home.btn_1add1,
        "RechargeBlack5Panel": [ElementsData.Home.btn_black5],
        "RechargeEndlessPanel": [ElementsData.Home.btn_endless],
        "RoulettePanel": [ElementsData.Home.btn_roulette],
        "StorePanel": [ElementsData.Home.btn_store],
        "TaskPanel": [ElementsData.Home.btn_task],
        "TreasureChestPanel": [ElementsData.Home.btn_chest],
    }

    panel_dict = {
        "AchievementPanel": ElementsData.Achievement.AchievementPanel,
        "BattlePassPanel": ElementsData.BattlePass.BattlePassPanel,
        "BaitAndRodAlbumPanel": ElementsData.BaitAndRodAlbum.BaitAndRodAlbumPanel,
        "BuyEnergyPanel": ElementsData.BuyEnergy.BuyEnergyPanel,
        "FishCardPanel": ElementsData.FishCard.FishCardPanel,
        "FisheryGiftPackPanel": ElementsData.FisheryGiftPack.FisheryGiftPackPanel,
        "MailPanel": ElementsData.Mail.MailPanel,
        "PlayerSettingPanel": ElementsData.PlayerSetting.PlayerSettingPanel,
        "PVPHallPanel": ElementsData.PVPHall.PVPHallPanel,
        "Recharge1And1Panel": ElementsData.Recharge1And1.Recharge1And1Panel,
        "RechargeBlack5Panel": ElementsData.RechargeBlack5.RechargeBlack5Panel,
        "RechargeEndlessPanel": ElementsData.RechargeEndless.RechargeEndlessPanel,
        "RoulettePanel": ElementsData.Roulette.RoulettePanel,
        "StorePanel": ElementsData.Store.StorePanel,
        "TaskPanel": ElementsData.Task.TaskPanel,
        "TreasureChestPanel": ElementsData.TreasureChest.TreasureChestPanel,

    }