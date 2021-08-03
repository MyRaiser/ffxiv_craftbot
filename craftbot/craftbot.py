import threading
import logging
from numbers import Number
from typing import Callable, Any
from collections import deque
from functools import partial

from .utils import is_admin, delay, get_hwnd, press, press_hwnd


class Craftbot(threading.Thread):
    """
    Async script executor
    """
    def __init__(self, window_title: str, *, debug: bool = False):
        """
        :param window_title: title of window
        :param debug: if True, admin permission will not be checked
        """
        # admin permission is needed
        if debug or is_admin():
            self.hwnd = get_hwnd(window_title)
            if self.hwnd == 0:
                raise ValueError("hwnd is zero!")
        else:
            raise ValueError("No admin permission!")
        super().__init__()
        self.__running = threading.Event()
        self.__running.set()
        self.__idle = threading.Event()
        self.__idle.set()
        self.__deque = deque()

    def stop(self):
        self.__running.clear()

    @property
    def is_running(self):
        return self.__running.isSet()

    @property
    def is_idle(self):
        return self.__idle.isSet()

    def do(self, action: Callable[[], Any]):
        """
        prepare to do action, push into action queue
        """
        self.__idle.clear()
        self.__deque.append(action)

    def press(self, key: str):
        self.do(partial(press, key))

    def delay(self, ms: Number):
        self.do(partial(delay, ms))

    def press_hwnd(self, key: str):
        self.do(partial(press_hwnd, self.hwnd, key))

    def execute(self):
        """
        get a action from deque and execute it
        """
        try:
            action = self.__deque.popleft()
            print(f"Got action: {action}")
            action()
            if len(self.__deque) == 0:
                self.__idle.set()
        except IndexError:
            pass

    def run(self):
        while self.is_running:
            self.execute()
