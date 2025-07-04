from tools.txtTableRead.get_table_data import get_table_data, write_table_data, get_table_data_by_file
import copy
from datetime import datetime,timedelta
from configs.pathConfig import EXCEL_PATH,RELEASE_EXCEL_PATH
import os

# 显示活动时间范围
show_start_data="2025-07-11 00:00:00"
show_end_data="2025-08-07 00:00:00"

SORT_OPEN_TIME=1
SORT_END_TIME=2

sort_type=SORT_END_TIME  # 排序方式

# timer数据
data_keys = "timer_main"
dev_path = os.path.dirname(os.path.dirname(EXCEL_PATH))+'/ElementData/BaseData/'+data_keys.upper()+".data.txt"
release_path = os.path.dirname(os.path.dirname(RELEASE_EXCEL_PATH))+'/ElementData/BaseData/'+data_keys.upper()+".data.txt"

# 这里用dev还是release
timer_data=get_table_data_by_file(data_keys,dev_path)

# 时间数据格式化
date_format = "%Y-%m-%d %H:%M:%S"
show_start_data=datetime.strptime(show_start_data,date_format)
show_end_data=datetime.strptime(show_end_data,date_format)


def get_timer_data(value):
    """ 兼容两种不同格式的数据，返回完整数据 """
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
for key,value in timer_data.items():
    try:
        openTime,endTime,delta_day=get_timer_data(value)
        # 筛选那种持续时间比较短的
        if 0<delta_day<60 and ((show_start_data<=openTime<=show_end_data) or (show_start_data<=endTime<=show_end_data) or (show_start_data>=openTime and show_end_data<=endTime) )  :
            result_list.append([value['name'],openTime,endTime,delta_day,key])
    except:
        pass

# 按时间先后排序
new_list=sorted(result_list,key=lambda x:x[sort_type])
for i in new_list:
    print(i[4],"  ",i[1],"  ",i[2],"    ",i[3],"   ",i[0])
