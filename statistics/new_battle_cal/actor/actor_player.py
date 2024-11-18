from statistics.new_battle_cal.actor.actor import Actor
from statistics.new_battle_cal import attr_config

def clamp(value,min_value,max_value):
    return max(min_value,min(max_value,value))


class Player(Actor):
    def __init__(self):
        super().__init__()
        # -------------------跑线相关-------------
        # 收线时的拉力速度
        self.velocityZ = attr_config.player_velocityZ
        # 放线时的拉力速度
        self.no_reel_velocityZ = attr_config.player_no_reel_velocityZ
        # -------------------伤害相关--------------------
        self.atk = attr_config.player_atk  # 每次收线 每200ms一次伤害

        # 状态维护
        self.energy = 0
        # 收线时的拉力速度加成百分比
        self.ReelVelocityZUpRate = 0
        # 伤害加成百分比
        self.DamageAmplifyRate=0

    def get_current_velocityZ(self,rod_tension_status):
        if rod_tension_status =='reel':
            return self.velocityZ * (self.ReelVelocityZUpRate + 1000) / 1000
        elif rod_tension_status=='not_reel':
            return self.no_reel_velocityZ

    # -------------- 张力相关 -------------
    def get_GrowthTensionStable(self):
        return attr_config.GrowthTensionStable

    def get_BattleTensionStable(self):
        """这个一般没有buff影响,先临时凑合"""
        return attr_config.GrowthTensionStable
    def get_BattleTensionDownSpeed(self,fish_object):
        """下降速度计算公式"""
        if attr_config.debug_tension:
            return attr_config.debug_BattleTensionDownSpeed
        else:
            temp = fish_object.get_GrowthTensionUnstable()-self.get_GrowthTensionStable()
            return -clamp(clamp(temp,1600,6000)*2.3,1600,15000)
    def get_BattleTensionUpSpeed(self,fish_object):
        """上升速度计算公式"""
        if attr_config.debug_tension:
            return attr_config.debug_BattleTensionUpSpeed
        else:
            temp = fish_object.get_BattleTensionUnstable()-self.get_BattleTensionStable()
            return clamp(temp,1600,15000)

    def trans_buff_to_attr(self, buff_name):
        if buff_name == 'ReelVelocityZUpRate':
            return "ReelVelocityZUpRate"
        if buff_name == 'DamageAmplifyRate':
            return "DamageAmplifyRate"
