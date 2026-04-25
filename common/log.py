#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一日志模块

全项目唯一的日志入口，替代原来的三套并行系统：
  - 旧 LoggerWriter (sys.stdout 劫持)
  - DeviceLoggerWriter 内置日志
  - 裸 print()

用法:
    from common.log import get_logger
    logger = get_logger("my_module")
    logger.info("hello")

或者在脚本入口调用 setup_logging() 同时输出到控制台和文件。
"""
import logging
import os
import sys
from typing import Optional


LOG_FORMAT = "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

_initialized = False


def get_logger(name: str = "auto_test") -> logging.Logger:
    """
    获取一个 logger 实例。

    始终可以安全调用，即使没调过 setup_logging()，也会输出到控制台。

    :param name: logger 名称，建议用模块名
    :return: logging.Logger
    """
    global _initialized
    if not _initialized:
        _setup_console_handler()
        _initialized = True
    return logging.getLogger(name)


def setup_logging(
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    console: bool = True,
) -> logging.Logger:
    """
    初始化全局日志系统。

    :param log_file: 日志文件路径，None 则不写文件
    :param level: 日志级别
    :param console: 是否输出到控制台
    :return: root logger
    """
    global _initialized

    root = logging.getLogger()
    root.setLevel(level)

    root.handlers.clear()

    formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

    if console:
        console_handler = logging.StreamHandler(sys.__stdout__)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        root.addHandler(console_handler)

    if log_file:
        os.makedirs(os.path.dirname(log_file) or ".", exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8", errors="replace")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)

    _quiet_noisy_loggers()

    _initialized = True
    return root


# 需要静默的第三方库 logger 名称
_NOISY_LOGGERS = [
    "websockets"
]


def _quiet_noisy_loggers():
    """将第三方库的 logger 级别提高到 WARNING，减少噪音"""
    for name in _NOISY_LOGGERS:
        logging.getLogger(name).setLevel(logging.WARNING)


def setup_device_logging(log_file: str, device_name: str = "", level: int = logging.INFO) -> logging.Logger:
    """
    为单个设备/脚本进程初始化日志。

    同时输出到控制台和设备日志文件。
    供脚本（guide_test.py / zhanlipin.py 等）在被 subprocess 调用时使用。

    :param log_file: 设备日志文件路径
    :param device_name: 设备名称（可选，用于 logger 名称）
    :param level: 日志级别
    :return: logger 实例
    """
    logger_name = f"device.{device_name}" if device_name else "device"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)

    console_handler = logging.StreamHandler(sys.__stdout__)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        os.makedirs(os.path.dirname(log_file) or ".", exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8", errors="replace")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def _setup_console_handler():
    """内部：懒初始化控制台 handler"""
    root = logging.getLogger()
    if not root.handlers:
        root.setLevel(logging.INFO)
        formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
        handler = logging.StreamHandler(sys.__stdout__)
        handler.setFormatter(formatter)
        root.addHandler(handler)
        _quiet_noisy_loggers()


logger = get_logger("log")


# ============================================================
# LoggerWriter 类 - 用于报告生成
# ============================================================


class LoggerWriter:
    def __init__(self, filename):
        self.file = open(filename, "a", encoding="utf-8", errors="replace")
        self.log_file_path = filename
        self.report_generated = False
    
    def write(self, message):
        self.file.write(message)
        self.file.flush()
        
        if "测试结束" in message and not self.report_generated:
            self._generate_test_report()
    
    def flush(self):
        self.file.flush()
    
    def close(self):
        self.file.close()
        
        if not self.report_generated:
            self._generate_test_report()
    
    def _generate_test_report(self):
        """生成测试报告"""
        try:
            from reports.guide_report_generator import GuideTestReportGenerator

            reports_dir = os.path.join(os.path.dirname(os.path.dirname(self.log_file_path)), "reports")
            os.makedirs(reports_dir, exist_ok=True)
            
            generator = GuideTestReportGenerator(self.log_file_path, reports_dir)
            report_path = generator.generate_report()
            
            summary = generator.get_report_summary()
            
            if summary['success']:
                stats = summary['summary']
                report_message = f"""
                
==================== 测试报告生成完成 ====================
[报告] HTML报告已生成: {report_path}
[提示] 请在浏览器中打开查看详细报告

========================================================
"""
            else:
                report_message = f"""
                
==================== 报告生成失败 ====================
[X] 生成报告时出现错误: {summary['error']}
[日志] 日志文件位置: {self.log_file_path}

====================================================
"""
            
            logger.info(report_message)
            
            self.report_generated = True
            
        except Exception as e:
            error_message = f"""
            
==================== 报告生成异常 ====================
[X] 生成报告时出现异常: {str(e)}
[日志] 日志文件位置: {self.log_file_path}

====================================================
"""
            logger.warning(error_message)
            self.report_generated = True

