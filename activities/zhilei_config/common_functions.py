import copy


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
