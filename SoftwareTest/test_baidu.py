# encoding=utf-8
from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    """Baidu search test"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu01(self):
        """search unitest"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        print 'title:', title
        self.assertEqual(title, u"unittest_百度搜索")

    def test_baidu02(self):
        """search django"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("django")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        print 'title:', title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(MyTest("test_baidu01"))
    testunit.addTest(MyTest("test_baidu02"))

    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    filename = './' + now + 'result.html'
    print filename
    # 定义报告存放路径
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况')
    runner.run(testunit)  # 运行测试用例
    fp.close()
