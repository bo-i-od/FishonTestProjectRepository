from tools.txtTableRead.get_table_data import get_table_data,write_table_data
import copy


from datetime import datetime,timedelta
time_str = "2025-05-09 00:00:00"
dt_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")  # 返回datetime对象
date_format = "%Y-%m-%d %H:%M:%S"


data_keys = "timer_main"
timer_data=get_table_data(data_keys)

show_start_data="2025-06-05 00:00:00"
show_start_data=datetime.strptime(show_start_data,date_format)
show_end_data="2025-07-10 00:00:00"
show_end_data=datetime.strptime(show_end_data,date_format)

result_list=[]

for key,value in timer_data.items():
    try:
        openTime=datetime.strptime(value['openTime'],date_format)
        delta_day=0
        if value.get('endTime'):
            endTime=datetime.strptime(value['endTime'],date_format)+timedelta(seconds=2)
            delta_day=(endTime-openTime).days
        else:
            if value.get('durationTime'):
                delta_day=int(value['durationTime']['day'])
        if 0<delta_day<30 and show_start_data<openTime<show_end_data:
            result_list.append([value['name'],openTime,delta_day])
    except:
        pass
new_list=sorted(result_list,key=lambda x:x[1])
for i in new_list:
    print(i[1],"  ",i[2],"     ",i[0])




# for key,value in xdays_rank_reward.items():
#     for reward in value['rankRewards']:
#         if reward.get('itemId') in replace_dict:
#             reward['itemId']=replace_dict[reward['itemId']]
#             reward['itemType']=1
#
#
# write_table_data(data_keys,xdays_rank_reward)