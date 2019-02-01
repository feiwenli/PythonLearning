# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


search_test = ['python', u'中文', 'text']

for text in search_test:
	driver = webdriver.Chrome()
	# driver.implicitly_wait(10)
	driver.get("http://www.baidu.com")
	element = WebDriverWait(driver, 5, 0.5).until(
		EC.presence_of_element_located((By.ID, 'kw'))
		)	# 判断元素是否在DOM树里，但并不一定可见
	element.send_keys(text)
	driver.find_element_by_id('su').click()
	driver.quit()
	
