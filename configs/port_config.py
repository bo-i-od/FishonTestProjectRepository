"""
端口配置模块
支持命令行参数、环境变量、默认值三种方式设置端口
优先级：命令行参数 > 环境变量 > 默认值
"""
from common.log import get_logger
logger = get_logger("port_config")
import os
import argparse
import sys
from typing import Optional


class PortConfig:
    """端口配置管理类"""
    
    DEFAULT_PORT = 5101
    
    def __init__(self):
        self._port: Optional[int] = None
    
    def get_port(self) -> int:
        """获取当前配置的端口号"""
        if self._port is None:
            self._port = self._parse_port()
        return self._port
    
    def _parse_port(self) -> int:
        """解析端口配置，按优先级获取"""
        # 1. 尝试从命令行参数获取
        port = self._get_port_from_args()
        if port is not None:
            return port
        
        # 2. 尝试从环境变量获取
        port = self._get_port_from_env()
        if port is not None:
            return port
        
        # 3. 使用默认端口
        return self.DEFAULT_PORT
    
    def _get_port_from_args(self) -> Optional[int]:
        """从命令行参数获取端口"""
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('--port', '-p', type=int, help='指定端口号')
        parser.add_argument('--ws-port', type=int, help='指定WebSocket端口号')
        
        # 只解析已知参数，避免影响其他脚本的参数解析
        args, _ = parser.parse_known_args()
        
        # 优先使用 --ws-port，其次使用 --port
        if args.ws_port is not None:
            return args.ws_port
        return args.port
    
    def _get_port_from_env(self) -> Optional[int]:
        """从环境变量获取端口"""
        port_str = os.getenv('TEST_PORT')
        if port_str:
            try:
                return int(port_str)
            except ValueError:
                logger.warning(f"警告: 环境变量 TEST_PORT 的值 '{port_str}' 不是有效的端口号，使用默认端口 {self.DEFAULT_PORT}")
        return None
    
    def set_port(self, port: int) -> None:
        """手动设置端口号"""
        if not isinstance(port, int) or port < 1 or port > 65535:
            raise ValueError(f"端口号必须是1-65535之间的整数，当前值: {port}")
        self._port = port
    
    def get_port_info(self) -> str:
        """获取端口配置信息"""
        port = self.get_port()
        
        # 检查端口来源
        args_port = self._get_port_from_args()
        env_port = self._get_port_from_env()
        
        if args_port is not None:
            # 检查具体是哪个参数
            parser = argparse.ArgumentParser(add_help=False)
            parser.add_argument('--port', '-p', type=int, help='指定端口号')
            parser.add_argument('--ws-port', type=int, help='指定WebSocket端口号')
            args, _ = parser.parse_known_args()
            
            if args.ws_port is not None:
                source = "command line args (--ws-port)"
            else:
                source = "command line args (--port)"
        elif env_port is not None:
            source = "environment variable"
        else:
            source = "default value"
            
        return f"Using port: {port} (source: {source})"


# 全局端口配置实例
port_config = PortConfig()


def get_port() -> int:
    """获取当前配置的端口号"""
    return port_config.get_port()


def set_port(port: int) -> None:
    """设置端口号"""
    port_config.set_port(port)


def get_port_info() -> str:
    """获取端口配置信息"""
    return port_config.get_port_info()


if __name__ == "__main__":
    # 测试端口配置
    logger.info(get_port_info())
