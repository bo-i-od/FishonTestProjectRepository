from load_log import load_log,load_log_new
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
data1 = load_log_new('new_cast_log.txt')
data2 = load_log_new('new_hook_log.txt')

# 统计次数
data_len = len(data2)
result_times = {}
protective_times = {}
cur = 0
while cur < data_len:
    tpId = data2[cur]['fishes']['1']['tpId']
    protectiveId = data1[cur]['debugInfos']['protectiveId']
    if tpId in result_times:
        result_times[tpId] += 1
    else:
        result_times[tpId] = 1

    if protectiveId == 0:
        cur += 1
        continue
    print(protectiveId)
    pt = f"protectiveId_{protectiveId} tpId_{tpId}"
    if pt in protective_times:
        protective_times[pt] += 1
    else:
        protective_times[pt] = 1
    cur += 1


# 转成百分比结果
result_percentage = {}
protective_percentage = {}
print(f"进行{data_len}次hook")
for r in result_times:
    result_percentage[r] = format(result_times[r] / data_len, ".2%")
print(result_percentage)
sorted_dict = dict(sorted(result_percentage.items(), key=lambda item: item[0]))
print(f"上鱼概率为{sorted_dict}")
for r in protective_times:
    protective_percentage[r] = format(protective_times[r] / data_len, ".2%")
sorted_dict = dict(sorted(protective_percentage.items(), key=lambda item: item[0]))
print(f"保底概率为{sorted_dict}")
