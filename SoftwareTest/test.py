# coding=utf-8
from calculator import Count
import unittest

class MyTest(unittest.TestCase):

	def setUp(slef):
		print 'test case start'

	def tearDown(self):
		print 'test case end'

class TestAdd(MyTest):

	def test_add(self):
		j = Count(2, 3)
		self.assertEqual(j.add(), 5)

	def test_add2(self):
		j = Count(9, 3)
		self.assertEqual(j.add(), 12)


class TestSub(MyTest):

	def test_sub(self):
		j = Count(2, 3)
		self.assertEqual(j.sub(), -1)

	def test_sub2(self):
		j = Count(9, 3)
		self.assertEqual(j.sub(), 6)


def setUpModule():
	print "test module start >>>>>>>>>"

def rearDownModule():
	print 'test module end >>>>>>>>>>'

class Test(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print 'test case end ============>'

	@classmethod
	def tearDownClass(cls):
		print 'test case end ============>'

	def setUp(self):
		print 'test case start -->'

	def tearDown(self):
		print 'test case end -->'

	def test_case(self):
		print 'test case'

	def test_case2(self):
		print 'test case2'




if __name__ == '__main__':
	# # 构造测试集
	# suite = unittest.TestSuite()
	# suite.addTest(TestAdd("test_add"))
	# suite.addTest(TestAdd("test_add2"))
	# suite.addTest(TestSub("test_sub"))
	# suite.addTest(TestSub("test_sub2"))

	# # 执行测试
	# runner = unittest.TextTestRunner()
	# runner.run(suite)
	unittest.main()