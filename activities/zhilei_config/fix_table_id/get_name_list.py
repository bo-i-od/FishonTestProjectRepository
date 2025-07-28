import os

from configs.pathConfig import EXCEL_PATH

# BaseData文件夹路径
base_dir = 'C:/Users/TU/Documents/fish_on/datapool/ElementData/BaseData/'

# 获取所有文件名
all_files = os.listdir(base_dir)

# 提取所有表名（去除扩展名和.decl/.data等后缀）
def extract_table_name(filename):
    # 只处理 .data.txt 文件
    if filename.endswith('.data.txt'):
        file_path = os.path.join(base_dir, filename)
        # 检查文件大小，小于等于2KB认为是空的
        file_size = os.path.getsize(file_path)
        if file_size > 512:  # 2KB = 2048 bytes
            return filename.replace('.data.txt', '')
    return None

table_names = [extract_table_name(f) for f in all_files]
table_names = [name for name in table_names if name]

# 分类
language_tables = [name for name in table_names if 'LANGUAGE' in name.upper()]
non_language_tables = [name for name in table_names if 'LANGUAGE' not in name.upper()]

# print('含LANGUAGE的表名:')
# for name in language_tables:
#     # print(name)
#     print("'", name, "',", sep='')

print('\n不含LANGUAGE的表名:')
for name in non_language_tables:
    # print(name)
    print("'",name,"',",sep='')