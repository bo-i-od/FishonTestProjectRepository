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

def load_log():
    """
    [{'fish_id': '302009', 'color': '10', 'flash_card_num': None, 'flash_card_id': None},
    ...
    ]
    """
    file_path = "log.txt"  # 替换为您的文件路径
    parsed_data = parse_data(file_path)
    return parsed_data

if __name__ == '__main__':
    print(load_log())