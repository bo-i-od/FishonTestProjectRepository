from statistics.load_log import *
import numpy as np

cast_log = load_log_new('../new_hook_log.txt')


# ------新增鱼获星数分布----------
star_dict={}
for i in cast_log:
    star=i['fishes']['1']['star']
    multi=i['energyMultiplying']
    if star > 0:
        if multi not in star_dict:
            star_dict[multi]=[]
        star_dict[multi].append(star)

if __name__ == '__main__':
    # from icecream import ic

    print("钓鱼星数统计")
    for key,value in star_dict.items():
        np_value=np.array(value)
        print("energyMultiplying:",key)
        print(
            "范围", np.min(np_value),"~",np.max(np_value),'\n',
            "均值",round(np.mean(np_value),2),'\n',
            "1/4、中位数、3/4位数",np.percentile(np_value, 25),np.median(np_value),np.percentile(np_value, 75),'\n',
        )
    # print(star_dict)