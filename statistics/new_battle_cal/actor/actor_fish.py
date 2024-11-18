from statistics.new_battle_cal.actor.actor import Actor
from statistics.new_battle_cal import attr_config


class Fish(Actor):
    def __init__(self):
        super().__init__()
        self.velocityZ = attr_config.fish_velocityZ
        # buff 状态维护
        self.damage_rate=0
        self.velocityZ_add_rate = 0
        # self.hp = 10000

    def get_current_velocityZ(self):
        return self.velocityZ*(self.velocityZ_add_rate+1000)/1000

    def trans_buff_to_attr(self,buff_name):
        if buff_name == 'SwimVelocityZUpRate':
            return 'velocityZ_add_rate'
        if buff_name == 'DamageReduceRate':
            return 'damage_rate'