import re

def parse_fields(text):
    """
    解析类似C结构的字段，返回 dict: 字段名 -> 备注
    """
    field_dict = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        # 匹配 字段名、尾注释
        match = re.match(r".*?([a-zA-Z_][\w$$$$]*)\s*;\s*(//(.*))?", line)
        if match:
            name = match.group(1).replace("[]", "")  # 如果有数组，去掉[]
            comment = match.group(3).strip() if match.group(3) else ""
            field_dict[name] = comment
    return field_dict

def print_fields(fields, title):
    print(f"\n{title}：")
    for field, comment in fields.items():
        print(f"  {field:20s} | {comment}")
    print()

def compare_fields(fields1, fields2):
    set1 = set(fields1.keys())
    set2 = set(fields2.keys())

    only_in_1 = set1 - set2
    only_in_2 = set2 - set1
    diff_comment = set(k for k in (set1 & set2) if fields1[k] != fields2[k])

    if only_in_1:
        print("只在第一批出现的字段：")
        for k in only_in_1:
            print(f"  {k:20s} | {fields1[k]}")
        print()
    if only_in_2:
        print("只在第二批出现的字段：")
        for k in only_in_2:
            print(f"  {k:20s} | {fields2[k]}")
        print()
    if diff_comment:
        print("字段备注有差异的字段：")
        for k in diff_comment:
            print(f"  {k:20s} | 第一批:'{fields1[k]}', 第二批:'{fields2[k]}'")
        print()
    if not (only_in_1 or only_in_2 or diff_comment):
        print("两批字段完全一致！")

def input_fields(batch_num):
    print(f"\n请粘贴第 {batch_num} 批字段，每行一个字段，直接按空回车结束：")
    lines = []
    while True:
        line = input()
        if line.strip() == '':
            break
        lines.append(line)
    return '\n'.join(lines)

if __name__ == "__main__":
    print("字段对比工具（粘贴字段，空行直接进入下一步）")
    text1 = input_fields(1)
    text2 = input_fields(2)
    fields1 = parse_fields(text1)
    fields2 = parse_fields(text2)

    print_fields(fields1, "第一批字段")
    print_fields(fields2, "第二批字段")
    compare_fields(fields1, fields2)
