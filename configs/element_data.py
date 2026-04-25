class ElementData:
    class LoginPanel:
        LoginPanel = {"locator": "UICanvas/Default/LoginPanel"}
        btn_login = {'locator': 'UICanvas/Default/LoginPanel/panel_internal/btn_login', 'focus': (0.5, 0.5)}

    class HomePanel:
        HomePanel = {"locator": "UICanvas/Default/HomePanel"}
        player_name = {'locator': 'UICanvas/Default/HomePanel/panel/panel_player_info/player_info/player_name', 'focus': (0.5, 0.5)}
        head_frame_com = {'locator': 'UICanvas/Default/HomePanel/panel/panel_player_info/player_info/head/head_frame/panel/head_frame_com', 'focus': (0.5, 0.5)}

    class Home3DPanel:
        Home3DPanel = {"locator": "HomeCanvas/Home3DPanel"}
        btn_chest = {"locator": "HomeCanvas/Home3DPanel/panel/chest/btn_chest", "locator_camera": "Camera3D"}