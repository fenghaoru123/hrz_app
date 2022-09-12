#coding=utf8
'''
该模块读取Excel文件中的内容
'''
from public.utils.ReadExcel import ReadExcel
class Login_Date:
    @staticmethod
    def get_url():
        #获取测试的URL地址
        url=ReadExcel('Data.xlsx','Sheet1').read_excel(1,0)
        return url

    @staticmethod
    def get_username():
        #获取测试的用户名
        username=ReadExcel('Data.xlsx','Sheet1').read_excel(1,1)
        return int(username)

    @staticmethod
    def get_pwd():
        #获取测试的密码
        pwd=ReadExcel('Data.xlsx','Sheet1').read_excel(1,2)
        return pwd
if __name__ == '__main__':
    print (Login_Date.get_url())
    print (Login_Date.get_username())
    print (Login_Date.get_pwd())

