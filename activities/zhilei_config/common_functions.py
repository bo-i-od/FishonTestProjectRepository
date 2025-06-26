import copy
import random


def match_keys(data,match_data):
    """ 按 match_data里的key_value 匹配配表里的数据，返回key"""
    for match_key in match_data:
        match_data[match_key]=str(match_data[match_key])

    for key,value in data.items():
        is_match=True
        for match_key,match_value in match_data.items():
            if match_value=='0' and (match_key not in value):
                continue
            else:
                if (match_key not in value) or value[match_key]!=match_value:
                    is_match=False
        if is_match:
            return key
    return False

def get_format_data(data,base_data):
    """ 基于base_config 格式的数据 筛选data的数据 """
    ret=copy.deepcopy(base_data)
    for key in base_data:
        if key in data:
            ret[key]=data[key]
    return ret


def rand_with_weight(weights):
    """ 按权重随机，输入weight,返回index """
    total = sum(weights)
    rand = random.randint(1, total)
    curr_sum = 0
    for index, weight in enumerate(weights):
        curr_sum += weight
        if rand <= curr_sum:
            return index


class Wheel():
    """ 按权重随机类 """
    def __init__(self, wheel_config):
        self.wheel = wheel_config['wheel']
        self.weights = wheel_config['weights']
        self.w = []
        self.type = []
        self.sum_weights = []
        for i in self.weights:
            sum_w = sum(i)
            self.sum_weights.append(sum_w)
            if sum_w < 1000:
                self.w.append(self.generate_weight_table_type1(i))
                self.type.append(1)
            else:
                self.w.append(self.generate_weight_table_type2(i))
                self.type.append(2)

    # 两种随机方法,适用不同情况来提高效率
    def generate_weight_table_type1(self, weights):
        w = []
        for i in range(len(weights)):
            for j in range(weights[i]):
                w.append(i)
        return w

    def generate_weight_table_type2(self, weights):
        w = []
        curr = 0
        for i in weights:
            curr += i
            w.append(curr)
        return w

    def spin(self, index=0):
        if self.type[index] == 1:
            return self.wheel[self.w[index][random.randint(0,len(self.w[index])-1)]]
        else:
            r = random.randint(0,self.sum_weights[index]-1)
            for index, value in enumerate(self.w[index]):
                if r < value:
                    return self.wheel[index]
        return self.wheel[-1]

    def pick(self, pick_num, index=0):
        pick_result = []
        temp_weights = copy.deepcopy(self.weights[index])
        for i in range(pick_num):
            result = rand_with_weight(temp_weights)
            pick_result.append(self.wheel[result])
            temp_weights[result] = 0
        return pick_result


w = Wheel({
    'wheel': [3,4,5,6,8,10,15,20,30],
    'weights': [
        [30,15,10,0,0,5,4,2,1],[30,15,10,5,4,1,0,0,0]
    ]
})
