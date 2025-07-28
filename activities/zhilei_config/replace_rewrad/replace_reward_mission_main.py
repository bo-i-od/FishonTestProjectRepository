"""
将xx表的xx字段的值，替换成另外一个值
"""
from activities.zhilei_config.fix_table_id.all_table_id_list import language_table_id_list, not_language_table_id_list
from tools.txtTableRead.get_table_data import get_table_list_data, write_table_data, get_table_data, get_tp_id_name, \
    get_name_name
# test
table_key='adv_level_up'
table_data=get_table_data(table_key)


replace_dict={
    '9700002':'102800',
    '9700003':'102900',
    '9700004':'103000',
    '9700005':'103100'
}

for key,value in table_data.items():
    for value_key,value_value in value.items():
        if value_key=='awards':
            for i in value_value:
                if i.get('itemId') in replace_dict:
                    i['itemId']=replace_dict[i['itemId']]
                    i['itemType'] = 1

write_table_data(table_key,table_data)