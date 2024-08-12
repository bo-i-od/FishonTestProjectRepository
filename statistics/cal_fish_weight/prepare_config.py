import random
from tools.excelRead import ExceTools
from configs.pathConfig import EXCEL_PATH
excelTools =  ExceTools(EXCEL_PATH)

fish_table_data=excelTools.get_table_data("FISH_STAR_PROBABILITY.xlsm")
fish_table_data.pop('id')
weight_list = fish_table_data['probabilities_fishtype1']

# 删掉概率为0的那些项
real_index=[]
for index, i in enumerate(weight_list):
    if i:
        real_index.append(index)
for key, value in fish_table_data.items():
    fish_table_data[key] = [i for i in value if value.index(i) in real_index]

# 新增求和的一列，这样做随机时比较高效
sum_weight=0
weight_list = fish_table_data['probabilities_fishtype1']
new_sum_weight_list=[]
for index, i in enumerate(weight_list):
    sum_weight+=i
    new_sum_weight_list.append(sum_weight)
fish_table_data['new_sum_weight_list']=new_sum_weight_list
print(sum_weight)
print(fish_table_data)