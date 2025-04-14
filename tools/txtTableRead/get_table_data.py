import json
import os

from configs.pathConfig import EXCEL_PATH
from tools.txtTableRead.translate_assist_diff_versions import doWorkOnDataTxtFile,doWriteConfigTable

file_path = os.path.dirname(os.path.dirname(EXCEL_PATH))+'/ElementData/BaseData/'

def get_table_data(data_key):
    # data_key = "BATTLE_SKILL"
    collect_list = []
    collect_map = {}
    collect_dup_map = None
    doWorkOnDataTxtFile(file_path + data_key + ".data.txt", 'en', collect_list, collect_dup_map, collect_map)
    return collect_map[data_key.lower()]

def get_table_list_data(data_keys):
    # data_keys = ["BATTLE_SKILL", "BATTLE_BUFF", "FISH_TYPECLASS_VISUAL", "FISH_STAR_GRADING", "FISHERIES", "FISH"]
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
    doWriteConfigTable(file_path, table_name, table_data.values())

if __name__ == '__main__':
    print(get_table_list_data(["BATTLE_SKILL", "BATTLE_BUFF"]))
