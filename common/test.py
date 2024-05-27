from typing import List

import os

import netMsg.achieve_cs


def count_lines(file_path):
    with open(file_path, 'r', encoding='gbk', errors='ignore') as file:
        count = sum(1 for line in file if line.strip() != '')
    return count


def count_code_lines(directory):
    total_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                count = count_lines(file_path)
                total_count += count
    return total_count

def move(m,n):
    if m == 1 and n == 1:
        return 0
    if m == 1:
        return 1
    if n == 1:
        return 1
    return move(m - 1, n) + move(m, n - 1)

def fun_test(a, b):
    if a < 10:
        return b - 1
    if b > 4:
        return b + 2
    while a > b:
        b += 1
    return b

def ab(s:str):
    cur = 0
    count = 0
    while cur < len(s):
        if s[cur] == 'a':
            count += 1
            cur += 1
            continue
        count -= 1
        if count < 0:
            return False
        cur += 1
    if count == 0:
        return True
    return False
if __name__ == '__main__':
    # input = "abab"
    # res = ab(input)
    # print(res)
    # print(move(4, 4))
    # project_directory = 'D:\FishonTestProject'
    # code_line_count = count_code_lines(project_directory)
    # print(f"Total code lines: {code_line_count}")
    pass






















