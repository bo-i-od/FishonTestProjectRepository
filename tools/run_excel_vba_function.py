# -*- coding: utf-8 -*-
import logging
import os
import sys
import time
import shutil

##################################################################
# 创建一个 logger 对象
logger = logging.getLogger('opt_logger')
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
##################################################################

def clear_win32com_cache():
    """清理 win32com 缓存"""
    try:
        import win32com
        # 找到缓存目录
        cache_dir = os.path.join(os.path.dirname(win32com.__file__), 'gen_py')
        if os.path.exists(cache_dir):
            logger.info(f"清理 win32com 缓存目录: {cache_dir}")
            shutil.rmtree(cache_dir)
            logger.info("缓存清理完成")
        return True
    except Exception as e:
        logger.error(f"清理缓存失败: {e}")
        return False

# 在导入 win32com.client 之前清理缓存
clear_win32com_cache()
import win32com.client as win32


def dealVBAExcelFile(file_path):
    excel = None
    wb = None
    try:
        # 使用 Late Binding，避免缓存问题
        excel = win32.Dispatch('Excel.Application')
        excel.Visible = False
        excel.DisplayAlerts = False

        wb = excel.Workbooks.Open(file_path)

        try:
            result = excel.Run('ReadDeclData')
        except Exception as e:
            print(f"运行vba【读取】错误: {e}")

        try:
            result = excel.Run('SortExcelData', False)
        except Exception as e:
            print(f"运行vba【一键生成】错误: {e}")

        wb.Save()

    finally:
        if wb:
            wb.Close()
        if excel:
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
        (fname, fextension) = os.path.splitext(file)
        txt_file_ab_path = os.path.dirname(path) + "/../ElementData/BaseData/" + fname + ".data.txt"
        if not os.path.exists(txt_file_ab_path):
            logger.info(f"文件 {fname}.data.txt 不存在, 跳过处理 {file}")
            return
        logger.info(f'work start {file}')
        start_time_file = time.time()
        dealVBAExcelFile(file_ab_path)
        printTimeCost(start_time_file,f"work done on file {file}")
    except Exception as e:
        print(f"替换 VBA 宏时发生错误: {e},3秒后重试")
        time.sleep(3)
        runVBAExcel(path)

if __name__ == "__main__":
    argv_len = len(sys.argv)
    start_time = time.time()

    # 直接运行目标excel
    excel_path = r"D:\\work\\fishing\\svn\\Dev_2024_3_30\\datapool\\策划模板导出工具\\OUT_DRAW_MAIN.xlsm"
    # 在目标目录下运行
    excel_path = r"D:\\work\\fishing\\svn\\Dev_2024_3_30\\datapool\\策划模板导出工具"
    # 在当前目录运行
    excel_path = ""

    if len(excel_path) == 0:
        file_path = os.path.abspath(__file__)
        exe_folder = os.path.dirname(file_path)
        excel_path = os.path.abspath(exe_folder + "/../策划模板导出工具")

    if excel_path.endswith(".xlsm"):
        runVBAExcel(excel_path)
    else:
        logger.info(f'work on one dir {excel_path}')

        # target_list = ["ADV_ROD_QUALITY.xlsm","BATTLE_BUFF.xlsm","BATTLE_SKILL.xlsm","NEW_PLOT_FISH_TYPE_DROP.xlsm","NEW_PLOT_MAIN.xlsm","NEW_PLOT_MAP_POINT.xlsm","PANEL_STATIC_LANGUAGE.xlsm"]

        # 忽略列表
        ignore_list = ["MISSION_MAIN.xlsm"
                       ,"DUEL_AI_TIMELINE.xlsm"
                       ,"MISSION_CONDITION.xlsm"
                       ,"FISH_WEIGHT.xlsm"
                       ,"DROP_ENTITY.xlsm"
                       ,"EFFECT_GROUP.xlsm"
                       ,"FISH.xlsm"
                       ,"SKILL.xlsm"
                       ,"TALENT_LEVEL.xlsm"
                       ]

        ignore_list = []

        for root, _, files in os.walk(excel_path):
            for file in files:
                file_ab_path = os.path.join(root, file)
                if file.endswith("xlsm") and not file.startswith("~"):
                    # 可以指定黑名单
                    if file in ignore_list:
                        logger.info(f"ignore {file}")
                        continue
                    # 可指定从某一个开始
                    # if file < "XDAYS_RANK_REWARD.xlsm":
                    #     pass
                    # else:
                    # 也可指定只运行某一个
                    # if file != "OUT_DRAW_MAIN.xlsm":
                    #     pass
                    # else:
                    # 也可指定只运行列表里的内容
                    # if file not in target_list:
                    #     pass
                    # else:
                    # ADV_GEAR_QUALITY.xlsm
                    runVBAExcel(file_ab_path)

