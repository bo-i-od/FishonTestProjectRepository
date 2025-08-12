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
        self.toughness_max_init = 10000
        self.toughness_max = 10000
        self.restrain = skill_power_init.restrain
        self.battle_damage = skill_power_init.battle_damage
        self.attack_interval = skill_power_init.attack_interval
        self.attack_interval_ult = skill_power_init.attack_interval_ult
        self.damage_modifier_ult = skill_power_init.damage_modifier_ult
        self.duration_ult = skill_power_init.duration_ult
        self.speed_modifier_ult = skill_power_init.speed_modifier_ult
        self.duration_exhausted = skill_power_init.duration_exhausted
        self.duration_exhausted_modifier = 0
        self.time_exhausted = 0
        self.duration_dizzy = skill_power_init.duration_dizzy
        self.duration_dizzy_modifier = 0
        self.time_dizzy = 0
        battle_parameter_estimate = skill_power_init.battle_parameter_estimate[battle_tag - 1]
        self.battle_parameter_estimate = battle_parameter_estimate
        self.hp_factor = battle_parameter_estimate.hp_factor
        self.battle_time = battle_parameter_estimate.battle_time
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
        self.fish_hp = self.hp_factor * skill_power_init.fish_base_hp
        self.damage_modifier = self.fish_hp * self.attack_interval / self.battle_damage
        self.damage_hook = 1.5 / self.damage_modifier
        self.damage_hook_base = self.damage_hook
        self.count_start = 1
        self.count_speed_down = 0
        self.time_speed_down = 0
        self.gear_id_list = []

        self.count_customize = {}
        # 变量名到属性名的映射
        self.name_to_attribute = {
            "鱼血量上限": "fish_hp",
            "fish_hp": "fish_hp",
            "克制加成": "restrain",
            "restrain": "restrain",
            "攻击间隔": "attack_interval",
            "attack_interval": "attack_interval",
            "攻击速度": "attack_speed",  # 这是计算属性
            "attack_speed": "attack_speed",  # 这是计算属性
            "爆气攻击间隔": "attack_interval_ult",
            "attack_interval_ult": "attack_interval_ult",
            "爆气伤害系数": "damage_modifier_ult",
            "damage_modifier_ult": "damage_modifier_ult",
            "爆气收线加成": "speed_modifier_ult",
            "speed_modifier_ult": "speed_modifier_ult",
            "爆气时长": "duration_ult",
            "duration_ult": "duration_ult",
            "气绝时长": "duration_exhausted",
            "duration_exhausted": "duration_exhausted",
            "气绝总时长": "time_exhausted",
            "time_exhausted": "time_exhausted",
            "眩晕时长": "duration_dizzy",
            "duration_dizzy": "duration_dizzy",
            "眩晕总时长": "time_dizzy",
            "time_dizzy": "time_dizzy",
            "战斗时长": "battle_time",
            "battle_time": "battle_time",
            "特殊QTE数量": "count_qte_special",
            "count_qte_special": "count_qte_special",
            "鱼跃QTE数量": "count_qte_jump",
            "count_qte_jump": "count_qte_jump",
            "连招内QTE数量": "count_qte_in_combo",
            "count_qte_in_combo": "count_qte_in_combo",
            "QTE数量": "count_qte",
            "count_qte": "count_qte",
            "气数量": "count_energy",
            "count_energy": "count_energy",
            "弹反数量": "count_counter",
            "count_counter": "count_counter",
            "压制数量": "count_oppress",
            "count_oppress": "count_oppress",
            "技能数量": "count_skill",
            "count_skill": "count_skill",
            "爆气数量": "count_ult",
            "count_ult": "count_ult",
            "气绝数量": "count_exhausted",
            "count_exhausted": "count_exhausted",
            "眩晕数量": "count_dizzy",
            "count_dizzy": "count_dizzy",
            "常规伤害倍率": "damage_modifier",
            "damage_modifier": "damage_modifier",
            "刺鱼伤害": "damage_hook",
            "damage_hook": "damage_hook",
            "默认刺鱼伤害": "damage_hook_base",
            "damage_hook_base": "damage_hook_base",
            "眩晕时长加成": "duration_dizzy_modifier",
            "duration_dizzy_modifier": "duration_dizzy_modifier",
            "气绝时长加成": "duration_exhausted_modifier",
            "duration_exhausted_modifier": "duration_exhausted_modifier",
            "控制减速效果": "fish_speed_down_factor_in_control",
            "fish_speed_down_factor_in_control": "fish_speed_down_factor_in_control",
            "鱼减速次数": "count_speed_down",
            "count_speed_down": "count_speed_down",
            "减速总时长": "time_speed_down",
            "time_speed_down": "time_speed_down",
            "韧性上限": "toughness_max",
            "toughness_max": "toughness_max",
        }

        # 定义变量关系 - 当一个变量改变时，自动更新相关变量
        self.variable_relationships = {
            "attack_interval": {
                "attack_speed": lambda x: 1 / x if x != 0 else float('inf'),
                "攻击速度": lambda x: 1 / x if x != 0 else float('inf')
            },
            "攻击间隔": {
                "attack_speed": lambda x: 1 / x if x != 0 else float('inf'),
                "攻击速度": lambda x: 1 / x if x != 0 else float('inf')
            },
            "attack_speed": {
                "attack_interval": lambda x: 1 / x if x != 0 else float('inf'),
                "攻击间隔": lambda x: 1 / x if x != 0 else float('inf')
            },
            "攻击速度": {
                "attack_interval": lambda x: 1 / x if x != 0 else float('inf'),
                "攻击间隔": lambda x: 1 / x if x != 0 else float('inf')
            }
        }

        # 用于追踪正在更新的变量，防止循环更新
        self._updating_variables = set()
        # 在初始化时创建 Formula 实例
        self.Formula = self.Formula()



    class Formula:
        def __init__(self):
            self.damage_once_args_list = []
            self.damage_increased_args_list = []
            self.damage_hook_extend_args_list = []
            self.speed_change_args_list = []
            self.damage_multiplicative_args_list = []

    def get_variable(self, name):
        """动态获取变量值"""
        # 特殊处理计算属性
        if name in ["攻击速度", "attack_speed"]:
            return 1 / self.attack_interval if self.attack_interval != 0 else float('inf')

        # 普通属性
        if name in self.name_to_attribute:
            attr_name = self.name_to_attribute[name]
            return getattr(self, attr_name)
        elif hasattr(self, name):
            return getattr(self, name)
        elif "自定义" in name:
            if name in self.count_customize:
                return self.count_customize[name]
            return 0
        else:
            raise KeyError(f"未定义的变量: {name}")

    def set_variable(self, name, value):
        """设置变量值并更新相关变量"""
        # 防止循环更新
        if name in self._updating_variables:
            return

        try:
            self._updating_variables.add(name)

            # 首先设置主变量
            self._set_variable_direct(name, value)

            # 然后更新相关变量
            if name in self.variable_relationships:
                for related_var, formula in self.variable_relationships[name].items():
                    if related_var not in self._updating_variables:
                        try:
                            new_value = formula(value)
                            self.set_variable(related_var, new_value)
                        except Exception as e:
                            print(f"更新相关变量 {related_var} 时出错: {e}")
        finally:
            self._updating_variables.discard(name)

    def _set_variable_direct(self, name, value):
        """直接设置变量值，不触发关系更新"""
        # 特殊处理计算属性
        if name in ["攻击速度", "attack_speed"]:
            # 攻击速度是计算属性，不能直接设置，通过设置攻击间隔来改变
            if value != 0:
                self.attack_interval = 1 / value
            return

        # 普通属性
        if name in self.name_to_attribute:
            attr_name = self.name_to_attribute[name]
            setattr(self, attr_name, value)
        elif hasattr(self, name):
            setattr(self, name, value)
        else:
            raise KeyError(f"未定义的变量: {name}")

    def add_variable_relationship(self, source_var, target_var, formula):
        """添加变量关系"""
        if source_var not in self.variable_relationships:
            self.variable_relationships[source_var] = {}
        self.variable_relationships[source_var][target_var] = formula

    def remove_variable_relationship(self, source_var, target_var=None):
        """移除变量关系"""
        if source_var not in self.variable_relationships:
            return

        if target_var is None:
            # 移除所有相关关系
            del self.variable_relationships[source_var]
        else:
            # 移除特定关系
            if target_var in self.variable_relationships[source_var]:
                del self.variable_relationships[source_var][target_var]

            # 如果没有更多关系，删除整个条目
            if not self.variable_relationships[source_var]:
                del self.variable_relationships[source_var]

    def get_all_variables(self):
        """获取所有可用的变量名"""
        return list(self.name_to_attribute.keys())

    def get_variable_relationships(self):
        """获取所有变量关系"""
        return dict(self.variable_relationships)




