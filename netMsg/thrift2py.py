import os
import re


from configs.pathConfig import thrift2py_folder_path

type_dict = {"i64": "int", "i32": "int", "i16": "int", "i8": "int", "string": "str", "bool": "bool", "double": "float", "binary": "bytes", "MergeProductType": "str", "CSAquariumNewFish": "str", "CSAquariumNewSpeedUpFish": "str", "NewLotteryDrawType": "str" }

# 把thrift文件需要的内容解析出来
def get_thrift_data(file_name):
    # 使用open()函数打开文件，文件路径为'path_to_file'（替换为你自己的文件路径）
    f = open(folder_path + file_name, 'r', encoding="utf-8")
    # 使用read()函数读取文件内容
    file_content = f.read()
    f.close()
    res = {'file_name': file_name.split('.')[0]}
    struct_list = []
    structs = re.findall(r"(?s)struct (.+?)\s*\{(.+?)\}", file_content)
    for st in structs:
        struct = {"struct_name": st[0].strip(), "struct_args": {}}

        # 使用正则表达式匹配字段
        fields = re.findall(r"\n\s*(\d+): (required|optional) ((?:\w+<.+?>|\w+)) (\w+)", st[1])
        for field in fields:
            # print("Field Number:", field[0])
            field_type = field[2]  # 主类型
            # print("Field Type:", field_type)
            # print("Field Name:", field[2])
            struct["struct_args"][field[3]] = field_type
        struct_list.append(struct)
        # print("---------------------------------------------------")
    res["struct_list"] = struct_list
    return res


# 根据thrift数据生成对应的py
def gen_py(thrift_data):
    file_root = "csMsg/"
    code = ""
    # 直接沿用thrift的名称
    file_name = thrift_data['file_name'] + '.py'
    file_path = file_root + file_name
    struct_list = thrift_data['struct_list']
    if not struct_list:
        return code

    # 添加内容
    cur = 0
    while cur < len(struct_list):
        struct = struct_list[cur]

        # 一个结构体生成一个对应的消息生成方法
        # 然后加到一起
        code += gen_py_function(struct)
        cur += 1

    # 写入所有内容
    with open(file_path, 'w') as f:
        f.write(code)
    return code


# 根据结构体生成对应的方法
def gen_py_function(struct):
    msg_name = struct['struct_name']
    struct_args = struct['struct_args']
    arg_list = list(struct_args)
    args_str = ""
    comment = ""
    ignore_check = "cmd_part = ''"
    cur = 0
    while cur < len(arg_list):
        # 每个变量后逗号分隔
        if cur > 0:
            args_str += ', '
        args_str += arg_list[cur]

        # 每个变量添加类型限制，设默认值为None
        py_type = thrift_type_to_py_type(struct_args[arg_list[cur]])
        comment += arg_list[cur] + ": " + struct_args[arg_list[cur]]
        if py_type is not None:
            args_str += f': {py_type} = None'


        # lua cmd.部分
        ignore_check += rf"""
    if {arg_list[cur]} is not None:
        arg = {arg_list[cur]}
        if isinstance({arg_list[cur]}, str):
            arg = f'"{{{arg_list[cur]}}}"'
        if isinstance({arg_list[cur]}, bool):
            arg = str({arg_list[cur]}).lower()
        if isinstance({arg_list[cur]}, list):
            arg = '{{'
            for index, j in enumerate({arg_list[cur]}):
                arg += f'[{{index + 1}}] = {{j}},'
            arg += '}}'
        cmd_part += f'cmd.{arg_list[cur]} = {{arg}}\n'
        """
        # cmd_part += rf"f'cmd.{arg_list[cur]} = {{{arg_list[cur]}}}\n'"
        cur += 1
        if cur < len(arg_list):
            comment += ", "
    # 空就不留参数位置
    if ignore_check == "":
        code = rf"""
        
def get_{msg_name}(addition_part="", {args_str}):
    lua_code = ('local cmd = NetworkMgr:NewMsg("{msg_name}")\n'
    f'{{addition_part}}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    """
        return code

    # 不为空就给参数赋值
    code = rf"""

# # {comment}
def get_{msg_name}(addition_part="", {args_str}):
    {ignore_check}
    lua_code = ('local cmd = NetworkMgr:NewMsg("{msg_name}")\n'
    f'{{cmd_part}}'
    f'{{addition_part}}'
    'NetworkMgr:Send(cmd)')
    return lua_code
    """
    return code

