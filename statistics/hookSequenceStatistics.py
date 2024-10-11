from common.basePage import BasePage

def get_result_list():
    result_list = []
    f = open("../statistics/hook_log.txt", "r")
    lines = f.readlines()
    f.close()
    cur = 0
    while cur < len(lines):
        fish_id = str_to_dict(lines[cur])['fish_id']
        result_list.append(fish_id)
        cur += 1
    return result_list


# 解析结果
def str_to_dict(input_string):
    pairs = input_string.replace(' ', '').split(',')
    # 创建 一个 字典来存储键值对
    data = {}

    # 遍历每个键值对
    for pair in pairs:
        # 使用split()方法将键值对拆分为键和值
        key, value = pair.split(':')

        # 将值存储在字典中
        if value:
            data[key] = value
        else:
            data[key] = ""
    return data

def count_target_occurrences(sequence, target):
    """
    统计目标序列target在sequence中出现的次数
    """
    count = 0
    target_length = len(target)
    for i in range(len(sequence) - target_length + 1):
        if sequence[i:i+target_length] == target:
            count += 1
    return count


def main():
    # 自定义的目标序列，"小"，"中"，"大"，"特大"，"超巨"，"奇珍"，"超奇珍"，"典藏"
    target_type_sequence = ["典藏", "典藏", "大"]
    result_list = get_result_list()
    type_sequence = bp.get_fish_type_list(result_list)
    print(f"目标序列为{target_type_sequence}")
    type_sequence_fish = []
    cur = 0
    while cur < len(type_sequence):
        if type_sequence[cur] in ["钓鱼失败", "其它"]:
            cur += 1
            continue
        type_sequence_fish.append(type_sequence[cur])
        cur += 1
    print(f"出鱼序列（不含杂物、钓鱼失败）为{type_sequence_fish}")
    occurrences = count_target_occurrences(type_sequence_fish, target_type_sequence)
    formatted = f"{occurrences * 100 / len(type_sequence_fish):.2f}%"
    print(f"钓鱼{len(type_sequence_fish)}次，目标序列出现的次数为: {occurrences}, 出现的概率为：{formatted}")


if __name__ == '__main__':
    bp = BasePage()
    main()
    bp.connect_close()