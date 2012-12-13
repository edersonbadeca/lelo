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


def value_retriever(name):
    def operator(self, *args, **kw):
        real_op = getattr(self._value, name)
        return real_op(*args, **kw)

class MetaParalell(type):
    def __new__(metacls, name, bases, dct):
        # FIXME: check the data_model
        # and other Python documentation -
        #  there are mssing dunder methods still
        special_methods = """
        __abs__ __add__ __and__ __class__ __cmp__ __coerce__
        __delattr__ __div__ __divmod__ __doc__ __float__
        __floordiv__ __format__ __getattribute__ __getnewargs__
        __hash__ __hex__ __index__ __init__ __int__ __invert__
        __long__ __lshift__ __mod__ __mul__ __neg__ __new__
        __nonzero__ __oct__ __or__ __pos__ __pow__ __radd__
        __rand__ __rdiv__ __rdivmod__ __reduce__ __reduce_ex__
        __repr__ __rfloordiv__ __rlshift__ __rmod__ __rmul__
        __ror__ __rpow__ __rrshift__ __rshift__ __rsub__
        __rtruediv__ __rxor__ __setattr__ __sizeof__
        __str__ __sub__ __subclasshook__ __truediv_
        __trunc__ __xor__ _contains__ __delitem__ __delslice__
        __eq__ __ge__ __getitem__ __getslice__ __gt__ __iadd__
        __imul__ __iter__ __le__ __len__ __lt__ __ne__ __reversed__
        __setitem__ __setslice__ __call__ __enter__ __exit__

        """
        for func_name in special_methods.split():
            dct[func_name] = value_retriever(name)
            dct[func_name].__name__ = name
        return type.__new__(metacls, name, bases, dct)

Paralell = MetaParalell("paralell", Wrapper, {})


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
