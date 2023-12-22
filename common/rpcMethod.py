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
def set_text_by_id(poco, id, text):
    return poco.agent.c.call("SetTextById", id, text)


@sync_wrapper
def get_text(poco, element):
    return poco.agent.c.call("GetText", element)


@sync_wrapper
def get_text_by_id(poco, id):
    return poco.agent.c.call("GetTextById", id)


@sync_wrapper
def get_slider_value(poco, element):
    return poco.agent.c.call("GetSliderValue", element)


@sync_wrapper
def get_slider_value_by_id(poco, id):
    return poco.agent.c.call("GetSliderValueById", id)


@sync_wrapper
def get_img_name(poco, element):
    return poco.agent.c.call("GetImgName", element)


@sync_wrapper
def get_img_name_by_id(poco, id):
    return poco.agent.c.call("GetImgNameById", id)


@sync_wrapper
def get_name(poco, element):
    return poco.agent.c.call("GetName", element)


@sync_wrapper
def get_name_by_id(poco, id):
    return poco.agent.c.call("GetNameById", id)


@sync_wrapper
def get_position(poco, element):
    return poco.agent.c.call("GetPosition", element)


@sync_wrapper
def get_position_by_id(poco, id):
    return poco.agent.c.call("GetPositionById", id)


@sync_wrapper
def get_size(poco, element):
    return poco.agent.c.call("GetSize", element)


@sync_wrapper
def get_size_by_id(poco, id):
    return poco.agent.c.call("GetSizeById", id)


@sync_wrapper
def get_object_id(poco, element):
    return poco.agent.c.call("GetObjectId", element)


@sync_wrapper
def get_object_id_by_id(poco, id):
    return poco.agent.c.call("GetObjectIdById", id)


@sync_wrapper
def get_child_id(poco, element, child_name):
    return poco.agent.c.call("GetChildId", element, child_name)


@sync_wrapper
def get_child_id_by_id(poco, id, child_name):
    return poco.agent.c.call("GetChildIdById", id, child_name)

# @sync_wrapper
# def get_offspring_id(bp, element, offspring_path):
#     return bp.poco.agent.c.call("GetOffspringId", element, offspring_path)


@sync_wrapper
def get_offspring_id_by_id(poco, id, offspring_path):
    return poco.agent.c.call("GetOffspringIdById", id, offspring_path)

@sync_wrapper
def get_parent_id(poco, element):
    return poco.agent.c.call("GetParentId", element)


@sync_wrapper
def get_parent_id_by_id(poco, id):
    return poco.agent.c.call("GetParentIdById", id)


@sync_wrapper
def get_item_count(poco, tpid):
    return poco.agent.c.call("GetItemCount", tpid)


@sync_wrapper
def get_toggle_is_on(poco, element):
    return poco.agent.c.call("GetToggleIsOn", element)


@sync_wrapper
def get_toggle_is_on_by_id(poco, id):
    return poco.agent.c.call("GetToggleIsOnById", id)

@sync_wrapper
def screen_shot(poco, ui_x, ui_y, ui_w, ui_h):
    return poco.agent.c.call("Screenshot", ui_x, ui_y, ui_w, ui_h)

@sync_wrapper
def get_dropdown_value(poco, element):
    return poco.agent.c.call("GetDropdownValue", element)

def set_dropdown_value(poco, element, index):
    poco.agent.c.call("SetDropdownValue", element, index)


def cmd(poco, command):
    poco.agent.c.call("CMD", command)


def lua_console(poco, command):
    poco.agent.c.call("LuaConsole", command)


def set_btn_enabled(poco, element, enabled):
    poco.agent.c.call("SetBtnEnabled", element, enabled)



