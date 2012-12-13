# coding: utf-8
# Author: João S. O. Bueno

from multiprocessing import Process, Queue

def _xecuter(queue, func, args, kwargs):
    queue.put(func(*args, **kwargs))


class Wrapper(object):
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kw):
        self.queue = Queue(1)
        process = Process(target=_xecuter,
            args=(self.queue, self.func,
                  args, kw)
            )
        process.start()

    @property
    def _value(self):
        if not hasattr(self, "_real_value"):
            self._real_value = self.queue.get()
        return self._real_value

        

def paralell(func):
    """
    Make so that the function is called in a separate process, 
    using Python multiprocessing, and gets started imediatelly -
    in a non blocking way.
    The return value is a proxy object that will bridge to the real
    return value whenever it is used - it will block at time
    of use if it is not complete
    """
    pass
