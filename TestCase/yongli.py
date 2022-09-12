#coding=utf8
import unittest
import time
from public.pages.BaseTestCase import BaseTestCase
from public.pages.page_element import Page_Elment as p

class yong(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        # BaseTestCase.sleep(3)
        print ('开始执行')

    @classmethod
    def tearDownClass(cls):
        BaseTestCase.sleep(3)
        print ('结束执行')
        # BaseTestCase.goto_home()

    def test001_yongli(self):
        try:
            m=BaseTestCase.find_element(p.shumaguan)
            BaseTestCase.click(m)
            text=BaseTestCase.get_text(p.shouji)
            self.assertEqual(text,u'手机')
        except Exception :
            print (Exception.message) #打印异常信息

