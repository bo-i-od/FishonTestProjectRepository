import re


def extract_msg_names(function_str):
    pattern = r'self\.msg_test\("([^"]*)"\)'  # 匹配双引号包裹的字符串
    match = re.findall(pattern, function_str)
    return match


def extract_keys(content):
    pattern = r'("[^"]+"):'  # 匹配引号括起来的字符串,后面跟一个冒号
    keys = re.findall(pattern, content)
    keys = [key[1:-1] for key in keys]  # 去掉双引号
    cur = 0
    while cur < len(keys):
        if "Msg" in keys[cur]:
            cur += 1
            continue
        keys.remove(keys[cur])
    return keys


def extract_function_names(content):
    # 正则表达式模式匹配函数定义
    pattern = r'def\s+(\w+)\s*\('

    # 使用re.findall查找所有匹配的函数名
    function_names = re.findall(pattern, content)
    return function_names


def get_test_content(file_path):
    f = open(file_path, "r", encoding="utf-8")
    content = f.read()
    f.close()

    keys = extract_keys(content)

    function_names = extract_function_names(content)

    msg_names = extract_msg_names(content)

    return keys, function_names, msg_names


def compare_test_content():
    keys_recently, function_names_recently, msg_names_recently = get_test_content("../netMsg/csMsgTestAll.py")
    keys_previous, function_names_previous, msg_names_previous = get_test_content("../netMsg/netMsgTest.py")
    keys_recently, function_names_recently, msg_names_recently, keys_previous, function_names_previous, msg_names_previous = set(keys_recently), set(function_names_recently), set(msg_names_recently), set(keys_previous), set(function_names_previous), set(msg_names_previous)
    keys_add = keys_recently - keys_previous
    keys_del = keys_previous - keys_recently
    function_names_add = function_names_recently - function_names_previous
    function_names_del = function_names_previous - function_names_recently
    msg_names_add = msg_names_recently - msg_names_previous
    msg_names_del = msg_names_previous - msg_names_recently
    if keys_add != set():
        print(f"新增消息：{keys_add}")
    if keys_del != set():
        print(f"删减消息：{keys_del}")
    if function_names_add != set():
        print(f"新增方法名：{function_names_add}")
    if function_names_del != set():
        print(f"删减方法名：{function_names_del}")
    if msg_names_add != set():
        print(f"新增消息测试：{msg_names_add}")
    if msg_names_del != set():
        print(f"删减消息测试：{msg_names_del}")





if __name__ == '__main__':

    compare_test_content()