import time
from common.basePage import BasePage
import luaLog
from panelObjs.loadingPanel import LoadingPanel
from panelObjs.loginPanel import LoginPanel


class NetMsgTest():
    def __init__(self, bp: BasePage):
        self.bp = bp
        self.username = ""
        self.charSimpleId = 0
        self.charId = ""
        self.userId = ""
        self.roomId_division = 0
        # self.login()
        self.msg_data = {
            "AchieveGroupRewardMsg": {"msg_arg": {"achieveGroupTpId": 201, "num": 50}, "expect_reply": {"msg": ["success", "已经领奖了", "没有这个成就点的奖励", "成就点数没有达到领奖要求"]}},
            "AchieveGroupUnlockMsg": {"msg_arg": {"achieveGroupTpId": 201}, "expect_reply": {"msg": ["success", "没有解锁成就组"]}},
            "AchieveCategoryRewardMsg": {"msg_arg": {"categoryTpId": 10001}, "expect_reply": {"msg": ["success", "成就点数没有达到领奖要求", "没有获得这个成就鱼种", "成就鱼种没有完成"]}},
            "AchieveCategoryFishLightMsg": {"msg_arg": {"categoryTpId": 10001, "fishTpId": 301004}, "expect_reply": {"msg": ["success"], "code": ["1"]}},
            "AchieveCategoryUnlockMsg": {"msg_arg": {"categoryTpId": 10001}, "expect_reply": {"msg": ["success", "没有获得这个成就鱼种"]}},
            "AchieveWantedRewardMsg": {"msg_arg": {"wantedTpId": 40030101}, "expect_reply":  {"msg": ["success", "成就点数没有达到领奖要求", "没有获得这个成就鱼种", "成就悬赏没有完成"]}},
            "AchieveWantedFishLightMsg": {"msg_arg": {"wantedTpId": 40030101, "fishTpId": 390001}, "expect_reply": {"msg":["success"], "code": ["1"]}},
            "AchieveWantedUnlockMsg": {"msg_arg": {"wantedTpId": 40030101}, "expect_reply": {"msg": ["success", "没有获得这个成就鱼种"]}},
            "ActivationCodeUseMsg": {"msg_arg": {"code": "123"}, "expect_reply": {"msg":["激活码不存在"]}},
            # "AdBeginViewMsg": {"msg_arg": {"advertId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "AquariumProsperityLvUpMsg": {"msg_arg": {"tpId": 101, "lv": 2}, "expect_reply": {"msg":["success", "水族箱等级错误", "不存在此水族箱"]}},
            "AquariumBuildingUpLvMsg": {"msg_arg": {"buildingTpId": 101003, "tpId": 101}, "expect_reply": {"msg":["success", "资源点不足！", "不存在此水族箱"]}},
            # "AquariumBuildingChangeSkinMsg": {"msg_arg": {"tpId": int, "buildingTpId": int, "skinTpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "AquariumPutFishMsg": {"msg_arg": {"ornamentalFishTpId": 10101, "tpId": 101}, "expect_reply": {"msg":["success", "水族箱不存在此观赏鱼", "不存在此水族箱","水族箱鱼已满"]}},
            "AquariumRemoveFishMsg": {"msg_arg": {"ornamentalFishTpId": 10101, "tpId": 101}, "expect_reply": {"msg":["success", "水族箱不存在此观赏鱼", "不存在此水族箱"]}},
            "AquariumBuyOrnamentalFishMsg": {"msg_arg": {"ornamentalFishTpId": 10101, "tpId": 101}, "expect_reply": {"msg":["success", "资源点不足！", "不存在此水族箱"]}},
            "AquariumRemoveAllFishMsg": {"msg_arg": {"tpId": 101}, "expect_reply": {"msg":["success", "不存在此水族箱"]}},
            # "AquariumFeedFishMsg": {"msg_arg": {"tpId": int, "fishTpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "AquariumSwitchMsg": {"msg_arg": {"tpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "AquariumSeeHangUpRewardMsg": {"msg_arg": {}, "expect_reply": {"msg":["success"]}},
            "AquariumHangUpRewardMsg": {"msg_arg": {}, "expect_reply": {"msg":["success"]}},
            "AquariumSurpriseRewardMsg": {"msg_arg": {"tpId": 101}, "expect_reply": {"msg":["success", "不存在此水族箱", "不存在惊喜奖励"]}},
            "AquariumSeeFishChangeMsg": {"msg_arg": {"tpId": 101}, "expect_reply": {"msg":["success", "不存在此水族箱"]}},
            "UseItemMsg": {"msg_arg": {"useTimes": 1, "itemType": 2, "itemTpId": 211001}, "expect_reply": {"msg":["success"], "code": ["2"]}},
            # "BatchUseItemMsg": {"msg_arg": {"useList": "", }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "BuyItemMsg": {"msg_arg": {"itemTpId": 100300, "priceTpId": 100100, "count": 1000, "itemType": 1, "source": 0}, "expect_reply": {"msg":["success", "资源点不足！"]}},
            # "SellItemMsg": {"msg_arg": {"source": 1, "itemType": 1, "itemTpId": 100100, "count": 1, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "BaitAndRodComposeMsg": {"msg_arg": {"source": int, "ioIdType": int, "tpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "BaitAndRodLevelUpMsg": {"msg_arg": {"source": int, "ioIdType": int, "tpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "BaitAndRodLevelUpToMsg": {"msg_arg": {"targetLevel": 2, "ioIdType": 5, "tpId": 500001}, "expect_reply": {"msg":["success", "资源点不足！"]}},
            # "BaitAndRodGenEffectMsg": {"msg_arg": {"source": int, "ioIdType": int, "tpId": int, "idx": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "BaitAndRodGenEffectConfirmMsg": {"msg_arg": {"source": int, "ioIdType": int, "tpId": int, "idx": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "BaitAndRodWashMsg": {"msg_arg": {"source": int, "ioIdType": int, "tpId": int, "idx": int, "times": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "BaitAndRodStarLevelUpMsg": {"msg_arg": {"source": 1, "ioIdType": 5, "tpId": 500001}, "expect_reply": {"msg":["success", "资源点不足！"], "code": ["2"]}},
            # "BaitAndRodStarChooseMsg": {"msg_arg": {"source": int, "ioIdType": int, "tpId": int, "idx": int, "effectIdx": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "BattlePassGetRewardMsg": {"msg_arg": {"lv": 1, "groupId": 4, "pay": False}, "expect_reply": {"msg":["success", "free奖励已经被领取了!", "活动已经结束，或者已经被刷新"]}},
            "BattlePassGetAllRewardMsg": {"msg_arg": {"groupId": 4}, "expect_reply": {"msg":["success", "活动已经结束，或者已经被刷新"]}},
            # "QueryChallengeRankMsg": {"msg_arg": {"tpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "QueryChallengeSelfRankMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "QueryChampionshipsRankMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChampionshipsBeginLimitedPlayMsg": {"msg_arg": {"source": int, "road": int, "championshipsId": int, "endTime": int, "slv": int, "limitedPlaySpotId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChampionshipsQueryLimitedPlayInfoMsg": {"msg_arg": {"source": int, "road": int, "championshipsId": int, "endTime": int, "slv": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "ChampionshipsGetUnGetRewardsMsg": {"msg_arg": {"championshipsId": 1, "source": 0, "road": 2}, "expect_reply": {"msg":["success", "锦标赛轮次已经结束！"], "code":["0"]}},
            "CharaRenameMsg": {"msg_arg": {"newName": self.username}, "expect_reply": {"msg": ["success", "改名系统维护中", "名字不能为空！"], "code":["1113"]}},
            "CharaSetIconMsg": {"msg_arg": {"icon": 1}, "expect_reply": {"msg": ["success"]}},
            # "CharaSetIconBoxMsg": {"msg_arg": {"iconBox": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "CharaSetSexMsg": {"msg_arg": {"sex": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "CharaSetSignMsg": {"msg_arg": {"sign": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "CharaSetLangMsg": {"msg_arg": {"lang": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "CharaGetVipGiftMsg": {"msg_arg": {"vipLv": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "UnbindThirdPartySdkMsg": {"msg_arg": {"tuYouUerId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "CharaReceiveUnGetRewardsMsg": {"msg_arg": {"id": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SetPlayerSourceTypeMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SetPlayerNationalFlagMsg": {"msg_arg": {"nationalFlag": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SetPlayerFbIconUrlMsg": {"msg_arg": {"fbIconUrl": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SetPlayerBadgeMsg": {"msg_arg": {"index": int, "badge": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "QueryPlayerCardInfoMsg": {"msg_arg": {"source": 1, "icon": 1, "charId": self.charId, "name": self.username}, "expect_reply": {"msg":["success"], "code":["1"]}},
            "SetPlayerBadgeAllMsg": {"msg_arg": {"indexToBadge": {}}, "expect_reply": {"msg":["success"]}},
            # "ChatLoginMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatPingMsg": {"msg_arg": {"clientTime": float, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatSendContentMsg": {"msg_arg": {"channelId": int, "content": str, "charIdB": str, "bytes": bytes, "otherArgs": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatSyncContentMsg": {"msg_arg": {"channelId": int, "msgNo": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatDeleteChannelMsg": {"msg_arg": {"charIdB": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatTopChannelMsg": {"msg_arg": {"channelId": int, "isTop": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatQueryLangChannelMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ChatSelectLangChannelMsg": {"msg_arg": {"channelId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GetChestRewardsMsg": {"msg_arg": {"chestPointId": 5}, "expect_reply": {"msg":["success"], "code":["1470"]}},
            "OpenChestMsg": {"msg_arg": {"itemTpId": 207004, "count": 1}, "expect_reply": {"msg":["success"], "code":["2"]}},
            "CommonExchangeMsg": {"msg_arg": {"exchangeId": 102, "buyTimes": 1}, "expect_reply": {"msg":["success"], "code":["2"]}},
            "QueryDivisionRankMsg": {"msg_arg": {"fromRank": 1,"roomId": self.roomId_division, "count": 1}, "expect_reply": {"msg":["success"]}},
            "DoubleWeekQueryOverallRankMsg": {"msg_arg": {"fromRank": 1, "fishSceneTpId": 400302, "season": 1,  "count": 100}, "expect_reply": {"msg": ["success", "当前活动期间不匹配，无法查询排行榜"], "code":["1"]}},
            "DoubleWeekQueryFishRankMsg": {"msg_arg": {"fromRank": 1, "fishSceneTpId": 400302, "fishTpId": 390017, "season": 1,  "count": 100}, "expect_reply": {"msg": ["success", "当前活动期间不匹配，无法查询排行榜"], "code":["1"]}},
            "QueryDuelInfoMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "EnterMatchMsg": {"msg_arg": {"seriesId": 1001}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "CancelMatchMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "DuelSelectCardMsg": {"msg_arg": {"duelId": int, "cardTpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "DuelConfirmCardMsg": {"msg_arg": {"duelId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SceneLoadedMsg": {"msg_arg": {"duelId": int, "reEnter": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "DuelGiveUpMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success", "不在对决中，或对决已结束！"], "code": ["0", "1448"]}},
            "DuelEndMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success", "当前没有结束待结算的对决结果！"], "code": ["0", "1457"]}},
            "ExistDuelMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success", "不在对决中，或对决已结束！"], "code": ["0", "1448"]}},
            # "DuelPingMsg": {"msg_arg": {"clientTime": float, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "QueryDuelRankMsg": {"msg_arg": {"fromRank": 1, "count": 200}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "BonusMsg": {"msg_arg": {"duelId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "DuelEmojiMsg": {"msg_arg": {"emojiId": int, "duelId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ExchangeItemsMsg": {"msg_arg": {"exchangeId": int, "num": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "UpdateFacadeMsg": {"msg_arg": {"wearInfo": dict, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SeeFacadeMsg": {"msg_arg": {"tpId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "UpdateFacadeDBMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "FishCardLevelUpMsg": {"msg_arg": {"fishCardTpId": 1000000}, "expect_reply": {"msg": ["success", "不存在此鱼卡！"], "code": ["0", "1494"]}},
            "FishCardOneKeyLevelUpMsg": {"msg_arg": {"fishCardTpIds":{}}, "expect_reply": {"msg": ["success", "请选择要升级的鱼卡！"], "code": ["0", "1494"]}},
            # "FishingCastMsg": {"msg_arg": {"source": int, "sceneArg1": int, "otherArgMap": dict, "fixedFishTpId": int, "boosterIds": str, "castG": int, "castGType": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingHookMsg": {"msg_arg": {"source": int, "castFlag": int, "timeCost": int, "qteInfos": str, "use_ULT_Ts": int, "minEstimateTimeMills": int, "hook_result": int, "battleResult": str, "battleResultArgs": dict, "fishArgs": dict, "rodArgs": dict, "playerArgs": dict, "fishSceneArgs": dict, "counterSuccessNum": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "shingQTEInfo": {"msg_arg": {"done": bool, "perfect": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingSelectFishMsg": {"msg_arg": {"fishSceneTpId": int, "fishTpId": int, "isInDoubleWeek": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingGetFishStarRewardMsg": {"msg_arg": {"fishSceneTpId": int, "fishTpId": int, "rewardStarIdx": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingGetSceneStarRewardMsg": {"msg_arg": {"fishSceneTpId": int, "rewardStarIdx": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingEquipChangeMsg": {"msg_arg": {"sceneArg1": int, "save": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingEquipPinMsg": {"msg_arg": {"fishSceneTpId": int, "ioIdType": int, "tpId": int, "doPin": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingBoosterOpenMsg": {"msg_arg": {"tpIds": str, "opens": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingSaveFishSpotMsg": {"msg_arg": {"source": int, "fishSceneTpId": int, "fishSpotId": int, "isInDoubleWeek": bool, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishSceneFishNewMsg": {"msg_arg": {"fishSceneTpId": int, "fishTpIds": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingContinueLimitedSpotMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingSaveLimitedSpotEnergyCostIdMsg": {"msg_arg": {"source": int, "chooseEnergyCostId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishSceneRewardSumPointMsg": {"msg_arg": {"fishSceneTpId": int, "sumPoint": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishSwitchSkinMsg": {"msg_arg": {"fishSceneTpId": int, "fishTpId": int, "useSeasonSkin": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FishingCastDistanceMsg": {"msg_arg": {"castG": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "FlashCardSeasonRewardMsg": {"msg_arg": {"seasonId": 0}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "FlashCardChapterRewardMsg": {"msg_arg": {"rewardId": 1}, "expect_reply": {"msg": ["success"], "code": ["0", "1", "1607"]}},
            "FlashCardShopExchangeMsg": {"msg_arg": {"shopTpId": 1, "cardInfos": {}}, "expect_reply": {"msg": ["success"], "code": ["0", "1612"]}},
            "FlashCardGuildRequestMsg": {"msg_arg": {"flashCardTpId": 1300001}, "expect_reply": {"msg": ["success", "尚未加入公会"], "code": ["0", "1585"]}},
            "FlashCardGuildDonateMsg": {"msg_arg": {"receiveSimpleCharId": self.charSimpleId, "flashCardTpId": 1300001, "receiveCharId": self.charId}, "expect_reply": {"msg": ["success"], "code": ["0", "3"]}},
            "FlashCardGuildCancelRequestMsg": {"msg_arg": {"flashCardTpId": 1300001}, "expect_reply": {"msg": ["success", "尚未加入公会"], "code": ["0", "1585"]}},
            # "GlobalFriendsQueryMsg": {"msg_arg": {"source": int, "simpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsApplyMsg": {"msg_arg": {"source": int, "simpleId": int, "targetCharId": str, "targetSimpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsIgnoreApplyMsg": {"msg_arg": {"source": int, "simpleId": int, "targetCharId": str, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsIgnoreAllAppliesMsg": {"msg_arg": {"source": int, "simpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsAcceptMsg": {"msg_arg": {"source": int, "simpleId": int, "targetCharId": str, "targetSimpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsAcceptAllMsg": {"msg_arg": {"source": int, "simpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsDeleteMsg": {"msg_arg": {"source": int, "simpleId": int, "targetCharId": str, "targetSimpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsInviteMsg": {"msg_arg": {"source": int, "simpleId": int, "targetCharId": str, "targetSimpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GlobalFriendsRefreshMsg": {"msg_arg": {"source": int, "simpleId": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GlobalRankQueryMsg": {"msg_arg": {"clientArgs": {}, "groupArg2": 1, "group": 301001, "type": 5, "groupArg1": 1, "groupArg": 400301}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GlobalRankFirstQueryMsg": {"msg_arg": {"groupToGroupArg": {}, "clientArgs": {}, "type": 5, "groupArg1": 1, "groupArg2": 1}, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            # "GlobalSpecialRankFirstQueryS1Msg": {"msg_arg": {"flashCardTpId": 1300001}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GmCommandMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildDragonQueryMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "龙舟分组中", "公会不存在或已解散"], "code": ["0", "1624", "1586"]}},
            "GuildDragonQueryDetailMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "龙舟分组中", "公会不存在或已解散"], "code": ["0", "1624", "1586"]}},
            "GuildDragonQueryRankMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "group": 0, "type": 0, }, "expect_reply": {"msg": ["success", "龙舟分组中", "公会不存在或已解散"], "code": ["0", "1624", "1586"]}},
            "GuildDragonQueryMemberMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "龙舟分组中", "公会不存在或已解散"], "code": ["0", "1624", "1586"]}},
            "GuildDragonRewardMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "rewardId": 0, }, "expect_reply": {"msg": ["success", "活动已经结束，或者尚未开始"], "code": ["0", "1162"]}},
            "GuildRefreshMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildAutoEnterMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "角色等级不足！"], "code": ["0", "6"]}},
            "GuildSearchMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "name": "guild", }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GameGuildCreateMsg": {"msg_arg": {"source": 0, "name": "gulid", "flag": 1, "pattern": 1, "color": 1, "introduce": "一起欢乐钓鱼吧！", "labels": {}, "joinType": 1, "joinLv": 0, }, "expect_reply": {"msg": ["success", "资源点不足！"], "code": ["0", "4"]}},
            "GuildQueryApplyGuildMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildQueryMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildQueryOtherMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            # "GuildQueryOtherBaseMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "simpleIds": {}, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildQueryAppliesMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "permission": 0, }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildApplyMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "角色等级不足！"], "code": ["0", "6"]}},
            "GuildCancelApplyMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "角色等级不足！"], "code": ["0", "6"]}},
            "GuildIgnoreApplyMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "targetCharId": "" }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "GuildIgnoreAllAppliesMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0}, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildAcceptMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "targetCharId": "0" }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildAcceptAllMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0 },"expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildDeleteMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "targetCharId": "0" }, "expect_reply": {"msg": ["success", "角色等级不足！"], "code": ["0", "6"]}},
            # "GameGuildSetGuildInfoCostMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "name": "gulid", "flag": 1, "pattern": 1, "color": 1, "introduce": "一起欢乐钓鱼吧！", "labels": {}, "joinType": 1, "joinLv": 0 }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildSetGuildInfoMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "labels": {}, "joinType": 1, "joinLv": 0 }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildSetMemberPosMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "targetCharId": "member", "pos": 1 }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildTransferPresidentMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "targetCharId": "0"}, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            "GuildMemberQuitMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            # "GuildSendMailToAllMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "title": "title", "content": "content"}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildQueryDialogMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success", "公会不存在或已解散"], "code": ["0", "1586"]}},
            # "GameGuildProgressRewardMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "rewardId": 1100001}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GameGuildReportMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GuildMemberPlayerCardMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "charSimpleId": 0, "charId": "0", }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "GameGuildSendRedEnvelopeMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GameGuildRewardRedEnvelopeMsg": {"msg_arg": {"source": 0, "guildSimpleId": 0, "redEnvelopeId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "HiddenTreasureDigMsg": {"msg_arg": {"groupId": 0, "roomId": 0, "stage": 1, "digXs": {}, "digYs": {}, }, "expect_reply": {"msg": ["success", "未携带坐标的挖宝请求，无效"], "code": ["0", "1632"]}},
            "HiddenTreasureSetMultipleMsg": {"msg_arg": {"groupId": 0, "roomId": 0, "stage": 1, "multiple": 1, }, "expect_reply": {"msg": ["success", "挖宝请求的活动或分组或关卡不匹配"], "code": ["0", "1634"]}},
            "HiddenTreasureQueryRankMsg": {"msg_arg": {"groupId": 0, "roomId": 0, "fromRank": 1, "count": 20, }, "expect_reply": {"msg": ["success", "挖宝请求的活动或分组或关卡不匹配"], "code": ["0", "1634"]}},
            "HiddenTreasureGetProgressRewardMsg": {"msg_arg": {"groupId": 0, "roomId": 0, }, "expect_reply": {"msg": ["success", "挖宝请求的活动或分组或关卡不匹配"], "code": ["0", "1634"]}},
            # "IOSStarNumMsg": {"msg_arg": {"starNum": 5, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "LoginAuthMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "LoginMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ReconnectMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "QueryServerListInfoMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "SwitchRealmMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "QueryLoginIdxMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "QuerySdkBoundSnsMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "EnterGameMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ReEnterGameMsg": {"msg_arg": {"needReEnter": False, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "MailReadMsg": {"msg_arg": {"mailId": 1, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "MailDeleteAllReadMsg": {"msg_arg": {"mailIds": {}, }, "expect_reply": {"msg": ["success", "没有需要删除的邮件"], "code": ["0", "1081"]}},
            "MailGetAttachmentsMsg": {"msg_arg": {"mailId": 1, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "MailGetAllAttachmentsMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "MailGetIdsAttachmentsMsg": {"msg_arg": {"mailIds": {}, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "GetMissionMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "ClearFailMissionMsg": {"msg_arg": {"missionType": 10, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GetMissionRewardsMsg": {"msg_arg": {"missionType": 0, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "JumpMissionMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "MonopolyRollDiceMsg": {"msg_arg": {"groupId": 0, "roomId": 0, "multiple": 1, }, "expect_reply": {"msg": ["success", "大富翁未开启", "大富翁活动组不匹配"], "code": ["0", "1559", "1560"]}},
            "MonopolyQueryRankMsg": {"msg_arg": {"groupId": 0, "roomId": 0, "fromRank": 1, "count": 20, }, "expect_reply": {"msg": ["success", "大富翁未开启", "大富翁活动组不匹配"], "code": ["0", "1559", "1560"]}},
            "MonopolyGetProgressRewardMsg": {"msg_arg": {"groupId": 0, "roomId": 0, }, "expect_reply": {"msg": ["success", "大富翁未开启", "大富翁活动组不匹配"], "code": ["0", "1559", "1560"]}},
            "MonopolyQueryFreeDiceMsg": {"msg_arg": {"groupId": 0, "roomId": 0, }, "expect_reply": {"msg": ["success", "大富翁未开启", "大富翁活动组不匹配"], "code": ["0", "1559", "1560"]}},
            "NewGuideStoreMsg": {"msg_arg": {"key": "", }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "NDaysEventGetTokenRewardsMsg": {"msg_arg": {"groupId": 0, }, "expect_reply": {"msg": ["success", "活动尚未开启"], "code": ["0", "1150"]}},
            "NDaysEventQueryRankMsg": {"msg_arg": {"groupId": 0, "roomId": 0, "fromRank": 1, "count": 20, }, "expect_reply": {"msg": ["success", "活动尚未开启"], "code": ["0", "1150"]}},
            "PaymentMonthCardGetRewardsMsg": {"msg_arg": {"cardTpId": 0, }, "expect_reply": {"msg": ["success", "尚未购买月卡"], "code": ["0", "1643"]}},
            "PaymentBuyMsg": {"msg_arg": {"source": 0, "orderType": 1, "goodsId": 0, "useVouchers": False, "extArg1": 0, "extArg2": 0, "extArgs": {}, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "ProgressRewardMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success", "进度条没有可以领的奖励"], "code": ["0", "1526"]}},
            "RepeatableChallengeGetRewardsMsg": {"msg_arg": {"challengeTpId": 0, }, "expect_reply": {"msg": ["success", "未开启的持续挑战型任务，不可以领奖"], "code": ["0", "1500"]}},
            "SaveRodAttachMsg": {"msg_arg": {"rodId": 500021, "useType2Id": {}, }, "expect_reply": {"msg": ["success", "数据格式不合法！"], "code": ["0", "2"]}},
            "SeeRodAttachMsg": {"msg_arg": {"type": 1, "attachId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0", "2"]}},
            "UpdateRodAttachDBMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "RouletteDrawMsg": {"msg_arg": {"groupId": 0, "lv": 1, }, "expect_reply": {"msg": ["success", "转盘 groupId 不匹配"], "code": ["0", "1480"]}},
            "SelfRankLikesMsg": {"msg_arg": {"charId": self.charId, "group": 0, "groupArg": 0, "groupArg1": 0, "groupArg2": 0, "type": 0, }, "expect_reply": {"msg": ["success", "没有第一名"], "code": ["0", "1552"]}},
            "SelfRankRecordMsg": {"msg_arg": {"timeType": 1, }, "expect_reply": {"msg": ["success", "记录只能是月榜和年榜"], "code": ["0", 1]}},
            "ShopRefreshMsg": {"msg_arg": {"shopTpId": 1, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "ShopBuyItemMsg": {"msg_arg": {"shopTpId": 1, "goodsId": 0, "refreshIdx": 0, "buyTimes": 0, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            "SignGiftSignMsg": {"msg_arg": {"groupId": 0, }, "expect_reply": {"msg": ["success", "签到活动不存在"], "code": ["0", "1573"]}},
            # "ReportMsg": {"msg_arg": {"beReportCharaId": self.charId, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "DoneSharingMsg": {"msg_arg": {}, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "DoneFollowMsg": {"msg_arg": {"followType": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "DoneQuestionnaireMsg": {"msg_arg": {"questionTpId": 0, }, "expect_reply": {"msg": ["success", "已经完成了问卷调查"], "code": ["0", "1307"]}},
            # "DoneQuestionnaireCell": {"msg_arg": {"cellTpId": 0, "answerLis": "", }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "QuestionnaireAnswerMsg": {"msg_arg": {"selectIdx": 0, "content": "content", }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "GetDLCNodeRewardsMsg": {"msg_arg": {"dlcNodeId": 0, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            # "PingMsg": {"msg_arg": {"clientTime": float, "flag": int, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "QueryCharInfoMsg": {"msg_arg": {"source": 0, "charId": self.charId, }, "expect_reply": {"msg": ["success"], "code": ["0", "1"]}},
            # "LikeQueryCharInfoMsg": {"msg_arg": {"idOrName": "name", }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            # "RecordPaymentMsg": {"msg_arg": {"source": 0, "orderIds": {}, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
            "TalentLvUpMsg": {"msg_arg": {"talentTpId": 0, }, "expect_reply": {"msg": ["success", "天赋页还没有解锁"], "code": ["0", "1566"]}},
            "TalentUnlockMsg": {"msg_arg": {"talentTpId": 0, }, "expect_reply": {"msg": ["success", "天赋页还没有解锁"], "code": ["0", "1566"]}},
            "TriggerGiftTryTriggerMsg": {"msg_arg": {"triggerType": 0, }, "expect_reply": {"msg": ["success"], "code": ["0"]}},
        }

    def login(self):
        while not LoginPanel.is_btn_login_active(self.bp):
            self.bp.sleep(0.5)
        self.username = str(time.time()).split('.')[0]
        if LoginPanel.is_InputField_UserName_active(self.bp):
            LoginPanel.set_login_name(self.bp, self.username)

        # 清空消息列表 开始收消息
        self.bp.log_list.clear()
        self.bp.log_list_flag = True

        LoginPanel.wait_for_btn_login(self.bp)
        LoginPanel.click_btn_login(self.bp)
        self.bp.sleep(2)

        # 直到读条消失
        LoadingPanel.wait_until_panel_disappear(self.bp, is_wait_for_appear=False)

        # 停止接收消息
        self.bp.sleep(0.5)
        self.bp.log_list_flag = False

        # 在最近收集的消息列表中筛出目标消息
        key_sc = '<==== [Lua] Receive Net Msg "SC'
        msg_name = "LoginMsg"
        msg_key = key_sc + msg_name
        target_log = self.get_target_log(msg_key)
        if target_log != "":
            # 根据键拿到值
            self.charSimpleId = luaLog.get_value(msg=target_log, key="charSimpleId", is_str=False)
            self.charId = luaLog.get_value(msg=target_log, key="charId", is_str=True)
            self.userId = luaLog.get_value(msg=target_log, key="userId", is_str=True)
        msg_name = "DivisionBatchDataMsg"
        msg_key = key_sc + msg_name
        target_log = self.get_target_log(msg_key)
        if target_log != "":
            self.roomId_division = luaLog.get_value(msg=target_log, key="roomId", is_str=False)



    def check_sc_msg(self, msg_name: str, expect_key):
        expect_value_list = self.msg_data[msg_name]["expect_reply"][expect_key]
        # 在最近收集的消息列表中筛出目标消息
        key_sc = '<==== [Lua] Receive Net Msg "SC'
        msg_key = key_sc + msg_name
        target_log = self.get_target_log(msg_key)
        if target_log == "":
            return False

        # 根据期望键拿到值
        value = luaLog.get_value(msg=target_log, key=expect_key, is_str=True)

        # 看值是否在期望的值列表中
        if value not in expect_value_list:
            return False
        return True

    # 根据消息键查找值
    def get_target_log(self, msg_key):
        target_log = ""
        for log in self.bp.log_list:
            if msg_key not in log:
                continue
            target_log = log
            break
        return target_log



    def msg_test(self, msg_name, duration=1):
        res = {}
        # 清空消息列表 开始收消息
        self.bp.log_list.clear()
        self.bp.log_list_flag = True
        try:
            # 发送cs请求
            lua_code = self.bp.call_function(module_name="csMsgAll", function_name=f"get_CS{msg_name}", **self.msg_data[msg_name]["msg_arg"])
            print(lua_code)
            self.bp.lua_console(lua_code)

            # 停止接收消息
            self.bp.sleep(duration)
            self.bp.log_list_flag = False

            # 判断结果是否正确
            expect_reply = self.msg_data[msg_name]["expect_reply"]
            expect_key_list = list(expect_reply)
            cur = 0
            while cur < len(expect_key_list):
                expect_key = expect_key_list[cur]
                res[msg_name] = self.check_sc_msg(msg_name, expect_key)
                if res[msg_name]:
                    break
                cur += 1
        except Exception as e:
            print(e)
            res[msg_name] = False
        return res

    def achieve_test(self):
        res = {}
        # 成就解锁
        res.update(self.msg_test("AchieveGroupUnlockMsg"))

        # 成就领奖
        res.update(self.msg_test("AchieveGroupRewardMsg"))

        return res

    def achieveCategory_test(self):
        res = {}
        # 鱼种成就解锁
        res.update(self.msg_test("AchieveCategoryUnlockMsg"))

        # 鱼种点亮
        res.update(self.msg_test("AchieveCategoryFishLightMsg"))

        # 鱼种领奖
        res.update(self.msg_test("AchieveCategoryRewardMsg"))

        return res

    def achieveWanted_test(self):
        res = {}
        # 鱼种成就解锁
        res.update(self.msg_test("AchieveWantedUnlockMsg"))

        # 鱼种点亮
        res.update(self.msg_test("AchieveWantedFishLightMsg"))

        # 鱼种领奖
        res.update(self.msg_test("AchieveWantedRewardMsg"))

        return res

    def activationCode_test(self):
        res = {}

        res.update(self.msg_test("ActivationCodeUseMsg"))
        return res

    def advert_test(self):
        res = {}

        res.update(self.msg_test("AdBeginViewMsg"))

        return res

    def aquarium_test(self):
        res = {}

        res.update(self.msg_test("AquariumProsperityLvUpMsg"))

        # 等级提升
        res.update(self.msg_test("AquariumBuildingUpLvMsg"))

        # res.update(self.msg_test("AquariumBuildingChangeSkinMsg"))

        # 放鱼
        res.update(self.msg_test("AquariumPutFishMsg"))

        # 收鱼
        res.update(self.msg_test("AquariumRemoveFishMsg"))

        # 买鱼
        res.update(self.msg_test("AquariumBuyOrnamentalFishMsg"))

        # 收全鱼
        res.update(self.msg_test("AquariumRemoveAllFishMsg"))

        # res.update(self.msg_test("AquariumFeedFishMsg"))
        #
        # res.update(self.msg_test("AquariumSwitchMsg"))

        # 查看挂机奖励
        res.update(self.msg_test("AquariumSeeHangUpRewardMsg"))

        # 领取挂机奖励
        res.update(self.msg_test("AquariumHangUpRewardMsg"))

        # 领取挂机奖励
        res.update(self.msg_test("AquariumSurpriseRewardMsg"))

        # 刷新鱼
        res.update(self.msg_test("AquariumSeeFishChangeMsg"))

        return res

    def backPack_test(self):
        res = {}

        res.update(self.msg_test("UseItemMsg"))

        # res.update(self.msg_test("BatchUseItemMsg"))

        res.update(self.msg_test("BuyItemMsg"))

        # res.update(self.msg_test("SellItemMsg"))

        return res

    def baitAndRod_test(self):
        res = {}

        # res.update(self.msg_test("BaitAndRodComposeMsg"))
        #
        # res.update(self.msg_test("BaitAndRodLevelUpMsg"))

        res.update(self.msg_test("BaitAndRodLevelUpToMsg"))

        # res.update(self.msg_test("BaitAndRodGenEffectMsg"))
        #
        # res.update(self.msg_test("BaitAndRodGenEffectConfirmMsg"))
        #
        # res.update(self.msg_test("BaitAndRodWashMsg"))

        res.update(self.msg_test("BaitAndRodStarLevelUpMsg"))

        # res.update(self.msg_test("BaitAndRodStarChooseMsg"))

        return res

    def battlePass_test(self):
        res = {}
        res.update(self.msg_test("BattlePassGetRewardMsg"))

        res.update(self.msg_test("BattlePassGetAllRewardMsg"))
        return res

    def challenge_test(self):
        res = {}

        res.update(self.msg_test("QueryChallengeRankMsg"))

        res.update(self.msg_test("QueryChallengeSelfRankMsg"))

        return res

    def championships_test(self):
        res = {}

        # res.update(self.msg_test("QueryChampionshipsRankMsg"))
        #
        # res.update(self.msg_test("ChampionshipsBeginLimitedPlayMsg"))
        #
        # res.update(self.msg_test("ChampionshipsQueryLimitedPlayInfoMsg"))

        res.update(self.msg_test("ChampionshipsGetUnGetRewardsMsg"))

        return res

    def chara_test(self):
        res = {}

        # 改名
        res.update(self.msg_test("CharaRenameMsg"))

        # 改头像
        res.update(self.msg_test("CharaSetIconMsg"))

        # res.update(self.msg_test("CharaSetIconBoxMsg"))
        #
        # res.update(self.msg_test("CharaSetSexMsg"))
        #
        # res.update(self.msg_test("CharaSetSignMsg"))
        #
        # res.update(self.msg_test("CharaSetLangMsg"))
        #
        # res.update(self.msg_test("CharaGetVipGiftMsg"))
        #
        # res.update(self.msg_test("UnbindThirdPartySdkMsg"))
        #
        # res.update(self.msg_test("CharaReceiveUnGetRewardsMsg"))
        #
        # res.update(self.msg_test("SetPlayerSourceTypeMsg"))
        #
        # res.update(self.msg_test("SetPlayerNationalFlagMsg"))
        #
        # res.update(self.msg_test("SetPlayerFbIconUrlMsg"))
        #
        # res.update(self.msg_test("SetPlayerBadgeMsg"))

        # 查询信息
        res.update(self.msg_test("QueryPlayerCardInfoMsg"))

        # 设置徽章
        res.update(self.msg_test("SetPlayerBadgeAllMsg"))

        return res

    def chat_test(self):
        res = {}

        res.update(self.msg_test("ChatLoginMsg"))

        res.update(self.msg_test("ChatPingMsg"))

        res.update(self.msg_test("ChatSendContentMsg"))

        res.update(self.msg_test("ChatSyncContentMsg"))

        res.update(self.msg_test("ChatDeleteChannelMsg"))

        res.update(self.msg_test("ChatTopChannelMsg"))

        res.update(self.msg_test("ChatQueryLangChannelMsg"))

        res.update(self.msg_test("ChatSelectLangChannelMsg"))

        return res

    def chest_test(self):
        res = {}

        res.update(self.msg_test("OpenChestMsg"))

        res.update(self.msg_test("GetChestRewardsMsg"))

        return res

    def commonExchange_test(self):
        res = {}

        res.update(self.msg_test("CommonExchangeMsg"))

        return res

    def division_test(self):
        res = {}

        res.update(self.msg_test("QueryDivisionRankMsg"))

        return res

    def double_week_rank_test(self):
        res = {}

        res.update(self.msg_test("DoubleWeekQueryOverallRankMsg"))

        res.update(self.msg_test("DoubleWeekQueryFishRankMsg"))

        return res

    def duel_test(self):
        res = {}

        res.update(self.msg_test("QueryDuelInfoMsg"))

        res.update(self.msg_test("EnterMatchMsg"))

        res.update(self.msg_test("CancelMatchMsg"))

        # res.update(self.msg_test("DuelSelectCardMsg"))
        #
        # res.update(self.msg_test("DuelConfirmCardMsg"))
        #
        # res.update(self.msg_test("SceneLoadedMsg"))

        res.update(self.msg_test("DuelGiveUpMsg"))

        res.update(self.msg_test("DuelEndMsg"))

        res.update(self.msg_test("ExistDuelMsg"))

        # res.update(self.msg_test("DuelPingMsg"))

        res.update(self.msg_test("QueryDuelRankMsg"))

        # res.update(self.msg_test("BonusMsg"))
        #
        # res.update(self.msg_test("DuelEmojiMsg"))

        return res

    def exchange_test(self):
        res = {}

        res.update(self.msg_test("ExchangeItemsMsg"))

        return res

    def facade_test(self):
        res = {}

        res.update(self.msg_test("UpdateFacadeMsg"))

        res.update(self.msg_test("SeeFacadeMsg"))

        res.update(self.msg_test("UpdateFacadeDBMsg"))

        return res

    def fishing_test(self):
        res = {}

        res.update(self.msg_test("FishingCastMsg"))

        res.update(self.msg_test("FishingHookMsg"))

        res.update(self.msg_test("shingQTEInfo"))

        res.update(self.msg_test("FishingSelectFishMsg"))

        res.update(self.msg_test("FishingGetFishStarRewardMsg"))

        res.update(self.msg_test("FishingGetSceneStarRewardMsg"))

        res.update(self.msg_test("FishingEquipChangeMsg"))

        res.update(self.msg_test("FishingEquipPinMsg"))

        res.update(self.msg_test("FishingBoosterOpenMsg"))

        res.update(self.msg_test("FishingSaveFishSpotMsg"))

        res.update(self.msg_test("FishSceneFishNewMsg"))

        res.update(self.msg_test("FishingContinueLimitedSpotMsg"))

        res.update(self.msg_test("FishingSaveLimitedSpotEnergyCostIdMsg"))

        res.update(self.msg_test("FishSceneRewardSumPointMsg"))

        res.update(self.msg_test("FishSwitchSkinMsg"))

        res.update(self.msg_test("FishingCastDistanceMsg"))

        return res

    def fish_card_test(self):
        res = {}

        res.update(self.msg_test("FishCardLevelUpMsg"))

        res.update(self.msg_test("FishCardOneKeyLevelUpMsg"))

        return res

    def flashcard_test(self):
        res = {}

        # res.update(self.msg_test("FlashCardSeasonRewardMsg"))

        res.update(self.msg_test("FlashCardChapterRewardMsg"))

        res.update(self.msg_test("FlashCardShopExchangeMsg"))

        res.update(self.msg_test("FlashCardGuildRequestMsg"))

        res.update(self.msg_test("FlashCardGuildDonateMsg"))

        res.update(self.msg_test("FlashCardGuildCancelRequestMsg"))

        return res

    def friends_test(self):
        res = {}

        res.update(self.msg_test("GlobalFriendsQueryMsg"))

        res.update(self.msg_test("GlobalFriendsApplyMsg"))

        res.update(self.msg_test("GlobalFriendsIgnoreApplyMsg"))

        res.update(self.msg_test("GlobalFriendsIgnoreAllAppliesMsg"))

        res.update(self.msg_test("GlobalFriendsAcceptMsg"))

        res.update(self.msg_test("GlobalFriendsAcceptAllMsg"))

        res.update(self.msg_test("GlobalFriendsDeleteMsg"))

        res.update(self.msg_test("GlobalFriendsInviteMsg"))

        res.update(self.msg_test("GlobalFriendsRefreshMsg"))

        return res

    def globalRank_test(self):
        res = {}

        res.update(self.msg_test("GlobalRankQueryMsg"))

        res.update(self.msg_test("GlobalRankFirstQueryMsg"))

        # res.update(self.msg_test("GlobalSpecialRankFirstQueryS1Msg"))

        return res

    def guild_test(self):
        res = {}

        res.update(self.msg_test("GuildRefreshMsg"))

        res.update(self.msg_test("GuildAutoEnterMsg"))

        res.update(self.msg_test("GuildSearchMsg"))

        res.update(self.msg_test("GameGuildCreateMsg"))

        res.update(self.msg_test("GuildQueryApplyGuildMsg"))

        res.update(self.msg_test("GuildQueryMsg"))

        res.update(self.msg_test("GuildQueryOtherMsg"))

        # res.update(self.msg_test("GuildQueryOtherBaseMsg"))

        res.update(self.msg_test("GuildQueryAppliesMsg"))

        res.update(self.msg_test("GuildApplyMsg"))

        res.update(self.msg_test("GuildCancelApplyMsg"))

        res.update(self.msg_test("GuildIgnoreApplyMsg"))

        res.update(self.msg_test("GuildIgnoreAllAppliesMsg"))

        res.update(self.msg_test("GuildAcceptMsg"))

        res.update(self.msg_test("GuildAcceptAllMsg"))

        res.update(self.msg_test("GuildDeleteMsg"))

        # res.update(self.msg_test("GameGuildSetGuildInfoCostMsg"))

        res.update(self.msg_test("GuildSetGuildInfoMsg"))

        res.update(self.msg_test("GuildSetMemberPosMsg"))

        res.update(self.msg_test("GuildTransferPresidentMsg"))

        res.update(self.msg_test("GuildMemberQuitMsg"))

        # res.update(self.msg_test("GuildSendMailToAllMsg"))

        res.update(self.msg_test("GuildQueryDialogMsg"))

        # res.update(self.msg_test("GameGuildProgressRewardMsg"))

        res.update(self.msg_test("GameGuildReportMsg"))

        res.update(self.msg_test("GuildMemberPlayerCardMsg"))

        res.update(self.msg_test("GameGuildSendRedEnvelopeMsg"))

        res.update(self.msg_test("GameGuildRewardRedEnvelopeMsg"))

        return res

    def gmCommand_test(self):
        res = {}

        res.update(self.msg_test("GmCommandMsg"))

        return res

    def guildDragon_test(self):
        res = {}

        res.update(self.msg_test("GuildDragonQueryMsg"))

        res.update(self.msg_test("GuildDragonQueryDetailMsg"))

        res.update(self.msg_test("GuildDragonQueryRankMsg"))

        res.update(self.msg_test("GuildDragonQueryMemberMsg"))

        res.update(self.msg_test("GuildDragonRewardMsg"))

        return res

    def hidden_treasure_test(self):
        res = {}

        res.update(self.msg_test("HiddenTreasureDigMsg"))

        res.update(self.msg_test("HiddenTreasureSetMultipleMsg"))

        res.update(self.msg_test("HiddenTreasureQueryRankMsg"))

        res.update(self.msg_test("HiddenTreasureGetProgressRewardMsg"))

        return res

    def iosStar_test(self):
        res = {}

        res.update(self.msg_test("IOSStarNumMsg"))

        return res

    def login_test(self):
        res = {}

        res.update(self.msg_test("LoginAuthMsg"))

        res.update(self.msg_test("LoginMsg"))

        res.update(self.msg_test("ReconnectMsg"))

        res.update(self.msg_test("QueryServerListInfoMsg"))

        res.update(self.msg_test("SwitchRealmMsg"))

        res.update(self.msg_test("QueryLoginIdxMsg"))

        res.update(self.msg_test("QuerySdkBoundSnsMsg"))

        res.update(self.msg_test("EnterGameMsg"))

        res.update(self.msg_test("ReEnterGameMsg"))

        return res

    def mail_test(self):
        res = {}

        res.update(self.msg_test("MailReadMsg"))

        res.update(self.msg_test("MailDeleteAllReadMsg"))

        res.update(self.msg_test("MailGetAttachmentsMsg"))

        res.update(self.msg_test("MailGetAllAttachmentsMsg"))

        res.update(self.msg_test("MailGetIdsAttachmentsMsg"))

        return res

    def mission_test(self):
        res = {}

        # res.update(self.msg_test("GetMissionMsg"))

        # res.update(self.msg_test("ClearFailMissionMsg"))

        res.update(self.msg_test("GetMissionRewardsMsg"))

        res.update(self.msg_test("JumpMissionMsg"))

        return res

    def monopoly_test(self):
        res = {}

        res.update(self.msg_test("MonopolyRollDiceMsg"))

        res.update(self.msg_test("MonopolyQueryRankMsg"))

        res.update(self.msg_test("MonopolyGetProgressRewardMsg"))

        res.update(self.msg_test("MonopolyQueryFreeDiceMsg"))

        return res

    def newGuide_test(self):
        res = {}

        res.update(self.msg_test("NewGuideStoreMsg"))

        return res

    def n_days_event_test(self):
        res = {}

        res.update(self.msg_test("NDaysEventGetTokenRewardsMsg"))

        res.update(self.msg_test("NDaysEventQueryRankMsg"))

        return res

    def paymetMothCard_test(self):
        res = {}

        res.update(self.msg_test("PaymentMonthCardGetRewardsMsg"))

        return res

    def paymet_test(self):
        res = {}

        res.update(self.msg_test("PaymentBuyMsg"))

        return res

    def progressReward_test(self):
        res = {}

        res.update(self.msg_test("ProgressRewardMsg"))

        return res

    def repeatable_challenge_test(self):
        res = {}

        res.update(self.msg_test("RepeatableChallengeGetRewardsMsg"))

        return res

    def rodAttach_test(self):
        res = {}

        res.update(self.msg_test("SaveRodAttachMsg"))

        res.update(self.msg_test("SeeRodAttachMsg"))

        res.update(self.msg_test("UpdateRodAttachDBMsg"))

        return res

    def roulette_test(self):
        res = {}

        res.update(self.msg_test("RouletteDrawMsg"))

        return res

    def selfRank_test(self):
        res = {}

        res.update(self.msg_test("SelfRankLikesMsg"))

        res.update(self.msg_test("SelfRankRecordMsg"))

        return res

    def shop_test(self):
        res = {}

        res.update(self.msg_test("ShopRefreshMsg"))

        res.update(self.msg_test("ShopBuyItemMsg"))

        return res

    def sign_gift_test(self):
        res = {}

        res.update(self.msg_test("SignGiftSignMsg"))

        return res

    def small_func_test(self):
        res = {}

        # res.update(self.msg_test("ReportMsg"))

        # res.update(self.msg_test("DoneSharingMsg"))

        # res.update(self.msg_test("DoneFollowMsg"))

        res.update(self.msg_test("DoneQuestionnaireMsg"))

        # res.update(self.msg_test("DoneQuestionnaireCell"))

        # res.update(self.msg_test("QuestionnaireAnswer"))

        res.update(self.msg_test("GetDLCNodeRewardsMsg"))

        return res

    def system_test(self):
        res = {}

        # res.update(self.msg_test("PingMsg"))

        res.update(self.msg_test("QueryCharInfoMsg"))

        # res.update(self.msg_test("LikeQueryCharInfoMsg"))
        #
        # res.update(self.msg_test("RecordPaymentMsg"))

        return res

    def talentTree_test(self):
        res = {}

        res.update(self.msg_test("TalentLvUpMsg"))

        res.update(self.msg_test("TalentUnlockMsg"))

        return res

    def trigger_gift_test(self):
        res = {}

        res.update(self.msg_test("TriggerGiftTryTriggerMsg"))

        return res

    def main(self):
        res = {}
        res.update(self.achieve_test())
        res.update(self.achieveCategory_test())
        res.update(self.achieveWanted_test())
        res.update(self.activationCode_test())
        res.update(self.aquarium_test())
        res.update(self.backPack_test())
        res.update(self.baitAndRod_test())
        res.update(self.battlePass_test())
        res.update(self.championships_test())
        res.update(self.chara_test())
        res.update(self.chest_test())
        res.update(self.commonExchange_test())
        res.update(self.division_test())
        res.update(self.double_week_rank_test())
        res.update(self.duel_test())
        res.update(self.fish_card_test())
        res.update(self.flashcard_test())
        res.update(self.globalRank_test())
        res.update(self.guild_test())
        res.update(self.guildDragon_test())
        res.update(self.hidden_treasure_test())
        res.update(self.mail_test())
        res.update(self.mission_test())
        res.update(self.monopoly_test())
        res.update(self.newGuide_test())
        res.update(self.n_days_event_test())
        res.update(self.paymetMothCard_test())
        res.update(self.paymet_test())
        res.update(self.progressReward_test())
        res.update(self.repeatable_challenge_test())
        res.update(self.rodAttach_test())
        res.update(self.roulette_test())
        res.update(self.selfRank_test())
        res.update(self.shop_test())
        res.update(self.sign_gift_test())
        res.update(self.small_func_test())
        res.update(self.system_test())
        res.update(self.talentTree_test())
        res.update(self.trigger_gift_test())
        return res


if __name__ == '__main__':
    bp = BasePage(serial_number="b6h65hd64p5pxcyh")
    netMsgTest = NetMsgTest(bp)
    r = netMsgTest.main()
    false_keys = [k for k, v in r.items() if not v]
    print(false_keys)
    bp.connect_close()

    # a = chara_test(bp)
    # print(a)

    # guildSimpleId = 10000012
    # lua_code = csMsgAll.get_CSHiddenTreasureSetMultipleMsg(multiple=50, stageId=1, groupId=6000001, roomId=1000298)
    # bp.lua_console(lua_code)
    # bp.connect_close()
