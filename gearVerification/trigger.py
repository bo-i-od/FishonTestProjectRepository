from configs.pathConfig import EXCEL_PATH
from gearVerification.blackboard import Blackboard
from gearVerification.formula import arg_to_value
from tools.excelRead import ExcelToolsForActivities





class Trigger:
    def __init__(self, bb: Blackboard):
        self.bb = bb
        self.trigger_dict = {
            "开局": {"name": "start", "trigger_func": self.start},
            "攻击": {"name": "attack", "trigger_func": self.attack, "triggered_count": self.bb.count_attack},
            "摆杆": {"name": "qte", "trigger_func": self.qte, "triggered_count": self.bb.count_qte},
            "摆竿": {"name": "qte", "trigger_func": self.qte, "triggered_count": self.bb.count_qte},
            "拔杆": {"name": "counter", "trigger_func": self.counter, "triggered_count": self.bb.count_counter},
            "拔竿": {"name": "counter", "trigger_func": self.counter, "triggered_count": self.bb.count_counter},
            "爆气": {"name": "ult", "trigger_func": self.ult, "triggered_count": self.bb.count_ult},
            "气绝": {"name": "exhausted", "trigger_func": self.exhausted, "triggered_count": self.bb.count_exhausted},
            "眩晕": {"name": "dizzy", "trigger_func": self.dizzy, "triggered_count": self.bb.count_dizzy},
            "回气": {"name": "energy", "trigger_func": self.energy, "triggered_count": self.bb.count_energy},
            "技能": {"name": "skill", "trigger_func": self.skill,  "triggered_count": self.bb.count_skill},
            "压制": {"name": "oppress", "trigger_func": self.oppress, "triggered_count": self.bb.count_oppress},
            "减速": {"name": "speed_down", "trigger_func": self.speed_down, "triggered_count": self.bb.count_speed_down},
            "自定义": {"name": "customize", "trigger_func": self.customize,  "triggered_count": self.bb.count_customize},
        }
        # 自定义触发关系字典
        # 格式: {"触发源": [{"target": "目标触发", "target_name": "目标名称", "delta": 倍数}, ...]}
        # 触发源可以是 "qte", "counter" 或 "customize:name" 格式
        self.custom_triggers = {}

        # # 动态效果追踪器
        # self.dynamic_effects = {
        #     2: {"handler": self.damage_increase},
        #     3: {"handler": self.damage_once},
        #     4: {"handler": self.speed_change}
        # }

    def generate_trigger(self, skill_id_list):
        excel_tool = ExcelToolsForActivities(root_path=EXCEL_PATH)
        skill_power_detail = excel_tool.get_table_data_detail(book_name="SKILL_POWER.xlsm")
        trigger_detail_list = []
        for skill_id in skill_id_list:
            json_object = excel_tool.get_table_data_object_by_key_value(key="sortId", value=skill_id, table_data_detail=skill_power_detail)
            self.bb.gear_id_list.append(json_object["tpId"])
            for trigger in json_object["trigger"]:
                if not trigger:
                    continue
                trigger_detail_list.append(trigger)

        cur = 0
        while cur < len(trigger_detail_list):
            trigger_detail = trigger_detail_list[cur]
            # 触发器可以使用或逻辑
            trigger_name_split = trigger_detail["triggerName"].split("|")
            if len(trigger_name_split) > 1:
                for trigger_name in trigger_name_split:
                    trigger_detail_copy = trigger_detail.copy()
                    trigger_detail_copy["triggerName"] = trigger_name
                    trigger_detail_list.append(trigger_detail_copy)
                cur += 1
                continue
            # 被触发器可以使用与逻辑
            triggered_trigger_name_split = []
            if "triggeredTriggerName" in trigger_detail:
                triggered_trigger_name_split = trigger_detail["triggeredTriggerName"].split("&")
            if len(triggered_trigger_name_split) > 1:
                for triggered_trigger_name in triggered_trigger_name_split:
                    trigger_detail_copy = trigger_detail.copy()
                    trigger_detail_copy["triggeredTriggerName"] = triggered_trigger_name
                    trigger_detail_list.append(trigger_detail_copy)
                cur += 1
                continue
            # 处理动态效果（2:伤害增加, 3:一次性伤害, 4:速度变化）
            effect = trigger_detail["effect"]
            if effect in [2, 3, 4, 5]:
                # 创建动态效果触发器
                effect_id = trigger_detail["triggerName"]
                self._create_dynamic_effect_trigger(
                    effect,
                    effect_id,
                    arg1=trigger_detail["arg1"],
                    arg2=trigger_detail["arg2"] if "arg2" in trigger_detail else None
                )
                cur += 1
                continue

            if trigger_detail["effect"] == 6:
                self.bb.Formula.damage_hook_extend_args_list.append({"arg1": trigger_detail["arg1"]})
                cur += 1
                continue
            if trigger_detail["effect"] == 7:
                arg1_split = trigger_detail["arg1"].split("=")
                self.bb.set_variable(name=arg1_split[0], value=arg_to_value(self.bb, arg=arg1_split[1]))
                cur += 1
                continue
            if trigger_detail["effect"] == 8:
                self.bb.Formula.damage_multiplicative_args_list.append({"arg1": trigger_detail["arg1"]})
                cur += 1
                continue
            # if trigger_detail["effect"] == 8:
            #     self.bb.Formula.damage_multiplicative_args_list.append({"arg1": trigger_detail["arg1"]})
            #     cur += 1
            #     continue
            # trigger_detail["effect"] == 1
            trigger_name = trigger_detail["triggerName"]
            triggered_trigger_name = trigger_detail["arg1"]
            source_name = None
            target_name = None
            if "自定义" in trigger_name:
                # source_name = trigger_name.split("自定义")[1]
                source_name = trigger_name
                source_trigger = "customize"
            else:
                source_trigger = self.trigger_dict[trigger_name]["name"]
            if "自定义" in triggered_trigger_name:
                # target_name = triggered_trigger_name.split("自定义")[1]
                target_name = triggered_trigger_name
                triggered_trigger = "customize"
            else:
                triggered_trigger = self.trigger_dict[triggered_trigger_name]["name"]
            delta = trigger_detail["arg2"]
            # if trigger_detail["arg0"] == 1:
            #     pass
            self.add_custom_trigger(
                source_trigger=source_trigger,
                triggered_trigger=triggered_trigger,
                delta=delta,
                source_name=source_name,
                target_name=target_name
            )
            cur += 1

        # print(self.custom_triggers)

    def _create_dynamic_effect_trigger(self, effect_type, effect_id, arg1, arg2=None):
        """
        创建动态效果触发器
        effect_type: 2=伤害增加, 3=一次性伤害, 4，5=速度变化
        effect_id: 效果标识符
        """
        # 将参数绑定到处理函数，避免额外传递参数问题
        def effect_handler(delta):
            # 直接调用对应的处理方法
            if effect_type == 2:
                self.damage_increase(arg1=arg1, arg2=arg2, delta=delta)
            elif effect_type == 3:
                self.damage_once(arg1=arg1, arg2=arg2, delta=delta)
            elif effect_type == 4:
                self.fish_speed_down(arg1=arg1, arg2=arg2, delta=delta)
            elif effect_type == 5:
                self.player_speed_up(arg1=arg1, arg2=arg2, delta=delta)

        # 处理源触发器
        if "自定义" in effect_id:
            # source_name = effect_id.split("自定义")[1]
            source_name = effect_id
            source_trigger = "customize"
        else:
            source_trigger = self.trigger_dict[effect_id]["name"]
            source_name = None

        # 添加回调触发器
        self.add_custom_trigger_callback(
            source_trigger=source_trigger,
            callback=effect_handler,
            delta=1.0,
            source_name=source_name
        )

    # 新增：伤害增加效果
    def damage_increase(self, arg1, arg2, delta):
        """
        伤害增加效果处理器
        delta: 触发次数
        arg1: 效果
        arg2: 持续时间期望
        """
        self.bb.Formula.damage_increased_args_list.append({"arg1": arg1, "arg2": arg2, "count": delta})

    # 新增：一次性伤害效果
    def damage_once(self, arg1, arg2, delta):
        """
        一次性伤害效果处理器
        delta: 触发次数
        arg1: 伤害值
        arg2 无意义
        """
        self.bb.Formula.damage_once_args_list.append({"arg1": arg1, "arg2": arg2, "count": delta})

    # 新增：速度变化效果
    def fish_speed_down(self, arg1, arg2, delta):
        """
        速度变化效果处理器
        delta: 触发次数
        arg1: 速度变化百分比 (正数鱼减速，负数鱼加速)
        arg2: 持续时间期望
        """
        self.bb.Formula.speed_change_args_list.append({"arg1": arg1, "arg2": arg2, "count": delta, "object": 2})

    # 新增：速度变化效果
    def player_speed_up(self, arg1, arg2, delta):
        """
        速度变化效果处理器
        delta: 触发次数
        arg1: 拉力变化百分比(正数收线加快，负数收线减慢)
        arg2: 持续时间期望
        """
        self.bb.Formula.speed_change_args_list.append({"arg1": arg1, "arg2": arg2, "count": delta, "object": 1})

    def add_custom_trigger_callback(self, source_trigger, callback, delta, source_name=None):
        """
        添加带回调的自定义触发器
        """
        source_key = self._get_trigger_key(source_trigger, source_name)
        if source_key not in self.custom_triggers:
            self.custom_triggers[source_key] = []

        self.custom_triggers[source_key].append({
            "callback": callback,
            "delta": delta
        })

    def run_trigger(self):
        battle_parameter_estimate = self.bb.battle_parameter_estimate
        count_qte = battle_parameter_estimate.count_qte
        count_skill = battle_parameter_estimate.count_skill
        count_counter = battle_parameter_estimate.count_skill * battle_parameter_estimate.ratio_counter
        count_oppress = battle_parameter_estimate.count_skill * battle_parameter_estimate.ratio_oppress
        count_skill_without_counter = count_skill - count_counter - count_oppress
        count_attack = self.bb.battle_parameter_estimate.battle_time / self.bb.attack_interval
        self.start(delta_start=1)
        self.oppress(delta_oppress=count_oppress)
        self.attack(delta_attack=count_attack)
        self.skill(delta_skill=count_skill_without_counter)
        self.counter(delta_counter=count_counter)  # 这会触发一系列连锁反应
        self.qte(delta_qte=count_qte)  # 这会触发一系列连锁反应

    def _get_trigger_key(self, trigger_type, name=None):
        """
        生成触发器的唯一键
        :param trigger_type: 触发器类型
        :param name: 名称（可选）
        :return: 唯一键
        """
        if name and trigger_type == "customize":
            return f"customize:{name}"
        return trigger_type

    def add_custom_trigger(self, source_trigger, triggered_trigger, delta, source_name=None, target_name=None):
        """
        添加自定义触发关系
        :param source_trigger: 源触发器名称 (如 "qte", "counter", "customize")
        :param triggered_trigger: 目标触发器名称 (如 "dizzy", "energy", "customize")
        :param delta: 触发倍数
        :param source_name: 源触发器名称（当source_trigger为"customize"时使用）
        :param target_name: 目标触发器名称（当triggered_trigger为"customize"时使用）
        """
        source_key = self._get_trigger_key(source_trigger, source_name)

        if source_key not in self.custom_triggers:
            self.custom_triggers[source_key] = []

        self.custom_triggers[source_key].append({
            "target": triggered_trigger,
            "target_name": target_name,
            "delta": delta
        })

        # print(f"添加触发: {source_key} -> {triggered_trigger}" +
              # (f":{target_name}" if target_name else "") + f" (倍数: {delta})")

    def remove_custom_trigger(self, source_trigger, triggered_trigger=None, source_name=None, target_name=None):
        """
        移除自定义触发关系
        :param source_trigger: 源触发器名称
        :param triggered_trigger: 目标触发器名称，如果为None则移除所有相关的触发关系
        :param source_name: 源触发器名称（当source_trigger为"customize"时使用）
        :param target_name: 目标触发器名称（当triggered_trigger为"customize"时使用）
        """
        source_key = self._get_trigger_key(source_trigger, source_name)

        if source_key not in self.custom_triggers:
            return
        if triggered_trigger is None:
            del self.custom_triggers[source_key]
            # print(f"移除所有来自 {source_key} 的触发")
            return
        original_count = len(self.custom_triggers[source_key])
        self.custom_triggers[source_key] = [
            item for item in self.custom_triggers[source_key]
            if not (item["target"] == triggered_trigger and item["target_name"] == target_name)
        ]
        if not self.custom_triggers[source_key]:
            del self.custom_triggers[source_key]
        removed_count = original_count - len(self.custom_triggers.get(source_key, []))
        # print(f"移除了 {removed_count} 个触发关系")

    def _execute_custom_triggers(self, source_trigger, source_delta, source_name=None):
        """
        执行自定义触发关系
        :param source_trigger: 源触发器名称
        :param source_delta: 源触发器的变化量
        :param source_name: 源触发器的名称（可选）
        """
        source_delta = arg_to_value(self.bb, source_delta)
        source_key = self._get_trigger_key(source_trigger, source_name)

        if source_key not in self.custom_triggers:
            return
        for custom_trigger in self.custom_triggers[source_key]:
            # 检查是回调类型还是目标类型
            if "callback" in custom_trigger:
                # 处理回调类型触发器
                delta = custom_trigger["delta"] * source_delta
                custom_trigger["callback"](delta)
                continue
            target = custom_trigger["target"]
            target_name = custom_trigger["target_name"]
            custom_trigger_delta = arg_to_value(self.bb, custom_trigger["delta"])
            delta = custom_trigger_delta * source_delta

            # print(f"  -> 触发 {target}" + (f":{target_name}" if target_name else "") + f" (变化量: {delta})")

            # 根据目标触发器执行相应的函数
            if target == "start":
                self.start(delta)
            elif target == "attack":
                self.attack(delta)
            elif target == "qte":
                self.qte(delta)
            elif target == "oppress":
                self.oppress(delta)
            elif target == "energy":
                self.energy(delta)
            elif target == "ult":
                self.ult(delta)
            elif target == "counter":
                self.counter(delta)
            elif target == "exhausted":
                self.exhausted(delta)
            elif target == "dizzy":
                self.dizzy(delta)
            elif target == "skill":
                self.skill(delta)
            elif target == "customize":
                if not target_name:
                    print(f"警告: customize触发器需要指定target_name")
                    return
                self.customize(delta, target_name)

    def get_custom_triggers_info(self):
        """
        获取所有自定义触发关系的信息
        """
        info = {}
        for source_key, triggers in self.custom_triggers.items():
            info[source_key] = []
            for trigger in triggers:
                target_info = trigger["target"]
                if trigger["target_name"]:
                    target_info += f":{trigger['target_name']}"
                info[source_key].append({
                    "target": target_info,
                    "delta": trigger["delta"]
                })
        return info

    def start(self, delta_start=1):
        delta_start = arg_to_value(self, delta_start)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="start", source_delta=delta_start)

    def attack(self, delta_attack):
        delta_attack = arg_to_value(self, delta_attack)
        if abs(delta_attack) < 0.001:
            return
        self.bb.count_attack += delta_attack
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="attack", source_delta=delta_attack)

    def qte(self, delta_qte):
        delta_qte = arg_to_value(self, delta_qte)
        if abs(delta_qte) < 0.001:
            return
        self.bb.count_qte += delta_qte
        # print(f"  -> 触发 energy" + f" (变化量: {delta_qte})")
        self.energy(delta_energy=delta_qte)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="qte", source_delta=delta_qte)

    def oppress(self, delta_oppress):
        delta_oppress = arg_to_value(self, delta_oppress)
        if abs(delta_oppress) < 0.001:
            return
        self.bb.count_oppress += delta_oppress
        self.energy(delta_energy=delta_oppress)
        self.skill(delta_skill=delta_oppress)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="oppress", source_delta=delta_oppress)

    def energy(self, delta_energy):
        delta_energy = arg_to_value(self, delta_energy)
        if abs(delta_energy) < 0.001:
            return
        self.bb.count_energy += delta_energy
        # print(f"  -> 触发 ult" + f" (变化量: {delta_energy/3})")
        self.ult(delta_ult=delta_energy/3)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="energy", source_delta=delta_energy)

    def ult(self, delta_ult):
        delta_ult = arg_to_value(self, delta_ult)
        if abs(delta_ult) < 0.001:
            return
        self.bb.count_ult += delta_ult
        # print(f"  -> 触发 exhausted" + f" (变化量: {delta_ult * 0.4})")
        self.exhausted(delta_exhausted=delta_ult * 4000/(self.bb.toughness_max+3000))
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="ult", source_delta=delta_ult)

    def counter(self, delta_counter):
        delta_counter = arg_to_value(self, delta_counter)
        if abs(delta_counter) < 0.001:
            return
        self.bb.count_counter += delta_counter
        # print(f"  -> 触发 exhausted" + f" (变化量: {delta_counter * 0.2})")
        self.exhausted(delta_exhausted=delta_counter * 2000/(self.bb.toughness_max+3000))
        # print(f"  -> 触发 energy" + f" (变化量: {-delta_counter})")
        self.energy(delta_energy=-delta_counter)
        # print(f"  -> 触发 skill" + f" (变化量: {delta_counter})")
        self.skill(delta_skill=delta_counter)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="counter", source_delta=delta_counter)

    def exhausted(self, delta_exhausted):
        delta_exhausted = arg_to_value(self, delta_exhausted)
        if abs(delta_exhausted) < 0.001:
            return
        if self.bb.count_exhausted > 3:
            return
        self.bb.count_exhausted += delta_exhausted
        delta_time_exhausted = delta_exhausted * self.bb.duration_exhausted * (1 + self.bb.duration_exhausted_modifier)
        self.bb.time_exhausted += delta_time_exhausted
        self.speed_down(delta_speed_down=delta_exhausted, delta_time_speed_down=delta_time_exhausted)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="exhausted", source_delta=delta_exhausted)

    def dizzy(self, delta_dizzy):
        delta_dizzy = arg_to_value(self, delta_dizzy)
        if abs(delta_dizzy) < 0.001:
            return
        self.bb.count_dizzy += delta_dizzy
        delta_time_dizzy = delta_dizzy * self.bb.duration_dizzy * (1 + self.bb.duration_dizzy_modifier)
        self.bb.time_dizzy += delta_time_dizzy
        self.speed_down(delta_speed_down=delta_dizzy, delta_time_speed_down=delta_time_dizzy)
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="dizzy", source_delta=delta_dizzy)

    def skill(self, delta_skill):
        delta_skill = arg_to_value(self, delta_skill)
        if abs(delta_skill) < 0.001:
            return
        self.bb.count_skill += delta_skill
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="skill", source_delta=delta_skill)

    def speed_down(self, delta_speed_down, delta_time_speed_down):
        delta_speed_down = arg_to_value(self, delta_speed_down)
        if abs(delta_speed_down) < 0.001:
            return
        self.bb.count_speed_down += delta_speed_down
        self.bb.time_speed_down += delta_time_speed_down
        # 执行自定义触发
        self._execute_custom_triggers(source_trigger="speed_down", source_delta=delta_speed_down)

    def customize(self, delta_customize, name):
        delta_customize = arg_to_value(self, delta_customize)
        if abs(delta_customize) < 0.001:
            return
        if name not in self.bb.count_customize:
            self.bb.count_customize[name] = 0
        self.bb.count_customize[name] += delta_customize
        # 执行自定义触发（带名称）
        self._execute_custom_triggers(source_trigger="customize", source_delta=delta_customize, source_name=name)




