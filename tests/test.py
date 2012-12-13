# coding: utf-8
# Author: João S. O. Bueno


import sys, os
#lelo_path = os.pwd().rsplit("/", 2)[0] 
sys.path.insert(0, "..")
#print sys.path, __name__, locals().keys()
#del lelo_path

from lelo import paralell
import unittest

class Tests(unittest.TestCase):
    def test_running(self):
        assert True

if __name__ == "__main__":

    unittest.main()
