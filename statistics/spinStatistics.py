from load_log import load_log

# 读取log
data = load_log('spin_log.txt')


# 索引转成分数
index2point = {'1': '40', '2': '300', '3': '80_1', '4': '200_zhuli', '5': '60', '6': '200', '7': '100', '8': '200_free', '9': '80_2', '10': '1000'}

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
print(result_times)

# 转成百分比结果
result_percentage = {}
for r in result_times:
    result_percentage[index2point[r]] = format(result_times[r] / data_len, ".2%")

print(f"共计进行{data_len}次实验")
print(result_percentage)







