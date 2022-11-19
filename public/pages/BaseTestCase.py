#coding=utf8
import unittest
from selenium import webdriver
import time
from public.pages.page_element import Page_Elment as p

class BaseTestCase(unittest.TestCase):
    '''
    所有页面的公共方法封装在BaseTestCase这个基类当中
    '''
    @classmethod
    def set_driver(cls,driver):
        '''
        设置driver对象
        需要保证每个用例的执行都是同一个driver对象
        '''

        cls.driver=driver

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def find_element(cls,element):
        '''
        封装定位元素的工具方法id,name,class,xpath,css定位
        :param element:
        :return:
        '''
        type=element[0]
        value=element[1]
        try:
            if type=='id' or type=='Id' or type=='ID':
                elem=cls.driver.find_element_by_id(value)
            elif type=='name' or type=='Name' or type=='NAME':
                elem=cls.driver.find_element_by_name(value)
            elif type=='class' or type=='Class' or type=='CLASS':
                elem=cls.driver.find_element_by_class_name(value)
            elif type=='xpath' or type=='Xpath' or type=='XPATH':
                elem=cls.driver.find_element_by_xpath(value)
            elif type=='css' or type=='Css' or type=='CSS':
                elem=cls.driver.find_element_by_css_selector(value)
            elif type=='link' or type=='Link' or type=='LINK':
                elem=cls.driver.find_element_by_link_text(value)
            elif type=='partical_link' or type=='Partical_Link' or type=='PARTICAL_LINK':
                elem=cls.driver.find_element_by_partial_link_text('value')
            else:
                raise NameError('please input correct parameter!!')
        except Exception:
            raise NameError('this element not found+str(element)')
        return elem

    @classmethod
    def send_keys(cls,element,text):
        element.send_keys(text)

    @classmethod
    def click(cls,element):
        element.click()

    @classmethod
    def sleep(cls,sec):
        return time.sleep(sec)

    @classmethod
    def wait(cls,sec):
        return cls.driver.implicitly_wait()

    @classmethod
    def close(cls):
        return cls.driver.close()

    @classmethod
    def get_title(cls):
        title=cls.driver.title
        return title

    @classmethod
    def get_text(cls,locator):
        text=BaseTestCase.find_element(locator).text   #获取定位页面的文本进行断言
        return text



