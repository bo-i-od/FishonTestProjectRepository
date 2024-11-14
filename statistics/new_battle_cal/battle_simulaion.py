import random
import pandas as pd
from statistics.battle_cal.my_wheel import Wheel
from tabulate import tabulate
from get_skill_list import *
from player import Player
from fish import Fish

class BattleCommon:
    # 张力条总长度
    tension_total_max=10000
    # 张力条到极限，开始松手
    tension_max=9000
    tension_min=8000

    # 初始鱼线位置
    start_line=20
    # 初始张力条位置
    start_tension=4000

    @classmethod
    def cal_tension_atk_rate(cls,tension_now):
        """ 张力伤害计算公式 """
        rate = tension_now / cls.tension_total_max
        if rate > 0.8:
            return 1
        elif rate > 0.6:
            return 0.85
        elif rate > 0.3:
            return 0.55
        else:
            return 0.25


# ----------初始化各项参数 ----------------
fish_object = Fish()
player_object = Player()
# 张力
now_tension = BattleCommon.start_tension  # 当前张力
rod_tension_status = 'reel'
# 剩余时间
now_skill_left_time=0
per_time=200 # 每0.2秒执行一次
# 距离，单位米
fish_line_distance = BattleCommon.start_line
# 当前鱼技能
now_skill=None
fish_skill_info=None
# 时间
now_time = 0
# 总伤害
total_damage = 0

result=[]
print("时间 状态     距离    鱼速度 人拉力  实际跑速  累计伤害   人buff  鱼buff")
#result.append(["时间","距离","状态","鱼速度","人拉力","实际跑速","累计伤害"])

for i in range(200):
    # check buff是否过期
    fish_object.check_and_remove_buff(now_time)
    player_object.check_and_remove_buff(now_time)

    # 需要放下一个技能了
    if now_skill_left_time <= 0:
        # 技能结束移除技能buff
        if fish_skill_info and BUFF_LIST in fish_skill_info:
            buff_id = fish_skill_info[BUFF_LIST][0]
            fish_object.remove_buff(buff_id)

        now_skill = skill_list.pop(0)  # 下个技能
        fish_skill_info = fish_skill_data[now_skill]
        if BUFF_LIST in fish_skill_info:
            buff_id=fish_skill_info[BUFF_LIST][0]
            fish_object.add_buff(buff_id,now_time)

        now_skill_left_time=fish_skill_info[TIMEMS]

        # 如果是QTE，还额外触发一次QTE
        if now_skill==JUMP:
            player_object.energy+=1
            # QTE触发技能
            # player_object.add_buff(200003, now_time)
            # if random.random()<0.67:
            #     player_object.add_buff(200003,now_time)
            # else:
            #     player_object.add_buff(200004,now_time)

    # 可弹反
    if COUNTER_TIME in fish_skill_info:
        # 到了时间
        if now_skill_left_time == (fish_skill_info[TIMEMS]-fish_skill_info[COUNTER_TIME]):
            # 有气
            if player_object.energy>=1:
                player_object.energy -= 1
                # 打断
                now_skill_left_time = 0
                # 弹反加buff
                # player_object.add_buff(200006, now_time)

    # 张力 行为变化
    if now_tension >= BattleCommon.tension_max:
        rod_tension_status = 'not_reel'
    if now_tension <= BattleCommon.tension_min:
        rod_tension_status = 'reel'

    if rod_tension_status=='reel':

        now_tension += player_object.rod_tension_increase * per_time/1000
        # # 根据鱼距离判断加buff
        # if fish_line_distance<=20:
        #     fish_object.add_buff(200010,now_time)
        # else:
        #     fish_object.remove_buff(200010)
        # 实际造成伤害,  基础攻击* 张力系数 * buff系数
        do_damage = player_object.atk * BattleCommon.cal_tension_atk_rate(now_tension) * (1000 + player_object.damage_rate - fish_object.damage_rate)/1000

    elif rod_tension_status=='not_reel':
        now_tension += player_object.rod_tension_decrease * per_time/1000

        do_damage = 0

    player_velocityZ = player_object.get_current_velocityZ(rod_tension_status)
    fish_velocityZ=fish_object.get_current_velocityZ()
    now_velocityZ = fish_velocityZ-player_velocityZ
    # 鱼跑远
    fish_line_distance += now_velocityZ/1000 * per_time/1000
    # 累计伤害
    total_damage += do_damage

    now_skill_left_time -= per_time
    now_time += per_time

    if now_time%1000==0:
        result.append([int(now_time/1000), now_skill,int(fish_line_distance), int(fish_velocityZ), int(player_velocityZ), int(now_velocityZ),int(total_damage),list(player_object.buff_dict.keys()),list(fish_object.buff_dict.keys())])

print(tabulate(result))

