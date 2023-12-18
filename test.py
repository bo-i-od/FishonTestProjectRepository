import cv2
# 得到单个点的像素rgb的和
def get_rgb_total(rgb_list):
    return rgb_list[0] + rgb_list[1] + rgb_list[2]

# 得到单列像素rgb的和
# 当前图像就是得到指定列2400个像素点rgb的和的和
def get_row_rgb_total(row_index):
    cur = 0
    row_gray_total = 0
    while cur < h:
        row_gray_total += get_rgb_total(img[cur][row_index])
        cur += 1
    return row_gray_total

# 得到黑边的起始列
def get_edge():
    cur = 0
    gate_value = 100
    while cur < w:
        # 黑色区域的单列像素rgb的和通常情况下为0，当检测到某列单列像素rgb的和大于0，就判定该列是黑边的起始列
        if get_row_rgb_total(cur) > gate_value:
            break
        cur += 1
    return cur

# 将原始的坐标转变为适配不填充刘海全面屏的坐标
def coordinate_translate(coordinate_orgin):
    scale_factor = 1 - bias
    coordinate_translated_x = bias + coordinate_orgin[0] * scale_factor
    coordinate_translated = [coordinate_translated_x, coordinate_orgin[1]]
    return coordinate_translated


if __name__ == '__main__':
    # 读取截屏
    img = cv2.imread("C:/Users/TU/Desktop/ss.png")
    h = len(img)
    w = len(img[0])
    edge = get_edge()
    bias = edge / w
    # 得到转换后的坐标
    res = coordinate_translate([0.3, 0.5])
    print(res)













