# coding=utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.set_window_size(800, 600)

driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()

# 通过js设置浏览器窗口的滚动条位置
js = "window.scrollTo(100, 450);"
driver.execute_script(js)
sleep(3)

# 截取当前窗口并保存到指定位置
driver.get_screenshot_as_file("E:/pyse/baidu_image.jpg")

driver.quit()

