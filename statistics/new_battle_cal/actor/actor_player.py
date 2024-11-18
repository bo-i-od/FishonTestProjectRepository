from statistics.new_battle_cal.actor.actor import Actor
from statistics.new_battle_cal import attr_config

class Player(Actor):
    def __init__(self):
        super().__init__()
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

        # 状态维护
        self.energy = 0
        # 收线时的拉力速度加成百分比
        self.velocityZ_add_rate = 0
        # 伤害加成百分比
        self.damage_rate=0

    def get_current_velocityZ(self,rod_tension_status):
        if rod_tension_status =='reel':
            return self.velocityZ * (self.velocityZ_add_rate + 1000) / 1000
        elif rod_tension_status=='not_reel':
            return self.no_reel_velocityZ
    def trans_buff_to_attr(self, buff_name):
        if buff_name == 'ReelVelocityZUpRate':
            return "velocityZ_add_rate"
        if buff_name == 'DamageAmplifyRate':
            return "damage_rate"