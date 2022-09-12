#coding=utf8
import xlrd
from config.globalconfig import data_path #导入date数据的绝对路径
import os
class ReadExcel:
    def __init__(self,filename,sheetname):
        datapath=os.path.join(data_path,filename)  #读取Excel文件绝对路径的文件名
        self.workbook=xlrd.open_workbook(datapath) #读取Excel文档，生成对象
        self.sheetName=self.workbook.sheet_by_name(sheetname)

    def read_excel(self,rownum,colnum):
        '''
        封装读取Excel文档具体行与列的工具方法
        :param rownum:
        :param colnum:
        :return:
        '''
        value=self.sheetName.cell(rownum,colnum).value
        return value