import os
from threading import Thread
from panelObjs.entryUpdateLoadind import EntryUpdateLoading
from panelObjs.loginPanel import LoginPanel
from panelObjs.homePanel import HomePanel
from panelObjs.loadingPanel import LoadingPanel
from common.basePage import BasePage
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
import subprocess
# from uiautomator import Device
import uiautomator2 as u2
import requests
from requests.auth import HTTPBasicAuth
from time import sleep
import time



def login(bp: BasePage, username):
    # if not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.wait_for_EntryUpdateLoading(bp)
    # # 在登录界面出现前，点击tap to start
    # while not LoginPanel.is_panel_active(bp):
    #     EntryUpdateLoading.click_tap_to_start(bp)
    LoginPanel.set_login_name(bp, username)
    # 选服务器
    LoginPanel.set_server(bp, 1)
    LoginPanel.click_btn_login(bp)
    LoadingPanel.wait_until_panel_disappear(bp)


def account_init(bp: BasePage, player_name, cmd_list):
    while not PlayerEditNamePanel.is_panel_active(bp):
        bp.sleep(0.1)
    PlayerEditNamePanel.set_player_name(bp, player_name)
    bp.cmd_list(cmd_list)
    bp.sleep(1)
    PlayerEditNamePanel.click_confirm(bp)


def login_to_hall(bp: BasePage, cmd_list):
    if HomePanel.is_panel_active(bp):
        bp.cmd_list(cmd_list)
        return
    username = str(time.time()).split('.')[0]
    login(bp, username)
    account_init(bp, username, cmd_list)
    bp.sleep(1)


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
    try:
        # 执行ADB命令并获取输出结果
        result = subprocess.check_output(cmd_list)
        # 将字节类型转换为字符串类型
        output = result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("ADB命令执行失败！错误信息：", str(e))
        output = ''  # 返回一个空串而不是None
    return output

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

def u2_connect(serial_number):
    adb_command(f'adb connect {serial_number}')
    sleep(1)
    u2_device = u2.connect(serial_number)
    return u2_device

def u2_app_install(u2_device:u2.Device, url, package_name):
    # 卸载原先的包
    # adb_command(f"adb shell pm uninstall com.github.uiautomator")
    # adb_command(f"adb shell pm uninstall com.github.uiautomator.test")
    u2_device.app_uninstall(package_name)
    u2_device.app_install(url)

def u2_app_start(u2_device:u2.Device,package_name):
    u2_device.app_start(package_name=package_name)

def authorize(u2_device, timeout):
    cur = 0
    while True:
        if cur > timeout:
            return
        if not u2_device(className="android.widget.Button").exists():
            sleep(1)
            cur += 1
            continue
        button_list = u2_device(className="android.widget.Button")
        for button in button_list:
            if not find_allow_button_by_text(button.info):
                continue
            button.click()
            cur = 0
            break

def find_allow_button_by_text(button_info):
    key_word_list = ["允许", "确定", "同意", "开启", "知道", "继续", "安装", "确认", "完成", "打开", "启动"]
    for key_word in key_word_list:
        if key_word in button_info['text']:
            return True
    return False

def install_monitor(u2_device):
    while run_install_monitor_thread:
        if not u2_device(className="android.widget.Button").exists():
            sleep(1)
            continue
        button_list = u2_device(className="android.widget.Button")
        for button in button_list:
            if not find_allow_button_by_text(button.info):
                continue
            button.click()
            break



def main():
    # Jenkins的用户名和密码
    username = 'chenjunfei'
    password = '19980327chEN.'

    # 取包地址
    apk_url = "http://172.16.8.194:8080/job/fishing_game_android_aggregate/532/artifact/fishing_v1.0.0.43664__EnvDebugDev__android-inhouse.apk"

    # # 设备号
    # # serial_number = "b6h65hd64p5pxcyh"
    serial_number ="127.0.0.1:21593"

    # 包名
    package_name = "com.fishgame.fishon"

    # 连接
    d = u2_connect(serial_number)


    # 下载包
    print("等待安装包下载...")
    apk_name = download_apk(apk_url, username, password)


    # 安装包
    print("等待安装完成...")
    install_monitor_thread = Thread(target=install_monitor, args=[d])
    install_monitor_thread.start()
    u2_app_install(d, apk_name, package_name)
    global run_install_monitor_thread
    run_install_monitor_thread = False

    # authorize(d, timeout=15)

    # 启动包
    print("等待App启动...")
    u2_app_start(d, package_name=package_name)

    # 进行授权
    print("等待授权")
    authorize(d, timeout=5)


if __name__ == '__main__':
    run_install_monitor_thread = True
    main()
