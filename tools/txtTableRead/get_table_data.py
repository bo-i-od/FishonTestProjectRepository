import json
import os

from configs.pathConfig import EXCEL_PATH
from tools.txtTableRead.translate_assist_diff_versions import doWorkOnDataTxtFile,doWriteConfigTable

file_path = os.path.dirname(os.path.dirname(EXCEL_PATH))+'/ElementData/BaseData/'


def get_table_data(data_key):
    """
    data_key: 表名，不带后缀
    返回值: {
        key1:value1,
        key2:value1,
        ...
    }
    key: 第一列的id（非tpid)
    value: 每一行的数据，同样以key-value的形式保存，key为表头字段
    """
    collect_list = []
    collect_map = {}
    collect_dup_map = None
    doWorkOnDataTxtFile(file_path + data_key.upper() + ".data.txt", 'en', collect_list, collect_dup_map, collect_map)
    return collect_map[data_key.lower()]


def get_table_data_by_file(data_key,file_name):
    """
    data_key: 表名，不带后缀
    返回值: {
        key1:value1,
        key2:value1,
        ...
    }
    key: 第一列的id（非tpid)
    value: 每一行的数据，同样以key-value的形式保存，key为表头字段
    """
    collect_list = []
    collect_map = {}
    collect_dup_map = None
    doWorkOnDataTxtFile(file_name, 'en', collect_list, collect_dup_map, collect_map)
    return collect_map[data_key.lower()]



def get_table_list_data(data_keys):
    """
    data_keys = ["BATTLE_SKILL", "BATTLE_BUFF", "FISH_TYPECLASS_VISUAL", "FISH_STAR_GRADING", "FISHERIES", "FISH"]
    返回值也是多套一层list
    """
    collect_list = []
    collect_map = {}
    collect_dup_map = None
    result={}

    # 读取txt数据
    for data_key in data_keys:
        doWorkOnDataTxtFile(file_path + data_key + ".data.txt", 'en', collect_list, collect_dup_map, collect_map)
        result[data_key.lower()+'_table'] = collect_map[data_key.lower()]
    return result

def write_table_data(table_name,table_data):
    """
    table_name: 表名，不带后缀
    table_data: 和上文 get_table_data 一致的数据结构
    """
    table_name=table_name.lower()
    doWriteConfigTable(file_path, table_name, table_data.values())

if __name__ == '__main__':
    battle_skill_data=get_table_data("BATTLE_SKILL")
    from icecream import ic
    ic(battle_skill_data)
