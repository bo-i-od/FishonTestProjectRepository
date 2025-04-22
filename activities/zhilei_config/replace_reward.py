from tools.txtTableRead.get_table_data import get_table_data,write_table_data
from icecream import ic
import copy

replace_dict={
    '9700002':'102800',
    '9700003':'102900',
    '9700004':'103000',
    '9700005':'103100'
}


data_keys = "xdays_rank_reward"
xdays_rank_reward=get_table_data(data_keys)
ic(xdays_rank_reward)

for key,value in xdays_rank_reward.items():
    for reward in value['rankRewards']:
        if reward.get('itemId') in replace_dict:
            reward['itemId']=replace_dict[reward['itemId']]
            reward['itemType']=1


write_table_data(data_keys,xdays_rank_reward)