# def gen_lua_code():
#     lua_code = (f'local cmd = NetworkMgr:NewMsg("CSFishingSaveLimitedSpotEnergyCostIdMsg")\n'
#                 f'cmd.chooseEnergyCostId = {tpId_list[index]}\n'
#                 'NetworkMgr:Send(cmd)')
#     return lua_code


# 把thrift转py类型用作限定
def thrift_type_to_py_type(type_str):
    if "list" in type_str:
        # result = re.findall(r"list<(.+?)>", type_str)
        return "list"
    if "map" in type_str:
        return "dict"
    if "set" in type_str:
        return "set"
    if type_str in type_dict:
        return type_dict[type_str]
    print(f"warning:{type_str}未处理")
    return None


def gen_test_py(thrift_data):
    file_root = "csMsgTest/"
    code_dict = ""
    code_function = ""
    code_main = ""
    # 直接沿用thrift的名称
    file_name = thrift_data['file_name'] + '_Test.py'
    file_path = file_root + file_name
    struct_list = thrift_data['struct_list']
    if not struct_list:
        return code_dict, code_function, code_main

    # 添加内容
    cur = 0
    while cur < len(struct_list):
        struct = struct_list[cur]
        code_dict += gen_test_py_dict(struct)
        cur += 1

    # 添加内容
    content = ""
    cur = 0
    while cur < len(struct_list):
        struct = struct_list[cur]
        content += gen_test_py_function(struct)
        cur += 1
    function_name = f"{thrift_data['file_name'][:-3]}_test"
    code_function = f"""\n\n
def {function_name}(self):
    res = {{}}
{content}
    return res"""

    # 写入所有内容
    with open(file_path, 'w') as f:
        f.write('{' + code_dict + '}' + code_function)
    code_main = f"""
    res.update(self.{function_name}())"""
    return code_dict, code_function, code_main


def gen_test_py_dict(struct):
    struct_args = struct['struct_args']
    arg_list = list(struct_args)
    args_str = ""
    comment = ""
    cur = 0
    while cur < len(arg_list):
        # 每个变量后逗号分隔
        if cur > 0:
            args_str += ', '
        args_str += arg_list[cur]

        # 每个变量添加类型
        if struct_args[arg_list[cur]] in type_dict:
            comment += f'"{arg_list[cur]}": {type_dict[struct_args[arg_list[cur]]]}, '
        else:
            comment += f'"{arg_list[cur]}": {thrift_type_to_py_type(struct_args[arg_list[cur]])}, '
        cur += 1

    msg_name = struct['struct_name'][2:]
    code = f'"{msg_name}": {{"msg_arg": {{{comment}}}, "expect_reply": {{"msg": ["success"], "code": ["0"]}}}},\n'
    return code


def gen_test_py_function(struct):
    msg_name = struct['struct_name'][2:]
    code = f'\n    res.update(self.msg_test("{msg_name}"))\n'
    return code



def main():
    # 获取协议文件名
    file_list = os.listdir(folder_path)
    code = ""
    for file in file_list:
        if file[-9:] != "cs.thrift":
            continue
        # 获取协议内容
        # 包括1.文件名 2.结构体名及其变量名和类型
        thrift_data = get_thrift_data(file)

        # 生成协议转换代码
        code += gen_py(thrift_data)

    # 写入到csMsgAll.py中
    with open("csMsgAll.py", 'w') as f:
        f.write(code)

    # 生成测试代码
    # 分别取到字典和方法进行累加
    code_dict, code_function = "", ""
    code_main = """\n\n
def main(self):
    res = {}
    """
    for file in file_list:
        if file[-9:] != "cs.thrift":
            continue
        thrift_data = get_thrift_data(file)
        cd, cf, cm = gen_test_py(thrift_data)
        code_dict += cd
        code_function += cf
        code_main += cm

    # 加上括号
    code_dict = 'msg_data = {' + code_dict + '}'

    # 写入
    with open("csMsgTestAll.py", 'w') as f:
        code = code_dict + code_function + code_main
        f.write(code)



if __name__ == '__main__':
    folder_path = thrift2py_folder_path
    try:
        main()
        print("协议解析生成成功")
    except Exception as e:
        print(e)
        print("协议解析生成失败")

