from poco.utils.simplerpc.utils import sync_wrapper


@sync_wrapper
def my_print(bp, element):
    return bp.poco.agent.c.call("MyPrint", element)


@sync_wrapper
def set_text(bp, element, text):
    return bp.poco.agent.c.call("SetText", element, text)


@sync_wrapper
def set_text_by_id(bp, id, text):
    return bp.poco.agent.c.call("SetTextById", id, text)


@sync_wrapper
def get_text(bp, element):
    return bp.poco.agent.c.call("GetText", element)


@sync_wrapper
def get_text_by_id(bp, id):
    return bp.poco.agent.c.call("GetTextById", id)


@sync_wrapper
def get_slider_value(bp, element):
    return bp.poco.agent.c.call("GetSliderValue", element)


@sync_wrapper
def get_slider_value_by_id(bp, id):
    return bp.poco.agent.c.call("GetSliderValueById", id)


@sync_wrapper
def get_img_name(bp, element):
    return bp.poco.agent.c.call("GetImgName", element)


@sync_wrapper
def get_img_name_by_id(bp, id):
    return bp.poco.agent.c.call("GetImgNameById", id)


@sync_wrapper
def get_name(bp, element):
    return bp.poco.agent.c.call("GetName", element)


@sync_wrapper
def get_name_by_id(bp, id):
    return bp.poco.agent.c.call("GetNameById", id)


@sync_wrapper
def get_position(bp, element):
    return bp.poco.agent.c.call("GetPosition", element)


@sync_wrapper
def get_position_by_id(bp, id):
    return bp.poco.agent.c.call("GetPositionById", id)


@sync_wrapper
def get_size(bp, element):
    return bp.poco.agent.c.call("GetSize", element)


@sync_wrapper
def get_size_by_id(bp, id):
    return bp.poco.agent.c.call("GetSizeById", id)


@sync_wrapper
def get_object_id(bp, element):
    return bp.poco.agent.c.call("GetObjectId", element)


@sync_wrapper
def get_object_id_by_id(bp, id):
    return bp.poco.agent.c.call("GetObjectIdById", id)


@sync_wrapper
def get_child_id(bp, element, child_name):
    return bp.poco.agent.c.call("GetChildId", element, child_name)


@sync_wrapper
def get_child_id_by_id(bp, id, child_name):
    return bp.poco.agent.c.call("GetChildIdById", id, child_name)

# @sync_wrapper
# def get_offspring_id(bp, element, offspring_path):
#     return bp.poco.agent.c.call("GetOffspringId", element, offspring_path)


@sync_wrapper
def get_offspring_id_by_id(bp, id, offspring_path):
    return bp.poco.agent.c.call("GetOffspringIdById", id, offspring_path)

@sync_wrapper
def get_parent_id(bp, element):
    return bp.poco.agent.c.call("GetParentId", element)


@sync_wrapper
def get_parent_id_by_id(bp, id):
    return bp.poco.agent.c.call("GetParentIdById", id)


@sync_wrapper
def get_item_count(bp, tpid):
    return bp.poco.agent.c.call("GetItemCount", tpid)

@sync_wrapper
def get_toggle_is_on(bp, element):
    return bp.poco.agent.c.call("GetToggleIsOn", element)

@sync_wrapper
def get_toggle_is_on_by_id(bp, id):
    return bp.poco.agent.c.call("GetToggleIsOnById", id)

def cmd(bp, command):
    bp.poco.agent.c.call("CMD", command)
