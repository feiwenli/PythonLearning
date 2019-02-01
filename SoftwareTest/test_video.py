# coding=utf-8
# emm...not work
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.videojs.com/")

video = driver.find_element_by_xpath(".//*[@id='preview-player']/button")
# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print url

# 播放视频
print "start"
driver.execute_script("return arguments[0].play()", video)

sleep(15)

print "stop"
driver.execute_script("arguments[0].pause()", video)

sleep(3)
driver.quit()