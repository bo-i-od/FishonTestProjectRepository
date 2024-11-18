import copy
# from statistics.battle_cal.my_wheel import Wheel
from tabulate import tabulate
from get_skill_list import *
from statistics.new_battle_cal.actor.actor_player import Player
from statistics.new_battle_cal.actor.actor_fish import Fish
from statistics.new_battle_cal.battle_common import BattleCommon


# ----------初始化各项参数 ----------------
fish_object = Fish()
player_object = Player()
# 张力
now_tension = BattleCommon.start_tension  # 当前张力
rod_tension_status = 'reel'
# 剩余时间
now_skill_left_time=0
per_time=200 # 每per_time毫秒执行一次
cal_damage_per_time=200 # 每cal_damage_per_time毫秒计算一次伤害
# 距离，单位米
fish_line_distance = BattleCommon.start_line
# 当前鱼技能
now_skill=None
fish_skill_info=None
fish_skill_list=[]
# 时间
now_time = 0
# 总伤害
total_damage = 0

result=[]
print("时间 鱼状态  人爆气   距离    鱼速度 人拉力  实际跑速  累计伤害   dps   人buff  鱼buff")
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
        # 初始化
        if len(fish_skill_list)==0:
            fish_skill_list = copy.deepcopy(skill_list)
        now_skill = fish_skill_list.pop(0)  # 下个技能
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
    # 爆气状态维护
    if player_object.ultimate_status:
        player_object.ultimate_left_time -= per_time
        if player_object.ultimate_left_time<=0:
            player_object.ultimate_status = False
    if player_object.energy>=3 and not player_object.ultimate_status:
        player_object.energy-=3
        player_object.ultimate_status = True
        player_object.ultimate_left_time = 2000

    # 张力 行为变化
    if player_object.ultimate_status:
        rod_tension_status = 'reel'
    else:
        if now_tension >= BattleCommon.tension_max:
            rod_tension_status = 'not_reel'
        if now_tension <= BattleCommon.tension_min:
            rod_tension_status = 'reel'

    if not player_object.ultimate_status:
        # 爆气时张力不变
        if rod_tension_status=='reel':
            now_tension += player_object.get_BattleTensionUpSpeed(fish_object) * per_time/1000
        elif rod_tension_status=='not_reel':
            now_tension += player_object.get_BattleTensionDownSpeed(fish_object) * per_time/1000

    if rod_tension_status == 'reel':
        do_damage = player_object.get_final_damage(fish_object,now_tension) * per_time/cal_damage_per_time
    else:
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
        # 计算DPS        
        total_time_seconds = now_time / 1000  # 总时间（秒）
        dps = total_damage / total_time_seconds
        result.append([int(now_time/1000), now_skill,player_object.ultimate_status,int(fish_line_distance), int(fish_velocityZ), int(player_velocityZ), int(now_velocityZ),int(total_damage),dps,list(player_object.buff_dict.keys()),list(fish_object.buff_dict.keys())])

print(tabulate(result))

