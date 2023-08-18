#The idea is to write to good quality tests that cover most of your cases.

import unittest
import script2

class TestScript2(unittest.TestCase):
    def setUp(self):
        # being run before each test; useful in case a default or precondition needs to be setup before each test
        print('about to test a function')

    def test_input(self):
        'hiiii!'
        answer = 5
        guess = 5
        result = script2.check_random(answer, guess)
        self.assertTrue(result)

    def test_wrong_guess(self):
        'hiiii!'
        answer = 5
        guess = 0
        result = script2.check_random(answer, guess)
        self.assertFalse(result)

    def test_wrong_number(self):
        'hiiii!'
        answer = 5
        guess = 11
        result = script2.check_random(answer, guess)
        self.assertFalse(result)

    def test_wrong_input_string(self):
        'hiiii!'
        answer = 5
        guess = '11'
        result = script2.check_random(answer, guess)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

#
#C:\Users\GayCalaranan.000\PycharmProjects\pythonProject>python test_script2.py -v
#test_input (__main__.TestScript2)
#hiiii! ... about to test a function
#you are a genius!
#ok
#test_wrong_guess (__main__.TestScript2)
#hiiii! ... about to test a function
#ok
#test_wrong_input_string (__main__.TestScript2)
#hiiii! ... about to test a function
#ok
#test_wrong_number (__main__.TestScript2)
#hiiii! ... about to test a function
#ok

#----------------------------------------------------------------------
#Ran 4 tests in 0.012s
#
#OK
