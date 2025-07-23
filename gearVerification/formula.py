from configs.pathConfig import EXCEL_PATH
from gearVerification.blackboard import Blackboard
from tools.excelRead import ExcelTools
import re


class ParseError(Exception):
    pass


# 克制伤害加成
def formula_restrain_bonus(bb: Blackboard):
    bonus = 0
    excel_tool = ExcelTools(EXCEL_PATH)
    adv_gear_fishing_gear_detail = excel_tool.get_table_data_detail(book_name="ADV_GEAR_FISHING_GEAR.xlsm")
    adv_gear_fishing_rod_detail = excel_tool.get_table_data_detail(book_name="ADV_GEAR_FISHING_ROD.xlsm")
    for gear_id in bb.gear_id_list:
        json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="tpId", value=gear_id, table_data_detail=adv_gear_fishing_gear_detail)
        if not json_object_list:
            json_object_list = excel_tool.get_table_data_object_list_by_key_value(key="tpId", value=gear_id, table_data_detail=adv_gear_fishing_rod_detail)
        if not json_object_list:
            continue
        json_object = json_object_list[0]
        if bb.battle_tag != json_object["counterType"]:
            continue
        bonus += 0.1
    print(f"克制伤害加成：{bonus:.2f}")
    return bonus


# 刺鱼伤害加成
def formula_hook_damage_bonus(bb: Blackboard):
    bonus = 0
    for damage_hook_extend_args in bb.Formula.damage_hook_extend_args_list:
        arg1 = arg_to_value(bb, arg=damage_hook_extend_args["arg1"])
        bonus += arg1
    print(f"刺鱼加成：{bonus:.2f}")
    return bonus


# 增伤伤害加成
def formula_damage_increased_bonus(bb: Blackboard):
    bonus = 0
    for damage_increased_args in bb.Formula.damage_increased_args_list:
        arg1 = arg_to_value(bb, arg=damage_increased_args["arg1"])
        arg2 = arg_to_value(bb, arg=damage_increased_args["arg2"])
        if arg2 is None:
            arg2 = 1
        count = damage_increased_args["count"]
        bonus += count * arg1 * arg2 / bb.battle_time

    print(f"增伤伤害加成：{bonus:.2f}")
    return bonus


# 一次性伤害加成
def formula_damage_once_bonus(bb: Blackboard):
    bonus = 0
    for damage_once_args in bb.Formula.damage_once_args_list:
        arg1 = arg_to_value(bb, arg=damage_once_args["arg1"])
        count = damage_once_args["count"]
        bonus += count * arg1 / bb.damage_modifier
    print(f"一次性伤害加成：{bonus:.2f}")
    return bonus


# 战斗时间延长加成
def formula_battle_extend_bonus(bb: Blackboard):
    bonus = get_time_extension_result(bb=bb) / bb.battle_time
    print(f"战斗时间延长加成：{bonus:.2f}")
    return bonus


def formula_main(bb: Blackboard):
    bonus = (1 + formula_restrain_bonus(bb)) * ((1 + formula_damage_increased_bonus(bb)) * (1 + formula_damage_once_bonus(bb)) * (1 + formula_battle_extend_bonus(bb)) + formula_hook_damage_bonus(bb)) - 1
    print(f"总体伤害加成：{bonus:.2f}")
    return bonus


def parse_expression(bb, expr: str):
    # 移除空格
    expr = expr.replace(" ", "")

    # 解析表达式
    value, remaining = parse_add_sub(bb, expr)

    # 如果还有剩余字符，说明解析不完整
    if remaining:
        raise ParseError(f"无法解析的表达式部分: '{remaining}'")

    return value


def parse_add_sub(bb, expr: str):
    """
    解析加减表达式（最低优先级）
    expression ::= term { ('+' | '-') term }
    """
    # 先解析第一个项
    value, remaining = parse_term(bb, expr)

    # 循环处理后续的加减操作
    while remaining and remaining[0] in ['+', '-']:
        op_char = remaining[0]
        term_value, remaining = parse_term(bb, remaining[1:])

        if op_char == '+':
            value += term_value
        else:  # op_char == '-'
            value -= term_value

    return value, remaining


def parse_term(bb, expr: str):
    """
    解析乘除表达式（中等优先级）
    term ::= factor { ('*' | '/') factor }
    """
    # 先解析第一个因子
    value, remaining = parse_factor(bb, expr)

    # 循环处理后续的乘除操作
    while remaining and remaining[0] in ['*', '/']:
        op_char = remaining[0]
        factor_value, remaining = parse_factor(bb, remaining[1:])

        if op_char == '*':
            value *= factor_value
        else:  # op_char == '/'
            try:
                value /= factor_value
            except ZeroDivisionError:
                raise ParseError("除以零错误")

    return value, remaining


