numbers=[]
data = []
with open("C:/Users/TU/desktop/log.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        items = tuple(line.strip().split())
        data.append(items)
        numbers.append(int(items[0]))
total_num=len(numbers)

def init_list(num):
    return [[0,[]] for i in range(num)]
boss_num=init_list(3)# rare\elite\monster
yugu_num=init_list(2)
yugu_gold=init_list(2)
def update_list(target_list,list_index,num):
    target_list[list_index][0]+=1
    target_list[list_index][1].append(num)


for index,i in enumerate(numbers):
    i_num = i % 10
    if i>391000:
        if i_num in [1,2]:
            yugu_index=0
        elif i_num in [3,4]:
            yugu_index=1
        else:
            print("error")
        update_list(yugu_num, yugu_index, index)
    elif 391000>i>390000:
        if i_num in [5,6]:
            boss_index=2
        elif i_num in [3,4]:
            boss_index=1
        elif i_num in [1,2]:
            boss_index=0
        else:
            print("error")
        update_list(boss_num,boss_index,index)
    elif 380000>i>370000:
        if i_num in [1,2]:
            yugu_index=0
        elif i_num in [3,4]:
            yugu_index=1
        else:
            print("error")
        update_list(yugu_gold,yugu_index,index)

def print_list(target_list,title=""):
    print("=====",title,"=====")
    for i in target_list:
        print(i)

print("钓鱼次数：",total_num)
print_list(boss_num,"rare,elite,monster 掉落数量和时机")
print_list(yugu_num,"elite、monster鱼骨 掉落数量和时机")
print_list(yugu_gold,"金色elite、monster鱼骨 掉落数量和时机")