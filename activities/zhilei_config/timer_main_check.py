from tools.txtTableRead.get_table_data import get_table_data,write_table_data
import copy
from datetime import datetime,timedelta

# 显示活动时间范围
show_start_data="2025-06-05 00:00:00"
show_end_data="2025-07-10 00:00:00"

# timer数据
data_keys = "timer_main"
timer_data=get_table_data(data_keys)

# 时间数据格式化
date_format = "%Y-%m-%d %H:%M:%S"
show_start_data=datetime.strptime(show_start_data,date_format)
show_end_data=datetime.strptime(show_end_data,date_format)

result_list=[]
for key,value in timer_data.items():
    try:
        openTime=datetime.strptime(value['openTime'],date_format)
        delta_day=0 # 持续时间
        if value.get('endTime'):
            endTime=datetime.strptime(value['endTime'],date_format)+timedelta(seconds=2)
            delta_day=(endTime-openTime).days
        else:
            if value.get('durationTime'):
                delta_day=int(value['durationTime']['day'])
        # 筛选那种持续时间比较短的
        if 0<delta_day<30 and show_start_data<openTime<show_end_data:
            result_list.append([value['name'],openTime,delta_day])
    except:
        pass
# 按时间先后排序
new_list=sorted(result_list,key=lambda x:x[1])
for i in new_list:
    print(i[1],"  ",i[2],"     ",i[0])
