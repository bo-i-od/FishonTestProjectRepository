from common.basePage import BasePageMain

element_data = {
    "panel": {"locator": "Canvas>Panel"},
    "button_list": {"locator": "Canvas>Panel>ButtonList>"},
    "text_list": {"locator": "Canvas>Panel>ButtonList>>Text (Legacy)"},
    "slider": {"locator": "Canvas>Panel>Slider"},
    "slider_wrong": {"locator": "Canvas>Panel>S"},
    "toggle_list": {"locator": "Canvas>Panel>ToggleGroup>"},
    "dropdown": {"locator": "Canvas>Panel>Dropdown"},
    "input_field": {"locator": "Canvas>Panel>InputField (TMP)"},
    "viewport": {"locator": "Canvas>Panel>Scroll View>Viewport"},
    "tab_list": {"locator": "Canvas>Panel>Scroll View>Viewport>Content>"},
}


def exist_test(bp: BasePageMain):
    # 输入存在的定位信息返回True
    result = bp.exist(element_data=element_data["slider"])
    print(result)

    # 输入不存在的定位信息返回False
    result = bp.exist(element_data=element_data["slider_wrong"])
    print(result)


def get_object_id_list_test(bp: BasePageMain):
    # 返回两个button的Instance ID组成列表
    result = bp.get_object_id_list(element_data=element_data["button_list"])
    print(result)

    # 两个button的Instance ID组成列表、两个text的Instance ID组成列表、一个slider的Instance ID组成列表
    # 三个列表进一步组成列表
    result = bp.get_object_id_list(element_data_list=[element_data["button_list"], element_data["text_list"], element_data["slider"]])
    print(result)

    # 返回Canvas>Panel>ButtonList>偏移Text (Legacy)的Instance ID组成列表，即Canvas>Panel>ButtonList>>Text (Legacy)的Instance ID组成列表
    result = bp.get_object_id_list(element_data=element_data["button_list"], offspring_path="Text (Legacy)")
    print(result)

    # Canvas>Panel>ButtonList>偏移Text (Legacy)的Instance ID组成列表，即Canvas>Panel>ButtonList>>Text (Legacy)的Instance ID组成列表
    # Canvas>Panel>ButtonList>>Text (Legacy)偏移Text (Legacy)的Instance ID组成列表，即Canvas>Panel>ButtonList>>Text (Legacy)>Text (Legacy)的Instance ID组成列表
    # Canvas>Panel>Slider偏移Text (Legacy)的Instance ID组成列表，即Canvas>Panel>Slider>Text (Legacy)的Instance ID组成列表
    # 后两个路径找不到对应物体因此返回[]
    # 三个列表组成进一步组成列表
    result = bp.get_object_id_list(element_data_list=[element_data["button_list"], element_data["text_list"], element_data["slider"]], offspring_path="Text (Legacy)")
    print(result)


def get_object_id_test(bp: BasePageMain):
    # get_object_id只能获取元素对应有且仅有一个的物体，否则会报错

    # 定位元素对应多个物体
    try:
        result = bp.get_object_id(element_data=element_data["button_list"])
        print(result)
    except Exception as e:
        print(e)

    # 定位元素无对应物体
    try:
        result = bp.get_object_id(element_data=element_data["slider_wrong"])
        print(result)
    except Exception as e:
        print(e)

    # 定位元素对应单一物体
    result = bp.get_object_id(element_data=element_data["slider"])
    print(result)


def get_offspring_id_list_test(bp: BasePageMain):
    # 等价于带offspring_path参数的get_object_id_list
    result = bp.get_offspring_id_list(element_data=element_data["button_list"], offspring_path="Text (Legacy)")
    print(result)

    # 等价于带offspring_path参数的get_object_id_list
    result = bp.get_offspring_id_list(element_data_list=[element_data["button_list"], element_data["text_list"], element_data["slider"]], offspring_path="Text (Legacy)")
    print(result)

    # 取得第一个button的Instance ID后，获取偏移的Instance ID
    object_id_list = bp.get_object_id_list(element_data=element_data["button_list"])
    object_id = object_id_list[0]
    result = bp.get_offspring_id_list(object_id=object_id, offspring_path="Text (Legacy)")
    print(result)

    # 取得全部button的Instance ID后，获取偏移的Instance ID
    result = bp.get_offspring_id_list(object_id_list=object_id_list, offspring_path="Text (Legacy)")
    print(result)


def get_offspring_id_test(bp: BasePageMain):
    # 都等同于bp.get_object_id(element_data=element_data["slider"])
    result = bp.get_offspring_id(element_data=element_data["panel"], offspring_path="Slider")
    print(result)

    object_id = bp.get_object_id(element_data=element_data["panel"])
    result = bp.get_offspring_id(object_id=object_id, offspring_path="Slider")
    print(result)


def get_parent_id_list_test(bp: BasePageMain):
    # 等同于bp.get_object_id_list(element_data=element_data["panel"])
    result = bp.get_parent_id_list(element_data=element_data["panel"], offspring_path="Slider")
    print(result)


def get_text_list_test(bp: BasePageMain):
    result = bp.get_text_list(element_data=element_data["input_field"])
    print(result)

    object_id_list = bp.get_object_id_list(element_data=element_data["text_list"])
    result = bp.get_text_list(object_id_list=object_id_list)
    print(result)


def set_text_list_test(bp: BasePageMain):
    bp.set_text_list(element_data=element_data["input_field"], text="123456")

    object_id_list = bp.get_object_id_list(element_data=element_data["text_list"])
    bp.set_text_list(object_id_list=object_id_list, text="456")


def get_icon_list_test(bp: BasePageMain):
    result = bp.get_icon_list(element_data=element_data["button_list"])
    print(result)


def get_name_list_test(bp: BasePageMain):
    result = bp.get_name_list(element_data=element_data["button_list"])
    print(result)


def get_slider_value_list_test(bp: BasePageMain):
    result = bp.get_name_list(element_data=element_data["slider"])
    print(result)


def get_dropdown_value_list_test(bp: BasePageMain):
    result = bp.get_name_list(element_data=element_data["dropdown"])
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




if __name__ == '__main__':
    base_page = BasePageMain(is_mobile_device=False, serial_number="b6h65hd64p5pxcyh")

    exist_test(bp=base_page)

    # get_object_id_list_test(bp=base_page)
    #
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

    base_page.connect_close()
