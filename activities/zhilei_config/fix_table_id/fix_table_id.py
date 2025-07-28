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
    table_tp_id_name = get_tp_id_name(table_key)
    table_name_name = get_name_name(table_key)
    pos_1=0
    table_data_list=list(table_data.items())
    remove_key_list=[]
    tp_id_value_list=[]

    # 遍历是否有问题的元素并进行修改，由于涉及到修改所以最好不要直接遍历数组本身，而是通过下标序号访问
    for num in range(len(table_data_list)):
        key,value=table_data_list[num]
        if table_tp_id_name not in value:
            # tpid不存在 则直接移除该行
            remove_key_list.append(num)
            continue
        # 重复性检查
        if value[table_tp_id_name] in tp_id_value_list:
            print("errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrorrrrrrrrrrrrrrr",value['tb'])
            error_table_list.append(value['tb'])
            break
        else:
            tp_id_value_list.append(value[table_tp_id_name])

        tp_id_value=value[table_tp_id_name]

        value_list=list(value.items())
        # print(value_list)
        if value_list[1][0]!='id':
            print(value_list)
            raise

        if value_list[1][1]!=tp_id_value:
            # 不一致，需要统一, 赋值
            value_list[1]=('id',tp_id_value)
            table_data_list[num]=(tp_id_value,dict(value_list))

    if len(remove_key_list)>0:
        for remove_key in reversed(remove_key_list):
            # 从大到小移除，避免乱序
            table_data_list.pop(remove_key)
        warning_remove_list.append(table_key)

    table_data=dict(table_data_list)
    # print(table_data)
    write_table_data(table_key, table_data)
    print('finish：'+table_key)
print(warning_remove_list)
if error_table_list:
    print("errrrrrrrrrrrrorrr!!!!,error_table_list=",error_table_list)






