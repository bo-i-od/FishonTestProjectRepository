"""
通用脚本执行引擎 (ScriptRunner)
负责：加载 async def run(bp, **kwargs) 格式的 .py 脚本并执行。

适用于录制回放脚本及任何遵循 async def run(bp) 约定的脚本。
可被 GUI 直接调用，也可通过 python -m common.script_runner 作为子进程调用。
"""
from dataclasses import dataclass
from typing import Optional, Callable

from common.log import get_logger

logger = get_logger("script_runner")

import asyncio
import importlib.util
import sys
import time
from pathlib import Path


@dataclass
class ScriptResult:
    """脚本执行结果"""
    name: str = ""
    success: bool = False
    elapsed: float = 0.0
    error_message: Optional[str] = None


class ScriptRunner:
    """加载并执行包含 async def run(bp) 的 Python 脚本。"""

    _PROJECT_MARKERS = ('common', 'configs', 'scripts', 'panelObjs')

    def __init__(self, base_page, script_path: str):
        self.bp = base_page
        self.script_path = Path(script_path).resolve()
        self.name = self.script_path.stem
        self._module = None
        self._load()

    def _ensure_project_root_in_path(self):
        """从脚本路径向上查找项目根目录并加入 sys.path，
        使脚本中 from scripts/common/configs 等项目内部导入正常工作。
        打包环境下磁盘无项目目录，退而将脚本所在目录加入 sys.path。"""
        candidate = self.script_path.parent
        for _ in range(10):
            if any((candidate / m).is_dir() for m in self._PROJECT_MARKERS):
                path_str = str(candidate)
                if path_str not in sys.path:
                    sys.path.insert(0, path_str)
                    logger.info(f"已添加项目根目录到 sys.path: {path_str}")
                return
            parent = candidate.parent
            if parent == candidate:
                break
            candidate = parent

        script_dir = str(self.script_path.parent)
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
            logger.info(f"未找到项目根目录，已将脚本目录加入 sys.path: {script_dir}")

    def _load(self):
        if not self.script_path.exists():
            raise FileNotFoundError(f"脚本文件不存在: {self.script_path}")

        self._ensure_project_root_in_path()

        spec = importlib.util.spec_from_file_location(
            "user_script", str(self.script_path)
        )
        if spec is None or spec.loader is None:
            raise ImportError(f"无法加载脚本: {self.script_path}")

        self._module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self._module)

        if not hasattr(self._module, 'run'):
            raise AttributeError(
                f"脚本 {self.script_path} 中未找到 'async def run(bp)' 函数"
            )
        logger.info(f"加载脚本 '{self.name}' ({self.script_path})")

    async def run(
        self,
        timeout: float = 0,
        on_progress: Optional[Callable[[str], None]] = None,
        **kwargs,
    ) -> ScriptResult:
        """执行脚本。

        Args:
            timeout: 超时秒数，0 表示不限时。
            on_progress: 可选进度回调，接收描述字符串。
            **kwargs: 透传给脚本 run(bp, **kwargs)。
        Returns:
            ScriptResult 结构化执行结果。
        """
        if on_progress:
            on_progress(f"开始执行 '{self.name}'")
        logger.info(f"开始执行脚本 '{self.name}'")

        start_time = time.time()
        try:
            coro = self._module.run(self.bp, **kwargs)
            if timeout > 0:
                await asyncio.wait_for(coro, timeout=timeout)
            else:
                await coro

            elapsed = time.time() - start_time
            logger.info(f"脚本 '{self.name}' 执行完成，耗时 {elapsed:.1f}s")
            if on_progress:
                on_progress(f"执行完成，耗时 {elapsed:.1f}s")

            return ScriptResult(name=self.name, success=True, elapsed=elapsed)

        except asyncio.TimeoutError:
            elapsed = time.time() - start_time
            msg = f"脚本执行超时 ({timeout}s)"
            logger.error(msg)
            return ScriptResult(
                name=self.name, success=False, elapsed=elapsed,
                error_message=msg,
            )
        except asyncio.CancelledError:
            logger.warning(f"脚本 '{self.name}' 被取消")
            raise
        except Exception as e:
            elapsed = time.time() - start_time
            msg = f"脚本执行异常: {e}"
            logger.error(msg, exc_info=True)
            return ScriptResult(
                name=self.name, success=False, elapsed=elapsed,
                error_message=msg,
            )


async def run_script(base_page, script_path: str, **kwargs) -> ScriptResult:
    """便捷入口：创建 ScriptRunner 并执行。"""
    runner = ScriptRunner(base_page, script_path)
    return await runner.run(**kwargs)


if __name__ == '__main__':
    import argparse
    import datetime
    import traceback
    from common.log import setup_logging
    from common.ws_server import rpc_server
    from common.base_page import BasePage

    setup_logging()

    parser = argparse.ArgumentParser(description='Recording Script Runner')
    parser.add_argument('--script-path', type=str, required=True,
                        help='待执行的 .py 脚本路径（包含 async def run(bp) 函数）')
    parser.add_argument('--ws-port', type=int, default=5101,
                        help='WebSocket 端口（默认 5101）')
    parser.add_argument('--device-type', type=str, default='pc',
                        help='设备类型 pc/android/ios/harmony（默认 pc）')
    parser.add_argument('--device-id', type=str, default=None,
                        help='设备 ID（android/ios 用）')
    args = parser.parse_args()

    if not args.script_path:
        logger.error("未指定 --script-path 参数")
        sys.exit(1)

    @rpc_server(port=args.ws_port)
    async def start_test(server):
        logger.info(f"启动脚本测试: 端口={args.ws_port}, 脚本={args.script_path}")
        bp = BasePage(
            server=server,
            device_type=args.device_type,
            device_id=args.device_id,
        )
        await bp.initialize()
        try:
            result = await run_script(bp, args.script_path)
            if not result.success:
                logger.error(f"脚本执行失败: {result.error_message}")
        except Exception:
            logger.error(traceback.format_exc())
        finally:
            await bp.connect_close()
            logger.info(f"测试结束: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    start_test()
