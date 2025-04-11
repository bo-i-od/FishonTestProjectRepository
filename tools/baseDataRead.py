import os
import re


def parse_decl_file(decl_file):
    encodings = ['gb2312', 'utf-8', 'gbk', 'gb18030', 'utf-16']
    content = None

    for encoding in encodings:
        try:
            with open(decl_file, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue

    structs = {}
    struct_matches = re.finditer(r'struct\s+(\w+)\s*(?://[^\n]*)?\s*{([^}]+)};', content, re.DOTALL)

    for match in struct_matches:
        struct_name = match.group(1)
        struct_content = match.group(2)
        # 清理注释
        cleaned_content = re.sub(r'//.*$', '', struct_content, flags=re.MULTILINE)

        # 改进的字段匹配正则表达式
        fields = re.findall(r'(\w+(?:\s*\*)?)\s+(\w+)(?:\s*(\[\s*\])?)?\s*;?', cleaned_content)
        struct_fields = {}
        for field_type, field_name, is_array in fields:
            if is_array:
                struct_fields[field_name] = (field_type, True)
                continue
            struct_fields[field_name] = (field_type, False)
        structs[struct_name] = struct_fields

    return structs


def parse_value(value, field_type):
    if field_type == 'int':
        return int(value)
    elif field_type == 'float':
        return float(value)
    elif field_type == 'string':
        return value
    else:
        return value  # 对于复杂类型，保持字符串形式


def parse_data_file(data_file):
    encodings = ['utf-8', 'utf-16', 'gbk', 'gb18030', 'gb2312']
    content = None

    for encoding in encodings:
        try:
            with open(data_file, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    struct_name = data_file.split(".")[0].split("/")[-1].lower()

    blocks = content.split(struct_name + '{')
    blocks = blocks[1:]
    # 处理每个块
    cleaned_blocks = []
    for block in blocks:
        # 移除开头的 '{' 和结尾的 '};'，然后去除首尾空白
        cleaned_block = block.strip().strip('};').strip()
        if cleaned_block:  # 只添加非空的块
            cleaned_blocks.append(cleaned_block)
    return cleaned_blocks


def deal_with_blocks(structs, blocks, prefix):
    result = []
    for block in blocks:
        lines = block.split('\n')
        data = deal_with_lines(structs, lines, prefix)
        result.append(data)

    return result


def deal_with_lines(structs, lines, prefix):
    current_struct = (prefix, True)
    data, delta = deal_with_struct(structs, lines, current_struct, -1)
    return data


def deal_with_struct(structs, lines, struct, start):
    i = start
    i += 1
    res = {}
    while i < len(lines) and '}' not in lines[i]:
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip().strip('";')
            field_info = structs[struct[0]].get(key, ('string', False))

            if field_info[1]:  # 是数组
                if key not in res:
                    res[key] = []
                res[key].append(parse_value(value, field_info[0]))
                i += 1
                continue
            res[key] = parse_value(value, structs[struct[0]][key][0])
            i += 1
            continue
        if '{' not in line:
            i += 1
            continue
        field_name = line.split('{')[0]
        current_field = field_name
        current_struct = structs[struct[0]][current_field]
        if current_struct[1]:
            if current_field not in res:
                res[current_field] = []
            value, delta = deal_with_struct(structs, lines, current_struct, i)
            res[current_field].append(parse_value(value, current_struct[0]))
            i += delta
            continue
        res[current_field], delta = deal_with_struct(structs, lines, current_struct, i)
        i += delta
    return res, i - start + 1


def convert_to_json(path, prefix):
    decl_file = path + prefix + '.decl.h'
    data_file = path + prefix + '.data.txt'
    try:
        structs = parse_decl_file(decl_file)
        blocks = parse_data_file(data_file)
    except FileNotFoundError:
        return [], {}, ""
    res = deal_with_blocks(structs, blocks, prefix)
    return res, structs, prefix




def get_files_in_current_directory(directory):
    """
    获取指定目录下（不包括子目录）所有文件的文件名。

    :param directory: 要搜索的目录路径
    :return: 包含所有文件名的列表
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_prefix_list(files):
    prefix_set = set()
    for file in files:
        prefix = file.split(".")[0]
        prefix_set.add(prefix)
    return list(prefix_set)

if __name__ == '__main__':
    path = r"C:/trunkCHS/datapool/ElementData/BaseData/"
    files = get_files_in_current_directory(path)
    a = get_prefix_list(files)
    for b in a:
        try:
            print(b)
            convert_to_json(path, b)
        except FileNotFoundError:
            pass
        except Exception as e:
            print("------------------")
            print(e)
            print("------------------")
    # convert_to_json(path,  'FISH')
