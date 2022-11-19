#coding=utf-8
import os
from public.utils.ReadConfigIni import ReadConfigIni
#读取当前文件路径
file_path=os.path.split(os.path.realpath(__file__))[0]
# print file_path
#读取config.ini配置文件的对象
path=os.path.join(file_path,'config.ini')
# print (path)
read_config=ReadConfigIni(os.path.join(file_path,'config.ini'))
# print (read_config)
#获取项目的绝对路径
project_path=read_config.getconfigValue('project','project_path')
# print (project_path)
#date数据的路径
data_path=os.path.join(project_path,'Date','TestDate')
# print (data_path)
#report报告路径
report_path=os.path.join(project_path,'report','TestReport')
# print (report_path)
#用例路径
TestCase_path=os.path.join(project_path,'TestCase')
# print (TestCase_path)
#运行用例路径
Run_all_path=os.path.join(project_path,'Run_all')
# print (Run_all_path)