# coding=utf-8
import unittest, time
from HTMLTestRunner import HTMLTestRunner

# 指定测试用例为当前文件夹下的test_case目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':

	now = time.strftime("%Y-%m-%d %H_%M_%S")

	filename = './'+ now +'result.html'
	# 定义报告存放路径
	fp = open(filename, 'wb')
	# 定义测试报告
	runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
	runner.run(discover) # 运行测试用例
	fp.close()