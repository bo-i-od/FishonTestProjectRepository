from statistics.new_battle_cal.read_config.translate_assist_diff_versions import doWorkOnDataTxtFile
from statistics.new_battle_cal import attr_config
file_path=attr_config.file_path

collect_list = []
collect_map = {}
collect_dup_map = None

# 将需要处理的文件名放入列表中
data_keys = ["BATTLE_SKILL", "BATTLE_BUFF", "FISH_TYPECLASS_VISUAL", "FISH_STAR_GRADING"]

for data_key in data_keys:
    doWorkOnDataTxtFile(file_path + data_key + ".data.txt", 'en', collect_list, collect_dup_map, collect_map)
    globals()[f"{data_key.lower()}_data"] = collect_map[data_key.lower()]

if __name__ == '__main__':
    # print(battle_buff_data)
    # print(battle_skill_data)
    print(battle_skill_data)
    # print(collect_list)
