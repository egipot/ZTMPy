
import unittest
import main

def do_stuff(num):
    return num + 5


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff