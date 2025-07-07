import copy
import json

from tools.txtTableRead.get_table_data import get_table_data,write_table_data


mission_keys = "MISSION_MAIN"
mission_data=get_table_data(mission_keys)

mission_condition_keys= "MISSION_CONDITION"
condition_data=get_table_data(mission_condition_keys)

condition_to_main_dict={}

for key,value in mission_data.items():
    if value['missionType']=='10':
        value['enabled']='0'
    condition_to_main_dict.update({value['missionConditionIDs'][0]:key})

for key,value in condition_data.items():
    condition_id=value['missionConditionID']
    if condition_id in condition_to_main_dict:
        main_id=condition_to_main_dict[condition_id]
        if mission_data[main_id]['missionType']=='10':
            value['enabled']='0'


write_table_data(mission_keys,mission_data)
write_table_data(mission_condition_keys,condition_data)