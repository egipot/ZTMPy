#improve the function by breaking it

import unittest
import main

class TestMain(unittest.TestCase):

    def setUp(self): #being run before each test; useful in case a default or precondition needs to be setup before each test
        print('about to test a function')

    def test_do_stuff(self):
        'hiiii!'
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    def test_do_stuff2(self):
        test_param = 'asdfaf'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))
    def test_do_stuff3(self):
        test_param = 'asdfaf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')
    def test_do_stuff5(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')
    def test_do_stuff6(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')
    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__': #this line is added to ensure that this test is going to be run only if the main file is being run
    unittest.main()


#when self.assertEqual(result, 15) , the result is:
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.000s
#OK

#when self.assertEqual(result, 10) , the result is:
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py
#F
#======================================================================
#FAIL: test_do_stuff (__main__.TestMain)
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "C:\Users\GayCalaranan.000\PycharmProjects\pythonProject\test.py", line 9, in test_do_stuff
#    self.assertEqual(result,10)
#AssertionError: 15 != 10
#----------------------------------------------------------------------
#Ran 1 test in 0.001s
#FAILED (failures=1)


#with additional test_do_stuff2
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.001s
#OK
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>

#with test4
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py
#....
#----------------------------------------------------------------------
#Ran 4 tests in 0.002s
#OK

#with tests 5 and 6
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py
#......
#----------------------------------------------------------------------
#Ran 6 tests in 0.002s
#OK

# -v means verbose = more information per test case
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py -v
#test_do_stuff (__main__.TestMain) ... ok
#test_do_stuff2 (__main__.TestMain) ... ok
#test_do_stuff3 (__main__.TestMain) ... ok
#test_do_stuff4 (__main__.TestMain) ... ok
#test_do_stuff5 (__main__.TestMain) ... ok
#test_do_stuff6 (__main__.TestMain) ... ok
#----------------------------------------------------------------------
#Ran 6 tests in 0.037s
#OK

#adding a greeting text
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py -v
#test_do_stuff (__main__.TestMain)
#hiiii! ... ok
#test_do_stuff2 (__main__.TestMain) ... ok
#test_do_stuff3 (__main__.TestMain) ... ok
#test_do_stuff4 (__main__.TestMain) ... ok
#test_do_stuff5 (__main__.TestMain) ... ok
#test_do_stuff6 (__main__.TestMain) ... ok
#
#----------------------------------------------------------------------
#Ran 6 tests in 0.010s
#OK

#setUp
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py -v
#test_do_stuff (__main__.TestMain)
#hiiii! ... about to test a function
#ok
#test_do_stuff2 (__main__.TestMain) ... about to test a function
#ok
#test_do_stuff3 (__main__.TestMain) ... about to test a function
#ok
#test_do_stuff4 (__main__.TestMain) ... about to test a function
#ok
#test_do_stuff5 (__main__.TestMain) ... about to test a function
#ok
#test_do_stuff6 (__main__.TestMain) ... about to test a function
#ok
#
#----------------------------------------------------------------------
#Ran 6 tests in 0.021s
#OK

#tearDown
#
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test.py -v
#test_do_stuff (__main__.TestMain)
#hiiii! ... about to test a function
#cleaning up
#ok
#test_do_stuff2 (__main__.TestMain) ... about to test a function
#cleaning up
#ok
#test_do_stuff3 (__main__.TestMain) ... about to test a function
#cleaning up
#ok
#test_do_stuff4 (__main__.TestMain) ... about to test a function
#cleaning up
#ok
#test_do_stuff5 (__main__.TestMain) ... about to test a function
#cleaning up
#ok
#test_do_stuff6 (__main__.TestMain) ... about to test a function
#cleaning up
#ok
#
#----------------------------------------------------------------------
#Ran 6 tests in 0.031s
#OK