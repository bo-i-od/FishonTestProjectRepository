import json
import os
import pickle


def save_main_id(file_name, id_dict):
    file_path = os.path.join(os.path.dirname(__file__)) + fr"\{file_name}.txt"
    print(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(id_dict, file, ensure_ascii=False, indent=4)

def load_main_id(file_name):
    file_path = os.path.join(os.path.dirname(__file__)) + fr"\{file_name}.txt"
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            dictionary = json.load(file)
        print(f"已从 {file_path} 成功读取主键id")
        return dictionary
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return None



if __name__ == '__main__':
    load_main_id(file_name="fish_bag.txt")
