S=1
M=2
L=3
H=4
B=5
Rare=11
Elite=12
Monster=13

def load_file():
    """读桌面 txt"""
    numbers = []
    data = []
    with open("C:/Users/TU/desktop/log.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            items = tuple(line.strip().split())
            if items:
                data.append(items)
                numbers.append(int(items[0]))
    return numbers

def get_fish_type(fish_id):
    """根据id最后1-2位确定fish类型，注：洪湖 和 最后两个渔场 少鱼，类型对不上！！！"""
    fish_num = fish_id %10
    fish_size=""
    fish_type="fish"

    if fish_id <370000:
        fish_num = fish_id % 100
        if fish_num in [1,2,3,4]:
            fish_size="Small"
        elif fish_num in [5,6,7,8]:
            fish_size="Median"
        elif fish_num in [9,10,11,12]:
            fish_size="Large"
        elif fish_num in [13,14]:
            fish_size="Huge"
        elif fish_num in [15]:
            fish_size="Giant"
    elif 380000>fish_id>370000:
        fish_type = "gold_yugu"
        if fish_num in [1,2]:
            fish_size="Elite"
        elif fish_num in [3,4]:
            fish_size="Monster"
    elif fish_id>391000:
        fish_type = "yugu"
        if fish_num in [1,2]:
            fish_size="Elite"
        elif fish_num in [3,4]:
            fish_size="Monster"
    elif 391000>fish_id>390000:
        fish_type='boss'
        if fish_num in [5,6]:
            fish_size="Monster"
        elif fish_num in [3,4]:
            fish_size="Elite"
        elif fish_num in [1,2]:
            fish_size="Rare"

    return {'fish_size':fish_size,'fish_type':fish_type}

def statistic_fish_size(numbers):
    """统计每种鱼出的数量"""
    count = {}
    for i in numbers:
        fish_result=get_fish_type(i)
        if fish_result['fish_type'] in ['fish','boss']:
            fish_size=fish_result['fish_size']
            count.setdefault(fish_size,0)
            count[fish_size]+=1
    return count

if __name__ == '__main__':
    # 测试
    numbers=load_file()
    count=statistic_fish_size(numbers)
    print(len(numbers),count)