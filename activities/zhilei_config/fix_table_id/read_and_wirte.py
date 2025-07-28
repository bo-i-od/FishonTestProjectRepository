from activities.zhilei_config.fix_table_id.all_table_id_list import language_table_id_list, not_language_table_id_list
from tools.txtTableRead.get_table_data import get_table_list_data, write_table_data, get_table_data, get_tp_id_name, \
    get_name_name


def insert_at(d, position, key, value):
    """通用的字典位置插入函数"""
    items = list(d.items())
    items.insert(position, (key, value))
    return dict(items)


# table_key_list=[
# 'giftpack_group_condition',
# ]
# table_key_list=language_table_id_list
table_key_list=not_language_table_id_list


warning_remove_list=[]
error_table_list = []
for table_key in table_key_list:
    table_data=get_table_data(table_key)
    # print(table_data)
    write_table_data(table_key, table_data)
    print('finish：'+table_key)
if error_table_list:
    print("errrrrrrrrrrrrorrr!!!!,error_table_list=",error_table_list)






