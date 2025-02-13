from statistics.base_func import get_fish_size
from statistics.load_log import *

cast_log=load_log_new('../new_cast_log.txt')

total_dict={}
"""
渔场id
{500301:{
    钓点id 
    10101: {
        'Elite': {360109: 4, 'count': 4},
        'Giant': {350114: 14, 'count': 14},
        'Huge': {350110: 7, 350113: 10, 'count': 17},
        'Large': {350109: 20, 'count': 20},
        'Median': {350104: 7, 350105: 6, 'count': 13},
        'Monster': {360113: 1, 'count': 1},
        'Rare': {360101: 6, 360105: 1, 'count': 7},
        'Small': {350101: 10, 350102: 11, 'count': 21},
        'count': 97},
    }
}}
"""

BASE_TYPE=["Small","Median","Large","Huge","Giant","Rare","Elite","Monster"]
TITLE_TYPE=["Rare","Elite","Monster"]

def init_data():
    ret={key:{'count':0} for key in BASE_TYPE}
    ret['count']=0
    return ret

def update_data(fish_id,fish_type,fish_data):
    fish_data['count'] += 1
    fish_data[fish_type].setdefault(fish_id,0)
    fish_data[fish_type][fish_id] += 1
    fish_data[fish_type]['count'] += 1

def print_fish(fish_data):
    print("count",fish_data['count'])
    for i in BASE_TYPE:
        print(i," ",fish_data[i])

for i_index,i in enumerate(cast_log):
    fisheries_id=i['sceneArg1']
    spot_id=i['otherArgMap']['102']
    # 初始化
    fisheries_data=total_dict.setdefault(fisheries_id,{'total':init_data()})
    spot_data=fisheries_data.setdefault(spot_id,init_data())
    # 获取鱼信息
    fish_id=get_fish_id(i)
    fish_type=get_fish_size(fish_id)
    if fish_type!='Special':
        update_data(fish_id,fish_type,spot_data)
        update_data(fish_id,fish_type,fisheries_data['total'])



if __name__ == '__main__':
    from icecream import ic
    # ic(total_dict)
    for fisheries_id,fisheries_data in total_dict.items():
        for spot_id,spot_data in fisheries_data.items():
            if spot_data['count']>0:
                print("fisheries_id",fisheries_id,'spot_id',spot_id,' count',spot_data['count'])
                ic_data={i:spot_data[i] for i in BASE_TYPE}
                print_fish(spot_data)
                print("------------------")
                # 每种鱼的概率
                final_rate = {i: round(spot_data[i]['count']/spot_data['count'], 3) for i in BASE_TYPE}
