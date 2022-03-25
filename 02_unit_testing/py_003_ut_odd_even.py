from py_002_ut_odd_even import py_002_ut_odd_even
import unittest


class Test_Odd_Even(unittest.TestCase):
    def test_return_odd(self):
        self.assertEqual(py_002_ut_odd_even([1, 2, 3, 4, 5], 1), [1, 3, 5], "Should be [3,5]")

    def test_return_even(self):
        self.assertEqual(py_002_ut_odd_even([1, 2, 3, 4, 5], 0), [2, 4, 6], "Should be [2,4]")

    def test_return_odd_empty(self):
        self.assertEqual(py_002_ut_odd_even([2, 4, 6, 8], 1), [2], "Should be empty")

    def test_return_even_empty(self):
        self.assertEqual(py_002_ut_odd_even([3, 5, 7, 9], 0), [1], "Should be empty")


if __name__ == '__main__':
    unittest.main()
