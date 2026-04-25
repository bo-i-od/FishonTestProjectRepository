from typing import Any, Tuple

async def get_screen_size(server) -> Tuple[int, int]:
    return await server.call("GetScreenSize")

async def set_text(server, element_data_list: list, text: str) -> Any:
    """
    设置目标元素的文本。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :param text: 需要设置的字符串文本。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetText", element_data_list, text)


async def set_text_by_id(server, id_list: list, offspring_path: str, text: str) -> Any:
    """
    通过实例ID和子节点路径设置文本。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :param text: 需要设置的字符串文本。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetTextById", id_list, offspring_path, text)


async def get_text(server, element_data_list: list) -> list:
    """
    获取目标元素的文本。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含元素文本的列表。
    """
    return await server.call("GetText", element_data_list)


async def get_text_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取文本。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含节点文本的列表。
    """
    return await server.call("GetTextById", id_list, offspring_path)


async def get_slider_value(server, element_data_list: list) -> list:
    """
    获取滑动条(Slider)的当前值。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含滑动条数值的列表。
    """
    return await server.call("GetSliderValue", element_data_list)


async def get_slider_value_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取滑动条(Slider)的值。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含滑动条数值的列表。
    """
    return await server.call("GetSliderValueById", id_list, offspring_path)


async def get_img_name(server, element_data_list: list) -> list:
    """
    获取图像(Image)组件的图片名称。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含图片名称的列表。
    """
    return await server.call("GetImgName", element_data_list)


async def get_img_name_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取图片名称。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含图片名称的列表。
    """
    return await server.call("GetImgNameById", id_list, offspring_path)


async def get_name(server, element_data_list: list) -> list:
    """
    获取目标对象的名称。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含对象名称的列表。
    """
    return await server.call("GetName", element_data_list)


async def get_name_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取对象名称。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含对象名称的列表。
    """
    return await server.call("GetNameById", id_list, offspring_path)


async def get_position(server, element_data_list: list) -> list:
    """
    获取目标元素的位置坐标。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含位置信息的列表（如坐标数组）。
    """
    return await server.call("GetPosition", element_data_list)


async def get_position_by_id(server, id_list: list, offspring_path: str, locator_camera: str) -> list:
    """
    通过实例ID和子节点路径在指定摄像机下获取坐标位置。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :param locator_camera: 摄像机名称。
    :return await: 包含位置信息的列表。
    """
    return await server.call("GetPositionById", id_list, offspring_path, locator_camera)


async def get_size(server, element_data_list: list) -> list:
    """
    获取目标元素的尺寸大小(宽高)。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含尺寸信息的列表。
    """
    return await server.call("GetSize", element_data_list)


async def get_size_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取元素尺寸。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含尺寸信息的列表。
    """
    return await server.call("GetSizeById", id_list, offspring_path)


async def get_object_id(server, element_data_list: list) -> list:
    """
    获取目标对象的实例ID。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含实例ID的列表。
    """
    return await server.call("GetObjectId", element_data_list)


async def get_offspring_id_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取子对象的实例ID。

    :param server: RPC服务器实例对象。
    :param id_list: 父级实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含子对象实例ID的列表。
    """
    return await server.call("GetOffspringIdById", id_list, offspring_path)


async def get_parent_id(server, element_data_list: list) -> list:
    """
    获取目标元素的父对象实例ID。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含父对象实例ID的列表。
    """
    return await server.call("GetParentId", element_data_list)


async def get_parent_id_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取其父对象的实例ID。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含父对象实例ID的列表。
    """
    return await server.call("GetParentIdById", id_list, offspring_path)


async def get_item_count(server, tpid_list: list) -> list:
    """
    获取指定模版/列表容器中的子项数量。

    :param server: RPC服务器实例对象。
    :param tpid_list: 目标对象的路径或ID列表。
    :return await: 包含子项数量的列表。
    """
    return await server.call("GetItemCount", tpid_list)


async def get_toggle_is_on(server, element_data_list: list) -> list:
    """
    获取开关(Toggle)组件当前的选中状态。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含布尔状态（是否选中）的列表。
    """
    return await server.call("GetToggleIsOn", element_data_list)


async def get_toggle_is_on_by_id(server, id_list: list, offspring_path: str) -> list:
    """
    通过实例ID和子节点路径获取开关(Toggle)组件的选中状态。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :return await: 包含布尔状态的列表。
    """
    return await server.call("GetToggleIsOnById", id_list, offspring_path)


async def screen_shot(server, ui_x: int, ui_y: int, ui_w: int, ui_h: int) -> Tuple[str, str]:
    """
    在指定屏幕UI区域进行截图。

    :param server: RPC服务器实例对象。
    :param ui_x: 截图区域左下角或左上角X坐标。
    :param ui_y: 截图区域左下角或左上角Y坐标。
    :param ui_w: 截图区域宽度。
    :param ui_h: 截图区域高度。
    :return await: 包含截图信息的元组（如格式类型和Base64图像数据）。
    """
    return await server.call("Screenshot", ui_x, ui_y, ui_w, ui_h)


async def get_dropdown_value(server, element_data_list: list) -> list:
    """
    获取下拉框(Dropdown)当前的选中值。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 包含下拉框选中值的列表。
    """
    return await server.call("GetDropdownValue", element_data_list)


async def set_dropdown_value(server, element_data_list: list, index: int) -> Any:
    """
    设置下拉框(Dropdown)的选中索引。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :param index: 要选中的目标索引。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetDropdownValue", element_data_list, index)


