#!/usr/bin/python3
"""unittest for max_integer([..]) list
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unitests for 6-max_integer"""
    def test_ints_unorderd(self):
        """tests for integers only list"""
        list1 = [1, 2, 7, 3]
        self.assertEqual(max_integer(list1), 7)

    def test_repeat(self):
        """checks for max with repeated numbers"""
        list2 = [1, 2, 2]
        self.assertEqual(max_integer(list2), 2)

    def test_ordered(self):
        """checks for max in ordered list"""
        list3 = [1, 2, 3]
        self.assertEqual(max_integer(list3), 3)

    def test_empty(self):
        """check for empty list"""
        list4 = []
        self.assertEqual(max_integer(list4), None)

    def test_str(self):
        """check for string"""
        list5 = ["emma"]
        self.assertEqual(max_integer(list5), 'emma')

    def test_float(self):
        """check for float"""
        list6 = [1.0, 4.5, 3.7]
        self.assertEqual(max_integer(list6), 4.5)


if __name__ == '__main__':
    unittest.main()
