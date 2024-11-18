from statistics.new_battle_cal import buff

class Actor:
    """
    人和鱼的基类，公共的部分写这里，比如buff
    """
    def __init__(self):
        self.buff_dict = {}
    def add_buff(self,buff_id,now_time):
        # 重复叠层
        if buff_id in self.buff_dict:
            buff_object=self.buff_dict[buff_id]
            buff_object.stack = max(buff_object.stack+1,buff_object.stackLimit)
            buff_object.refresh_time(now_time)
        else:
            buff_object = buff.get_buff_object(buff_id,now_time)
            self.buff_dict[buff_id]=buff_object
        # 添加buff
        attr_name=self.trans_buff_to_attr(buff_object.name)
        setattr(self,attr_name,getattr(self,attr_name)+int(buff_object.value))

    def trans_buff_to_attr(self,buff_name):
        return None


    def remove_buff(self,buff_id):
        if buff_id in self.buff_dict:
            buff_object=self.buff_dict.pop(buff_id)
            # 移除buff
            attr_name = self.trans_buff_to_attr(buff_object.name)
            setattr(self, attr_name, getattr(self, attr_name) - int(buff_object.value)*buff_object.stack)

    def check_and_remove_buff(self,now_time):
        remove_list=[]
        for buff_id,buff_object in self.buff_dict.items():
            if buff_object.is_expired(now_time):
                remove_list.append(buff_id)
        for buff_id in remove_list:
            self.remove_buff(buff_id)