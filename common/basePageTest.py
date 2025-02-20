from common.basePage import BasePageMain, BasePage
from common.slider import Slider
from common.viewport import Viewport
from configs.elementsData import ElementsData

element_data = {
    "panel": {"locator": "Canvas>Panel"},
    "button_list": {"locator": "UICanvas>Default>RankPanel>panel>panel_right>tab>mouth"},
    "slider": {"locator": "UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options_music>slider"},
    "slider_wrong": {"locator": "Canvas>Panel>S"},
    "toggle_list": {"locator": "Canvas>Panel>ToggleGroup>"},
    "dropdown": {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown"},
    "input_field": {"locator": "UICanvas>Default>LoginPanel>panel_internal>InputField_UserName"},
    "viewport": { "locator":"UICanvas>Default>FishCardPanel>panel_normal>content>FishCardList>Viewport"},
    "tab_list": {"locator": "Canvas>Panel>Scroll View>Viewport>Content>"},
    "btn_login": {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login"},
    "btn_normal": {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login>btn_normal"},
    "btn_text": {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login>text"},
    "text_list": {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>>Item Label"},
    "icon_list": {"locator": "UICanvas>Default>HomePanel>panel>panel_giftpack>list>Viewport>Content>>img"},
    "FishCardList":{"locator":"UICanvas>Default>FishCardPanel>panel_normal>content>FishCardList>Viewport>content>>"}
}

def get_device_unity_test(bp: BasePage):
    device = bp.get_device()
    print(device)

def get_device_mobile_test(bp: BasePage):
    device = bp.get_device(serial_number="127.0.0.1:21503")
    print(device)

def connect_close_test(bp: BasePage):
    bp.connect_close()


def debug_log_true_test(bp: BasePage):
    bp.is_debug_log = True
    bp.debug_log('true')

def debug_log_false_test(bp: BasePage):
    bp.is_debug_log = False
    bp.debug_log('false')


def is_single_element_0_test(bp: BasePage):
    element_data = []
    bp.is_single_element(element_data)

def is_single_element_1_test(bp: BasePage):
    element_data = [1]

    bp.is_single_element(element_data)

def is_single_element_2_test(bp: BasePage):
    element_data = [1,2]

    bp.is_single_element(element_data)

def get_element_data_test(bp: BasePage):
    element_data = ElementsData.BattlePanel.BattlePanel
    offspring_path = 'test'
    element_data_copy = bp.get_element_data(element_data,offspring_path)
    print(element_data_copy)

def get_element_data_list_test(bp: BasePage):
    element_data_list =[ElementsData.BattlePanel.BattlePanel,ElementsData.BattlePanel.hud_power_list]
    offspring_path = 'test'
    element_data_list = bp.get_element_data_list(element_data_list,offspring_path)
    print(element_data_list)

def exist_true_test(bp: BasePageMain):
    # 输入存在的定位信息返回True
    result = bp.exist(element_data=ElementsData.LoginPanel.btn_login)
    print(result)

def exist_false_test(bp: BasePageMain):
    # 输入不存在的定位信息返回False
    result = bp.exist(element_data=ElementsData.BattlePanel.BattlePanel)
    print(result)

def get_object_id_list_test(bp: BasePageMain):
    element_data = ElementsData.LoginPanel.btn_login
    object_id_list = bp.get_object_id_list(element_data=element_data)
    print(object_id_list)

def get_object_id_list_list_test(bp: BasePageMain):
    element_data_list = [ElementsData.LoginPanel.LoginPanel,ElementsData.LoginPanel.btn_login, {"locator":"UICanvas>Default>LoginPanel>panel_internal>Dropdown>Dropdown List>Viewport>Content>"}]
    object_id_list = bp.get_object_id_list(element_data_list=element_data_list)
    print(object_id_list)


def get_object_id_test(bp: BasePageMain):
    # get_object_id只能获取元素对应有且仅有一个的物体，否则会报错

    # 定位元素对应单一物体
    result = bp.get_object_id(element_data=ElementsData.LoginPanel.btn_login)
    print(result)


def get_offspring_id_list_test(bp: BasePageMain):
    # # 等价于带offspring_path参数的get_object_id_list
    # result = bp.get_offspring_id_list(element_data=element_data["button_list"], offspring_path="Text (Legacy)")
    # print(result)
    #
    # # 等价于带offspring_path参数的get_object_id_list
    # result = bp.get_offspring_id_list(element_data_list=[element_data["button_list"], element_data["text_list"], element_data["slider"]], offspring_path="Text (Legacy)")
    # print(result)

    # 取得第一个button的Instance ID后，获取偏移的Instance ID
    object_id_list = bp.get_object_id_list(element_data=element_data["btn_login"])
    object_id = object_id_list[0]
    result = bp.get_offspring_id_list(object_id=object_id, offspring_path="btn_normal")
    print(result)

    # # 取得全部button的Instance ID后，获取偏移的Instance ID
    # result = bp.get_offspring_id_list(object_id_list=object_id_list, offspring_path="Text (Legacy)")
    # print(result)


def get_offspring_id_test(bp: BasePageMain):
    # 都等同于bp.get_object_id(element_data=element_data["slider"])
    result = bp.get_offspring_id(element_data=element_data["panel"], offspring_path="Slider")
    print(result)

    object_id = bp.get_object_id(element_data=element_data["panel"])
    result = bp.get_offspring_id(object_id=object_id, offspring_path="Slider")
    print(result)


def get_parent_id_list_test(bp: BasePageMain):
    # 等同于bp.get_object_id_list(element_data=element_data["panel"])
    result = bp.get_parent_id_list(element_data=element_data["btn_login"], offspring_path="btn_normal")
    print(result)


def get_text_list_test(bp: BasePageMain):
    result = bp.get_text_list(element_data=element_data["btn_text"])
    print(result)

    object_id_list = bp.get_object_id_list(element_data=element_data["text_list"])
    result = bp.get_text_list(object_id_list=object_id_list)
    print(result)


def set_text_list_test(bp: BasePageMain):
    bp.set_text_list(element_data=element_data["input_field"], text="123456")

    object_id_list = bp.get_object_id_list(element_data=element_data["text_list"])
    print(object_id_list)
    bp.set_text_list(object_id_list=object_id_list, text="456")


def get_icon_list_test(bp: BasePageMain):
    result = bp.get_icon_list(element_data=element_data["button_list"])
    print(result)

    result = bp.get_icon_list(element_data_list=[element_data["icon_list"], element_data["button_list"]])
    print(result)

def get_name_list_test(bp: BasePageMain):
    result = bp.get_name_list(element_data=element_data["button_list"])
    print(result)


def get_slider_value_list_test(bp: BasePageMain):
    result = bp.get_slider_value(element_data=element_data["slider"])
    print(result)


def get_dropdown_value_list_test(bp: BasePageMain):
    result = bp.get_dropdown_value(element_data=element_data["dropdown"])
    print(result)


def get_size_list_test(bp: BasePageMain):
    result = bp.get_size_list(element_data=element_data["dropdown"])
    print(result)


def get_toggle_is_on_list_test(bp: BasePageMain):
    result = bp.get_toggle_is_on_list(element_data=element_data["toggle_list"])
    print(result)


def get_position_list_test(bp: BasePageMain):
    result = bp.get_position_list(element_data=element_data["button_list"])
    print(result)

def press_test(bp: BasePageMain):
    bp.press(element_data=ElementsData.RoulettePanel.btn_spin)

def click_position_base_test(bp: BasePageMain):
    position =bp.get_position(element_data=ElementsData.RoulettePanel.btn_spin)
    bp.click_position(position=position)

def click_position_test(bp: BasePageMain):
    # position = bp.get_position(element_data=ElementsData.HomePanel.btn_aquarium)
    bp.click_position(position=[0.5,0.5])

def click_object_of_plural_objects_test(bp: BasePageMain):

    bp.click_object_of_plural_objects(element_data=element_data['FishCardList'],element_viewport=element_data["viewport"],index=-1)

def click_a_until_b_appear_list_test(bp:BasePageMain):
    perform_list=[
        {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_fishcard"},
        {"locator": "UICanvas>Default>FishCardPanel>btn_close>img"},
        {"locator": "UICanvas>Default>HomePanel>panel>navbar>btns>btn_fishcard"},
    ]
    bp.click_a_until_b_appear_list(perform_list=perform_list)

def clear_popup_once_test(bp:BasePageMain):
    bp.clear_popup_once()

def clear_popup_once_ignore_test(bp:BasePageMain):
    bp.clear_popup_once(ignore_set={"PlayerLevelupPanel"})

def go_home_test(bp:BasePageMain):
    bp.go_home(target_panel="TournamentsPanel")

def go_to_panel_test(bp:BasePageMain):

    bp.go_to_panel("AquariumMainPanel")

def swipe_test(bp:BasePageMain):
    position_list = bp.get_position_list(element_data={"locator":"UICanvas>Default>FishCardPanel>panel_tab>content>TabList>Viewport>Content>tab_model(Clone)","focus":(0.2,0.5)})

    bp.swipe(point_start=position_list[5],point_end=position_list[0])

def swipe_slider_base_test(bp:BasePageMain):
    slider = {"locator":"UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_setting>Scroll View>Viewport>Content>options_music>slider"}
    slider = Slider(bp,slider)
    bp.swipe_slider_base(value_start=0.3,value_end=0.8,slider=slider)

def get_screen_shot_test(bp:BasePage):
    img=bp.get_screen_shot(500,500,300,400)
    bp.save_img(img=img)

def get_element_shot_test(bp:BasePageMain):
    img = bp.get_element_shot(element_data=ElementsData.PlayerInfoPanel.tab_avatar)
    bp.save_img(img=img)
#     {"locator":"UICanvas>Default>PlayerInfoPanel>Panel_Popups_Edit>Panel>panel_tab>TabList>Viewport>Content>tab_1>bg","focus":(0.5,0.5)}

def ray_input_test(bp:BasePageMain):
    bp.ray_input(element_data={"locator":"UICanvas>Default>HomePanel>panel>panel_left>btn_chat>chat_model(Clone)>btn_chat"},kind="click")

def set_time_scale_test(bp:BasePageMain):
    bp.set_time_scale(time_scale=3)

def get_target_log_test(bp:BasePageMain):
    bp.sleep(20)
    target_log = bp.get_target_log("SCFishingCastMsg")
    print(target_log)

def receive_until_get_msg_test(bp:BasePageMain):
    target_log = bp.receive_until_get_msg(msg_name='FishingCastMsg')
    # print(target_log)


if __name__ == '__main__':
    base_page = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21503")
    # get_device_unity_test(base_page)

    # get_device_mobile_test(base_page)

    # exist_true_test(bp=base_page)
    #
   #exist_false_test(bp=base_page)
    # get_object_id_list_test(bp=base_page)
    #
    # get_object_id_list_list_test(bp=base_page)
    # get_object_id_test(bp=base_page)
    #
    # get_offspring_id_list_test(bp=base_page)
    #
    # get_offspring_id_test(bp=base_page)
    #
    # get_parent_id_list_test(bp=base_page)
    #
    # get_text_list_test(bp=base_page)
    #
    # set_text_list_test(bp=base_page)
    #
    # get_icon_list_test(bp=base_page)
    #
    # get_name_list_test(bp=base_page)
    #
    # get_slider_value_list_test(bp=base_page)
    #
    # get_dropdown_value_list_test(bp=base_page)
    #
    # get_size_list_test(bp=base_page)
    #
    # get_toggle_is_on_list_test(bp=base_page)
    #
    # get_position_list_test(bp=base_page)

    # connect_close_test(bp=base_page)
    # debug_log_true_test(bp=base_page)

    # debug_log_false_test(bp=base_page)

    # is_single_element_0_test(bp=base_page)
    # is_single_element_1_test(bp=base_page)
    # is_single_element_2_test(bp=base_page)
    #get_element_data_test(bp=base_page)
    # get_element_data_list_test(bp=base_page)

    # press_test(bp=base_page)
    # click_position_base_test(bp=base_page)
    # click_position_test(bp=base_page)
    # click_object_of_plural_objects_test(bp=base_page)
    # click_a_until_b_appear_list_test(bp=base_page)
    # clear_popup_once_ignore_test(bp=base_page)
    # go_home_test(bp=base_page)
    # go_to_panel_test(
    #     bp=base_page
    # )
    # swipe_test(bp=base_page)
    # swipe_slider_base_test(bp=base_page)
    # get_screen_shot_test(bp=base_page)
    # get_element_shot_test(bp=base_page)
    # ray_input_test(bp=base_page)
    # base_page.is_time_scale=True
    # set_time_scale_test(bp=base_page)
    # get_target_log_test(bp=base_page)
    receive_until_get_msg_test(bp=base_page)
    base_page.connect_close()









