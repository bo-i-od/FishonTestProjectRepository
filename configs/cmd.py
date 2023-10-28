from tools.rpcMethod import *
from common.basePage import BasePage


# 开启自动钓鱼
def open_auto_fish(bp: BasePage):
    cmd(bp,  "autofish")
