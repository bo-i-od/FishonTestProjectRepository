from poco.utils.simplerpc.utils import sync_wrapper


@sync_wrapper
def my_print(poco):
    # request = {
    #     "jsonrpc": "2.0",
    #     "id": "1",
    #     "method": "MyPrint",
    #     "params": {
    #         "data": "Hello, PocoManager!"
    #     }
    # }
    #
    # # 将请求消息转换为JSON字符串
    # request_json = json.dumps(request)
    # request_json.encode()
    # 发送请求消息
    param0 = "aaa"
    param1 = 123
    param2 = [123, "45", True]
    param3 = 0.6
    param4 = True
    return poco.agent.c.call("MyPrint", param0, param1, param2, param3, param4)


@sync_wrapper
def set_text(poco, element, text):
    return poco.agent.c.call("SetText", element, text)


@sync_wrapper
def set_text_by_id(poco, id_list, offspring_path, text):
    return poco.agent.c.call("SetTextById", id_list, offspring_path, text)


@sync_wrapper
def get_text(poco, element):
    return poco.agent.c.call("GetText", element)


@sync_wrapper
def get_text_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetTextById", id_list, offspring_path)


@sync_wrapper
def get_slider_value(poco, element):
    return poco.agent.c.call("GetSliderValue", element)


@sync_wrapper
def get_slider_value_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetSliderValueById", id_list, offspring_path)


@sync_wrapper
def get_img_name(poco, element):
    return poco.agent.c.call("GetImgName", element)


@sync_wrapper
def get_img_name_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetImgNameById", id_list, offspring_path)


@sync_wrapper
def get_name(poco, element):
    return poco.agent.c.call("GetName", element)


@sync_wrapper
def get_name_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetNameById", id_list, offspring_path)


@sync_wrapper
def get_position(poco, element):
    return poco.agent.c.call("GetPosition", element)


@sync_wrapper
def get_position_by_id(poco, id_list, offspring_path, camera_name):
    return poco.agent.c.call("GetPositionById", id_list, offspring_path, camera_name)


@sync_wrapper
def get_size(poco, element):
    return poco.agent.c.call("GetSize", element)


@sync_wrapper
def get_size_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetSizeById", id_list, offspring_path)


@sync_wrapper
def get_object_id(poco, element):
    return poco.agent.c.call("GetObjectId", element)


@sync_wrapper
def get_offspring_id_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetOffspringIdById", id_list, offspring_path)


@sync_wrapper
def get_parent_id(poco, element):
    return poco.agent.c.call("GetParentId", element)


@sync_wrapper
def get_parent_id_by_id(poco, id_list, offspring_path):
    return poco.agent.c.call("GetParentIdById", id_list, offspring_path)


@sync_wrapper
def get_item_count(poco, tpid_list):
    return poco.agent.c.call("GetItemCount", tpid_list)


@sync_wrapper
def get_toggle_is_on(poco, element):
    return poco.agent.c.call("GetToggleIsOn", element)


@sync_wrapper
def get_toggle_is_on_by_id(poco, tpid_list, offspring_path):
    return poco.agent.c.call("GetToggleIsOnById", tpid_list, offspring_path)


@sync_wrapper
def screen_shot(poco, ui_x, ui_y, ui_w, ui_h):
    return poco.agent.c.call("Screenshot", ui_x, ui_y, ui_w, ui_h)


@sync_wrapper
def get_dropdown_value(poco, element):
    return poco.agent.c.call("GetDropdownValue", element)

@sync_wrapper
def set_dropdown_value(poco, element, index):
    return poco.agent.c.call("SetDropdownValue", element, index)

@sync_wrapper
def cmd(poco, command_list):
    return poco.agent.c.call("CMD", command_list)

@sync_wrapper
def lua_console(poco, command_list):
    return poco.agent.c.call("LuaConsole", command_list)

@sync_wrapper
def custom_cmd(poco, command_list):
    return poco.agent.c.call("CustomCMD", command_list)

@sync_wrapper
def set_btn_enabled(poco, element, enabled):
    return poco.agent.c.call("SetBtnEnabled", element, enabled)

@sync_wrapper
def set_object_active(poco, element, active):
    return poco.agent.c.call("SetObjectActive", element, active)

@sync_wrapper
def set_object_active_by_id(poco, id_list, offspring_path, active):
    return poco.agent.c.call("SetObjectActiveById", id_list, offspring_path, active)

@sync_wrapper
def click_button(poco, element):
    return poco.agent.c.call("ClickButton", element)

@sync_wrapper
def ray_input(poco, element, kind):
    return poco.agent.c.call("RayInput", element, kind)

@sync_wrapper
def ray_input_by_id(poco, id_list, offspring_path, kind):
    return poco.agent.c.call("RayInputById", id_list, offspring_path, kind)

@sync_wrapper
def set_time_scale(poco, time_scale):
    return poco.agent.c.call("SetTimeScale", time_scale)

@sync_wrapper
def fish(poco, execute_list):
    return poco.agent.c.call("Fish", execute_list)

@sync_wrapper
def get_scene_list(poco):
    return poco.agent.c.call("GetSceneList")

@sync_wrapper
def set_send_log_flag(poco, send_log_flag):
    return poco.agent.c.call("SetSendLogFlag", send_log_flag)



