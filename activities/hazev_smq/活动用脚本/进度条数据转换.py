# 在这里输入您的四列数据
data = """
5	97	9700001	8
10	1	100100	25
15	2	205009	1
25	2	201001	2
50	1	100100	50
30	97	9700001	48
35	2	201001	2
40	1	100100	40
50	97	9700001	80
160	1	100100	150
50	1	100210	80
55	1	100100	50
65	97	9700001	104
80	2	201002	3
425	1	100100	375
70	97	9700001	112
80	1	100100	70
85	2	205014	1
95	1	100210	152
675	1	100100	575
100	97	9700001	160
115	1	100100	95
110	1	100210	176
130	97	9700001	208
1150	1	100100	925
140	2	201003	3
150	97	9700001	240
160	1	100210	256
750	1	100100	575
180	97	9700001	288
190	1	100210	304
210	1	100100	150
160	2	205009	1
230	1	100210	368
1500	1	100100	1100
250	97	9700001	400
300	1	100100	200
450	1	100210	720
1350	1	100100	925
325	1	100210	520
350	97	9700001	560
375	1	100210	600
2250	1	100100	1400
350	2	205003	1
450	97	9700001	720
575	1	100100	350
500	1	100210	800
3000	1	100100	1650
550	97	9700001	880
450	2	205007	1
650	1	100210	1040
1800	1	100100	800
700	97	9700001	1120
825	1	100100	500
950	1	100210	1520
4500	1	100100	2200
500	2	205010	1
800	1	100100	375
950	1	100210	1520
1400	1	100100	625
1500	1	100210	2400
10000	1	100100	5000
"""


def convert_data():
    # 存储结果
    result = []

    # 处理输入数据
    lines = data.strip().split('\n')

    print("原始数据：")
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        print(f"第{i}行: {line}")

        # 支持Tab和空格分隔
        if '\t' in line:
            row_data = line.split('\t')
        else:
            row_data = line.split()

        # 将当前行的所有数据添加到结果中（头尾接续）
        result.extend(row_data)

    print("\n转换过程：")
    current_pos = 0
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        row_data = line.split('\t') if '\t' in line else line.split()
        row_length = len(row_data)
        row_result = result[current_pos:current_pos + row_length]
        print(f"第{i}行数据: {' '.join(row_result)}")
        current_pos += row_length

    print("\n转换结果（Tab分隔，可直接复制到Excel）：")
    print("\t".join(result))

    print(f"\n共{len(result)}个数值")

    return result


# 执行转换
convert_data()