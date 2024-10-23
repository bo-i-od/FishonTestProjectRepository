import glob
import json
import os
import sys
from pathlib import Path

from tools import baseDataRead
from tools.excelRead import ExcelTools
from datetime import datetime
from configs import excelConfig


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


def get_key_dict_excel():
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

def get_key_dict_base_data():
    key_dict = {}
    files = baseDataRead.get_files_in_current_directory(base_data_path)
    prefix_list = baseDataRead.get_prefix_list(files)
    for prefix in prefix_list:
        temp_dict = {}
        decl_file = base_data_path + prefix + '.decl.h'
        try:
            structs = baseDataRead.parse_decl_file(decl_file)
        except FileNotFoundError:
            continue
        for struct in structs:
            if prefix == struct:
                temp_dict[prefix + '.xlsm'] = list(structs[struct])
            else:
                temp_dict[prefix + '.xlsm+' + struct] = list(structs[struct])
        key_dict.update(temp_dict)

    return key_dict


# 根据路径找到表中图片
def get_pic_list_by_table_data(table_data, pic_path: str):
    pic_path_split_list = pic_path.split(">")
    res = [table_data]
    for pic_path_split in pic_path_split_list:
        res = get_child_list(res, pic_path_split)
    return res


def get_pic_list_by_table_data_object_list(table_data_object_list, pic_path: str):
    pic_path_split_list = pic_path.split(">")
    res = []
    for table_data_object in table_data_object_list:
        temp = [table_data_object]
        for pic_path_split in pic_path_split_list:
            temp = get_list(temp, pic_path_split)
        res += temp
    return res


def get_list(parent_list, child_name):
    child_list = []
    for parent in parent_list:
        if not parent:
            continue
        if not isinstance(parent, list):
            if child_name not in parent:
                continue
            child_list.append(parent[child_name])
            continue
        for p in parent:
            if not p:
                continue
            if child_name not in p:
                continue
            child_list.append(p[child_name])
    return child_list


def get_child_list(parent_list, child_name):
    child_list = []
    for parent in parent_list:
        if not parent:
            continue
        children = parent[child_name]
        for child in children:
            child_list.append(child)
    return child_list


def find_file(target_filename):
    root_path = Path(pictures_folder)
    for path in root_path.rglob(target_filename):
        if path.is_file():  # 检查路径是否是文件
            return True
    return False


def get_pictures_by_excel(excel_name):
    table_data = excel_tools.get_table_data(excel_name)
    pic_path_list = excelConfig.pic_path_data_dict[excel_name]["item_name"]
    pic_set = set()

    for pic_path in pic_path_list:
        pic_list = get_pic_list_by_table_data(table_data, pic_path)
        pic_set |= set(pic_list)
    return pic_set


def get_pictures_by_base_data(excel_name):
    print(excel_name)
    prefix = excel_name.split(".")[0]
    table_data_object_list = baseDataRead.convert_to_json(base_data_path, prefix)[0]
    pic_path_list = excelConfig.pic_path_data_dict[excel_name]["item_name"]
    pic_set = set()

    for pic_path in pic_path_list:
        pic_list = get_pic_list_by_table_data_object_list(table_data_object_list, pic_path)
        for pic in pic_list:
            if not isinstance(pic, list):
                pic_set |= set(pic_list)
                break
            pic_set |= set(pic)
    return pic_set


def check_pictures(excel_name, pic_set):
    res = set()
    for index, pic in enumerate(pic_set):
        output = f"进度：{index + 1}/{len(pic_set)}"
        # 打印并刷新 stdio
        sys.stdout.write(f"\r{output}")
        sys.stdout.flush()
        if "ignore_icon_list" in excelConfig.pic_path_data_dict[excel_name]:
            pic_ignore_list = excelConfig.pic_path_data_dict[excel_name]["ignore_icon_list"]
            if pic in pic_ignore_list:
                continue
        target_filename = str(pic) + '.png'
        found = find_file(target_filename)
        if found:
            continue
        target_filename = str(pic) + '.mat'
        found = find_file(target_filename)
        if found:
            continue
        res.add(target_filename)
        sys.stdout.write('\r' + ' ' * len(output) + '\r')
        print(f"'{target_filename}' not found in '{pictures_folder}' or its subfolders.")
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
        if old_value == new_value:
            continue
        changes["modified_values"][key] = {
            "added": list(new_value - old_value),
            "removed": list(old_value - new_value)
        }

    return changes


def version_comparison():
    # 版本对照
    version_new = get_key_dict_base_data()
    version_old = version_new
    try:
        with open("../report/comparison_2024-10-10-19-43-48.txt", "r", encoding="utf-8") as file:
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
    for pic_path_data in excelConfig.pic_path_data_dict:
        # pictures = get_pictures_by_excel(pic_path_data)
        # print(pictures)
        pictures = get_pictures_by_base_data(pic_path_data)
        print(pictures)
        check_result = check_pictures(pic_path_data, pictures)
        res |= check_result
    if res:
        print(f"找不到的资源为{res}")
        return
    print("资源都找到了")


if __name__ == '__main__':
    # unity工程路径，需根据自己配置
    root_path = 'C:/trunkCHS'
    # 图片资源路径

    pictures_folder = root_path + '/client/MainProject/Assets/InBundle'

    # 配置表路径
    excel_path = root_path + r"/datapool/策划模板导出工具/"
    excel_tools = ExcelTools(excel_path)
    base_data_path = root_path + r"/datapool/ElementData/BaseData/"

    # 版本对比
    # version_comparison()

    main()
