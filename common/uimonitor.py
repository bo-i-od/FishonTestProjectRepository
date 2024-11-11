import threading
import ctypes
import time
from configs.elementsData import ElementsData


class TimeoutException(Exception):
    pass


class UIMonitor:
    def __init__(self, bp):
        self.bp = bp
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.main_thread = None
        self.monitor_thread = None

    def start_monitoring(self, main_thread):
        self.main_thread = main_thread
        self.monitor_thread = threading.Thread(target=self.main)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def main(self):
        try:
            self.monitor()
        except TimeoutException as e:
            self._raise_exception_in_main_thread(e)
        except Exception as e:
            print(e)

    def monitor(self):
        cur = 0
        panel_id_list_pre = []
        while True:
            time.sleep(10)
            panel_id_list = self.bp.get_object_id_list(element_data=ElementsData.Panels_Default)
            if panel_id_list != panel_id_list_pre:
                panel_id_list_pre = panel_id_list
                cur = 0
                continue
            cur += 1
            if cur > 15:
                raise TimeoutException("Timeout!")

    def _raise_exception_in_main_thread(self, e):
        thread_id = self.main_thread.ident
        exception = e
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id),
                                                         ctypes.py_object(exception))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            print("Failed to raise exception in main thread")

    def stop_monitoring(self):
        self.stop_event.set()
        if self.monitor_thread:
            self.monitor_thread.join()