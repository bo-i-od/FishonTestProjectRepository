from statistics.new_battle_cal.actor.actor import Actor
from statistics.new_battle_cal import attr_config


class Fish(Actor):
    def __init__(self):
        super().__init__()
        self.velocityZ = attr_config.fish_velocityZ
        # 战斗中鱼免伤率
        self.DamageReduceRate=0
        # 战斗中鱼跑线增加百分比
        self.SwimVelocityZUpRate = 0
        # 鱼切线概率，千分位
        self.LineCutChance = 200
        # 鱼张力战斗值系数1
        self.TensionUnstableRate = 0
        # 鱼张力战斗值系数2
        self.TensionUnstableValue = 0
        # buff系统里对 鱼张力战斗值 直接影响的增量值 （一般buff不会直接修改对应值的增量，而是修改相关系数，但是少量buff这么改了，且客户端逻辑支持，就先保障和客户端实现效果一样处理了 ）
        self.BattleTensionUnstable = 0

    def get_current_velocityZ(self):
        """获取鱼跑速"""
        return self.velocityZ*(self.SwimVelocityZUpRate+1000)/1000
    def get_GrowthTensionUnstable(self):
        """获取鱼养成张力值"""
        return attr_config.GrowthTensionUnstable
    def get_BattleTensionUnstable(self):
        """获取鱼战斗张力值"""
        return attr_config.GrowthTensionUnstable*(1000+self.TensionUnstableRate)/1000+self.TensionUnstableValue+self.BattleTensionUnstable

    def trans_buff_to_attr(self,buff_name):
        if buff_name == 'SwimVelocityZUpRate':
            return 'SwimVelocityZUpRate'
        if buff_name == 'DamageReduceRate':
            return 'DamageReduceRate'
        if buff_name == 'TensionUnstableRate':
            return 'TensionUnstableRate'
        if buff_name == 'TensionUnstableValue':
            return 'TensionUnstableValue'
        if buff_name == 'BattleTensionUnstable':
            return 'BattleTensionUnstable'
        if buff_name == 'LineCutChance':
            return 'LineCutChance'