def parse_factor(bb, expr: str):
    """
    解析因子（最高优先级）
    factor ::= number | variable | '(' expression ')' | unary_op factor
    unary_op ::= '+' | '-'
    """
    # 处理一元运算符
    sign = 1
    while expr and expr[0] in ['+', '-']:
        if expr[0] == '-':
            sign *= -1  # 每次负号改变符号
        expr = expr[1:]  # 移除操作符

    # 解析数字
    if expr[0].isdigit() or expr[0] == '.':
        value, remaining = parse_number(bb, expr)
        return sign * value, remaining

    # 解析变量
    if expr[0].isalpha() or expr[0] == '_':
        value, remaining = parse_variable(bb, expr)
        return sign * value, remaining

    # 解析括号表达式
    if expr[0] == '(':
        # 跳过左括号
        expr = expr[1:]
        # 解析括号内的表达式
        value, remaining = parse_add_sub(bb, expr)
        # 确保右括号存在
        if not remaining or remaining[0] != ')':
            raise ParseError("缺少右括号")
        # 跳过右括号
        remaining = remaining[1:]
        return sign * value, remaining

    raise ParseError(f"无法解析的字符: '{expr[0]}'")




def parse_number(bb, expr: str):
    """
    解析数字（整数或浮点数）
    """
    # 匹配数字模式（支持整数和小数）
    match = re.match(r"[-+]?(\d+(\.\d*)?|\.\d+)", expr)
    if not match:
        raise ParseError(f"无效的数字: '{expr}'")

    number_str = match.group(0)
    try:
        return float(number_str), expr[len(number_str):]
    except ValueError:
        raise ParseError(f"无效的数字格式: '{number_str}'")


def parse_variable(bb, expr: str):
    """
    解析变量名
    """
    # 匹配变量名模式（字母、数字、下划线，但不能以数字开头）
    match = re.match(r"[\u4e00-\u9fffa-zA-Z_][\u4e00-\u9fffa-zA-Z0-9_]*", expr)
    if not match:
        raise ParseError(f"无效的变量名: '{expr}'")

    var_name = match.group(0)
    try:
        value = bb.get_variable(var_name)
        return value, expr[len(var_name):]
    except KeyError:
        raise ParseError(f"未定义的变量: '{var_name}'")


def arg_to_value(bb, arg):
    """
    主函数，调用解析器并处理异常
    """
    if arg is None:
        return arg
    if type(arg) in [int, float]:
        return arg
    try:
        return parse_expression(bb, arg)
    except ParseError as e:
        raise ValueError(f"表达式解析错误: {str(e)} 表达式: '{arg}'") from e



def get_time_extension_temp(bb: Blackboard, buff_value):
    rounds = 0
    normalized_remaining_line_pre = buff_value * 0.82/0.12
    while True:
        normalized_remaining_line = normalized_remaining_line_pre - 5 / 0.12 / bb.battle_time * (0.82 * (1 + 0.06 * (rounds + 1)) * (1 - buff_value) - 0.7)
        if normalized_remaining_line < 0:
            break
        normalized_remaining_line_pre = normalized_remaining_line
        rounds += 1
    time_extension = rounds * 5 + normalized_remaining_line_pre * 0.12 * bb.battle_time / (0.82 * (1 + 0.06 * (rounds + 1)) * (1 - buff_value) - 0.7)
    return time_extension

def get_fish_speed_down_factor_from_player_speed_up(bb: Blackboard, time_extension):
    rounds = time_extension // 5
    remaining_time = time_extension - rounds * 5
    k = 5 * (1 + rounds) * (rounds / 2 + remaining_time) / bb.battle_time
    return k

def get_time_extension_result(bb: Blackboard):
    fish_speed_down = 0
    player_speed_up = 0
    for speed_change_args in bb.Formula.speed_change_args_list:
        arg1 = arg_to_value(bb, arg=speed_change_args["arg1"])
        arg2 = arg_to_value(bb, arg=speed_change_args["arg2"])
        if arg2 is None:
            arg2 = 1
        count = speed_change_args["count"]
        target_object = speed_change_args["object"]
        speed = arg1 * arg2 * count
        if target_object == 1:
            player_speed_up += speed
        if target_object == 2:
            fish_speed_down += speed
    player_speed_up_ave = player_speed_up / bb.battle_time
    fish_speed_down_ave = fish_speed_down / bb.battle_time
    fish_speed_down_factor = 1
    time_extension = 0
    cur = 0
    while cur < 10:
        fish_speed_down_ave_from_player_speed_up_ave = 0.7 / 0.82 * player_speed_up_ave / (1 + 0.06 *fish_speed_down_factor)
        time_extension = get_time_extension_temp(bb=bb, buff_value=fish_speed_down_ave_from_player_speed_up_ave + fish_speed_down_ave)
        fish_speed_down_factor = get_fish_speed_down_factor_from_player_speed_up(bb=bb, time_extension=time_extension)
        cur += 1
    return time_extension















