from statistics.new_battle_cal.read_config.translate_assist_diff_versions import doWorkOnDataTxtFile
from statistics.new_battle_cal import attr_config
file_path=attr_config.file_path
battle_skill="BATTLE_SKILL"
battle_buff = "BATTLE_BUFF"

collect_list = []
collect_map = {}
collect_dup_map = None
doWorkOnDataTxtFile(file_path+battle_skill+".data.txt", 'en', collect_list, collect_dup_map, collect_map)
doWorkOnDataTxtFile(file_path+battle_buff+".data.txt", 'en', collect_list, collect_dup_map, collect_map)

battle_buff_data=collect_map[battle_buff.lower()]
battle_skill_data=collect_map[battle_skill.lower()]


if __name__ == '__main__':
    print(battle_buff_data)
    print(battle_skill_data)

