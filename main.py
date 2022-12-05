import unittest

class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b


class TestCalculator(unittest.TestCase):
    def test_add(self):
        '''Test case function for addition'''
        self.calc\
            =Calculator()
        result=self.calc.add(2,7)
        expected=9
        self.assertEqual(result,expected)
    def test_sub(self):
        '''Test case function for subtraction'''
        self.calc=Calculator()
        result=self.calc.sub(10,3)
        expected=7
        self.assertEqual(result,expected) @unittest.skip('some reason')

    def test_mul(self):
        '''Test case function for multiplication'''
        self.calc = Calculator()
        result = self.calc.mul(10, 3)
        expected = 30
        self.assertEqual(result, expected)

