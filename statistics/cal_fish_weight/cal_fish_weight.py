import random,numpy

from fish_weight_config import fish_weight_table,sum_weight

def random_with_weight():
    random_num=random.randint(0,sum_weight)
    for index,i in enumerate(fish_weight_table['new_sum_weight_list']):
        if i>random_num:
            return fish_weight_table['star'][index]

def random_num_max(num,add_num=0):
    max_weight=0
    for i in range(num):
        result=random_with_weight()+add_num
        if result>max_weight:
            max_weight=result
    return max_weight

def random_num_max_list(num1,num2,add_num=0):
    result_list=[]
    for i in range(num1):
        result_list.append(random_num_max(num2,add_num))
    return numpy.mean(result_list),result_list


final_tables=[
    [10,0],
    [20,50],
    [50,100],
    [100,150],
    [200,200],
    [500,250],
    [1000,300],
    [2000,350]
]

start_power=10000
test_times=50

print("每次消耗:",start_power,"体力,每组试验次数:",test_times)
for i in final_tables:
    fish_num=int(start_power/i[0])
    add_num=i[1]
    print(i[0],"体力：",random_num_max_list(test_times,fish_num,add_num))

