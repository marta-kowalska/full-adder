import unittest
import adder
import random
import sys


class BasicTestCase(unittest.TestCase):
    def test_zero_and_positive(self):
        a = 0
        b = 5
        actual_result = adder.add(a, b)
        self.assertEqual(actual_result, a + b)

    def test_positive_and_zero(self):
        a = 1234
        b = 0
        actual_result = adder.add(a, b)
        self.assertEqual(actual_result, a + b)

    def test_not_negatives(self):
        a = random.randint(0, sys.maxsize)
        b = random.randint(0, sys.maxsize)
        actual_result = adder.add(a, b)
        self.assertEqual(actual_result, a + b)
    
    def test_negative_and_positive(self):
        a = -5
        b = 54
        actual_result = adder.add(a, b)
        self.assertEqual(actual_result, a + b)


if __name__ == '__main__':
    unittest.main()