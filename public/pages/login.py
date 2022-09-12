#coding=utf8
from public.pages.BaseTestCase import BaseTestCase
import unittest
import time
from selenium import webdriver
from public.utils.Login_Date import Login_Date as login
from public.pages.page_element import Page_Elment as p

url=login.get_url()
username=login.get_username()
pwd=login.get_pwd()

class Testlogin(BaseTestCase):

    @classmethod
        driver=webdriver.Chrome()
        BaseTestCase.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        BaseTestCase.sleep(3)
        BaseTestCase.goto_home()

    def testLogin(self):
        driver=BaseTestCase.get_driver()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        # BaseTestCase.wait(20)
        #定位登录窗口
        loginBtn=BaseTestCase.find_element(p.loginBtn)
        BaseTestCase.click(loginBtn)
        #输入账户名
        userName=BaseTestCase.find_element(p.userName)
        BaseTestCase.send_keys(userName,username)
        #输入密码
        passWord=BaseTestCase.find_element(p.passWord)
        BaseTestCase.send_keys(passWord,pwd)
        #点击登录按钮
        comeBtn=BaseTestCase.find_element(p.comeBtn)
        BaseTestCase.click(comeBtn)
        #断言
        text=BaseTestCase.get_text(p.loginOut)
        assert text==u'立即注册'
if __name__ == '__main__':
    unittest.main()