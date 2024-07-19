import os
from threading import Thread
from airtest.core.api import connect_device,  install, Template, start_app, shell, click, sleep, stop_app
from airtest.core.helper import G
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from panelObjs.loginPanel import LoginPanel
from panelObjs.homePanel import HomePanel
from panelObjs.loadingPanel import LoadingPanel
from common.basePage import BasePage
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
import requests
from requests.auth import HTTPBasicAuth
from time import sleep
import time
from tools import commonTools


def login(bp: BasePage, username):
    # if not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.wait_for_EntryUpdateLoading(bp)
    # # 在登录界面出现前，点击tap to start
    # while not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.click_tap_to_start(bp)
    # 选服务器 输入名称 点击登录
    LoginPanel.set_server(bp, 9)
    LoginPanel.set_login_name(bp, username)
    LoginPanel.click_btn_login(bp)
    bp.sleep(2)

    # 直到读条消失
    LoadingPanel.wait_until_panel_disappear(bp, is_wait_for_appear=False)


# 设置摇杆
def set_joystick(bp:BasePage, state="FLOATING"):
    if state == "FLOATING":
        bp.lua_console( "SettingMgr:Write(_G.FISH_SETTING_JOYSTICK.JOYSTICK_NAME, _G.FISH_SETTING_JOYSTICK.TYPE_FLOATING)")
        return
    if state == "FIXED":
        bp.lua_console( "SettingMgr:Write(_G.FISH_SETTING_JOYSTICK.JOYSTICK_NAME, _G.FISH_SETTING_JOYSTICK.TYPE_FIXED)")
        return


# 初始化账号
def account_init(bp: BasePage, player_name, cmd_list):
    while not PlayerEditNamePanel.is_panel_active(bp):
        bp.sleep(0.1)
    bp.cmd_list(cmd_list)
    set_joystick(bp)
    while True:
        PlayerEditNamePanel.set_player_name(bp, player_name)
        PlayerEditNamePanel.click_confirm(bp)
        bp.sleep(1)
        if not PlayerEditNamePanel.is_panel_active(bp):
            break
        player_name = "t" + str(time.time()).split('.')[0]


# 登录到大厅
def login_to_hall(bp: BasePage, cmd_list=None):
    LoginPanel.wait_for_btn_login(bp)
    username = "t" + str(time.time()).split('.')[0]
    login(bp, username)

    account_init(bp, username, cmd_list)


def app_start_to_login(dev=None):
    cur = 0
    bp = None
    while cur < 300:
        # try:
        #     authorize(poco)
        # except:
        #     pass
        bp = get_basePage(dev=dev)
        if bp is not None:
            break
        time.sleep(1)
    # EntryUpdateLoading.click_tap_to_start(bp)
    LoginPanel.wait_for_btn_login(bp)
    return bp


def tap_to_start():
    img = G.DEVICE.snapshot(filename=None, quality=10)
    query = Template(r"confirm.png", record_pos=(0.109, 0.114), resolution=(2400, 1080))
    # print(img)
    match_pos = commonTools.get_img_position(query, img)
    return match_pos


def get_basePage(serial_number=None, dev=None):
    try:
        bp = BasePage(serial_number=serial_number, dev=dev)
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
    # try:
    #     # 执行ADB命令并获取输出结果
    #     result = subprocess.check_output(cmd_list)
    #     # 将字节类型转换为字符串类型
    #     output = result.decode('utf-8')
    # except subprocess.CalledProcessError as e:
    #     print("ADB命令执行失败！错误信息：", str(e))
    #     output = ''  # 返回一个空串而不是None
    # return output


def check_apk_installed(package: str):
    output = adb_command(f'adb shell pm list packages')
    return package in output


def check_app_running(package: str):
    output = adb_command('adb shell dumpsys window | grep mCurrentFocus')
    return package in output


def download_apk(apk_url:str, username:str, password:str):
    # Jenkins中的apk链接
    url = apk_url

    apk_url_split = apk_url.split('/')
    apk_name = apk_url_split[len(apk_url_split) - 1]
    # 检查APK是否已经存在
    if os.path.exists(apk_name):
        print("apk已下载，跳过下载")
        return apk_name
    # 下载apk
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        with open(apk_name, 'wb') as f:
            f.write(response.content)
    else:
        print("APK下载失败，状态码：", response.status_code)
    return apk_name


