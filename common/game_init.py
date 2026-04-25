import time
import traceback

from airtest.core.api import shell

from common.base_page import BasePage


def get_bp(dev, is_monitor=False):
    bp = restart_to_login(dev, is_monitor=is_monitor, package_list=["com.xuejing.smallfish.official", "com.arkgame.fishingmaster"])
    if not LoginPanel.is_panel_active(bp):
        return bp
    LoginPanel.click_btn_login(bp)
    bp.sleep(2)
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)
    bp.sleep(5)
    return bp


def reset_bp(dev, is_monitor=False):
    try:
        bp = get_bp(dev, is_monitor=is_monitor)
    except:
        traceback.print_exc()
        bp = reset_bp(dev, is_monitor=is_monitor)
    return bp

def login(bp: BasePage, username, index=0):
    # if not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.wait_for_EntryUpdateLoading(bp)
    # # 在登录界面出现前，点击tap to start
    # while not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.click_tap_to_start(bp)
    # 选服务器 输入名称 点击登录
    LoginPanel.set_server(bp, index)
    LoginPanel.set_login_name(bp, username)
    LoginPanel.click_btn_login(bp)
    bp.sleep(2)

    # 直到读条消失
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)

def login_to_hall(bp: BasePage, cmd_list=None, is_skip_guide=True):
    LoginPanel.wait_for_btn_login(bp)
    t = str(time.time()).split('.')
    username = "t" +t[0][-2:]+ t[1]
    login(bp, username)

    # account_init(bp, username, cmd_list, is_skip_guide=is_skip_guide)

def app_start_to_login(dev=None, is_monitor=False):
    cur = 0
    bp = None
    while cur < 300:
        # try:
        #     authorize(poco)
        # except:
        #     pass
        bp = get_basePage(dev=dev, is_monitor=is_monitor)
        if bp is not None:
            break
        time.sleep(1)
        cur += 1
    time.sleep(10)
    # EntryUpdateLoading.click_tap_to_start(bp)
    LoginPanel.wait_for_btn_login(bp)
    return bp

def get_basePage(serial_number=None, dev=None, is_monitor=False):
    try:
        bp = BasePage(serial_number=serial_number, dev=dev, is_monitor=is_monitor)
        return bp
    except:
        return None


def get_device_id():
    res = adb_command('adb devices')
    res = res.split('\n')[1]
    res = res.split('\tdevice')[0]
    return res


def open_package(package_name):
    cmd = f'adb shell am start -n {package_name}'
    adb_command(cmd)

def adb_command(cmd: str):
    cmd_list = cmd.split(' ')
    return shell(cmd=cmd_list)

def restart_to_login(dev, is_monitor=False, package=None, package_list=None):
    if package_list is None:
        return restart_to_login(dev, is_monitor=is_monitor, package_list=[package])
    for p in package_list:
        try:
            dev.stop_app(package=p)
            time.sleep(1)
            dev.start_app(package=p)
        except:
            continue
    # poco_uiautomation = AndroidUiautomationPoco(device=G.DEVICE)
    bp = app_start_to_login(dev=dev, is_monitor=is_monitor)
    return bp