from common.log import get_logger
logger = get_logger("ws_server")
import asyncio
import json
import uuid
import websockets
from colorama import Fore, Style, init
from common import rpc_method_request
from configs.port_config import get_port, get_port_info
from collections import deque
init(autoreset=True)
COLOR_MAPPING = {
    'log': Style.RESET_ALL,
    'error': Fore.RED,
    'warn': Fore.YELLOW,
    'info': Fore.BLUE,
    'debug': Fore.CYAN
}


class RPCServer:
    def __init__(self, websocket):
        self.websocket = websocket
        self.pending_requests = {}
        self.listener_task = None
        self.msg_deque = deque()
        self._is_handle_msg = False
        self._msg_watchers: list[asyncio.Queue] = []
        self.recording_events = deque()
        self._is_recording = False
        self._on_record_event = None

    async def _response_listener(self):
        try:
            async for message in self.websocket:
                data = json.loads(message)
                if 'id' not in data:
                    continue
                if 'msg' in data:
                    msg = data.get('msg')
                    if isinstance(msg, dict) and msg.get('type') == 'record_event':
                        self.get_record_data(msg=msg)
                        continue
                    if not self._is_handle_msg:
                        continue
                    self.handle_msg(msg)
                    continue
                rid = data['id']
                future = self.pending_requests.pop(rid, None)
                if not future:
                    continue
                if 'error' in data:
                    future.set_exception(Exception(data['error'].get('message', 'RPC Error')))
                    continue
                future.set_result(data.get('result'))
        except Exception as e:
            for future in self.pending_requests.values():
                future.set_exception(e)
            self.pending_requests.clear()

    async def call(self, method, *args, **kwargs):
        rid = str(uuid.uuid4())
        future = asyncio.Future()
        self.pending_requests[rid] = future

        request = json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": args or kwargs,
            "id": rid
        })

        await self.websocket.send(request)
        return await future

    async def start(self):
        self.listener_task = asyncio.create_task(self._response_listener())

    async def close(self):
        if not self.listener_task:
            await self.websocket.close()
            return
        self.listener_task.cancel()
        try:
            await self.listener_task
        except asyncio.CancelledError:
            pass
        await self.websocket.close()

    # 处理CocosCreator的console输出
    # 目前是按照类型打印
    def handle_msg(self, msg):
        msg_type = msg.get('type', 'log')
        data = msg.get('data', '')

        color = COLOR_MAPPING.get(msg_type, Style.RESET_ALL)

        # 处理整个数据字符串
        try:
            # 尝试解析为JSON（例如传输的是对象或数组）
            parsed = json.loads(data)
            formatted = json.dumps(parsed, indent=2, ensure_ascii=False)
        except (json.JSONDecodeError, TypeError):
            # 否则直接使用原始字符串
            formatted = data
        self.msg_deque.append((msg_type, formatted))
        for wq in self._msg_watchers:
            try:
                wq.put_nowait((msg_type, formatted))
            except Exception:
                pass

    def create_msg_watcher(self) -> asyncio.Queue:
        wq = asyncio.Queue()
        self._msg_watchers.append(wq)
        return wq

    def remove_msg_watcher(self, wq: asyncio.Queue):
        try:
            self._msg_watchers.remove(wq)
        except ValueError:
            pass

    def handle_msg_start(self):
        self.msg_deque.clear()
        self._is_handle_msg = True

    def handle_msg_close(self):
        self.msg_deque.clear()
        self._is_handle_msg = False

    def recording_start(self):
        self.recording_events.clear()
        self._is_recording = True
        self._recording_needs_ts_reset = False

    def recording_stop(self):
        self._is_recording = False
        self._recording_needs_ts_reset = False

    def recording_undo(self):
        """撤销最后一个录制事件，并标记下一个事件需要重置计时。"""
        if not self._is_recording or not self.recording_events:
            return False
        self.recording_events.pop()
        self._recording_needs_ts_reset = True
        return True

    def get_recording_events(self):
        return list(self.recording_events)

    def get_record_data(self, msg):
        if not self._is_recording:
            return
        evt_data = msg.get('data')
        if self._recording_needs_ts_reset:
            last_ts = self.recording_events[-1].get('timestamp_ms', 0) if self.recording_events else 0
            evt_data['timestamp_ms'] = last_ts
            self._recording_needs_ts_reset = False
        self.recording_events.append(evt_data)
        if not self._on_record_event:
            return
        try:
            self._on_record_event(evt_data)
        except Exception:
            pass


def rpc_server(port=None, connect_timeout=60):
    """
    RPC服务器装饰器
    支持动态端口配置
    Args:
        port: 端口号，如果为None则使用配置的端口
    """
    def decorator(handler):
        async def wrapped_handler(websocket, stop_event, connected_event):
            # 如果服务器已经在停止过程中，直接关闭新连接
            if stop_event.is_set():
                await websocket.close()
                return
            if connected_event.is_set():
                await websocket.close()
                return
            # 标记已有客户端连接
            connected_event.set()

            server = RPCServer(websocket)
            await server.start()
            try:
                await handler(server)
            finally:
                await server.close()
                stop_event.set()  # 触发服务器停止事件

        def run_server():
            async def server_main():
                stop_event = asyncio.Event()
                connected_event = asyncio.Event()
                # 使用传入的端口或配置的端口
                actual_port = port if port is not None else get_port()
                
                # 显示端口配置信息
                logger.info(get_port_info())
                host = "0.0.0.0"
                async with websockets.serve(lambda ws: wrapped_handler(ws, stop_event, connected_event), host, actual_port):
                    logger.info(f"RPC Server running at ws://{host}:{actual_port}， 等待客户端连接，超时时间: {connect_timeout}秒...")
                    try:
                        # ✅ 等待客户端连接，超时则抛出异常
                        await asyncio.wait_for(
                            connected_event.wait(),
                            timeout=connect_timeout
                        )
                        logger.info("客户端已连接，开始处理...")
                        # 连接成功后继续等待任务完成
                        await stop_event.wait()

                    except asyncio.TimeoutError:
                        # ❌ 超时未连接，触发停止并抛出错误
                        stop_event.set()
                        raise TimeoutError(
                            f"等待客户端连接超时！已等待 {connect_timeout} 秒，"
                            f"请确认客户端是否正常启动并连接到 ws://{host}:{actual_port}"
                        )

            asyncio.run(server_main())

        return run_server

    return decorator


async def sleep(t):
    await asyncio.sleep(t)


@rpc_server(port=5102)
async def main(server):
    screen_size = await rpc_method_request.get_screen_size(server)
    logger.info(f"Screen size: {screen_size}")
    await sleep(10)



if __name__ == "__main__":
    main()
