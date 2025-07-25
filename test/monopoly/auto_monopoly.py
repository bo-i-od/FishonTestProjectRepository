# -*- encoding=utf8 -*-
import datetime
import logging
import os
from time import sleep
from airtest.core.api import device, connect_device
from test.monopoly.my_cv import Template, comprehensive_image_comparison


# auto_setup(__file__)


# class MyApp(App):
#     def build(self):
#
#         device_init()
#         main()


# 循环查找
def my_loop_find(query):
    cur = 0
    while cur < 2:
        query.threshold = 0.8
        match_pos = find(query)
        if match_pos is not None:
            return match_pos
        cur += 1
    return None
    # screen = device().snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)
    # if screen is None:
    #     return False
    # if pos_pre != None:
    #     screen = fill_black(screen, pos_pre)
    # query.threshold = 0.85
    # match_pos = query.match_in(screen)
    # if match_pos is None:
    #     return False
    # return match_pos


def my_exists(v):
    pos = my_loop_find(v)
    return pos

# 等到这幅图片找到了就点击 否则停滞
def wait_for_touch(img):
    res = try_exists(img)
    while res is None:
        res = try_exists(img)
        sleep(0.2)
    device().touch(res)


def try_exists(v):
    pos = find(v)
    return pos


# 查找图像并点击图像
def my_touch(v, threshold=0.8):
    pos = find(v, threshold=threshold)
    if pos is None:
        return None
    device().touch(pos)
    sleep(0.05)
    return pos


def find(query, threshold=0.8):
    screen = device().snapshot(filename=None)
    if screen is None:
        return None
    query.threshold = threshold
    match_pos = query.match_in(screen)
    return match_pos


def may_touch(img):
    cur = 0
    while cur < 5:
        pos = try_exists(img)
        if pos:
            device().touch(pos)
            return True
        sleep(1)
        cur += 1
    return False


def touch_a_until_b(img_a, img_b):
    while find(img_b) is None:
        # print("没找到")
        try:
            my_touch(img_a)
        except:
            pass
        sleep(0.5)

def wait_for_appear(img):
    cur=0
    while True:
        pos = find(img)
        if pos:
            return pos
        sleep(0.5)
        cur += 1
        if cur > 30:
            print("定位超时")
            break
    return None

def touch_until_disappear(img):
    pos = wait_for_appear(img)
    while True:
        if not pos:
            break
        device().touch(pos)
        sleep(0.5)
        pos = find(img)
        continue





def device_init():
    pass
    # connect_device("android://127.0.0.1:5037/127.0.0.1:"+port)
    #     if not cli_setup():
    #         auto_setup(__file__, logdir=True, devices=["android:///cap_method=ADBCAP&touch_method=MAXTOUCH&",])
    # start_app("com.bilibili.umamusu")
    # print("优俊少女启动！！")
    # script content
    # generate html report
    # from airtest.report.report import simple_report
    # simple_report(__file__, logpath=True)



