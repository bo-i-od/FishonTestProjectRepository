from statistics.base_func import get_fish_size
from statistics.load_log import *

cast_log=load_log_new('../new_cast_log1.txt')

total_dict={}

BASE_TYPE=["Small","Median","Large","Huge","Giant","Rare","Elite","Monster"]
TITLE_TYPE=["Rare","Elite","Monster"]

for i in cast_log:
    fisheries_id=i['sceneArg1']
    if fisheries_id not in total_dict:
        total_dict[fisheries_id]={key:{'count':0} for key in BASE_TYPE}
        total_dict[fisheries_id]['count']=0

    fish_id=get_fish_id(i)
    fish_type=get_fish_size(fish_id)
    if fish_type!='Special':
        total_dict[fisheries_id]['count']+= 1
        if fish_id not in total_dict[fisheries_id][fish_type]:
            total_dict[fisheries_id][fish_type][fish_id]=0
        total_dict[fisheries_id][fish_type][fish_id]+=1
        total_dict[fisheries_id][fish_type]['count']+=1




if __name__ == '__main__':
    from icecream import ic
    # ic(total_dict)
    for key,value in total_dict.items():
        print("fisheries_id",key,' count',value['count'])
        ic_data={i:value[i] for i in TITLE_TYPE}
        ic(ic_data)
        # 每种鱼的概率
        final_rate = {i: round(value[i]['count']/value['count'], 3) for i in TITLE_TYPE}
        ic(final_rate)





