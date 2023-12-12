from common.error import *
import ctypes
import inspect
import re
# 对比值或对象，不一致报错



def compare(a, b):
    if a != b:
        raise DifferError


def compare_list(list_a, list_b):
    compare(len(list_a), len(list_b))
    for a in list_a:
        if (a in list_b) is False:
            raise DifferError

def compare_dict(dict_a, dict_b):
    compare(len(dict_a), len(dict_b))
    for key in dict_a:
        compare(dict_a[key], dict_b[key])


def checktoggle(toggle_is_on_list, index):
    cur = 0
    while cur < len(toggle_is_on_list):
        if cur == index and toggle_is_on_list[cur] is False:
            raise DifferError
        if cur != index and toggle_is_on_list[cur] is True:
            raise DifferError
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


def unit_conversion_int_to_str(count:int):
    if count < 10000:
        return str(count)
    elif count < 10000000:
        return str(int(count/1000)) + "K"
    elif count < 10000000000:
        return str(int(count / 1000000)) + "M"


def str_to_int(count:str):
    if count[-1:] == 'K':
        return int(count[:-1]) * 1000
    elif count[-1:] == 'M':
        return int(count[:-1]) * 1000000
    else:
        return int(count)

def str_to_int_list(count_list:list):
    cur = 0
    while cur < len(count_list):
        if count_list[cur][-3:] == 'min':
            count_list[cur] = 0
        elif count_list[cur][-1:] == 'K':
            count_list[cur] = int(count_list[cur][:-1]) * 1000
        elif count_list[cur][-1:] == 'M':
            count_list[cur] = int(count_list[cur][:-1]) * 1000000
        else:
            count_list[cur] = int(count_list[cur])
        cur += 1



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




if __name__ == '__main__':
    a = split_string_by_uppercase("Bartletts Anthias")
    print(a)