# # ---------------------------------------------------------------------#
# #   将base64的截屏数据转opencv格式图像
# # ---------------------------------------------------------------------#
# def get_cv_img(img):
#     img_b64encode = base64.b64encode(img)
#     img_b64decode = base64.b64decode(img_b64encode)  # base64解码
#     img_array = np.frombuffer(img_b64decode, np.uint8)  # 转换np序列
#     full_img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)  # 转换Opencv格式
#     return full_img
def init_templates():
    res = {}

    res["go_enable"] = Template(r"source_img/go_enable_0002_0726.png", record_pos=(0.002, 0.726), resolution=(1080, 2400), threshold=0.8, strict_brightness=True)
    res["go_disable"] = Template(r"source_img/go_disable_m0001_0747.png", record_pos=(-0.001, 0.747), resolution=(1080, 2400), threshold=0.8, strict_brightness=True)
    res["go_hide"] = Template(r"source_img/go_hide.png", record_pos=None, resolution=(1080, 2400), threshold=0.8, strict_brightness=True)
    res["go_special"]= Template(r"source_img/go_special_m0002_0792.png", record_pos=(-0.002, 0.792), resolution=(1080, 2400), threshold=0.8)
    res["target"] = Template(r"source_img/target.png", record_pos=None, resolution=(1080, 2400), threshold=0.1)
    res["target_2"] = Template(r"source_img/target_2.png", record_pos=None, resolution=(1080, 2400), threshold=0.1)
    res["collect_2"] = Template(r"source_img/collect_2_00_096.png", record_pos=(0.002, 0.933), resolution=(1080, 2400), threshold=0.8)
    res["close_1"] = Template(r"source_img/close_1_0408_m0642.png", record_pos=(0.408, -0.642), resolution=(1080, 2400), threshold=0.8)
    res["close_2"] = Template(r"source_img/close_2_0447_m0834.png", record_pos=(0.447, -0.834), resolution=(1080, 2400), threshold=0.8)
    res["close_3"] = Template(r"source_img/close_3_m0001_1018.png", record_pos=(-0.001, 1.018), resolution=(1080, 2400), threshold=0.8)
    res["close_4"] = Template(r"source_img/close_4_00_1013.png", record_pos=(0.0, 1.013), resolution=(1080, 2400), threshold=0.8)
    res["confirm"] = Template(r"source_img/confirm_m0001_0506.png", record_pos=(-0.001, 0.506), resolution=(1080, 2400), threshold=0.8)
    res["collect_1"] = Template(r"source_img/collect_1_0002_0933.png", record_pos=(0.002, 0.933), resolution=(1080, 2400), threshold=0.8)
    res["door"] = Template(r"source_img/door.png", record_pos=None, resolution=(1080, 2400), threshold=0.8)
    res["change"] = Template(r"source_img/change_m0001_0999.png", record_pos=(-0.001, 0.999), resolution=(1080, 2400), threshold=0.8)
    return res

def if_gone(blackboard):
    res = comprehensive_image_comparison(img1=blackboard["snapshot_pre"], img2=device().snapshot(filename=None))
    if "histogram" in res and res["histogram"] < 0.9:
        blackboard["go_success"] = True
        return
    if "template_matching" in res and res["template_matching"] < 0.9:
        blackboard["go_success"] = True
        return


def go(blackboard):

    if blackboard["go_success"]:
        blackboard["go_count"] += 1
        blackboard["snapshot_pre"] = device().snapshot(filename=blackboard["path"] + f"/{blackboard['go_count']}.png")
        print("移动次数：",blackboard["go_count"])
    else:
        if_gone(blackboard=blackboard)
        if blackboard["go_success"]:
            blackboard["go_count"] += 1
            blackboard["snapshot_pre"] = device().snapshot(filename=f"./result/{blackboard['go_count']}.png")
            print("移动次数：", blackboard["go_count"])


    blackboard["go_success"] = False
    sleep(1)
    device().touch(blackboard["pos"])
    go_disable = blackboard["templates"]["go_disable"]
    cur = 0
    while True:
        if cur > 5:
            break
        sleep(0.1)
        screen = device().snapshot(filename=None)
        match_pos_go_disable = go_disable.match_in(screen)
        if not match_pos_go_disable:
            cur += 1
            continue
        blackboard["go_success"] = True
        break

def destroy(blackboard):
    target = blackboard["templates"]["target"]
    collect_2 = blackboard["templates"]["collect_2"]
    resolution = device().get_current_resolution()
    my_touch(v=target)
    x = int(resolution[0] * 0.3)
    y = int(resolution[1] * 0.3)
    # print((x, y))
    while find(collect_2) is None:
        device().touch((x, y))
        sleep(0.5)
        x += resolution[0] * 0.1
        if x > resolution[0]:
            y += resolution[1] * 0.075
            x = int(resolution[0] * 0.3)
        if y > resolution[1] * 0.9:
            break


    touch_until_disappear(img=collect_2)

