# coding=utf-8
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbb'})
for cookie in driver.get_cookies():
	print "%s -> %s"  % (cookie['name'],cookie['value'])
driver.quit()

# 将用户名和密码写入浏览器cookie
# driver.add_cookie({'name':'Login_UserName','value':'username'})
# driver.add_cookie({'name':'Login_Passwd','value':'password'})
# 再次访问将会自动登录
