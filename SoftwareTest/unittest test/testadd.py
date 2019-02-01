# coding=utf-8
from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print 'test case start'

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(9, 3)
        self.assertEqual(j.add(), 12)

    def tearDown(self):
        print 'test case end'


if __name__ == '__main__':
    unittest.main()
