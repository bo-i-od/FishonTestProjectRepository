from common.basePage import BasePage


if __name__ == '__main__':
    bp = BasePage()
    # 读取截屏
    filename = 'C:/Users/TU/Desktop/report/log.txt'  # 替换为实际的文件路径
    fish_set= set()
    # 打开文件
    with open(filename, 'r') as file:
        # 使用 read() 方法读取整个文件内容
        file_content = file.read()
        # print(file_content)
        fish_list2 = []
        # # 使用 readlines() 方法按行读取文件内容
        file.seek(0)  # 将文件的指针移到开头
        lines = file.readlines()
        for line in lines:
            data = int(line.split('\n')[0])
            fish_set.add(data)
            fish_list2.append(data)

    fish_list = list(fish_set)

    tpid = "tpId"
    fishtype = "fishType"
    worksheet = bp.excelTools.get_worksheet("FISH.xlsm", "模板数据")
    res_list = bp.excelTools.same_row_different_column_convert_list(worksheet=worksheet, source_header=tpid,target_header=fishtype, source_list=fish_list)
    fish_dict = {}
    cur = 0
    while cur < len(fish_list):
        fish_dict[fish_list[cur]] = res_list[cur]
        cur += 1
    cur = 0
    s = 0
    m = 0
    l = 0
    h = 0
    b = 0
    other = 0
    for fish in fish_list2:
        cur += 1
        if fish_dict[fish] == 1:
            s += 1
            continue
        if fish_dict[fish] == 2:
            m += 1
            continue
        if fish_dict[fish] == 3:
            l += 1
            continue
        if fish_dict[fish] == 4:
            h += 1
            continue
        if fish_dict[fish] == 5:
            b += 1
            continue
        other += 1

    print(s/cur,m/cur,l/cur,h/cur,b/cur,other/cur)
    print(cur)
    "small:44%,medium:29%,large:19%,hidden:5%,boss:4%"



















