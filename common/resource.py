from tools.commonTools import *


def check_icon_list(icon_list:list):
    pass


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
        try:
            item_quantity = int(item_quantity_list[cur])
        except:
            item_quantity = 1
        if item_icon_list[cur] in item_dict:
            item_dict[item_icon_list[cur]] += item_quantity
        else:
            item_dict[item_icon_list[cur]] = item_quantity
        cur += 1
    return item_dict