import threading
import ctypes
import time

from configs.elementsData import ElementsData
from threading import Timer


class TimeoutException(Exception):
    pass


class UIMonitor:
    def __init__(self, bp):
        self.bp = bp
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.main_thread = None
        self.monitor_thread = None
        self.timer = None
        self.cur = 0
        self.panel_id_list_pre = []
        self.is_checking = False
        self.task_list = []
        self.task_map = {
            "monitor": self.monitor,
            "schedule_next_check": self.schedule_next_check,
            "check_panels": self.check_panels,
            "cancel_timer": self.cancel_timer,
            "stop_monitoring": self.stop_monitoring,
            "reset_monitoring": self.reset_monitoring,
            # 添加更多任务
        }

    def start_monitoring(self, main_thread):
        self.main_thread = main_thread
        self.add_task("check_panels")
        self.monitor_thread = threading.Thread(target=self.monitor)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def monitor(self):
        try:
            while True:
                with self.lock:
                    if len(self.task_list) < 1:
                        time.sleep(0.5)
                        continue
                    task, args, kwargs = self.task_list[-1]
                if task not in self.task_map:
                    time.sleep(0.1)
                    continue
                with self.lock:
                    self.task_list.clear()

                self.task_map[task](*args, **kwargs)
                time.sleep(0.1)
                continue
        except TimeoutException as e:
            self._raise_exception_in_main_thread(e)
        except Exception as e:
            print(e)
            self.stop_monitoring()

    def add_task(self, task, *args, **kwargs):
        with self.lock:
            self.task_list.append((task, args, kwargs))

    def check_panels(self):
        with self.lock:
            if self.is_checking:
                return
        if self.stop_event.is_set():
            return
        with self.lock:
            self.is_checking = True

        panel_id_list = self.bp.get_object_id_list(element_data=ElementsData.Panels_Default)

        with self.lock:
            self.is_checking = False

        if panel_id_list != self.panel_id_list_pre:
            self.panel_id_list_pre = panel_id_list
            self.cur = 0
        else:
            self.cur += 1
        if self.cur > 15:
            raise TimeoutException("Timeout!")

        self.schedule_next_check(self.cur)

    def reset_monitoring(self):
        self.stop_monitoring()
        self.start_monitoring(main_thread=self.main_thread)

    def _raise_exception_in_main_thread(self, e):
        thread_id = self.main_thread.ident
        exception = e
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id),
                                                         ctypes.py_object(exception))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            print("Failed to raise exception in main thread")

    def schedule_next_check(self, cur=0):

        if self.stop_event.is_set():
            return
        self.cancel_timer()
        self.cur = cur
        self.timer = Timer(15, self.add_task, args=["check_panels"])
        self.timer.start()

    def cancel_timer(self):
        if self.timer is None:
            return
        self.timer.cancel()
        self.timer = None

    def stop_monitoring(self):
        self.stop_event.set()
        self.cancel_timer()
        while True:
            with self.lock:
                if not self.is_checking:
                    break
            time.sleep(0.1)
        if self.monitor_thread:
            self.monitor_thread.join()
