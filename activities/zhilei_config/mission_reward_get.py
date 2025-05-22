def generate_data(num, title):
    result = []
    # 遍历num数组
    for row in num:
        # 跳过空行
        if not row:
            continue

        # 生成每行数据
        line = []

        for i in range(0, len(row)):
            if row[i] is not None and row[i] != 0:
                line.extend([int(title[i] / 100000), title[i], row[i], 0])

        # 如果没有任何有效数据，跳过该行
        if not line:
            continue

        # 确保每行有9个元素
        while len(line) < 12:
            line.extend([0, 0, 0, 0])

        # 将行转换为字符串并添加到结果中
        result.append("\t".join(map(str, line[:12])))

    return "\n".join(result)


def main():
    # 输入数据
    num = [
        [0, 30000, 300, 0, 0],
        [1, 0, 0, 500, 500],
        [0, 30000, 300, 0, 0],
        [1, 0, 0, 500, 500],
        [1, 50000, 500, 0, 0],
        [1, 0, 0, 700, 700],
        [2, 100000, 1000, 0, 0],
        [0, 30000, 300, 0, 0],
        [0, 0, 0, 400, 400],
        [1, 50000, 500, 0, 0],
        [1, 0, 0, 500, 500],
        [1, 70000, 700, 0, 0],
        [2, 0, 0, 1000, 1000],
    ]

    title = [102700, 9700002, 9700003, 9700004, 9700005]

    # 生成数据
    output = generate_data(num, title)
    print("生成的数据：")
    print(output)


if __name__ == "__main__":
    main()