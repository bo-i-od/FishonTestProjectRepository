import random
from statistics.new_battle_cal.fish_ai.fish_command import FishCommand




ActionUnitA = [
    FishCommand.EXAMPLE_SWIM,
    random.choices([FishCommand.EXAMPLE_QTE,FishCommand.EXAMPLE_JUMP],weights=[50,50])[0],
    FishCommand.EXAMPLE_SWIM,
]

ActionUnitB = [
    FishCommand.EXAMPLE_QTE,
    FishCommand.EXAMPLE_RUSH,
    FishCommand.EXAMPLE_SWIM,
]

ActionUnitC = [
    FishCommand.EXAMPLE_QTE,
    random.choices([FishCommand.EXAMPLE_ACCUMULATING, FishCommand.EXAMPLE_PLAY_DEAD], weights=[80, 20])[0],
    FishCommand.EXAMPLE_FRENZY,
    FishCommand.EXAMPLE_SWIM,
]

DefaultUnitGroup=[
    ActionUnitA,
    ActionUnitA,
    ActionUnitA,
    random.choices([ActionUnitB,ActionUnitC], weights=[50, 50])[0],
]

def shuffle(lst):
    rt = lst[:]
    n = len(rt)
    # 从第二个物品开始洗牌（index 为 1）
    for i in range(n-1, 1, -1):
        # 生成 1 到 i 之间的随机数（注意 i 的下标在 Python 中是包含上限的）
        j = random.randint(1, i)
        # 交换 rt[i] 和 rt[j]
        rt[i], rt[j] = rt[j], rt[i]
    return rt

skill_list=[]
for i in range(10):
    skill_group=shuffle(DefaultUnitGroup)
    for j in skill_group:
        for k in j:
            skill_list.append(k())


print(skill_list)





# fish_skill_data={
#     FISH_SWIM:{TIMEMS:1000},
#     CUT_LINE:{TIMEMS:3000,COUNTER_TIME:1000},
#     RUSH:{TIMEMS:3000,BUFF_LIST:[200001]},
#     ESCAPE:{TIMEMS:3000,BUFF_LIST:[200001],COUNTER_TIME:1000},
#     JUMP:{TIMEMS:2500}
# }

# skill_list 运行到最后一个后，会重新循环
# skill_list=['swim', 'jump','jump','swim','escape','swim','jump','rush']

#  以下内容暂时无视
if __name__ == '__main__':
    a="'swim'"
    b="'lache1'"
    c="'lache2'"
    for i in range(10):
        test1=random.randint(3, 10)*1000
        test2=random.randint(3, 8)*1000
        skill1=a
        skill2=b if random.random()<0.8 else c
        print("{",skill1,',',test1,'},\n{',skill2,',',test2,'},')

