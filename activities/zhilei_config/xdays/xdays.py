import copy
import json

from tools.txtTableRead.get_table_data import get_table_data,write_table_data
from icecream import ic
import pandas as pd
from datetime import datetime, timedelta

# 读取Excel文件
# 替换为您的Excel文件路径
df = pd.read_excel('xdays.xlsx',
                   header=0,  # 第一行作为列名
                   )  # 指定空值标记
print(df)


def add_time_to_datetime(datetime_obj, days=0, hours=0, seconds=0):
    """
    将日期时间对象加上指定的天数、小时数和秒数
    :param datetime_obj: 日期时间对象（可以是datetime、Timestamp或字符串）
    :param days: 要增加的天数
    :param hours: 要增加的小时数
    :param seconds: 要增加的秒数
    :return: 处理后的日期时间字符串
    """
    try:
        # 处理不同类型的输入
        if isinstance(datetime_obj, str):
            dt = datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M:%S')
        elif isinstance(datetime_obj, pd.Timestamp):
            dt = datetime_obj.to_pydatetime()
        elif isinstance(datetime_obj, datetime):
            dt = datetime_obj
        else:
            raise ValueError("不支持的日期时间格式")

        # 计算时间增量
        delta = timedelta(days=days, hours=hours, seconds=seconds)

        # 增加时间
        new_dt = dt + delta

        # 转换回字符串格式
        return new_dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(f"错误：{str(e)}")
        return None

def trans_fisheries_list(fisheries_list):
    result=str(fisheries_list).split(',')
    return result

xdays_main_data=get_table_data("xdays_main")
xdays_rank_data=get_table_data("xdays_rank")
mission_group_data=get_table_data("mission_group")
timer_main_data = get_table_data("timer_main")
xdays_rank_reward_data = get_table_data("xdays_rank_reward")
fisheries_data = get_table_data("fisheries")

def get_fisheries_level(fisheries_list):
    min_lv=999
    for key,value in fisheries_data.items():
        if value['tpId'] in fisheries_list:
            need_lv=int(value.get('needPlayerLv',0))
            if need_lv and need_lv<min_lv:
                min_lv=need_lv
    if min_lv!=999:
        return min_lv
    else:
        return 0

for index, row in df.iterrows():
    full_name = f"{'' if row['fisheries_list']==0 else row['fisheries_list']}{row['xdays_type']},{row['start_time'].month}.{row['start_time'].day}"
    print(full_name)
    fisheries_list=trans_fisheries_list(row['fisheries_list'])
    single_fisheries=fisheries_list[-1]
    # =============处理xdays main==============
    xdays_id=row['xdays_id']
    # 先拷贝一下数据
    for key,value in xdays_main_data.items():
        if value['name']==row['xdays_type']:
            xdays_main_append_data=copy.deepcopy(value)
            break
    else:
        print("run error")
        break
    # 临时记录一下old group id,后面用
    old_rank_group_id=xdays_main_append_data['rankGroupId']
    # 替换相关数据
    xdays_main_append_data.update({
        'id':xdays_id,
        'name':full_name,
        'tpId':xdays_id,
        'rankGroupId':row['groupId'],
        'fisheries':single_fisheries,
    })
    # =============处理xdays rank==============
    xdays_rank_id=row['groupId']
    # 先拷贝一下数据
    for key,value in xdays_rank_data.items():
        if value['name']==row['xdays_type']:
            xdays_rank_append_data=copy.deepcopy(value)
            break
    else:
        print("run error")
        break
    # 替换相关数据
    xdays_rank_append_data.update({
        'id':xdays_rank_id,
        'name': full_name,
        'groupId':xdays_rank_id,
        'fisheries':single_fisheries,
        'rankEarlyEndTime':39600,
    })
    if row['xdays_type'] in ['最高单鱼得分','钓鱼王冠军赛','典藏奇珍超奇珍']:
        xdays_rank_append_data['rankTypeArgs'][0]=row['fisheries_list']

    # =============处理 mission group==============
    # 先拷贝一下数据
    for key,value in mission_group_data.items():
        if value['groupId']==old_rank_group_id:
            mission_group_append_data=copy.deepcopy(value)
            break
    else:
        print("run error")
        break
    mission_group_append_data.update({
        'id':xdays_rank_id,
        'name':full_name,
        'groupId':xdays_rank_id,
        'fisheriesId':single_fisheries,
        'openArg':row['group_timer'],
        'closeArg':row['group_timer'],
    })
    if single_fisheries!='0':
        mission_group_append_data.update({
            'serverCharaLevel':get_fisheries_level(fisheries_list)
        })

    # =============处理 timer表=============
    timer_append_data1={
        'tb': 'timer_main',
        'id': row['group_timer'],
        'name': full_name,
        'timerID': row['group_timer'],
        'timerName': row['xdays_type'],
        'cycleType': '1',
        'openTime': row['start_time'],
        'endTime': add_time_to_datetime(row['start_time'],days=row['days'],seconds=-1),
    }
    # ========处理 xdays reward表================
    # 先拷贝一下数据
    reward_now_id = xdays_id * 100+1
    reward_append_data={}
    for key,value in xdays_rank_reward_data.items():
        if value['groupId']==old_rank_group_id:
            reward_append_data[str(reward_now_id)]=copy.deepcopy(value)
            reward_append_data[str(reward_now_id)].update({
                'id':reward_now_id,
                'name':full_name,
                'tpId':reward_now_id,
                'groupId':xdays_rank_id,
            })
            reward_now_id += 1

    #  !!!!!!!!!!!!!!!!回写时主key一定要是字符串！！！！！！！！！！！！！
    xdays_main_data[str(xdays_id)]=xdays_main_append_data
    xdays_rank_data[str(xdays_rank_id)]=xdays_rank_append_data
    mission_group_data[str(xdays_rank_id)] = mission_group_append_data
    timer_main_data.update({
        str(row['group_timer']):timer_append_data1,
    })
    xdays_rank_reward_data.update(reward_append_data)

# ic(xdays_rank_reward_data)

write_table_data('xdays_main',xdays_main_data)
write_table_data('xdays_rank',xdays_rank_data)
write_table_data('mission_group',mission_group_data)
write_table_data('timer_main',timer_main_data)
write_table_data('xdays_rank_reward',xdays_rank_reward_data)



