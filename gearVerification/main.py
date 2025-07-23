import re


from gearVerification.blackboard import Blackboard
from gearVerification.formula import formula_main, get_time_extension_temp, get_time_extension_result
from gearVerification.trigger import Trigger
import builtins

def format_floats(obj, decimals=2):
    """递归格式化对象中的所有float为指定小数位数"""
    if isinstance(obj, float):
        return round(obj, decimals)
    elif isinstance(obj, (list, tuple)):
        return [format_floats(item, decimals) for item in obj]
    elif isinstance(obj, dict):
        return {k: format_floats(v, decimals) for k, v in obj.items()}
    else:
        return obj

def print_round(*args, **kwargs):
    """自定义print函数，自动格式化float"""
    formatted_args = []
    for arg in args:
        if isinstance(arg, str):
            # 使用正则表达式找到并替换字符串中的float
            def replace_float(match):
                num = float(match.group())
                return f"{num:.2f}"

            # 匹配float格式的数字
            arg = re.sub(r'\b\d+\.\d+\b', replace_float, arg)
            formatted_args.append(arg)
        elif isinstance(arg, float):
            formatted_args.append(f"{arg:.2f}")
        else:
            formatted_args.append(format_floats(arg))

    builtins.print(*formatted_args, **kwargs)


def main():
    # 1力 2敏 3智
    battle_tag = 1

    # 使用skill_power_init表中sortId多少的环境
    skill_power_init_id = 1

    # skill_power表
    skill_id_list = [17000155, 17000205]

    # 获取skill_power_init_id战斗环境下无技能的黑板
    bb_without_skill = Blackboard(battle_tag=battle_tag, skill_power_init_id=skill_power_init_id)

    # 初始化trigger读取黑板上的变量，然后把变量放入trigger触发得到结果
    trigger = Trigger(bb=bb_without_skill)
    trigger.run_trigger()

    # 获取有技能运行后的黑板
    bb = Blackboard(battle_tag=battle_tag, skill_power_init_id=skill_power_init_id)

    # 初始化trigger读取黑板上的变量，生成额外技能的trigger，然后把变量放入trigger触发得到结果
    trigger = Trigger(bb=bb)
    trigger.generate_trigger(skill_id_list=skill_id_list)
    trigger.run_trigger()

    print("===============预估战斗过程数据===============")
    print_round("count_counter:", bb.count_counter)
    print_round("count_qte:", bb.count_qte)
    print_round("count_ult:", bb.count_ult)
    print_round("count_energy:", bb.count_energy)
    print_round("count_exhausted:", bb.count_exhausted)
    print_round("count_dizzy:", bb.count_dizzy)
    print_round("count_skill:", bb.count_skill)
    print_round("count_customize:", bb.count_customize)
    print_round("time_exhausted:", bb.time_exhausted)
    print_round("time_dizzy:", bb.time_dizzy)

    # 计算无技能和有技能的攻击次数、爆气次数、气绝总时长、眩晕总时长的差值
    count_attack_delta = bb.count_attack - bb_without_skill.count_attack
    count_ult_delta = bb.count_ult - bb_without_skill.count_ult
    time_exhausted_delta = bb.time_exhausted -bb_without_skill.time_exhausted
    time_dizzy_delta = bb.time_dizzy - bb_without_skill.time_dizzy
    print("===============预估提升数据===============")
    print_round("count_attack_delta:", count_attack_delta)
    print_round("count_ult_delta:", count_ult_delta)
    print_round("time_exhausted_delta:", time_exhausted_delta)
    print_round("time_dizzy_delta:", time_dizzy_delta)

    # 攻击次数、爆气、气绝、眩晕影响伤害加成和战斗时长
    bb.Formula.damage_increased_args_list.append({"arg1": f"{count_attack_delta/bb_without_skill.count_attack}", "arg2": f"{bb_without_skill.battle_time}", "count": 1})
    bb.Formula.damage_once_args_list.append({"arg1": f"{count_ult_delta}*modifier_ult*duration_ult/attack_interval_ult", "count": 1})
    bb.Formula.speed_change_args_list.append({"arg1": "speed_modifier_ult-1", "arg2": f"{count_ult_delta}*duration_ult", "count": 1, "object": 1})
    bb.Formula.speed_change_args_list.append({"arg1": f"{bb.fish_speed_down_factor_in_control}", "arg2": f"{time_exhausted_delta}", "count": 1, "object": 2})
    bb.Formula.speed_change_args_list.append({"arg1": f"{bb.fish_speed_down_factor_in_control}", "arg2": f"{time_dizzy_delta}", "count": 1, "object": 2})
    bb.Formula.damage_increased_args_list.append({"arg1": "0.2", "arg2": f"{time_exhausted_delta}", "count": 1})

    # 运行整体公式
    print("===============预估加成结果===============")
    formula_main(bb)



if __name__ == '__main__':
    main()
