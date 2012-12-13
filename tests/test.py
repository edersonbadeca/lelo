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


if __name__ == "__main__":

    unittest.main()
