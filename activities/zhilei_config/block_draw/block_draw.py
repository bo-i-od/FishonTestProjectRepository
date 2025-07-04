from activities.zhilei_config.common_functions import rand_with_weight
from activities.zhilei_config.block_draw.block_draw_config import *
N=14
round_price=[0,3,9,12,15,15,20,20,20,20,20,20,20,20]
round_total_cost=[sum(round_price[:i+1]) for i in range(N)]
print(round_total_cost)
# pos_weight=[[850,100,50] for i in range(N)]
# pos_weight_multi=[
# [0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0.7],
# [1.5,0,0.5],
# [2.5,0,0],
# [0,1.2,1.5],
# [0,0,0],
# [0,0,0],
# [0,0,0],
# [0,0,0.7],
# [1.5,0,0.5],
# [3,0,1.5],
# [0,1.5,2.5],
# ]
# for i in range(N):
#     for j in range(3):
#         if pos_weight_multi[i][j]>0:
#             pos_weight[i][j]=int(pos_weight[i][j]*pos_weight_multi[i][j])
# print(pos_weight)
# roll_wheel=Wheel({
#     'wheel':[1,2,3],
#     'weights':pos_weight
# })

def do_roll_once(now_count,now_pos):
    if now_count==1:
        weights=start_weight
    else:
        now_level=level_config[now_count-2]
        if now_pos<=now_level[0]:
            weights=weight_list[0]
        else:
            if now_level[1]<14:
                if now_pos>=now_level[1]:
                    weights=weight_list[2]
                else:
                    weights=weight_list[1]
            else:
                if now_pos<11:
                    weights=weight_list[3]
                else:
                    weights=special_weight_list[{11:0,12:1,13:2}[now_pos]]

    index=rand_with_weight(weights)
    return index+1

def do_roll():
    now_pos=0
    total_cost=0
    guajian_collect=0
    guajian_cost=[0,0]
    result_list=[]
    cost_list=[]
    pos_list=[]

    for i in range(N):
        now_result=do_roll_once(i+1,now_pos)
        now_pos+=now_result
        now_cost=round_price[i]
        total_cost+=now_cost
        cost_list.append(total_cost)
        result_list.append(now_result)
        pos_list.append(now_pos)
        if not guajian_collect and now_pos>=7:
            guajian_collect=1
            guajian_cost=[i+1,total_cost]
        if now_pos>=14:
            yugan_cost=[i+1,total_cost]
            return guajian_cost,yugan_cost,result_list,cost_list,pos_list


count_list1=[]
count_list2=[]
sum123=[0,0,0]

def count123(result_list):
    for i in result_list:
        sum123[i-1]+=1

def get_final_cost(cost_list,pos_list):
    final_cost_list=[]
    for i in range(N):
        for j_index in range(len(pos_list)):
            j=pos_list[j_index]
            if i+1<=j:
                final_cost_list.append(cost_list[j_index])
                break
    return final_cost_list

total_cost=[0 for i in range(N)]

for i in range(100000):
    result=do_roll()
    count123(result[2])
    # print(result[2])
    count_list1.append(result[0][1])
    count_list2.append(result[1][1])

    cost_list = result[3]
    pos_list = result[4]
    final_cost_list= get_final_cost(cost_list,pos_list)
    total_cost=[total_cost[i]+final_cost_list[i] for i in range(N)]
total_cost=[total_cost[i]/1000 for i in range(N)]
print(total_cost)
print(sum(count_list1)/len(count_list1))
print(sum(count_list2)/len(count_list2))
total=sum(sum123)
sum123=[round(i/total,2) for i in sum123]
print(sum123)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文黑体
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
# 示例数据

# 绘制直方图
plt.hist(count_list1, bins=range(min(count_list1), max(count_list1)+2), edgecolor='black', align='left')

# 绘制直方图
plt.hist(count_list2, bins=range(min(count_list2), max(count_list2)+2), edgecolor='black', align='left')


# 添加标题和标签
plt.title('数字分布直方图')
plt.xlabel('数字')
plt.ylabel('出现次数')

# 显示网格
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 显示图形
plt.show()