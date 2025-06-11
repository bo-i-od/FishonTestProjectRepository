"""
文件说明，比对当前线上timer和 将要上线的timer，判断是否有存在正在运转的活动的timer被修改
"""


from tools.txtTableRead.get_table_data import get_table_data,write_table_data,get_table_data_by_file
import copy
from datetime import datetime,timedelta

# 线上文件
PATH1 = r"C:/Users/TU/Documents/release_2025_4_1/datapool/ElementData/BaseData/TIMER_MAIN.data.txt"
# 将要上线的文件
PATH2 = r"C:/Users/TU/Documents/release_2025_4_1/datapool/ElementData/TIMER_MAIN.data.txt"

# 活动开始时间范围
open_start_data="2025-06-05 00:00:00"
open_end_data="2025-06-13 00:00:00"

# 活动结束时间范围
end_start_data="2025-06-12 23:00:00"
end_end_data="2025-07-10 00:00:00"

# timer数据
timer_data1 = get_table_data_by_file("timer_main",PATH1)
timer_data2 = get_table_data_by_file("timer_main",PATH2)

# 时间数据格式化
date_format = "%Y-%m-%d %H:%M:%S"
open_start_data=datetime.strptime(open_start_data,date_format)
open_end_data=datetime.strptime(open_end_data,date_format)
end_start_data=datetime.strptime(end_start_data,date_format)
end_end_data=datetime.strptime(end_end_data,date_format)


def get_timer_data(value):
    openTime = datetime.strptime(value['openTime'], date_format)
    delta_day = 0  # 持续时间
    if value.get('endTime'):
        endTime = datetime.strptime(value['endTime'], date_format)
        delta_day = (endTime + timedelta(seconds=2) - openTime).days
    else:
        delta_day = int(value['durationTime']['day'])
        endTime = openTime + timedelta(days=delta_day) - timedelta(seconds=1)
    return openTime,endTime,delta_day


result_list=[]
for key,value in timer_data1.items():
    try:
        openTime,endTime,delta_day=get_timer_data(value)
        # 筛选那种持续时间比较短的
        if 0<delta_day<30 and open_start_data<openTime<open_end_data and end_start_data<endTime<end_end_data:
            compare_result="相同"
            if key not in timer_data2:
                compare_result="严重问题！！timer消失！！！"
                result_list.append([key, openTime, endTime, delta_day,compare_result, value['name'],])
            else:
                value2=timer_data2[key]
                openTime2,endTime2,delta_day2=get_timer_data(value2)
                if openTime2!=openTime or endTime2!=endTime or delta_day2!=delta_day:
                    compare_result="timer被改变"
                    result_list.append([key, openTime, endTime, delta_day, compare_result,openTime2, endTime2, delta_day2, value['name'], ])
                else:
                    result_list.append([key, openTime, endTime, delta_day,compare_result, value['name'],])

    except:
        pass

# 按时间先后排序
new_list=sorted(result_list,key=lambda x:x[1])
for i in new_list:
    print(i)


