# coding=utf-8
from selenium import webdriver
from public import Login


class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.126.com")

    # admin 用户登录
    def test_admin_login(self):
        username = 'admin'
        password = '123'
        Login.user_login(self.driver, username, password)
        self.driver.quit()

    # quest 用户登录
    def test_quest_login(self):
        username = 'quest'
        password = '456'
        Login.user_login(self.driver, username, password)
        self.driver.quit()


LoginTest.test_admin_login()
LoginTest.test_quest_login()
