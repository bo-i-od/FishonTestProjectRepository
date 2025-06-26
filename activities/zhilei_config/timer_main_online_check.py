"""
文件说明，比对当前线上timer和 将要上线的timer，判断是否有存在正在运转的活动的timer被修改
"""
from activities.zhilei_config.timer_main_check import get_timer_data
from tools.txtTableRead.get_table_data import get_table_data,write_table_data,get_table_data_by_file
import copy
from datetime import datetime,timedelta

# 线上文件
PATH1 = r"C:/Users/TU/Documents/release_2025_4_1/datapool/ElementData/BaseData/TIMER_MAIN.data.txt"
# 将要上线的文件
PATH2 = r"C:/Users/TU/Documents/release_2025_4_1/datapool/ElementData/TIMER_MAIN.data.txt"

# 更新时间 ,注意，一般是会早一些开服，就设在23点就可以
update_data_time="2025-07-10 23:00:00"

activity_end_time=update_data_time

# timer数据
timer_data1 = get_table_data_by_file("timer_main",PATH1)
timer_data2 = get_table_data_by_file("timer_main",PATH2)

# 时间数据格式化
date_format = "%Y-%m-%d %H:%M:%S"
update_data_time=datetime.strptime(update_data_time,date_format)

result_list=[]
for key,value in timer_data1.items():
    try:
        openTime,endTime,delta_day=get_timer_data(value)
        # 筛选那种持续时间比较短的
        if 0<delta_day<60 and openTime<update_data_time<endTime:
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


