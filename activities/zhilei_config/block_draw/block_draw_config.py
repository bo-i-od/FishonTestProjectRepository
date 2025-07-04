level_config=[
[1,2],
[2,4],
[3,5],
[4,7],
[5,8],
[6,10],
[7,14],
[8,14],
[9,14],
[10,14],
[11,15],
[12,16],
[13,17],
]
weight_list=[
[0,10,5], # 不出1
[85,10,4], # 出1、2、3
[85,10,0], # 不出3
[85,8,4], # 出1、2、3
]

start_weight = [3,2,1]
special_weight_list= [
    [80, 18, 2], # 用于刚好差3 到的情况
    [85, 3, 3],  # 用于 2、3 没区别的情况
    [3, 3, 2], # 完全均等概率，用于就差1,

]

if __name__ == '__main__':
    final_list=[[1,0,99]+start_weight]
    for i in range(13):
        now_list1 = [i+2,0, level_config[i][0]] + weight_list[0]
        final_list.append(now_list1)
        print(i+2,level_config[i][1])
        if level_config[i][1]<14:
            now_list2 = [i+2,level_config[i][0]+1,level_config[i][1]-1] + weight_list[1]
            now_list3 = [i+2,level_config[i][1],99] + weight_list[2]
            final_list.append(now_list2)
            final_list.append(now_list3)
        else:
            if level_config[i][0]<=10:
                if level_config[i][0]<=9:
                    final_list.append([i + 2, level_config[i][0] + 1, 10] + weight_list[3])
                final_list.append([i+2, 11, 11]+special_weight_list[0])
                final_list.append([i + 2, 12, 12] + special_weight_list[1])
                final_list.append([i + 2, 13, 99] + special_weight_list[2])
            elif level_config[i][0]==11:
                final_list.append([i + 2, 12, 12] + special_weight_list[1])
                final_list.append([i + 2, 13, 99] + special_weight_list[2])
            elif level_config[i][0]==12:
                final_list.append([i + 2, 13, 99] + special_weight_list[2])

    for i in final_list:
        for j in i:
            print(j,end="\t")
        print()