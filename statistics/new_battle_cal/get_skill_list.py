import random

FISH_SWIM='swim'
CUT_LINE='cut_line'
RUSH='rush'
ESCAPE='escape'
JUMP='jump'
TIMEMS='time'
BUFF_LIST='buff_list'
COUNTER_TIME='canCounterTimingMS'

fish_skill_data={
    FISH_SWIM:{TIMEMS:1000},
    CUT_LINE:{TIMEMS:3000,COUNTER_TIME:1000},
    RUSH:{TIMEMS:3000,BUFF_LIST:[200001]},
    ESCAPE:{TIMEMS:3000,BUFF_LIST:[200001],COUNTER_TIME:1000},
    JUMP:{TIMEMS:2500}
}

# skill_list 运行到最后一个后，会重新循环
skill_list=['swim', 'jump','swim','escape','swim','rush']

if __name__ == '__main__':
    # fish_random_skill_list=[CUT_LINE,RUSH,ESCAPE,JUMP]
    #
    # now_skill=FISH_SWIM
    # skill_list=[now_skill]
    # for i in range(50):
    #     if now_skill==FISH_SWIM:
    #         now_skill=random.choice(fish_random_skill_list)
    #     else:
    #         now_skill=FISH_SWIM
    #     skill_list.append(now_skill)
    a="'swim'"
    b="'lache1'"
    c="'lache2'"
    for i in range(10):
        test1=random.randint(3, 10)*1000
        test2=random.randint(3, 8)*1000
        skill1=a
        skill2=b if random.random()<0.8 else c
        print("{",skill1,',',test1,'},\n{',skill2,',',test2,'},')



