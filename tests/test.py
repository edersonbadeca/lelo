# coding: utf-8
# Author: João S. O. Bueno


import sys, os
sys.path.insert(0, "..")

from lelo import paralell
import unittest

class Tests(unittest.TestCase):
    def test_can_import(self):
        self.assert_(__import__("lelo"))

    def test_can_execute_func_out_of_process(self):
        from multiprocessing import Queue, Process
        from lelo._lelo import _xecuter
        queue = Queue(1)

        def sum_(a, b):
            return a + b

        proc  = Process(target=_xecuter, 
            args=(queue, sum_, (2, 3), {}))
        proc.start()

        self.assertEqual(queue.get(), 5)

    def test_proc_wrapper_works(self):

        from lelo._lelo import Wrapper, LazyCallWrapper
        def sum_(a,b):
            return a + b

        wrapped = Wrapper(sum_)
        result = wrapped(2,3)
        self.assertEqual(type(result), LazyCallWrapper)
        self.assertEqual(result._value, 5)
        
    def test_lazy_class_factory(self):
        from lelo._lelo import MetaParalell
        X = MetaParalell("X", (object,), {})
        x = X()
        object.__setattr__(x, "_value", 10)
        self.assertEqual(x + 0, 10)
        object.__setattr__(x, "_value", {"y": 10})
        self.assertEqual(list(x.keys()), ["y"])

    def test_paralell_function_creation(self):
        from types import MethodType
        @paralell
        def soma(a, b):
            return a + b
        x = getattr(soma, "__call__")
        self.assert_(x.__class__, MethodType)

    def test_paralell_execution(self):
        @paralell
        def soma(a, b):
            return a + b
        result = soma(2,3)
        #print result.__repr__
        self.assertEqual(result, 5)

if __name__ == "__main__":

    unittest.main()
