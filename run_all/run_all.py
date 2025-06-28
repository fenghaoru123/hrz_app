#coding=utf-8
import time
import unittest

from config import globalconfig
from report.HTMLTestRunnerCN import HTMLTestRunner

report_path=globalconfig.report_path
now=time.strftime('%Y-%m-%d_%H_%M_%S')
filename=report_path +'\\' +str(now) +'_app_report.html'

def auto_run():
    suite=unittest.TestSuite()   #装载用例套件
    loader=unittest.TestLoader()   #用例加载器
    suite.addTest(loader.loadTestsFromName('TestCase.login.Testlogin.testLogin'))
    # suite.addTest(loader.loadTestsFromName('TestCase.yongli.yong.test001_yongli'))

    f=open(filename,'wb')
    runner=HTMLTestRunner(stream=f,title=u'Ui自动化报告',description='用例执行情况如下',tester=u'冯浩儒')
    runner.run(suite)
if __name__ == '__main__':
    auto_run()


#123