import os
import re
import keyword

type_dict = {"i64": "int", "i32": "int", "i16": "int", "i8": "int", "string": "str", "bool": "bool", "double": "float", "binary": "bytes"}

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
        fields = re.findall(r"\n\s*(\d+): optional ((?:\w+<.+?>|\w+)) (\w+)", st[1])
        for field in fields:
            # print("Field Number:", field[0])
            field_type = field[1]  # 主类型
            # print("Field Type:", field_type)
            # print("Field Name:", field[2])
            struct["struct_args"][field[2]] = field_type
        struct_list.append(struct)
        # print("---------------------------------------------------")
    res["struct_list"] = struct_list
    return res


# 根据thrift数据生成对应的py
def gen_py(thrift_data):
    file_path = "csMsg/"
    code = ""
    # 直接沿用thrift的名称
    file_name = thrift_data['file_name'] + '.py'
    file_path = file_path + file_name
    struct_list = thrift_data['struct_list']
    if not struct_list:
        return code

    # 添加内容
    cur = 0
    while cur < len(struct_list):
        struct = struct_list[cur]
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
        cmd_part += f'cmd.{arg_list[cur]} = {{arg}}\n'
        """
        # cmd_part += rf"f'cmd.{arg_list[cur]} = {{{arg_list[cur]}}}\n'"
        cur += 1
        if cur < len(arg_list):
            comment += ", "
    # 空就不留参数位置
    if ignore_check == "":
        code = rf"""
        
def get_{msg_name}({args_str}):
    lua_code = ('local cmd = NetworkMgr:NewMsg("{msg_name}")\n'
    'NetworkMgr:Send(cmd)')
    return lua_code
    """
        return code

    # 不为空就给参数赋值
    code = rf"""

# # {comment}
def get_{msg_name}({args_str}):
    {ignore_check}
    lua_code = ('local cmd = NetworkMgr:NewMsg("{msg_name}")\n'
    f'{{cmd_part}}'
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
        return "str"
    if "map" in type_str:
        return "dict"
    if "set" in type_str:
        return "set"
    if type_str in type_dict:
        return type_dict[type_str]
    print(f"warning:{type_str}未处理")
    return None


def main():
    file_list = os.listdir(folder_path)
    code = ""
    for file in file_list:
        if file[-9:] != "cs.thrift":
            continue
        thrift_data = get_thrift_data(file)
        print(thrift_data)
        code += gen_py(thrift_data)
    print(code)
    with open("csMsgAll.py", 'w') as f:
        f.write(code)



if __name__ == '__main__':
    folder_path = 'C:\\Dev\\tools\\gen-message\\messages\\'
    main()

