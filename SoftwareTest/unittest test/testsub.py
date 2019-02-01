# coding=utf-8
from calculator import Count
import unittest


class TestAdd(unittest.TestCase):
    def setUp(slef):
        print 'test case start'

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(9, 3)
        self.assertEqual(j.sub(), 6)

    def tearDown(self):
        print 'test case end'


if __name__ == '__main__':
    unittest.main()
