
class ElementsData:
    Panels = {"locator": "UICanvas>>"}

    class AchievementGroup:
        AchievementGroupPanel = {"locator": "UICanvas>Default>AchievementGroupPanel"}
        btn_close = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>btn_close>img"}
        text_100000 = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>resource_bar>top_resource>100000>value"}
        item_icon_list = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_preview>item_list>>icon"}
        item_quantity_list = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_preview>item_list>>quantity>value"}
        box = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>bar_rewards>Rewards>btn_collect>item"}
        box_collectable = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>bar_rewards>Rewards>particle"}
        progress = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>bar_rewards>text"}
        achievement_list = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>List>Viewport>Content>"}
        achievement_icon_list = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>List>Viewport>Content>>iconbg>icon"}
        achievement_bg_icon_list = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>List>Viewport>Content>>iconbg"}
        achievement_collectable_list = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>List>Viewport>Content>>tip_reward_bubble>bg>arrow"}
        icon_main = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_preview>iconbg>icon"}
        btn_collect = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_preview>btn_rewards"}
        btn_go = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_preview>btn_go>btn_normal"}
        title = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>title_group>title"}
        complete = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_value>exp_value>value"}

    class Achievement:
        AchievementPanel = {"locator": "UICanvas>Default>AchievementPanel"}
        achievement_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>"}
        btn_close = {"locator": "UICanvas>Default>AchievementPanel>panel>btn_close>img"}
        btn_i = {"locator": "UICanvas>Default>AchievementPanel>panel>title_group>btn_i"}
        tips = {"locator": "UICanvas>Default>AchievementPanel>panel>title_group>btn_i>tips"}
        tips_unlock = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>tips_unlock"}
        task_mini_icon = {"locator": "UICanvas>Default>AchievementPanel>panel>task_mini>icon"}
        viewport = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport", "focus": (0, 0)}
        achievement_icon_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>group_com>icon_gray"}
        achievement_group_name_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>group_com>groupbg>groupname"}

    class Aquarium:
        AquariumPanel = {"locator": "UICanvas>Default>AquariumPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumPanel>panel>btn_close>img"}

    class AquariumCommonFishChange:
        AquariumCommonFishChangePanel = {"locator": "UICanvas>Default>AquariumCommonFishChangePanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumCommonFishChangePanel>panel>btn_close>tip"}
    class BaitAndRodAlbum:
        BaitAndRodAlbumPanel = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel"}
        btn_close = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>btn_close>img"}
        btn_filter = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>btn_filter>btn_normal"}
        tab_rod = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>tab>tab_1>bg"}
        tab_bait = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>tab>tab_2>bg"}
        tab_list = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>tab>>bg"}
        panel_bag_rod = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_bag_rod"}
        panel_bag_bait = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_bag_bait"}
        options = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>>options"}
        toggle_hide_unowned = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>>options>option_0>Toggle"}
        toggle_rarity_list = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>>options>type_1>>Toggle"}
        toggle_available_location_list = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>>options>type_2>>Toggle"}
        btn_apply = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>>btns>btn_apply>btn_normal"}
        btn_reset = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>panel_tab>>btns>btn_reset>btn_normal"}
        model_list = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>>List>Viewport>Content>>model"}
        Viewport = {"locator": "UICanvas>Default>BaitAndRodAlbumPanel>panel>>List>Viewport", "focus": (0, 0)}

    class BaitAndRodShow:
        BaitAndRodShowPanel = {"locator": "UICanvas>Default>BaitAndRodShowPanel"}
        closeArea = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>closeArea"}
        talent = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>panel_rod_info>panel_right>content>bg>sign"}
        tips_talent = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>tips_talent"}
        five_dimension ={"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>panel_rod_info>5d>bg"}
        tips_five_dimension = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>tips_5d"}
        name = {"locator":"UICanvas>Default>BaitAndRodShowPanel>panel>>panel_right>content>bg>nameBG>name"}

    class BattleExplain:
        BattleExplainPanel = {"locator": "UICanvas>Default>BattleExplainPanel"}
        close = {"locator": "UICanvas>Default>BattleExplainPanel>close"}

    class BattleFailed:
        BattleFailedPanel = {"locator": "UICanvas>Default>BattleFailedPanel"}
        btn_cancel = {"locator": "UICanvas>Default>BattleFailedPanel>panel_fail>btns>btn_cancel>btn_normal"}
        btn_again = {"locator": "UICanvas>Default>BattleFailedPanel>panel_fail>btns>btn_again>btn_normal"}

    class Battle:
        BattlePanel = {"locator": "UICanvas>Default>BattlePanel"}
        btn_reel = {"locator": "UICanvas>Default>BattlePanel>btn_cast>btn"}
        tip_slide = {"locator": "UICanvas>Default>BattlePanel>btn_cast>tip_slide"}

    class BattlePassBuyLevel:
        BattlePassBuyLevelPanel = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>btn_close>img"}
        btn_buy_text = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>btns>btn_confirm>text"}
        btn_buy_disabled = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>btns>btn_confirm>btn_disabled"}
        btn_add = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>btn_add>img"}
        btn_sub = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>btn_sub>img"}
        level_cal = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>title>title"}
        btn_add_100100 = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>top_res>ResourceBar>100100>btn_add>btn_normal"}
        text_100100 = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>top_res>ResourceBar>100100>value"}
        Viewport = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport", "focus": (0, 0)}
        reward_icon_free_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>free>item>item_model_new(Clone)>icon"}
        reward_icon_premium_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>>item>item_model_new(Clone)>quantity>value"}
        reward_gear_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>>item>gear_model_new(Clone)>icon"}
        licenseLock_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>licenseLock"}
        slider = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>slider"}

    class BattlePassBuyLicense:
        BattlePassBuyLicensePanel =  {"locator": "UICanvas>Default>BattlePassBuyLicensePanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>btn_close>img"}
        btn_buy_pro = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>panel_right>btn>text"}
        btn_buy_standard = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>panel_left>btn>text"}

    class BattlePassIntro:
        BattlePassIntroPanel = {"locator": "UICanvas>Default>BattlePassIntroPanel"}
        time = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>info>time>text"}
        panel1 = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>01"}
        panel2 = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>02"}
        panel3 = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>03"}
        panel1to2Btn = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>01>panel1to2Btn>img"}
        next1to2 = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>01>next1to2>btn_normal"}
        panel2to1Btn = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>02>panel2to1Btn>img"}
        panel2to3Btn = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>02>panel2to3Btn>img"}
        next2to3 = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>02>next2to3>btn_normal"}
        panel3to2Btn = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>03>panel3to2Btn>img"}
        btn_go = {"locator": "UICanvas>Default>BattlePassIntroPanel>panel_BP_pictips>03>go>btn_normal"}

    class BattlePass:
        BattlePassPanel = {"locator": "UICanvas>Default>BattlePassPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>btn_close>img"}
        btn_detail = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_left>rewards_preview>btn_detall"}
        time = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_left>rewards_preview>info>time>text"}
        btn_i = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>title_group>btn_i>img"}
        exp = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>exp"}
        btn_task = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>btns>btn_task>btn_normal"}
        btn_buy = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>btns>btn_buy>btn_normal"}
        btn_premium = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>title_group>lock>btn", "focus": (0, 0.5)}
        btn_unlock = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>btns>btn_unlock>btn_normal"}
        btn_collect = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>btns>btn_collect>btn_normal"}
        exp_value = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>exp_value>value"}
        exp_value_max = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>exp_value>value2"}
        level = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>level>value"}
        Viewport = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport", "focus": (0, 0)}
        particle_claim_free_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>free>particle_claim"}
        particle_claim_premium_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>premium>particle_claim"}
        reward_icon_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>>item>item_model_new(Clone)>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>>item>item_model_new(Clone)>quantity>value"}
        reward_gear_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>>item>gear_model_new(Clone)>icon"}
        licenseLock_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>licenseLock>lock"}
        title_bg = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>title_bg>img_1"}
        preview_item_icon_list ={"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>list_preview>reward_model>model>>item>item_model_new(Clone)>icon"}
        preview_gear_icon_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>list_preview>reward_model>model>>item>gear_model_new(Clone)>icon"}
        btn_i_goldbank = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>goldbank>btn_i>img"}
        Tip_goldbank = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>Tip_goldbank"}

    class BattlePassPop:
        BattlePassPopPanel = {"locator": "UICanvas>Default>BattlePassPopPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>btn_close>img"}
        btn_confirm = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>btns>btn_confirm>btn_normal"}
        Viewport = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>panel_advertisement>panel_premium>List>Viewport", "focus": (0, 0)}
        icon_list = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>panel_advertisement>panel_premium>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}

    class BattlePassReward:
        BattlePassRewardPanel = {"locator": "UICanvas>Default>BattlePassRewardPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>btn_close>tip"}
        btn_unLock = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>unLockBtn>btn_normal"}
        reward_icon_free_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>item_model_new(Clone)>icon"}
        reward_quantity_free_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>item_model_new(Clone)>quantity>value"}
        reward_gear_free_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>gear_model_new(Clone)>icon"}
        reward_icon_premium_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}
        reward_quantity_premium_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>quantity>value"}
        reward_gear_premium_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>gear_model_new(Clone)>icon"}
        Viewport_free = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport", "focus": (0, 0)}
        Viewport_premium = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport", "focus": (0, 0)}

    class BattlePrepare:
        BattlePreparePanel = {"locator": "UICanvas>Default>BattlePreparePanel"}
        btn_gohome = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_gohome>btn_gohome>img"}
        quick_switch = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>quick_switch>btn_quick_switch>btn_normal"}
        btn_i = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>quick_switch>btn_i>img"}
        rod_model = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>rod>rod_model>gear_model_new(Clone)>icon"}
        bait_model = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>bait>rod_model>gear_model_new(Clone)>icon"}
        rod = {"locator": "RodRoot>"}
        bait = {"offspring_locator": "RodRoot>000>rod001>LineBone_Start>LineBone_End>"}
        btn_switch_gear_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>>btn_switch>btn_normal"}
        btn_switch_item_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>btn_switch>bg"}
        item_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>icon"}
        item_quantity_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>quantity>value"}
        switch_tip_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>switch_tip>items>>icon"}
        switch_tip_quantity_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>switch_tip>items>>quantity>value"}
        tag_equipped = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>switch_tip>items>>tag_equipped"}
        panel_gears_switch = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch"}
        btn_cast = {"locator": "UICanvas>Default>BattlePreparePanel>>>btn_cast>btn_normal"}

    class BuyEnergy:
        BuyEnergyPanel = {"locator": "UICanvas>Default>BuyEnergyPanel"}
        btn_close = {"locator": "UICanvas>Default>BuyEnergyPanel>btn_close>text"}
        btn_drink = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>drink>btn>btn_normal"}
        remaining_drink_value = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>drink>remaining>value"}
        btn_cash = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>cash>btn>text"}
        text_100100 = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>100100>value"}
        text_100500 = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>100500>value"}
        btn_add_100100 = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>100100>btn_add>btn_normal"}

    class ChampointshipResult:
        ChampointshipResultPopup = {"locator":"UICanvas>Default>ChampointshipResultPopup"}
        btn_collect = {"locator":"UICanvas>Default>ChampointshipResultPopup>panel>btn_close>btn_normal"}

    class ChampoinshipTournaments:
        ChampoinshipTournamentsPanel = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel"}
        btn_fold = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_bg>btn_fold>arrow"}
        btn_unfold = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar_fold>panel"}

        logo_big = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>target>logo_big"}
        location = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>target>loaction>text"}
        time = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>target>time>text"}
        tab_rank = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>subtab>tab_1>bg"}
        tab_rewards = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>subtab>tab_2>bg"}
        tab_targets = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>subtab>tab_3>bg"}
        rank_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>Viewport>Content>>num_value"}
        head_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>Viewport>Content>>head>head_mask>head_img"}
        player_name_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>Viewport>Content>>player_name"}
        flag_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>Viewport>Content>>flag"}
        rank_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>list_myself>num_value"}
        head_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>list_myself>head>head_mask>head_img"}
        player_name_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>list_myself>player_name"}
        flag_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>>list_myself>flag"}
        points_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_ranking>list_myself>points_value"}
        points_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_ranking>Viewport>Content>>points_value"}
        reward_1_icon_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>list_myself>rewards>reward_1>icon"}
        reward_2_icon_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>list_myself>rewards>reward_2>icon"}
        reward_1_value_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>list_myself>rewards>reward_1>value"}
        reward_2_value_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>list_myself>rewards>reward_2>value"}
        reward_1_icon_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>Viewport>Content>>rewards>reward_1>icon"}
        reward_2_icon_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>Viewport>Content>>rewards>reward_2>icon"}
        reward_1_value_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>Viewport>Content>>rewards>reward_1>value"}
        reward_2_value_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>Viewport>Content>>rewards>reward_2>value"}
        reward_3_icon_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>list_myself>rewards>reward_1>icon"}
        reward_3_value_myself = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>list_myself>rewards>reward_1>value"}
        reward_3_icon_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>Viewport>Content>>rewards>reward_1>icon"}
        reward_3_value_list = {"locator": "UICanvas>Important>ChampoinshipTournamentsPanel>panel_sidebar>panel>panel_ing>panel_rewards>Viewport>Content>>rewards>reward_1>value"}

    class CommonPurchaseBox:
        CommonPurchaseBoxVIew = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew"}
        btn_close = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew>Panel>btn_close>img"}
        btn_purchase = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew>Panel>btn>btn_purchase>btn_normal"}
        item_icon = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew>Panel>item_info>item>item_model_mini>icon"}
        item_quantity = {"locator": "UICanvas>Default>CommonPurchaseBoxVIew>Panel>item_info>info>quantity>value"}
        cost_icon = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>cost_detail>icon"}
        cost_quantity = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>cost_detail>value"}
        btn_add = {"locator": "UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>btn_add"}
        btn_sub = {"locator":"UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>btn_sub"}
        btn_max = {"locator": "UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>btn_max"}
        btn_min = {"locator": "UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>btn_min"}
        slider = {"locator": "UICanvas>Default>CommonPurchaseBoxVIew>Panel>cost>slider"}

    class DivisionChange:
        DivisionChangePanel = {"locator":"UICanvas>Default>DivisionChangePanel"}
        tap_to_close = {"locator":"UICanvas>Default>DivisionChangePanel>Panel>btn_close>text"}

    class EntryUpdateLoading:
        EntryUpdateLoading = {"locator": "GameUpdater>Canvas>EntryUpdateLoading"}
        tap_to_start = {"locator": "GameUpdater>Canvas>EntryUpdateLoading>panel_go>Button_Login>Text"}

    class FishBag:
        tap_to_continue = {"locator": "UICanvas>Default>FishBagPanel>text"}
        FishBagPanel = {"locator": "UICanvas>Default>FishBagPanel"}

    class FishCardGiftPack:
        FishCardGiftPackPanel = {"locator": "UICanvas>Default>FishCardGiftPackPanel"}
        btn_close = {"locator": "UICanvas>Default>FishCardGiftPackPanel>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>FishCardGiftPackPanel>panel>btns>btn_buy"}
        icon_list = {"locator": "UICanvas>Default>FishCardGiftPackPanel>panel>main>>>item_model_mini(Clone)>icon"}
        quantity_list = {"locator": "UICanvas>Default>FishCardGiftPackPanel>panel>main>>>item_model_mini(Clone)>quantity>value"}

    class FishCardPackTips:
        FishCardPackTipsPanel = {"locator": "UICanvas>Default>FishCardPackTipsPanel"}
        item_icon = {"locator": "UICanvas>Default>FishCardPackTipsPanel>bg>list>fishbag>icon"}
        fish_card_name = {"locator": "UICanvas>Default>FishCardPackTipsPanel>bg>list>fishbag>title_bg>title"}

    class FishCard:
        FishCardPanel = {"locator": "UICanvas>Default>FishCardPanel"}
        fisheries_model_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fisheries>content>FisheriesList>Viewport>Content>"}
        fisheries_bg_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fisheries>content>FisheriesList>Viewport>Content>>bg"}
        fisheries_viewport = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fisheries>content>FisheriesList>Viewport", "focus": (0, 0)}
        fisheries_title_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fisheries>content>FisheriesList>Viewport>Content>>title"}
        btn_close = {"locator": "UICanvas>Default>FishCardPanel>btn_close>img"}
        btn_upgrade = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>upgrade>normal>btn_upgrade", "focus": (0.2, 0.8)}
        talent_now_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>upgrade>normal>detail_list>Viewport>Content>>now>title"}
        talent_next_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>upgrade>normal>detail_list>Viewport>Content>>next>title"}
        main_name = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>content>name>name"}
        main_size = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>content>name>size"}
        fish_card_model_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>"}
        fish_card_viewport = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport", "focus": (0, 0)}
        fisheries_name_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>>name"}
        fish_name_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>>title_bg>fisheries"}
        progress_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>>kind_02>progress>text"}
        level_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>>kind_02>level_bg>number"}
        talent_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>>kind_02>talent_bg>text"}
        title_bg_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>>title_bg"}
        fisheries_name_selected = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>FishCard_on>>name"}
        fish_name_selected = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>FishCard_on>>title_bg>fisheries"}
        progress_selected = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>FishCard_on>>kind_02>progress>text"}
        level_selected = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>FishCard_on>>kind_02>level_bg>number"}
        talent_selected = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>FishCard_on>>kind_02>talent_bg>text"}
        title_bg_selected = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_fishcard>content>FishCardList>Viewport>content>FishCard_on>>title_bg"}
        btn_add_100000 = {"locator": "UICanvas>Default>FishCardPanel>top_res>ResourceBar>100000>btn_add>btn_normal"}
        btn_add_100100 = {"locator": "UICanvas>Default>FishCardPanel>top_res>ResourceBar>100100>btn_add>btn_normal"}
        btn_add_100500 = {"locator": "UICanvas>Default>FishCardPanel>top_res>ResourceBar>100500>btn_add>btn_normal"}
        res_icon_list = {"locator": "UICanvas>Default>FishCardPanel>top_res>ResourceBar>>icon"}
        res_value_list = {"locator": "UICanvas>Default>FishCardPanel>top_res>ResourceBar>>value"}
        btn_events = {"locator": "UICanvas>Default>FishCardPanel>panel>btn_events>img"}

    class FishCardUpgrade:
        FishCardUpgradePanel = {"locator": "UICanvas>Default>FishCardUpgradePanel"}
        btn_close = {"locator": "UICanvas>Default>FishCardUpgradePanel>btn_close>text"}
        btn_level_up = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>btns>btn_draw", "focus": (0.5, 1)}
        talent_now_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>percentList>>now>title"}
        talent_next_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>percentList>>now>next"}
        progress = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>progress>text"}
        level_now = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>level>now"}
        level_next = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>level>next"}
        cost_value_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>btns>cost>>value_cost"}
        cost_icon_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>Content>btns>cost>>icon"}
        fisheries_name_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>name"}
        fish_name_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>title_bg>fisheries"}
        progress_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>kind_02>progress>text"}
        level_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>kind_02>level_bg>number"}
        talent_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>kind_02>talent_bg>text"}
        title_bg_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>title_bg"}
        btn_add_100000 = {"locator": "UICanvas>Default>FishCardPanel>top_res>ResourceBar>100500>btn_add>btn_normal"}
        text_100000 = {"locator": "UICanvas>Default>FishCardUpgradePanel>top_res>ResourceBar>100000>value"}

    class FisheryGiftPack:
        FisheryGiftPackPanel = {"locator": "UICanvas>Default>FisheryGiftPackPanel"}
        btn_close = {"locator": "UICanvas>Default>FisheryGiftPackPanel>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>FisheryGiftPackPanel>panel>btns>btn_buy>btn_normal"}
        icon_list = {"locator": "UICanvas>Default>FisheryGiftPackPanel>panel>main>item_list>>item_model_mini(Clone)>icon"}
        quantity_list = {"locator": "UICanvas>Default>FisheryGiftPackPanel>panel>main>item_list>>item_model_mini(Clone)>quantity>value"}

    class FlashTips:
        FlashTipsPanel = {"locator": "UICanvas>Important>FlashTipsPanel"}

    class Gear:
        GearPanel = {"locator": "UICanvas>Default>GearPanel"}
        btn_close = {"locator": "UICanvas>Default>GearPanel>btn_close>img"}
        tab = {"locator": "UICanvas>Default>GearPanel>navbar_tab>bg"}
        tab_info = {"locator": "UICanvas>Default>GearPanel>navbar_tab>bg>tab_1>normal"}
        tab_level_up = {"locator": "UICanvas>Default>GearPanel>navbar_tab>bg>tab_2>normal"}
        tab_enhance = {"locator": "UICanvas>Default>GearPanel>navbar_tab>bg>tab_3>normal"}
        tab_draw = {"locator": "UICanvas>Default>GearPanel>navbar_tab>bg>tab_4>normal"}
        panel_info = {"locator": "UICanvas>Default>GearPanel>panel_info"}
        panel_upgrade = {"locator": "UICanvas>Default>GearPanel>panel_upgrade"}
        panel_enhance = {"locator": "UICanvas>Default>GearPanel>panel_enhance"}
        panel_draw = {"locator": "UICanvas>Default>GearPanel>panel_draw"}
        btn_next = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>arrow>btn_next>img"}
        btn_previous = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>arrow>btn_previous>img"}
        rating = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>rating>value"}
        name = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>name>bg>name"}
        kind = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>name>btn_kind>img"}
        tips_discribe = {"locator":"UICanvas>Default>GearPanel>tips_discribe"}
        stars = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>name>stars"}
        level = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>detail>level>text"}
        damage = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>detail>damage>text"}
        btn_magnifier_open = {"locator":"UICanvas>Default>GearPanel>>panel>btn_magnifier>icon"}
        btn_magnifier_close = {"locator":"UICanvas>Default>GearPanel>panel_show>btn_magnifier"}
        img_5d =  {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>5d>bg"}
        value_5d_list = {"locator":"UICanvas>Default>GearPanel>tips_5d>bg>list>>current>num"}
        tips_5d = {"locator":"UICanvas>Default>GearPanel>tips_5d"}
        talent = {"locator":"UICanvas>Default>GearPanel>panel_basic_info>panel>talent", "focus": (1, 1)}
        tips_talent = {"locator":"UICanvas>Default>GearPanel>tips_talent"}
        btn_add_100000 = {"locator": "UICanvas>Default>GearPanel>top_res>ResourceBar>100000>btn_add>btn_normal"}
        res_icon_list = {"locator": "UICanvas>Default>GearPanel>top_res>ResourceBar>>icon"}
        res_value_list = {"locator": "UICanvas>Default>GearPanel>top_res>ResourceBar>>value"}
        class Info:
            attribute_icon_list = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>attribute_list>Viewport>Content>>normal>icon"}
            attribute_add_list = {"locator":"UICanvas>Default>GearPanel>panel_info>panel>attribute_list>Viewport>Content>>add>text"}
            attribute_lock_list = {"locator":"UICanvas>Default>GearPanel>panel_info>panel>attribute_list>Viewport>Content>>lock>text"}
            attribute_value_list = {"locator":"UICanvas>Default>GearPanel>panel_info>panel>attribute_list>Viewport>Content>>normal>progress>text"}
            attribute_text_list = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>attribute_list>Viewport>Content>>normal>text", "focus": (0, 0.5)}
            EffectTips = {"locator": "UICanvas>Default>EffectTipsPanel>panel>title_group>title"}
            select = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>attribute_list>Viewport>Content>>select"}

        class Upgrade:
            level = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>level_change>text_now"}
            level_next = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>level_change>text_net"}
            level_select = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>title>value"}
            level_denominator = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>title>max"}
            rating = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>list>rating>value"}
            rating_next = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>list>rating>value_next"}
            damage = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>list>damage>value"}
            damage_next = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>list>damage>value_next"}
            btn_add = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>progress>btn_add>img"}
            btn_sub = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>progress>btn_sub>img"}
            cost_value_list = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>cost>>value"}
            cost_icon_list = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>cost>>icon"}
            btn_upgrade = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>normal>btn_upgrade","focus": (0.5, 1)}
            max = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>max"}
            level_max = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>max>max_level>text_now"}
            rating_max = {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>max>list>rating>value_next"}
            damage_max =  {"locator": "UICanvas>Default>GearPanel>panel_upgrade>content>max>list>damage>value_next"}

        class Enhance:
            stars = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>normal>star_change>stars_now"}
            stars_next = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>normal>star_change>stars_next"}
            stars_max = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>max>stars_max"}
            rating = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>normal>list>rating>value"}
            rating_next = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>normal>list>rating>value_next"}
            rating_max = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>max>list>rating>value_next"}
            value_5d_list = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>normal>list>5d>5d_list>>text_incrase"}
            value_5d_max_list =  {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>max>list>5d>5d_list>>text_incrase"}
            btn_enhance = {"locator": "UICanvas>Default>GearPanel>panel_enhance>content>normal>btn_enhance"}

        class Draw:
            tab_perk = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>tab>tab_1>bg"}
            tab_value = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>tab>tab_2>bg"}
            name = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>name>text"}
            rating = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>rating>value"}
            cost_perk_glod = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>cost_1>res_1>value_cost"}
            icon_perk_glod = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>cost_1>res_1>icon"}
            cost_perk = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>cost>res_1>value_cost"}
            icon_perk = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>cost>res_1>icon"}
            btn_draw_perk_glod = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>btn_draw_1","focus": (0.5, 1)}
            btn_draw_perk= {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>btn_draw", "focus": (0.5, 1)}
            btn_save = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>panel>btns>btn_save", "focus": (0.5, 1)}
            cost_value_10 = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>btns>Draw10>cost>res_1>value_cost"}
            icon_value_10 = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>btns>Draw10>cost>res_1>icon"}
            cost_value = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>btns>Draw1>cost>res_1>value_cost"}
            icon_value = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>btns>Draw1>cost>res_1>icon"}
            btn_draw_value_10 = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>btns>Draw10>btn_draw","focus": (0.5, 1)}
            btn_draw_value = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>btns>Draw1>btn_draw", "focus": (0.5, 1)}
            value_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>panel>machine>draw_list>>text"}
            perk_icon_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>>panel>machine>draw_list>>icon"}
            perk_text_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>>panel>machine>draw_list>>title"}
            perk_value_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>>panel>machine>draw_list>>text"}
            viewport_attribute = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>attribute_list>Viewport"}
            attribute_icon_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>attribute_list>Viewport>Content>>normal>icon"}
            attribute_text_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>attribute_list>Viewport>Content>>normal>text"}
            attribute_value_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>attribute_list>Viewport>Content>>normal>progress>text"}
            attribute_add_list = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>attribute_list>Viewport>Content>>add"}
            tips_draw_value = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>value>tips"}
            select = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>panel_left>content>attribute_list>Viewport>Content>>select"}
            Panel_Tip = {"locator": "UICanvas>Default>GearPanel>panel_draw>panel>id>effect_tips>>Panel_Tip"}

    class Home:
        # 大厅
        # panel_events
        HomePanel = {"locator": "UICanvas>Default>HomePanel"}
        btn_questionnaire = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_questionnaire>img"}
        btn_roulette = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_roulette>img"}
        btn_iaa = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_iaa>img"}
        btn_endless = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_endless>img"}
        btn_bp = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>btn_bp>bg"}
        btn_1add1 = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_1add1>img"}
        btn_black5 = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_black5>img"}
        # panel_entrance
        btn_pve = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>btn_pve>btn_normal"}
        btn_pvp = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>btn_pvp>btn_normal"}
        btn_album = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>btn_album>btn_normal"}
        btn_next = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>page_arrow>btn_next>img"}
        btn_previous = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>page_arrow>btn_previous>img"}
        task_mini = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>task_mini>bg"}
        # panel_player_info
        btn_event_location = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>giftpack>btn_event_location", "focus": (1, 0.5)}
        btn_mail = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btn_mail>bg"}
        btn_exp_buff = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btn_exp_buff>icon"}
        Panel_tip = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btn_exp_buff>Panel_tip"}
        player_info = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>bg"}
        player_name = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>player_name"}  # text
        player_lv = {"locator":"UICanvas>Default>HomePanel>panel>panel_player_info>player_info>player_exp>player_lv>value"}  # text
        exp = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>player_exp>exp"}  # value
        ResourceBar = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar"}
        # btn_add
        btn_add_100500 = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>100500>btn_add>btn_normal"}
        btn_add_100000 = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>100000>btn_add>btn_normal"}
        btn_add_100100 = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>100100>btn_add>btn_normal"}
        # navbar
        btn_chest = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_chest"}
        btn_gears = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_gears"}
        btn_task_main = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_task_main"}
        btn_task = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_task"}
        btn_store = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_store"}
        btn_task_rookie = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_task_rookie"}
        btn_achievement = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_achievement"}

    class IAA:
        IAAPanel= {"locator": "UICanvas>Default>IAAPanel"}
        btn_close = {"locator": "UICanvas>Default>IAAPanel>panel>btn_close>img"}


    class ItemTips:
        ItemTipsPanel = {"locator": "UICanvas>Default>ItemTipsPanel"}
        title = {"locator": "UICanvas>Default>ItemTipsPanel>panel>title_bg>title"}
        icon = {"locator": "UICanvas>Default>ItemTipsPanel>panel>bg>patterns1>icon"}
        quantity = {"locator": "UICanvas>Default>ItemTipsPanel>panel>info>quantity>value"}

    class LeaderBoardPopResult:
        LeaderBoardPopResultPanel = {"locator":"UICanvas>Default>LeaderBoardPopResultPanel"}
        btn_claim = {"locator":"UICanvas>Default>LeaderBoardPopResultPanel>Panel>btn_collect>btn_normal"}

    class Loading:
        LoadingPanel = {"locator": "UICanvas>Default>LoadingPanel"}

    class LoadingFishery:
        LoadingFisheryPanel = {"locator": "UICanvas>Default>LoadingFisheryPanel"}

    class Login:
        LoginPanel = {"locator": "UICanvas>Default>LoginPanel"}
        InputField_UserName = {"locator": "UICanvas>Default>LoginPanel>panel_internal>InputField_UserName"}
        btn_login = {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login>btn_normal"}
        Dropdown = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Label"}
        DropdownList_Viewport = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport", "focus": (0, 0)}
        DropdownList = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>"}
        dev_server = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>Item 0: dev server"}
        dev_qa_server = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>Item 1: dev-qa server"}
        dev_release_server = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>Item 2: dev-release server"}

    # 邮箱
    class Mail:
        MailPanel = {"locator": "UICanvas>Default>MailPanel"}
        btn_close = {"locator": "UICanvas>Default>MailPanel>btn_close>img"}
        EmptyMailTip = {"locator": "UICanvas>Default>MailPanel>EmptyMailTip"}
        MailDetail = {"locator": "UICanvas>Default>MailPanel>MailDetail"}
        tab_list = {"locator": "UICanvas>Default>MailPanel>MailList>tab_switch>>bg"}
        mail_list = {"locator": "UICanvas>Default>MailPanel>MailList>MailArea>Scroll View>Viewport>Content>", "focus": (0.5, 0)}
        mail_Viewport = {"locator":"UICanvas>Default>MailPanel>MailList>MailArea>Scroll View>Viewport", "focus": (0, 0)}
        reward_icon_list = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>rewards>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>rewards>>quantity>value"}
        btn_claim = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>btn_group>btn_claim>btn_normal"}
        text_claimed = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>btn_group>text_claimed"}

    class MessageBox:
        MessageBoxPanel = {"locator": "UICanvas>Important>MessageBoxPanel"}
        btn_cancel = {"locator": "UICanvas>Important>MessageBoxPanel>Panel>btns>btn_cancel>btn_normal"}
        btn_confirm = {"locator": "UICanvas>Important>MessageBoxPanel>Panel>btns>btn_confirm>btn_normal"}

    class NewbieGuide:
        NewbieGuidePanel_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_1(Clone)"}
        NewbieGuidePanel_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_10(Clone)"}
        NewbieGuidePanel_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_15(Clone)"}
        NewbieGuidePanel_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_1(Clone)"}
        NBG_rookie_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_1(Clone)>Guide_VirtualBtn>text"}
        NBG_rookie_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_2(Clone)>Guide_Highlight>et_Panel_Home_New_pve"}
        NBG_rookie_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_3(Clone)>Guide_Highlight>et_Panel_Tournaments_entrance"}
        NBG_rookie_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_4(Clone)>Guide_VirtualBtn"}
        NBG_rookie_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_5(Clone)>Guide_VirtualBtn"}
        NBG_rookie_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_6(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_7 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_7(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_8 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_8(Clone)>Guide_highTension"}
        NBG_rookie_9 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_9(Clone)>Guide_VirtualBtn>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_10 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_10(Clone)>Guide_VirtualBtn"}
        NBG_rookie_11 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_11(Clone)>Guide_VirtualBtn"}
        NBG_rookie_12 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_12(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_13_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTEInfoCloseBtn>text"}
        NBG_rookie_13_Guide_QTEInfo = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTEInfo"}
        NBG_rookie_13_Guide_QTE_left = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTE_left"}
        NBG_rookie_13_Guide_ULTInfoCloseBtn = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_ULTInfoCloseBtn"}
        NBG_rookie_13_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)"}
        joystick = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTE_right>Guide_Hand_Joystick>joystick"}
        NBG_rookie_14 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_14(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_15 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_15(Clone)>Guide_VirtualBtn"}
        NBG_rookie_16 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_16(Clone)>Guide_VirtualBtn"}
        NBG_rookie_17 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_17(Clone)"}
        NBG_rookie_18 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_18(Clone)>Guide_VirtualBtn"}
        NBG_system_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_1(Clone)>Guide_VirtualBtn"}
        NBG_system_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_2(Clone)>Guide_VirtualBtn"}
        NBG_system_click_TreasureChest =  {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_click_TreasureChest(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_system_get_reward_TreasureChest_01 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_get_reward_TreasureChest_01(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_system_close_TreasureChest = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_close_TreasureChest(Clone)>Guide_Highlight>ep_UI_novice guide"}

    class PlayerEditName:
        PlayerEditNamePanel = {"locator": "UICanvas>Default>PlayerEditNamePanel"}
        btn_confirm = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>btns>btn_confirm>btn_normal"}
        Input_PlayerName = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>Input_PlayerName"}
        head_list = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>HeadList>Viewport>Content>>head>head_mask>head_img"}
        select = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>HeadList>Viewport>Content>>select"}

    class PlayerLevelup:
        PlayerLevelupPanel = {"locator":"UICanvas>Default>DivisionChangePanel"}
        tap_to_continue = {"locator":"UICanvas>Default>PlayerLevelupPanel>panel>text"}

    #  设置
    class PlayerSetting:
        PlayerSettingPanel = {"locator": "UICanvas>Default>PlayerSettingPanel"}
        btn_close = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>btn_close>img"}
        btn_close_additional = {"locator": "UICanvas>Default>PlayerSettingPanel>>Panel>btn_close>img"}
        # 左侧标签
        tab_player = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_1>title"}
        tab_setting = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_2>title"}
        tab_language = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_3>title"}
        panel_player = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo"}
        panel_setting = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting"}
        panel_language = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_language"}
        # player页面右侧按钮
        btn_edit_info = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>btn_edit>img"}
        btn_edit_badge = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_badge>btn_edit>img"}
        btn_i_badge = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_badge>btn_i>img"}
        Panel_Tip_Rules = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_badge>Panel_Tip_Rules"}
        head = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>head>head_mask"}
        btn_set_name = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>head>head_mask"}
        flag = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>flag"}  # text
        player_name = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>player_name"}  # text
        player_lv = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>player_exp>player_lv>value"}  # text
        exp = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>player_exp>exp"}  # value
        # 编辑弹窗
        Panel_Popups_Edit = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit"}
        tab_avatar = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_1>bg"}
        tab_banner = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_2>bg"}
        tab_name = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_3>bg"}
        tab_badge = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_4>bg"}
        panel_avatar = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_avatar"}
        panel_banner = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_banner"}
        panel_name = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_name"}
        panel_badge = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_badge"}
        HeadList_head_img = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_avatar>HeadList>Viewport>Content>>head>head_mask>head_img"}
        HeadList_select = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_avatar>HeadList>Viewport>Content>>head>select"}
        Input_PlayerName = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_name>Input_PlayerName"}
        btn_save_profile = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>>btn>btn_save>btn_normal"}
        btn_saved_profile = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>>btn>tip"}
        # settings页面
        options_music = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_music>slider"}
        options_sound = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_sound>slider"}
        options_music_bg = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_music>slider"}
        options_sound_bg= {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_sound>slider"}
        options_graphics_list = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_graphics>btn_switch>>text"}
        options_joystick_list = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_joystick>btn_switch>>text"}
        options_frame_list = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_frame>btn_switch>>text"}
        options_vibration_list = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_vibration>btn_switch>>text"}
        options_id = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>options_id>value"}
        btn_help = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>btns>btn_help>btn_normal"}
        btn_terms = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>btns>btn_terms>btn_normal"}
        btn_privacy = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>btns>btn_privacy>btn_normal"}
        btn_logout = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>btns>btn_logout>btn_normal"}
        google_login_btn_normal = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>google_login>btn_login>btn_normal"}
        facebook_login_btn_normal = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>facebook_login>btn_login>btn_normal"}
        google_login_btn_disabled = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>google_login>btn_login>btn_disabled"}
        facebook_login_btn_disabled = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_setting>facebook_login>btn_login>btn_disabled"}
        # language页面
        btn_save_language = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_language>btn_save>btn_normal"}
        btn_saved_language = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_language>tip"}
        language_title_list = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_language>List>Viewport>Content>>title"}
        select = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_language>List>Viewport>Content>>select"}
        Panel_Giftcode=  {"locator":"UICanvas>Default>PlayerSettingPanel>Panel_Giftcode"}



    class PVERuleTips:
        PVERuleTipsPanel = {"locator": "UICanvas>Default>PVERuleTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>PVERuleTipsPanel>Panel_Popups_Edit>Panel>btn_close>img"}

    class PVPBattleHUD:
        PVPBattleHUDPanel = {"locator": "UICanvas>Default>PVPBattleHUDPanel"}
        btn_give_up = {"locator": "UICanvas>Default>PVPBattleHUDPanel>panel_pvp_scoreboard>panel>blue>btn_surrender>btn_normal"}

    class PVPBoosterGiftPack:
        PVPBoosterGiftPackPanel = {"locator":"UICanvas>Default>PVPBoosterGiftPackPanel"}
        btn_close = {"locator":"UICanvas>Default>PVPBoosterGiftPackPanel>btn_close>img"}

    class PVPHall:
        PVPHallPanel = {"locator": "UICanvas>Default>PVPHallPanel"}
        btn_play_list = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_entrance>List>Viewport>Content>>model>btn_match>btn_normal"}
        btn_close = {"locator": "UICanvas>Default>PVPHallPanel>Panel>btn_close>img"}
        Viewport = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_entrance>List>Viewport", "focus": (0, 0)}
        entrance_list = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_entrance>List>Viewport>Content>"}
        btn_turntable = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_turntable>btn_normal"}

    class PVPMatch:
        PVPMatchPanel = {"locator":"UICanvas>Default>PVPMatchPanel"}
        btn_cancel = {"locator":"UICanvas>Default>PVPMatchPanel>panel_opponent_top>btn_cancel>btn_normal"}

    class PVPResult:
        PVPResultPanel = {"locator": "UICanvas>Default>PVPResultPanel"}
        tap_to_close = {"locator": "UICanvas>Default>PVPResultPanel>panel>result>btn_close>text"}
        points_enemy = {"locator": "UICanvas>Default>PVPResultPanel>panel>top>red>player_info>points"}
        points_mine = {"locator": "UICanvas>Default>PVPResultPanel>panel>top>blue>player_info>points"}
        btn_open = {"locator": "UICanvas>Default>PVPResultPanel>panel>result>result_detail_list>detail_list>btn_open>img"}

    class PVPRuleTipsPanel:
        PVPRuleTipsPanel = {"locator": "UICanvas>Default>PVPRuleTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>PVPRuleTipsPanel>Panel_Popups_Edit>Panel>btn_close>img"}

    class Recharge1And1:
        Recharge1And1Panel = {"locator": "UICanvas>Default>Recharge1And1Panel"}
        btn_close = {"locator": "UICanvas>Default>Recharge1And1Panel>panel_events_1and1>btn_close>img"}
        icon_list = {"locator": "UICanvas>Default>Recharge1And1Panel>panel_events_1and1>panel>>item_list>>icon"}
        btn_buy = {"locator": "UICanvas>Default>Recharge1And1Panel>panel_events_1and1>panel>pearls_higher>btn_buy", "focus": (0, 0.5)}

    class RechargeBlack5:
        RechargeBlack5Panel = {"locator": "UICanvas>Default>RechargeBlack5Panel"}
        btn_close = {"locator": "UICanvas>Default>RechargeBlack5Panel>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>btns>btn_buy"}
        btn_collect = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>btns>btn_collect"}
        # icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>>item_list>>icon"}
        icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>>item_list>>icon"}
        day1_icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>day1>item_list>>icon"}
        day1_quantity_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>day1>item_list>>quantity>value"}
        day2_icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>day2>item_list>>icon"}
        day2_quantity_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>day2>item_list>>quantity>value"}
        day3_icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>day3>item_list>>icon"}
        day3_quantity_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>list>day3>item_list>>quantity>value"}
        # day1_icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>day1>item_list>>icon"}
        # day1_quantity_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>day1>item_list>>quantity>value"}
        # day2_icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>day2>item_list>>icon"}
        # day2_quantity_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>day2>item_list>>quantity>value"}
        # day3_icon_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>day3>item_list>>icon"}
        # day3_quantity_list = {"locator": "UICanvas>Default>RechargeBlack5Panel>panel>panel_right>day3>item_list>>quantity>value"}

    class RechargeEndless:
        RechargeEndlessPanel = {"locator": "UICanvas>Default>RechargeEndlessPanel"}
        btn_close = {"locator": "UICanvas>Default>RechargeEndlessPanel>panel>btn_close>img"}
        btn_buy_list = {"locator": "UICanvas>Default>RechargeEndlessPanel>panel_list>view_port>content>>>btn_buy>text"}
        icon_list = {"locator": "UICanvas>Default>RechargeEndlessPanel>panel_list>view_port>content>>>group_list>group>icon"}
        quantity_list = {"locator": "UICanvas>Default>RechargeEndlessPanel>panel_list>view_port>content>>>group_list>group>icon>quantity>value"}
        group_list = {"locator": "UICanvas>Default>RechargeEndlessPanel>panel_list>view_port>content>>>group_list>group"}

    class Result:
        ResultPanel = {"locator": "UICanvas>Default>ResultPanel"}
        btn_claim = {"locator": "UICanvas>Default>ResultPanel>panel_result>>btn_castAgain>btn_normal"}
        class pve_result:
            panel_pve_result = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result"}
            exp = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result>rewards>exp>value"}
            btn_gohome = {
                "locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result>btns>btn_gohome>btn_normal"}
            btn_nextFish = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result>btn_nextFish>btn_normal"}
            btn_i_tip = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result>points>btn_i_tip>img"}
            panel_result_sundries = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result_sundries"}
            btn_open_and_cast_again ={"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result_sundries>btns>btn_big>btn_normal"}
            btn_throw = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result_sundries>rewards>btn_throw>btn_normal"}
            btn_open_by_key = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result_sundries>btns>btn_open_right1>btn_normal"}
            btn_open_by_cash = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result_sundries>btns>btn_open_right2>btn_normal"}
            icon_sundries = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result>panel_result_sundries>rewards>icon"}

    class Rewards:
        RewardsPanel = {"locator": "UICanvas>Default>RewardsPanel"}
        tap_to_claim = {"locator": "UICanvas>Default>RewardsPanel>panel>text", "focus": (1, 0.5)}
        reward_icon_list = {"locator": "UICanvas>Default>RewardsPanel>panel>rewards_list>Viewport>Content>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>RewardsPanel>panel>rewards_list>Viewport>Content>>quantity>value"}

    class RewardsPreview:
        RewardsPreviewPanel = {"locator": "UICanvas>Default>RewardsPreviewPanel"}
        reward_icon_list = {"locator": "UICanvas>Default>RewardsPreviewPanel>panel>Content>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>RewardsPreviewPanel>panel>Content>>quantity>value"}

    class RodMoreToOne:
        RodMoreToOnePanel = {"locator": "UICanvas>Default>RodMoreToOnePanel"}
        icon_list = {"locator": "UICanvas>Default>RodMoreToOnePanel>list>Viewport>Content>>model>icon"}
        tipsBtn_list = {"locator": "UICanvas>Default>RodMoreToOnePanel>list>Viewport>Content>>tipsBtn"}
        btn_close = {"locator": "UICanvas>Default>RodMoreToOnePanel>btn_close>img"}
        btn_confirm = {"locator": "UICanvas>Default>RodMoreToOnePanel>btn>btn_normal"}

    class Rookie:
        btn_close = {"locator": "UICanvas>Default>RookiePanel>panel_result>btn_close>btn_normal"}

    class Roulette:
        RoulettePanel = {"locator": "UICanvas>Default>RoulettePanel"}
        btn_close = {"locator": "UICanvas>Default>RoulettePanel>Panel>btn_close>img"}
        btn_i = {"locator": "UICanvas>Default>RoulettePanel>Panel>level>btn_i>img"}
        btn_spin = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>btn_spin>img_text_green_spin"}
        cost = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>btn_spin>cost>value"}
        ticket_count = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>quantity>Text"}
        item_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>turntable>turntable_1>"}
        turntable_lv = {"locator": "UICanvas>Default>RoulettePanel>Panel>level>turntable_lv>value"}
        level_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>level>level>"}
        turntable_icon_list =  {"locator":"UICanvas>Default>RoulettePanel>Panel>turntable>turntable_1>>icon"}
        reward_icon_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>reward>reward>List>Viewport>Content>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>reward>reward>List>Viewport>Content>>value"}

    class Store:
        StorePanel = {"locator": "UICanvas>Default>StorePanel"}
        tab_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab>content>TabList>Viewport>Content>", "focus":(0, 0.5)}
        panel_gift_pack = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1"}
        panel_resource = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2"}
        panel_cash = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3"}
        panel_box = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4"}

        btn_close = {"locator": "UICanvas>Default>StorePanel>Panel>btn_close>img"}
        # time = {"locator": "UICanvas>Default>TreasureChestMerchantPanel>Panel>time>text"}
        ResourceBar = {"locator": "UICanvas>Default>StorePanel>Panel>top_res>ResourceBar"}
        text_100100 = {"locator": "UICanvas>Default>StorePanel>Panel>top_res>ResourceBar>100100>value"}
        text_100000= {"locator": "UICanvas>Default>StorePanel>Panel>top_res>ResourceBar>100000>value"}
        # btn_add
        btn_add_100100 = {"locator": "UICanvas>Default>StorePanel>Panel>top_res>ResourceBar>100100>btn_add>btn_normal"}
        btn_add_100000 = {"locator": "UICanvas>Default>StorePanel>Panel>top_res>ResourceBar>100000>btn_add>btn_normal"}
        btn_buy_list = {"locator": "UICanvas>Default>StorePanel>Panel>>panel_list_type1>view_port>content>>btn_buy>text"}

        class GiftPack:
            gift_pack_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1>panel_list_type1>view_port>content>"}
            icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1>panel_list_type1>view_port>content>>group>item_list>>icon"}

        class Resource:
            resource_tab_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_subtab>subtab>view_port>content>>bg"}
            item_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>>view_port>content>"}
            gear_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>>panel_list_type1>view_port>content>>group>>img"}
            gear_name_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list_type1>view_port>content>>group>title_bg>title"}
            fish_card_name_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list_type1>view_port>content>>group>title_bg>title"}
            fish_card_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>>panel_list_type1>view_port>content>>group>icon"}
            fish_card_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>>panel_list_type1>view_port>content>>group>quantity>value"}
            booster_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list_type2>view_port>content>>group>icon_list>>icon"}
            materials_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list_type1>view_port>content>>group>icon"}
            materials_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list_type1>view_port>content>>group>quantity>value"}

        class Box:
            btn_refresh_text = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>tips>btn_refresh>text"}
            btn_refresh_value = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>tips>btn_refresh>value"}
            times_refresh = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>tips>refresh>text"}
            quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>quantity>value"}
            btn_buy_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>btn_buy>text"}
            btn_disabled_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>btn_disabled>text"}
            off_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>value_bg>number"}
            box_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>group>icon_box"}
            item_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>"}

        class Cash:
            cash_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3>panel_list_type1>view_port>content>"}
            cash_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3>panel_list_type1>view_port>content>>group>icon"}
            cash_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3>panel_list_type1>view_port>content>>group>quantity>value"}

    class TaskFishingCareer:
        TaskFishingCareerPanel = {"locator": "UICanvas>Default>TaskFishingCareerPanel"}
        btn_close = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>btn_close>img"}
        task_btn_complete_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>btn_completed>btn_normal"}
        task_btn_undone_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>btn_undone>btn_normal"}
        chapter_title = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>progressbar>title"}
        chapter_btn_complete = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>btn_completed>btn_normal"}
        chapter_btn_undone = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>btn_undone>btn_normal"}
        chapter_item1_title = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>item>item1>item_model_new>title"}
        chapter_item2_title = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>item>item2>item_model_new>title"}
        chapter_item1_quantity = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>item>item1>item_model_new>quantity>value"}
        chapter_item2_quantity = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>item>item2>item_model_new>quantity>value"}
        chapter_porgressbar = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>rewards>item>progressbar>number"}
        task_text_list= {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>text"}
        # title不一定有
        task_item1_icon_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>item1>item_model_new>icon"}
        task_item2_icon_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>item2>item_model_new>icon"}
        task_item1_quantity_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>item1>item_model_new>quantity>value"}
        task_item2_quantity_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>item2>item_model_new>quantity>value"}
        task_porgressbar_list = {"locator": "UICanvas>Default>TaskFishingCareerPanel>Panel>list>view_port>content>>porgressbar>text"}

    class Task:
        TaskPanel = {"locator": "UICanvas>Default>TaskPanel"}
        btn_close = {"locator": "UICanvas>Default>TaskPanel>panel>btn_close>img"}
        tab_daily = {"locator": "UICanvas>Default>TaskPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_daily>bg"}
        tab_weekly = {"locator": "UICanvas>Default>TaskPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_weekly>bg"}
        tab_month = {"locator": "UICanvas>Default>TaskPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_month>bg"}
        tab_list = {"locator": "UICanvas>Default>TaskPanel>panel>panel_tab>content>TabList>Viewport>Content>>bg"}
        # 根据颜色看选中框
        tab_icon_list = {"locator": "UICanvas>Default>TaskPanel>panel>panel_tab>content>TabList>Viewport>Content>>icon"}
        kind_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress_text>Text(TMP)"}
        # 对照数量
        task_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>"}
        btn_completed_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>btn_completed"}
        btn_undone_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>btn_undone"}
        btn_finish_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>finish"}
        view_port = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port"}
        item_quantity_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>>item_model_new>quantity"}
        item_icon_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>>item_model_new>icon"}
        progress_value = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg"}
        box_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>"}
        text_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>Image>text"}
        award_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>award"}
        ing_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>ing"}
        done_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>done"}
        award_detail = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>detialObj>detail"}
        award_quantity_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>detialObj>detail>>quantity>value"}
        award_icon_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>detialObj>detail>>icon"}

    class Tournaments:
        TournamentsPanel = {"locator": "UICanvas>Default>TournamentsPanel"}
        btn_close = {"locator": "UICanvas>Default>TournamentsPanel>panel>btn_close>img"}
        entrance_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>btn_enter>btn_normal"}
        time_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>tournaments_info>time>text"}


        class gears_switch:
            location_name = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>location_info>bg>location>value"}
            location_icon = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>location_info>bg>kind>icon"}
            location_rank = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>location_info>bg>kind>value"}
            btn_quick_switch = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>btns>btn_quick_switch>btn_normal"}
            btn_apply = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>btns>btn_apply>btn_normal"}
            btn_cancel = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>btns>btn_cancel>btn_normal"}
            class rod:
                Viewport = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_rod>List>Viewport"}
                rating_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_rod>List>Viewport>Content>>gear_model_new(Clone)>rating>value"}
                location_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_rod>List>Viewport>Content>>gear_model_new(Clone)>kinds>icon"}
                location_rank_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_rod>List>Viewport>Content>>gear_model_new(Clone)>kinds>value"}

            class bait:
                Viewport = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_bait>List>Viewport"}
                rating_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_bait>List>Viewport>Content>>gear_model_new(Clone)>rating>value"}
                location_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_bait>List>Viewport>Content>>gear_model_new(Clone)>kinds>icon"}
                location_rank_list = {
                    "locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>panel_bait>List>Viewport>Content>>gear_model_new(Clone)>kinds>value"}

            class buff:
                item_buff_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>item_buff_model(Clone)>btn_normal"}
        class pve_prepare:
            npc_tips = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>npc_tips>img"}
            btn_gohome = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_gohome>btn_gohome>btn_normal"}
            btn_add_100500 = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>top_res>ResourceBar>100500>btn_add>btn_normal"}
            text_100500 = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>top_res>ResourceBar>100500>value"}
            btn_panel_tournaments = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>btn_panel_tournaments"}

    class TreasureChestGearsShards:
        TreasureChestGearsShardsPanel = {"locator": "UICanvas>Default>TreasureChestGearsShardsPanel"}
        btn_close = {"locator": "UICanvas>Default>TreasureChestGearsShardsPanel>btn_close>text"}

    # 宝箱
    class TreasureChest:
        TreasureChestPanel = {"locator": "UICanvas>Default>TreasureChestPanel"}
        btn_close = {"locator": "UICanvas>Default>TreasureChestPanel>panel>btn_close>img"}
        box_list = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>select>>box"}
        quantity_list = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>select>>quantity>value"}
        box = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>box_particle>>box>0"}
        btn_open = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>btn_open>text"}
        box_points = {"locator": "UICanvas>Default>TreasureChestPanel>panel>panel_left>content>progressbar>progressbar_bg>progressbarbar_text_bg>text"}
        progressbar_box = {"locator": "UICanvas>Default>TreasureChestPanel>panel>panel_left>content>progressbar>progressbar_bg>box"}
        btn_buy = {"locator": "UICanvas>Default>TreasureChestPanel>panel>panel_left>content>merchant>btn_buy>btn_normal"}
        btn_magnifier = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>items_bg>btn_magnifier>icon"}
        tips = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>tips"}
        preview_icon_list = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>items_bg>items>>icon"}



    class TreasureChestRewards:
        TreasureChestRewardsPanel = {"locator": "UICanvas>Default>TreasureChestRewardsPanel"}
        btn_close = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>btn>btn_receive>btn_normal"}
        item_icon_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>item_model_new(Clone)>icon"}
        item_quantity_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>item_model_new(Clone)>quantity>value"}
        gear_icon_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>gear_model_new(Clone)>icon"}
        gear_location_icon_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>gear_model_new(Clone)>kinds>icon"}
        gear_rarity_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>gear_model_new(Clone)>bg"}
        btn_open_x = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>btn>btn_open>text"}
        btn_disabled = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>btn>btn_open>btn_disabled"}





























