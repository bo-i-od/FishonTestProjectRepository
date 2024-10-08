import glob
import json
import os
import sys
from pathlib import Path
from tools.excelRead import ExcelTools
from datetime import datetime

pic_path_data_dict = {
    "ACHIEVEMENT_CATEGORY.xlsm": {"item_name": ["icon", "fishList>pic"], "ignore_icon_list": ["0", 0]},
    "ACHIEVEMENT_GROUP.xlsm": {"item_name": ["icon"]},

    }


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
    files = find_files_with_extension(folder_path=excel_path, extension=".xlsm")
    key_dict = {}
    for index, file in enumerate(files):
        table_data = excel_tools.get_table_data(file)
        key_dict[file] = list(table_data)
        output = f"进度：{index + 1}/{len(files)}"
        # 打印并刷新 stdio
        sys.stdout.write(f"\r{output}")
        sys.stdout.flush()
    return key_dict


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
    pic_path_list = pic_path_data_dict[excel_name]["item_name"]
    pic_set = set()
    res = set()
    for pic_path in pic_path_list:
        pic_list = get_pic_list(table_data, pic_path)
        pic_set |= set(pic_list)

    for index, pic in enumerate(pic_set):
        output = f"进度：{index + 1}/{len(pic_set)}"
        # 打印并刷新 stdio
        sys.stdout.write(f"\r{output}")
        sys.stdout.flush()
        if "ignore_icon_list" in pic_path_data_dict[excel_name]:
            pic_ignore_list = pic_path_data_dict[excel_name]["ignore_icon_list"]
            if pic in pic_ignore_list:
                continue
        target_filename = str(pic) + '.png'
        found = find_file(target_filename)
        if found:
            continue
        res.add(target_filename)
        sys.stdout.write('\r' + ' ' * len(output) + '\r')
        print(f"'{target_filename}' not found in '{root_folder}' or its subfolders.")
    print("\n")
    return res

def compare_dicts(old_dict, new_dict):
    old_keys = set(old_dict.keys())
    new_keys = set(new_dict.keys())

    added_keys = new_keys - old_keys
    removed_keys = old_keys - new_keys
    common_keys = old_keys.intersection(new_keys)

    changes = {
        "added_keys": list(added_keys),
        "removed_keys": list(removed_keys),
        "modified_values": {}
    }

    for key in common_keys:
        old_value = set(old_dict[key])
        new_value = set(new_dict[key])
        if old_value != new_value:
            changes["modified_values"][key] = {
                "added": list(new_value - old_value),
                "removed": list(old_value - new_value)
            }

    return changes


def version_comparison():
    version_new = get_excel_key_dict()
    version_old = version_new
    try:
        with open("../report/comparison_2024-10-08-14-07-53.txt", "r", encoding="utf-8") as file:
            content = file.read()
            version_old = json.loads(content.replace("'", '"'))
    except Exception as e:
        print(e)
        print("历史数据存在问题")

    now = datetime.now()
    # 构建文件夹名称
    # 获取当前时间的字符串表示
    time_str = now.strftime("%Y-%m-%d-%H-%M-%S")

    # 定义文件路径
    file_dir = "../report"
    file_path = f"{file_dir}/comparison_{time_str}.txt"

    # 确保目录存在
    os.makedirs(file_dir, exist_ok=True)

    version_change = compare_dicts(version_new, version_old)
    print(version_change)

    # 写入文件
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(version_new))


def main():
    res = set()
    for pic_path_data in pic_path_data_dict:
        print(pic_path_data)
        check_result = check_pic(pic_path_data)
        res |= check_result
    print(f"找不到的资源为{res}")


if __name__ == '__main__':
    # 图片资源路径
    root_folder = 'C:/trunkCHS/client/MainProject/Assets/InBundle'

    # 配置表路径
    excel_path = r"C:/trunkCHS/datapool/策划模板导出工具/"
    excel_tools = ExcelTools(excel_path)

    # 版本对照
    version_comparison()

    # main()
