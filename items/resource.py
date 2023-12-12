from tools.commonTools import *

def check_icon_list(icon_list:list):
    cur = 0
    while cur < len(icon_list):
        icon_list[cur] = check_icon(icon_list[cur])
        cur += 1
def check_icon(icon:str):
    "store_buff_doublehook"
    s = icon.split('_')
    if s[0] == 'coin' and s[1] == "gold":
        icon = 'coin_gold'
    elif s[0] == 'store':
        if s[1] == "money":
            icon = 'coin_gem'
        elif "box" in s[1]:
            icon = s[1]
        elif s[1] == "buff":
            icon = icon.replace("store", "item")
        elif s[1] == "res" and s[2] == "gear":
            icon = f'{s[1]}_{s[2]}_{s[3]}'
        elif s[1] == "fishbag":
            icon = icon.replace("store_", "")
    return icon

def get_resource(bp, item_tpid:str, element_data:dict, is_unit_conversion=False):
    item_db = bp.get_item_count(item_tpid=item_tpid)
    item_show = bp.get_text(element_data=element_data)
    if is_unit_conversion:
        item_db_str = unit_conversion_int_to_str(item_db)
    else:
        item_db_str = str(item_db)
    compare(item_db_str, item_show)
    return item_db

    # 生成或更新item_dict

def make_item_dict(item_coin_list: list, item_quantity_list: list, item_dict: dict = None):
    item_coin_list_len = len(item_coin_list)
    item_quantity_list_len = len(item_quantity_list)
    if item_coin_list_len != item_quantity_list_len:
        print("请保证图标列表长度和数量列表长度想等")
        return None
    cur = 0
    if item_dict is None:
        item_dict = {}
    while cur < item_quantity_list_len:
        if item_coin_list[cur] in item_dict:
            try:
                item_quantity = int(item_quantity_list[cur])
            except:
                item_quantity = 1
            item_dict[item_coin_list[cur]] += item_quantity
        else:
            try:
                item_quantity = int(item_quantity_list[cur])
            except:
                item_quantity = 1
            item_dict[item_coin_list[cur]] = item_quantity
        cur += 1
    return item_dict


def divide_item_and_gear_icon(icon_list:list):
    item_icon_list = []
    gear_icon_list = []
    for icon in icon_list:
        icon_splited = icon.split('_')
        if icon_splited[0] == 'rod' or icon_splited[0] == 'bait':
            gear_icon_list.append(icon)
            continue
        item_icon_list.append(icon)
    return item_icon_list, gear_icon_list






