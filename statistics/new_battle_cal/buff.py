import time
from statistics.new_battle_cal.read_config.read_config import *
class Buff:
    def __init__(self, name, duration, value, stackLimit,now_time):
        self.name = name # buff名
        self.duration = duration
        self.value = value # buff值
        self.start_time = now_time
        self.stack = 1 # 堆叠层数
        self.stackLimit =int(stackLimit) # 上限

    def is_expired(self,now_time):
        return (now_time - self.start_time) >= self.duration

    def refresh_time(self,now_time):
        self.start_time=now_time

def get_buff_object(buff_id,now_time):

    buff_info=battle_buff_data[str(buff_id)]
    duration=int(buff_info['duration'])
    effectGroup=buff_info['effectGroup'][0]
    effectName=effectGroup['effectName']
    effectValue=int(effectGroup['fac1'])
    stackLimit = buff_info['stackLimit']

    return Buff(effectName,duration,effectValue,stackLimit,now_time)



if __name__ == '__main__':
    pass