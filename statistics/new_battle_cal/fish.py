from buff import *
class Fish:
    def __init__(self):
        self.velocityZ = 4000
        self.damage_rate=0
        self.velocityZ_add_rate = 0
        self.buff_dict={}
        self.hp = 10000

    def get_current_velocityZ(self):
        return self.velocityZ*(self.velocityZ_add_rate+1000)/1000


    def add_buff(self,buff_id,now_time):
        # 重复叠层
        if buff_id in self.buff_dict:
            buff_object=self.buff_dict[buff_id]
            buff_object.stack = max(buff_object.stack+1,buff_object.stackLimit)
            buff_object.refresh_time(now_time)
        else:
            buff_object = get_buff_object(buff_id,now_time)
            self.buff_dict[buff_id]=buff_object

        if buff_object.name == 'SwimVelocityZUpRate':
            self.velocityZ_add_rate+= int(buff_object.value)
        if buff_object.name == 'DamageReduceRate':
            self.damage_rate +=buff_object.value

    def remove_buff(self,buff_id):
        if buff_id in self.buff_dict:
            buff_object=self.buff_dict.pop(buff_id)
            if buff_object.name == 'SwimVelocityZUpRate':
                self.velocityZ_add_rate -= buff_object.value*buff_object.stack
            if buff_object.name == 'DamageReduceRate':
                self.damage_rate -= buff_object.value*buff_object.stack

    def check_and_remove_buff(self,now_time):
        remove_list=[]
        for buff_id,buff_object in self.buff_dict.items():
            if buff_object.is_expired(now_time):
                remove_list.append(buff_id)
        for buff_id in remove_list:
            self.remove_buff(buff_id)