def bank(blackboard):
    door = blackboard["templates"]["door"]
    collect_2 = blackboard["templates"]["collect_2"]
    touch_a_until_b(img_a=door, img_b=collect_2)
    touch_until_disappear(img=collect_2)

def prison(blackboard):
    go_special = blackboard["templates"]["go_special"]
    touch_until_disappear(img=go_special)


def create_screenshot_folder(rate):
    """为截图创建时间命名的文件夹"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    folder_name = f"./result/ratex{rate}_{timestamp}"

    os.makedirs(folder_name, exist_ok=True)
    print(f"截图文件夹已创建: {folder_name}")
    return folder_name

def go_or_other_action(blackboard, target_count, rate):
    go_enable = blackboard["templates"]["go_enable"]
    go_disable = blackboard["templates"]["go_disable"]
    change = blackboard["templates"]["change"]
    door = blackboard["templates"]["door"]
    go_special = blackboard["templates"]["go_special"]
    go_hide = blackboard["templates"]["go_hide"]
    close_1 = blackboard["templates"]["close_1"]
    close_2 = blackboard["templates"]["close_2"]
    close_3 = blackboard["templates"]["close_3"]
    close_4 = blackboard["templates"]["close_4"]
    confirm = blackboard["templates"]["confirm"]
    blackboard["go_success"] = True
    blackboard["go_count"] = 0
    blackboard["snapshot_pre"] = device().snapshot(filename=blackboard["path"] + f"/{blackboard['go_count']}.png")
    blackboard["path"] = create_screenshot_folder(rate)
    while True:
        if blackboard["go_count"] >= target_count:
            return
        sleep(0.1)
        screen = device().snapshot(filename=None)
        match_pos_go_enable = go_enable.match_in(screen)
        match_pos_go_disable = go_disable.match_in(screen)
        if match_pos_go_enable:
            blackboard["pos"] = match_pos_go_enable
            go(blackboard)
            continue
        if match_pos_go_disable:
            sleep(1)
            blackboard["go_success"] = True
            continue

        match_pos_change = change.match_in(screen)

        if match_pos_change:
            print("破坏")
            destroy(blackboard)
            blackboard["go_success"] = True
            continue

        match_pos_door = door.match_in(screen)
        if match_pos_door:
            print("打劫")
            bank(blackboard)
            blackboard["go_success"] = True
            continue

        match_pos_go_special = go_special.match_in(screen)
        if match_pos_go_special:
            print("进监狱")
            prison(blackboard)
            blackboard["go_success"] = True
            continue

        match_pos_go_hide = go_hide.match_in(screen)
        if match_pos_go_hide:
            touch_until_disappear(img=go_hide)
            continue

        match_pos_close_1 = close_1.match_in(screen)
        if match_pos_close_1:
            touch_until_disappear(img=close_1)
            continue

        match_pos_close_2 = close_2.match_in(screen)
        if match_pos_close_2:
            touch_until_disappear(img=close_2)
            continue

        match_pos_close_3 = close_3.match_in(screen)
        if match_pos_close_3:
            touch_until_disappear(img=close_3)
            continue

        match_pos_close_4 = close_4.match_in(screen)
        if match_pos_close_4:
            touch_until_disappear(img=close_4)
            continue

        match_pos_confirm = confirm.match_in(screen)
        if match_pos_confirm:
            touch_until_disappear(img=confirm)
            continue


        # match_pos_go_special, confidence_go_special = go_special.match_in(screen)
        # if match_pos_go_special:
        #     prison(blackboard)
        #     blackboard["go_success"] = True
        #     continue




def main():
    logging.getLogger("airtest").setLevel(logging.ERROR)
    target_count = 100
    rate = 1
    connect_device("android://127.0.0.1:5037/a58a6a67")
    templates = init_templates()
    blackboard = {}
    blackboard["templates"] = templates
    go_or_other_action(blackboard=blackboard, target_count=target_count, rate=rate)


if __name__ == "__main__":
    main()













