
class ElementsData:
    Panels = {"locator": "UICanvas>>"}
    Panels_Default = {"locator": "UICanvas>Default>"}
    Panels_Important = {"locator": "UICanvas>Important>"}

    class AchievementGroupPanel:
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
        title = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>title_group>content>title"}
        complete = {"locator": "UICanvas>Default>AchievementGroupPanel>panel>item_value>exp_value>value"}

    class AchievementPanel:
        AchievementPanel = {"locator": "UICanvas>Default>AchievementPanel"}
        achievement_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>"}
        achievement_bg_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>>groupbg"}
        btn_close = {"locator": "UICanvas>Default>AchievementPanel>panel>btn_close>img"}
        btn_i = {"locator": "UICanvas>Default>AchievementPanel>panel>title_group>content>btn_i>img"}
        tips = {"locator": "UICanvas>Default>AchievementPanel>panel>title_group>tips"}
        tips_unlock = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>tips_unlock"}
        task_mini_icon = {"locator": "UICanvas>Default>AchievementPanel>panel>task_mini>icon"}
        viewport = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport", "focus": (0, 0)}
        achievement_icon_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>group_com>icon_gray"}
        achievement_group_name_list = {"locator": "UICanvas>Default>AchievementPanel>panel>List>Viewport>Content>>group_com>groupbg>groupname"}
        tab_list = {"locator": "UICanvas>Default>AchievementPanel>panel>panel_tab>tab>>icon"}

    class AchievementCategoryPanel:
        AchievementCategoryPanel = {"locator": "UICanvas>Default>AchievementCategoryPanel"}
        btn_close = {"locator": "UICanvas>Default>AchievementCategoryPanel>panel>btn_close>img"}
        item_list =  {"locator": "UICanvas>Default>AchievementCategoryPanel>panel>panel_info>List>Viewport>Content>>bg"}
        reward_icon_list = {"locator": "UICanvas>Default>AchievementCategoryPanel>panel>btn_rewards>item_list>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>AchievementCategoryPanel>panel>btn_rewards>item_list>>quantity>value"}
        btn_rewards = {"locator": "UICanvas>Default>AchievementCategoryPanel>panel>btn_rewards>bg"}
        category_viewport = {"locator": "UICanvas>Default>AchievementCategoryPanel>panel>panel_info>List>Viewport"}

    class AchievementPopupPanel:
        AchievementPopupPanel = {"locator": "UICanvas>Important>AchievementPopupPanel"}
        btn_orange = {"locator": "UICanvas>Important>AchievementPopupPanel>panel>btn_achv_fast>btn_orange"}


    class AchievementWantedPanel:
        AchievementWantedPanel = {"locator": "UICanvas>Default>AchievementWantedPanel"}
        btn_close = {"locator": "UICanvas>Default>AchievementWantedPanel>panel>btn_close>img"}
        item_list = {"locator": "UICanvas>Default>AchievementWantedPanel>panel>panel_info>group>"}
        reward_icon_list = {"locator": "UICanvas>Default>AchievementWantedPanel>panel>btn_rewards>item_list>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>AchievementWantedPanel>panel>btn_rewards>item_list>>quantity>value"}
        btn_rewards = {"locator": "UICanvas>Default>AchievementWantedPanel>panel>btn_rewards>bg"}

    class ActivityCenterPanel:
        ActivityCenterPanel = {"locator": "UICanvas>Important>ActivityCenterPanel"}
        btn_close = {"locator": "UICanvas>Important>ActivityCenterPanel>panel>btn_close>img"}

    class AlbumFishDetailPanel:
        AlbumFishDetailPanel = {"locator": "UICanvas>Default>AlbumFishDetailPanel"}
        btn_close = {"locator": "UICanvas>Default>AlbumFishDetailPanel>btn_close>img"}
        btn_share = {"locator": "UICanvas>Default>AlbumFishDetailPanel>btn_share>icon"}
        btn_share_chat = {"locator": "UICanvas>Default>AlbumFishDetailPanel>btn_share_chat>icon"}
        btn_close_share_chat = {"locator": "UICanvas>Default>AlbumFishDetailPanel>Panel_Popups_Tournaments>Panel>btn_close>img"}
        btn_confirm_list = {"locator": "UICanvas>Default>AlbumFishDetailPanel>Panel_Popups_Tournaments>Panel>panel_list>list>Viewport>Content>>btn_confirm", "focus": (1, 0.5)}

    class AquariumPanel:
        AquariumPanel = {"locator": "UICanvas>Default>AquariumPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumPanel>panel>btn_close>img"}
        ResourceBar = {"locator": "UICanvas>Default>AquariumPanel>panel>top_res>ResourceBar>"}
        btn_add_100100 = {"locator": "UICanvas>Default>AquariumPanel>panel>top_res>ResourceBar>100100>btn_add"}
        Rewards = {"locator": "UICanvas>Default>AquariumPanel>panel>navbar>lv_bar>Rewards>ing>item"}
        btn_fish = {"locator": "UICanvas>Default>AquariumPanel>panel>navbar>btns>btn_fish>img"}
        btn_build = {"locator": "UICanvas>Default>AquariumPanel>panel>navbar>btns>btn_build>bg"}
        fish_num = {"locator": "UICanvas>Default>AquariumPanel>panel>navbar>panel_down>panel_info>fish_num>text"}


    class AquariumBuildPanel:
        AquariumBuildPanel = {"locator": "UICanvas>Default>AquariumBuildPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>btn_close>img"}
        ResourceBar = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>top_res>ResourceBar"}
        btn_add_100100 = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>top_res>ResourceBar>100100>btn_add"}
        btn_next = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_left>arrow>btn_next>img"}
        btn_previous = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_left>arrow>btn_previous>img"}
        tab_list = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>tab>"}
        cost_numerator = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>cost>res_1>value_cost"}
        cost_denominator = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>cost>res_1>value"}
        icon_cost = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>cost>res_1>icon"}
        btn_level_up = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>btn", "focus":(0.5, 1)}
        lv_now = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>content>level_change>text_now"}
        lv_next = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>content>level_change>text_net"}
        icon_list = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>content>normal>list>>icon"}
        value_now_list = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>content>normal>list>>value"}
        value_next_list = {"locator": "UICanvas>Default>AquariumBuildPanel>panel>panel_tab>content>panel_upgrade>content>normal>list>>value_next"}



    class AquariumBuildMainPanel:
        AquariumBuildMainPanel = {"locator": "UICanvas>Default>AquariumBuildMainPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumBuildMainPanel>btn_close>img"}
        buliding_list = {"locator": "UICanvas>Default>AquariumBuildMainPanel>buliding_models>"}
        build_lv_list = {"locator": "UICanvas>Default>AquariumBuildMainPanel>buliding_models>>build_lv"}
        tip_levelup_bubble_list = {"locator": "UICanvas>Default>AquariumBuildMainPanel>buliding_models>>tip_levelup_bubble"}


    class AquariumCommonFishChangePanel:
        AquariumCommonFishChangePanel = {"locator": "UICanvas>Default>AquariumCommonFishChangePanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumCommonFishChangePanel>panel>btn_close>tip"}

    class AquariumFishPanel:
        AquariumFishPanel = {"locator":"UICanvas>Default>AquariumFishPanel"}
        btn_close = {"locator":"UICanvas>Default>AquariumFishPanel>panel>panel_fish>btn_close", "focus": (1, 0)}
        btn_add_100100 = {"locator": "UICanvas>Default>AquariumFishPanel>panel>top_res>ResourceBar>100100>btn_add"}
        ResourceBar = {"locator": "UICanvas>Default>AquariumFishPanel>panel>top_res>ResourceBar"}
        btn_i = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>fish_num>btn_i>img"}
        tips_discribe = {"locator": "UICanvas>Default>AquariumFishPanel>panel>tips_discribe"}
        btn_retrieve = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>btn_retrieve>img"}
        fish_num = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>fish_num>text>value"}
        fish_num_max = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>fish_num>text>text"}
        tab_list = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>tab>"}
        Viewport = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>List>Viewport"}
        fish_model_list = {"locator": "UICanvas>Default>AquariumFishPanel>panel>panel_fish>List>Viewport>Content>"}

    class AquariumNewActivityInnerPopupPanel:
        AquariumNewActivityInnerPopupPanel = {"locator": "UICanvas>Default>AquariumNewActivityInnerPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumNewActivityInnerPopupPanel>panel>btn_close>img"}

    class AquariumNewActivityPopupPanel:
        AquariumNewActivityPopupPanel = {"locator": "UICanvas>Default>AquariumNewActivityPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumNewActivityPopupPanel>panel>btn_close>img"}

    class AquariumFishNewPanel:
        AquariumFishNewPanel = {"locator": "UICanvas>Default>AquariumFishNewPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>btn_close"}
        btn_accelerate_reddot_list = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>List>Viewport>Content>fish_model>aquarium_fish_new_model>btns>btn_accelerate>reddot"}
        btn_sell_reddot_list = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>List>Viewport>Content>fish_model>aquarium_fish_new_model>btns>btn_sell>reddot"}
        tab_list = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>tab>view_port>content>>bg"}
        btn_change = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>fish_num>panel_info>btn_change>icon"}
        btn_fast = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>btn_fast>text"}
        top_res_btns = {"locator": "UICanvas>Default>AquariumFishNewPanel>top_res>ResourceBar>>btn_add"}
        btns = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>List>Viewport>Content>fish_model>aquarium_fish_new_model>btns>"}
        btns_operate = {"locator": "UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>List_operate>btn>>text"}
        aquarium_fish_list = {"locator":"UICanvas>Default>AquariumFishNewPanel>panel>panel_fish>List_operate>Viewport>Content>list_fish>>aquarium_fish_new_model"}

    class AquariumMainPanel:
        AquariumMainPanel = {"locator":"UICanvas>Default>AquariumMainPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumMainPanel>panel>btn_close>img"}
        btn_fish = {"locator": "UICanvas>Default>AquariumMainPanel>panel>navbar>btns>btn_fish>bg"}
        top_res_btns = {"locator": "UICanvas>Default>AquariumMainPanel>panel>top_res>ResourceBar>>btn_add"}
        btn_i = {"locator": "UICanvas>Default>AquariumMainPanel>panel>title_group>content>btn_i>img"}
        btns = {"locator": "UICanvas>Default>AquariumMainPanel>panel>navbar>btns>", "focus": (0.5, 1)}
        btn_change = {"locator": "UICanvas>Default>AquariumMainPanel>panel>navbar>panel_down>panel_info>btn_change", "focus": (1, 1)}
        btn_collect = {"locator": "UICanvas>Default>AquariumMainPanel>Panel_Popups_lvup>Panel>btn>btn_collect", "focus": (0.5, 1)}
        btn_close_level_up = {"locator": "UICanvas>Default>AquariumMainPanel>Panel_Popups_lvup>Panel>btn_close>img"}

    class AquariumNewSkinPanel:
        AquariumNewSkinPanel = {"locator": "UICanvas>Default>AquariumNewSkinPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumNewSkinPanel>panel>panel_fish>btn_close", "focus": (1, 0)}
        viewport = {"locator": "UICanvas>Default>AquariumNewSkinPanel>panel>panel_fish>List>Viewport"}
        btns = {"locator": "UICanvas>Default>AquariumNewSkinPanel>panel>panel_fish>List>Viewport>Content>>aquarium_skin_model>btns>>text"}

    class AquariumShopPanel:
        AquariumShopPanel = {"locator": "UICanvas>Default>AquariumShopPanel"}
        btn_close = {"locator": "UICanvas>Default>AquariumShopPanel>Panel>btn_close>img"}
        btn_magnifier = {"locator": "UICanvas>Default>AquariumShopPanel>Panel>panel_avatar>panel_name>btn_magnifier"}
        viewport = {"locator": "UICanvas>Default>AquariumShopPanel>Panel>panel_list>Viewport"}
        btn_buy_list = {"locator": "UICanvas>Default>AquariumShopPanel>Panel>panel_list>Viewport>content>>btn_buy"}
        item_icon_list = {"locator": "UICanvas>Default>AquariumShopPanel>Panel>panel_list>Viewport>content>>item_list>item_model_mini(Clone)>icon"}
        item_icon_purchase = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>item_info>item>item_model_mini>icon"}
        btn_close_purchase = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>btn_close>img"}
        btn_sub = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>cost>btn_sub"}
        btn_add = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>cost>btn_add"}
        btn_max = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>cost>btn_max"}
        btn_min = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>cost>btn_min"}
        btn_exchange = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>btn>btn_exchange", "focus": (0.5, 1)}
        slider = {"locator": "UICanvas>Default>AquariumShopPanel>Panel_Popups_Purchase>Panel>cost>slider"}




    class AvatarSelectPanel:
        AvatarSelectPanel = {"locator": "UICanvas>Default>AvatarSelectPanel"}
        gender_icon_list = {"locator": "UICanvas>Default>AvatarSelectPanel>panel_edit>panel_tab>content>TabList>Viewport>Content>" }
        btn_start = {"locator": "UICanvas>Default>AvatarSelectPanel>panel_edit>btn_start", "focus": (1, 1)}

    class AvatarSkinPopPanel:
        AvatarSkinPopPanel = {"locator": "UICanvas>Default>AvatarSkinPopPanel"}
        btn_close = {"locator": "UICanvas>Default>AvatarSkinPopPanel>panel>btn_close>img"}
        btn_enter = {"locator": "UICanvas>Default>AvatarSkinPopPanel>panel>btn_enter"}

    class AvatarSkinPopPanel_subType_2:
        AvatarSkinPopPanel = {"locator": "UICanvas>Default>AvatarSkinPopPanel_subType_2"}
        btn_close = {"locator": "UICanvas>Default>AvatarSkinPopPanel_subType_2>panel>btn_close>img"}
        btn_enter = {"locator": "UICanvas>Default>AvatarSkinPopPanel_subType_2>panel>btn_enter"}

    class AvatarTipsView:
        AvatarTipsView = {"locator": "UICanvas>Default>AvatarTipsView"}
        tap_to_continue = {"locator": "UICanvas>Default>AvatarTipsView>panel>panel_rod_info>tap_to_continue", "focus": (1, 0.5)}
        btn_changesex = {"locator": "UICanvas>Default>AvatarTipsView>panel>panel_rod_info>panel_left>btns>btn_changesex"}
        btn_changecamera = {"locator": "UICanvas>Default>AvatarTipsView>panel>panel_rod_info>panel_left>btns>btn_changecamera"}

    class AvatarMainPanel:
        AvatarMainPanel = {"locator": "UICanvas>Default>AvatarMainPanel"}
        btn_close = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>btn_close>img"}
        tab_avatar = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_tab>tab>1>bg"}
        tab_rod = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_tab>tab>2>bg"}
        tab_bag = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_tab>tab>3>bg"}
        tab_list = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_tab>tab>"}

        class panel_Avatar:
            panel_Avatar = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar"}
            tab_list = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_tab>TabList>Viewport>Content>>bg"}
            viewport_tab = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_tab>TabList>Viewport", "focus": (0, 0)}
            tags = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>left>avatar_info>info>tags"}
            btn_changesex = { "locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>left>panel_btns_change>btn_changesex"}
            btn_changecamera = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>left>panel_btns_change>btn_changecamera"}
            btn_hide = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>left>panel_btns_change>btn_hide"}
            btns_change = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>left>panel_btns_change>"}
            btn_confirm = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_list>btn_confirm"}
            tip = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_list>tip"}
            toggle_own = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_list>panel_top>title_avatar>online>option>Toggle"}
            item_list = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_list>list>Viewport>Content>>item_model_square"}
            viewport = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Avatar>right>panel_list>list>Viewport", "focus": (0, 0)}

        class panel_Rod:
            panel_Rod = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod"}
            btn_hide = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>left>panel_btns_change>btn_hide"}
            btn_changecamera = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_btns_change>btn_changecamera"}
            tab_rod_list = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_tab>TabList>Viewport>Content>>bg"}
            viewport_tab_rod = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_tab>TabList>Viewport", "focus": (0, 0)}
            btn_bobox = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_tab>tab_bobox>btn_bobox>text"}
            item_list = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_list>list>Viewport>Content>>item_model_square>bg"}
            viewport = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_list>list>Viewport", "focus": (0, 0)}
            tabs_top = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_list>panel_top>rod_tab>tabs>"}
            bobox_on_list = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_tab>tab_bobox>bobox_on_list>>text"}
            btn_confirm = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_list>btn_confirm", "focus": (0.5, 1)}
            tip = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_list>tip"}
            btn_form = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>avatar_info>btn_form"}
            tags = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>avatar_info>info>tags"}
            btn_fast = {"locator": "UICanvas>Default>AvatarMainPanel>panel_avatar>panel_Rod>panel_list>btns>btn_fast"}

    class BaitAndRodAlbumPanel:
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

    class BaitAndRodShowPanel:
        BaitAndRodShowPanel = {"locator": "UICanvas>Default>BaitAndRodShowPanel"}
        tap_to_continue = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>panel_rod_info>panel_right>content>tap_to_continue"}
        talent = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>panel_rod_info>panel_right>content>bg>sign"}
        tips_talent = {"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>tips_talent"}
        five_dimension ={"locator": "UICanvas>Default>BaitAndRodShowPanel>panel>panel_rod_info>5d>bg"}
        tips_five_dimension = {"locator": "GGGanvas>Default>BaitAndRodShowPanel>panel>tips_5d"}
        name = {"locator":"UICanvas>Default>BaitAndRodShowPanel>panel>>panel_right>content>bg>nameBG>name"}
        skill_list = {"locator":"UICanvas>Default>BaitAndRodShowPanel>panel>panel_rod_info>panel_right>content>bg>skill_list>>rod_skill"}

    class BattleExplainPanel:
        BattleExplainPanel = {"locator": "UICanvas>Default>BattleExplainPanel"}
        close = {"locator": "UICanvas>Default>BattleExplainPanel>close"}

    class BattleFailedPanel:
        BattleFailedPanel = {"locator": "UICanvas>Default>BattleFailedPanel"}
        btn_upgrade = {"locator": "UICanvas>Default>BattleFailedPanel>panel_fail>btns>btn_upgrade>btn_normal"}
        btn_again = {"locator": "UICanvas>Default>BattleFailedPanel>panel_fail>btns>btn_again>btn_normal"}
        btns = {"locator": "UICanvas>Default>BattleFailedPanel>panel_fail>btns>"}

    class BattlePanel:
        BattlePanel = {"locator": "UICanvas>Default>BattlePanel"}
        joystick = {"locator": "UICanvas>Default>BattlePanel>joystick"}
        btn_reel = {"locator": "UICanvas>Default>BattlePanel>btn_cast", "focus": (1, 1)}
        tip_slide = {"locator": "UICanvas>Default>BattlePanel>btn_cast>tip_slide"}
        progress = {"locator": "UICanvas>Default>BattlePanel>hook>progress>bg"}
        arrow = {"locator": "UICanvas>Default>BattlePanel>hook>progress>arrow"}
        qte_list = {"locator": "UICanvas>Default>BattlePanel>FishHUD>>qte"}
        qte_left = {"locator": "UICanvas>Default>BattlePanel>FishHUD>qte_left>qte"}
        qte_right = {"locator": "UICanvas>Default>BattlePanel>FishHUD>qte_right>qte"}
        qte_jump_left = {"locator": "UICanvas>Default>BattlePanel>FishHUD>qte_left_fishJump>qte"}
        qte_jump_right = {"locator": "UICanvas>Default>BattlePanel>FishHUD>qte_right_fishJump>qte"}
        qte_up = {"locator": "UICanvas>Default>BattlePanel>FishHUD>qte_up>qte"}
        m_value = {"locator": "UICanvas>Default>BattlePanel>FishHUD>m_value"}
        warning = {"locator": "UICanvas>Default>BattlePanel>Warning"}
        hud_power_list = {"locator":"UICanvas>Default>BattlePanel>hud_power>barPanel>list>>baseParticle"}
        hud_power_list_old = {"locator":"UICanvas>Default>BattlePanel>hud_power>bar_normal>"}
        hud_escaping = {"locator":"UICanvas>Default>BattlePanel>FishHUD>fish_HP>m_value>hud_escaping>text"}

    class BattlePassBuyLevelPanel:
        BattlePassBuyLevelPanel = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>btns>btn_confirm>text"}
        btn_buy_disabled = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>btns>btn_confirm>btn_disabled"}
        btn_add = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>btn_add>img"}
        btn_sub = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>btn_sub>img"}
        level_cal = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>title>title"}
        top_res_btns = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>top_res>ResourceBar>>btn_add"}
        btn_add_100100 = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>top_res>ResourceBar>100100>btn_add>btn_normal"}
        text_100100 = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>top_res>ResourceBar>100100>value"}
        Viewport = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport", "focus": (0, 0)}
        reward_icon_free_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>free>item>item_model_new(Clone)>icon"}
        reward_icon_premium_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>>item>item_model_new(Clone)>quantity>value"}
        reward_gear_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>>item>gear_model_new(Clone)>icon"}
        licenseLock_list = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>List>Viewport>Content>>model>licenseLock"}
        slider = {"locator": "UICanvas>Default>BattlePassBuyLevelPanel>panel_BP_Lv_buy>panel_popup>continuous_upgrade>slider"}

    class BattlePassBuyLicensePanel:
        BattlePassBuyLicensePanel =  {"locator": "UICanvas>Default>BattlePassBuyLicensePanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>btn_close>img"}
        btn_buy_list = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>>btn"}
        cost_icon_list = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>>btn>icon"}
        cost_quantity_list = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>>btn>text"}
        btn_buy_pro = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>panel_right>btn>text"}
        btn_buy_standard = {"locator": "UICanvas>Default>BattlePassBuyLicensePanel>panel_BP_buy>panel_left>btn>text"}

    class BattlePassIntroPanel:
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

    class BattlePassPanel:
        BattlePassPanel = {"locator": "UICanvas>Default>BattlePassPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>btn_close>img"}
        btn_detail = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_left>rewards_preview>btn_detall"}
        time = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_left>rewards_preview>info>time>text"}
        btn_i = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>title_group>content>btn_i>img"}
        exp = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>exp"}
        btn_task = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>btns>btn_task>btn_normal"}
        btn_task_text ={"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>btns>btn_task>text"}
        btn_buy = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>btns>btn_buy>btn_normal"}
        btn_buy_text = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>exp>btns>btn_buy>text"}
        btn_premium = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>title_group>lock>btn", "focus": (0, 0.5)}
        bg_img = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>title_group>bg_img"}
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
        item_icon_list =  {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>>item>item_model_new(Clone)>icon"}
        free_icon_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>free>item>item_model_new(Clone)>icon"}
        premium_icon_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}
        free_quantity_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>free>item>item_model_new(Clone)>quantity>value"}
        premium_quantity_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>quantity>value"}
        free_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>free"}
        premium_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>>model>premium"}
        preview_item_icon_list ={"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>list_preview>reward_model>model>>item>item_model_new(Clone)>icon"}
        preview_gear_icon_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>list_preview>reward_model>model>>item>gear_model_new(Clone)>icon"}
        preview_item_list = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>list_preview>reward_model>model>>item>"}
        btn_i_goldbank = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>List>Viewport>Content>goldbank>btn_i>img"}
        Tip_goldbank = {"locator": "UICanvas>Default>BattlePassPanel>panel_BP>panel_right>Tip_goldbank"}

    class BattlePassPopPanel:
        BattlePassPopPanel = {"locator": "UICanvas>Default>BattlePassPopPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>btn_close>img"}
        btn_confirm = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>btns>btn_confirm>btn_normal"}
        Viewport = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>panel_advertisement>panel_premium>List>Viewport", "focus": (0, 0)}
        icon_list = {"locator": "UICanvas>Default>BattlePassPopPanel>panel_BP_advertisement>panel_advertisement>panel_premium>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}

    class BattlePassRewardPanel:
        BattlePassRewardPanel = {"locator": "UICanvas>Default>BattlePassRewardPanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>btn_close>tip"}
        btn_unLock = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>unLockBtn>btn_normal"}
        reward_icon_free_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>item_model_new(Clone)>icon"}
        reward_quantity_free_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>item_model_new(Clone)>quantity>value"}
        reward_gear_free_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>gear_model_new(Clone)>icon"}
        reward_icon_premium_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>icon"}
        reward_quantity_premium_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>item_model_new(Clone)>quantity>value"}
        reward_gear_premium_list = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>gear_model_new(Clone)>icon"}
        item_list_free = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport>Content>>model>free>item>"}
        item_list_premium = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport>Content>>model>premium>item>"}
        Viewport_free = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_free>List>Viewport", "focus": (0, 0)}
        Viewport_premium = {"locator": "UICanvas>Default>BattlePassRewardPanel>panel_BP_Lv_up>panel_right>panel_premium>List>Viewport", "focus": (0, 0)}

    class BattlePreparePanel:
        BattlePreparePanel = {"locator": "UICanvas>Default>BattlePreparePanel"}
        btn_close = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_gohome>btn_gohome>img"}
        quick_switch = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>quick_switch>btn_quick_switch>btn_normal"}
        btn_i = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>quick_switch>btn_i>img"}
        rod_model_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears_new>panel_gears_switch>panel_rod>List>Viewport>Content>>gear_model_new(Clone)>bg"}
        bait_model = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>bait>rod_model>gear_model_new(Clone)>icon"}
        btn_switch_gear_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>gears>>btn_switch>btn_normal"}
        btn_switch_item_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>btn_switch>bg"}
        item_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>icon"}
        item_quantity_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>quantity>value"}
        switch_tip_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>switch_tip>items>>icon"}
        switch_tip_quantity_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>switch_tip>items>>quantity>value"}
        tag_equipped = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_preview>item_sys>buff>>switch_tip>items>>tag_equipped"}
        panel_gears_switch = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch"}
        btn_cast = {"locator": "UICanvas>Default>BattlePreparePanel>>>btn_cast>btn_normal"}
        location = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears>panel_gears_switch>location_info>bg>location>value"}

        btn_tournaments = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_activity>btn_activity>btn_tournaments>img"}
        btn_location = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>btn_location>btn_normal"}
        panel_tip_location = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>panel_tip_location"}
        location_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>panel_tip_location>panel>list_location>", "focus": (0, 0)}
        treasure_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>panel_tip_location>panel>list_treasure>", "focus": (0, 0)}
        location_energy_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>panel_tip_location>panel>list_location>>energy>value"}
        treasure_energy_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>panel_tip_location>panel>list_treasure>>energy>value"}
        btn_add_100500 = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>top_res>ResourceBar>100500>btn_add"}
        btn_collection = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_gohome>btn_collection>icon"}
        panel_tip_location_newtreasure = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>panel_tip_location_newtreasure", "focus": (1, 0.8)}

        btn_icon = {"locator":"UICanvas>Default>BattlePreparePanel>Panel_Prepare_Warning>panel>panel_icon>btn_icon_b>btn_icon>bg_icon"}
        value_cost = {"locator":"UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_pve>btn_cast>value_cost"}

        wait_for_join = {"locator":"UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_activity>btn_activity>btn_tournaments>rank>value_3"}

        gears = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears_new>panel_gears_preview>gears>bg"}
        btn_apply = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears_new>panel_gears_switch>btns>btn_apply>btn_normal"}
        btn_cancel = {"locator":"UICanvas>Default>BattlePreparePanel>panel_gears_new>panel_gears_switch>btns>btn_cancel>text"}
        btn_go = {"locator": "UICanvas>Default>BattlePreparePanel>panel_gears_new>panel_gears_switch>panel_gears_preview>btns>btn_go"}

        class GlobalProgress:
            progress_info = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>progress_info", "focus": (0.5, 0.5)}
            progress_cur = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>progress_info>progressValueLayout>cur"}
            progress_max = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>progress_info>progressValueLayout>max"}
            next_reward_icon = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>progress_info>reward>item_model_mini>icon"}
            next_reward_quantity = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>progress_info>reward>item_model_mini>quantity>value"}
            current_rewards_icon_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>rewards_list>Viewport>Content>>icon"}
            current_rewards_quantity_list = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>rewards_list>Viewport>Content>>quantity>value"}
            progress_finish = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_tournaments_mini>panel_global_progress>panel_rewards>rewards>progress_finish"}

        class Panel_MiniTask:
            # minitask
            Panel_MiniTask = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask"}
            btn_recommend = {
                "locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask>Panel>btn_recommend"}
            btn_go = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask>Panel>btn_go"}
            btn_gift = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask>Panel>btn_gift"}
            btn_claim = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask>Panel>btn_claim"}
            text_task = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask>Panel>text"}
            progress = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>Panel_MiniTask>Panel>progress>value"}

        class PanelPrepareWarning:
            btn_icon = {"locator": "UICanvas>Default>BattlePreparePanel>Panel_Prepare_Warning>panel>panel_icon>>btn_icon>bg_icon"}

        class Sidebar:
            btn_menu = {"locator":"UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_gohome>btn_menu>icon"}
            panel_main_sidebar= {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar"}
            btn_close = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>btn_close"}
            panel_sidebar = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar"}
            panel_bg = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_bg"}
            head_img = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>head>head_mask>head_img"}
            head_frame = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>head>head_frame>panel>head_frame"}
            head_frame_com = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>head>head_frame>panel>head_frame_com"}
            division = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>player_top>division>icon"}
            player_name = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>player_top>player_name"}
            player_lv_lv= {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>player_down>player_lv>lv"}
            player_lv_value = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>player_down>player_lv>value"}
            player_rating_img = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>player_down>player_rating>rating>img"}
            player_rating_num = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_info>player_down>player_rating>rating>num"}
            player_id_text = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_id>text"}
            player_id_value = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_top>player_id>value"}
            btn_leaderboard = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_down>btns>btn_leaderboard>img"}
            btn_changeroom = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_down>btns>btn_changeroom>img"}
            btn_mail = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_down>btns>btn_mail>img"}
            btn_announcement = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_down>btns>btn_announcement>img"}
            btn_setting = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_down>btns>btn_setting>img"}
            gears = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>gears>rod"}
            btn_club = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_club>btn"}
            btn_friend = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_friend>btn"}
            btn_aquarium = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_aquarium>btn"}
            btn_career = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_career>btn"}
            btn_fishcard = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_fishcard>btn"}
            btn_store = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_store>btn"}
            btn_avatar = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_avatar>btn"}
            btn_flashcard = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_flashcard>btn"}
            btn_achievement = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_achievement>btn"}
            btn_fishalbum = {"locator": "UICanvas>Default>BattlePreparePanel>panel_pve_prepare>panel_main_sidebar>panel>panel_sidebar>panel_info>btn_fishalbum>btn"}


    class BattleTreasureMapPanel:
        BattleTreasureMapPanel = {"locator": "UICanvas>Default>BattleTreasureMapPanel"}
        btn_close = {"locator": "UICanvas>Default>BattleTreasureMapPanel>panel>Panel>btn_close>img"}
        btn_go = {"locator": "UICanvas>Default>BattleTreasureMapPanel>panel>Panel>btn_go"}

    class BattleTreasureMapDescriptionPanel:
        BattleTreasureMapDescriptionPanel = {"locator": "UICanvas>Default>BattleTreasureMapDescriptionPanel"}
        btn_close = {"locator": "UICanvas>Default>BattleTreasureMapDescriptionPanel>bg>btn_close>img"}

    class BugMultiplePanel:
        BugMultiplePanel = {"locator": "UICanvas>Default>BugMultiplePanel"}
        btn_cancel = {"locator": "UICanvas>Default>BugMultiplePanel>panel>btns>btn_cancel"}
        btn_confirm = {"locator": "UICanvas>Default>BugMultiplePanel>panel>btns>btn_confirm"}
        btn_min = {"locator": "UICanvas>Default>BugMultiplePanel>panel>btn_min"}
        btn_max = {"locator": "UICanvas>Default>BugMultiplePanel>panel>btn_max"}
        btn_sub = {"locator": "UICanvas>Default>BugMultiplePanel>panel>btn_sub"}
        btn_add = {"locator": "UICanvas>Default>BugMultiplePanel>panel>btn_add"}
        slider = {"locator": "UICanvas>Default>BugMultiplePanel>panel>slider"}
        value = {"locator": "UICanvas>Default>BugMultiplePanel>panel>value"}
        icon = {"locator":"UICanvas>Default>BugMultiplePanel>panel>item>item_model_mini>icon"}
        quantity= {"locator":"UICanvas>Default>BugMultiplePanel>panel>item>item_model_mini>quantity>value"}

    class BuyEnergyPanel:
        BuyEnergyPanel = {"locator": "UICanvas>Default>BuyEnergyPanel"}
        btn_close = {"locator": "UICanvas>Default>BuyEnergyPanel>btn_close>text"}
        btn_drink = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>drink>btn"}
        remaining_drink_value = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>drink>remaining>value"}
        btn_cash = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>cash>btn"}
        btn_cash_usd = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>cash_usd>btn"}
        drink_recovery_value = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>drink>amount>value"}
        cash_recovery_value = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>cash>amount>value"}
        cash_usd_recovery_value = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>cash_usd>amount>value"}
        text_100100 = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>100100>value"}
        text_100500 = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>100500>value"}
        btn_add_100100 = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>100100>btn_add>btn_normal"}
        btn_buy_list =  {"locator": "UICanvas>Default>BuyEnergyPanel>tab>>btn"}
        top_res_btns = {"locator": "UICanvas>Default>BuyEnergyPanel>top_res>ResourceBar>>btn_add"}
        item_list = {"locator": "UICanvas>Default>BuyEnergyPanel>tab>month_card>group_rewards>>item_icon>item_model_mini"}

    class CareerPanel:
        CareerPanel = {"locator": "UICanvas>Default>CareerPanel"}
        btn_close = {"locator": "UICanvas>Default>CareerPanel>panel_talent>btn_close>img"}
        btn_i = {"locator": "UICanvas>Default>CareerPanel>panel_talent>title_group>content>btn_i>img"}
        tips = {"locator": "UICanvas>Default>CareerPanel>panel_talent>title_group>content>btn_i>tips"}
        btn_enhance = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>btns>btn_enhance>text"}
        cost_icon_list = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>btns>cost>>icon"}
        cost_quantity_list = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>btns>cost>>value"}
        rating = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips>top>rating>num"}
        rating_total = {"locator": "UICanvas>Default>CareerPanel>panel_talent>rating>num"}
        item_icon = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips>item>item_model>icon_bg>icon"}
        rating_tips = {"locator": "UICanvas>Default>RatingTipsPanel>panel>Content>text_child"}
        rating_child = {"locator": "UICanvas>Default>RatingTipsPanel>panel>Content>rating_child>num"}
        item_lv = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips>item>item_model>text"}
        item_lock = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips>item>item_model>lock"}
        tips_lock = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips_lock"}
        tips_max = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips_max"}
        text_100000 = {"locator": "UICanvas>Default>CareerPanel>panel_talent>top_res>ResourceBar>100000>value"}
        text_100400 = {"locator": "UICanvas>Default>CareerPanel>panel_talent>top_res>ResourceBar>100400>value"}
        btn_add_100000 = {"locator": "UICanvas>Default>CareerPanel>panel_talent>top_res>ResourceBar>100000>btn_add>btn_normal"}
        top_res_btns = {"locator": "UICanvas>Default>CareerPanel>panel_talent>top_res>ResourceBar>>btn_add"}
        describe = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>tips>describe"}
        group_list = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list>panel_list_main>list>Viewport>Content>>"}
        career_viewport = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list>panel_list_main>list>Viewport", "focus": (0, 0)}
        page_item_middle_list = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list>panel_list_main>list>Viewport>Content>>>item_Middle>"}
        list_lockbg_mask = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list>list_lockbg_mask>img_back1"}
        btn_guide = {"locator": "UICanvas>Default>CareerPanel>panel_talent>btn_guide"}
        item_list = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list>panel_list_main>list>Viewport>Content>>>>>icon_bg"}




    class ChampointshipResultPopup:
        ChampointshipResultPopup = {"locator":"UICanvas>Default>ChampointshipResultPopup"}
        btn_close = {"locator":"UICanvas>Default>ChampointshipResultPopup>panel>btn_close"}
        btn_enhance = {"locator":"UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>btns>btn_enhance>text"}
        cost_icon_list = {"locator":"UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>btns>cost>>icon"}
        cost_quantity_list = {"locator": "UICanvas>Default>CareerPanel>panel_talent>panel_list_tips>btns>cost>>icon"}

    class ChatPanel:
        ChatPanel = {"locator":"UICanvas>Default>ChatPanel"}
        btn_close = {"locator": "UICanvas>Default>ChatPanel>panel>btn_close"}
        Input_enter = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>chat_enter>Input_enter"}
        btn_enter = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>chat_enter>btn_enter"}
        btn_share = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>chat_enter>btn_share"}
        btn_emoji = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>chat_enter>btn_emoji"}
        tab_list = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_tab>content>TabList>Viewport>Content>"}
        viewport_tab = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_tab>content>TabList>Viewport"}
        btns_nothing ={"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_nothing>btns>"}
        tab_list_emoji = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_emoji>tab_list>view_port>content>", "focus": (0, 0.5)}
        viewport_tab_list_emoji = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_emoji>tab_list>view_port"}
        emoji_list = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_emoji>emoji_list>Viewport>Content>>icon"}
        viewport_emoji = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_emoji>emoji_list>Viewport", "focus": (0, 0)}
        btn_fisheries = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_share>panel>btns>btn_fisheries"}
        toggle = {"locator": "UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_top>screen>option>Toggle"}
        btn_share_list = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_share>panel>list>Viewport>Content>fish_info_1>info>btn_share"}
        viewport_share = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_down>panel_share>panel>list>Viewport", "focus": (0, 0)}
        head_list = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_List>list>Viewport>Content>>playerInfo>head>head_mask>head_img"}
        btn_more_list = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_List>list>Viewport>Content>>fish_info>fast>btn_more"}
        btn_fast_list = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_List>list>Viewport>Content>>fish_info>fast>Viewport>Content>"}
        viewport_info = {"locator":"UICanvas>Default>ChatPanel>panel>panel_info>panel_info>panel_List>list>Viewport", "focus": (0, 0)}

    class ClubApplyPanel:
        ClubApplyPanel = {"locator":"UICanvas>Default>ClubApplyPanel"}
        btn_close = {"locator":"UICanvas>Default>ClubApplyPanel>panel>btn_close>img"}
        btn_apply = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_info>content>btns>btn_apply"}
        btn_report = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_info>content>top>btn_report>img"}
        btn_copy = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_info>content>info>clubid>btn_copy>img", "focus": (1, 0.5)}
        club_id = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_info>content>info>clubid>value"}
        club_list = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>panel_list>Viewport>Content>InfoItem"}
        viewport = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>panel_list>Viewport"}
        btn_create = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>btns>btn_create"}
        btn_fast = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>btns>btn_fast"}
        btn_refresh = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>refresh>btn_refresh"}
        toggle = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>applyed>option>Toggle"}
        Input_clubid = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>clubid_search>Input_clubid"}
        btn_search = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>clubid_search>btn_search"}
        btn_delete = {"locator":"UICanvas>Default>ClubApplyPanel>panel>panel_clubhome>panel_clublist>clubid_search>btn_close>img"}

    class ClubCreatePanel:
        ClubCreatePanel = {"locator": "UICanvas>Default>ClubCreatePanel"}
        btn_close = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>btn_close>img"}
        btn_cast = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>btns>btn_cast", "focus": (0.5, 1)}
        Input_clubintroduction = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_introduction>Input_clubintroduction", "focus": (0.5, 1)}
        Input_clubname = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_name>Input_clubname", "focus": (0.5, 1)}
        tag_list = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_tags>type>>Toggle"}
        btns_limit =  {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_limit>>>img"}
        tabs_flag = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_flag>flag_tab>tabs>"}
        block_list = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_flag>bg_block>type>>Toggle"}
        flag_list = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_flag>bg_flags>Viewport>type>>Toggle"}
        viewport_flag = {"locator": "UICanvas>Default>ClubCreatePanel>panel>panel_popup_clubedit>club_flag>bg_flags>Viewport", "focus": (0, 0)}

    class ClubModifyPanel:
        ClubModifyPanel = {"locator": "UICanvas>Default>ClubModifyPanel"}
        btn_close = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>btn_close>img"}
        btn_disband = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>btns>btn_disband"}
        btn_confirm = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>btns>btn_confirm", "focus": (0.5, 1)}
        Input_clubintroduction = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_introduction>Input_clubintroduction", "focus": (0.5, 1)}
        Input_clubname = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_name>Input_clubname", "focus": (0.5, 1)}
        tag_list = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_tags>type>>Toggle"}
        btns_limit =  {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_limit>>>img"}
        tabs_flag = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_flag>flag_tab>tabs>"}
        block_list = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_flag>bg_block>type>>Toggle"}
        flag_list = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_flag>bg_flags>Viewport>type>>Toggle"}
        viewport_flag = {"locator": "UICanvas>Default>ClubModifyPanel>panel>panel_popup_clubedit>club_flag>bg_flags>Viewport", "focus": (0, 0)}


    class ClubPanel:
        ClubPanel = {"locator": "UICanvas>Default>ClubPanel"}
        btn_close = {"locator": "UICanvas>Default>ClubPanel>panel>btn_close>img"}
        tab_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_tab>content>TabList>Viewport>Content>", "focus": (0, 0.5)}

        class panel_clubhome:
            btn_chat = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>btn_chat"}
            task_mini = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>task_mini"}
            toggle = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_chat>content>option>Toggle"}
            btn_goweek = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_week_mini>bar_rewards>Rewards>btn_goweek"}
            btn_copy = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_info>content>clubid>btn_copy"}
            red_envelope_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_chat>content>chatinfo>Viewport>Content>red_envelope", "focus": (0, 0)}
            viewport = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_chat>content>chatinfo>Viewport", "focus": (0, 0)}
            btn_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_chat>content>chatinfo>Viewport>Content>>btn"}
            btn_flashcard = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_events>btn_flashcard", "focus": (1, 0.5)}
            btn_dragonboat = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_events>btn_dragonboat", "focus": (1, 0.5)}
            btn_edit = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubhome>panel_info>content>btn_edit>icon"}

        class panel_clubmember:
            btn_leave = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubmember>btns>btns>btn_leave"}
            btn_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubmember>btns>btns>btn_list"}
            btn_playercard_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubmember>panel_list>Viewport>Content>>memberInfo>btn_playercard"}
            btn_edit_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubmember>panel_list>Viewport>Content>>btn_edit"}
            viewport = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubmember>panel_list>Viewport", "focus": (0, 0)}
            btns = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubmember>panel_list>tips_clubpoint>panel>btns>"}

        class panel_clubweek:
            reward_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubweek>rewards>content>>Rewards"}
            top_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubweek>rank>>btn"}
            btn_i = {"locator": "UICanvas>Default>ClubPanel>panel>panel_clubweek>rewards>singlenum>btn_i>img"}

        class Panel_Flashcard:
            btn_close = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>btn_close>img"}
            btn_save = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>panel_list>btns>btn_save", "focus": (0.5, 1)}
            btn_cancel = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>panel_list>btns>btn_cancel", "focus": (0.5, 1)}
            tab_list = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>panel_tab>TabList>Viewport>Content>", "focus": (0, 0.5)}
            viewport_tab = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>panel_tab>TabList>Viewport", "focus": (0, 0)}
            flashcard_list = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>panel_list>group>FlashcardList>Viewport>Content>"}
            viewport_flashcard = {"locator": "UICanvas>Default>ClubPanel>panel>Panel_Flashcard>Panel>panel_list>group>FlashcardList>Viewport", "focus": (0, 0)}


        class panel_popups_confirm:
            btn_close = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popups_confirm>Panel>btn_close>img"}
            btn_exchange = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popups_confirm>Panel>btn>btn_exchange", "focus": (0.5, 1)}

        class panel_popup_applylist:
            btn_close = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popup_applylist>btn_close>img"}
            btn_leave = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popup_applylist>btns>btn_leave"}
            btn_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popup_applylist>btns>btn_list"}
            btn_cancel_list =  {"locator": "UICanvas>Default>ClubPanel>panel>panel_popup_applylist>panel_applylist>Viewport>Content>>btns>btn_cancel", "focus": (0, 0.5)}
            btn_confirm_list = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popup_applylist>panel_applylist>Viewport>Content>>btns>btn_confirm"}
            viewport = {"locator": "UICanvas>Default>ClubPanel>panel>panel_popup_applylist>panel_applylist>Viewport", "focus": (0, 0)}


    class ClubRedEnvelopePanel:
        ClubRedEnvelopePanel = {"locator": "UICanvas>Default>ClubRedEnvelopePanel"}
        btn_close = {"locator": "UICanvas>Default>ClubRedEnvelopePanel>Panel_normal>bg", "focus": (-0.25, 0.5)}

    class CommonItemGetPanel:
        CommonItemGetPanel = {"locator":"UICanvas>Default>CommonItemGetPanel"}
        btn_close = {"locator":"UICanvas>Default>CommonItemGetPanel>panel>btn_close>img"}
        btn_list = {"locator":"UICanvas>Default>CommonItemGetPanel>panel>panel_sources>panel_list>sourcesList>Viewport>Content>>btn_purchase", "focus": (0.5, 1)}
        viewport = {"locator":"UICanvas>Default>CommonItemGetPanel>panel>panel_sources>panel_list>sourcesList>Viewport", "focus": (0, 0)}


    class CommonWebViewPanel:
        CommonWebViewPanel = {"locator":"UICanvas>Default>CommonWebViewPanel"}
        btn_close = {"locator": "UICanvas>Default>CommonWebViewPanel>Panel>btn_close>img"}




    class DailyTipsPanel:
        DailyTipsPanel = {"locator":"UICanvas>Default>DailyTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>DailyTipsPanel>panel>btn_close>img"}
        toggle = {"locator": "UICanvas>Default>DailyTipsPanel>panel>option_2>Toggle"}

    class DivisionChangePanel:
        DivisionChangePanel = {"locator":"UICanvas>Default>DivisionChangePanel"}
        tap_to_close = {"locator":"UICanvas>Default>DivisionChangePanel>Panel>btn_close>text"}

    class DivisionLeaderboardPanel:
        DivisionLeaderboardPanel = {"locator":"UICanvas>Default>DivisionLeaderboardPanel"}
        btn_close = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>btn_close>img"}
        tab_list = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_tab>content>TabList>Viewport>Content>", "focus": (0, 0.5)}
        class panel_myleague:
            btn_alldivisions = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>banner>btn_alldivisions"}
            crown = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>banner>crown", "focus": (0.5, 1)}
            btn_playercard_list = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>panel_ranking>Viewport>Content>>rank_info>info>playerInfo>btn_playercard"}
            btn_playercard_self = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>panel_ranking>list_myself>rank_info>info>playerInfo>btn_playercard"}
            item_list = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>panel_ranking>Viewport>Content>>rank_info>info>rewards>item>"}
            item_self = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>panel_ranking>list_myself>rank_info>info>rewards>item>"}
            viewport = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_myleague>panel_ranking>Viewport", "focus": (0, 0)}

        class panel_arena:
            tab_list = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_arena>tab>"}
            btn_playercard_list = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_arena>panel_ranking>Viewport>Content>>rank_info>info>playerInfo>btn_playercard"}
            btn_playercard_self = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_arena>panel_ranking>list_myself>rank_info>info>playerInfo>btn_playercard"}
            item_list = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_arena>panel_ranking>Viewport>Content>>rank_info>info>rewards>item>"}
            item_self = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_arena>panel_ranking>list_myself>rank_info>info>rewards>item>"}
            viewport = {"locator": "UICanvas>Default>DivisionLeaderboardPanel>Panel>panel_arena>panel_ranking>Viewport", "focus": (0, 0)}


    class DivisionListPanel:
        DivisionListPanel = {"locator":"UICanvas>Default>DivisionListPanel"}
        btn_close = {"locator": "UICanvas>Default>DivisionListPanel>Panel>btn_close>img"}
        item_list = {"locator": "UICanvas>Default>DivisionListPanel>Panel>divisions>List>Viewport>Content>>rewards>item>"}
        viewport = {"locator": "UICanvas>Default>DivisionListPanel>Panel>divisions>List>Viewport", "focus": (0, 0)}


    class DLCDownloadPanel:
        DLCDownloadPanel = {"locator": "UICanvas>Important>DLCDownloadPanel"}
        icon_list = {"locator": "UICanvas>Important>DLCDownloadPanel>Panel>bg>group_list>>item>>icon"}
        btn_close = {"locator": "UICanvas>Important>DLCDownloadPanel>Panel>btn_close>img"}
        group_list = {"locator": "UICanvas>Important>DLCDownloadPanel>Panel>bg>group_list>"}

    class DLCDownloadPanel_oversea:
        DLCDownloadPanel = {"locator": "UICanvas>Important>DLCDownloadPanel"}
        icon_list = {"locator": "UICanvas>Important>DLCDownloadPanel>Panel>bg>group_list>>item>>icon"}
        btn_close = {"locator": "UICanvas>Important>DLCDownloadPanel>Panel>btn_close>img"}
        group_list = {"locator": "UICanvas>Important>DLCDownloadPanel>Panel>bg>group_list>"}


    class EntryUpdateLoading:
        EntryUpdateLoading = {"locator": "GameUpdater>Canvas>EntryUpdateLoading"}
        panel_update = {"locator": "GameUpdater>Canvas>EntryUpdateLoading>panel_update"}
        progress_label_update = {"locator": "GameUpdater>Canvas>EntryUpdateLoading>panel_update>progress_label"}
        panel_loading = {"locator": "GameUpdater>Canvas>EntryUpdateLoading>panel_loading"}
        tap_to_start = {"locator": "GameUpdater>Canvas>EntryUpdateLoading>panel_go>Button_Login>Text"}

    class EnergyGiftPackPanel:
        EnergyGiftPackPanel = {"locator": "UICanvas>Default>EnergyGiftPackPanel"}

    class EventSignSevenDayPanel:
        EventSignSevenDayPanel = {"locator": "UICanvas>Default>EventSignSevenDayPanel"}
        btn_receive = {"locator": "UICanvas>Default>EventSignSevenDayPanel>panel>btn_receive"}

    class EventsGiftCenterPanel:
        EventsGiftCenterPanel = {"locator": "UICanvas>Important>EventsGiftCenterPanel"}
        btn_close = {"locator": "UICanvas>Important>EventsGiftCenterPanel>panel>btn_close>img"}
        tab_list = {"locator": "UICanvas>Important>EventsGiftCenterPanel>panel>panel_tab>list>Viewport>Content>"}
        viewport = {"locator": "UICanvas>Important>EventsGiftCenterPanel>panel>panel_tab>list>Viewport", "focus": (0, 0)}

    class FishAlbum3DPanel:
        FishAlbum3DPanel = {"locator": "UICanvas>Default>FishAlbum3DPanel"}
        btn_close = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>btn_close>img"}
        btn_share = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>btn_share>btn_normal"}
        btn_switch = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>btn_switch>btn_normal"}
        reward_icon = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>photo_paper>rewards>reward>item_model_mini>icon"}
        btn_preview = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>photo_paper>btn_preview>icon"}
        btn_i = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>photo_paper>rewards>btn_i>img"}
        panel_rewards_tip = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>panel_rewards_tip"}
        panel_fisheries = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_fisheries"}
        fisheries_list_viewport = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_fisheries>panel>FisheriesList>Viewport", "focus": (0, 0)}
        fisheries_list = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_fisheries>panel>FisheriesList>Viewport>Content>", "focus": (0, 0.5)}
        btn_close_tab = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_fisheries>btn_closeb"}
        progress_cur_list = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_top>>progress_value>ValueLayout>cur"}
        photo_name = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>photo_paper>detail>name"}
        photo_bg = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>photo_paper>img_mask>img"}
        star_list = {"locator": "UICanvas>Default>FishAlbum3DPanel>panel_album>panel_left>photo_paper>detail>stars>"}

    class FishAlbumPreviewPanel:
        FishAlbumPreviewPanel ={"locator": "UICanvas>Default>FishAlbumPreviewPanel"}
        btn_close = {"locator": "UICanvas>Default>FishAlbumPreviewPanel>panel>panel_5>btn_close>img"}
        rewards_icon_list = {"locator": "UICanvas>Default>FishAlbumPreviewPanel>btn_rewards>item_list>>icon"}
        rewards_quantity_list = {"locator": "UICanvas>Default>FishAlbumPreviewPanel>btn_rewards>item_list>>quantity>value"}

    class FishBagPanel:
        FishBagPanel = {"locator": "UICanvas>Default>FishBagPanel"}
        btn_close = {"locator": "UICanvas>Default>FishBagPanel>btn_close>img"}
        btn_next = {"locator": "UICanvas>Default>FishBagPanel>panel>panel_bag>btn>btn_next>text"}

    class FishCardGiftPackCustomizePanel:
        FishCardGiftPackCustomizePanel = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel"}
        btn_close = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel>panel>btns>btn_buy"}
        icon_list = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel>panel>main>>>item_model_mini(Clone)>icon"}
        quantity_list = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel>panel>main>>>item_model_mini(Clone)>quantity>value"}
        tab_list = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel>panel>panel_tab>content>TabList>Viewport>Content>", "focus": (0, 0.5)}
        viewport = {"locator": "UICanvas>Default>FishCardGiftPackCustomizePanel>panel>panel_tab>content>TabList>Viewport"}

    class FishCardPackTipsPanel:
        FishCardPackTipsPanel = {"locator": "UICanvas>Default>FishCardPackTipsPanel"}
        item_icon = {"locator": "UICanvas>Default>FishCardPackTipsPanel>bg>list>fishbag>icon"}

        fish_card_name = {"locator": "UICanvas>Default>FishCardPackTipsPanel>bg>list>fishbag>title_bg>title"}

    class FishCardPanel:
        FishCardPanel = {"locator": "UICanvas>Default>FishCardPanel"}
        tab_list = {"locator": "UICanvas>Default>FishCardPanel>panel_tab>content>TabList>Viewport>Content>", "focus": (0, 0.5)}
        fisheries_bg_list = {"locator": "UICanvas>Default>FishCardPanel>panel_tab>content>TabList>Viewport>Content>>bg"}
        fisheries_viewport = {"locator": "UICanvas>Default>FishCardPanel>panel_tab>content>TabList>Viewport", "focus": (0, 0)}
        fisheries_title_list = {"locator": "UICanvas>Default>FishCardPanel>panel_tab>content>TabList>Viewport>Content>>title"}
        btn_close = {"locator": "UICanvas>Default>FishCardPanel>btn_close>img"}
        btn_i = {"locator": "UICanvas>Default>FishCardPanel>title_group>content>btn_i>img"}
        tips_cardbonus = {"locator": "UICanvas>Default>FishCardPanel>tips_cardbonus"}
        btn_upgrade = {"locator": "UICanvas>Default>FishCardPanel>btn_upgrade>text"}
        talent_now_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>upgrade>normal>detail_list>Viewport>Content>>now>title"}
        talent_next_list = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>upgrade>normal>detail_list>Viewport>Content>>next>title"}
        main_name = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>content>name>name"}
        main_size = {"locator": "UICanvas>Default>FishCardPanel>panel>panel_ehhance>content>name>size"}
        fish_card_model_list = {"locator": "UICanvas>Default>FishCardPanel>panel_normal>content>FishCardList>Viewport>content>>"}
        fish_card_viewport = {"locator": "UICanvas>Default>FishCardPanel>panel_normal>content>FishCardList>Viewport"}
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
        btn_events = {"locator": "UICanvas>Default>FishCardPanel>btn_events>img"}
        sub_tab_list = {"locator": "UICanvas>Default>FishCardPanel>panel_normal>subTab>", "focus": (0, 0)}
        rating = {"locator": "UICanvas>Default>FishCardPanel>gs>rating>num"}
        rating_fisheries = {"locator": "UICanvas>Default>FishCardPanel>gs>rating_fisheries>num"}


    class FishCardMultipleLevelUpPanel:
        FishCardMultipleLevelUpPanel = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel"}
        btn_close = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel>Panel>btn_close>img"}
        btn_draw = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel>Panel>content_fishcard>btns>btn_draw>text"}
        choice_all = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel>Panel>content_fishcard>choice>choice>Toggle>Background"}
        choice_list = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel>Panel>content_fishcard>fishcard_list>Viewport>Content>>group>level>Toggle>Background"}
        card_list = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel>Panel>content_fishcard>fishcard_list>Viewport>Content>>group>card"}
        viewport = {"locator": "UICanvas>Default>FishCardMultipleLevelUpPanel>Panel>content_fishcard>fishcard_list>Viewport"}
    class FishCardMultipleLevelUpSuccessPanel:
        FishCardMultipleLevelUpSuccessPanel = {"locator": "UICanvas>Default>FishCardMultipleLevelUpSuccessPanel"}
        btn_close = {"locator": "UICanvas>Default>FishCardMultipleLevelUpSuccessPanel>btn_close>text"}


    class FlashCardPanel:
        FlashCardPanel = {"locator": "UICanvas>Default>FlashCardPanel"}
        FlashCardPanel_btn_shop = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>btns>btn_shop>img"}
        FlashCardPanel_btn_comcard = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>btns>btn_comcard>img"}
        FlashCardPanel_btn_close = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>btn_close>img"}
        FlashCardPanel_btn_i = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>title_group>content>btn_i>img"}
        FlashCardPanel_arrow_right = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_right>arrow>arrow_right>img"}
        FlashCardPanel_arrow_left = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_right>arrow>arrow_left>img"}
        FlashCardPanel_left_item2 = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_left>panel_banner>item2>item_model_mini>icon"}
        FlashCardPanel_left_item1 = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_left>panel_banner>item1>item_model_mini>icon"}
        FlashCardPanel_left_type3 = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_left>panel_type>type3>item>item_model_mini>icon"}
        FlashCardPanel_left_type2 = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_left>panel_type>type2>item>item_model_mini>icon"}
        FlashCardPanel_left_type1 = {"locator": "UICanvas>Default>FlashCardPanel>Panel>Panel_info>panel_left>panel_type>type1>item>item_model_mini>icon"}

    class FlashCardBoxesPanel:
        FlashCardBoxesPanel = {"locator": "UICanvas>Default>FlashCardBoxesPanel"}
        FlashCardBoxes_btn_close = {"locator": "UICanvas>Default>FlashCardBoxesPanel>panel>btn_close>img"}
        FlashCardBoxes_btn_i = {"locator": "UICanvas>Default>FlashCardBoxesPanel>panel>title_group>content>btn_i>img"}


    class FlashCardReceivePanel:
        FlashCardReceivePanel = {"locator": "UICanvas>Default>FlashCardReceivePanel"}
        btn_close = {"locator": "UICanvas>Default>FlashCardReceivePanel>>btn_close>tip"}



    class FishCardUpgradePanel:
        FishCardUpgradePanel = {"locator": "UICanvas>Default>FishCardUpgradePanel"}
        btn_close = {"locator": "UICanvas>Default>FishCardUpgradePanel>btn_close>img"}
        btn_level_up = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>btns>btn_draw", "focus": (0.5, 0.75)}
        talent_now_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>percentList>>now>now"}
        talent_next_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>percentList>>now>next"}
        progress = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>progress>text"}
        level_now = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>level>now"}
        level_next = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>level>next"}
        cost_value_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>cost>bg>>value_cost"}
        cost_icon_list = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>cost>bg>>icon"}
        fisheries_name_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard>card>Fishcard_group>card_group>fishcard_1>>fisheries_bg>fisheries"}
        fish_name_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard>card>Fishcard_group>card_group>fishcard_1>>frame>name"}

        # progress_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>progress>text"}
        level_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard>card>Fishcard_group>card_group>fishcard_1>>kind_02>level>number"}
        rating_card = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard>card>Fishcard_group>card_group>fishcard_1>>kind_02>talent>text"}
        rating_fisheries = {"locator": "UICanvas>Default>FishCardUpgradePanel>rating_fisheries>num"}
        rating = {"locator": "UICanvas>Default>FishCardUpgradePanel>rating>num"}
        # title_bg_selected = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel>FishCard>>title_bg"}
        btn_add_100000 = {"locator": "UICanvas>Default>FishCardUpgradePanel>top_res>ResourceBar>100000>btn_add"}
        text_100000 = {"locator": "UICanvas>Default>FishCardUpgradePanel>top_res>ResourceBar>100000>value"}
        btn_next = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard>arrow>btn_next", "focus": (1, 0.5)}
        btn_previous = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard>arrow>btn_previous", "focus": (0, 0.5)}
        cotent_fishcard= {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>cotent_fishcard"}
        max_text = {"locator": "UICanvas>Default>FishCardUpgradePanel>panel_upgrade>Content>max_text"}

    class FishingTipsPanel:
        FishingTipsPanel = {"locator": "UICanvas>Default>FishingTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>FishingTipsPanel>panel>btn_close>img"}
        tab_main_list = {"locator": "UICanvas>Default>FishingTipsPanel>panel>tab>TabList>Viewport>Content>>bg"}
        tab_sub_list = {"locator": "UICanvas>Default>FishingTipsPanel>panel>>tab>>bg"}
        btn_arrow = {"locator": "UICanvas>Default>FishingTipsPanel>panel>>tips>>btn_arrow>img"}

    class FisheryGiftPackPanel:
        FisheryGiftPackPanel = {"locator": "UICanvas>Default>FisheryGiftPackPanel"}
        btn_close = {"locator": "UICanvas>Default>FisheryGiftPackPanel>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>FisheryGiftPackPanel>panel>btns>btn_buy>btn_normal"}
        icon_list = {"locator": "UICanvas>Default>FisheryGiftPackPanel>panel>main>item_list>>item_model_mini(Clone)>icon"}
        quantity_list = {"locator": "UICanvas>Default>FisheryGiftPackPanel>panel>main>item_list>>item_model_mini(Clone)>quantity>value"}

    class FisheryUnlockPanel:
        FisheryUnlockPanel = {"locator": "UICanvas>Default>FisheryUnlockPanel"}
        btn_close = {"locator": "UICanvas>Default>FisheryUnlockPanel>panel>btn_close>img"}
        btn_go = {"locator": "UICanvas>Default>FisheryUnlockPanel>panel>btn_go"}



    class FlashTipsPanel:
        FlashTipsPanel = {"locator": "UICanvas>Important>FlashTipsPanel"}


    class FriendPanel:
        FriendPanel = {"locator": "UICanvas>Default>FriendPanel"}
        btn_close = {"locator": "UICanvas>Default>FriendPanel>btn_close", "focus": (0.25, 0.5)}
        btn_friend = {"locator": "UICanvas>Default>FriendPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_1>title"}
        btn_add_friend = {"locator": "UICanvas>Default>FriendPanel>panel>panel_tab>content>TabList>Viewport>Content>tab_2>title"}
        input_search = {"locator": "UICanvas>Default>FriendPanel>panel>panel_info>panel_top>search>Input_search"}
        btn_search = {"locator": "UICanvas>Default>FriendPanel>panel>panel_info>panel_top>search>btn_search>icon"}
        btn_add = {"locator": "UICanvas>Default>FriendPanel>panel>panel_info>panel_List>list>Viewport>Content>list(Clone)>add_info>btns>btn_add>text"}



    class GearPanel:
        GearPanel = {"locator": "UICanvas>Default>GearPanel"}
        btn_close = {"locator": "UICanvas>Default>GearPanel>btn_close>img"}
        rodlist_viewport = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport"}
        t_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>"}
        rod_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>>list>>gear_model_new(Clone)"}
        rod_bg_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>>list>>gear_model_new(Clone)>bg"}
        rod_t1_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>group_1>list>>gear_model_new(Clone)"}
        rod_t2_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>group_2>list>>gear_model_new(Clone)"}
        rod_t3_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>group_3>list>>gear_model_new(Clone)"}
        rod_t4_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>Rodlist>Viewport>Content>group_4>list>>gear_model_new(Clone)"}
        btn_filter = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>btn_filter","focus": (0, 1)}
        tip_filter_rod = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>tip_filter_rod"}
        btn_apply = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>tip_filter_rod>options>btns>btn_apply>btn_normal"}
        btn_reset = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>tip_filter_rod>options>btns>btn_reset>btn_normal"}
        available_location_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>tip_filter_rod>options>type_2>>Toggle","focus": (1, 0.5)}
        rarity_list = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>tip_filter_rod>options>type_1>>Toggle","focus": (1, 0.5)}
        hide_unowned = {"locator": "UICanvas>Default>GearPanel>panel_rodlist>content>tip_filter_rod>options>option_0>Toggle","focus": (1, 0.5)}
        dps = {"locator": "UICanvas>Default>GearPanel>dps_bg>num"}
        level = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>level>level"}
        progress_now = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>level>progress>bg>level>now"}
        progress_max = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>level>progress>bg>level>max"}
        btn_upgrade = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>level>btn_upgrade", "focus": (0.75, 0.5)}
        upgrade_max = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>level>btn_max"}
        btn_enhence = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>enhance_bg>btn_collection", "focus": (0.75, 0.5)}
        enhance_max = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>enhance_bg>btn_max"}
        stars = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>enhance_bg>stars>>star_y"}
        t = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>name_bg>t1"}
        kind = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>name_bg>kind"}
        name = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>upgrade_bg>name_bg>name"}
        skill_list = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>enhance_bg>skill_list>>rod_skill>icon_bg>icon"}
        btn_equip = {"locator": "UICanvas>Default>GearPanel>panel_info>panel>content>btn>btn_equip", "focus": (0.5, 1)}


    class GearLevelupPanel:
        GearLevelupPanel = {"locator": "UICanvas>Default>GearLevelupPanel"}
        btn_close = {"locator": "UICanvas>Default>GearLevelupPanel>btn_close>img"}
        btn_next = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>arrow>btn_next", "focus": (1, 0.5)}
        btn_previous = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>arrow>btn_previous", "focus": (0, 0.5)}
        t = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>name_bg>t1"}
        kind = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>name_bg>kind"}
        name = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>name_bg>name"}
        stars = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>stars>>star_y"}
        dps = {"locator": "UICanvas>Default>GearLevelupPanel>panel_basic>panel>dps_bg>num"}
        lv = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>level_change>value"}
        lv_next = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>level_change>value_next"}
        skill_value_list = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>list>>value"}
        skill_value_next_list = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>list>>value_next"}
        cost_icon_list = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>cost>>icon"}
        cost_quantity_list = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>cost>>value"}
        btn_upgrade = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>btn_upgrade", "focus": (0.5, 1)}
        btn_add_100000 = {"locator": "UICanvas>Default>GearLevelupPanel>top_res>ResourceBar>100000>btn_add"}
        resource_icon_list = {"locator": "UICanvas>Default>GearLevelupPanel>top_res>ResourceBar>>icon"}
        resource_quantity_list = {"locator": "UICanvas>Default>GearLevelupPanel>top_res>ResourceBar>>value"}
        max = {"locator": "UICanvas>Default>GearLevelupPanel>panel_upgrade>content>normal>max_text"}


    class GearEnhancePanel:
        GearEnhancePanel = {"locator": "UICanvas>Default>GearEnhancePanel"}
        btn_close = {"locator": "UICanvas>Default>GearEnhancePanel>btn_close>img"}
        btn_next = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>arrow>btn_next", "focus": (1, 0.5)}
        btn_previous = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>arrow>btn_previous", "focus": (0, 0.5)}
        stars = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>stars>>star_y"}
        t = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>name_bg>t1"}
        kind = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>name_bg>kind"}
        name = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>name_bg>name"}
        dps = {"locator": "UICanvas>Default>GearEnhancePanel>panel_basic>panel>dps_bg>num"}
        stars_now = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>star_change>stars_now>>star_y"}
        stars_next = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>star_change>stars_next>>star_y"}
        btn_enhance = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>btn_enhance", "focus": (0.5, 1)}
        cost_numerator = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>cost>res_1>value_cost"}
        cost_denominator = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>cost>res_1>value"}
        skill_value_list = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>list>>value"}
        skill_value_next_list = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>list>>value_next"}
        skill_icon = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>normal>skill>bg>rod_skill>rod_skill>icon_bg>icon"}
        max = {"locator": "UICanvas>Default>GearEnhancePanel>panel_enhance>content>max_text"}

    class GearEnhanceSuccesPanel:
        GearEnhanceSuccesPanel = {"locator": "UICanvas>Default>GearEnhanceSuccesPanel"}
        btn_close = {"locator": "UICanvas>Default>GearEnhanceSuccesPanel>panel>btn_close>tip"}

    class GearSkillTipsPanel:
        GearSkillTipsPanel = {"locator": "UICanvas>Default>GearSkillTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>GearSkillTipsPanel>btn_close", "focus": (0.5, 1)}
        skill_icon = {"locator": "UICanvas>Default>GearSkillTipsPanel>panel>Content>title_group>rod_skill>rod_skill>icon_bg>icon"}

    class HomePanel:
        #panel_left
        HomePanel = {"locator": "UICanvas>Default>HomePanel"}
        btn_rookie3days = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Viewport>Content>btn_rookie3days>img"}
        btn_bp = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>btn_bp>img"}
        # panel_events
        btn_globa_progress = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Viewport>Content>btn_globa_progress"}
        btn_center_new = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Viewport>Content>btn_center_new"}
        btn_iaa = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_iaa>img"}
        btn_endless = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_endless>img"}
        btn_events_endless_thanksgiving = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>btn_events_endless_thanksgiving>img"}
        btn_events_endless_newyear = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>btn_events_endless_newyear>img"}
        btn_1add1 = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>btn_1add1", "focus": (1, 0.5)}
        btn_black5 = {"locator": "UICanvas>Default>HomePanel>panel>panel_events>events_list>Viewport>Content>btn_black5>img"}
        # panel_entrance
        btn_fishcard = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_fishcard"}
        btn_next = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>page_arrow>btn_next>img"}
        btn_previous = {"locator": "UICanvas>Default>HomePanel>panel>panel_entrance>page_arrow>btn_previous>img"}
        # panel_player_info
        btn_event_location = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>giftpack>btn_event_location", "focus": (1, 0.5)}
        btn_mail = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btns>btn_mail>icon"}
        btn_questionnaire = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btns>btn_questionnaire>icon"}
        btn_download = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btns>btn_download>icon"}
        btn_code = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btns>btn_code"}
        btn_exp_buff = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btn_exp_buff>icon"}
        btn_friend = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btns>btn_friend>icon"}
        Panel_tip = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btn_exp_buff>Panel_tip"}
        player_info = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>bg"}
        panel_player_info_btns = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>btns>", "focus": (0, 0)}
        player_name = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>player_name"}  # text
        player_lv = {"locator":"UICanvas>Default>HomePanel>panel>panel_player_info>player_info>player_exp>player_lv>value"}  # text
        exp = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>player_exp>exp"}  # value
        head_img = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>head>head_mask>head_img"}
        head_frame = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>head>head_frame>panel>head_frame"}
        flag = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>flag"}
        rating = {"locator": "UICanvas>Default>HomePanel>panel>panel_player_info>player_info>rating>num"}
        ResourceBar = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar"}
        # btn_add
        btn_add_100500 = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>100500>btn_add"}
        btn_add_100000 = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>100000>btn_add"}
        btn_add_100100 = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>100100>btn_add"}
        # navbar
        btn_career = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_career"}
        btn_gears = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_gears"}
        btn_task_main = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_task_main"}
        btn_task = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_task"}
        btn_task_rookie = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_task_rookie"}
        btn_achievement = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_achievement"}
        btn_fishalbum = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_fishalbum"}
        btn_aquarium = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_aquarium"}
        # panel_giftpack
        btn_fishranking = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>btn_fishranking>img"}
        btn_store = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>btn_store>img"}
        panel_left_btns = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Viewport>Content>>img"}
        panel_giftpack_btns = {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>", "focus": (0, 0.5)}
        top_res_btns = {"locator": "UICanvas>Default>HomePanel>panel>top_res>ResourceBar>>btn_add"}
        navbar_btns = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>"}
        btn_chat = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>btn_chat"}


        class Panel_mini_task:
            # minitask
            panel_mini_task = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Panel_mini_task"}
            btn_recommend = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Panel_mini_task>Panel>btn_recommend"}
            btn_go = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Panel_mini_task>Panel>btn_go"}
            btn_claim = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Panel_mini_task>Panel>btn_claim"}
            text_task = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Panel_mini_task>Panel>text"}
            progress = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>list>Panel_mini_task>Panel>progress>value"}

    class Home3DPanel:
        Home3DPanel ={"locator": "HomeCanvas>Home3DPanel", "camera": "Camera3D"}
        panel_entrance_btns = {"locator": "HomeCanvas>Home3DPanel>panel>panel_entrance>", "camera": "Camera3D"}
        btn_chest = {"locator": "HomeCanvas>Home3DPanel>panel>chest>btn_chest", "camera": "Camera3D"}
        btn_pve = {"locator": "HomeCanvas>Home3DPanel>panel>panel_entrance>btn_pve>text", "camera": "Camera3D"}
        btn_pvp = {"locator": "HomeCanvas>Home3DPanel>panel>panel_entrance>btn_pvp", "camera": "Camera3D"}
        btn_avatar = {"locator": "HomeCanvas>Home3DPanel>panel>panel_avatar>btn_avatar", "camera": "Camera3D"}


    class KatanaPackPopupPanel:
        KatanaPackPopupPanel= {"locator":"UICanvas>Default>KatanaPackPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>KatanaPackPopupPanel>btn_close>img"}

    class IAAPanel:
        IAAPanel= {"locator": "UICanvas>Default>IAAPanel"}
        btn_close = {"locator": "UICanvas>Default>IAAPanel>panel>btn_close>img"}



    class ItemTipsPanel:
        ItemTipsPanel = {"locator": "UICanvas>Default>ItemTipsPanel"}
        title = {"locator": "UICanvas>Default>ItemTipsPanel>panel>title_bg>title"}
        icon = {"locator": "UICanvas>Default>ItemTipsPanel>panel>bg>patterns1>icon"}
        quantity = {"locator": "UICanvas>Default>ItemTipsPanel>panel>info>quantity>value"}

    class LeaderBoardPanel:
        LeaderBoardPanel = {"locator":"UICanvas>Default>LeaderBoardPanel"}
        btn_close = {"locator":"UICanvas>Default>LeaderBoardPanel>Panel>btn_close>img"}
        btn_i = {"locator":"UICanvas>Default>LeaderBoardPanel>Panel>left_banner>btn_i>img"}
        tap_to_close = {"locator":"UICanvas>Default>LeaderBoardPanel>Panel>tips>btn_close"}
        top_100_rewards_icon_list = {"locator":"UICanvas>Default>LeaderBoardPanel>Panel>left_banner>rewards>>icon"}
        top_100_rewards_quantity_list = {"locator": "UICanvas>Default>LeaderBoardPanel>Panel>left_banner>rewards>>quantity>value"}
        coin = {"locator": "UICanvas>Default>LeaderBoardPanel>Panel>rigth_ranking>list_myself>coin>value"}
        ranking = {"locator": "UICanvas>Default>LeaderBoardPanel>Panel>rigth_ranking>list_myself>num_value"}
        rewards_icon_list = {"locator":"UICanvas>Default>LeaderBoardPanel>Panel>rigth_ranking>list_myself>rewards>>icon"}
        rewards_quantity_list = {"locator": "UICanvas>Default>LeaderBoardPanel>Panel>rigth_ranking>list_myself>rewards>>quantity>value"}

    class LeaderBoardPopResultPanel:
        LeaderBoardPopResultPanel = {"locator":"UICanvas>Default>LeaderBoardPopResultPanel"}
        reward_icon_list = {"locator":"UICanvas>Default>LeaderBoardPopResultPanel>Panel>rewards>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>LeaderBoardPopResultPanel>Panel>rewards>>quantity>value"}
        btn_claim = {"locator":"UICanvas>Default>LeaderBoardPopResultPanel>Panel>btn_collect>btn_normal"}

    class LoadingPanel:
        LoadingPanel = {"locator": "UICanvas>Default>LoadingPanel"}

    class LocationPanel:
        LocationPanel = {"locator": "UICanvas>Default>LocationPanel"}
        btn_cancel = {"locator": "UICanvas>Default>LocationPanel>panel>btns>btn_cancel"}

    class LoadingFisheryPanel:
        LoadingFisheryPanel = {"locator": "UICanvas>Default>LoadingFisheryPanel"}

    class LoginPanel:
        LoginPanel = {"locator": "UICanvas>Default>LoginPanel"}
        InputField_UserName = {"locator": "UICanvas>Default>LoginPanel>panel_internal>InputField_UserName"}
        btn_login = {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login>text"}
        btn_login_cn = {"locator": "UICanvas>Default>LoginPanel>panel_cn>btn_login>Text"}
        Dropdown = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown", "focus": (1, 0.5)}
        DropdownList_Viewport = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport", "focus": (0, 0)}
        DropdownList = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>"}
        dev_server = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>Item 0: dev server"}
        dev_qa_server = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>Item 1: dev-qa server"}
        dev_release_server = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>Item 2: dev-release server"}

    class LoginAnnouncementPanel:
        LoginAnnouncementPanel = {"locator": "UICanvas>Default>LoginAnnouncementPanel"}
        btn_close = {"locator": "UICanvas>Default>LoginAnnouncementPanel>Panel>btn_close>img"}

    # 邮箱
    class MailPanel:
        MailPanel = {"locator": "UICanvas>Default>MailPanel"}
        btn_close = {"locator": "UICanvas>Default>MailPanel>btn_close>img"}
        EmptyMailTip = {"locator": "UICanvas>Default>MailPanel>EmptyMailTip"}
        MailDetail = {"locator": "UICanvas>Default>MailPanel>MailDetail"}
        tab_list = {"locator": "UICanvas>Default>MailPanel>MailList>tab_switch>>bg"}
        mail_list = {"locator": "UICanvas>Default>MailPanel>MailList>MailArea>Scroll View>Viewport>Content>", "focus": (0.5, 0)}
        mail_viewport = {"locator": "UICanvas>Default>MailPanel>MailList>MailArea>Scroll View>Viewport", "focus": (0, 0)}
        mail_detail_viewport = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport","focus": (0, 0)}
        reward_icon_list = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>rewards>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>rewards>>quantity>value"}
        btn_claim = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>btn_group>btn_claim>btn_normal"}
        text_claimed = {"locator": "UICanvas>Default>MailPanel>MailDetail>panel>Content>Scroll View>Viewport>Content>rewards_group>btn_group>text_claimed"}

    class MessageBoxPanel:
        MessageBoxPanel = {"locator": "UICanvas>Important>MessageBoxPanel"}
        btn_cancel = {"locator": "UICanvas>Important>MessageBoxPanel>Panel>btns>btn_cancel>btn_normal"}
        btn_confirm = {"locator": "UICanvas>Important>MessageBoxPanel>Panel>btns>btn_confirm>btn_normal"}
        toggle = {"locator": "UICanvas>Important>MessageBoxPanel>Panel>option_2>Toggle>Background>bg"}

    class MidAutumnPackPopupPanel:
        MidAutumnPackPopupPanel = {"locator": "UICanvas>Default>MidAutumnPackPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>MidAutumnPackPopupPanel>btn_close>img"}

    class MonthCardPopPanel:
        MonthCardPopPanel = {"locator": "UICanvas>Default>MonthCardPopPanel"}
        btn_close = {"locator": "UICanvas>Default>MonthCardPopPanel>panel>btn_close>img"}
        btn_go = {"locator": "UICanvas>Default>MonthCardPopPanel>panel>btn_go", "focus": (1, 1)}


    class NewbieGuidePanel:
        NewbieGuidePanel = {"locator": "UICanvas>Default>NewbieGuidePanel"}
        NewbieGuidePanel_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_1(Clone)"}
        NewbieGuidePanel_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_10(Clone)"}
        NewbieGuidePanel_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_15(Clone)"}
        NewbieGuidePanel_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_1(Clone)"}
        NBG_rookie_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_1(Clone)>Guide_VirtualBtn>text"}
        NBG_rookie_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_2(Clone)>Guide_VirtualBtn"}
        NBG_rookie_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_3(Clone)>Guide_Highlight>et_Panel_Tournaments_entrance"}
        NBG_rookie_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_4(Clone)>Guide_VirtualBtn"}
        NBG_rookie_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_5(Clone)>Guide_VirtualBtn"}
        NBG_rookie_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_6(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_7 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_7(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_8 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_8(Clone)>Guide_HighTensionCloseBtn>text", "focus": (0.5, 1)}
        NBG_rookie_9 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_9(Clone)>Guide_VirtualBtn>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_10 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_10(Clone)"}
        NBG_rookie_11 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_11(Clone)"}
        NBG_rookie_12 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_12(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_13_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTEInfoCloseBtn>text"}
        NBG_rookie_13_Guide_ULTUp = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_ULTUp"}
        NBG_rookie_13_Guide_QTEInfo = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTEInfo"}
        NBG_rookie_13_Guide_QTE_left = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTE_left"}
        NBG_rookie_13_Guide_ULTInfoCloseBtn = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_ULTInfoCloseBtn"}
        # NBG_rookie_13_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)"}
        joystick = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_13(Clone)>Guide_QTE_right>Guide_Hand_Joystick>joystick"}
        NBG_rookie_14 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_14(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_rookie_15 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_15(Clone)>Guide_VirtualBtn"}
        NBG_rookie_16 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_16(Clone)>Guide_VirtualBtn"}
        NBG_rookie_17 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_17(Clone)"}
        NBG_rookie_18 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_rookie_18(Clone)>Guide_VirtualBtn"}
        NBG_system_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_1(Clone)>Guide_VirtualBtn"}
        NBG_system_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_2(Clone)>Guide_VirtualBtn"}
        NBG_system_click_TreasureChest = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_click_TreasureChest(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_system_get_reward_TreasureChest_01 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_get_reward_TreasureChest_01(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_system_close_TreasureChest = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_close_TreasureChest(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 鱼册引导
        NBG_prepare_2_album_01= {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_prepare_2_album_01(Clone)>Guide_VirtualBtn>text", "focus": (0.5, 1)}
        NBG_prepare_2_album_02 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_prepare_2_album_02(Clone)>Guide_VirtualBtn>text","focus": (0.5, 1)}
        NBG_prepare_2_album_03 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_prepare_2_album_03(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_album_01 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_album_01(Clone)"}
        NBG_album_02 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_album_02(Clone)"}
        NBG_album_03 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_album_03(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_album_04 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_album_04(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_prepare_weak_01 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_prepare_weak_01(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 水族箱引导
        NBG_aquarium_1_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_1_1(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_2_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_1(Clone)"}
        NBG_aquarium_2_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_2(Clone)"}
        NBG_aquarium_2_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_3(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_2_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_4(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_2_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_5(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_2_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_6(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_2_7= {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_2_7(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_3_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_3_1(Clone)"}
        NBG_aquarium_3_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_3_2(Clone)"}
        NBG_aquarium_3_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_3_3(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_3_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_3_4(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_3_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_3_5(Clone)"}

        # 水族箱引导新
        NBG_aquarium_new_1_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_1_1(Clone)"}
        NBG_aquarium_new_1_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_1_2(Clone)"}
        NBG_aquarium_new_1_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_1_3(Clone)>Guide_Arrow>arrow"}
        NBG_aquarium_new_2_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_2_1(Clone)"}
        NBG_aquarium_new_2_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_2_2(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_2_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_2_3(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_2_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_2_4(Clone)"}
        NBG_aquarium_new_2_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_2_5(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_3_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_3_1(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_3_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_3_2(Clone)"}
        NBG_aquarium_new_3_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_3_3(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_3_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_3_4(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_4_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_4_1(Clone)"}
        NBG_aquarium_new_4_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_4_2(Clone)"}
        NBG_aquarium_new_4_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_4_3(Clone)"}
        NBG_aquarium_new_4_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_4_4(Clone)"}
        NBG_aquarium_new_4_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_4_5(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_aquarium_new_4_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_aquarium_new_4_6(Clone)"}

        # 刺鱼引导
        NBG_hook_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_hook_1(Clone)"}
        NBG_hook_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_hook_2(Clone)"}
        NBG_hook_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_hook_3(Clone)"}
        NBG_hook_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_hook_4(Clone)"}
        NBG_hook_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_hook_5(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 鱼卡引导
        NBG_fishcard_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishcard_1(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishcard_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishcard_2(Clone)"}
        NBG_fishcard_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishcard_5(Clone)"}
        NBG_fishcard_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishcard_3(Clone)"}
        NBG_fishcard_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishcard_4(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 悬赏鱼引导
        NBG_fishphoto_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishphoto_2(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishphoto_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishphoto_3(Clone)"}

        # 升装备引导
        NBG_fishing_fail_0 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_0(Clone)"}
        NBG_fishing_fail_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_1(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_2(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_3(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_4(Clone)"}
        NBG_fishing_fail_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_5(Clone)"}
        NBG_fishing_fail_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_6(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_7 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_7(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 俱乐部引导
        NBG_system_click_Club = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_click_Club(Clone)>Guide_VirtualBtn", "focus": (1, 1) }
        NBG_system_club_apply = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_system_club_apply(Clone)"}

        # 对决引导
        NBG_friend_duel_1_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_friend_duel_1_1(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 多人房引导
        NBG_multiRoom_0 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_multiRoom_20200(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_multiRoom_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_multiRoom_20201(Clone)>Guide_Highlight>ep_UI_novice guide", "focus": (0.5, 0.2) }
        NBG_multiRoom_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_multiRoom_20202(Clone)>Guide_Highlight>ep_UI_novice guide"}

        # 抛竿引导
        NBG_fishingcast_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishingcast_1(Clone)"}
        NBG_fishingcast_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishingcast_2(Clone)>Guide_btn>btn_orange"}

        # 钓点引导
        NBG_fishpoint_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_1(Clone)"}
        NBG_fishpoint_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_2(Clone)"}
        NBG_fishpoint_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_3(Clone)"}
        NBG_fishpoint_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_4(Clone)"}
        NBG_fishpoint_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_5(Clone)"}
        NBG_fishpoint_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_6(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishpoint_7 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_7(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishpoint_8 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishpoint_8(Clone)>Guide_Highlight>ep_UI_novice guide"}


    class NewbieGuidePanel_oversea:
        # 升装备引导
        NBG_fishing_fail_1 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_1(Clone)"}
        NBG_fishing_fail_2 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_2(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_3 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_3(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_4 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_4(Clone)"}
        NBG_fishing_fail_5 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_5(Clone)"}
        NBG_fishing_fail_6 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_6(Clone)>Guide_Highlight>ep_UI_novice guide"}
        NBG_fishing_fail_7 = {"locator": "UICanvas>Default>NewbieGuidePanel>NBG_fishing_fail_7(Clone)>Guide_Highlight>ep_UI_novice guide"}


    class NewbieTaskPanel:
        NewbieTaskPanel = {"locator": "UICanvas>Default>NewbieTaskPanel"}
        btn_close = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>btn_close>img"}
        remain_time = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_left>time"}
        btn_i = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>title_group>content>btn_i>img"}
        tap_to_close = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>tips>btn_close>text", "focus": (0.5, 1)}
        btn_sale = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_left>bottom>btn_sale"}
        btn_leaderboard = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_right>banner_up>btn_leaderboard"}
        coin = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>rewards>left>value"}
        progress_reward_viewport = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>rewards>reward_list>view", "focus": (0, 0)}
        progress_reward_list = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>rewards>reward_list>view>content>"}

        max_reward = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>rewards>right"}
        tab_list = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_right>tab>content>"}
        task_viewport = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_right>task>Viewport", "focus": (0, 0)}
        task_list = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_right>task>Viewport>Content>"}
        challenge_viewport = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_right>challenge>Viewport", "focus": (0, 0)}
        challenge_list = {"locator": "UICanvas>Default>NewbieTaskPanel>Panel>panel_right>challenge>Viewport>Content>"}


    class PartySalePanel:
        PartySalePanel = {"locator": "UICanvas>Default>PartySalePanel"}
        btn_close = {"locator": "UICanvas>Default>PartySalePanel>panel_gift>btn_close>text","focus": (0.5, 1)}
        btn_buy = {"locator": "UICanvas>Default>PartySalePanel>panel_gift>content>btn_buy", "focus": (0.5, 0.5)}
        item_icon_list = {"locator": "UICanvas>Default>PartySalePanel>panel_gift>content>bg>item>>icon"}
        item_quantity_list = {"locator": "UICanvas>Default>PartySalePanel>panel_gift>content>bg>item>>quantity>value"}
        cost_icon = {"locator": "UICanvas>Default>PartySalePanel>panel_gift>content>btn_buy>icon"}
        cost_quantity = {"locator": "UICanvas>Default>PartySalePanel>panel_gift>content>btn_buy>text"}

    class PlayerEditNamePanel:
        PlayerEditNamePanel = {"locator": "UICanvas>Default>PlayerEditNamePanel"}
        head_viewport = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>panel_info>HeadList>Viewport","focus": (0, 0)}
        btn_confirm = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>panel_info>btns>btn_confirm"}
        Input_PlayerName = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>panel_info>Input_PlayerName"}
        btn_confirm_oversea = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>btns>btn_confirm>btn_normal"}
        Input_PlayerName_oversea = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>Input_PlayerName"}
        head_list = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>panel_info>HeadList>Viewport>Content>>head>head_mask>head_img"}
        select = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>panel_info>HeadList>Viewport>Content>>select"}

    class PlayerEditNamePanel_oversea:
        PlayerEditNamePanel = {"locator": "UICanvas>Default>PlayerEditNamePanel"}
        head_viewport = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>HeadList>Viewport","focus": (0, 0)}
        btn_confirm = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>btns>btn_confirm"}
        Input_PlayerName = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>Input_PlayerName"}
        head_list = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>HeadList>Viewport>Content>>head"}
        select = {"locator": "UICanvas>Default>PlayerEditNamePanel>panel>HeadList>Viewport>Content>>select"}


    class PlayerInfoPanel:
        PlayerInfoPanel = {"locator": "UICanvas>Default>PlayerInfoPanel"}
        btn_close = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>btn_close>img"}

        btn_changecamera = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>btns_left>btn_changecamera>img"}
        tab_list = {"locator":"UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_tab>tab>>bg"}

        btn_edit_player_info = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>btn_edit"}
        btn_copy = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>player_top>btn_copy>img"}
        btn_i_rating = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>btn_i>img"}
        rating_fishcard = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>tips_rating>bg>list>rating2>text"}
        rating_career = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>tips_rating>bg>list>rating1>text"}
        player_name = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>player_top>player_name"}
        lv = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>player_top>player_lv>value"}
        rating = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>rating>num"}
        head_img = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>head>head_mask>head_img"}
        head_frame = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>player_info>head>head_frame>panel>"}
        division_value = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>playerinfo>division_info>num>value"}
        btn_i_rod = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>badgewallinfo>player_rod>btn_i>img"}
        Panel_Tip_Rules = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard>panel>panel_playerinfo>panel_right>badgewallinfo>Panel_Tip_Rules"}
        btn_giftcode = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>btn>btn_giftcode>icon"}
        giftcode_input = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Giftcode>Panel>input_box"}
        btn_close_additional = {"locator": "UICanvas>Default>PlayerInfoPanel>>Panel>btn_close>img"}
        btn_setting = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>btn>btn_setting>icon"}
        btn_logout = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>btns>btn_logout>icon"}

        btn_edit_achievement = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>badgewallinfo>player_badge>btn_edit"}
        btn_confirm = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Popups_Edit_badge>btns>btn_confirm"}
        viewport_badge_show = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>badgewallinfo>player_badge>Viewport", "focus": (0, 0)}
        viewport_badge_select = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Popups_Edit_badge>list>Viewport"}
        badge_show_list = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Panel_PlayerCard_new>panel>panel_playerinfo>badgewallinfo>player_badge>Viewport>Content>go>"}
        badge_select_list = {"locator": "UICanvas>Default>PlayerInfoPanel>panel>Popups_Edit_badge>list>Viewport>Content>"}

        options_music = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options_music>slider"}
        options_sound = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options_sound>slider"}
        options_graphics_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_graphics>btn_switch>>text"}
        options_joystick_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_joystick>btn_switch>>text"}
        options_frame_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_frame>btn_switch>>text"}
        options_vibration_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_vibration>btn_switch>>text"}
        options_gyro_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_gyro>btn_switch>>text"}
        options_id = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_id>value"}
        options_invite_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_invite>btn_switch>>text"}
        btn_copy_id = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options>options_id>btn_copy>img"}

        tab_avatar = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_1>bg"}
        tab_head_frame = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_5>bg"}
        tab_name = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_3>bg"}
        tab_setting = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_4>bg"}
        btn_save_profile = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>>btn>btn_save", "focus": (0.5, 1)}
        btn_save_head_frame = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_head_frame>Head_frame_right>Head_frame>btn>btn_save", "focus": (0.5, 1)}
        btn_save_pay = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_name>btn>btn_cast", "focus": (0.5, 1)}
        Input_PlayerName = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_name>Input_PlayerName"}
        value_cost = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_name>btn>btn_cast>value_cost"}
        head_frame_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_head_frame>Head_frame_left>Head_frame_List>Viewport>Content>>head_frame>panel>" }
        avatar_list = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_avatar>HeadList>Viewport>Content>"}
        viewport_avatar = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_avatar>HeadList>Viewport", "focus": (0, 0)}
        viewport_head_frame = {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_head_frame>Head_frame_left>Head_frame_List>Viewport", "focus": (0, 0)}

    class PlayerInteractPanel:
        PlayerInteractPanel = {"locator": "UICanvas>Default>PlayerInteractPanel"}
        btn_close = {"locator":"UICanvas>Default>PlayerInteractPanel>panel>btn_close>img"}
        btn_changecamera = {"locator": "UICanvas>Default>PlayerInteractPanel>panel>btns_left>btn_changecamera>img"}
        panel_tab1 = {"locator": "UICanvas>Default>PlayerInteractPanel>panel>panel_tab>tab>1>icon"}
        panel_tab2 = {"locator": "UICanvas>Default>PlayerInteractPanel>panel>panel_tab>tab>2>icon"}
        panel_tab3 = {"locator": "UICanvas>Default>PlayerInteractPanel>panel>panel_tab>tab>3>icon"}

        player_rod_btn_i = {"locator": "UICanvas>Default>PlayerInteractPanel>panel>panel_playerinfo>badgewallinfo>player_rod>btn_i>img"}
        btn_aquarium = {"locator": "UICanvas>Default>PlayerInteractPanel>panel>btn>btn_aquarium>btn_normal"}

    class PlayerLevelupPanel:
        PlayerLevelupPanel = {"locator":"UICanvas>Default>PlayerLevelupPanel"}
        tap_to_continue = {"locator":"UICanvas>Default>PlayerLevelupPanel>panel>text"}

    #  设置
    class PlayerSettingPanel:
        PlayerSettingPanel = {"locator": "UICanvas>Default>PlayerSettingPanel"}
        btn_close = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>btn_close>img"}
        btn_giftcode = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_tab>content>btn_giftcode"}
        giftcode_input = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Giftcode>Panel>input_box"}
        btn_close_additional = {"locator": "UICanvas>Default>PlayerSettingPanel>>Panel>btn_close>img"}
        btn_confirm = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Giftcode>Panel>btn>btn_confirm", "focus":(0.5, 1)}
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
        flag = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>flag"}
        player_name = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>player_name"}
        player_lv = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>player_exp>player_lv>value"}
        exp = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_info>player_exp>exp"}
        badge_player_list = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_right>content>player_badge>badges>>badge_img"}
        points = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_record>detail>panel_info>points>value"}
        weight = {"locator": "UICanvas>Default>PlayerSettingPanel>panel>panel_playerinfo>panel_record>detail>panel_info>weight>value"}
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
        avatar_list = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_avatar>HeadList>Viewport>Content>", "focus": (0, 0)}
        banner_list = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_banner>BannerList>Viewport>Content>", "focus": (0, 0)}
        badge_list = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_badge>BadgeList>Viewport>Content>", "focus": (0, 0)}
        Input_PlayerName = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_name>Input_PlayerName"}
        btn_save_profile = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>>btn>btn_save>btn_normal"}
        btn_saved_profile = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>>btn>tip"}
        viewport_avatar = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_avatar>HeadList>Viewport", "focus":(0, 0)}
        viewport_banner = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_banner>BannerList>Viewport", "focus":(0, 0)}
        viewport_badge = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_badge>BadgeList>Viewport", "focus":(0, 0)}
        badge_slot_list = {"locator": "UICanvas>Default>PlayerSettingPanel>Panel_Popups_Edit>Panel>panel_badge>badge_slot>badges>"}
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

    class ProgressRewardsPanel:
        ProgressRewardsPanel = {"locator": "UICanvas>Default>ProgressRewardsPanel"}
        btn_close = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>btn_close>img"}
        btn_go = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>btn_go"}
        btn_i = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>progress_info>btn_i>img"}
        big_rewards_icon_list = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>big_rewards>>icon"}
        progress_cur = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>progress_info>progress>progressValueLayout>cur"}
        progress_max = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>progress_info>progress>progressValueLayout>max"}
        next_reward_icon = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>progress_info>reward>reward_1>item_model_mini>icon"}
        next_reward_quantity = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>progress_info>reward>reward_1>item_model_mini>quantity>value"}
        current_rewards_icon_list = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>big_rewards>>icon"}
        current_rewards_quantity_list = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>AD>big_rewards>>quantity>value"}
        btn_claim = {"locator": "UICanvas>Default>ProgressRewardsPanel>Panel>current_rewards>btn_claim"}

    class PVEMultiRoomFriendPanel:
        PVEMultiRoomFriendPanel = {"locator": "UICanvas>Default>PVEMultiRoomFriendPanel"}
        btn_close = {"locator": "UICanvas>Default>PVEMultiRoomFriendPanel>btn_close"}

    class PVENewbieGiftPackPanel:
        PVENewbieGiftPackPanel = {"locator": "UICanvas>Default>PVENewbieGiftPackPanel"}
        btn_close = {"locator": "UICanvas>Default>PVENewbieGiftPackPanel>btn_close>img"}
        btn_buy = {"locator": "UICanvas>Default>PVENewbieGiftPackPanel>panel>btns>btn_buy"}
        item_icon_list = {"locator":"UICanvas>Default>PVENewbieGiftPackPanel>panel>main>item_list_up>model(Clone)>item_model_mini(Clone)>icon"}

    class PVERuleTipsPanel:
        PVERuleTipsPanel = {"locator": "UICanvas>Default>PVERuleTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>PVEMultiRoomFriendPanel>btn_close"}


    class PVPBattleHUDPanel:
        PVPBattleHUDPanel = {"locator": "UICanvas>Default>PVPBattleHUDPanel"}
        btn_chat = {"locator": "UICanvas>Default>PVPBattleHUDPanel>panel_pvp_scoreboard>panel>blue>btn_chat_new>icon"}
        btn_surrender = {"locator": "UICanvas>Default>PVPBattleHUDPanel>panel_pvp_scoreboard>panel>blue>chat_list>btn_surrender>text"}
        emoji_list = {"locator": "UICanvas>Default>PVPBattleHUDPanel>panel_pvp_scoreboard>panel>blue>chat_list>emoji>>bg"}
    class PVPBoosterGiftPackPanel:
        PVPBoosterGiftPackPanel = {"locator":"UICanvas>Default>PVPBoosterGiftPackPanel"}
        btn_close = {"locator":"UICanvas>Default>PVPBoosterGiftPackPanel>btn_close>img"}

    class PVPHallPanel:
        PVPHallPanel = {"locator": "UICanvas>Default>PVPHallPanel"}
        btn_play_list = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_entrance>List>Viewport>Content>>model>btn_match>btn_normal"}
        btn_close = {"locator": "UICanvas>Default>PVPHallPanel>Panel>btn_close>img"}
        Viewport = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_entrance>List>Viewport", "focus": (0, 0)}
        entrance_list = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_entrance>List>Viewport>Content>"}
        btn_turntable = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_turntable>btn_normal"}
        btn_leaderboard = {"locator": "UICanvas>Default>PVPHallPanel>Panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_leaderboard", "focus":(1, 0.5)}
        btn_i = {"locator": "UICanvas>Default>PVPHallPanel>Panel>title_group>btn_i>img"}

    class PVPMatchPanel:
        PVPMatchPanel = {"locator":"UICanvas>Default>PVPMatchPanel"}
        btn_cancel = {"locator":"UICanvas>Default>PVPMatchPanel>panel_opponent_top>btn_cancel>btn_normal"}

    class PVPResultPanel:
        PVPResultPanel = {"locator": "UICanvas>Default>PVPResultPanel"}
        tap_to_close = {"locator": "UICanvas>Default>PVPResultPanel>panel>result>btn_close>text"}
        points_enemy = {"locator": "UICanvas>Default>PVPResultPanel>panel>top>red>player_info>points"}
        points_mine = {"locator": "UICanvas>Default>PVPResultPanel>panel>top>blue>player_info>points"}
        btn_open = {"locator": "UICanvas>Default>PVPResultPanel>panel>result>result_detail_list>detail_list>btn_open>img"}
        right_list = {"locator": "UICanvas>Default>PVPResultPanel>panel>result>result_detail_list>detail_list>points>Viewport>Content>>type_right>"}

    class PVPRoomInvitePanel:
        PVPRoomInvitePanel = {"locator": "UICanvas>Important>PVPRoomInvitePanel"}
        btn_cancel = {"locator": "UICanvas>Important>PVPRoomInvitePanel>Panel>btns>btn_cancel", "focus":(0, 0)}
        btn_confirm = {"locator": "UICanvas>Important>PVPRoomInvitePanel>Panel>btns>btn_confirm", "focus":(0, 0)}

    class PVPRoomPanel:
        PVPRoomPanel = {"locator": "UICanvas>Default>PVPRoomPanel"}
        btn_close = {"locator": "UICanvas>Default>PVPRoomPanel>panel>btn_close>img"}
        btn_start = {"locator":"UICanvas>Default>PVPRoomPanel>panel>btn_start"}

    class PVPRuleTipsPanel:
        PVPRuleTipsPanel = {"locator": "UICanvas>Default>PVPRuleTipsPanel"}
        btn_close = {"locator": "UICanvas>Default>PVPRuleTipsPanel>Panel_Popups_Edit>Panel>btn_close>img"}

    class QuestionnairePanel:
        QuestionnairePanel = {"locator": "UICanvas>Important>QuestionnairePanel"}
        btn_close = {"locator": "UICanvas>Important>QuestionnairePanel>Panel>btn_close>img"}

    class RankPanel:
        RankPanel = {"locator": "UICanvas>Default>RankPanel"}
        btn_close = {"locator": "UICanvas>Default>RankPanel>panel>btn_close>img"}
        fisheries_viewport = {"locator": "UICanvas>Default>RankPanel>panel>FisheriesList>Viewport", "focus": (0, 0)}
        fisheries_list = {"locator": "UICanvas>Default>RankPanel>panel>FisheriesList>Viewport>Content>>bg>img"}
        tab_area_list = {"locator": "UICanvas>Default>RankPanel>panel>panel_right>tab_top>view_port>content>>bg"}
        tab_time_list = {"locator": "UICanvas>Default>RankPanel>panel>panel_right>tab>>text"}
        photo_list = {"locator": "UICanvas>Default>RankPanel>panel>panel_right>FishCardList>Viewport>content>"}
        photo_viewport = {"locator": "UICanvas>Default>RankPanel>panel>panel_right>FishCardList>Viewport"}
        time = {"locator": "UICanvas>Default>RankPanel>panel>panel_right>time"}

    class RankFishLeaderboardPanel:
        RankFishLeaderboardPanel = {"locator": "UICanvas>Default>RankFishLeaderboardPanel"}
        btn_close = {"locator": "UICanvas>Default>RankFishLeaderboardPanel>panel>btn_close>img"}
        btn_like = {"locator": "UICanvas>Default>RankFishLeaderboardPanel>panel>btn_like"}
        like_value = {"locator": "UICanvas>Default>RankFishLeaderboardPanel>panel>like>value"}
        points = {"locator": "UICanvas>Default>RankFishLeaderboardPanel>panel>photo>points"}
        photo = {"locator": "UICanvas>Default>RankFishLeaderboardPanel>panel>photo"}
        rank_list = {"locator": "UICanvas>Default>RankFishLeaderboardPanel>panel>rigth_ranking>Viewport>Content>"}

    class RankFishSettleResultPanel:
        RankFishSettleResultPanel = {"locator": "UICanvas>Default>RankFishSettleResultPanel"}
        btn_close = {"locator": "UICanvas>Default>RankFishSettleResultPanel>panel>btn_close>img"}

    class Recharge1And1Panel:
        Recharge1And1Panel = {"locator": "UICanvas>Default>Recharge1And1Panel"}
        btn_close = {"locator": "UICanvas>Default>Recharge1And1Panel>panel_events_1and1>btn_close>img"}
        icon_list = {"locator": "UICanvas>Default>Recharge1And1Panel>panel_events_1and1>panel>>item_list>>icon"}
        btn_buy = {"locator": "UICanvas>Default>Recharge1And1Panel>panel_events_1and1>panel>pearls_higher>btn_buy", "focus": (0, 0.5)}

    class RechargeBlack5Panel:
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

    class RechargeEndlessPanel:
        item_model_list = {"locator": "UICanvas>Default>>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)"}
        icon_main_list = {"locator": "UICanvas>Default>>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>item_free>group>icon"}
        quantity_main_list = {"locator": "UICanvas>Default>>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>item_free>group>icon>quantity>value"}
        icon_sub_list = {"locator": "UICanvas>Default>>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>group>item_list>item_model_mini(Clone)>icon"}
        quantity_sub_list = {"locator": "UICanvas>Default>>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>group>item_list>item_model_mini(Clone)>quantity>value"}
        btn_buy_list = {"locator": "UICanvas>Default>>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>btn"}

    class RechargeEndlessNewYearPanel:
        RechargeEndlessNewYearPanel = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel"}
        btn_close = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>btn_close>img"}
        item_model_list = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)"}
        icon_main_list = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>item_free>group>icon"}
        quantity_main_list = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>item_free>group>icon>quantity>value"}
        icon_sub_list = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>group>item_list>item_model_mini(Clone)>icon"}
        quantity_sub_list = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>group>item_list>item_model_mini(Clone)>quantity>value"}
        btn_buy_list = {"locator": "UICanvas>Default>RechargeEndlessNewYearPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>btn"}

    class RechargeEndlessThanksPanel:
        RechargeEndlessThanksPanel = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel"}
        btn_close = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>btn_close>img"}
        item_model_list = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)"}
        icon_main_list = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>item_free>group>icon"}
        quantity_main_list = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>item_free>group>icon>quantity>value"}
        icon_sub_list = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>group>item_list>item_model_mini(Clone)>icon"}
        quantity_sub_list = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>group>item_list>item_model_mini(Clone)>quantity>value"}
        btn_buy_list = {"locator": "UICanvas>Default>RechargeEndlessThanksPanel>panel>panel_info>panel_list>Viewport>content>itemModel(Clone)>>btn"}

    class ResultPanel:
        ResultPanel = {"locator": "UICanvas>Default>ResultPanel"}
        btn_claim = {"locator": "UICanvas>Default>ResultPanel>panel_result>>btn_castAgain>text"}
        btn_claim_token_fish = {"locator":"UICanvas>Default>ResultPanel>panel_result_sundries>token_fish>btn_cast>text"}
        exp = {"locator": "UICanvas>Default>ResultPanel>panel_result>rewards>exp>value"}
        class panel_pve_result:
            panel_pve_result = {"locator": "UICanvas>Default>ResultPanel>panel_pve_result"}
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

    class RewardsPanel:
        RewardsPanel = {"locator": "UICanvas>Default>RewardsPanel"}
        tap_to_claim = {"locator": "UICanvas>Default>RewardsPanel>panel>text", "focus": (1, 0.5)}
        reward_icon_list = {"locator": "UICanvas>Default>RewardsPanel>panel>rewards_list>Viewport>Content>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>RewardsPanel>panel>rewards_list>Viewport>Content>>quantity>value"}

    class RewardsPreviewPanel:
        RewardsPreviewPanel = {"locator": "UICanvas>Default>RewardsPreviewPanel"}
        reward_icon_list = {"locator": "UICanvas>Default>RewardsPreviewPanel>panel>Content>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>RewardsPreviewPanel>panel>Content>>quantity>value"}

    class RodMoreToOnePanel:
        RodMoreToOnePanel = {"locator": "UICanvas>Default>RodMoreToOnePanel"}
        icon_list = {"locator": "UICanvas>Default>RodMoreToOnePanel>list>Viewport>Content>>model>icon"}
        tipsBtn_list = {"locator": "UICanvas>Default>RodMoreToOnePanel>list>Viewport>Content>>tipsBtn"}
        btn_close = {"locator": "UICanvas>Default>RodMoreToOnePanel>btn_close>img"}
        btn_confirm = {"locator": "UICanvas>Default>RodMoreToOnePanel>btn>btn_normal"}

    class RodSkinGiftPack027Panel:
        RodSkinGiftPack027Panel = {"locator": "UICanvas>Default>RodSkinGiftPack027Panel"}
        btn_close = {"locator": "UICanvas>Default>RodSkinGiftPack027Panel>btn_close>img"}

    class RodSkinGiftPack030Panel:
        RodSkinGiftPack030Panel = {"locator": "UICanvas>Default>RodSkinGiftPack030Panel"}
        btn_close = {"locator": "UICanvas>Default>RodSkinGiftPack030Panel>btn_close>img"}

    class RookiePanel:
        RookiePanel = {"locator": "UICanvas>Default>RookiePanel"}
        btn_close = {"locator": "UICanvas>Default>RookiePanel>panel_result>btn_close>btn_normal"}

    class RoulettePanel:
        RoulettePanel = {"locator": "UICanvas>Default>RoulettePanel"}
        btn_close = {"locator": "UICanvas>Default>RoulettePanel>Panel>btn_close>img"}
        btn_i = {"locator": "UICanvas>Default>RoulettePanel>Panel>level>btn_i>img"}
        btn_spin = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>btn_spin", "focus":(0.5, 1)}
        cost = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>btn_spin>cost>value"}
        ticket_count = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>quantity>Text"}
        item_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>turntable>turntable_1>"}
        turntable_lv = {"locator": "UICanvas>Default>RoulettePanel>Panel>level>turntable_lv>value"}
        level_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>level>level>"}
        turntable_icon_list =  {"locator":"UICanvas>Default>RoulettePanel>Panel>turntable>turntable_1>>icon"}
        reward_icon_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>reward>reward>List>Viewport>Content>>icon"}
        reward_quantity_list = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>reward>reward>List>Viewport>Content>>value"}
        btn_announcement = {"locator": "UICanvas>Default>RoulettePanel>Panel>panel_right>btn_announcement"}

    class SharePanel:
        SharePanel = {"locator": "UICanvas>Default>SharePanel"}
        btn_close = {"locator": "UICanvas>Default>SharePanel>panel_share_preview>btn_close>img"}
        btn_share = {"locator": "UICanvas>Default>SharePanel>panel_share_preview>btns>btn_share>btn_normal"}

    class StorePanel:
        StorePanel = {"locator": "UICanvas>Default>StorePanel"}
        viewport_tab = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab>content>TabList>Viewport", "focus":(0, 0)}
        tab_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab>content>TabList>Viewport>Content>", "focus":(0, 0.5)}
        panel_gift_pack = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1"}
        panel_resource = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2"}
        panel_cash = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3"}
        panel_box = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4"}

        btn_close = {"locator": "UICanvas>Default>StorePanel>Panel>btn_close>img"}
        # time = {"locator": "UICanvas>Default>TreasureChestMerchantPanel>Panel>time>text"}
        ResourceBar = {"locator": "UICanvas>Default>StorePanel>top_res>ResourceBar"}
        text_100100 = {"locator": "UICanvas>Default>StorePanel>top_res>ResourceBar>100100>value"}
        text_100000= {"locator": "UICanvas>Default>StorePanel>top_res>ResourceBar>100000>value"}
        # btn_add
        btn_add_100100 = {"locator": "UICanvas>Default>StorePanel>top_res>ResourceBar>100100>btn_add>btn_normal"}
        btn_add_100000 = {"locator": "UICanvas>Default>StorePanel>top_res>ResourceBar>100000>btn_add>btn_normal"}



        class GiftPack:
            gift_pack_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1>panel_list_pack>view_port>content>"}
            icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1>panel_list_pack>view_port>content>>group>item_list>>icon"}
            viewport = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_1>panel_list_pack>view_port"}

        class Resource:
            resource_tab_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_subtab>subtab>view_port>content>"}
            item_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show"}
            gear_card_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list>group_gear>>card"}
            gear_name_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list>group_gear>>card>title_bg>title"}
            btn_info = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>btn_info"}
            fish_card_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list>group_cardpacks>>icon>Panel_CardPacks(Clone)>fisheries_bg"}
            fish_card_name_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list>group_cardpacks>>icon>Panel_CardPacks(Clone)>fisheries_bg>name"}
            fish_card_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list>group_cardpacks>>icon>Panel_CardPacks(Clone)>quantity>value"}
            fish_card_main_name = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_cardpacks>Panel_CardPacks(Clone)>fisheries_bg>name"}
            booster_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list_type2>view_port>content>>group>icon_list>>icon"}
            materials_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>panel_list>group_item>>icon", "focus":(0.5, 1)}
            btn_purchase = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>btn_buy>btn_normal"}
            item_icon = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>img"}
            item_quantity = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>quantity>value"}
            cost_icon = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>cost_detail>icon"}
            cost_quantity = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>cost_detail>value"}
            btn_add = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>btn_add"}
            btn_sub = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>btn_sub"}
            btn_max = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>btn_max"}
            btn_min = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>btn_min"}
            slider = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_2>show>icon_item>cost>slider"}

        class Box:
            btn_refresh_text = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>tips>btn_refresh>text"}
            btn_refresh_value = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>tips>soldout>text"}
            times_refresh = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>tips>refresh>text"}
            quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>quantity>value"}
            btn_buy_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>btn_buy>text"}
            btn_disabled_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>btn_disabled>text"}
            box_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>>group>icon_box"}
            item_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_4>panel_list_type2>view_port>content>"}


        class Cash:
            cash_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3>content>"}
            cash_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3>content>>group>icon"}
            cash_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_3>content>>group>quantity>value"}

        class Coupons:
            coupons_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_13>panel_list>"}
            coupons_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_13>panel_list>>icon"}
            coupons_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_13>panel_list>>price>text"}

        class MonthCard:
            month_model_1 = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_01>content>"}
            month_card_1_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_01>content>month_model_1>group_rewards>>item_icon>item_model_mini(Clone)>icon"}
            month_card_1_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_01>content>month_model_1>group_rewards>>item_icon>item_model_mini(Clone)>quantity>value"}
            month_card_1_quantity_total = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_01>content>month_model_1>value>text"}
            month_model_2_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_02>content>"}
            month_card_2_icon_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_02>content>>group_rewards>>item_icon>item_model_mini(Clone)>icon"}
            month_card_2_quantity_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_02>content>>group_rewards>>item_icon>item_model_mini(Clone)>quantity>value"}
            month_card_2_quantity_total_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_02>content>>value>text"}
            month_card_2_item_model_list = {"locator": "UICanvas>Default>StorePanel>Panel>panel_tab_7>panel_month_02>content>>group_rewards>>item_icon>item_model_mini(Clone)"}

    class StoreSuitPopupPanel:
        StoreSuitPopupPanel = {"locator": "UICanvas>Default>StoreSuitPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>StoreSuitPopupPanel>panel>btn_close>img"}

    class StoreChristmasPopupPanel:
        StoreChristmasPopupPanel = {"locator": "UICanvas>Default>StoreChristmasPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>StoreChristmasPopupPanel>Panel>btn_close>img"}

    class TaskFishingCareerPanel:
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

    class TaskPanel:
        TaskPanel = {"locator": "UICanvas>Default>TaskPanel"}
        btn_close = {"locator": "UICanvas>Default>TaskPanel>panel>btn_close>img"}
        # 侧边栏
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

        task_award_quantity_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>>item_model_new>quantity"}
        task_award_icon_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>>item_model_new>icon"}
        progress_value = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg"}
        box_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>"}
        month_box_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>icon1"}
        text_list = {"locator": "UICanvas>Default>TaskPanel>panel>>ranking_list>view_port>content>>Image>text"}
        award_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>award"}
        ing_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>ing"}
        done_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>done"}
        award_detail = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>detialObj>detail"}
        award_quantity_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>detialObj>detail>>quantity>value"}
        award_icon_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>progress_bg>>detialObj>detail>>icon"}
        month_award_detail = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>icon1>detialObj>detail"}
        month_award_quantity_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>icon1>detialObj>detail>>quantity>value"}
        month_award_icon_list = {"locator": "UICanvas>Default>TaskPanel>panel>>banner>progress>item>icon1>detialObj>detail>>icon"}

    class TournamentsPanel:
        TournamentsPanel = {"locator": "UICanvas>Default>TournamentsPanel"}
        btn_close = {"locator": "UICanvas>Default>TournamentsPanel>panel>btn_close>img"}
        btn_enter_list_multi = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>btn_players>btn_players>text"}
        btn_enter_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>btn_enter>text"}
        time_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>tournaments_info>time>text"}
        bg_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>bg"}
        model_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model"}
        entrance_viewport = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport", "focus": (0, 0)}
        btn_leaderboard = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_leaderboard", "focus":(1, 0.5)}
        btn_turntable = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_turntable>btn_normal"}
        panel_sidebar_bg = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_division_sidebar>panel_sidebar>panel_bg"}
        tournaments_info_list = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_entrance>List>Viewport>Content>>model>tournaments_info>logo"}
        btn_flashcard_banner = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_flashcard_banner"}
        btn_magnifier = {"locator": "UICanvas>Default>TournamentsPanel>panel>panel_division_sidebar>panel_sidebar>panel_detail>btn_flashcard_banner>panel_name>btn_magnifier>icon"}

    class TournamentsInfoPanel:
        TournamentsInfoPanel = {"locator": "UICanvas>Default>TournamentsInfoPanel"}
        btn_close = {"locator": "UICanvas>Default>TournamentsInfoPanel>panel>btn_close>img"}
        tab_list = {"locator": "UICanvas>Default>TournamentsInfoPanel>panel>panel_tab_list>panel_tab>TabList>Viewport>Content>>bg"}
        check = {"locator": "UICanvas>Default>TournamentsInfoPanel>panel>panel_rules>rules_2>progress_info>reward>item_model_mini>collected>check"}
        progress_cur = {"locator": "UICanvas>Default>TournamentsInfoPanel>panel>panel_rules>rules_2>progress_info>progressValueLayout>cur"}
        progress_max = {"locator": "UICanvas>Default>TournamentsInfoPanel>panel>panel_rules>rules_2>progress_info>progressValueLayout>max"}

    class TreasureChestGearsShardsPanel:
        TreasureChestGearsShardsPanel = {"locator": "UICanvas>Default>TreasureChestGearsShardsPanel"}
        btn_close = {"locator": "UICanvas>Default>TreasureChestGearsShardsPanel>btn_close>text"}
        btn_enhance_list = {"locator": "UICanvas>Default>TreasureChestGearsShardsPanel>rewards_list>Viewport>Content>>btn_enhance", "focus":(0.5, 1)}

    # 宝箱
    class TreasureChestPanel:
        TreasureChestPanel = {"locator": "UICanvas>Default>TreasureChestPanel"}
        btn_close = {"locator": "UICanvas>Default>TreasureChestPanel>panel>btn_close>img"}
        box_list = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>select>>box"}
        quantity_list = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>select>>quantity>value"}
        box = {"locator": "HomeCanvas>Home3DPanel>panel>chest>"}
        btn_open = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>btn_open>text"}
        box_points = {"locator": "UICanvas>Default>TreasureChestPanel>panel>panel_left>content>progressbar>progressbar_bg>progressbarbar_text_bg>text"}
        progressbar_box = {"locator": "UICanvas>Default>TreasureChestPanel>panel>panel_left>content>progressbar>progressbar_bg>box"}
        btn_buy = {"locator": "UICanvas>Default>TreasureChestPanel>panel>panel_left>content>merchant>btn_buy>btn_normal"}
        btn_magnifier = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>items_bg>btn_magnifier>icon"}
        tips = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>tips"}
        preview_icon_list = {"locator": "UICanvas>Default>TreasureChestPanel>panel>ChestInfo>items_bg>items>>icon"}



    class TreasureChestRewardsPanel:
        TreasureChestRewardsPanel = {"locator": "UICanvas>Default>TreasureChestRewardsPanel"}
        btn_close = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>btn>btn_receive>btn_normal"}
        item_icon_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>item_model_new(Clone)>icon"}
        item_quantity_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>item_model_new(Clone)>quantity>value"}
        gear_icon_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>gear_model_new(Clone)>icon"}
        gear_location_icon_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>gear_model_new(Clone)>kinds>icon"}
        gear_rarity_list = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>list>item_mask>item_list>>gear_model_new(Clone)>bg"}
        btn_open = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>btn>btn_open>text"}
        btn_disabled = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>btn>btn_open>btn_disabled"}
        box_fragment = {"locator": "UICanvas>Default>TreasureChestRewardsPanel>panel>box_fragment"}

    class WaitHintPanel:
        WaitHintPanel = {"locator": "UICanvas>Default>WaitHintPanel"}
































