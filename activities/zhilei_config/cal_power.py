import copy

from activities.zhilei_config.common_functions import match_keys,get_format_data
from tools.txtTableRead.get_table_data import get_table_data,write_table_data
# from icecream import ic
import pandas as pd
import numpy as np

adv_level_data=get_table_data("ADV_LEVEL_UP")
adv_quality_data=get_table_data("ADV_GEAR_QUALITY")
adv_star_data=get_table_data("ADV_GEAR_STAR")
power_convert_data=get_table_data("POWER_NEW_PLOT_CONVERT")

damage=100
hookDamage=1000
lineLength=1000
reelVelocityZ=2323


base_attr_config={
    'damage':0,
    'hookDamage':0,
    'lineLength':0,
    'reelVelocityZ':0,
}



star_type_data={
    1:'14211',
    2:'14206',
    3:'14205'
}
base_star_config={
    'add_damage':0,
    'add_lineLength':0,
    'add_hookDamage':0,
    'add_reelVelocityZ':0,
    'powerSkillRate':0,
}

def get_star_data(adv_type,star):
    """ 返还指定装备，指定星级的加成数值 """
    match_data={'starGroupId':star_type_data[adv_type],'star':str(star)}
    key=match_keys(adv_star_data,match_data)
    value=adv_star_data[key]
    return get_format_data(value,base_star_config)

base_quality_config={
    'damageCoefficient':0,
    'lineLengthCoefficient':0,
    'reelVelocityZCoefficient':0,
    'hookDamageCoefficient':0,
}

def get_quality_data(adv_type,quality):
    """ 返回指定品质，加成数值"""
    key=match_keys(adv_quality_data, {'qualityType':str(quality)})
    value=adv_quality_data[key]
    key2={1:'rod',2:'line',3:'bait'}[adv_type]
    return get_format_data(value[key2],base_quality_config)

def int_data(data):
    for key in data:
        data[key]=int(data[key])

def add_dict(data1,data2):
    for key in data1:
        data1[key]+=data2[key]

def get_attr(suit_data):
    """ quality_data={
            1:  {'star':5,'quality':5},
    }
    """
    final_attr=copy.deepcopy(base_attr_config)
    # 竿、线、饵
    for adv_type in [1,2,3]:
        level=suit_data[adv_type]['level']
        key=match_keys(adv_level_data,{'upgradeID':str(14100+adv_type),'level':str(level)})
        value=adv_level_data[key]
        attr_data=get_format_data(value,base_attr_config)
        star=suit_data[adv_type]['star']
        quality=suit_data[adv_type]['quality']
        star_data=get_star_data(adv_type,star)
        quality_data=get_quality_data(adv_type,quality)

        int_data(attr_data)
        int_data(star_data)
        int_data(quality_data)

        attr_data['damage']*=(1+star_data['add_damage']/1000)*quality_data['damageCoefficient']/1000
        attr_data['lineLength']*=(1+star_data['add_lineLength']/1000)*quality_data['lineLengthCoefficient']/1000
        attr_data['reelVelocityZ']*=(1+star_data['add_reelVelocityZ']/1000)*quality_data['reelVelocityZCoefficient']/1000
        attr_data['hookDamage'] *= (1 + star_data['add_hookDamage'] / 1000) * quality_data['hookDamageCoefficient'] / 1000

        attr_data['damage']/=1000
        attr_data['hookDamage']/=1000
        attr_data['lineLength'] /= 1000

        add_dict(final_attr,attr_data)
    return final_attr

def get_skill_rate(suit_data):
    """先默认红色"""
    ret=[]
    for adv_type in [1, 2, 3]:
        star = suit_data[adv_type]['star']
        star_data = get_star_data(adv_type, star)
        ret.append(int(star_data['powerSkillRate']))
    return ret

