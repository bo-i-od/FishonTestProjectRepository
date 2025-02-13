import json
def load_log_new(file_name):
    with open(file_name, 'r') as file:
        data = file.read().strip()
    lines = data.split("\n")
    return [json.loads(line) for line in lines]

def get_fish_id(data):
    return data["fishes"]['1']["tpId"]

def get_flashcard_data(data):
    """hook log"""
    other_item=data['otherItems']
    if 'tiacs' in other_item:
        return other_item['tiacs']['1']
    else:
        return {}

def get_flashcard_id(data):
    """hook log"""
    other_item=data['otherItems']
    if 'tiacs' in other_item:
        return other_item['tiacs']['1']['id']
    else:
        return 0

def get_energy_cost(data):
    """hook log"""
    energyMultiplying = data["energyMultiplying"]
    return energyMultiplying*10

DebugInfo='debugInfos'
ProtectiveId='protectiveId'

def check_3001_control():
    cast_log = load_log_new('new_cast_log.txt')
    data = cast_log[0]
    return data[DebugInfo]['abTestOpen3001'],data[DebugInfo].get('abTestControlLevel',0)

def check_msg_success(msg_data):
    if msg_data.get('notify',{}).get('code',-1)==0:
        return True
    else:
        return False


def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip()

    lines = data.split("\n")
    result = []

    for line in lines:
        fields = line.split(", ")
        fish_data = {}
        for field in fields:
            if ":" in field:
                key, value = field.split(":")
                fish_data[key] = value or None
        result.append(fish_data)

    return result

def load_log(file_name):
    """
    [{'fish_id': '302009', 'color': '10', 'flash_card_num': None, 'flash_card_id': None},
    ...
    ]
    """
    # file_path = "log.txt"  # 替换为您的文件路径
    parsed_data = parse_data(file_name)
    return parsed_data


if __name__ == '__main__':
    # print(load_log_new('new_hook_log.txt'))
    print(check_3001_control())