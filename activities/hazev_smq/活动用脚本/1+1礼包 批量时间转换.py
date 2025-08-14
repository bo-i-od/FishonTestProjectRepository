import sys
from datetime import datetime

def convert_time_format(line):
    line = line.strip()
    if not line:
        return ""
    # 拆分考虑tab和多种空格
    parts = [x for x in line.replace('\t', ' ').split(' ') if x]
    if len(parts) < 2:
        return ""
    try:
        # 先合并日期与时间
        if ':' in parts[0] and ':' in parts[1]:
            start_str = parts[0] + ' ' + parts[1]
            end_str = parts[2] + ' ' + parts[3]
        elif ':' in parts[1]:
            start_str = parts[0] + ' ' + parts[1]
            end_str = parts[2] + ' ' + parts[3]
        else:
            start_str = parts[0]
            end_str = parts[1]
        start = datetime.strptime(start_str, "%Y/%m/%d %H:%M:%S")
        end = datetime.strptime(end_str, "%Y/%m/%d %H:%M:%S")
        return f"{start.strftime('%Y-%m-%d %H:%M:%S')}\t{end.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Error parsing: {line}"

if __name__ == "__main__":
    print("请粘贴所有待转换的时间组，输入完后按 Ctrl+D (Linux/macOS) 或 Ctrl+Z (Windows) 结束输入：")
    lines = sys.stdin.read().split('\n')   # 一次性读取所有
    for line in lines:
        res = convert_time_format(line)
        if res:
            print(res)