def wait_for_authorize(poco, timeout):
    cur = 0
    while True:
        if cur > timeout:
            return
        if authorize(poco):
            return
        time.sleep(1)
        cur += 1


def authorize(poco):
    if not poco(type="android.widget.TextView").exists():
        print("不存在按钮")
        return False
    button_list = poco(type="android.widget.TextView")
    for button in button_list:
        button_text =button.get_text()
        if not find_allow_button_by_text(button_text):
            continue
        button.click()
        print(f"点击{button_text}")
        return True
    return False


def find_allow_button_by_text(button_text):
    key_word_list = ["确定", "允许", "同意", "开启", "知道", "继续", "安装", "确认", "完成", "打开", "启动"]
    for key_word in key_word_list:
        if key_word in button_text:
            return True
    return False


def install_monitor(poco):
    while run_install_monitor_thread:
        if not poco(type="android.widget.TextView").exists():
            sleep(1)
            continue
        button_list = poco(type="android.widget.TextView")
        for button in button_list:
            button_text = button.get_text()
            if not find_allow_button_by_text(button_text):
                continue
            button.click()
            print(f"点击{button_text}")
            break


# 重启
def restart_to_login(dev, package):
    dev.stop_app(package=package)
    sleep(1)
    dev.start_app(package=package)
    # poco_uiautomation = AndroidUiautomationPoco(device=G.DEVICE)
    bp = app_start_to_login(dev=dev)
    return bp


def main():
    # Jenkins的用户名和密码
    username = 'chenjunfei'
    password = '19980327chEN.'

    # 取包地址
    apk_url = "http://172.16.8.194:8080/job/fishing_game_android_template/181/artifact/fishing_v1.0.0.47863__officialsmallfish__EnvDebugDev__android-cninhouse.apk"

    # # 设备号
    # # serial_number = "b6h65hd64p5pxcyh"
    serial_number = "192.168.111.81:20010"

    # 连接
    dev = connect_device(f"android://127.0.0.1:5037/{serial_number}")

    # 下载包
    print("等待安装包下载...")
    apk_name = download_apk(apk_url, username, password)

    poco_uiautomation = AndroidUiautomationPoco(device=dev)

    # # 安装包
    print("等待安装完成...")
    install_monitor_thread = Thread(target=install_monitor, args=[poco_uiautomation])
    install_monitor_thread.start()

    install(filepath=apk_name, replace=True)
    global run_install_monitor_thread
    run_install_monitor_thread = False

    # 包名
    package_name = "com.fishgame.fishon"
    # 启动包
    print("等待App启动...")
    start_app(package=package_name)

    while True:
        pos = tap_to_start()
        if pos is None:
            continue
        click(pos)
        break

    # # 进行授权
    # print("等待授权")
    # wait_for_authorize(poco_uiautomation, timeout=5)
    # time.sleep(5)

    bp = app_start_to_login()
    login_to_hall(bp)


def start_time_test():
    dev = connect_device(f"android://127.0.0.1:5037/FMR0223830025758")

    stop_app("com.xuejing.smallfish.official")
    sleep(1)
    start_app("com.xuejing.smallfish.official")
    start = time.time()  # 返回的是一个浮点数，代表当前时间
    end = start
    while True:
        pos = tap_to_start()
        if pos is None:
            continue
        end = time.time()  # 记录结束时间
        click(pos)
        break
    print('start time: ', end - start)  # 两个时间差就是花费的时间
    start = time.time()
    bp = get_basePage(dev=dev)
    # EntryUpdateLoading.click_tap_to_start(bp)
    LoginPanel.wait_for_btn_login(bp)
    end = time.time()  # 记录结束时间
    print('loading time: ', end - start)  # 两个时间差就是花费的时间


if __name__ == '__main__':
    pass

    # bp = BasePage("127.0.0.1:21503")
    # start_time_test()
    # LoginPanel.wait_for_btn_login(bp)

    # if not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.wait_for_EntryUpdateLoading(bp)
    # # 在登录界面出现前，点击tap to start
    # while not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.click_tap_to_start(bp)
