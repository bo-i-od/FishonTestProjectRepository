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
        self.check_panels()

    def check_panels(self):
        if self.stop_event.is_set():
            return

        panel_id_list = self.bp.get_object_id_list(element_data=ElementsData.Panels_Default)
        if panel_id_list != self.panel_id_list_pre:
            self.panel_id_list_pre = panel_id_list
            self.cur = 0
        else:
            self.cur += 1

        if self.cur > 5:
            raise TimeoutException("Timeout!")

        self.schedule_next_check()

    def reset_monitoring(self):
        with self.lock:
            self.cur = 0
            self.panel_id_list_pre = []


    def _raise_exception_in_main_thread(self, e):
        thread_id = self.main_thread.ident
        exception = e
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id),
                                                         ctypes.py_object(exception))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            print("Failed to raise exception in main thread")

    def schedule_next_check(self):
        self.cancel_timer()
        self.timer = Timer(20, self.check_panels)
        self.timer.start()

    def cancel_timer(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

    def stop_monitoring(self):
        self.stop_event.set()
        self.cancel_timer()
        if self.monitor_thread:
            self.monitor_thread.join()
