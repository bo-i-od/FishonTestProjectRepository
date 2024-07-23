from load_log import load_log

import re

# 自定义排序函数，以获取数字进行排序
def extract_number(text):
    if text.isdigit():
        return int(text)
    else:
        # 提取所有数字部分并转为整数，如果键中包含非数字部分，则保持不变，适合更复杂场景
        numbers = re.findall(r'\d+', text)
        return int(numbers[0]) if numbers else text





# 读取log
data = load_log('spin_log.txt')


# 索引转成分数
index2point = {'1': '40', '2': '300', '3': '80_1', '4': '200_partner', '5': '60', '6': '200', '7': '100', '8': '200_free', '9': '80_2', '10': '1000'}

# 统计次数
data_len = len(data)
result_times = {}
cur = 0
while cur < data_len:
    spinIndex = data[cur]['spinIndex']
    if spinIndex in result_times:
        result_times[spinIndex] += 1
        cur += 1
        continue
    result_times[spinIndex] = 1
    cur += 1

# 转成百分比结果
result_percentage = {}
for r in result_times:
    result_percentage[index2point[r]] = format(result_times[r] / data_len, ".2%")

# 按键的数值部分排序并生成新字典
sorted_dict = dict(sorted(result_percentage.items(), key=lambda item: extract_number(item[0])))
print(f"共计进行{data_len}次实验")
print(sorted_dict)







