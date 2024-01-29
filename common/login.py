from panelObjs.entryUpdateLoadind import EntryUpdateLoading
from panelObjs.loginPanel import LoginPanel
from panelObjs.homePanel import HomePanel
from common.basePage import BasePage
from panelObjs.playerEditNamePanel import PlayerEditNamePanel
import time
import subprocess



def login(bp: BasePage, username):
    if not LoginPanel.is_panel_active(bp):
        EntryUpdateLoading.wait_for_EntryUpdateLoading(bp)
    # 在登录界面出现前，点击tap to start
    while not LoginPanel.is_panel_active(bp):
        EntryUpdateLoading.click_tap_to_start(bp)
    LoginPanel.set_login_name(bp,username)
    # 选服务器
    LoginPanel.set_server(bp, 1)
    LoginPanel.click_btn_login(bp)


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
    bp.sleep(4)

def adb_command(cmd:str):
    cmd_list = cmd.split(' ')
    try:
        # 执行ADB命令并获取输出结果
        result = subprocess.check_output(cmd_list)
        # 将字节类型转换为字符串类型
        output = result.decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        print("ADB命令执行失败！错误信息：", str(e))

def get_device_id():
    res = adb_command('adb devices')
    res = res.split('\n')[1]
    res = res.split('\tdevice')[0]
    return res

def open_package(package_name):
    cmd = f'adb shell am start -n {package_name}'
    adb_command(cmd)


if __name__ == '__main__':
    # print(get_device_id())
    package_name = "com.fishgame.fishon/com.happysky.aggregate.AggregateSDKActivity"
    open_package(package_name)
    # "List of devices attached\r\n127.0.0.1:21593\tdevice\r\n\r\n"
    # bp = BasePage()
    # cmd_l = ["guideskip", "add 1 100200 100000"]
    # login_to_hall(bp, cmd_l)
    # bp.go_to_panel("BattlePassPanel")



