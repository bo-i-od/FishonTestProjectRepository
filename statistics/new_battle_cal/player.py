from buff import *
import attr_config
class Player:
    def __init__(self):
        # -------------------跑线相关-------------
        # 收线时的拉力速度
        self.velocityZ = attr_config.player_velocityZ
        # 放线时的拉力速度
        self.no_reel_velocityZ = attr_config.player_no_reel_velocityZ
        # ----------------张力相关-------------------
        # 鱼竿属性
        # 对抗张力
        self.rod_tension_increase = attr_config.rod_tension_increase
        # 放松时的下降速度，写死，固定
        self.rod_tension_decrease = attr_config.rod_tension_decrease
        # -------------------伤害相关--------------------
        self.atk = attr_config.player_atk  # 每次收线 每200ms一次伤害


        # 玩家鱼线长度
        #self.lineLength = 80
        # 攻击频率，每200ms一下伤害
        # self.atk_freq = 200 # 攻击频率，每200ms一下伤害
        # 爆气相关
        # self.utl_atk_multi = 2  # 爆气伤害倍率
        # self.power_time = 2

        # buff、状态维护
        self.energy = 0
        self.buff_dict={}
        # 收线时的拉力速度加成百分比
        self.velocityZ_add_rate = 0
        # 伤害加成百分比
        self.damage_rate=0


    def get_current_velocityZ(self,rod_tension_status):
        if rod_tension_status =='reel':
            return self.velocityZ * (self.velocityZ_add_rate + 1000) / 1000
        elif rod_tension_status=='not_reel':
            return self.no_reel_velocityZ


    def add_buff(self, buff_id, now_time):
        isNeedAdd = True
        # 重复叠层
        if buff_id in self.buff_dict:
            buff_object = self.buff_dict[buff_id]
            if buff_object.stack + 1 > buff_object.stackLimit:
                isNeedAdd = False
            else:
                buff_object.stack += 1
            # buff_object.stack = max(buff_object.stack+1,buff_object.stackLimit)
            # buff_object.stack = max(buff_object.stack + 1, buff_object.stackLimit)
            # TODO 无论叠层是否满都 refresh_time?
            buff_object.refresh_time(now_time)
        else:
            buff_object = get_buff_object(buff_id, now_time)
            self.buff_dict[buff_id] = buff_object

        if buff_object.name == 'ReelVelocityZUpRate' and isNeedAdd:
            self.velocityZ_add_rate += buff_object.value
        if buff_object.name == 'DamageAmplifyRate' and isNeedAdd:
            self.damage_rate += buff_object.value

    def remove_buff(self, buff_id):
        if buff_id in self.buff_dict:
            buff_object = self.buff_dict.pop(buff_id)
            if buff_object.name == 'ReelVelocityZUpRate':
                self.velocityZ_add_rate -= buff_object.value * buff_object.stack
            if buff_object.name == 'DamageAmplifyRate':
                self.damage_rate -= buff_object.value * buff_object.stack

    def check_and_remove_buff(self, now_time):
        remove_list = []
        for buff_id, buff_object in self.buff_dict.items():
            if buff_object.is_expired(now_time):
                remove_list.append(buff_id)
        for buff_id in remove_list:
            self.remove_buff(buff_id)