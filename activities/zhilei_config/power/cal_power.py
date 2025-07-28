"""
计算当前装备的最终战力是多少
"""
import copy
from activities.zhilei_config.common_functions import match_keys, get_format_data, match_keys_get_value
from tools.txtTableRead.get_table_data import get_table_data,write_table_data
# from icecream import ic
import pandas as pd
import numpy as np

# 装备战力计算

# 读表
adv_level_data=get_table_data("ADV_LEVEL_UP")
adv_quality_data=get_table_data("ADV_GEAR_QUALITY")
adv_star_data=get_table_data("ADV_GEAR_STAR")
power_convert_data=get_table_data("POWER_NEW_PLOT_CONVERT")
medal_star_data=get_table_data("FISHING_MEDAL_STARS")

base_attr_config={
    'damage':0,
    'hookDamage':0,
    'lineLength':0,
    'reelVelocityZ':0,
}

# 根据装备品质+部位 找到 adv_gear_star表对应的group id
star_type_data={
    # 红色
    6:{
        1:'14211',
        2:'14206',
        3:'14205',
    },
    # 金色
    5: {
        1: '14209',
        2: '14203',
        3: '14204',
    }
}

base_star_config={
    'add_damage':0,
    'add_lineLength':0,
    'add_hookDamage':0,
    'add_reelVelocityZ':0,
    'powerSkillRate':0,
}

def get_star_data(adv_type,star,quality):
    """ 返还指定品质指定星级的装备的  ADV_GEAR_STAR表对应参数， 包括 星级加成数值、技能强度数值 等配置 """
    match_data={'starGroupId':star_type_data[quality][adv_type],'star':str(star)}
    value=match_keys_get_value(adv_star_data,match_data)
    return get_format_data(value,base_star_config)

base_quality_config={
    'damageCoefficient':0,
    'lineLengthCoefficient':0,
    'reelVelocityZCoefficient':0,
    'hookDamageCoefficient':0,
}

def get_quality_data(adv_type,quality):
    """ 返回指定品质的ADV_GEAR_QUALITY表的 加成数值"""
    value=match_keys_get_value(adv_quality_data, {'qualityType':str(quality)})
    key2={1:'rod',2:'line',3:'bait'}[adv_type]
    return get_format_data(value[key2],base_quality_config)

# 1代表词条，2代表技能勋章
medal_group_id={
    1:{
        4:4,
        5:5,
        6:6,
    },
    2:{
        4:7,
        5:8,
        6:9,
    },
}
medal_base_star_config={
    'powerRate':0,
    'powerCollectionScore':0,
}
def get_medal_star_data(medal_type,star,quality):
    """ 返还指定品质指定星级的勋章的  FISHING_MEDAL_STARS表 对应参数"""
    match_data={'starGroup':str(medal_group_id[medal_type][quality]),'starNum':str(star)}
    print(match_data)
    value=match_keys_get_value(medal_star_data,match_data)
    return get_format_data(value,medal_base_star_config)


def int_data(data):
    for key in data:
        data[key]=int(data[key])

def add_dict(data1,data2):
    for key in data1:
        data1[key]+=data2[key]

def get_attr(suit_data):
    """
    获取每个部位的装备的属性，并且将他们汇总
    输入样例：
    suit_data={
        1:{'level':195,'quality':5,'star':3},
        2:{'level':200,'quality':6,'star':1},
        3:{'level':198,'quality':6,'star':0},
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
        star_data=get_star_data(adv_type,star,quality)
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
    """ 获取当前装备的技能强度系数 """
    ret=[]
    for adv_type in [1, 2, 3]:
        star = suit_data[adv_type]['star']
        quality = suit_data[adv_type]['quality']
        star_data = get_star_data(adv_type, star,quality)
        ret.append(int(star_data['powerSkillRate']))
    return ret

def get_medal_rate(medal_list):
    """获取当前勋章的技能强度系数"""
    ret=[]
    for medal_data in medal_list:
        star = medal_data['star']
        quality = medal_data['quality']
        medal_type = medal_data['type']
        star_data = get_medal_star_data(medal_type, star,quality)
        ret.append(int(star_data['powerRate']))
    return ret


def convert_power(pre_num,data):
    """ 计算战力的最后一步，缩放映射，主要是减小高低属性之间的战力差距 """
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
def cal_power(suit_data,medal_list=[]):
    """ 根据属性值计算最终的战力 """
    attr_data=get_attr(suit_data)
    # print(attr_data)
    skill_rate=sum(get_skill_rate(suit_data))
    medal_rate=sum(get_medal_rate(medal_list))
    power=(attr_data['damage']+attr_data['hookDamage']*0.005)/100*attr_data['lineLength']/10*((attr_data['reelVelocityZ']/1000)**2)*(1+skill_rate/100+medal_rate/1000)
    return convert_power(power,power_convert_data)

def get_level_cost(level):
    """ 计算3个部位装备 在当前等级 提升1级所需要的金币花费，返回[10w,10w,10w] 各部位的花费 """
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
    """ 按照 总持有金币数 获取 当前等级能 升级的次数 """
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
    """ 构造套装数据，默认红装，支持star=数字 或者分部位配置 [4,5,6] """
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
    """ 输入装备等级和 星级列表，返还最终战力"""
    return cal_power(get_suit_data(level,star_list))

def get_up_num_power(star,start_level,up_num):
    """ 计算升到xx级，会提升多少战力 """
    power1 = cal_power_simple(start_level,star)
    power2 = cal_power_simple(start_level+up_num, star)
    return power2-power1

# 样例展示，计算指定装备战力
suit_data={
    1:{'level':300,'quality':6,'star':5},
    2:{'level':300,'quality':6,'star':5},
    3:{'level':300,'quality':6,'star':5},
}
medal_list=[
    # {'type':1,'quality':6,'star':10} for i in range(9)
]
print(cal_power(suit_data,medal_list))

# 样例展示，计算指定级别 升1级的消耗
level_list=[50,100,150,190]
for level in level_list:
    cost_list=get_level_cost(level)
    total_cost=sum(cost_list)
    print(level,total_cost)

# 样例展示，计算指定级别 花费指定金币数，能够提升的等级以及能战力
# 以红2星为例
now_star=2

data1=[
[50,1000000],
[100,1700000],
[150,2400000],
[190,3000000],]

for value in data1:
    up_num=get_level_up_num(value[0],value[1])
    power_num=get_up_num_power(now_star,value[0],up_num)
    print(up_num,power_num)

def output_full_power():
    """ 计算全装备星级+等级 对应的详细战力值 """
    data=np.zeros((300,6))
    for level in range(1,301):
        for star in [0, 1,2,3,4,5]:
            power = cal_power_simple(level, star)
            data[level-1][star]=power
    column_labels = [0, 1, 2, 3, 4, 5]
    index_labels = list(range(1, 301))
    df=pd.DataFrame(data,columns=column_labels,index=index_labels)
    df.to_excel('output.xlsx', index=True)