async def cmd(server, command: list) -> Any:
    """
    执行内置命令。

    :param server: RPC服务器实例对象。
    :param command: 包含命令及其参数的列表。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("CMD", command)


async def lua_console(server, command: list) -> Any:
    """
    通过Lua控制台执行Lua脚本命令。

    :param server: RPC服务器实例对象。
    :param command: 需要执行的Lua指令列表或参数。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("LuaConsole", command)


async def custom_cmd(server, command_list: list) -> Any:
    """
    执行自定义命令。

    :param server: RPC服务器实例对象。
    :param command_list: 自定义指令及其参数组成的列表。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("CustomCMD", command_list)


async def set_btn_enabled(server, element_data_list: list, enabled: bool) -> Any:
    """
    设置按钮(Button)组件是否可交互。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :param enabled: True为启用交互，False为禁用。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetBtnEnabled", element_data_list, enabled)


async def set_object_active(server, path_list: list, active: bool) -> Any:
    """
    设置游戏对象的激活状态(Active)。

    :param server: RPC服务器实例对象。
    :param path_list: 目标元素路径列表。
    :param active: True为激活显示，False为隐藏。
    :return await: 服务器返回的执行结果。
    """
    if not path_list:
        return None
    return await server.call("SetObjectActive", path_list, active)


async def click_button(server, element_data_list: list) -> Any:
    """
    模拟点击按钮(Button)。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("ClickButton", element_data_list)


async def ray_input(server, element_data_list: list, kind: str) -> Any:
    """
    对目标元素发送射线输入事件（如点击、按下、抬起等）。

    :param server: RPC服务器实例对象。
    :param element_data_list: 目标元素路径或标识列表。
    :param kind: 输入事件类型（如"Down", "Up", "Click"等）。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("RayInput", element_data_list, kind)


async def ray_input_by_id(server, id_list: list, offspring_path: str, kind: str) -> Any:
    """
    通过实例ID和子节点路径对目标发送射线输入事件。

    :param server: RPC服务器实例对象。
    :param id_list: 实例ID列表。
    :param offspring_path: 子节点相对路径。
    :param kind: 输入事件类型。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("RayInputById", id_list, offspring_path, kind)


async def set_time_scale(server, time_scale: float) -> Any:
    """
    设置游戏的时间缩放（倍速）。

    :param server: RPC服务器实例对象。
    :param time_scale: 时间缩放比例（例如1.0为正常速度，0为暂停）。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetTimeScale", time_scale)


async def set_send_log_flag(server, send_log_flag: bool) -> Any:
    """
    设置是否向服务端发送日志标记。

    :param server: RPC服务器实例对象。
    :param send_log_flag: True开启发送，False关闭。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetSendLogFlag", send_log_flag)


async def register_push_channel(server) -> Any:
    """
    注册服务器推送消息通道。

    :param server: RPC服务器实例对象。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("RegisterPushChannel")


async def set_camera(server, path_node: str, path_camera: str, camera_type: str) -> Any:
    """
    注册相机配置到 CameraRegistry。

    :param server: RPC服务器实例对象。
    :param path_node: 节点路径（该节点 + 子树共享此相机）。
    :param path_camera: 相机节点路径。
    :param camera_type: 相机类型 "2d" 或 "3d"。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("SetCamera", path_node, path_camera, camera_type)


async def remove_camera(server, path_node: str) -> Any:
    """
    从 CameraRegistry 中移除指定节点路径的相机配置。

    :param server: RPC服务器实例对象。
    :param path_node: 要移除的节点路径。
    :return await: 服务器返回的执行结果。
    """
    return await server.call("RemoveCamera", path_node)