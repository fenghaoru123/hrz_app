#coding=utf8
#python中处理ini文件的的模块configparser
import configparser

class ReadConfigIni:
    #读取config.ini文件
    def __init__(self,filename):
        self.cf=configparser.ConfigParser()
        self.cf.read(filename)
    def getconfigValue(self,config,name):
        #读取section和option对应的value值
        value=self.cf.get(config,name)
        return value

