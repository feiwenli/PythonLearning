# coding=utf-8
from selenium import webdriver

class Login():

	# 登录
	def user_login(slef, driver, username, password):
		driver.find_element_by_id("idInput").clear()
		driver.find_element_by_id("idInput").send_keys(username)
		driver.find_element_by_id("pwdInput").clear()
		driver.find_element_by_id("pwdInput").send_keys(password)
		driver.find_element_by_id("loginBtn").click()

	# 退出
	def user_logout(self,driver):
		driver.find_element_by_id("退出").click()
		driver.quit()

