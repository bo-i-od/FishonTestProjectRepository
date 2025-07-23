from activities.decl.SKILL_POWER_INIT import SKILL_POWER_INIT
from configs.pathConfig import EXCEL_PATH
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelTools


class Blackboard:
    def __init__(self, battle_tag, skill_power_init_id):
        self.excel_tool = ExcelTools(EXCEL_PATH)
        skill_power_init: SKILL_POWER_INIT
        skill_power_init =json_to_instance(json_object=self.excel_tool.get_table_data_object_by_key_value(key="sortId", value=skill_power_init_id, book_name="SKILL_POWER_INIT.xlsm"), cls=SKILL_POWER_INIT)
        self.battle_tag = battle_tag
        self.restrain = skill_power_init.restrain
        self.battle_damage = skill_power_init.battle_damage
        self.attack_interval = skill_power_init.attack_interval
        self.attack_interval_ult = skill_power_init.attack_interval_ult
        self.damage_modifier_ult = skill_power_init.damage_modifier_ult
        self.duration_ult = skill_power_init.duration_ult
        self.speed_modifier_ult = skill_power_init.speed_modifier_ult
        self.duration_exhausted = skill_power_init.duration_exhausted
        self.time_exhausted = 0
        self.duration_dizzy = skill_power_init.duration_dizzy
        self.time_dizzy = 0
        battle_parameter_estimate = skill_power_init.battle_parameter_estimate[battle_tag - 1]
        self.battle_parameter_estimate = battle_parameter_estimate
        self.hp_factor = battle_parameter_estimate.hp_factor
        self.battle_time = battle_parameter_estimate.battle_time
        self.battle_time_extend = 0
        self.fish_speed_down_factor_in_control = battle_parameter_estimate.fish_speed_down_factor_in_control
        self.count_qte_special = battle_parameter_estimate.ratio_qte_special * battle_parameter_estimate.count_qte
        self.count_qte_jump = battle_parameter_estimate.ratio_qte_jump * battle_parameter_estimate.count_qte
        self.count_qte_in_combo = battle_parameter_estimate.ratio_qte_in_combo * battle_parameter_estimate.count_qte
        self.count_qte = 0
        self.count_energy = 0
        self.count_counter = 0
        self.count_oppress = 0
        self.count_skill = 0
        self.count_ult = 0
        self.count_exhausted = 0
        self.count_dizzy = 0
        self.count_attack = 0
        self.damage_modifier = self.hp_factor * skill_power_init.fish_base_hp * self.attack_interval / self.battle_damage
        self.damage_hook = 1.5 / self.damage_modifier
        self.count_start = 1

        self.gear_id_list = []

        self.count_customize = {}
        self.name_to_variable = {
            "克制加成": self.restrain,
            "restrain": self.restrain,
            "攻击间隔": self.attack_interval,
            "attack_interval": self.attack_interval,
            "攻击速度": 1 / self.attack_interval,
            "attack_speed": 1 / self.attack_interval,
            "爆气攻击间隔": self.attack_interval_ult,
            "attack_interval_ult": self.attack_interval_ult,
            "爆气伤害系数": self.damage_modifier_ult,
            "modifier_ult": self.damage_modifier_ult,
            "爆气收线加成": self.speed_modifier_ult,
            "speed_modifier_ult": self.speed_modifier_ult,
            "爆气时长": self.duration_ult,
            "duration_ult": self.duration_ult,
            "气绝时长": self.duration_exhausted,
            "duration_exhausted": self.duration_exhausted,
            "气绝总时长": self.time_exhausted,
            "time_exhausted": self.time_exhausted,
            "眩晕时长": self.duration_dizzy,
            "duration_dizzy": self.duration_dizzy,
            "眩晕总时长": self.time_dizzy,
            "time_dizzy": self.time_dizzy,
            "战斗时长": self.battle_time,
            "battle_time": self.battle_time,
            "特殊QTE数量": self.count_qte_special,
            "count_qte_special": self.count_qte_special,
            "鱼跃QTE数量": self.count_qte_jump,
            "count_qte_jump": self.count_qte_jump,
            "连招内QTE数量": self.count_qte_in_combo,
            "count_qte_in_combo": self.count_qte_in_combo,
            "QTE数量": self.count_qte,
            "count_qte": self.count_qte,
            "气数量": self.count_energy,
            "count_energy": self.count_energy,
            "弹反数量": self.count_counter,
            "count_counter": self.count_counter,
            "压制数量": self.count_oppress,
            "count_oppress": self.count_oppress,
            "技能数量": self.count_skill,
            "count_skill": self.count_skill,
            "爆气数量": self.count_ult,
            "count_ult": self.count_ult,
            "气绝数量": self.count_exhausted,
            "count_exhausted": self.count_exhausted,
            "眩晕数量": self.count_dizzy,
            "count_dizzy": self.count_dizzy,
            "常规伤害倍率": self.damage_modifier,
            "damage_modifier": self.damage_modifier,
            "默认刺鱼伤害": self.damage_hook,
            "damage_hook": self.damage_hook,
        }

    class Formula:
        damage_once_args_list = []
        damage_increased_args_list = []
        damage_hook_extend_args_list = []
        speed_change_args_list = []

    def get_variable(self, name):
        if "自定义" in name:
            return self.count_customize[name]
        return self.name_to_variable[name]

    def set_variable(self, name, value):
        # 找到对应的属性并设置值
        if name in ["攻击间隔", "attack_interval"]:
            self.attack_interval = value
            # 同时更新攻击速度
            self.name_to_variable["攻击速度"] = 1 / value
            self.name_to_variable["attack_speed"] = 1 / value
            return
        if name in ["攻击速度", "attack_speed"]:
            self.attack_speed = value
            # 同时更新攻击速度
            self.name_to_variable["攻击间隔"] = 1 / value
            self.name_to_variable["attack_interval"] = 1 / value
            return
        if name in ["爆气攻击间隔", "attack_interval_ult"]:
            self.attack_interval_ult = value
            return
        if name in ["爆气伤害系数", "damage_modifier_ult"]:
            self.damage_modifier_ult = value
            return
        if name in ["爆气收线加成", "speed_modifier_ult"]:
            self.speed_modifier_ult = value
            return
        if name in ["爆气时长", "duration_ult"]:
            self.duration_ult = value
            return
        if name in ["气绝时长", "duration_exhausted"]:
            self.duration_exhausted = value
            return
        if name in ["眩晕时长", "duration_dizzy"]:
            self.duration_dizzy = value
            return




