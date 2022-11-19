#coding=utf8
from public.pages.BaseTestCase import BaseTestCase
import unittest
import time
from selenium import webdriver
from public.utils.Login_Date import Login_Date as login
from public.pages.page_element import Page_Elment as p

url=login.get_Url()
username=login.get_Username()
pwd=login.get_Pwd()
code=login.get_Code()

class Testlogin(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        driver=webdriver.Chrome()
        BaseTestCase.set_driver(driver)

    @classmethod
    def tearDownClass(cls):
        driver = BaseTestCase.get_driver()
        driver.quit()

    def testLogin(self):
        driver=BaseTestCase.get_driver()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(20)
        #输入账户名
        loginUserName=BaseTestCase.find_element(p.loginUserName)
        BaseTestCase.send_keys(loginUserName,username)
        #输入密码
        loginPwd=BaseTestCase.find_element(p.loginPwd)
        BaseTestCase.send_keys(loginPwd,pwd)
        #输入验证码
        loginCode = BaseTestCase.find_element(p.loginCode)
        BaseTestCase.send_keys(loginCode, code)
        #点击登录按钮
        loginBtn=BaseTestCase.find_element(p.loginBtn)
        BaseTestCase.click(loginBtn)
if __name__ == '__main__':
    unittest.main()