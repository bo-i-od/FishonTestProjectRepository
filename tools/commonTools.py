from slpp import slpp
from common.error import *
import ctypes
import inspect
import re
from collections import Counter


# 对比值或对象，不一致报错
def compare(a, b):
    if a != b:
        print(f"erro{a,b}")
        # raise DifferError(f"a,b:{a,b}")


# 比较列表中的
def compare_list(list_a, list_b):
    if Counter(list_a) != Counter(list_b):
        # raise DifferError(f"list_a, list_b:{list_a, list_b}")
        print(f"erro{list_a, list_b}")


def compare_dict(dict_a, dict_b):
    if len(dict_a) != len(dict_b):
        print(sort_dict_recursively(dict_a), sort_dict_recursively(dict_b))
        return
    for key in dict_a:
        compare(dict_a[key], dict_b[key])




def checktoggle(toggle_is_on_list, index):
    cur = 0
    while cur < len(toggle_is_on_list):
        if cur == index and toggle_is_on_list[cur] is False:
            raise DifferError(f"cur,index,toggle_is_on_list[cur]{cur,index,toggle_is_on_list[cur]}")
        if cur != index and toggle_is_on_list[cur] is True:
            raise DifferError(f"cur,index,toggle_is_on_list[cur]{cur,index,toggle_is_on_list[cur]}")
        cur += 1


# def str_to_int_list(str_list):
#     cur = 0
#     while cur < len(str_list):
#         try:
#             str_list[cur] = int(str_list[cur])
#         except:
#             str_list[cur] = 0
#         cur += 1


def positive_percentage_to_float(text:str = "", text_list:list = None):
    if text != "":
        if '+' in text:
            text = text.split('+')[1]
        text = float(text.split('%')[0])
        return text
    cur = 0
    while cur < len(text_list):
        if '+' in text_list[cur]:
            text_list[cur] = text_list[cur].split('+')[1]
        text_list[cur] = float(text_list[cur].split('%')[0])
        cur += 1


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")



def stop_thread( thread):
    _async_raise(thread.ident, SystemExit)


def unit_conversion_int_to_str(count: int, significant_digits=0):
    if count < 10000:
        return str(count)
    elif count < 10000000:
        return str(int(count/1000)) + "K"
    elif count < 10000000000:
        return str(int(count / 1000000)) + "M"
    elif count < 10000000000000:
        return str(int(count / 1000000000)) + "B"

def unit_conversion_int_to_str_chs(count: int, significant_digits=0):
    if count < 10000:
        return str(count)
    elif count < 100000000:
        return str(int(count/10000)) + "万"
    elif count < 1000000000000:
        return str(int(count / 100000000)) + "亿"
    elif count < 10000000000000000:
        return str(int(count / 1000000000000)) + "兆"



def remove_decimals(value_with_unit):
    # 正则表达式匹配小数点后的数字
    pattern = re.compile(r"(\.\d+)")
    # 替换为空字符串，即删除小数点后的数字
    return pattern.sub('', value_with_unit)


def str_to_int(count:str):
    if count[-1:] == 'K':
        return int(float(count[:-1]) * 1000)
    elif count[-1:] == 'M':
        return int(float(count[:-1]) * 1000000)
    elif count[-1:] == 'B':
        return int(float(count[:-1]) * 1000000000)
    elif count[-1:] == '万':
        return int(float(count[:-1]) * 10000)
    elif count[-1:] == '亿':
        return int(float(count[:-1]) * 100000000)
    else:
        return int(float(count))


def extract_number(text):
    # 使用正则表达式来匹配数字模式
    number_pattern = r'[-+]?\d*\.?\d+'

    # 使用 search() 方法来找到第一个符合这个模式的子字符串
    match = re.search(number_pattern, text)

    if match:
        # 获取匹配的字符串
        number_str = match.group(0)
        return number_str
    else:
        # 如果没有找到符合的数字，返回 None 或抛出异常
        return None

def str_to_int_list(count_list:list):
    cur = 0
    while cur < len(count_list):
        if len(count_list[cur]) > 2 and count_list[cur][-3:] == 'min':
            count_list[cur] = 0
        elif count_list[cur][-1:] == 'K':
            count_list[cur] = int(float(count_list[cur][:-1]) * 1000)
        elif count_list[cur][-1:] == 'M':
            count_list[cur] = int(float(count_list[cur][:-1]) * 1000000)
        elif count_list[cur][-1:] == '万':
            count_list[cur] = int(float(count_list[cur][:-1]) * 10000)
        elif count_list[cur][-1:] == '亿':
            count_list[cur] = int(float(count_list[cur][:-1]) * 100000000)
        else:
            count_list[cur] = int(float(count_list[cur]))
        cur += 1

def str_to_int_list_oversea(count_list):
   count_list = float(count_list[0].split(' ')[1])


def split_string_by_uppercase(string):
    pattern = r"(?=[A-Z])"
    substrings = re.split(pattern, string)
    return substrings

def get_toggle_is_on_index(toggle_is_on_list:list):
    cur = 0
    res = -1
    while cur < len(toggle_is_on_list):
        if toggle_is_on_list[cur]:
            res = cur
            break
        cur += 1
    return res

def merge_list(list_before_merge):
    list_after_merge = []
    for child_list in list_before_merge:
        list_after_merge += child_list
    return list_after_merge


def get_img_position(query,img):
    if img is None:
        print("屏幕可能锁定")
        return
    match_pos = query.match_in(img)
    return match_pos


def lua_dict_to_python_dict(lua_string):
    lua_string = lua_string.split("\n", 1)[1]
    # 解析 Lua 字符串并装换为 Python dict
    data = slpp.decode(lua_string)
    return data

def sort_dict_recursively(d):
    # 如果是字典类型，进行递归排序
    if isinstance(d, dict):
        # 创建一个新的有序字典
        return {
            key: sort_dict_recursively(value)
            for key, value in sorted(d.items())
        }
    # 如果是列表类型，对列表中的每个元素进行递归排序
    elif isinstance(d, list):
        return [sort_dict_recursively(item) for item in d]
    # 如果是其他类型，直接返回
    else:
        return d




if __name__ == '__main__':
    compare_list(["0.5",2,3],["0.5",3,2])

