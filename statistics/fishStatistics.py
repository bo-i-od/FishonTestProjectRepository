from base_func import *
from load_log import load_log

data = load_log('hook_log.txt')
numbers = []
for i in data:
    if i['fish_id']:
        numbers.append(int(i['fish_id']))

def init_list(num):
    return [[0,[]] for i in range(num)]
boss_num=init_list(3)# rare\elite\monster
yugu_num=init_list(2)
yugu_gold=init_list(2)
def update_list(target_list,list_index,num):
    target_list[list_index][0]+=1
    target_list[list_index][1].append(num)


for index,i in enumerate(numbers):
    fish_result=get_fish_type(i)
    if fish_result['fish_type']=='yugu':
        yugu_index= ['Elite','Monster'].index(fish_result['fish_size'])
        update_list(yugu_num, yugu_index, index)
    elif fish_result['fish_type']=='gold_yugu':
        gold_yugu_index= ['Elite','Monster'].index(fish_result['fish_size'])
        update_list(yugu_gold, gold_yugu_index, index)
    elif fish_result['fish_type']=='boss':
        boss_index = ['Rare','Elite','Monster'].index(fish_result['fish_size'])
        update_list(boss_num, boss_index, index)



def print_list(target_list,title=""):
    print("=====",title,"=====")
    for i in target_list:
        print(i)
print("钓鱼次数：",len(numbers))
print_list(boss_num,"rare,elite,monster 掉落数量和时机")
print_list(yugu_num,"elite、monster鱼骨 掉落数量和时机")
print_list(yugu_gold,"金色elite、monster鱼骨 掉落数量和时机")


count=statistic_fish_size(numbers)
print("完整鱼货统计：")
print(len(numbers),count)