from poco.pocofw import Poco


def set_text(poco:Poco, element: dict, text: str) -> any:
    ...

def set_text_by_id(poco:Poco, id_list: list, offspring_path:str, text: str) -> any:
    ...

def get_text(poco:Poco, element: dict) -> list:
    ...

def get_text_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_slider_value(poco:Poco, element: dict) -> list:
    ...

def get_slider_value_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_img_name(poco:Poco, element: dict) -> list:
    ...

def get_img_name_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_name(poco:Poco, element: dict) -> list:
    ...

def get_name_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_position(poco:Poco, element: dict) -> list:
    ...

def get_position_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_size(poco:Poco, element: dict) -> list:
    ...

def get_size_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_object_id(poco:Poco, element: dict) -> list:
    ...


def get_offspring_id_by_id(poco:Poco, id_list: list, offspring_path: str) -> list:
    ...

def get_parent_id(poco:Poco, element: dict) -> list:
    ...

def get_parent_id_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_children_id(poco:Poco, element: dict) -> list:
    ...

def get_children_id_by_id(poco:Poco, id_list: list, offspring_path:str) -> list:
    ...

def get_item_count(poco:Poco, tpid_list: list) -> list:
    ...


def get_toggle_is_on(poco:Poco, element: dict)-> list:
    ...

def get_toggle_is_on_by_id(poco:Poco, id_list: list, offspring_path:str)-> list:
    ...

def screen_shot(poco:Poco, ui_x:int, ui_y:int, ui_w:int, ui_h:int)-> (str, str):
    ...

def get_dropdown_value(poco:Poco, element: dict)-> int:
    ...

def set_dropdown_value(poco:Poco, element: dict, index:int)-> any:
    ...

def cmd(poco:Poco, command: list)-> any:
    ...

def lua_console(poco:Poco, command: list)-> any:
    ...

def set_btn_enabled(poco:Poco, element: dict, enabled: bool)-> any:
    ...
