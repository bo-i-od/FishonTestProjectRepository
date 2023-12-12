from poco.drivers.unity3d.device import UnityEditorWindow
from poco.drivers.unity3d import UnityPoco
import random
from configs.elementsData import ElementsData
from airtest.core.api import connect_device


# 与C#建立rpc通信 调用PocoManager.cs的SetBtn方法
def set_btn_enabled(panel, enabled):
    Poco.agent.c.call("SetBtn", panel, enabled)

# 初始化poco
def poco_init():
    # dev = UnityEditorWindow()
    dev = connect_device("android://127.0.0.1:5037/127.0.0.1:21593")
    # make sure your poco-sdk in the game runtime listens on the following port.
    # 默认端口 5001
    # IP is not used for now
    addr = ('', 5001)
    return UnityPoco(addr, device=dev)

# 随机点击
def randomClick(times):
    # 屏幕长宽
    screen_w = 1920
    screen_h = 1080
    # 归一化系数
    w_n = 1 / screen_w
    h_n = 1 / screen_h
    # 计数
    cur = 0
    while cur < times:
        # 在屏幕范围内随机选择一点
        x = random.randint(0, screen_w - 1)
        y = random.randint(0, screen_h - 1)
        # 计算归一化后的坐标
        position_normal = [x * w_n, y * h_n]
        Poco.click(position_normal)
        # 10%的概率点击同一位置两次
        r = random.randint(0,10)
        if r == 0:
            Poco.click(position_normal)
        cur += 1
        print(cur)

if __name__ == '__main__':
    Poco = poco_init()
    # 将名为RoulettePanel的物体下的所有子物体的按钮组件禁用
    # set_btn_enabled("BattlePassPanel", False)
    # 随机点击1000次
    randomClick(1000)
    pass





