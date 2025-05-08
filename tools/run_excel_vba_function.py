import logging
import os
import sys
import time

from configs.pathConfig import EXCEL_PATH

##################################################################
# 创建一个 logger 对象
logger = logging.getLogger('opt_logger')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
##################################################################

import win32com.client as win32

def dealVBAExcelFile(file_path):
    # 启动 Excel 应用
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False  # 隐藏 Excel 界面

    # 打开工作簿
    wb = excel.Workbooks.Open(file_path)

    # 调用 VBA 函数（通过 Application.Run）
    try:
        result = excel.Run('ReadDeclData')
    except Exception as e:
        print(f"运行vba【读取】错误: {e}")

    try:
        result = excel.Run('SortExcelData', False)
    except Exception as e:
        print(f"运行vba【一键生成】错误: {e}")

    # 保存并关闭
    wb.Save()
    wb.Close()
    excel.Quit()

def printTimeCost(start_time, str_prefix):
    end_time = time.time()
    total_seconds = end_time - start_time
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    logger.info(f"{str_prefix} {int(hours)}时 {int(minutes)}分 {seconds:.3f}秒")

def runVBAExcel(path):
    try:
        file_ab_path = path
        file = os.path.basename(path)
        logger.info(f'work start {file}')
        start_time_file = time.time()
        dealVBAExcelFile(file_ab_path)
        printTimeCost(start_time_file,f"work done on file {file}")
    except Exception as e:
        print(f"替换 VBA 宏时发生错误: {e},3秒后重试")
        time.sleep(3)
        runVBAExcel(path)

if __name__ == "__main__":
    excel_list = ["TIMER_MAIN.xlsm", "MISSION_GROUP.xlsm", "MISSION_MAIN.xlsm", "MISSION_CONDITION.xlsm", "MISSION_LANGUAGE.xlsm", "EVENT_N_DAY_TASKS_MILESTONE.xlsm"]
    cur = 0
    while cur < len(excel_list):
        runVBAExcel(EXCEL_PATH + excel_list[cur])
        time.sleep(1)
        cur += 1