def convert_power(pre_num,data):
    key_list=list(data.keys())
    for i in range(1,len(key_list)):
        key=key_list[i]
        value=data[key]
        preValue=int(value['preValue'])
        afterValue=int(value['afterValue'])

        next_key=key_list[i+1]
        next_value=data[next_key]
        next_preValue=int(next_value['preValue'])
        next_afterValue=int(next_value['afterValue'])

        if pre_num<next_preValue:
            ret=afterValue+(pre_num-preValue)*(next_afterValue-afterValue)/(next_preValue-preValue)
            return int(ret)
def cal_power(suit_data):
    attr_data=get_attr(suit_data)
    # print(attr_data)
    skill_rate=sum(get_skill_rate(suit_data))
    power=(attr_data['damage']+attr_data['hookDamage']*0.005)/100*attr_data['lineLength']/10*((attr_data['reelVelocityZ']/1000)**2)*(1+skill_rate/100)
    return convert_power(power,power_convert_data)

def get_level_cost(level):
    cost_list=[]
    for adv_type in [1, 2, 3]:
        total_cost=0
        count=0
        for i in range(-10,10,1):
            now_level=level+i
            key = match_keys(adv_level_data, {'upgradeID': str(14100 + adv_type), 'level': str(now_level)})
            value=adv_level_data[key]
            cost=int(value['upgradeCost'][0]['count'])
            total_cost+=cost
            count+=1
        cost=total_cost/count
        cost_list.append(cost)
    return cost_list

def get_level_up_num(start_level,cost):
    """ 按消耗获取升级次数 """
    now_level=start_level
    num=0
    for i in range(999):
        now_cost=sum(get_level_cost(now_level))
        cost-=now_cost
        now_level+=1
        num+=1
        if cost<0:
            return num

def get_suit_data(level,star):
    """ 构造套装数据，默认红装 """
    if isinstance(star,int):
        ret={
            1:{'level':level,'quality':6,'star':star},
            2:{'level':level,'quality':6,'star':star},
            3:{'level':level,'quality':6,'star':star},
        }
        return ret
    elif isinstance(star,list):
        ret={
            1:{'level':level,'quality':6,'star':star[0]},
            2:{'level':level,'quality':6,'star':star[1]},
            3:{'level':level,'quality':6,'star':star[2]},
        }
        return ret

def cal_power_simple(level,star_list):
    return cal_power(get_suit_data(level,star_list))

def get_up_num_power(star,start_level,up_num):
    """ 升级提升多少战力 """
    power1 = cal_power_simple(start_level,star)
    power2 = cal_power_simple(start_level+up_num, star)
    return power2-power1

suit_data={
    1:{'level':194,'quality':6,'star':2},
    2:{'level':193,'quality':6,'star':4},
    3:{'level':193,'quality':6,'star':2},
}
cal_power(suit_data)



target=[
[180,1],
[180,2],
[180,3],
[190,3],
[200,3],
[200,4],
]
for i in target:
    cal_power(get_suit_data(i[0],i[1]))

level_list=[50,100,150,190]
for level in level_list:
    cost_list=get_level_cost(level)
    total_cost=sum(cost_list)
    print(total_cost)

data1=[
[50,1000000],
[100,1700000],
[150,2400000],
[190,3000000],]

for value in data1:
    up_num=get_level_up_num(value[0],value[1])
    print(up_num)
    power_num=get_up_num_power(3,value[0],up_num)
    print(power_num)

for value in data1:
    power1=cal_power_simple(value[0],[4,3,3])
    power2=cal_power_simple(value[0],[3,3,3])
    print(power1,power2,power1-power2)

for level in data1:
    for star in [1,2,3,4]:
        power1=cal_power_simple(value[0],star)
        print(star,power1)

data=np.zeros((300,6))

for level in range(1,301):
    for star in [0, 1,2,3,4,5]:
        power = cal_power_simple(level, star)
        data[level-1][star]=power
column_labels = [0, 1, 2, 3, 4, 5]
index_labels = list(range(1, 301))
df=pd.DataFrame(data,columns=column_labels,index=index_labels)

df.to_excel('output.xlsx', index=True)