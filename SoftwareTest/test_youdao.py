# coding=utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.youdao.com"

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath('//*[@id="translateContent"]').clear()
        driver.find_element_by_xpath('//*[@id="translateContent"]').send_keys("webdriver")
        driver.find_element_by_xpath("/html/body/div[5]/div/form/button").click()
        time.sleep(2)
        result = EC.alert_is_present()(driver)
        if result:
            print result.text
        else:
            print 'alert is not present.'
        title = driver.title
        self.assertEqual(title, u"【webdriver】什么意思_英语webdriver的翻译_音标_读音_用法_例句_在线翻译_有道词典")

    def tearDown(self):
        self.driver.close()




if __name__ == "__main__":
    unittest.main()
