from tools.commonTools import *


def check_icon_list(icon_list:list):
    cur = 0
    while cur < len(icon_list):
        icon_list[cur] = check_icon(icon_list[cur])
        cur += 1

# 由于金币、绿钞、鱼卡包会有多个图标
# 该check就是按图标名转为最普通的图标（表里tpid对应的图标名）
def check_icon(icon:str):
    "store_buff_doublehook"
    if icon == "store_items_shop_1":
        return 'coin_gold'
    if icon == "store_items_shop_2":
        return 'res_gear_1'
    if icon == "store_items_shop_3":
        return 'coin_turntable'
    if "res_power" in icon:
        return "res_power"

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

# 得到数据库中物品数量
def get_resource(bp, item_tpid:str, element_data:dict):
    item_db = bp.get_item_count(item_tpid=item_tpid)
    item_show = bp.get_text(element_data=element_data)

    target_list = [unit_conversion_int_to_str(item_db), unit_conversion_int_to_str_chs(item_db), str(item_db)]
    if item_show not in target_list:
        raise DifferError
    return item_db

# 生成或更新item_dict
# 物品及数量以字典格式{'图标名0':数量0，'图标名1':数量1，……}展示
def make_item_dict(item_icon_list: list, item_quantity_list: list, item_dict: dict = None):
    item_coin_list_len = len(item_icon_list)
    item_quantity_list_len = len(item_quantity_list)
    if item_coin_list_len != item_quantity_list_len:
        print("请保证图标列表长度和数量列表长度想等")
        return None
    cur = 0
    if item_dict is None:
        item_dict = {}
    while cur < item_quantity_list_len:
        if item_icon_list[cur] in item_dict:
            try:
                item_quantity = int(item_quantity_list[cur])
            except:
                item_quantity = 1
            item_dict[item_icon_list[cur]] += item_quantity
        else:
            try:
                item_quantity = int(item_quantity_list[cur])
            except:
                item_quantity = 1
            item_dict[item_icon_list[cur]] = item_quantity
        cur += 1
    return item_dict

# 普通物品与鱼竿鱼饵的图标会有区别
# 鱼竿鱼饵的图标没有对应的数量，有时需要区分下
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








