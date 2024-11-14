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
    CUT_LINE:{TIMEMS:3000},
    RUSH:{TIMEMS:3000,BUFF_LIST:[200001]},
    ESCAPE:{TIMEMS:3000,BUFF_LIST:[200001],COUNTER_TIME:1000},
    JUMP:{TIMEMS:2500}
}
fish_random_skill_list=[CUT_LINE,RUSH,ESCAPE,JUMP]

now_skill=FISH_SWIM
skill_list=[now_skill]
for i in range(50):
    if now_skill==FISH_SWIM:
        now_skill=random.choice(fish_random_skill_list)
    else:
        now_skill=FISH_SWIM
    skill_list.append(now_skill)

skill_list=['swim', 'jump', 'swim', 'jump', 'swim', 'cut_line', 'swim', 'rush', 'swim', 'escape', 'swim', 'rush', 'swim', 'escape', 'swim', 'rush', 'swim', 'cut_line', 'swim', 'escape', 'swim', 'jump', 'swim', 'jump', 'swim', 'escape', 'swim', 'rush', 'swim', 'rush', 'swim', 'cut_line', 'swim', 'jump', 'swim', 'jump', 'swim', 'jump', 'swim', 'escape', 'swim', 'rush', 'swim', 'escape', 'swim', 'jump', 'swim', 'jump', 'swim', 'jump', 'swim']

# print(skill_list)




# new_list= [JUMP,ESCAPE,RUSH,JUMP,CUT_LINE,JUMP,RUSH,ESCAPE,CUT_LINE,CUT_LINE,RUSH]
# new_skill_list=[FISH_SWIM]
#
# for i in range(20):
#     if now_skill==FISH_SWIM:
#         now_skill=new_list.pop(0)
#     else:
#         now_skill=FISH_SWIM
#     new_skill_list.append(now_skill)
# print(new_skill_list)


# 鱼行为：
# 中立：游、
# 负向：冲、成长、切线、叠怒气
# 正向：弹反、QTE
# 终结技：狂暴（叠满怒气）、或疯狂切线
#
# 人：
# 弹反： 伤害、拉回、   （可能）破弱点
# QTE:  伤害、集气、  （可能）破弱点
# 爆气：击杀
# 破弱点达到x层：击杀


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



