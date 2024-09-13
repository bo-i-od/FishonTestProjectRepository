import glob
import os
import sys
from pathlib import Path
from configs.pathConfig import EXCEL_PATH
from tools.excelRead import ExcelTools

pic_path_data_dict = {"ACHIEVEMENT_CATEGORY.xlsm": ["icon", "fishList>pic"], "ACHIEVEMENT_GROUP.xlsm": ["icon"]}


def find_files_with_extension(folder_path, extension):
    # 确保扩展名以点开头
    if not extension.startswith('.'):
        extension = '.' + extension

    # 构建搜索模式
    search_pattern = os.path.join(folder_path, f'*{extension}')

    # 使用 glob 查找匹配的文件
    matching_files = glob.glob(search_pattern)

    # 只返回文件名，不包含路径
    return [os.path.basename(file) for file in matching_files]


def get_excel_key_dict():
    files = find_files_with_extension(folder_path=EXCEL_PATH, extension=".xlsm")
    key_dict = {}
    for index, file in enumerate(files):
        table_data = excel_tools.get_table_data(file)
        key_dict[file] = list(table_data)
        output = f"进度：{index + 1}/{len(files)}"
        # 打印并刷新 stdio
        sys.stdout.write(f"\r{output}")
        sys.stdout.flush()
    print(key_dict)


# 根据路径找到表中图片
def get_pic_list(table_data, pic_path: str):
    pic_path_split_list = pic_path.split(">")
    res = [table_data]
    for pic_path_split in pic_path_split_list:
        res = get_child_list(res, pic_path_split)
    return res


def get_child_list(parent_list, child_name):
    child_list = []
    for parent in parent_list:
        children = parent[child_name]
        for child in children:
            child_list.append(child)
    return child_list


def find_file(target_filename):
    root_path = Path(root_folder)
    for path in root_path.rglob(target_filename):
        if path.is_file():  # 检查路径是否是文件
            return True
    return False


def check_pic(excel_name):
    table_data = excel_tools.get_table_data(excel_name)
    pic_path_list = pic_path_data_dict[excel_name]
    pic_set = set()
    res = set()
    for pic_path in pic_path_list:
        pic_list = get_pic_list(table_data, pic_path)
        pic_set |= set(pic_list)

    for pic in pic_set:
        if pic == "0" or pic == 0:
            continue
        target_filename = str(pic) + '.png'
        found = find_file(target_filename)
        if found:
            continue
        res.add(target_filename)
        print(f"'{target_filename}' not found in '{root_folder}' or its subfolders.")
    return res


def main():
    res = set()
    for pic_path_data in pic_path_data_dict:
        check_result = check_pic(pic_path_data)
        res |= check_result
    print(f"找不到的资源为{res}")


if __name__ == '__main__':
    # 使用示例
    root_folder = 'C:/trunkCHS/client/MainProject/Assets/InBundle'
    excel_tools = ExcelTools(EXCEL_PATH)
    get_excel_key_dict()
    # main()
