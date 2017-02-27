import threading
import time

class TimeUtil:
    def __init__(self): pass

    @staticmethod
    def sec_to_ms(sec):
        return sec*1e-2

    @staticmethod
    def sec_to_us(sec):
        return sec*1e-6

    @staticmethod
    def current_time():
        return time.time()

    def wait_millisc(self, sec):
        time.sleep(self.sec_to_ms(sec))

    def wait_microsc(self, sec):
        time.sleep(self.sec_to_us(sec))

    def wait_seconds():
        time.sleep(sec)


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, target=None, name=None):
        super(StoppableThread, self).__init__(target=target, name=name)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
