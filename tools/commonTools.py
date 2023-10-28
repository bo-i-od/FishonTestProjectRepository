from common.error import *
import ctypes
import inspect
# 对比值或对象，不一致报错



def compare(a, b):
    if a != b:
        raise DifferError


def compare_list(list_a, list_b):
    for a in list_a:
        if a in list_b is False:
            raise DifferError


def checktoggle(toggle_is_on_list, index):
    cur = 0
    while cur < len(toggle_is_on_list):
        if cur == index and toggle_is_on_list[cur] is False:
            raise DifferError
        if cur != index and toggle_is_on_list[cur] is True:
            raise DifferError
        cur += 1


def str_to_int_list(str_list):
    cur = 0
    while cur < len(str_list):
        str_list[cur] = int(str_list[cur])
        cur += 1


def positive_percentage_to_float_list(text:str = "", text_list:list = None):
    if text != "":
        text = float(text.split('+')[1].split('%')[0])
        return text
    cur = 0
    while cur < len(text_list):
        text_list[cur] = float(text_list[cur].split('+')[1].split('%')[0])
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



def unit_conversion_str_to_int(count:str):
    if count[-1:] == 'K':
        return int(count[:-1]) * 1000
    elif count[-1:] == 'M':
        return int(count[:-1]) * 1000000
    else:
        return int(count)

if __name__ == '__main__':
    a = unit_conversion_str_to_int("10M")
    print(a)
